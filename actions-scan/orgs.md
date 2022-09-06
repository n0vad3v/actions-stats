
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 581.95 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 193.98 mins              | 581.95 mins            |
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
    
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                       | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node   | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go     | 155.22 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.19 mins                | 35.07 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.19 mins               | 79.12 mins             |
|                            |               | CodeQL                          | 1.95 mins                | 41.03 mins             |
| webp-sh/webp               | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java   | 0.0 mins      |                                 |                          |                        |
|                            |               | dev                             | 0.0 mins                 | 0.0 mins               |
|                            |               | release                         | 0.0 mins                 | 0.0 mins               |
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
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 97744.73 mins |                                     |                          |                        |
|                                     |               | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 95.28 mins               | 4287.55 mins           |
|                                     |               | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 79.05 mins               | 16126.37 mins          |
|                                     |               | Build Tool                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Dev Linux                           | 22.88 mins               | 23496.62 mins          |
|                                     |               | Dev MacOS                           | 52.34 mins               | 53757.22 mins          |
|                                     |               | Unit Tests and Coverage             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless Cluster Tests             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test                                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Binary Size Check                   | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful test(cluster)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Stateless Cluster              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Statful Standalone             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Test Unit                           | 0.0 mins                 | 0.0 mins               |
|                                     |               | Build Debug                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | Build Release                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Crowdin Action                      | 3.21 mins                | 76.98 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 2134.88 mins  |                                     |                          |                        |
|                                     |               | ci                                  | 13.47 mins               | 1791.73 mins           |
|                                     |               | commit-message-check                | 1.4 mins                 | 229.32 mins            |
|                                     |               | Unit test coverage                  | 7.46 mins                | 89.47 mins             |
|                                     |               | DevSkim                             | 0.77 mins                | 3.07 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.05 mins                | 2.35 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.39 mins                | 3.08 mins              |
|                                     |               | .github/workflows/pages.yaml        | 0.36 mins                | 1.82 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 1.82 mins                | 10.93 mins             |
|                                     |               | pages build and deployment          | 0.62 mins                | 3.12 mins              |
| datafuselabs/fusebots               | 0.0 mins      |                                     |                          |                        |
|                                     |               | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 4.15 mins     |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.41 mins                | 1.65 mins              |
|                                     |               | pages build and deployment          | 0.62 mins                | 2.5 mins               |
| datafuselabs/databend-playground    | 0.0 mins      |                                     |                          |                        |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 19338.0 mins  |                                     |                          |                        |
|                                     |               | CI                                  | 13.22 mins               | 3820.67 mins           |
|                                     |               | Service Test S3                     | 6.84 mins                | 1991.58 mins           |
|                                     |               | Service Test Fs                     | 8.12 mins                | 2362.65 mins           |
|                                     |               | Docs                                | 4.33 mins                | 923.28 mins            |
|                                     |               | Service Test Memory                 | 5.05 mins                | 1469.6 mins            |
|                                     |               | Service Test Azblob                 | 5.48 mins                | 1594.05 mins           |
|                                     |               | Service Test HDFS                   | 6.55 mins                | 1906.47 mins           |
|                                     |               | Service Test HTTP                   | 11.0 mins                | 3201.88 mins           |
|                                     |               | Service Test Gcs                    | 5.7 mins                 | 1282.32 mins           |
|                                     |               | Test Vault                          | 2.42 mins                | 7.25 mins              |
|                                     |               | Service Test Obs                    | 5.78 mins                | 768.62 mins            |
|                                     |               | Service Test IPFS                   | 3.21 mins                | 9.63 mins              |
| datafuselabs/opensrv                | 419.82 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 10.24 mins               | 419.82 mins            |
| datafuselabs/databend-perf          | 769.95 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 10.49 mins               | 535.1 mins             |
|                                     |               | pages build and deployment          | 0.59 mins                | 10.07 mins             |
|                                     |               | Reload tpch                         | 5.66 mins                | 50.9 mins              |
|                                     |               | Reload hits                         | 13.03 mins               | 13.03 mins             |
|                                     |               | Reload ontime                       | 0.13 mins                | 0.13 mins              |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins      |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/parquet2               | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tidb                       | 11874.07 mins |                                                      |                          |                        |
|                                    |               | .github/workflows/codeql-analysis.yml                | 0.0 mins                 | 0.0 mins               |
|                                    |               | License checker                                      | 3.15 mins                | 8339.47 mins           |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 10.43 mins               | 417.03 mins            |
|                                    |               | BR & Lightning                                       | 1.11 mins                | 431.02 mins            |
|                                    |               | Dumpling                                             | 8.08 mins                | 2559.87 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.58 mins                | 48.97 mins             |
|                                    |               | Leaked Secrets Scan                                  | 2.51 mins                | 7.52 mins              |
|                                    |               | Pull request labeler                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 42.48 mins    |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 6.07 mins                | 42.48 mins             |
| pingcap/kvproto                    | 1257.82 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.48 mins                | 505.52 mins            |
|                                    |               | Golang Test                                          | 2.37 mins                | 184.68 mins            |
|                                    |               | Rust Test                                            | 7.28 mins                | 567.62 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 9824.87 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.79 mins                | 51.93 mins             |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 1.81 mins                | 530.42 mins            |
|                                    |               | external-link-check                                  | 11.31 mins               | 33.92 mins             |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 93.73 mins             |
|                                    |               | ci                                                   | 5.44 mins                | 6967.85 mins           |
|                                    |               | Links                                                | 0.75 mins                | 4.48 mins              |
|                                    |               | bot                                                  | 0.79 mins                | 17.28 mins             |
|                                    |               | cron                                                 | 2.38 mins                | 71.47 mins             |
|                                    |               | Links (Fail Fast)                                    | 1.38 mins                | 1436.78 mins           |
|                                    |               | Prevent Deletion                                     | 1.57 mins                | 617.0 mins             |
|                                    |               | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5797.3 mins   |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.4 mins                 | 16.83 mins             |
|                                    |               | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 1.74 mins                | 424.87 mins            |
|                                    |               | external-link-check                                  | 6.73 mins                | 6.73 mins              |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 73.83 mins             |
|                                    |               | ci                                                   | 4.8 mins                 | 4369.0 mins            |
|                                    |               | Links                                                | 2.53 mins                | 40.45 mins             |
|                                    |               | Flush PDF                                            | 0.34 mins                | 11.33 mins             |
|                                    |               | Links (Fail Fast)                                    | 1.18 mins                | 596.43 mins            |
|                                    |               | Prevent Deletion                                     | 1.66 mins                | 257.82 mins            |
| pingcap/tidb-binlog                | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tispark                    | 9479.53 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 15.35 mins               | 2348.5 mins            |
|                                    |               | alter-primary-key-false-test                         | 10.72 mins               | 1640.22 mins           |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 17.29 mins               | 2714.73 mins           |
|                                    |               | Close inactive issues                                | 0.28 mins                | 8.38 mins              |
|                                    |               | License checker                                      | 4.52 mins                | 692.07 mins            |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 13.57 mins               | 2075.63 mins           |
| pingcap/octopus                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/grpc                       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | PR AutoFix                                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/jepsen                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins      |                                                      |                          |                        |
| pingcap/chaos                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/meetup                     | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
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
| pingcap/go-ycsb                    | 17.05 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.98 mins                | 11.93 mins             |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 1.28 mins                | 5.12 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 2.65 mins     |                                                      |                          |                        |
|                                    |               | testbuild                                            | 1.08 mins                | 1.08 mins              |
|                                    |               | release                                              | 1.57 mins                | 1.57 mins              |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 9660.18 mins  |                                                      |                          |                        |
|                                    |               | ci                                                   | 34.71 mins               | 3367.27 mins           |
|                                    |               | chaos                                                | 70.62 mins               | 6284.83 mins           |
|                                    |               | Close stale issues/prs                               | 0.27 mins                | 8.08 mins              |
|                                    |               |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5514.53 mins  |                                                      |                          |                        |
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
| pingcap/tiflash                    | 2474.68 mins  |                                                      |                          |                        |
|                                    |               | License checker                                      | 2.51 mins                | 2474.68 mins           |
|                                    |               | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Bug Closed                                           | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tiflow                     | 77107.03 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 18.66 mins               | 25998.68 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 11.42 mins               | 91.33 mins             |
|                                    |               | Upgrade DM via TiUP                                  | 5.26 mins                | 1121.13 mins           |
|                                    |               | DM Chaos                                             | 29.07 mins               | 6279.98 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 3.7 mins                 | 2244.58 mins           |
|                                    |               | DM Binlog 999999                                     | 11.69 mins               | 2467.37 mins           |
|                                    |               | Upstream Database Switch                             | 15.52 mins               | 3260.03 mins           |
|                                    |               | CDC Integration Tests                                | 19.56 mins               | 17467.47 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 5.32 mins                | 63.82 mins             |
|                                    |               | Dataflow Engine e2e tests                            | 18.4 mins                | 13763.55 mins          |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 20.06 mins               | 4273.37 mins           |
| pingcap/br                         | 0.0 mins      |                                                      |                          |                        |
|                                    |               | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 17.18 mins    |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.15 mins                | 17.18 mins             |
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
|                                    |               |                                                      | 0.0 mins                 | 0.0 mins               |
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
