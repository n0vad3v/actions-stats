
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
| webp-sh/webp_server_go     | 237.38 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.36 mins                | 43.62 mins             |
|                            |               | Release Binaries                | 2.85 mins                | 5.7 mins               |
|                            |               | Build and release docker images | 17.4 mins                | 139.18 mins            |
|                            |               | CodeQL                          | 2.04 mins                | 48.88 mins             |
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
| datafuselabs/databend               | 95404.13 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 97.15 mins               | 3691.68 mins           |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 85.17 mins               | 20440.35 mins          |
|                                     |               | Build Tool                          | 31.42 mins               | 31.42 mins             |
|                                     |               | Dev Linux                           | 18.01 mins               | 18408.75 mins          |
|                                     |               | Dev MacOS                           | 49.99 mins               | 51086.62 mins          |
|                                     |               | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Debug                               | 0.41 mins                | 6.1 mins               |
|                                     |               | Benchmark                           | 3.85 mins                | 1690.65 mins           |
|                                     |               | Benchmark Commentator (trusted)     | 0.11 mins                | 44.28 mins             |
|                                     |               | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 8637.68 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 55.51 mins               | 7382.75 mins           |
|                                     |               | commit-message-check                | 6.34 mins                | 913.35 mins            |
|                                     |               | Unit test coverage                  | 8.24 mins                | 247.3 mins             |
|                                     |               | DevSkim                             | 0.82 mins                | 3.27 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 0.72 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 10.75 mins               | 53.75 mins             |
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
| datafuselabs/weekly                 | 7.5 mins      |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.92 mins                | 2.75 mins              |
|                                     |               | pages build and deployment          | 1.58 mins                | 4.75 mins              |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 88781.63 mins |                                     |                          |                        |
|                                     |               | CI                                  | 21.74 mins               | 8150.82 mins           |
|                                     |               | Service Test S3                     | 11.43 mins               | 4044.45 mins           |
|                                     |               | Service Test Fs                     | 8.95 mins                | 3169.52 mins           |
|                                     |               | Docs                                | 15.54 mins               | 3931.98 mins           |
|                                     |               | Service Test Memory                 | 7.42 mins                | 2625.38 mins           |
|                                     |               | Service Test Azblob                 | 7.96 mins                | 2819.48 mins           |
|                                     |               | Service Test HDFS                   | 9.22 mins                | 3236.98 mins           |
|                                     |               | Service Test HTTP                   | 9.48 mins                | 3357.45 mins           |
|                                     |               | Service Test Gcs                    | 8.59 mins                | 3042.55 mins           |
|                                     |               | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                    | 9.97 mins                | 3530.57 mins           |
|                                     |               | Service Test IPMFS                  | 7.94 mins                | 2818.92 mins           |
|                                     |               | Service Test Ftp                    | 12.94 mins               | 4594.78 mins           |
|                                     |               | Service Test Redis                  | 7.98 mins                | 2834.6 mins            |
|                                     |               | Service Test Oss                    | 10.19 mins               | 3616.8 mins            |
|                                     |               | Service Test Moka                   | 8.09 mins                | 2871.47 mins           |
|                                     |               | Service Test RocksDB                | 15.21 mins               | 5400.6 mins            |
|                                     |               | Service Test Azdfs                  | 8.36 mins                | 2966.6 mins            |
|                                     |               | Service Test Ghac                   | 8.45 mins                | 2999.1 mins            |
|                                     |               | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached              | 7.57 mins                | 2688.15 mins           |
|                                     |               | Benchmark                           | 23.11 mins               | 2333.78 mins           |
|                                     |               | pages build and deployment          | 3.08 mins                | 310.95 mins            |
|                                     |               | Bindings Python CI                  | 25.7 mins                | 9764.38 mins           |
|                                     |               | Service Test WebDAV                 | 11.76 mins               | 3868.62 mins           |
|                                     |               | Service Test WebHDFS                | 11.04 mins               | 2130.97 mins           |
|                                     |               | Service Test HDFS and WebHDFS       | 4.72 mins                | 14.17 mins             |
|                                     |               | Service Test Sled                   | 10.39 mins               | 1579.6 mins            |
|                                     |               | Service Test Dashmap                | 11.28 mins               | 78.97 mins             |
|                                     |               | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 383.22 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 11.98 mins               | 383.22 mins            |
| datafuselabs/databend-perf          | 923.95 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 46.51 mins               | 744.13 mins            |
|                                     |               | pages build and deployment          | 0.76 mins                | 4.53 mins              |
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
| pingcap/tidb                       | 6700.58 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 25.42 mins               | 25.42 mins             |
|                                    |               | BR & Lightning                                       | 1.19 mins                | 846.37 mins            |
|                                    |               | Dumpling                                             | 8.82 mins                | 5036.6 mins            |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.31 mins                | 776.13 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 153.18 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 4.79 mins                | 153.18 mins            |
| pingcap/kvproto                    | 1099.2 mins   |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 8.5 mins                 | 569.52 mins            |
|                                    |               | Golang Test                                          | 1.68 mins                | 112.57 mins            |
|                                    |               | Rust Test                                            | 6.23 mins                | 417.12 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5431.8 mins   |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.52 mins                | 3.13 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 69.42 mins             |
|                                    |               | external-link-check                                  | 4.59 mins                | 22.97 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 72.67 mins             |
|                                    |               | ci                                                   | 3.38 mins                | 4273.27 mins           |
|                                    |               | Links                                                | 2.19 mins                | 8.77 mins              |
|                                    |               | bot                                                  | 0.88 mins                | 19.42 mins             |
|                                    |               | cron                                                 | 1.23 mins                | 36.98 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.41 mins                | 483.97 mins            |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 441.22 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5882.02 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.46 mins                | 3.2 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 60.65 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 58.68 mins             |
|                                    |               | ci                                                   | 3.68 mins                | 4800.88 mins           |
|                                    |               | Links                                                | 2.58 mins                | 10.33 mins             |
|                                    |               | Flush PDF                                            | 0.26 mins                | 11.0 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.4 mins                 | 492.5 mins             |
|                                    |               | Prevent Deletion                                     | 0.33 mins                | 444.77 mins            |
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
| pingcap/tispark                    | 257.47 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 7.8 mins                 | 46.78 mins             |
|                                    |               | alter-primary-key-false-test                         | 5.21 mins                | 31.23 mins             |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 11.89 mins               | 118.87 mins            |
|                                    |               | Follower Read test                                   | 4.97 mins                | 29.83 mins             |
|                                    |               | Close inactive issues                                | 0.22 mins                | 6.55 mins              |
|                                    |               | License checker                                      | 0.81 mins                | 4.88 mins              |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 3.22 mins                | 19.32 mins             |
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
| pingcap/go-ycsb                    | 33.65 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.66 mins                | 18.6 mins              |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.15 mins                | 15.05 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 6572.9 mins   |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 23.19 mins               | 3223.2 mins            |
|                                    |               | ci                                                   | 20.38 mins               | 3342.6 mins            |
|                                    |               | Close stale issues/prs                               | 0.24 mins                | 7.1 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5022.23 mins  |                                                      |                          |                        |
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
| pingcap/tiflow                     | 43475.05 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.22 mins               | 12963.95 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.37 mins                | 8.22 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 4.91 mins                | 1030.73 mins           |
|                                    |               | DM Chaos                                             | 26.95 mins               | 5658.95 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.26 mins                | 145.77 mins            |
|                                    |               | DM Binlog 999999                                     | 12.36 mins               | 2595.42 mins           |
|                                    |               | Upstream Database Switch                             | 15.51 mins               | 3257.55 mins           |
|                                    |               | CDC Integration Tests                                | 17.2 mins                | 11629.08 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.14 mins                | 3.42 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 29.43 mins               | 6179.75 mins           |
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
