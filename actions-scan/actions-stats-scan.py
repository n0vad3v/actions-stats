import requests
import sys
import datetime
from terminaltables import AsciiTable

def get_header(gh_token):
    return {'Authorization': 'token {}'.format(gh_token)}

def get_all_repo_full_names(owner,gh_token):
    url = 'https://api.github.com/orgs/{}/repos?per_page=100'.format(owner)
    response = requests.get(url,headers=get_header(gh_token))
    all_repo_full_names = []
    for repo in response.json():
        all_repo_full_names.append(repo['full_name'])
    return all_repo_full_names

def get_workflow_ids(full_repo_name,gh_token):
    url = 'https://api.github.com/repos/{}/actions/workflows?per_page=100'.format(full_repo_name)
    response = requests.get(url,headers=get_header(gh_token))
    workflow_ids = []
    for workflow in response.json()['workflows']:
        workflow_ids.append(workflow['id'])
    
    return workflow_ids

def get_workflow_runs(full_repo_name,workflow_id,gh_token,date_period):
    url = 'https://api.github.com/repos/{}/actions/workflows/{}/runs?per_page=1'.format(full_repo_name,workflow_id)
    response = requests.get(url,headers=get_header(gh_token))
    all_workflow_runs = []

    workflow_total_count = response.json()['total_count']

    try:
        workflow_name = response.json()['workflow_runs'][0]['name']
    except:
        workflow_name = 'No workflow name(why?)'

    total_pages = int(workflow_total_count/100) + 1
    for page in range(1,total_pages+1):
        url = 'https://api.github.com/repos/{}/actions/workflows/{}/runs?per_page=100&page={}'.format(full_repo_name,workflow_id,page)
        response = requests.get(url,headers=get_header(gh_token))
        try:
            # Check if workflow created_at has already meet the date period requirements, in this case, we could just skip
            datetime_before_today = datetime.datetime.now() - datetime.timedelta(days=int(date_period))
            if response.json()['workflow_runs'][0]['created_at'] < datetime_before_today.strftime('%Y-%m-%dT%H:%M:%SZ'):
                break
            all_workflow_runs.extend(response.json()['workflow_runs'])
        except:
            print('Error: {}'.format(response.json()))
            break

    # Filter by date
    datetime_before_today = datetime.datetime.now() - datetime.timedelta(days=int(date_period))
    all_workflow_runs = [workflow_run for workflow_run in all_workflow_runs if workflow_run['created_at'] > datetime_before_today.isoformat()]
    if len(all_workflow_runs) == 0:
        return 0,0,workflow_name

    # Calculate time taken for each workflow run
    for workflow_run in all_workflow_runs:
        workflow_created_at = datetime.datetime.strptime(workflow_run['run_started_at'], '%Y-%m-%dT%H:%M:%SZ')
        workflow_completed_at = datetime.datetime.strptime(workflow_run['updated_at'], '%Y-%m-%dT%H:%M:%SZ')

        workflow_run['time_taken'] = (workflow_completed_at - workflow_created_at).total_seconds()
    
    average_workflow_run_time = sum(workflow_run['time_taken'] for workflow_run in all_workflow_runs) / len(all_workflow_runs)
    total_workflow_run_time = sum(workflow_run['time_taken'] for workflow_run in all_workflow_runs)

    return average_workflow_run_time,total_workflow_run_time,workflow_name

if __name__ == '__main__':
    owner = sys.argv[1]
    gh_token = sys.argv[2]
    date_period = sys.argv[3]

    start_msg = """
<details><summary><b>{}</b> <i>[click to show]</i></summary>
<div>

```
    """.format(owner)

    print(start_msg)

    repo_list = get_all_repo_full_names(owner,gh_token)

    total_ret = {}

    for repo in repo_list:
        repo_workflow_ids = get_workflow_ids(repo,gh_token)
        repo_total_run_time = 0
        for workflow_id in repo_workflow_ids:
            average_workflow_run_time,total_workflow_run_time,workflow_name = get_workflow_runs(repo,workflow_id,gh_token,date_period)
            if repo not in total_ret:
                total_ret[repo] = {}
                total_ret[repo]['per_workflow'] = {}
            total_ret[repo]['per_workflow'][workflow_name] = {'total_runtime': '{} mins'.format(round(total_workflow_run_time/60,2)),'average_runtime': '{} mins'.format(round(average_workflow_run_time/60,2))}
            repo_total_run_time += total_workflow_run_time
        # Sum up all workflows total runtime
        try:
            total_ret[repo]['total_runtime'] = '{} mins'.format(round(repo_total_run_time/60,2))
        except KeyError:
            total_ret[repo] = {'total_runtime': '{} mins'.format(round(repo_total_run_time/60,2))}

    table_data = []
    table_data.append(['Repo','Total Runtime','Workflow Name', 'Workflow Average Runtime','Workflow Total Runtime'])
    for repo in total_ret:
        table_data.append([repo,total_ret[repo]['total_runtime']])
        if 'per_workflow' in total_ret[repo]:
            for workflow in total_ret[repo]['per_workflow']:
                table_data.append(['','',workflow,total_ret[repo]['per_workflow'][workflow]['average_runtime'],total_ret[repo]['per_workflow'][workflow]['total_runtime']])
    
    ret_table = AsciiTable(table_data)
    print(ret_table.table)
    
    end_msg = """
```
</div>
</details>
***
    """
    print(end_msg)