
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
| webp-sh/webp_server_go     | 145.5 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 2.99 mins                | 29.88 mins             |
|                            |               | Release Binaries                | 2.67 mins                | 2.67 mins              |
|                            |               | Build and release docker images | 10.35 mins               | 72.43 mins             |
|                            |               | CodeQL                          | 2.03 mins                | 40.52 mins             |
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
| datafuselabs/databend               | 90481.27 mins |                                            |                          |                        |
|                                     |               | Unit Tests                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                                    | 90.44 mins               | 2260.88 mins           |
|                                     |               | License checker                            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                                 | 86.01 mins               | 19008.63 mins          |
|                                     |               | Build Tool                                 | 31.42 mins               | 31.42 mins             |
|                                     |               | Dev Linux                                  | 19.68 mins               | 19816.17 mins          |
|                                     |               | Dev MacOS                                  | 48.64 mins               | 48978.93 mins          |
|                                     |               | Backport                                   | 69.41 mins               | 208.23 mins            |
|                                     |               | Dev Perf                                   | 17.7 mins                | 177.0 mins             |
|                                     |               | Stateless(Cluster)                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                            |                          |                        |
| datafuselabs/openraft               | 1638.15 mins  |                                            |                          |                        |
|                                     |               | chaos-test                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                         | 19.9 mins                | 1452.6 mins            |
|                                     |               | commit-message-check                       | 2.19 mins                | 115.87 mins            |
|                                     |               | Unit test coverage                         | 7.23 mins                | 65.08 mins             |
|                                     |               | DevSkim                                    | 0.87 mins                | 4.35 mins              |
|                                     |               | .github/workflows/issue-cmds.yml           | 0.05 mins                | 0.05 mins              |
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
| datafuselabs/opendal                | 40649.17 mins |                                            |                          |                        |
|                                     |               | CI                                         | 17.47 mins               | 4350.55 mins           |
|                                     |               | Service Test S3                            | 9.24 mins                | 2318.02 mins           |
|                                     |               | Service Test Fs                            | 5.12 mins                | 1285.67 mins           |
|                                     |               | Docs                                       | 13.56 mins               | 2928.07 mins           |
|                                     |               | Service Test Memory                        | 5.4 mins                 | 1354.87 mins           |
|                                     |               | Service Test Azblob                        | 5.46 mins                | 1370.55 mins           |
|                                     |               | Service Test HDFS                          | 6.48 mins                | 1606.67 mins           |
|                                     |               | Service Test HTTP                          | 6.67 mins                | 1673.1 mins            |
|                                     |               | Service Test Gcs                           | 6.16 mins                | 1545.38 mins           |
|                                     |               | Test Vault                                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Obs                           | 7.73 mins                | 1938.98 mins           |
|                                     |               | Service Test IPMFS                         | 4.95 mins                | 1243.25 mins           |
|                                     |               | Service Test Ftp                           | 10.23 mins               | 2567.15 mins           |
|                                     |               | Service Test Redis                         | 5.53 mins                | 1388.2 mins            |
|                                     |               | Service Test Oss                           | 7.83 mins                | 1964.93 mins           |
|                                     |               | Service Test Moka                          | 5.36 mins                | 1345.38 mins           |
|                                     |               | Service Test RocksDB                       | 12.46 mins               | 3127.67 mins           |
|                                     |               | Service Test Azdfs                         | 6.3 mins                 | 1581.68 mins           |
|                                     |               | Service Test Ghac                          | 5.68 mins                | 1426.03 mins           |
|                                     |               | A Test                                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test Memcached                     | 5.33 mins                | 1102.37 mins           |
|                                     |               | Benchmark                                  | 22.06 mins               | 816.4 mins             |
|                                     |               | pages build and deployment                 | 2.04 mins                | 77.42 mins             |
|                                     |               | Bindings Python CI                         | 23.91 mins               | 3132.0 mins            |
|                                     |               | Service Test WebDAV                        | 6.81 mins                | 490.67 mins            |
|                                     |               | .github/workflows/service_test_webhdfs.yml | 0.0 mins                 | 0.0 mins               |
|                                     |               | Service Test HDFS and WebHDFS              | 4.72 mins                | 14.17 mins             |
|                                     |               | Service Test IPFS                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 312.87 mins   |                                            |                          |                        |
|                                     |               | CI                                         | 9.78 mins                | 312.87 mins            |
| datafuselabs/databend-perf          | 523.73 mins   |                                            |                          |                        |
|                                     |               | Perf                                       | 30.89 mins               | 339.77 mins            |
|                                     |               | pages build and deployment                 | 0.71 mins                | 4.27 mins              |
|                                     |               | Reload tpch                                | 9.97 mins                | 59.85 mins             |
|                                     |               | Reload hits                                | 12.22 mins               | 73.33 mins             |
|                                     |               | Reload ontime                              | 9.3 mins                 | 46.52 mins             |
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
| pingcap/tidb                       | 9411.43 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 20.73 mins               | 103.63 mins            |
|                                    |               | BR & Lightning                                       | 1.14 mins                | 520.78 mins            |
|                                    |               | Dumpling                                             | 8.96 mins                | 3725.97 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.81 mins                | 5061.05 mins           |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 169.42 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 4.34 mins                | 169.42 mins            |
| pingcap/kvproto                    | 1237.23 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 4.75 mins                | 460.27 mins            |
|                                    |               | Golang Test                                          | 2.02 mins                | 195.65 mins            |
|                                    |               | Rust Test                                            | 5.99 mins                | 581.32 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 6491.3 mins   |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.28 mins                | 14.1 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.55 mins                | 220.92 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 78.35 mins             |
|                                    |               | ci                                                   | 4.21 mins                | 4525.18 mins           |
|                                    |               | Links                                                | 2.06 mins                | 8.25 mins              |
|                                    |               | bot                                                  | 0.91 mins                | 19.12 mins             |
|                                    |               | cron                                                 | 1.05 mins                | 31.37 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.82 mins                | 749.47 mins            |
|                                    |               | Prevent Deletion                                     | 0.77 mins                | 844.55 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5062.72 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.77 mins                | 8.5 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.2 mins                 | 63.78 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 61.02 mins             |
|                                    |               | ci                                                   | 3.43 mins                | 3953.97 mins           |
|                                    |               | Links                                                | 3.47 mins                | 17.35 mins             |
|                                    |               | Flush PDF                                            | 0.26 mins                | 8.25 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.52 mins                | 556.65 mins            |
|                                    |               | Prevent Deletion                                     | 0.34 mins                | 393.2 mins             |
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
| pingcap/tispark                    | 969.15 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 12.16 mins               | 218.93 mins            |
|                                    |               | alter-primary-key-false-test                         | 8.28 mins                | 148.97 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 13.4 mins                | 308.3 mins             |
|                                    |               | Follower Read test                                   | 8.49 mins                | 152.82 mins            |
|                                    |               | Close inactive issues                                | 0.23 mins                | 7.0 mins               |
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
| pingcap/tidb-operator              | 3742.45 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 23.53 mins               | 1905.97 mins           |
|                                    |               | ci                                                   | 17.93 mins               | 1828.73 mins           |
|                                    |               | Close stale issues/prs                               | 0.26 mins                | 7.75 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 3140.22 mins  |                                                      |                          |                        |
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
| pingcap/tiflow                     | 35922.78 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.06 mins               | 8719.73 mins           |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.37 mins                | 8.22 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 5.02 mins                | 1054.3 mins            |
|                                    |               | DM Chaos                                             | 28.44 mins               | 5972.3 mins            |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.4 mins                 | 132.3 mins             |
|                                    |               | DM Binlog 999999                                     | 12.21 mins               | 2564.95 mins           |
|                                    |               | Upstream Database Switch                             | 14.84 mins               | 3117.32 mins           |
|                                    |               | CDC Integration Tests                                | 16.98 mins               | 8097.68 mins           |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.41 mins                | 8.45 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 29.75 mins               | 6247.53 mins           |
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
