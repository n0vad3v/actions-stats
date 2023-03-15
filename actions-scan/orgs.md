
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
| webp-sh/webp_server_go     | 163.7 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.5 mins                 | 31.5 mins              |
|                            |               | CodeQL                          | 1.97 mins                | 37.37 mins             |
|                            |               | Release Binaries                | 2.68 mins                | 2.68 mins              |
|                            |               | Build and release docker images | 15.36 mins               | 92.15 mins             |
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
| datafuselabs/databend               | 159809.1 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 112.46 mins              | 5510.45 mins           |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 88.16 mins               | 25477.43 mins          |
|                                     |               | Build Tool                          | 34.49 mins               | 172.45 mins            |
|                                     |               | Dev Linux                           | 22.63 mins               | 31973.83 mins          |
|                                     |               | Dev MacOS                           | 64.04 mins               | 90483.45 mins          |
|                                     |               | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Benchmark                           | 2.52 mins                | 4452.38 mins           |
|                                     |               | Benchmark (trusted)                 | 0.16 mins                | 276.33 mins            |
|                                     |               | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |               | Typos Check                         | 1.68 mins                | 1458.48 mins           |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 10162.63 mins |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 57.46 mins               | 8389.15 mins           |
|                                     |               | commit-message-check                | 7.0 mins                 | 1133.4 mins            |
|                                     |               | Unit test coverage                  | 8.83 mins                | 379.8 mins             |
|                                     |               | DevSkim                             | 0.92 mins                | 3.67 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.07 mins                | 2.42 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 5.0 mins                 | 55.05 mins             |
|                                     |               | .github/workflows/pages.yaml        | 3.43 mins                | 27.45 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 10.23 mins               | 51.17 mins             |
|                                     |               | pages build and deployment          | 15.07 mins               | 120.53 mins            |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 14.9 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.98 mins                | 2.95 mins              |
|                                     |               | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |               | pages build and deployment          | 1.62 mins                | 4.87 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 98163.17 mins |                                     |                          |                        |
|                                     |               | Benchmark                           | 22.76 mins               | 2048.72 mins           |
|                                     |               | Binding NodeJS CI                   | 7.92 mins                | 1663.0 mins            |
|                                     |               | Bindings Python CI                  | 27.21 mins               | 12298.87 mins          |
|                                     |               | CI                                  | 18.48 mins               | 10567.85 mins          |
|                                     |               | Docs                                | 11.93 mins               | 3005.4 mins            |
|                                     |               | Publish                             | 23.73 mins               | 71.18 mins             |
|                                     |               | Service Test Azblob                 | 8.65 mins                | 2698.37 mins           |
|                                     |               | Service Test Azdfs                  | 9.76 mins                | 3014.95 mins           |
|                                     |               | Service Test Dashmap                | 7.15 mins                | 1509.27 mins           |
|                                     |               | Service Test Fs                     | 10.79 mins               | 3248.73 mins           |
|                                     |               | Service Test Ftp                    | 13.69 mins               | 4161.73 mins           |
|                                     |               | Service Test Gcs                    | 9.82 mins                | 2964.25 mins           |
|                                     |               | Service Test Ghac                   | 9.81 mins                | 2961.87 mins           |
|                                     |               | Service Test HDFS                   | 10.88 mins               | 3273.62 mins           |
|                                     |               | Service Test HDFS and WebHDFS       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test HTTP                   | 10.9 mins                | 3281.18 mins           |
|                                     |               | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test IPMFS                  | 9.54 mins                | 2880.03 mins           |
|                                     |               | Service Test Memcached              | 8.83 mins                | 2691.85 mins           |
|                                     |               | Service Test Memory                 | 8.43 mins                | 2537.88 mins           |
|                                     |               | Service Test Moka                   | 9.22 mins                | 2775.28 mins           |
|                                     |               | Service Test Obs                    | 11.48 mins               | 3465.72 mins           |
|                                     |               | Service Test Oss                    | 10.33 mins               | 3130.35 mins           |
|                                     |               | Service Test Redis                  | 8.95 mins                | 2692.7 mins            |
|                                     |               | Service Test RocksDB                | 14.11 mins               | 4387.82 mins           |
|                                     |               | Service Test S3                     | 11.49 mins               | 3480.95 mins           |
|                                     |               | Service Test Sled                   | 8.44 mins                | 2581.42 mins           |
|                                     |               | Service Test WebDAV                 | 17.49 mins               | 5526.78 mins           |
|                                     |               | Service Test WebHDFS                | 10.47 mins               | 3150.12 mins           |
|                                     |               | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 3.59 mins                | 1570.6 mins            |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 3.68 mins                | 522.68 mins            |
| datafuselabs/opensrv                | 767.8 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 18.28 mins               | 767.8 mins             |
| datafuselabs/databend-perf          | 1921.82 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 190.32 mins              | 1712.92 mins           |
|                                     |               | pages build and deployment          | 1.17 mins                | 4.67 mins              |
|                                     |               | Reload tpch                         | 16.59 mins               | 66.37 mins             |
|                                     |               | Reload hits                         | 26.56 mins               | 106.25 mins            |
|                                     |               | Reload ontime                       | 7.9 mins                 | 31.62 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 19.38 mins    |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.74 mins                | 8.17 mins              |
|                                     |               | pages build and deployment          | 1.02 mins                | 11.22 mins             |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 18.62 mins    |                                     |                          |                        |
|                                     |               | Rust                                | 2.07 mins                | 18.62 mins             |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 3052.62 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 12.57 mins               | 12.57 mins             |
|                                    |               | BR & Lightning                                       | 1.14 mins                | 791.97 mins            |
|                                    |               | Dumpling                                             | 9.37 mins                | 1733.48 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.89 mins                | 514.38 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 178.05 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.24 mins                | 178.05 mins            |
| pingcap/kvproto                    | 1345.37 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.19 mins                | 557.43 mins            |
|                                    |               | Golang Test                                          | 1.76 mins                | 158.1 mins             |
|                                    |               | Rust Test                                            | 7.0 mins                 | 629.83 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5685.42 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.52 mins                | 4.7 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 83.72 mins             |
|                                    |               | external-link-check                                  | 2.93 mins                | 17.58 mins             |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 89.0 mins              |
|                                    |               | ci                                                   | 3.75 mins                | 4514.72 mins           |
|                                    |               | Links                                                | 2.82 mins                | 11.27 mins             |
|                                    |               | bot                                                  | 0.79 mins                | 17.47 mins             |
|                                    |               | cron                                                 | 1.3 mins                 | 39.03 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.43 mins                | 470.2 mins             |
|                                    |               | Prevent Deletion                                     | 0.36 mins                | 437.73 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5933.77 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.43 mins                | 6.47 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 74.48 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 26.1 mins              |
|                                    |               | ci                                                   | 3.98 mins                | 4904.12 mins           |
|                                    |               | Links                                                | 1.76 mins                | 7.03 mins              |
|                                    |               | Flush All PDF                                        | 0.26 mins                | 8.72 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.41 mins                | 473.95 mins            |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 432.35 mins            |
|                                    |               | Flush PDF by Version                                 | 0.28 mins                | 0.55 mins              |
| pingcap/tidb-binlog                | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
|                                    |               | Merge Schedule                                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | links                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                                      |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                                      |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog-cn                    | 0.47 mins     |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn             | 0.47 mins                | 0.47 mins              |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark                    | 4042.88 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.49 mins               | 930.82 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.32 mins                | 643.37 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 17.8 mins                | 1299.37 mins           |
|                                    |               | Follower Read test                                   | 9.74 mins                | 672.12 mins            |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.83 mins              |
|                                    |               | License checker                                      | 1.13 mins                | 78.18 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 5.97 mins                | 412.2 mins             |
| pingcap/octopus                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/grpc                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | PR AutoFix                                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/jepsen                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins      |                                                      |                          |                        |
| pingcap/chaos                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/meetup                     | 0.0 mins      |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins      |                                                      |                          |                        |
| pingcap/campaign                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/community                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-vision                | 0.0 mins      |                                                      |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins      |                                                      |                          |                        |
| pingcap/tla-plus                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-ycsb                    | 33.68 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.64 mins                | 18.45 mins             |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.18 mins                | 15.23 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 10434.25 mins |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 1066.49 mins             | 2132.98 mins           |
|                                    |               | chaos                                                | 21.07 mins               | 4172.47 mins           |
|                                    |               | ci                                                   | 18.0 mins                | 4121.27 mins           |
|                                    |               | Close stale issues/prs                               | 0.25 mins                | 7.53 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5015.27 mins  |                                                      |                          |                        |
|                                    |               | Pull Request CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins      |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins      |                                                      |                          |                        |
| pingcap/dm                         | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Test binlog 999999                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade via TiUP                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream database switch                             | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins      |                                                      |                          |                        |
| pingcap/log                        | 1.67 mins     |                                                      |                          |                        |
|                                    |               | Audit License                                        | 0.54 mins                | 1.08 mins              |
|                                    |               | Unit Test                                            | 0.29 mins                | 0.58 mins              |
| pingcap/tiflash                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/capnproto                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/boost-extra                | 0.0 mins      |                                                      |                          |                        |
| pingcap/kdt                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/failpoint                  | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                                      |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/diag                       | 121.88 mins   |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.18 mins               | 89.45 mins             |
|                                    |               | static-tests                                         | 3.24 mins                | 32.43 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 54309.27 mins |                                                      |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.27 mins                | 184.28 mins            |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 0.74 mins                | 2.22 mins              |
|                                    |               | Dataflow Engine Chaos                                | 30.92 mins               | 6493.27 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                                     | 14.06 mins               | 2952.88 mins           |
|                                    |               | DM Chaos                                             | 27.95 mins               | 5869.73 mins           |
|                                    |               | DM Web UI Lint                                       | 1.51 mins                | 4.52 mins              |
|                                    |               | Upstream Database Switch                             | 15.1 mins                | 3170.1 mins            |
|                                    |               | Design Docs Lint                                     | 0.53 mins                | 26.02 mins             |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Integration Tests                                | 17.84 mins               | 15931.87 mins          |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                                  | 5.36 mins                | 1124.63 mins           |
| pingcap/br                         | 21.37 mins    |                                                      |                          |                        |
|                                    |               | build                                                | 8.47 mins                | 16.95 mins             |
|                                    |               | compatibility-test                                   | 2.21 mins                | 4.42 mins              |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 1.1 mins      |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.1 mins                 | 1.1 mins               |
| pingcap/kops                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/sysutil                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Test                                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins      |                                                      |                          |                        |
|                                    |               | (experimental) Ember CLI tests (core)                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Linting                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Tests                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse-chat-integration | 0.0 mins      |                                                      |                          |                        |
| pingcap/discourse_docker           | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-helper                | 0.0 mins      |                                                      |                          |                        |
| pingcap/dumpling                   | 8.17 mins     |                                                      |                          |                        |
|                                    |               | Go                                                   | 8.17 mins                | 8.17 mins              |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
