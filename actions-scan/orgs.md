
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
| webp-sh/webp_server_go     | 116.65 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.33 mins                | 9.98 mins              |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 28.78 mins               | 86.33 mins             |
|                            |               | CodeQL                          | 2.03 mins                | 20.33 mins             |
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
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 100174.08 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 95.52 mins               | 4202.92 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 89.42 mins               | 19940.58 mins          |
|                                     |                | Build Tool                          | 28.01 mins               | 252.13 mins            |
|                                     |                | Crowdin Action                      | 3.31 mins                | 294.88 mins            |
|                                     |                | Dev Linux                           | 20.74 mins               | 19995.92 mins          |
|                                     |                | Dev MacOS                           | 57.5 mins                | 55426.88 mins          |
|                                     |                | Build Sqllogic Test Image           | 1.35 mins                | 60.77 mins             |
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
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 1323.88 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 18.66 mins               | 1156.68 mins           |
|                                     |                | commit-message-check                | 1.64 mins                | 82.08 mins             |
|                                     |                | Unit test coverage                  | 8.62 mins                | 77.62 mins             |
|                                     |                | DevSkim                             | 0.84 mins                | 3.35 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 3.3 mins               |
|                                     |                | .github/workflows/issue-welcome.yml | 0.21 mins                | 0.85 mins              |
|                                     |                | .github/workflows/pages.yaml        | 0.0 mins                 | 0.0 mins               |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 4.58 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.31 mins                | 1.53 mins              |
|                                     |                | pages build and deployment          | 0.61 mins                | 3.05 mins              |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 47644.28 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 22.28 mins               | 4991.6 mins            |
|                                     |                | Service Test S3                     | 13.8 mins                | 3106.07 mins           |
|                                     |                | Service Test Fs                     | 10.45 mins               | 2351.05 mins           |
|                                     |                | Docs                                | 16.82 mins               | 3599.83 mins           |
|                                     |                | Service Test Memory                 | 9.84 mins                | 2214.42 mins           |
|                                     |                | Service Test Azblob                 | 10.18 mins               | 2291.45 mins           |
|                                     |                | Service Test HDFS                   | 11.91 mins               | 2679.88 mins           |
|                                     |                | Service Test HTTP                   | 10.22 mins               | 2298.8 mins            |
|                                     |                | Service Test Gcs                    | 11.22 mins               | 2525.28 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Obs                    | 13.58 mins               | 3055.15 mins           |
|                                     |                | Service Test IPMFS                  | 10.16 mins               | 2285.52 mins           |
|                                     |                | Service Test Ftp                    | 13.42 mins               | 3019.5 mins            |
|                                     |                | Service Test Redis                  | 10.71 mins               | 2409.42 mins           |
|                                     |                | Service Test Oss                    | 13.34 mins               | 3000.45 mins           |
|                                     |                | Service Test Moka                   | 10.24 mins               | 2303.78 mins           |
|                                     |                | Service Test RocksDB                | 17.44 mins               | 3872.78 mins           |
|                                     |                | Service Test Azdfs                  | 14.73 mins               | 810.32 mins            |
|                                     |                | Service Test IPFS                   | 27.63 mins               | 828.98 mins            |
| datafuselabs/opensrv                | 627.9 mins     |                                     |                          |                        |
|                                     |                | CI                                  | 9.23 mins                | 627.9 mins             |
| datafuselabs/databend-perf          | 1894.88 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 54.45 mins               | 1633.37 mins           |
|                                     |                | pages build and deployment          | 0.77 mins                | 16.08 mins             |
|                                     |                | Reload tpch                         | 16.08 mins               | 96.5 mins              |
|                                     |                | Reload hits                         | 15.99 mins               | 95.93 mins             |
|                                     |                | Reload ontime                       | 13.25 mins               | 53.0 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 5.38 mins      |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.38 mins                | 2.67 mins              |
|                                     |                | pages build and deployment          | 0.91 mins                | 2.72 mins              |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

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
