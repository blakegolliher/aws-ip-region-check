from ipaddress import ip_network, ip_address
import socket
import json
import sys

# inspiration
# https://thameera.com/awsip/

# region data generated here (https://github.com/jsonmaur/aws-regions)
# https://raw.githubusercontent.com/jsonmaur/aws-regions/master/regions.json

# aws ip information generated here (https://github.com/joetek/aws-ip-ranges-json)
# https://github.com/joetek/aws-ip-ranges-json/blob/master/ip-ranges-amazon.json

ip = sys.argv[1]

def is_valid_v4_addr(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(ip)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True

def find_aws_reg_code(ip):
  ip_json = json.load(open('aws-ip-ranges-json/ip-ranges-amazon.json'))
  prefixes = ip_json['prefixes']
  my_ip = ip_address(ip)
  region = 'Unknown'
  for prefix in prefixes:
    if my_ip in ip_network(prefix['ip_prefix']):
      region = prefix['region']
      break
  return region

def find_aws_co_code():
  objects = json.load(open('aws-co-ranges.json'))
  for item in objects:
    region = find_aws_reg_code(ip)
    if region in item.values():
      data = {}
      data['ip'] = ip
      data['country'] = item['full_name']
      data['region'] = region
      return(json.dumps(data))
    else:
      pass

valid = is_valid_v4_addr(ip)
# print(valid)
if is_valid_v4_addr(ip):
    data = json.loads(find_aws_co_code())
    # print("{}".format(find_aws_co_code()))
    print("The ip {} is in {}, located out of {}".format(data['ip'],data['region'].upper(),data['country']))
else:
    print(f"Check that ip {ip} is valid (it didn't pass)")
    pass
