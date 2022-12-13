# encoding=utf-8

from collections import defaultdict
import xml.etree.ElementTree as ET

def pomparser(pomData:str):
    pom_xml_data = defaultdict(lambda: None)
    root = ET.fromstring(pomData)

    for child in root:
        # 注意，child.tag是如下的这种，并不是直接的groupId
        # {http://maven.apache.org/POM/4.0.0}groupId
        if 'parent' in child.tag:
            for child_parent in child:
                if 'groupId' in child_parent.tag:
                    pom_xml_data['parent_group_id'] = child_parent.text
                if 'artifactId' in child_parent.tag:
                    pom_xml_data['parent_artifactId'] = child_parent.text
                if 'version' in child_parent.tag:
                    pom_xml_data['parent_version'] = child_parent.text
        if 'groupId' in child.tag:
            pom_xml_data['group_id'] = child.text
        if "artifactId" in child.tag:
            pom_xml_data['artifact_id'] = child.text
        if 'version' in child.tag:
            pom_xml_data['version'] = child.text
        if 'name' in child.tag:
            pom_xml_data['name'] = child.text
        if 'description' in child.tag:
            pom_xml_data['description'] = child.text
        if 'url' in child.tag:
            pom_xml_data['url'] = child.text
        if 'organization' in child.tag:
            pom_xml_data['organization'] = child.text
        if "dependencies" in child.tag:
            pom_xml_data['dependencies'] = []
            for child_dependency in child:
                pom_xml_dependency = defaultdict(lambda: None)
                for part_dependency in child_dependency:
                    if "groupId" in part_dependency.tag:
                        pom_xml_dependency['group_id'] = part_dependency.text
                    if "artifactId" in part_dependency.tag:
                        pom_xml_dependency['artifactId'] = part_dependency.text
                    if "version" in part_dependency.tag:
                        pom_xml_dependency['version'] = part_dependency.text
                    if "scope" in part_dependency.tag:
                        pom_xml_dependency['scope'] = part_dependency.text
                    if "optional" in part_dependency.tag:
                        if "true" == part_dependency.text:
                            pom_xml_dependency['optional'] = 1
                pom_xml_data['dependencies'].append(pom_xml_dependency)
        if 'licenses' in child.tag:
            pom_xml_data['licenses'] = []
            for child_license in child:
                pom_xml_license = defaultdict(lambda: None)
                for part_license in child_license:
                    if "name" in part_license.tag:
                        pom_xml_data['licenses'].append(part_license.text)

    # 处理下<parent>标签的传递
    if pom_xml_data['group_id'] == None and pom_xml_data['parent_group_id'] != None:
        # 上面两行代码主要处理的是类似于 https://mirrors.huaweicloud.com/repository/maven/org/MyBatis/MyBatis/3.1.1/MyBatis-3.1.1.pom 的问题
        # 没有GroupId，但是有parent标签，其中的GroupId存在
        pom_xml_data['group_id'] = pom_xml_data['parent_group_id']
    if pom_xml_data['artifact_id'] == None and pom_xml_data['parent_artifactId'] != None:
        pom_xml_data['artifact_id'] = pom_xml_data['parent_artifactId']
    if pom_xml_data['version'] == None and pom_xml_data['parent_version'] != None:
        pom_xml_data['version'] = pom_xml_data['parent_version']

    if pom_xml_data['group_id'] != None and pom_xml_data['artifact_id'] != None and pom_xml_data['version'] != None:
        return pom_xml_data
    else:
        raise Exception("Not exists one of [group_id, artifact_id, version]")