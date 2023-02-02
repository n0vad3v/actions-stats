
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
| webp-sh/webp_server_go     | 102.0 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.05 mins                | 21.38 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 9.59 mins                | 47.95 mins             |
|                            |               | CodeQL                          | 1.92 mins                | 32.67 mins             |
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
+-------------------------------------+---------------+--------------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                              | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+--------------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 87465.42 mins |                                            |                          |                        |
|                                     |               | Unit Tests                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                                 | 89.05 mins               | 18611.68 mins          |
|                                     |               | Build Tool                                 | 31.42 mins               | 31.42 mins             |
|                                     |               | Dev Linux                                  | 19.9 mins                | 19281.05 mins          |
|                                     |               | Dev MacOS                                  | 48.61 mins               | 47099.55 mins          |
|                                     |               | Backport                                   | 69.41 mins               | 208.23 mins            |
|                                     |               | Dev Perf                                   | 17.7 mins                | 177.0 mins             |
|                                     |               | Release                                    | 89.41 mins               | 2056.48 mins           |
|                                     |               | Stateless(Cluster)                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                            |                          |                        |
| datafuselabs/openraft               | 1747.15 mins  |                                            |                          |                        |
|                                     |               | chaos-test                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                         | 20.68 mins               | 1551.27 mins           |
|                                     |               | commit-message-check                       | 2.09 mins                | 116.93 mins            |
|                                     |               | Unit test coverage                         | 7.44 mins                | 74.38 mins             |
|                                     |               | DevSkim                                    | 0.88 mins                | 3.5 mins               |
|                                     |               | .github/workflows/issue-cmds.yml           | 0.05 mins                | 0.38 mins              |
|                                     |               | .github/workflows/issue-welcome.yml        | 0.23 mins                | 0.68 mins              |
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
| datafuselabs/opendal                | 38456.25 mins |                                            |                          |                        |
|                                     |               | CI                                         | 16.79 mins               | 4112.82 mins           |
|                                     |               | Service Test S3                            | 8.79 mins                | 2170.48 mins           |
|                                     |               | Service Test Fs                            | 4.96 mins                | 1225.97 mins           |
|                                     |               | Docs                                       | 13.5 mins                | 2848.93 mins           |
|                                     |               | Service Test Memory                        | 5.22 mins                | 1290.55 mins           |
|                                     |               | Service Test Azblob                        | 5.31 mins                | 1312.1 mins            |
|                                     |               | Service Test HDFS                          | 6.27 mins                | 1547.95 mins           |
|                                     |               | Service Test HTTP                          | 6.53 mins                | 1612.2 mins            |
|                                     |               | Service Test Gcs                           | 6.07 mins                | 1499.27 mins           |
|                                     |               | Test Vault                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                           | 7.56 mins                | 1867.67 mins           |
|                                     |               | Service Test IPMFS                         | 4.78 mins                | 1180.85 mins           |
|                                     |               | Service Test Ftp                           | 9.8 mins                 | 2419.7 mins            |
|                                     |               | Service Test Redis                         | 5.46 mins                | 1349.78 mins           |
|                                     |               | Service Test Oss                           | 7.63 mins                | 1884.9 mins            |
|                                     |               | Service Test Moka                          | 5.25 mins                | 1296.67 mins           |
|                                     |               | Service Test RocksDB                       | 12.23 mins               | 3021.22 mins           |
|                                     |               | Service Test Azdfs                         | 6.13 mins                | 1514.72 mins           |
|                                     |               | Service Test Ghac                          | 5.55 mins                | 1370.85 mins           |
|                                     |               | A Test                                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached                     | 5.43 mins                | 1021.48 mins           |
|                                     |               | Benchmark                                  | 22.08 mins               | 772.65 mins            |
|                                     |               | pages build and deployment                 | 2.1 mins                 | 75.68 mins             |
|                                     |               | Bindings Python CI                         | 24.29 mins               | 2720.15 mins           |
|                                     |               | Service Test WebDAV                        | 6.41 mins                | 339.67 mins            |
|                                     |               | .github/workflows/service_test_webhdfs.yml | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test IPFS                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 329.63 mins   |                                            |                          |                        |
|                                     |               | CI                                         | 9.99 mins                | 329.63 mins            |
| datafuselabs/databend-perf          | 554.27 mins   |                                            |                          |                        |
|                                     |               | Perf                                       | 32.49 mins               | 389.85 mins            |
|                                     |               | pages build and deployment                 | 0.71 mins                | 4.98 mins              |
|                                     |               | Reload tpch                                | 7.5 mins                 | 37.5 mins              |
|                                     |               | Reload hits                                | 10.63 mins               | 74.43 mins             |
|                                     |               | Reload ontime                              | 7.92 mins                | 47.5 mins              |
|                                     |               | No workflow name(why?)                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 4.55 mins     |                                            |                          |                        |
|                                     |               | Release Charts                             | 0.41 mins                | 2.05 mins              |
|                                     |               | pages build and deployment                 | 0.83 mins                | 2.5 mins               |
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
| pingcap/tidb                       | 9554.42 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 20.73 mins               | 103.63 mins            |
|                                    |               | BR & Lightning                                       | 1.08 mins                | 466.92 mins            |
|                                    |               | Dumpling                                             | 8.96 mins                | 3331.58 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.82 mins                | 5652.28 mins           |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 163.22 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 4.41 mins                | 163.22 mins            |
| pingcap/kvproto                    | 1225.4 mins   |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 4.69 mins                | 455.22 mins            |
|                                    |               | Golang Test                                          | 2.0 mins                 | 194.2 mins             |
|                                    |               | Rust Test                                            | 5.94 mins                | 575.98 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 6488.93 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.17 mins                | 24.47 mins             |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.53 mins                | 223.85 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 79.18 mins             |
|                                    |               | ci                                                   | 4.14 mins                | 4495.17 mins           |
|                                    |               | Links                                                | 2.06 mins                | 8.25 mins              |
|                                    |               | bot                                                  | 0.91 mins                | 20.08 mins             |
|                                    |               | cron                                                 | 1.0 mins                 | 30.1 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.82 mins                | 758.48 mins            |
|                                    |               | Prevent Deletion                                     | 0.77 mins                | 849.35 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4666.95 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.78 mins                | 9.37 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.2 mins                 | 62.55 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 61.3 mins              |
|                                    |               | ci                                                   | 3.46 mins                | 3618.03 mins           |
|                                    |               | Links                                                | 3.47 mins                | 17.35 mins             |
|                                    |               | Flush PDF                                            | 0.26 mins                | 8.18 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.55 mins                | 528.98 mins            |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 361.18 mins            |
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
| pingcap/tispark                    | 955.5 mins    |                                                      |                          |                        |
|                                    |               | TLS test                                             | 12.16 mins               | 218.93 mins            |
|                                    |               | alter-primary-key-false-test                         | 8.28 mins                | 148.97 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 13.39 mins               | 294.68 mins            |
|                                    |               | Follower Read test                                   | 8.49 mins                | 152.82 mins            |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.97 mins              |
|                                    |               | License checker                                      | 2.73 mins                | 49.22 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 4.66 mins                | 83.92 mins             |
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
| pingcap/tidb-operator              | 4289.87 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 27.6 mins                | 2291.05 mins           |
|                                    |               | ci                                                   | 19.52 mins               | 1990.93 mins           |
|                                    |               | Close stale issues/prs                               | 0.26 mins                | 7.88 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 3116.03 mins  |                                                      |                          |                        |
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
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 35925.18 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.14 mins               | 9128.43 mins           |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.38 mins                | 7.5 mins               |
|                                    |               | Upgrade DM via TiUP                                  | 5.06 mins                | 1061.83 mins           |
|                                    |               | DM Chaos                                             | 28.47 mins               | 5979.07 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.41 mins                | 132.65 mins            |
|                                    |               | DM Binlog 999999                                     | 12.24 mins               | 2570.55 mins           |
|                                    |               | Upstream Database Switch                             | 14.79 mins               | 3105.85 mins           |
|                                    |               | CDC Integration Tests                                | 16.83 mins               | 7674.48 mins           |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.41 mins                | 8.45 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 29.79 mins               | 6256.37 mins           |
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
| pingcap/go-tpc                     | 1.32 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.32 mins                | 1.32 mins              |
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
| pingcap/tipocket                   | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build-image                                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build-workflow                                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pre-Check                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Test                                                 | 0.0 mins                 | 0.0 mins               |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
