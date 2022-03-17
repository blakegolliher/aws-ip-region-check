## Table of Contents
- [aws-ip-region-check](#aws-ip-region-check)
- [Example](#example)
- [Inspiration](#Inspiration)
- [Data Needed](#Data-Needed)

# aws-ip-region-check
It's a quick check if the ip is valid, then check if the ip exists in the aws published ip list, finally checks what zones are in that region, and prints all of that out. It's useful for knowing where the IP you are connecting to is located.

## Example
```
bgolliher@notbsd:~/ipcheck$ aws-ip-region-check.py 52.19.10.227
The ip 52.19.10.227 is in eu-west-1, located out of EU (Ireland).
bgolliher@notbsd:~/ipcheck$
```

# Inspiration
https://thameera.com/awsip/

# Data Needed
- region data generated here 
  - https://github.com/jsonmaur/aws-regions
  - https://raw.githubusercontent.com/jsonmaur/aws-regions/master/regions.json
- aws ip information generated here (https://github.com/joetek/aws-ip-ranges-json
  - https://github.com/joetek/aws-ip-ranges-json/blob/master/ip-ranges-amazon.json
