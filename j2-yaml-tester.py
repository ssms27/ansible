#!/usr/bin/python3.6
import yaml
import jinja2

### Test Rendering Yaml
with open('test.yaml') as f:
    result = yaml.load(f)
    # print('Printing overall results and type:')
    # print(result)
    type(result)
    print('Printing the Product list')
    print(result['product'][0]['description'])
