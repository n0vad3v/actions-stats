
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 216.63 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 108.32 mins              | 216.63 mins            |
| knatnetwork/github-runner-kms  | 0.0 mins      |                    |                          |                        |
|                                |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder | 0.0 mins      |                    |                          |                        |
|                                |               | Build Image        | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server  | 0.0 mins      |                    |                          |                        |
|                                |               | Build Image        | 0.0 mins                 | 0.0 mins               |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>webp-sh</b> <i>[click to show]</i></summary>
<div>

```
    
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                       | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node   | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go     | 88.5 mins     |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.38 mins                | 10.15 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 17.37 mins               | 52.12 mins             |
|                            |               | CodeQL                          | 2.19 mins                | 26.23 mins             |
| webp-sh/webp               | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java   | 0.0 mins      |                                 |                          |                        |
|                            |               | dev                             | 0.0 mins                 | 0.0 mins               |
|                            |               | release                         | 0.0 mins                 | 0.0 mins               |
| webp-sh/fiber              | 0.0 mins      |                                 |                          |                        |
| webp-sh/gowebp             | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif            | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh       | 0.0 mins      |                                 |                          |                        |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>datafuselabs</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 111046.52 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 85.75 mins               | 2915.53 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 66.96 mins               | 18280.02 mins          |
|                                     |                | Build Tool                          | 23.73 mins               | 47.45 mins             |
|                                     |                | Dev Linux                           | 27.04 mins               | 30668.13 mins          |
|                                     |                | Dev MacOS                           | 52.03 mins               | 58997.23 mins          |
|                                     |                | Build Sqllogic Test Image           | 3.73 mins                | 138.15 mins            |
|                                     |                | Unit Tests and Coverage             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless Cluster Tests             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test                                | 0.0 mins                 | 0.0 mins               |
|                                     |                | Binary Size Check                   | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful test(cluster)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Cluster              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Statful Standalone             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Unit                           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Build Debug                         | 0.0 mins                 | 0.0 mins               |
|                                     |                | Build Release                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Crowdin Action                      | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 1595.92 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 16.2 mins                | 16.2 mins              |
|                                     |                | ci                                  | 17.45 mins               | 1099.4 mins            |
|                                     |                | commit-message-check                | 3.98 mins                | 290.63 mins            |
|                                     |                | Unit test coverage                  | 10.71 mins               | 149.88 mins            |
|                                     |                | DevSkim                             | 0.79 mins                | 3.17 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.15 mins                | 4.93 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.23 mins                | 0.92 mins              |
|                                     |                | .github/workflows/pages.yaml        | 4.77 mins                | 19.08 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 9.13 mins                | 9.13 mins              |
|                                     |                | pages build and deployment          | 0.64 mins                | 2.57 mins              |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 5.43 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.38 mins                | 1.52 mins              |
|                                     |                | pages build and deployment          | 0.98 mins                | 3.92 mins              |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 30426.63 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 10.13 mins               | 3321.87 mins           |
|                                     |                | Docs                                | 5.19 mins                | 1443.4 mins            |
|                                     |                | Service Test Azblob                 | 6.53 mins                | 2147.67 mins           |
|                                     |                | Service Test Fs                     | 6.11 mins                | 2010.08 mins           |
|                                     |                | Service Test Ftp                    | 8.15 mins                | 2069.35 mins           |
|                                     |                | Service Test Gcs                    | 6.54 mins                | 2152.48 mins           |
|                                     |                | Service Test HDFS                   | 7.49 mins                | 2464.18 mins           |
|                                     |                | Service Test HTTP                   | 6.67 mins                | 2193.85 mins           |
|                                     |                | Service Test IPFS                   | 6.73 mins                | 3916.2 mins            |
|                                     |                | Service Test IPMFS                  | 6.4 mins                 | 1990.53 mins           |
|                                     |                | Service Test Memory                 | 6.13 mins                | 2016.25 mins           |
|                                     |                | Service Test Obs                    | 6.69 mins                | 2201.92 mins           |
|                                     |                | Service Test S3                     | 7.6 mins                 | 2498.85 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 321.4 mins     |                                     |                          |                        |
|                                     |                | CI                                  | 10.71 mins               | 321.4 mins             |
| datafuselabs/databend-perf          | 1087.37 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 21.67 mins               | 845.2 mins             |
|                                     |                | pages build and deployment          | 0.63 mins                | 16.35 mins             |
|                                     |                | Reload tpch                         | 24.0 mins                | 95.98 mins             |
|                                     |                | Reload hits                         | 16.46 mins               | 82.32 mins             |
|                                     |                | Reload ontime                       | 15.84 mins               | 47.52 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 26.92 mins     |                                     |                          |                        |
|                                     |                | CI                                  | 13.46 mins               | 26.92 mins             |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
