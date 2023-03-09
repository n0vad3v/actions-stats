
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 184.8 mins    |                    |                          |                        |
|                                |               | Build Runner Image | 92.4 mins                | 184.8 mins             |
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
| webp-sh/webp_server_go     | 293.45 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.58 mins                | 46.5 mins              |
|                            |               | Release Binaries                | 2.86 mins                | 5.72 mins              |
|                            |               | Build and release docker images | 17.19 mins               | 189.08 mins            |
|                            |               | CodeQL                          | 1.93 mins                | 52.15 mins             |
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
| datafuselabs/databend               | 135851.0 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 104.76 mins              | 4923.92 mins           |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 83.9 mins                | 23996.2 mins           |
|                                     |               | Build Tool                          | 31.82 mins               | 95.47 mins             |
|                                     |               | Dev Linux                           | 19.92 mins               | 26489.53 mins          |
|                                     |               | Dev MacOS                           | 57.08 mins               | 75919.88 mins          |
|                                     |               | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Benchmark                           | 2.82 mins                | 3857.13 mins           |
|                                     |               | Benchmark Commentator (trusted)     | 0.09 mins                | 124.22 mins            |
|                                     |               | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |               | Typos Check                         | 0.98 mins                | 440.37 mins            |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 10135.03 mins |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 51.65 mins               | 8212.13 mins           |
|                                     |               | commit-message-check                | 6.84 mins                | 1279.63 mins           |
|                                     |               | Unit test coverage                  | 8.53 mins                | 400.92 mins            |
|                                     |               | DevSkim                             | 0.83 mins                | 3.32 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 1.25 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 4.27 mins                | 55.47 mins             |
|                                     |               | .github/workflows/pages.yaml        | 3.77 mins                | 26.42 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 10.23 mins               | 51.17 mins             |
|                                     |               | pages build and deployment          | 14.96 mins               | 104.73 mins            |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 15.77 mins    |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.82 mins                | 3.28 mins              |
|                                     |               | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |               | pages build and deployment          | 1.35 mins                | 5.4 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 95370.87 mins |                                     |                          |                        |
|                                     |               | CI                                  | 20.07 mins               | 9251.58 mins           |
|                                     |               | Service Test S3                     | 11.96 mins               | 3756.72 mins           |
|                                     |               | Service Test Fs                     | 11.0 mins                | 3431.72 mins           |
|                                     |               | Service Test Memory                 | 8.49 mins                | 2647.83 mins           |
|                                     |               | Service Test Azblob                 | 8.7 mins                 | 2724.02 mins           |
|                                     |               | Service Test HDFS                   | 10.92 mins               | 3407.08 mins           |
|                                     |               | Service Test HTTP                   | 11.16 mins               | 3480.55 mins           |
|                                     |               | Service Test Gcs                    | 9.92 mins                | 3106.32 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                    | 11.64 mins               | 3642.87 mins           |
|                                     |               | Service Test IPMFS                  | 9.44 mins                | 2955.17 mins           |
|                                     |               | Service Test Ftp                    | 14.09 mins               | 4438.65 mins           |
|                                     |               | Service Test Redis                  | 9.3 mins                 | 2902.18 mins           |
|                                     |               | Service Test Oss                    | 11.16 mins               | 3502.9 mins            |
|                                     |               | Service Test Moka                   | 9.4 mins                 | 2934.2 mins            |
|                                     |               | Service Test RocksDB                | 16.28 mins               | 5176.2 mins            |
|                                     |               | Service Test Azdfs                  | 9.93 mins                | 3108.83 mins           |
|                                     |               | Service Test Ghac                   | 10.03 mins               | 3140.13 mins           |
|                                     |               | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached              | 8.89 mins                | 2773.22 mins           |
|                                     |               | pages build and deployment          | 4.08 mins                | 485.65 mins            |
|                                     |               | Bindings Python CI                  | 28.15 mins               | 12077.7 mins           |
|                                     |               | Service Test WebDAV                 | 16.26 mins               | 5333.72 mins           |
|                                     |               | Service Test WebHDFS                | 10.52 mins               | 3197.22 mins           |
|                                     |               | Service Test HDFS and WebHDFS       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Sled                   | 8.88 mins                | 2503.22 mins           |
|                                     |               | Service Test Dashmap                | 7.83 mins                | 1048.63 mins           |
|                                     |               | Benchmark                           | 22.07 mins               | 1147.88 mins           |
|                                     |               | Docs                                | 13.25 mins               | 1841.25 mins           |
|                                     |               | Typos Check                         | 3.6 mins                 | 831.4 mins             |
|                                     |               | Binding NodeJS CI                   | 4.6 mins                 | 524.03 mins            |
|                                     |               | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 552.13 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 15.34 mins               | 552.13 mins            |
| datafuselabs/databend-perf          | 2081.25 mins  |                                     |                          |                        |
|                                     |               | Perf                                | 115.83 mins              | 1853.23 mins           |
|                                     |               | pages build and deployment          | 1.14 mins                | 6.85 mins              |
|                                     |               | Reload tpch                         | 12.37 mins               | 61.85 mins             |
|                                     |               | Reload hits                         | 23.94 mins               | 119.68 mins            |
|                                     |               | Reload ontime                       | 7.93 mins                | 39.63 mins             |
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
| pingcap/tidb                       | 5250.82 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 12.57 mins               | 12.57 mins             |
|                                    |               | BR & Lightning                                       | 1.28 mins                | 895.67 mins            |
|                                    |               | Dumpling                                             | 9.19 mins                | 3757.08 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.89 mins                | 569.43 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 186.87 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.5 mins                 | 186.87 mins            |
| pingcap/kvproto                    | 1190.97 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.49 mins                | 512.88 mins            |
|                                    |               | Golang Test                                          | 1.82 mins                | 143.8 mins             |
|                                    |               | Rust Test                                            | 6.76 mins                | 534.28 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5817.53 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.5 mins                 | 6.03 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 86.38 mins             |
|                                    |               | external-link-check                                  | 3.73 mins                | 26.13 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 89.75 mins             |
|                                    |               | ci                                                   | 3.55 mins                | 4568.07 mins           |
|                                    |               | Links                                                | 2.48 mins                | 9.9 mins               |
|                                    |               | bot                                                  | 0.81 mins                | 17.88 mins             |
|                                    |               | cron                                                 | 1.32 mins                | 39.45 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.43 mins                | 510.87 mins            |
|                                    |               | Prevent Deletion                                     | 0.36 mins                | 463.07 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5865.03 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.43 mins                | 8.15 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 77.7 mins              |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 82.0 mins              |
|                                    |               | ci                                                   | 4.16 mins                | 4812.42 mins           |
|                                    |               | Links                                                | 1.72 mins                | 6.88 mins              |
|                                    |               | Flush All PDF                                        | 0.26 mins                | 9.92 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.42 mins                | 450.0 mins             |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 417.68 mins            |
|                                    |               | Flush PDF by Version                                 | 0.28 mins                | 0.28 mins              |
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
| pingcap/tispark                    | 2252.28 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.27 mins               | 504.23 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.16 mins                | 347.98 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 18.13 mins               | 761.5 mins             |
|                                    |               | Follower Read test                                   | 9.43 mins                | 358.2 mins             |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.92 mins              |
|                                    |               | License checker                                      | 1.14 mins                | 43.18 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 6.06 mins                | 230.27 mins            |
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
| pingcap/go-ycsb                    | 43.5 mins     |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.67 mins                | 24.0 mins              |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.17 mins                | 19.5 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 11809.08 mins |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 1066.49 mins             | 2132.98 mins           |
|                                    |               | chaos                                                | 21.45 mins               | 4869.9 mins            |
|                                    |               | ci                                                   | 18.46 mins               | 4798.87 mins           |
|                                    |               | Close stale issues/prs                               | 0.24 mins                | 7.33 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 6115.28 mins  |                                                      |                          |                        |
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
| pingcap/diag                       | 121.88 mins   |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.18 mins               | 89.45 mins             |
|                                    |               | static-tests                                         | 3.24 mins                | 32.43 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 53614.75 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.93 mins               | 18046.78 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.51 mins                | 21.48 mins             |
|                                    |               | Upgrade DM via TiUP                                  | 5.27 mins                | 1107.42 mins           |
|                                    |               | DM Chaos                                             | 27.98 mins               | 5875.57 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.27 mins                | 188.83 mins            |
|                                    |               | DM Binlog 999999                                     | 13.93 mins               | 2925.7 mins            |
|                                    |               | Upstream Database Switch                             | 15.45 mins               | 3244.48 mins           |
|                                    |               | CDC Integration Tests                                | 17.68 mins               | 15466.88 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.51 mins                | 4.52 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 32.05 mins               | 6730.87 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
| pingcap/br                         | 10.18 mins    |                                                      |                          |                        |
|                                    |               | compatibility-test                                   | 2.23 mins                | 2.23 mins              |
|                                    |               | build                                                | 7.95 mins                | 7.95 mins              |
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
