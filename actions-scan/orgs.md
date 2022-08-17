
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 166.83 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 166.83 mins              | 166.83 mins            |
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
| webp-sh/webp_server_go     | 199.33 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.28 mins                | 42.63 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.25 mins               | 105.97 mins            |
|                            |               | CodeQL                          | 1.95 mins                | 50.73 mins             |
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
| datafuselabs/databend               | 105023.67 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 92.64 mins               | 3520.23 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 71.88 mins               | 15381.68 mins          |
|                                     |                | Build Tool                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Dev Linux                           | 21.41 mins               | 23659.42 mins          |
|                                     |                | Dev MacOS                           | 55.92 mins               | 61788.23 mins          |
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
|                                     |                | Crowdin Action                      | 3.0 mins                 | 674.1 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 2647.55 mins   |                                     |                          |                        |
|                                     |                | ci                                  | 17.04 mins               | 2487.48 mins           |
|                                     |                | commit-message-check                | 0.78 mins                | 141.1 mins             |
|                                     |                | DevSkim                             | 0.78 mins                | 3.12 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 5.58 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.27 mins                | 4.58 mins              |
|                                     |                | .github/workflows/pages.yaml        | 0.34 mins                | 0.68 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 1.89 mins                | 3.78 mins              |
|                                     |                | pages build and deployment          | 0.61 mins                | 1.22 mins              |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 3.93 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.4 mins                 | 1.58 mins              |
|                                     |                | pages build and deployment          | 0.59 mins                | 2.35 mins              |
| datafuselabs/databend-playground    | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 21756.22 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 36.43 mins               | 6557.57 mins           |
|                                     |                | Docs                                | 4.87 mins                | 813.17 mins            |
|                                     |                | Add issues into projects            | 0.45 mins                | 13.87 mins             |
|                                     |                | Service Test Azblob                 | 6.14 mins                | 1104.65 mins           |
|                                     |                | Service Test Fs                     | 26.88 mins               | 4839.03 mins           |
|                                     |                | Service Test Gcs                    | 4.73 mins                | 23.63 mins             |
|                                     |                | Service Test HDFS                   | 6.97 mins                | 1254.43 mins           |
|                                     |                | Service Test HTTP                   | 28.91 mins               | 4915.5 mins            |
|                                     |                | Service Test Memory                 | 5.58 mins                | 1003.92 mins           |
|                                     |                | Service Test S3                     | 6.84 mins                | 1230.45 mins           |
| datafuselabs/opensrv                | 366.13 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 8.93 mins                | 366.13 mins            |
| datafuselabs/databend-perf          | 667.53 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 16.73 mins               | 535.32 mins            |
|                                     |                | Reload                              | 9.33 mins                | 121.28 mins            |
|                                     |                | pages build and deployment          | 0.64 mins                | 10.93 mins             |
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
| pingcap/tidb                       | 22640.27 mins  |                                                      |                          |                        |
|                                    |                | .github/workflows/codeql-analysis.yml                | 0.0 mins                 | 0.0 mins               |
|                                    |                | License checker                                      | 4.21 mins                | 15515.92 mins          |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 12.02 mins               | 973.6 mins             |
|                                    |                | BR & Lightning                                       | 1.11 mins                | 888.03 mins            |
|                                    |                | Dumpling                                             | 11.88 mins               | 5122.2 mins            |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull request labeler                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 75.1 mins      |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 7.51 mins                | 75.1 mins              |
| pingcap/kvproto                    | 481.72 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 5.01 mins                | 150.2 mins             |
|                                    |                | Golang Test                                          | 3.22 mins                | 96.55 mins             |
|                                    |                | Rust Test                                            | 7.83 mins                | 234.97 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 11072.13 mins  |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 10.59 mins               | 285.92 mins            |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 4.53 mins                | 1221.92 mins           |
|                                    |                | external-link-check                                  | 14.96 mins               | 44.87 mins             |
|                                    |                | Automatic Rebase                                     | 0.07 mins                | 121.68 mins            |
|                                    |                | ci                                                   | 5.99 mins                | 8610.28 mins           |
|                                    |                | Links                                                | 0.69 mins                | 2.75 mins              |
|                                    |                | bot                                                  | 0.81 mins                | 17.75 mins             |
|                                    |                | cron                                                 | 2.01 mins                | 60.38 mins             |
|                                    |                | Links (Fail Fast)                                    | 1.72 mins                | 706.58 mins            |
|                                    |                | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5758.72 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 1.37 mins                | 12.33 mins             |
|                                    |                | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 1.34 mins                | 266.15 mins            |
|                                    |                | external-link-check                                  | 20.2 mins                | 20.2 mins              |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 69.42 mins             |
|                                    |                | ci                                                   | 4.2 mins                 | 5376.48 mins           |
|                                    |                | Links                                                | 1.21 mins                | 4.83 mins              |
|                                    |                | Flush PDF                                            | 0.3 mins                 | 9.3 mins               |
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
| pingcap/blog-cn                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog-cn             | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark                    | 20316.95 mins  |                                                      |                          |                        |
|                                    |                | TLS test                                             | 17.84 mins               | 4995.07 mins           |
|                                    |                | alter-primary-key-false-test                         | 12.97 mins               | 3191.63 mins           |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 21.38 mins               | 6070.87 mins           |
|                                    |                | Close inactive issues                                | 0.27 mins                | 8.08 mins              |
|                                    |                | License checker                                      | 7.4 mins                 | 2071.95 mins           |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 14.21 mins               | 3979.35 mins           |
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
| pingcap/go-ycsb                    | 82.32 mins     |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 3.37 mins                | 47.23 mins             |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 2.51 mins                | 35.08 mins             |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 7.58 mins      |                                                      |                          |                        |
|                                    |                | testbuild                                            | 2.53 mins                | 7.58 mins              |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 10975.98 mins  |                                                      |                          |                        |
|                                    |                | ci                                                   | 21.06 mins               | 4253.47 mins           |
|                                    |                | chaos                                                | 38.15 mins               | 6713.53 mins           |
|                                    |                | Close stale issues/prs                               | 0.3 mins                 | 8.98 mins              |
|                                    |                |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 2602.27 mins   |                                                      |                          |                        |
|                                    |                | Pull Request CI                                      | 13.7 mins                | 137.02 mins            |
|                                    |                | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins       |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                                      |                          |                        |
| pingcap/dm                         | 908.62 mins    |                                                      |                          |                        |
|                                    |                | Test binlog 999999                                   | 40.78 mins               | 81.57 mins             |
|                                    |                | chaos                                                | 27.05 mins               | 649.32 mins            |
|                                    |                | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                                     | 49.97 mins               | 99.93 mins             |
|                                    |                | Upstream database switch                             | 38.9 mins                | 77.8 mins              |
| pingcap/talent-plan                | 0.0 mins       |                                                      |                          |                        |
| pingcap/log                        | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 2368.7 mins    |                                                      |                          |                        |
|                                    |                | License checker                                      | 3.03 mins                | 2368.7 mins            |
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
| pingcap/tiflow                     | 121871.02 mins |                                                      |                          |                        |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 21.73 mins               | 44348.67 mins          |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Design Docs Lint                                     | 14.99 mins               | 149.87 mins            |
|                                    |                | Upgrade DM via TiUP                                  | 6.21 mins                | 1335.65 mins           |
|                                    |                | DM Chaos                                             | 31.58 mins               | 6695.07 mins           |
|                                    |                | Auto Assign to Bugs and Questions                    | 13.72 mins               | 11126.58 mins          |
|                                    |                | DM Binlog 999999                                     | 11.81 mins               | 2492.52 mins           |
|                                    |                | Upstream Database Switch                             | 13.19 mins               | 2796.15 mins           |
|                                    |                | CDC Integration Tests                                | 21.83 mins               | 27222.12 mins          |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Web UI Lint                                       | 4.37 mins                | 56.78 mins             |
|                                    |                | Dataflow Engine e2e tests                            | 20.09 mins               | 20634.48 mins          |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 20.84 mins               | 4877.57 mins           |
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
| pingcap/go-tpc                     | 10.8 mins      |                                                      |                          |                        |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | workflow                                             | 1.08 mins                | 10.8 mins              |
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
Error: {'message': 'Server Error'}
