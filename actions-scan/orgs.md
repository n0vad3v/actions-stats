
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
| webp-sh/webp_server_go     | 177.63 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.29 mins                | 39.45 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.29 mins               | 93.05 mins             |
|                            |               | CodeQL                          | 1.96 mins                | 45.13 mins             |
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
| datafuselabs/databend               | 101798.98 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 90.48 mins               | 3257.22 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 72.93 mins               | 15243.2 mins           |
|                                     |                | Build Tool                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Dev Linux                           | 21.43 mins               | 22569.1 mins           |
|                                     |                | Dev MacOS                           | 57.01 mins               | 60030.23 mins          |
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
|                                     |                | Crowdin Action                      | 2.99 mins                | 699.23 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 2449.8 mins    |                                     |                          |                        |
|                                     |                | ci                                  | 18.39 mins               | 2298.38 mins           |
|                                     |                | commit-message-check                | 0.85 mins                | 132.78 mins            |
|                                     |                | DevSkim                             | 0.78 mins                | 3.12 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 5.25 mins              |
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
| datafuselabs/opendal                | 20572.42 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 41.19 mins               | 6343.37 mins           |
|                                     |                | Docs                                | 4.95 mins                | 742.37 mins            |
|                                     |                | Add issues into projects            | 0.23 mins                | 5.38 mins              |
|                                     |                | Service Test Azblob                 | 6.25 mins                | 961.8 mins             |
|                                     |                | Service Test Fs                     | 30.66 mins               | 4722.25 mins           |
|                                     |                | Service Test HDFS                   | 7.07 mins                | 1088.68 mins           |
|                                     |                | Service Test HTTP                   | 32.87 mins               | 4733.73 mins           |
|                                     |                | Service Test Memory                 | 5.75 mins                | 885.12 mins            |
|                                     |                | Service Test S3                     | 7.08 mins                | 1089.72 mins           |
| datafuselabs/opensrv                | 240.48 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 7.52 mins                | 240.48 mins            |
| datafuselabs/databend-perf          | 674.48 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 16.92 mins               | 541.33 mins            |
|                                     |                | Reload                              | 9.33 mins                | 121.28 mins            |
|                                     |                | pages build and deployment          | 0.66 mins                | 11.87 mins             |
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
    
Error: {'total_count': 100, 'workflow_runs': []}
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
| pingcap/tidb                       | 21495.47 mins  |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/codeql-analysis.yml                | 0.0 mins                 | 0.0 mins               |
|                                    |                | License checker                                      | 4.27 mins                | 14696.57 mins          |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 12.05 mins               | 927.93 mins            |
|                                    |                | BR & Lightning                                       | 1.1 mins                 | 844.82 mins            |
|                                    |                | Dumpling                                             | 12.12 mins               | 4886.03 mins           |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull request labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 80.57 mins     |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 7.32 mins                | 80.57 mins             |
| pingcap/kvproto                    | 452.97 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 4.93 mins                | 142.97 mins            |
|                                    |                | Golang Test                                          | 3.0 mins                 | 86.95 mins             |
|                                    |                | Rust Test                                            | 7.69 mins                | 223.05 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 9756.78 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 11.89 mins               | 273.48 mins            |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 4.95 mins                | 1168.78 mins           |
|                                    |                | external-link-check                                  | 14.96 mins               | 44.87 mins             |
|                                    |                | Automatic Rebase                                     | 0.07 mins                | 109.45 mins            |
|                                    |                | ci                                                   | 6.05 mins                | 7639.77 mins           |
|                                    |                | Links                                                | 0.66 mins                | 3.32 mins              |
|                                    |                | bot                                                  | 0.84 mins                | 17.6 mins              |
|                                    |                | cron                                                 | 1.57 mins                | 47.05 mins             |
|                                    |                | Links (Fail Fast)                                    | 1.75 mins                | 452.47 mins            |
|                                    |                | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5512.87 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 1.74 mins                | 10.43 mins             |
|                                    |                | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 1.44 mins                | 255.52 mins            |
|                                    |                | external-link-check                                  | 20.2 mins                | 20.2 mins              |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 62.83 mins             |
|                                    |                | ci                                                   | 4.2 mins                 | 5148.73 mins           |
|                                    |                | Links                                                | 1.15 mins                | 5.75 mins              |
|                                    |                | Flush PDF                                            | 0.3 mins                 | 9.4 mins               |
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
| pingcap/tispark                    | 18987.4 mins   |                                                      |                          |                        |
|                                    |                | TLS test                                             | 17.89 mins               | 4687.22 mins           |
|                                    |                | alter-primary-key-false-test                         | 13.05 mins               | 2924.05 mins           |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 21.56 mins               | 5733.9 mins            |
|                                    |                | Close inactive issues                                | 0.27 mins                | 8.02 mins              |
|                                    |                | License checker                                      | 7.37 mins                | 1930.08 mins           |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 14.14 mins               | 3704.13 mins           |
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
| pingcap/go-ycsb                    | 76.28 mins     |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 3.08 mins                | 43.08 mins             |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 2.37 mins                | 33.2 mins              |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 7.58 mins      |                                                      |                          |                        |
|                                    |                | testbuild                                            | 2.53 mins                | 7.58 mins              |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 10407.28 mins  |                                                      |                          |                        |
|                                    |                | ci                                                   | 21.12 mins               | 4139.32 mins           |
|                                    |                | chaos                                                | 36.39 mins               | 6258.95 mins           |
|                                    |                | Close stale issues/prs                               | 0.3 mins                 | 9.02 mins              |
|                                    |                |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 2177.0 mins    |                                                      |                          |                        |
|                                    |                | Pull Request CI                                      | 13.7 mins                | 137.02 mins            |
|                                    |                | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins       |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                                      |                          |                        |
| pingcap/dm                         | 1790.12 mins   |                                                      |                          |                        |
|                                    |                | Test binlog 999999                                   | 40.99 mins               | 163.95 mins            |
|                                    |                | chaos                                                | 26.71 mins               | 1282.18 mins           |
|                                    |                | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                                     | 47.4 mins                | 189.6 mins             |
|                                    |                | Upstream database switch                             | 38.6 mins                | 154.38 mins            |
| pingcap/talent-plan                | 0.0 mins       |                                                      |                          |                        |
| pingcap/log                        | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 2228.58 mins   |                                                      |                          |                        |
|                                    |                | License checker                                      | 2.99 mins                | 2228.58 mins           |
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
| pingcap/tiflow                     | 135360.52 mins |                                                      |                          |                        |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 30.45 mins               | 59525.65 mins          |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Design Docs Lint                                     | 14.99 mins               | 149.87 mins            |
|                                    |                | Upgrade DM via TiUP                                  | 6.25 mins                | 1325.23 mins           |
|                                    |                | DM Chaos                                             | 32.39 mins               | 6834.68 mins           |
|                                    |                | Auto Assign to Bugs and Questions                    | 14.34 mins               | 10941.37 mins          |
|                                    |                | DM Binlog 999999                                     | 12.0 mins                | 2532.78 mins           |
|                                    |                | Upstream Database Switch                             | 12.35 mins               | 2618.68 mins           |
|                                    |                | CDC Integration Tests                                | 21.82 mins               | 26293.77 mins          |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Web UI Lint                                       | 4.37 mins                | 56.78 mins             |
|                                    |                | Dataflow Engine e2e tests                            | 20.16 mins               | 20043.85 mins          |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 20.95 mins               | 4902.28 mins           |
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
|                                    |                | workflow                                             | 0.91 mins                | 5.45 mins              |
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
Error: {'total_count': 0, 'workflow_runs': []}
