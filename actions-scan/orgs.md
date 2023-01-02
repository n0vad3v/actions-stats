
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+-----------------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name               | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+-----------------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                             |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                             |                          |                        |
| knatnetwork/github-runner      | 177.4 mins    |                             |                          |                        |
|                                |               | Build Runner Image          | 59.13 mins               | 177.4 mins             |
| knatnetwork/github-runner-kms  | 0.0 mins      |                             |                          |                        |
|                                |               | Build Image                 | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder | 0.0 mins      |                             |                          |                        |
|                                |               | Build Image                 | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server  | 0.0 mins      |                             |                          |                        |
|                                |               | Build Image                 | 0.0 mins                 | 0.0 mins               |
| knatnetwork/zlib-searcher      | 0.0 mins      |                             |                          |                        |
|                                |               | Build/release docker images | 0.0 mins                 | 0.0 mins               |
+--------------------------------+---------------+-----------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>webp-sh</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                       | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node   | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go     | 98.95 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.55 mins                | 24.83 mins             |
|                            |               | Release Binaries                | 3.08 mins                | 6.17 mins              |
|                            |               | Build and release docker images | 8.42 mins                | 42.08 mins             |
|                            |               | CodeQL                          | 1.85 mins                | 25.87 mins             |
| webp-sh/webp               | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java   | 0.0 mins      |                                 |                          |                        |
|                            |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
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
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 96629.77 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 104.29 mins              | 3545.8 mins            |
|                                     |               | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 83.74 mins               | 16413.07 mins          |
|                                     |               | Build Tool                          | 31.16 mins               | 124.63 mins            |
|                                     |               | Dev Linux                           | 23.36 mins               | 21120.43 mins          |
|                                     |               | Dev MacOS                           | 61.31 mins               | 55425.83 mins          |
|                                     |               | Unit Tests and Coverage             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless Cluster Tests             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test                                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Binary Size Check                   | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful test(cluster)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Cluster              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Statful Standalone             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Unit                           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Build Debug                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | Build Release                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 3541.73 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 36.85 mins               | 3243.07 mins           |
|                                     |               | commit-message-check                | 1.44 mins                | 116.33 mins            |
|                                     |               | Unit test coverage                  | 8.67 mins                | 173.38 mins            |
|                                     |               | DevSkim                             | 0.77 mins                | 3.08 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.05 mins                | 1.27 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.25 mins                | 1.25 mins              |
|                                     |               | .github/workflows/pages.yaml        | 0.23 mins                | 0.23 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 3.12 mins                | 3.12 mins              |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 5.77 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.35 mins                | 2.08 mins              |
|                                     |               | pages build and deployment          | 0.61 mins                | 3.68 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 26247.83 mins |                                     |                          |                        |
|                                     |               | CI                                  | 21.63 mins               | 2444.43 mins           |
|                                     |               | Service Test S3                     | 16.2 mins                | 1846.77 mins           |
|                                     |               | Service Test Fs                     | 10.24 mins               | 1166.85 mins           |
|                                     |               | Docs                                | 19.5 mins                | 2125.47 mins           |
|                                     |               | Service Test Memory                 | 10.59 mins               | 1207.63 mins           |
|                                     |               | Service Test Azblob                 | 10.99 mins               | 1252.42 mins           |
|                                     |               | Service Test HDFS                   | 11.73 mins               | 1337.43 mins           |
|                                     |               | Service Test HTTP                   | 11.35 mins               | 1294.47 mins           |
|                                     |               | Service Test Gcs                    | 12.26 mins               | 1398.03 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                    | 13.6 mins                | 1550.0 mins            |
|                                     |               | Service Test IPMFS                  | 10.39 mins               | 1184.42 mins           |
|                                     |               | Service Test Ftp                    | 16.28 mins               | 1856.35 mins           |
|                                     |               | Service Test Redis                  | 11.42 mins               | 1301.5 mins            |
|                                     |               | Service Test Oss                    | 13.54 mins               | 1544.12 mins           |
|                                     |               | Service Test Moka                   | 11.07 mins               | 1261.85 mins           |
|                                     |               | Service Test RocksDB                | 17.68 mins               | 2015.97 mins           |
|                                     |               | Service Test Azdfs                  | 11.89 mins               | 1355.95 mins           |
|                                     |               | Service Test Ghac                   | 4.96 mins                | 94.25 mins             |
|                                     |               | A Test                              | 1.66 mins                | 9.93 mins              |
|                                     |               | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 381.73 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 11.57 mins               | 381.73 mins            |
| datafuselabs/databend-perf          | 1337.78 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 54.83 mins               | 1261.02 mins           |
|                                     |               | pages build and deployment          | 0.63 mins                | 11.92 mins             |
|                                     |               | Reload tpch                         | 2.95 mins                | 17.72 mins             |
|                                     |               | Reload hits                         | 4.8 mins                 | 28.8 mins              |
|                                     |               | Reload ontime                       | 4.58 mins                | 18.33 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

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

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
