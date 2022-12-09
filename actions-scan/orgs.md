
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+-----------------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name               | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+-----------------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                             |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                             |                          |                        |
| knatnetwork/github-runner      | 450.03 mins   |                             |                          |                        |
|                                |               | Build Runner Image          | 225.02 mins              | 450.03 mins            |
| knatnetwork/github-runner-kms  | 0.0 mins      |                             |                          |                        |
|                                |               | Build Image                 | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder | 0.0 mins      |                             |                          |                        |
|                                |               | Build Image                 | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server  | 0.0 mins      |                             |                          |                        |
|                                |               | Build Image                 | 0.0 mins                 | 0.0 mins               |
| knatnetwork/zlib-searcher      | 88.13 mins    |                             |                          |                        |
|                                |               | Build/release docker images | 11.02 mins               | 88.13 mins             |
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
| webp-sh/webp_server_go     | 146.3 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.49 mins                | 24.43 mins             |
|                            |               | Release Binaries                | 3.02 mins                | 3.02 mins              |
|                            |               | Build and release docker images | 18.04 mins               | 90.2 mins              |
|                            |               | CodeQL                          | 1.91 mins                | 28.65 mins             |
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
| datafuselabs/databend               | 99507.45 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 96.1 mins                | 4228.57 mins           |
|                                     |               | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 92.27 mins               | 20391.02 mins          |
|                                     |               | Build Tool                          | 27.6 mins                | 220.77 mins            |
|                                     |               | Crowdin Action                      | 3.22 mins                | 402.97 mins            |
|                                     |               | Dev Linux                           | 20.08 mins               | 19078.15 mins          |
|                                     |               | Dev MacOS                           | 58.03 mins               | 55125.55 mins          |
|                                     |               | Build Sqllogic Test Image           | 1.34 mins                | 60.43 mins             |
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
| datafuselabs/openraft               | 2287.18 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 35.82 mins               | 2149.22 mins           |
|                                     |               | commit-message-check                | 1.21 mins                | 55.83 mins             |
|                                     |               | Unit test coverage                  | 9.4 mins                 | 75.23 mins             |
|                                     |               | DevSkim                             | 0.84 mins                | 3.35 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 2.7 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.21 mins                | 0.85 mins              |
|                                     |               | .github/workflows/pages.yaml        | 0.0 mins                 | 0.0 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 5.72 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.32 mins                | 1.92 mins              |
|                                     |               | pages build and deployment          | 0.63 mins                | 3.8 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 48218.38 mins |                                     |                          |                        |
|                                     |               | CI                                  | 22.49 mins               | 5038.35 mins           |
|                                     |               | Service Test S3                     | 14.06 mins               | 3162.43 mins           |
|                                     |               | Service Test Fs                     | 10.51 mins               | 2365.75 mins           |
|                                     |               | Docs                                | 17.2 mins                | 3766.87 mins           |
|                                     |               | Service Test Memory                 | 10.09 mins               | 2269.95 mins           |
|                                     |               | Service Test Azblob                 | 10.41 mins               | 2342.72 mins           |
|                                     |               | Service Test HDFS                   | 12.08 mins               | 2718.33 mins           |
|                                     |               | Service Test HTTP                   | 10.4 mins                | 2339.03 mins           |
|                                     |               | Service Test Gcs                    | 11.59 mins               | 2608.38 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                    | 13.8 mins                | 3105.93 mins           |
|                                     |               | Service Test IPMFS                  | 10.22 mins               | 2300.03 mins           |
|                                     |               | Service Test Ftp                    | 13.55 mins               | 3048.27 mins           |
|                                     |               | Service Test Redis                  | 11.02 mins               | 2479.67 mins           |
|                                     |               | Service Test Oss                    | 13.44 mins               | 3024.68 mins           |
|                                     |               | Service Test Moka                   | 10.36 mins               | 2330.43 mins           |
|                                     |               | Service Test RocksDB                | 17.77 mins               | 3997.43 mins           |
|                                     |               | Service Test Azdfs                  | 14.04 mins               | 982.48 mins            |
|                                     |               | Service Test IPFS                   | 22.51 mins               | 337.63 mins            |
| datafuselabs/opensrv                | 626.52 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 9.21 mins                | 626.52 mins            |
| datafuselabs/databend-perf          | 1812.07 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 51.88 mins               | 1556.3 mins            |
|                                     |               | pages build and deployment          | 0.7 mins                 | 15.4 mins              |
|                                     |               | Reload tpch                         | 13.96 mins               | 69.82 mins             |
|                                     |               | Reload hits                         | 20.7 mins                | 103.52 mins            |
|                                     |               | Reload ontime                       | 13.41 mins               | 67.03 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 5.38 mins     |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.38 mins                | 2.67 mins              |
|                                     |               | pages build and deployment          | 0.91 mins                | 2.72 mins              |
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

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
