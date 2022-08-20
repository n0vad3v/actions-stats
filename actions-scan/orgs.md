
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 166.83 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 166.83 mins              | 166.83 mins            |
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
| webp-sh/webp_server_go     | 185.77 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.16 mins                | 34.78 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.25 mins               | 105.97 mins            |
|                            |               | CodeQL                          | 1.96 mins                | 45.02 mins             |
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
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 103489.95 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 89.87 mins               | 3594.67 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 71.63 mins               | 15831.22 mins          |
|                                     |                | Build Tool                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Dev Linux                           | 21.89 mins               | 23792.12 mins          |
|                                     |                | Dev MacOS                           | 54.91 mins               | 59688.08 mins          |
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
|                                     |                | Crowdin Action                      | 3.01 mins                | 583.87 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 2960.25 mins   |                                     |                          |                        |
|                                     |                | ci                                  | 15.89 mins               | 2654.32 mins           |
|                                     |                | commit-message-check                | 1.31 mins                | 278.2 mins             |
|                                     |                | DevSkim                             | 0.77 mins                | 3.87 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 5.22 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.32 mins                | 5.73 mins              |
|                                     |                | .github/workflows/pages.yaml        | 0.35 mins                | 1.38 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 1.79 mins                | 8.93 mins              |
|                                     |                | pages build and deployment          | 0.65 mins                | 2.6 mins               |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 4.08 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.4 mins                 | 1.62 mins              |
|                                     |                | pages build and deployment          | 0.62 mins                | 2.47 mins              |
| datafuselabs/databend-playground    | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 15922.65 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 25.25 mins               | 4291.7 mins            |
|                                     |                | Docs                                | 4.75 mins                | 674.23 mins            |
|                                     |                | Add issues into projects            | 0.48 mins                | 12.87 mins             |
|                                     |                | Service Test Azblob                 | 6.05 mins                | 1028.03 mins           |
|                                     |                | Service Test Fs                     | 17.34 mins               | 2948.03 mins           |
|                                     |                | Service Test Gcs                    | 5.86 mins                | 199.1 mins             |
|                                     |                | Service Test HDFS                   | 6.87 mins                | 1167.97 mins           |
|                                     |                | Service Test HTTP                   | 20.78 mins               | 3532.62 mins           |
|                                     |                | Service Test Memory                 | 5.49 mins                | 933.0 mins             |
|                                     |                | Service Test S3                     | 6.63 mins                | 1127.85 mins           |
|                                     |                | Test Vault                          | 2.42 mins                | 7.25 mins              |
| datafuselabs/opensrv                | 394.67 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 9.63 mins                | 394.67 mins            |
| datafuselabs/databend-perf          | 720.82 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 17.68 mins               | 601.17 mins            |
|                                     |                | Reload                              | 6.75 mins                | 108.02 mins            |
|                                     |                | pages build and deployment          | 0.65 mins                | 11.63 mins             |
| datafuselabs/helm-charts            | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/parquet2               | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 44.0 mins      |                                     |                          |                        |
|                                     |                | CI                                  | 10.68 mins               | 42.73 mins             |
|                                     |                | .github/workflows/pages.yml         | 0.3 mins                 | 0.6 mins               |
|                                     |                | pages build and deployment          | 0.67 mins                | 0.67 mins              |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'message': 'Server Error'}

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
