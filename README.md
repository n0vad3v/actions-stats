# Action Stats

Wonder what repo are using your quota? This silly script can quickly give you a view on which repo is using a lot of GitHub Actions minutes.

![](./images/actions-quota.png)

## Usage

Download and install dependencies:

```
wget https://raw.githubusercontent.com/n0vad3v/action-stats/master/action-stats.py
wget https://raw.githubusercontent.com/n0vad3v/action-stats/master/requirements.txt
pip3 install -r requirements.txt
```

Get last 30 days of usage for org:

```
python3 action-stats.py '<Org_name>' 'ghp_Txxxxxxxxxxxxxxxxxx2F' 30
```

## Example output

![](./images/actions-output.png)
