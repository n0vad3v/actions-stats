
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 351.18 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 117.06 mins              | 351.18 mins            |
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
| webp-sh/webp_server_go     | 155.98 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.54 mins                | 28.33 mins             |
|                            |               | Release Binaries                | 2.68 mins                | 2.68 mins              |
|                            |               | Build and release docker images | 15.36 mins               | 92.15 mins             |
|                            |               | CodeQL                          | 1.93 mins                | 32.82 mins             |
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
| datafuselabs/databend               | 148347.95 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 107.28 mins              | 5149.35 mins           |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 86.81 mins               | 24394.88 mins          |
|                                     |                | Build Tool                          | 34.49 mins               | 172.45 mins            |
|                                     |                | Dev Linux                           | 21.65 mins               | 29253.48 mins          |
|                                     |                | Dev MacOS                           | 62.0 mins                | 83766.62 mins          |
|                                     |                | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Benchmark                           | 2.61 mins                | 4353.73 mins           |
|                                     |                | Benchmark (trusted)                 | 0.1 mins                 | 170.17 mins            |
|                                     |                | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |                | Typos Check                         | 1.44 mins                | 1082.98 mins           |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 10147.58 mins  |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 55.65 mins               | 8346.77 mins           |
|                                     |                | commit-message-check                | 7.01 mins                | 1192.28 mins           |
|                                     |                | Unit test coverage                  | 8.69 mins                | 365.18 mins            |
|                                     |                | DevSkim                             | 0.92 mins                | 3.67 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 2.32 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 5.0 mins                 | 55.05 mins             |
|                                     |                | .github/workflows/pages.yaml        | 3.77 mins                | 26.42 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 10.23 mins               | 51.17 mins             |
|                                     |                | pages build and deployment          | 14.96 mins               | 104.73 mins            |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 15.77 mins     |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.82 mins                | 3.28 mins              |
|                                     |                | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |                | pages build and deployment          | 1.35 mins                | 5.4 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 97418.82 mins  |                                     |                          |                        |
|                                     |                | Benchmark                           | 22.76 mins               | 2048.72 mins           |
|                                     |                | Binding NodeJS CI                   | 7.56 mins                | 1435.93 mins           |
|                                     |                | Bindings Python CI                  | 27.65 mins               | 12415.2 mins           |
|                                     |                | CI                                  | 18.35 mins               | 10219.0 mins           |
|                                     |                | Docs                                | 12.67 mins               | 2773.77 mins           |
|                                     |                | Publish                             | 23.73 mins               | 71.18 mins             |
|                                     |                | Service Test Azblob                 | 8.76 mins                | 2696.58 mins           |
|                                     |                | Service Test Azdfs                  | 9.84 mins                | 2999.88 mins           |
|                                     |                | Service Test Dashmap                | 7.44 mins                | 1392.02 mins           |
|                                     |                | Service Test Fs                     | 11.01 mins               | 3269.9 mins            |
|                                     |                | Service Test Ftp                    | 13.98 mins               | 4194.77 mins           |
|                                     |                | Service Test Gcs                    | 9.94 mins                | 2961.88 mins           |
|                                     |                | Service Test Ghac                   | 10.01 mins               | 2983.95 mins           |
|                                     |                | Service Test HDFS                   | 11.07 mins               | 3288.82 mins           |
|                                     |                | Service Test HDFS and WebHDFS       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test HTTP                   | 11.1 mins                | 3297.52 mins           |
|                                     |                | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test IPMFS                  | 9.58 mins                | 2855.52 mins           |
|                                     |                | Service Test Memcached              | 8.96 mins                | 2697.05 mins           |
|                                     |                | Service Test Memory                 | 8.52 mins                | 2530.57 mins           |
|                                     |                | Service Test Moka                   | 9.31 mins                | 2766.25 mins           |
|                                     |                | Service Test Obs                    | 11.6 mins                | 3456.7 mins            |
|                                     |                | Service Test Oss                    | 10.67 mins               | 3189.95 mins           |
|                                     |                | Service Test Redis                  | 9.14 mins                | 2715.6 mins            |
|                                     |                | Service Test RocksDB                | 15.07 mins               | 4565.0 mins            |
|                                     |                | Service Test S3                     | 11.7 mins                | 3508.8 mins            |
|                                     |                | Service Test Sled                   | 8.65 mins                | 2619.82 mins           |
|                                     |                | Service Test WebDAV                 | 17.45 mins               | 5460.72 mins           |
|                                     |                | Service Test WebHDFS                | 10.6 mins                | 3159.78 mins           |
|                                     |                | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 3.42 mins                | 1352.35 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 3.51 mins                | 491.6 mins             |
| datafuselabs/opensrv                | 755.08 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 17.98 mins               | 755.08 mins            |
| datafuselabs/databend-perf          | 1952.15 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 193.64 mins              | 1742.77 mins           |
|                                     |                | pages build and deployment          | 1.03 mins                | 5.15 mins              |
|                                     |                | Reload tpch                         | 16.59 mins               | 66.37 mins             |
|                                     |                | Reload hits                         | 26.56 mins               | 106.25 mins            |
|                                     |                | Reload ontime                       | 7.9 mins                 | 31.62 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 19.38 mins     |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.74 mins                | 8.17 mins              |
|                                     |                | pages build and deployment          | 1.02 mins                | 11.22 mins             |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 18.62 mins     |                                     |                          |                        |
|                                     |                | Rust                                | 2.07 mins                | 18.62 mins             |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
