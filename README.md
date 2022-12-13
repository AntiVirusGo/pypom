# pypom

pypom is used to analyse Maven's pom.xml data format.

I'll compelete its functions in future.If u have some issues, plz commit them as issues so that i can see them and improve its function.Thks Really!

### Installation Procedure

Enter the dir with `setup.py`,then install it with command:`python setup.py install` to make it into ur python.

### Usage

My `pom_path` is a file Path of a pom.xml.Of course, U can transmit as the param of the function too.

```python
from pypom import pomparser

pom_path = r"C:\Users\ranja\.m2\repository\net\minidev\accessors-smart\1.2\accessors-smart-1.2.pom"

with open(pom_path, 'r') as f:
    content = f.read()
    f.close()

print(pomparser(content))
```

I used collections.defaultdict to save pom's data.

output:
```
defaultdict(<function pomparser.<locals>.<lambda> at 0x02ACEF18>, {'group_id': 'net.minidev', 'artifact_id': 'accessors-smart', 'version': '1.2', 'name': 'ASM based accessors helper used by json-smart
', 'description': 'Java reflect give poor performance on getter setter an constructor calls, accessors-smart use ASM to speed up those calls.\n    ', 'url': 'http://www.minidev.net/', 'organization':
'\n        ', 'licenses': ['The Apache Software License, Version 2.0'], 'dependencies': [defaultdict(<function pomparser.<locals>.<lambda> at 0x02B3F540>, {'group_id': 'junit', 'artifactId': 'junit',
'version': '4.12', 'scope': 'test'}), defaultdict(<function pomparser.<locals>.<lambda> at 0x02B3FED0>, {'group_id': 'org.ow2.asm', 'artifactId': 'asm', 'version': '5.0.4'})]})
```