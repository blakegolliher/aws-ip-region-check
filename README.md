# aws-ip-region-check
It's a quick check if the ip is valid, then check if the ip exists in the aws published ip list, finally checks what zones are in that region, and prints all of that out. It's useful for knowing where the IP you are connecting to is located.

bgolliher@notbsd:~/ipcheck$ python3 aws-ip-region-check.py 52.19.10.227
The ip 52.19.10.227 is in eu-west-1, located out of EU (Ireland).
bgolliher@notbsd:~/ipcheck$
