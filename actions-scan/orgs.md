
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 444.48 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 148.16 mins              | 444.48 mins            |
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
| webp-sh/webp_server_go     | 108.63 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.38 mins                | 13.5 mins              |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 16.28 mins               | 65.12 mins             |
|                            |               | CodeQL                          | 2.14 mins                | 30.02 mins             |
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
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 117652.7 mins |                                     |                          |                        |
|                                     |               | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 84.32 mins               | 3035.63 mins           |
|                                     |               | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 68.45 mins               | 19509.48 mins          |
|                                     |               | Build Tool                          | 23.73 mins               | 47.45 mins             |
|                                     |               | Dev Linux                           | 26.97 mins               | 32419.27 mins          |
|                                     |               | Dev MacOS                           | 52.01 mins               | 62510.02 mins          |
|                                     |               | Build Sqllogic Test Image           | 3.74 mins                | 130.85 mins            |
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
| datafuselabs/openraft               | 1746.73 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 16.2 mins                | 16.2 mins              |
|                                     |               | ci                                  | 16.13 mins               | 1241.73 mins           |
|                                     |               | commit-message-check                | 3.08 mins                | 271.42 mins            |
|                                     |               | Unit test coverage                  | 10.17 mins               | 172.93 mins            |
|                                     |               | DevSkim                             | 0.79 mins                | 3.93 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.15 mins                | 4.8 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.23 mins                | 0.92 mins              |
|                                     |               | .github/workflows/pages.yaml        | 4.77 mins                | 19.08 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 4.38 mins                | 13.15 mins             |
|                                     |               | pages build and deployment          | 0.64 mins                | 2.57 mins              |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 5.43 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.38 mins                | 1.52 mins              |
|                                     |               | pages build and deployment          | 0.98 mins                | 3.92 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 27094.88 mins |                                     |                          |                        |
|                                     |               | CI                                  | 10.13 mins               | 3079.58 mins           |
|                                     |               | Docs                                | 5.01 mins                | 1188.52 mins           |
|                                     |               | Service Test Azblob                 | 6.33 mins                | 1929.43 mins           |
|                                     |               | Service Test Fs                     | 5.86 mins                | 1787.98 mins           |
|                                     |               | Service Test Ftp                    | 8.25 mins                | 1699.85 mins           |
|                                     |               | Service Test Gcs                    | 6.26 mins                | 1910.6 mins            |
|                                     |               | Service Test HDFS                   | 7.34 mins                | 2238.35 mins           |
|                                     |               | Service Test HTTP                   | 6.77 mins                | 2063.92 mins           |
|                                     |               | Service Test IPFS                   | 6.39 mins                | 3509.78 mins           |
|                                     |               | Service Test IPMFS                  | 6.41 mins                | 1686.45 mins           |
|                                     |               | Service Test Memory                 | 5.96 mins                | 1816.6 mins            |
|                                     |               | Service Test Obs                    | 6.36 mins                | 1939.15 mins           |
|                                     |               | Service Test S3                     | 7.36 mins                | 2244.67 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 323.42 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 10.78 mins               | 323.42 mins            |
| datafuselabs/databend-perf          | 1105.48 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 18.0 mins                | 863.93 mins            |
|                                     |               | pages build and deployment          | 0.63 mins                | 15.73 mins             |
|                                     |               | Reload tpch                         | 24.0 mins                | 95.98 mins             |
|                                     |               | Reload hits                         | 16.46 mins               | 82.32 mins             |
|                                     |               | Reload ontime                       | 15.84 mins               | 47.52 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 26.92 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 13.46 mins               | 26.92 mins             |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
