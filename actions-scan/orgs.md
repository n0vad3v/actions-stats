
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 0.0 mins      |                    |                          |                        |
|                                |               | Build Runner Image | 0.0 mins                 | 0.0 mins               |
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
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                       | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node   | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go     | 96.17 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.38 mins                | 13.5 mins              |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.85 mins               | 55.42 mins             |
|                            |               | CodeQL                          | 2.1 mins                 | 27.25 mins             |
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
Error: {'total_count': 100, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 214357.1 mins |                                     |                          |                        |
|                                     |               | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 109.7 mins               | 4717.03 mins           |
|                                     |               | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 104.95 mins              | 33269.27 mins          |
|                                     |               | Build Tool                          | 28.57 mins               | 114.28 mins            |
|                                     |               | Dev Linux                           | 34.76 mins               | 46579.3 mins           |
|                                     |               | Dev MacOS                           | 96.64 mins               | 129493.5 mins          |
|                                     |               | Build Sqllogic Test Image           | 3.11 mins                | 183.72 mins            |
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
|                                     |               | Crowdin Action                      | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 2473.97 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 20.43 mins               | 1695.45 mins           |
|                                     |               | commit-message-check                | 6.79 mins                | 577.38 mins            |
|                                     |               | Unit test coverage                  | 10.86 mins               | 173.73 mins            |
|                                     |               | DevSkim                             | 0.82 mins                | 3.27 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 2.33 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.2 mins                 | 1.4 mins               |
|                                     |               | .github/workflows/pages.yaml        | 0.39 mins                | 0.78 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 9.81 mins                | 19.62 mins             |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 4.7 mins      |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.36 mins                | 1.82 mins              |
|                                     |               | pages build and deployment          | 0.58 mins                | 2.88 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 60368.37 mins |                                     |                          |                        |
|                                     |               | CI                                  | 14.81 mins               | 2058.8 mins            |
|                                     |               | Docs                                | 7.85 mins                | 926.43 mins            |
|                                     |               | Service Test Azblob                 | 9.39 mins                | 1304.7 mins            |
|                                     |               | Service Test Fs                     | 8.85 mins                | 1230.35 mins           |
|                                     |               | Service Test Ftp                    | 11.57 mins               | 1608.73 mins           |
|                                     |               | Service Test Gcs                    | 9.68 mins                | 1345.33 mins           |
|                                     |               | Service Test HDFS                   | 10.36 mins               | 1439.58 mins           |
|                                     |               | Service Test HTTP                   | 8.92 mins                | 1240.33 mins           |
|                                     |               | Service Test IPFS                   | 131.55 mins              | 18285.53 mins          |
|                                     |               | Service Test IPMFS                  | 9.44 mins                | 1311.53 mins           |
|                                     |               | Service Test Memory                 | 9.16 mins                | 1272.77 mins           |
|                                     |               | Service Test Moka                   | 8.7 mins                 | 966.12 mins            |
|                                     |               | Service Test Obs                    | 11.36 mins               | 1578.52 mins           |
|                                     |               | Service Test Oss                    | 138.84 mins              | 19298.52 mins          |
|                                     |               | Service Test Redis                  | 9.8 mins                 | 1361.87 mins           |
|                                     |               | Service Test RocksDB                | 14.0 mins                | 167.98 mins            |
|                                     |               | Service Test S3                     | 35.76 mins               | 4971.27 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 460.05 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 15.34 mins               | 460.05 mins            |
| datafuselabs/databend-perf          | 1513.98 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 31.16 mins               | 1121.67 mins           |
|                                     |               | pages build and deployment          | 0.63 mins                | 12.05 mins             |
|                                     |               | Reload tpch                         | 17.4 mins                | 174.03 mins            |
|                                     |               | Reload hits                         | 14.97 mins               | 149.72 mins            |
|                                     |               | Reload ontime                       | 14.13 mins               | 56.52 mins             |
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
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
