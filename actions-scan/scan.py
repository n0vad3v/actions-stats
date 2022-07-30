import yaml
import sys
import os

with open('./orgs.yml') as f:
    orgs = yaml.load(f, Loader=yaml.FullLoader)

org_list = []
for item,doc in orgs.items():
    org_list = doc

token = sys.argv[1]
# Call actions-stats.py for each org
for org in org_list:
    cmd = "python3 actions-stats-scan.py {} {} 30".format(org,token)
    os.system(cmd)