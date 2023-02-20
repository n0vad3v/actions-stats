
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 412.03 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 29.43 mins               | 412.03 mins            |
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
| webp-sh/webp_server_go     | 224.45 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.32 mins                | 36.55 mins             |
|                            |               | Release Binaries                | 2.85 mins                | 5.7 mins               |
|                            |               | Build and release docker images | 17.4 mins                | 139.18 mins            |
|                            |               | CodeQL                          | 2.05 mins                | 43.02 mins             |
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
| datafuselabs/databend               | 90601.03 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 97.38 mins               | 3700.47 mins           |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 87.48 mins               | 20121.1 mins           |
|                                     |               | Build Tool                          | 31.42 mins               | 31.42 mins             |
|                                     |               | Dev Linux                           | 17.98 mins               | 17256.17 mins          |
|                                     |               | Dev MacOS                           | 50.03 mins               | 48024.8 mins           |
|                                     |               | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Debug                               | 0.41 mins                | 6.1 mins               |
|                                     |               | Benchmark                           | 4.28 mins                | 1420.28 mins           |
|                                     |               | Benchmark Commentator (trusted)     | 0.12 mins                | 36.42 mins             |
|                                     |               | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 8549.13 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 56.72 mins               | 7316.42 mins           |
|                                     |               | commit-message-check                | 6.53 mins                | 907.2 mins             |
|                                     |               | Unit test coverage                  | 8.25 mins                | 231.03 mins            |
|                                     |               | DevSkim                             | 0.82 mins                | 3.27 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 0.72 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 8.99 mins                | 53.95 mins             |
|                                     |               | .github/workflows/pages.yaml        | 11.1 mins                | 11.1 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 25.45 mins               | 25.45 mins             |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 1.72 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.32 mins                | 0.63 mins              |
|                                     |               | pages build and deployment          | 0.54 mins                | 1.08 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 84061.37 mins |                                     |                          |                        |
|                                     |               | CI                                  | 21.85 mins               | 7733.37 mins           |
|                                     |               | Service Test S3                     | 11.52 mins               | 3892.77 mins           |
|                                     |               | Service Test Fs                     | 8.94 mins                | 3020.43 mins           |
|                                     |               | Docs                                | 15.54 mins               | 3652.03 mins           |
|                                     |               | Service Test Memory                 | 7.42 mins                | 2509.6 mins            |
|                                     |               | Service Test Azblob                 | 7.97 mins                | 2695.12 mins           |
|                                     |               | Service Test HDFS                   | 9.17 mins                | 3072.42 mins           |
|                                     |               | Service Test HTTP                   | 9.57 mins                | 3233.62 mins           |
|                                     |               | Service Test Gcs                    | 8.49 mins                | 2868.33 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                    | 9.81 mins                | 3314.5 mins            |
|                                     |               | Service Test IPMFS                  | 7.95 mins                | 2687.33 mins           |
|                                     |               | Service Test Ftp                    | 12.91 mins               | 4364.15 mins           |
|                                     |               | Service Test Redis                  | 7.98 mins                | 2698.22 mins           |
|                                     |               | Service Test Oss                    | 10.22 mins               | 3454.85 mins           |
|                                     |               | Service Test Moka                   | 8.11 mins                | 2742.1 mins            |
|                                     |               | Service Test RocksDB                | 15.34 mins               | 5184.47 mins           |
|                                     |               | Service Test Azdfs                  | 8.38 mins                | 2831.5 mins            |
|                                     |               | Service Test Ghac                   | 8.45 mins                | 2856.5 mins            |
|                                     |               | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached              | 7.51 mins                | 2536.87 mins           |
|                                     |               | Benchmark                           | 23.22 mins               | 2206.07 mins           |
|                                     |               | pages build and deployment          | 3.2 mins                 | 303.55 mins            |
|                                     |               | Bindings Python CI                  | 25.81 mins               | 9241.35 mins           |
|                                     |               | Service Test WebDAV                 | 11.44 mins               | 3556.52 mins           |
|                                     |               | Service Test WebHDFS                | 11.27 mins               | 1971.58 mins           |
|                                     |               | Service Test HDFS and WebHDFS       | 4.72 mins                | 14.17 mins             |
|                                     |               | Service Test Sled                   | 10.6 mins                | 1419.97 mins           |
|                                     |               | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 343.32 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 11.44 mins               | 343.32 mins            |
| datafuselabs/databend-perf          | 973.48 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 49.57 mins               | 793.13 mins            |
|                                     |               | pages build and deployment          | 0.72 mins                | 5.07 mins              |
|                                     |               | Reload tpch                         | 11.78 mins               | 58.9 mins              |
|                                     |               | Reload hits                         | 18.06 mins               | 72.25 mins             |
|                                     |               | Reload ontime                       | 11.03 mins               | 44.13 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 1.4 mins      |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.48 mins                | 0.48 mins              |
|                                     |               | pages build and deployment          | 0.92 mins                | 0.92 mins              |
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
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 6804.03 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 25.42 mins               | 25.42 mins             |
|                                    |               | BR & Lightning                                       | 1.2 mins                 | 832.25 mins            |
|                                    |               | Dumpling                                             | 8.68 mins                | 5045.05 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.36 mins                | 885.25 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 141.62 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 4.72 mins                | 141.62 mins            |
| pingcap/kvproto                    | 883.22 mins   |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.95 mins                | 416.98 mins            |
|                                    |               | Golang Test                                          | 1.65 mins                | 99.17 mins             |
|                                    |               | Rust Test                                            | 6.12 mins                | 367.07 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 4853.42 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.52 mins                | 3.13 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 60.15 mins             |
|                                    |               | external-link-check                                  | 4.59 mins                | 22.97 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 64.55 mins             |
|                                    |               | ci                                                   | 3.43 mins                | 3840.12 mins           |
|                                    |               | Links                                                | 1.95 mins                | 9.73 mins              |
|                                    |               | bot                                                  | 0.9 mins                 | 18.92 mins             |
|                                    |               | cron                                                 | 1.18 mins                | 35.47 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.4 mins                 | 418.45 mins            |
|                                    |               | Prevent Deletion                                     | 0.34 mins                | 379.93 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5360.18 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.46 mins                | 3.2 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 52.55 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 52.1 mins              |
|                                    |               | ci                                                   | 3.61 mins                | 4362.9 mins            |
|                                    |               | Links                                                | 3.02 mins                | 15.1 mins              |
|                                    |               | Flush PDF                                            | 0.25 mins                | 7.58 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.4 mins                 | 456.43 mins            |
|                                    |               | Prevent Deletion                                     | 0.33 mins                | 410.32 mins            |
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
| pingcap/tispark                    | 194.55 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 6.77 mins                | 33.83 mins             |
|                                    |               | alter-primary-key-false-test                         | 4.24 mins                | 21.18 mins             |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 10.7 mins                | 96.3 mins              |
|                                    |               | Follower Read test                                   | 4.11 mins                | 20.53 mins             |
|                                    |               | Close inactive issues                                | 0.22 mins                | 6.62 mins              |
|                                    |               | License checker                                      | 0.75 mins                | 3.75 mins              |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 2.47 mins                | 12.33 mins             |
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
| pingcap/go-ycsb                    | 28.55 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.63 mins                | 15.78 mins             |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.13 mins                | 12.77 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 5806.48 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 23.22 mins               | 2786.67 mins           |
|                                    |               | ci                                                   | 21.37 mins               | 3012.67 mins           |
|                                    |               | Close stale issues/prs                               | 0.24 mins                | 7.15 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 4313.4 mins   |                                                      |                          |                        |
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
| pingcap/diag                       | 176.63 mins   |                                                      |                          |                        |
|                                    |               | reprotest                                            | 5.96 mins                | 113.18 mins            |
|                                    |               | static-tests                                         | 3.02 mins                | 63.45 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 40257.43 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.09 mins               | 11136.7 mins           |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.37 mins                | 8.22 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 4.91 mins                | 1030.62 mins           |
|                                    |               | DM Chaos                                             | 27.07 mins               | 5683.82 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.26 mins                | 121.37 mins            |
|                                    |               | DM Binlog 999999                                     | 12.31 mins               | 2585.47 mins           |
|                                    |               | Upstream Database Switch                             | 15.53 mins               | 3261.05 mins           |
|                                    |               | CDC Integration Tests                                | 17.39 mins               | 10243.35 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.14 mins                | 3.42 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 29.43 mins               | 6181.22 mins           |
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
