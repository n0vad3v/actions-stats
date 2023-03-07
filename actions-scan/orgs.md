
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
| webp-sh/webp_server_go     | 302.27 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.57 mins                | 53.5 mins              |
|                            |               | Release Binaries                | 2.86 mins                | 5.72 mins              |
|                            |               | Build and release docker images | 17.19 mins               | 189.08 mins            |
|                            |               | CodeQL                          | 1.93 mins                | 53.97 mins             |
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
Error: {'total_count': 100, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 126923.45 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 106.34 mins              | 4997.87 mins           |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 82.45 mins               | 22838.88 mins          |
|                                     |                | Build Tool                          | 31.82 mins               | 95.47 mins             |
|                                     |                | Dev Linux                           | 19.15 mins               | 24345.6 mins           |
|                                     |                | Dev MacOS                           | 55.48 mins               | 70515.35 mins          |
|                                     |                | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Debug                               | 0.41 mins                | 6.1 mins               |
|                                     |                | Benchmark                           | 3.11 mins                | 3798.77 mins           |
|                                     |                | Benchmark Commentator (trusted)     | 0.1 mins                 | 116.68 mins            |
|                                     |                | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |                | Typos Check                         | 0.7 mins                 | 204.45 mins            |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 9503.37 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 52.45 mins               | 7867.78 mins           |
|                                     |                | commit-message-check                | 6.26 mins                | 1076.52 mins           |
|                                     |                | Unit test coverage                  | 8.5 mins                 | 365.33 mins            |
|                                     |                | DevSkim                             | 0.83 mins                | 3.32 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 1.17 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 5.0 mins                 | 55.05 mins             |
|                                     |                | .github/workflows/pages.yaml        | 3.73 mins                | 22.35 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 7.87 mins                | 31.48 mins             |
|                                     |                | pages build and deployment          | 13.39 mins               | 80.37 mins             |
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
| datafuselabs/opendal                | 92646.78 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 20.77 mins               | 9053.78 mins           |
|                                     |                | Service Test S3                     | 11.81 mins               | 3780.2 mins            |
|                                     |                | Service Test Fs                     | 10.57 mins               | 3371.15 mins           |
|                                     |                | Service Test Memory                 | 8.21 mins                | 2619.72 mins           |
|                                     |                | Service Test Azblob                 | 8.63 mins                | 2761.78 mins           |
|                                     |                | Service Test HDFS                   | 10.43 mins               | 3327.58 mins           |
|                                     |                | Service Test HTTP                   | 10.79 mins               | 3442.43 mins           |
|                                     |                | Service Test Gcs                    | 9.54 mins                | 3053.35 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Obs                    | 11.25 mins               | 3601.33 mins           |
|                                     |                | Service Test IPMFS                  | 9.06 mins                | 2898.35 mins           |
|                                     |                | Service Test Ftp                    | 13.9 mins                | 4461.55 mins           |
|                                     |                | Service Test Redis                  | 9.1 mins                 | 2901.78 mins           |
|                                     |                | Service Test Oss                    | 10.79 mins               | 3464.58 mins           |
|                                     |                | Service Test Moka                   | 9.01 mins                | 2875.02 mins           |
|                                     |                | Service Test RocksDB                | 16.48 mins               | 5256.78 mins           |
|                                     |                | Service Test Azdfs                  | 9.59 mins                | 3067.22 mins           |
|                                     |                | Service Test Ghac                   | 9.57 mins                | 3062.67 mins           |
|                                     |                | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Memcached              | 8.65 mins                | 2759.4 mins            |
|                                     |                | pages build and deployment          | 4.03 mins                | 447.57 mins            |
|                                     |                | Bindings Python CI                  | 27.51 mins               | 12161.13 mins          |
|                                     |                | Service Test WebDAV                 | 15.11 mins               | 5062.83 mins           |
|                                     |                | Service Test WebHDFS                | 10.49 mins               | 2946.93 mins           |
|                                     |                | Service Test HDFS and WebHDFS       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Sled                   | 9.4 mins                 | 2275.95 mins           |
|                                     |                | Service Test Dashmap                | 8.32 mins                | 823.3 mins             |
|                                     |                | Benchmark                           | 21.57 mins               | 754.93 mins            |
|                                     |                | Docs                                | 14.97 mins               | 1497.15 mins           |
|                                     |                | Typos Check                         | 3.51 mins                | 579.17 mins            |
|                                     |                | Binding NodeJS CI                   | 3.94 mins                | 339.13 mins            |
|                                     |                | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 549.13 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 15.25 mins               | 549.13 mins            |
| datafuselabs/databend-perf          | 1918.28 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 110.15 mins              | 1762.37 mins           |
|                                     |                | pages build and deployment          | 1.05 mins                | 7.38 mins              |
|                                     |                | Reload tpch                         | 12.37 mins               | 61.85 mins             |
|                                     |                | Reload hits                         | 13.35 mins               | 53.38 mins             |
|                                     |                | Reload ontime                       | 8.32 mins                | 33.3 mins              |
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
| pingcap/tidb                       | 5625.27 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 12.57 mins               | 12.57 mins             |
|                                    |               | BR & Lightning                                       | 1.24 mins                | 857.12 mins            |
|                                    |               | Dumpling                                             | 9.03 mins                | 4137.03 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.88 mins                | 602.48 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 153.43 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.68 mins                | 153.43 mins            |
| pingcap/kvproto                    | 1278.08 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 7.2 mins                 | 575.92 mins            |
|                                    |               | Golang Test                                          | 1.82 mins                | 145.58 mins            |
|                                    |               | Rust Test                                            | 6.96 mins                | 556.58 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5644.6 mins   |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.5 mins                 | 6.03 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 79.58 mins             |
|                                    |               | external-link-check                                  | 3.73 mins                | 26.13 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 82.33 mins             |
|                                    |               | ci                                                   | 3.5 mins                 | 4416.37 mins           |
|                                    |               | Links                                                | 2.17 mins                | 10.87 mins             |
|                                    |               | bot                                                  | 0.83 mins                | 18.32 mins             |
|                                    |               | cron                                                 | 1.31 mins                | 39.37 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.43 mins                | 510.5 mins             |
|                                    |               | Prevent Deletion                                     | 0.36 mins                | 455.1 mins             |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5791.02 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.43 mins                | 6.87 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 73.93 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 77.45 mins             |
|                                    |               | ci                                                   | 4.22 mins                | 4760.9 mins            |
|                                    |               | Links                                                | 1.74 mins                | 8.7 mins               |
|                                    |               | Flush All PDF                                        | 0.26 mins                | 10.5 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.42 mins                | 445.13 mins            |
|                                    |               | Prevent Deletion                                     | 0.35 mins                | 407.25 mins            |
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
| pingcap/tispark                    | 1317.48 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.0 mins                | 286.08 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.22 mins                | 202.93 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 17.4 mins                | 452.35 mins            |
|                                    |               | Follower Read test                                   | 9.64 mins                | 212.13 mins            |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.88 mins              |
|                                    |               | License checker                                      | 1.13 mins                | 24.92 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 6.01 mins                | 132.18 mins            |
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
| pingcap/tidb-operator              | 8884.98 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 22.72 mins               | 4475.13 mins           |
|                                    |               | ci                                                   | 19.83 mins               | 4402.52 mins           |
|                                    |               | Close stale issues/prs                               | 0.24 mins                | 7.33 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 6363.97 mins  |                                                      |                          |                        |
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
| pingcap/diag                       | 103.33 mins   |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.11 mins               | 77.78 mins             |
|                                    |               | static-tests                                         | 3.19 mins                | 25.55 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 51476.63 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.92 mins               | 16878.13 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.53 mins                | 20.52 mins             |
|                                    |               | Upgrade DM via TiUP                                  | 5.28 mins                | 1107.75 mins           |
|                                    |               | DM Chaos                                             | 28.16 mins               | 5912.78 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.27 mins                | 184.22 mins            |
|                                    |               | DM Binlog 999999                                     | 13.88 mins               | 2914.07 mins           |
|                                    |               | Upstream Database Switch                             | 15.4 mins                | 3234.72 mins           |
|                                    |               | CDC Integration Tests                                | 17.62 mins               | 14498.38 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 2.25 mins                | 2.25 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 32.01 mins               | 6721.6 mins            |
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
| pingcap/go-tpc                     | 2.82 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.41 mins                | 2.82 mins              |
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
    
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
