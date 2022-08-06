
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 182.02 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 182.02 mins              | 182.02 mins            |
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
| webp-sh/webp_server_go     | 75.67 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.66 mins                | 14.65 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 13.28 mins               | 39.85 mins             |
|                            |               | CodeQL                          | 1.92 mins                | 21.17 mins             |
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
| datafuselabs/databend               | 113575.23 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 95.43 mins               | 3244.73 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 71.97 mins               | 16337.53 mins          |
|                                     |                | Build Tool                          | 19.97 mins               | 99.87 mins             |
|                                     |                | Crowdin Action                      | 2.92 mins                | 806.33 mins            |
|                                     |                | Dev Linux                           | 21.84 mins               | 23592.4 mins           |
|                                     |                | Dev MacOS                           | 64.35 mins               | 69494.37 mins          |
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
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 2777.42 mins   |                                     |                          |                        |
|                                     |                | ci                                  | 17.82 mins               | 2602.08 mins           |
|                                     |                | commit-message-check                | 0.74 mins                | 142.2 mins             |
|                                     |                | DevSkim                             | 2.76 mins                | 13.78 mins             |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 5.65 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.28 mins                | 4.48 mins              |
|                                     |                | .github/workflows/pages.yaml        | 0.55 mins                | 3.32 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 2.02 mins                | 2.02 mins              |
|                                     |                | pages build and deployment          | 0.65 mins                | 3.88 mins              |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 4.1 mins       |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.42 mins                | 1.68 mins              |
|                                     |                | pages build and deployment          | 0.6 mins                 | 2.42 mins              |
| datafuselabs/databend-playground    | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 18007.1 mins   |                                     |                          |                        |
|                                     |                | CI                                  | 38.26 mins               | 5700.65 mins           |
|                                     |                | Docs                                | 4.7 mins                 | 733.37 mins            |
|                                     |                | Add issues into projects            | 0.24 mins                | 6.88 mins              |
|                                     |                | Service Test Azblob                 | 6.19 mins                | 921.57 mins            |
|                                     |                | Service Test Fs                     | 28.74 mins               | 4282.68 mins           |
|                                     |                | Service Test HDFS                   | 7.03 mins                | 1046.93 mins           |
|                                     |                | Service Test HTTP                   | 34.92 mins               | 3456.7 mins            |
|                                     |                | Service Test Memory                 | 5.53 mins                | 824.57 mins            |
|                                     |                | Service Test S3                     | 6.94 mins                | 1033.75 mins           |
| datafuselabs/opensrv                | 263.38 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 7.75 mins                | 263.38 mins            |
| datafuselabs/databend-perf          | 1044.47 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 18.33 mins               | 659.95 mins            |
|                                     |                | Reload                              | 10.85 mins               | 368.83 mins            |
|                                     |                | pages build and deployment          | 0.65 mins                | 15.68 mins             |
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
| pingcap/tidb                       | 29484.62 mins  |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/codeql-analysis.yml                | 0.0 mins                 | 0.0 mins               |
|                                    |                | License checker                                      | 4.41 mins                | 18255.02 mins          |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 13.12 mins               | 1167.92 mins           |
|                                    |                | BR & Lightning                                       | 1.22 mins                | 1029.38 mins           |
|                                    |                | Dumpling                                             | 12.07 mins               | 8760.05 mins           |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull request labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 95.82 mins     |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 7.37 mins                | 95.82 mins             |
| pingcap/kvproto                    | 450.62 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 4.81 mins                | 139.37 mins            |
|                                    |                | Golang Test                                          | 3.02 mins                | 87.7 mins              |
|                                    |                | Rust Test                                            | 7.71 mins                | 223.55 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 8389.85 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 17.47 mins               | 262.08 mins            |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 4.27 mins                | 1067.27 mins           |
|                                    |                | external-link-check                                  | 14.96 mins               | 44.87 mins             |
|                                    |                | Automatic Rebase                                     | 0.07 mins                | 99.02 mins             |
|                                    |                | ci                                                   | 6.07 mins                | 6820.9 mins            |
|                                    |                | Links                                                | 0.62 mins                | 2.47 mins              |
|                                    |                | bot                                                  | 0.75 mins                | 16.43 mins             |
|                                    |                | cron                                                 | 2.56 mins                | 76.82 mins             |
|                                    |                | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 6066.27 mins   |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 2.52 mins                | 17.63 mins             |
|                                    |                | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 1.32 mins                | 306.58 mins            |
|                                    |                | external-link-check                                  | 20.2 mins                | 20.2 mins              |
|                                    |                | Automatic Rebase                                     | 0.05 mins                | 73.13 mins             |
|                                    |                | ci                                                   | 4.31 mins                | 5630.77 mins           |
|                                    |                | Links                                                | 1.25 mins                | 5.02 mins              |
|                                    |                | Flush PDF                                            | 0.38 mins                | 12.93 mins             |
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
| pingcap/tispark                    | 23195.63 mins  |                                                      |                          |                        |
|                                    |                | TLS test                                             | 18.58 mins               | 5982.3 mins            |
|                                    |                | alter-primary-key-false-test                         | 13.9 mins                | 2626.85 mins           |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 22.19 mins               | 7256.68 mins           |
|                                    |                | Close inactive issues                                | 0.26 mins                | 7.82 mins              |
|                                    |                | License checker                                      | 7.98 mins                | 2569.17 mins           |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 14.76 mins               | 4752.82 mins           |
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
| pingcap/go-ycsb                    | 118.15 mins    |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 3.42 mins                | 68.47 mins             |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 2.48 mins                | 49.68 mins             |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 7.58 mins      |                                                      |                          |                        |
|                                    |                | testbuild                                            | 2.53 mins                | 7.58 mins              |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 10885.73 mins  |                                                      |                          |                        |
|                                    |                | ci                                                   | 22.45 mins               | 4894.5 mins            |
|                                    |                | chaos                                                | 31.65 mins               | 5981.9 mins            |
|                                    |                | Close stale issues/prs                               | 0.31 mins                | 9.33 mins              |
|                                    |                |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 1608.53 mins   |                                                      |                          |                        |
|                                    |                | Pull Request CI                                      | 13.7 mins                | 137.02 mins            |
|                                    |                | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins       |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                                      |                          |                        |
| pingcap/dm                         | 5782.5 mins    |                                                      |                          |                        |
|                                    |                | Test binlog 999999                                   | 41.49 mins               | 539.4 mins             |
|                                    |                | chaos                                                | 26.51 mins               | 4135.33 mins           |
|                                    |                | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                                     | 45.83 mins               | 595.77 mins            |
|                                    |                | Upstream database switch                             | 39.38 mins               | 512.0 mins             |
| pingcap/talent-plan                | 0.0 mins       |                                                      |                          |                        |
| pingcap/log                        | 3.42 mins      |                                                      |                          |                        |
|                                    |                | Audit License                                        | 1.13 mins                | 2.27 mins              |
|                                    |                | Unit Test                                            | 0.57 mins                | 1.15 mins              |
| pingcap/tiflash                    | 2757.85 mins   |                                                      |                          |                        |
|                                    |                | License checker                                      | 2.98 mins                | 2757.85 mins           |
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
| pingcap/tiflow                     | 262768.73 mins |                                                      |                          |                        |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 92.91 mins               | 184603.22 mins         |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Design Docs Lint                                     | 13.43 mins               | 161.17 mins            |
|                                    |                | Upgrade DM via TiUP                                  | 6.6 mins                 | 1399.25 mins           |
|                                    |                | DM Chaos                                             | 33.51 mins               | 7036.8 mins            |
|                                    |                | Auto Assign to Bugs and Questions                    | 14.83 mins               | 11375.05 mins          |
|                                    |                | DM Binlog 999999                                     | 12.89 mins               | 2706.0 mins            |
|                                    |                | Upstream Database Switch                             | 10.21 mins               | 2164.65 mins           |
|                                    |                | CDC Integration Tests                                | 21.88 mins               | 28272.35 mins          |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Web UI Lint                                       | 12.59 mins               | 62.93 mins             |
|                                    |                | Dataflow Engine e2e tests                            | 20.73 mins               | 19778.35 mins          |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 21.27 mins               | 5020.72 mins           |
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
|                                    |                | workflow                                             | 1.36 mins                | 5.45 mins              |
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
    
