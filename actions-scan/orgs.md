
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
| datafuselabs/databend               | 110649.75 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 84.65 mins               | 2878.03 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 67.4 mins                | 18399.37 mins          |
|                                     |                | Build Tool                          | 23.73 mins               | 47.45 mins             |
|                                     |                | Dev Linux                           | 27.05 mins               | 30486.32 mins          |
|                                     |                | Dev MacOS                           | 52.09 mins               | 58704.72 mins          |
|                                     |                | Build Sqllogic Test Image           | 3.72 mins                | 133.87 mins            |
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
| datafuselabs/openraft               | 1548.23 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 16.2 mins                | 16.2 mins              |
|                                     |                | ci                                  | 17.49 mins               | 1067.1 mins            |
|                                     |                | commit-message-check                | 3.67 mins                | 267.78 mins            |
|                                     |                | Unit test coverage                  | 10.5 mins                | 157.47 mins            |
|                                     |                | DevSkim                             | 0.79 mins                | 3.17 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.15 mins                | 4.82 mins              |
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
| datafuselabs/opendal                | 30397.38 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 10.12 mins               | 3330.33 mins           |
|                                     |                | Docs                                | 5.24 mins                | 1419.6 mins            |
|                                     |                | Service Test Azblob                 | 6.5 mins                 | 2144.68 mins           |
|                                     |                | Service Test Fs                     | 6.09 mins                | 2010.9 mins            |
|                                     |                | Service Test Ftp                    | 8.16 mins                | 2048.35 mins           |
|                                     |                | Service Test Gcs                    | 6.52 mins                | 2150.97 mins           |
|                                     |                | Service Test HDFS                   | 7.46 mins                | 2463.42 mins           |
|                                     |                | Service Test HTTP                   | 6.7 mins                 | 2209.65 mins           |
|                                     |                | Service Test IPFS                   | 6.73 mins                | 3924.45 mins           |
|                                     |                | Service Test IPMFS                  | 6.41 mins                | 1973.72 mins           |
|                                     |                | Service Test Memory                 | 6.12 mins                | 2021.23 mins           |
|                                     |                | Service Test Obs                    | 6.68 mins                | 2203.75 mins           |
|                                     |                | Service Test S3                     | 7.56 mins                | 2496.33 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 320.15 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 10.67 mins               | 320.15 mins            |
| datafuselabs/databend-perf          | 1083.78 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 21.58 mins               | 841.58 mins            |
|                                     |                | pages build and deployment          | 0.63 mins                | 16.38 mins             |
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
Error: {'total_count': 100, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
