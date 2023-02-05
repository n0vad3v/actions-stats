
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
| webp-sh/webp_server_go     | 126.52 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 2.92 mins                | 26.27 mins             |
|                            |               | Release Binaries                | 2.67 mins                | 2.67 mins              |
|                            |               | Build and release docker images | 10.21 mins               | 61.27 mins             |
|                            |               | CodeQL                          | 2.02 mins                | 36.32 mins             |
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
Error: {'total_count': 300, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+--------------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                              | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+--------------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 88637.22 mins |                                            |                          |                        |
|                                     |               | Unit Tests                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                                    | 89.95 mins               | 2338.58 mins           |
|                                     |               | License checker                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                                 | 85.48 mins               | 19061.3 mins           |
|                                     |               | Build Tool                                 | 31.42 mins               | 31.42 mins             |
|                                     |               | Dev Linux                                  | 19.38 mins               | 18891.45 mins          |
|                                     |               | Dev MacOS                                  | 49.16 mins               | 47929.23 mins          |
|                                     |               | Backport                                   | 69.41 mins               | 208.23 mins            |
|                                     |               | Dev Perf                                   | 17.7 mins                | 177.0 mins             |
|                                     |               | Stateless(Cluster)                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                            |                          |                        |
| datafuselabs/openraft               | 1637.33 mins  |                                            |                          |                        |
|                                     |               | chaos-test                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                         | 19.89 mins               | 1451.83 mins           |
|                                     |               | commit-message-check                       | 2.19 mins                | 115.87 mins            |
|                                     |               | Unit test coverage                         | 7.23 mins                | 65.08 mins             |
|                                     |               | DevSkim                                    | 0.87 mins                | 4.35 mins              |
|                                     |               | .github/workflows/issue-cmds.yml           | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-welcome.yml        | 0.2 mins                 | 0.2 mins               |
|                                     |               | .github/workflows/pages.yaml               | 0.0 mins                 | 0.0 mins               |
|                                     |               | No workflow name(why?)                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment                 | 0.0 mins                 | 0.0 mins               |
| datafuselabs/fusebots               | 0.0 mins      |                                            |                          |                        |
|                                     |               | docker                                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                            |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                            |                          |                        |
|                                     |               | pages build and deployment                 | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                            |                          |                        |
| datafuselabs/weekly                 | 2.7 mins      |                                            |                          |                        |
|                                     |               | Build and deploy on push                   | 0.33 mins                | 1.0 mins               |
|                                     |               | pages build and deployment                 | 0.57 mins                | 1.7 mins               |
| datafuselabs/.github                | 0.0 mins      |                                            |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                            |                          |                        |
|                                     |               | .github/workflows/pages.yml                | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment                 | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 42445.87 mins |                                            |                          |                        |
|                                     |               | CI                                         | 17.77 mins               | 4512.63 mins           |
|                                     |               | Service Test S3                            | 9.18 mins                | 2350.15 mins           |
|                                     |               | Service Test Fs                            | 5.14 mins                | 1316.95 mins           |
|                                     |               | Docs                                       | 13.73 mins               | 3047.33 mins           |
|                                     |               | Service Test Memory                        | 5.53 mins                | 1415.32 mins           |
|                                     |               | Service Test Azblob                        | 5.48 mins                | 1403.73 mins           |
|                                     |               | Service Test HDFS                          | 6.56 mins                | 1659.9 mins            |
|                                     |               | Service Test HTTP                          | 6.72 mins                | 1719.43 mins           |
|                                     |               | Service Test Gcs                           | 6.34 mins                | 1623.72 mins           |
|                                     |               | Test Vault                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                           | 7.76 mins                | 1987.42 mins           |
|                                     |               | Service Test IPMFS                         | 5.02 mins                | 1285.2 mins            |
|                                     |               | Service Test Ftp                           | 10.23 mins               | 2618.9 mins            |
|                                     |               | Service Test Redis                         | 5.58 mins                | 1428.18 mins           |
|                                     |               | Service Test Oss                           | 7.94 mins                | 2032.9 mins            |
|                                     |               | Service Test Moka                          | 5.51 mins                | 1411.68 mins           |
|                                     |               | Service Test RocksDB                       | 12.58 mins               | 3221.22 mins           |
|                                     |               | Service Test Azdfs                         | 6.39 mins                | 1635.42 mins           |
|                                     |               | Service Test Ghac                          | 5.79 mins                | 1482.1 mins            |
|                                     |               | A Test                                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached                     | 5.44 mins                | 1196.85 mins           |
|                                     |               | Benchmark                                  | 22.03 mins               | 947.2 mins             |
|                                     |               | pages build and deployment                 | 1.89 mins                | 83.15 mins             |
|                                     |               | Bindings Python CI                         | 23.89 mins               | 3464.02 mins           |
|                                     |               | Service Test WebDAV                        | 6.92 mins                | 588.3 mins             |
|                                     |               | .github/workflows/service_test_webhdfs.yml | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test HDFS and WebHDFS              | 4.72 mins                | 14.17 mins             |
|                                     |               | Service Test IPFS                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 321.12 mins   |                                            |                          |                        |
|                                     |               | CI                                         | 10.03 mins               | 321.12 mins            |
| datafuselabs/databend-perf          | 504.63 mins   |                                            |                          |                        |
|                                     |               | Perf                                       | 30.89 mins               | 339.77 mins            |
|                                     |               | pages build and deployment                 | 0.71 mins                | 4.27 mins              |
|                                     |               | Reload tpch                                | 13.27 mins               | 53.08 mins             |
|                                     |               | Reload hits                                | 16.65 mins               | 66.58 mins             |
|                                     |               | Reload ontime                              | 10.23 mins               | 40.93 mins             |
|                                     |               | No workflow name(why?)                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 1.65 mins     |                                            |                          |                        |
|                                     |               | Release Charts                             | 0.4 mins                 | 0.8 mins               |
|                                     |               | pages build and deployment                 | 0.85 mins                | 0.85 mins              |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                            |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                            |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                            |                          |                        |
|                                     |               | CI                                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml                | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment                 | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                            |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                            |                          |                        |
+-------------------------------------+---------------+--------------------------------------------+--------------------------+------------------------+

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
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 8930.37 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 20.73 mins               | 103.63 mins            |
|                                    |               | BR & Lightning                                       | 1.15 mins                | 516.4 mins             |
|                                    |               | Dumpling                                             | 8.92 mins                | 3594.48 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.82 mins                | 4715.85 mins           |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 169.42 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 4.34 mins                | 169.42 mins            |
| pingcap/kvproto                    | 1162.7 mins   |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 4.79 mins                | 436.12 mins            |
|                                    |               | Golang Test                                          | 2.04 mins                | 186.07 mins            |
|                                    |               | Rust Test                                            | 5.94 mins                | 540.52 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 6311.92 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.35 mins                | 13.48 mins             |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.56 mins                | 218.47 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 74.57 mins             |
|                                    |               | ci                                                   | 4.22 mins                | 4385.4 mins            |
|                                    |               | Links                                                | 2.06 mins                | 8.25 mins              |
|                                    |               | bot                                                  | 0.91 mins                | 18.22 mins             |
|                                    |               | cron                                                 | 1.06 mins                | 31.78 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.84 mins                | 736.12 mins            |
|                                    |               | Prevent Deletion                                     | 0.78 mins                | 825.63 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4857.33 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.77 mins                | 8.5 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.2 mins                 | 59.62 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 56.83 mins             |
|                                    |               | ci                                                   | 3.4 mins                 | 3785.78 mins           |
|                                    |               | Links                                                | 3.47 mins                | 17.35 mins             |
|                                    |               | Flush PDF                                            | 0.26 mins                | 8.27 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.53 mins                | 543.58 mins            |
|                                    |               | Prevent Deletion                                     | 0.34 mins                | 377.4 mins             |
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
| pingcap/tispark                    | 895.57 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 11.79 mins               | 200.5 mins             |
|                                    |               | alter-primary-key-false-test                         | 7.93 mins                | 134.83 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 13.4 mins                | 281.3 mins             |
|                                    |               | Follower Read test                                   | 8.45 mins                | 143.63 mins            |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.97 mins              |
|                                    |               | License checker                                      | 2.83 mins                | 48.15 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 4.72 mins                | 80.18 mins             |
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
|                                    |               | Docker Image CI                                      | 2.72 mins                | 5.43 mins              |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.24 mins                | 4.48 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 3650.93 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 23.75 mins               | 1852.27 mins           |
|                                    |               | ci                                                   | 18.09 mins               | 1790.95 mins           |
|                                    |               | Close stale issues/prs                               | 0.26 mins                | 7.72 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 2884.77 mins  |                                                      |                          |                        |
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
| pingcap/tiflow                     | 35616.03 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.04 mins               | 8422.65 mins           |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.37 mins                | 8.22 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 5.02 mins                | 1054.55 mins           |
|                                    |               | DM Chaos                                             | 28.42 mins               | 5968.35 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.4 mins                 | 134.7 mins             |
|                                    |               | DM Binlog 999999                                     | 12.17 mins               | 2556.12 mins           |
|                                    |               | Upstream Database Switch                             | 15.45 mins               | 3243.8 mins            |
|                                    |               | CDC Integration Tests                                | 16.96 mins               | 7970.8 mins            |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.41 mins                | 8.45 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 29.75 mins               | 6248.4 mins            |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
| pingcap/br                         | 12.12 mins    |                                                      |                          |                        |
|                                    |               | compatibility-test                                   | 1.23 mins                | 1.23 mins              |
|                                    |               | build                                                | 10.88 mins               | 10.88 mins             |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 5.85 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 1.83 mins                | 1.83 mins              |
|                                    |               | workflow                                             | 1.34 mins                | 4.02 mins              |
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
Error: {'message': 'Server Error'}
