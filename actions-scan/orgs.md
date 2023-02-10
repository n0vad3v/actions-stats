
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 231.65 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 16.55 mins               | 231.65 mins            |
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
| webp-sh/webp_server_go     | 210.35 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.24 mins                | 35.63 mins             |
|                            |               | Release Binaries                | 2.85 mins                | 5.7 mins               |
|                            |               | Build and release docker images | 15.81 mins               | 126.52 mins            |
|                            |               | CodeQL                          | 2.02 mins                | 42.5 mins              |
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
| datafuselabs/databend               | 83674.3 mins  |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 91.24 mins               | 3284.55 mins           |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 91.11 mins               | 18676.95 mins          |
|                                     |               | Build Tool                          | 31.42 mins               | 31.42 mins             |
|                                     |               | Dev Linux                           | 18.69 mins               | 17588.13 mins          |
|                                     |               | Dev MacOS                           | 46.34 mins               | 43608.12 mins          |
|                                     |               | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Dev Perf                            | 2.32 mins                | 459.07 mins            |
|                                     |               | Debug                               | 0.41 mins                | 6.1 mins               |
|                                     |               | Perf Commentator (trusted)          | 0.14 mins                | 19.97 mins             |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 1741.35 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 19.34 mins               | 1508.3 mins            |
|                                     |               | commit-message-check                | 2.34 mins                | 142.88 mins            |
|                                     |               | Unit test coverage                  | 7.81 mins                | 85.95 mins             |
|                                     |               | DevSkim                             | 0.91 mins                | 3.63 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 0.17 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.21 mins                | 0.42 mins              |
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
| datafuselabs/weekly                 | 1.77 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.33 mins                | 0.65 mins              |
|                                     |               | pages build and deployment          | 0.56 mins                | 1.12 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 50256.82 mins |                                     |                          |                        |
|                                     |               | CI                                  | 20.26 mins               | 5389.43 mins           |
|                                     |               | Service Test S3                     | 9.23 mins                | 2472.35 mins           |
|                                     |               | Service Test Fs                     | 6.02 mins                | 1613.8 mins            |
|                                     |               | Docs                                | 13.67 mins               | 2870.78 mins           |
|                                     |               | Service Test Memory                 | 5.76 mins                | 1544.1 mins            |
|                                     |               | Service Test Azblob                 | 5.92 mins                | 1587.48 mins           |
|                                     |               | Service Test HDFS                   | 6.89 mins                | 1824.88 mins           |
|                                     |               | Service Test HTTP                   | 7.15 mins                | 1916.07 mins           |
|                                     |               | Service Test Gcs                    | 6.43 mins                | 1724.3 mins            |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                    | 8.0 mins                 | 2144.27 mins           |
|                                     |               | Service Test IPMFS                  | 5.37 mins                | 1439.08 mins           |
|                                     |               | Service Test Ftp                    | 10.83 mins               | 2901.12 mins           |
|                                     |               | Service Test Redis                  | 5.86 mins                | 1570.4 mins            |
|                                     |               | Service Test Oss                    | 8.09 mins                | 2167.83 mins           |
|                                     |               | Service Test Moka                   | 5.75 mins                | 1541.43 mins           |
|                                     |               | Service Test RocksDB                | 12.56 mins               | 3366.12 mins           |
|                                     |               | Service Test Azdfs                  | 6.37 mins                | 1706.82 mins           |
|                                     |               | Service Test Ghac                   | 6.32 mins                | 1694.82 mins           |
|                                     |               | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached              | 5.63 mins                | 1509.03 mins           |
|                                     |               | Benchmark                           | 21.91 mins               | 1446.23 mins           |
|                                     |               | pages build and deployment          | 2.28 mins                | 152.45 mins            |
|                                     |               | Bindings Python CI                  | 26.48 mins               | 6037.98 mins           |
|                                     |               | Service Test WebDAV                 | 7.56 mins                | 1270.62 mins           |
|                                     |               | Service Test WebHDFS                | 6.96 mins                | 326.92 mins            |
|                                     |               | Service Test HDFS and WebHDFS       | 4.72 mins                | 14.17 mins             |
|                                     |               | Service Test Sled                   | 4.06 mins                | 24.33 mins             |
|                                     |               | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 275.35 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 9.18 mins                | 275.35 mins            |
| datafuselabs/databend-perf          | 621.2 mins    |                                     |                          |                        |
|                                     |               | Perf                                | 23.47 mins               | 422.43 mins            |
|                                     |               | pages build and deployment          | 0.77 mins                | 5.37 mins              |
|                                     |               | Reload tpch                         | 10.74 mins               | 64.43 mins             |
|                                     |               | Reload hits                         | 16.0 mins                | 80.02 mins             |
|                                     |               | Reload ontime                       | 9.79 mins                | 48.95 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 1.65 mins     |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.4 mins                 | 0.8 mins               |
|                                     |               | pages build and deployment          | 0.85 mins                | 0.85 mins              |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'message': 'Server Error'}
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 9553.83 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 20.73 mins               | 103.63 mins            |
|                                    |               | BR & Lightning                                       | 1.11 mins                | 637.28 mins            |
|                                    |               | Dumpling                                             | 8.77 mins                | 5305.75 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.78 mins                | 3491.32 mins           |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 187.12 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 4.56 mins                | 187.12 mins            |
| pingcap/kvproto                    | 1242.05 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 5.43 mins                | 505.33 mins            |
|                                    |               | Golang Test                                          | 1.77 mins                | 164.85 mins            |
|                                    |               | Rust Test                                            | 6.15 mins                | 571.87 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 6452.65 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 1.38 mins                | 12.43 mins             |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.56 mins                | 218.03 mins            |
|                                    |               | external-link-check                                  | 8.55 mins                | 8.55 mins              |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 76.53 mins             |
|                                    |               | ci                                                   | 3.95 mins                | 4518.37 mins           |
|                                    |               | Links                                                | 1.48 mins                | 5.93 mins              |
|                                    |               | bot                                                  | 0.93 mins                | 20.4 mins              |
|                                    |               | cron                                                 | 1.14 mins                | 34.33 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.73 mins                | 723.82 mins            |
|                                    |               | Prevent Deletion                                     | 0.72 mins                | 834.25 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5562.0 mins   |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.72 mins                | 7.9 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.2 mins                 | 57.67 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 57.45 mins             |
|                                    |               | ci                                                   | 3.47 mins                | 4467.88 mins           |
|                                    |               | Links                                                | 3.63 mins                | 18.17 mins             |
|                                    |               | Flush PDF                                            | 0.26 mins                | 8.25 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.41 mins                | 494.23 mins            |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 450.45 mins            |
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
| pingcap/blog-cn                    | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark                    | 77.73 mins    |                                                      |                          |                        |
|                                    |               | TLS test                                             | 0.18 mins                | 0.37 mins              |
|                                    |               | alter-primary-key-false-test                         | 0.17 mins                | 0.33 mins              |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 9.87 mins                | 69.07 mins             |
|                                    |               | Follower Read test                                   | 0.17 mins                | 0.35 mins              |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.92 mins              |
|                                    |               | License checker                                      | 0.17 mins                | 0.33 mins              |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 0.18 mins                | 0.37 mins              |
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
| pingcap/go-ycsb                    | 9.92 mins     |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.75 mins                | 5.5 mins               |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.21 mins                | 4.42 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 4138.47 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 23.31 mins               | 2028.35 mins           |
|                                    |               | ci                                                   | 20.02 mins               | 2102.47 mins           |
|                                    |               | Close stale issues/prs                               | 0.26 mins                | 7.65 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 3377.07 mins  |                                                      |                          |                        |
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
| pingcap/log                        | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
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
| pingcap/diag                       | 87.72 mins    |                                                      |                          |                        |
|                                    |               | reprotest                                            | 3.61 mins                | 46.93 mins             |
|                                    |               | static-tests                                         | 2.91 mins                | 40.78 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 35340.67 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.09 mins               | 10062.73 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.37 mins                | 8.22 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 4.95 mins                | 1040.13 mins           |
|                                    |               | DM Chaos                                             | 28.14 mins               | 5909.97 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.38 mins                | 147.65 mins            |
|                                    |               | DM Binlog 999999                                     | 12.16 mins               | 2553.9 mins            |
|                                    |               | Upstream Database Switch                             | 15.48 mins               | 3250.45 mins           |
|                                    |               | CDC Integration Tests                                | 16.82 mins               | 9669.85 mins           |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.14 mins                | 3.42 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 26.94 mins               | 2694.35 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
| pingcap/br                         | 0.0 mins      |                                                      |                          |                        |
|                                    |               | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | build                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 7.57 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 1.83 mins                | 1.83 mins              |
|                                    |               | workflow                                             | 1.43 mins                | 5.73 mins              |
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
| pingcap/dumpling                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
