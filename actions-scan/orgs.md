
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 182.22 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 91.11 mins               | 182.22 mins            |
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
| webp-sh/webp_server_go     | 77.47 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.66 mins                | 14.65 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.28 mins               | 39.85 mins             |
|                            |               | CodeQL                          | 1.91 mins                | 22.97 mins             |
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
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 114261.03 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 95.4 mins                | 3243.53 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 74.43 mins               | 16672.05 mins          |
|                                     |                | Build Tool                          | 25.52 mins               | 76.57 mins             |
|                                     |                | Dev Linux                           | 21.81 mins               | 24532.4 mins           |
|                                     |                | Dev MacOS                           | 61.28 mins               | 68935.4 mins           |
|                                     |                | Unit Tests and Coverage             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless Cluster Tests             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test                                | 0.0 mins                 | 0.0 mins               |
|                                     |                | Binary Size Check                   | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful test(cluster)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Cluster              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Statful Standalone             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Unit                           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Build Debug                         | 0.0 mins                 | 0.0 mins               |
|                                     |                | Build Release                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Add issues into projects            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Crowdin Action                      | 2.96 mins                | 801.08 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 2761.53 mins   |                                     |                          |                        |
|                                     |                | ci                                  | 18.99 mins               | 2601.52 mins           |
|                                     |                | commit-message-check                | 0.78 mins                | 139.75 mins            |
|                                     |                | DevSkim                             | 0.83 mins                | 3.32 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 5.9 mins               |
|                                     |                | .github/workflows/issue-welcome.yml | 0.28 mins                | 4.98 mins              |
|                                     |                | .github/workflows/pages.yaml        | 0.36 mins                | 1.43 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 2.02 mins                | 2.02 mins              |
|                                     |                | pages build and deployment          | 0.65 mins                | 2.62 mins              |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 5.0 mins       |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.41 mins                | 2.05 mins              |
|                                     |                | pages build and deployment          | 0.59 mins                | 2.95 mins              |
| datafuselabs/databend-playground    | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 15706.55 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 43.25 mins               | 4844.43 mins           |
|                                     |                | Docs                                | 5.21 mins                | 619.55 mins            |
|                                     |                | Add issues into projects            | 0.24 mins                | 5.22 mins              |
|                                     |                | Service Test Azblob                 | 6.77 mins                | 758.5 mins             |
|                                     |                | Service Test Fs                     | 32.53 mins               | 3643.28 mins           |
|                                     |                | Service Test HDFS                   | 7.58 mins                | 849.12 mins            |
|                                     |                | Service Test HTTP                   | 34.22 mins               | 3456.7 mins            |
|                                     |                | Service Test Memory                 | 6.13 mins                | 686.87 mins            |
|                                     |                | Service Test S3                     | 7.53 mins                | 842.88 mins            |
| datafuselabs/opensrv                | 266.75 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 8.08 mins                | 266.75 mins            |
| datafuselabs/databend-perf          | 801.77 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 20.38 mins               | 611.28 mins            |
|                                     |                | Reload                              | 9.85 mins                | 177.3 mins             |
|                                     |                | pages build and deployment          | 0.66 mins                | 13.18 mins             |
| datafuselabs/helm-charts            | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/parquet2               | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 44.0 mins      |                                     |                          |                        |
|                                     |                | CI                                  | 10.68 mins               | 42.73 mins             |
|                                     |                | .github/workflows/pages.yml         | 0.3 mins                 | 0.6 mins               |
|                                     |                | pages build and deployment          | 0.67 mins                | 0.67 mins              |
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
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb                       | 25797.18 mins  |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/codeql-analysis.yml                | 0.0 mins                 | 0.0 mins               |
|                                    |                | License checker                                      | 4.24 mins                | 16929.05 mins          |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 12.38 mins               | 1027.53 mins           |
|                                    |                | BR & Lightning                                       | 1.13 mins                | 929.52 mins            |
|                                    |                | Dumpling                                             | 11.48 mins               | 6670.68 mins           |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull request labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 98.27 mins     |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 7.02 mins                | 98.27 mins             |
| pingcap/kvproto                    | 483.27 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 4.69 mins                | 150.22 mins            |
|                                    |                | Golang Test                                          | 2.89 mins                | 92.38 mins             |
|                                    |                | Rust Test                                            | 7.52 mins                | 240.67 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 9092.78 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 14.82 mins               | 266.83 mins            |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 4.48 mins                | 1093.67 mins           |
|                                    |                | external-link-check                                  | 14.96 mins               | 44.87 mins             |
|                                    |                | Automatic Rebase                                     | 0.07 mins                | 105.62 mins            |
|                                    |                | ci                                                   | 5.97 mins                | 7320.15 mins           |
|                                    |                | Links                                                | 0.65 mins                | 2.58 mins              |
|                                    |                | bot                                                  | 0.81 mins                | 18.62 mins             |
|                                    |                | cron                                                 | 2.07 mins                | 62.08 mins             |
|                                    |                | Links (Fail Fast)                                    | 1.56 mins                | 178.37 mins            |
|                                    |                | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5888.8 mins    |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 1.74 mins                | 10.43 mins             |
|                                    |                | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 1.31 mins                | 284.23 mins            |
|                                    |                | external-link-check                                  | 20.2 mins                | 20.2 mins              |
|                                    |                | Automatic Rebase                                     | 0.05 mins                | 74.27 mins             |
|                                    |                | ci                                                   | 4.24 mins                | 5484.92 mins           |
|                                    |                | Links                                                | 1.3 mins                 | 5.22 mins              |
|                                    |                | Flush PDF                                            | 0.31 mins                | 9.53 mins              |
| pingcap/tidb-binlog                | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
|                                    |                | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Links                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
|                                    |                | Merge Schedule                                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | links                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins       |                                                      |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins       |                                                      |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/blog-cn                    | 0.95 mins      |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog-cn             | 0.47 mins                | 0.95 mins              |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark                    | 22802.13 mins  |                                                      |                          |                        |
|                                    |                | TLS test                                             | 18.27 mins               | 5918.98 mins           |
|                                    |                | alter-primary-key-false-test                         | 13.16 mins               | 2829.32 mins           |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 21.81 mins               | 7152.42 mins           |
|                                    |                | Close inactive issues                                | 0.27 mins                | 8.1 mins               |
|                                    |                | License checker                                      | 7.66 mins                | 2488.18 mins           |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 13.55 mins               | 4405.13 mins           |
| pingcap/octopus                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/grpc                       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | PR AutoFix                                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/jepsen                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins       |                                                      |                          |                        |
| pingcap/chaos                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/meetup                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins       |                                                      |                          |                        |
| pingcap/campaign                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/community                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-vision                | 0.0 mins       |                                                      |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins       |                                                      |                          |                        |
| pingcap/tla-plus                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-ycsb                    | 90.23 mins     |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 3.16 mins                | 50.53 mins             |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 2.48 mins                | 39.7 mins              |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 7.58 mins      |                                                      |                          |                        |
|                                    |                | testbuild                                            | 2.53 mins                | 7.58 mins              |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 11562.65 mins  |                                                      |                          |                        |
|                                    |                | ci                                                   | 22.07 mins               | 4921.23 mins           |
|                                    |                | chaos                                                | 33.67 mins               | 6632.1 mins            |
|                                    |                | Close stale issues/prs                               | 0.31 mins                | 9.32 mins              |
|                                    |                |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 2225.58 mins   |                                                      |                          |                        |
|                                    |                | Pull Request CI                                      | 13.7 mins                | 137.02 mins            |
|                                    |                | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins       |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                                      |                          |                        |
| pingcap/dm                         | 3573.55 mins   |                                                      |                          |                        |
|                                    |                | Test binlog 999999                                   | 41.49 mins               | 331.95 mins            |
|                                    |                | chaos                                                | 26.55 mins               | 2548.98 mins           |
|                                    |                | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                                     | 46.96 mins               | 375.72 mins            |
|                                    |                | Upstream database switch                             | 39.61 mins               | 316.9 mins             |
| pingcap/talent-plan                | 0.0 mins       |                                                      |                          |                        |
| pingcap/log                        | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 2482.8 mins    |                                                      |                          |                        |
|                                    |                | License checker                                      | 2.94 mins                | 2482.8 mins            |
|                                    |                | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | Bug Closed                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/capnproto                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/boost-extra                | 0.0 mins       |                                                      |                          |                        |
| pingcap/kdt                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/failpoint                  | 10.22 mins     |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build & Test                                         | 1.7 mins                 | 10.22 mins             |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins       |                                                      |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidiff                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/fn                         | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqlsmith                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                                      |                          |                        |
| pingcap/tiflow                     | 261825.87 mins |                                                      |                          |                        |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 92.39 mins               | 184406.78 mins         |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Design Docs Lint                                     | 12.59 mins               | 151.13 mins            |
|                                    |                | Upgrade DM via TiUP                                  | 6.33 mins                | 1342.53 mins           |
|                                    |                | DM Chaos                                             | 32.81 mins               | 6923.33 mins           |
|                                    |                | Auto Assign to Bugs and Questions                    | 14.75 mins               | 11477.52 mins          |
|                                    |                | DM Binlog 999999                                     | 12.38 mins               | 2599.22 mins           |
|                                    |                | Upstream Database Switch                             | 11.85 mins               | 2512.5 mins            |
|                                    |                | CDC Integration Tests                                | 21.7 mins                | 27255.4 mins           |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Web UI Lint                                       | 1.61 mins                | 4.83 mins              |
|                                    |                | Dataflow Engine e2e tests                            | 20.22 mins               | 20015.4 mins           |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 21.15 mins               | 4948.97 mins           |
| pingcap/br                         | 50.6 mins      |                                                      |                          |                        |
|                                    |                | build                                                | 9.58 mins                | 28.75 mins             |
|                                    |                | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                                   | 7.28 mins                | 21.85 mins             |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-tpc                     | 5.45 mins      |                                                      |                          |                        |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | workflow                                             | 1.09 mins                | 5.45 mins              |
| pingcap/kops                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/sysutil                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Test                                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins       |                                                      |                          |                        |
|                                    |                | (experimental) Ember CLI tests (core)                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Linting                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Tests                                                | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse-chat-integration | 0.0 mins       |                                                      |                          |                        |
| pingcap/discourse_docker           | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-helper                | 0.0 mins       |                                                      |                          |                        |
| pingcap/dumpling                   | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tipocket                   | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build-image                                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build-workflow                                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pre-Check                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Test                                                 | 0.0 mins                 | 0.0 mins               |
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
