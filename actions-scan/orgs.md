
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 233.7 mins    |                    |                          |                        |
|                                |               | Build Runner Image | 116.85 mins              | 233.7 mins             |
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
| webp-sh/webp_server_go     | 108.7 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.38 mins                | 13.5 mins              |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 16.28 mins               | 65.12 mins             |
|                            |               | CodeQL                          | 2.15 mins                | 30.08 mins             |
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
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 113946.48 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 87.09 mins               | 3396.55 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 69.48 mins               | 18204.58 mins          |
|                                     |                | Build Tool                          | 23.73 mins               | 47.45 mins             |
|                                     |                | Dev Linux                           | 26.52 mins               | 31165.52 mins          |
|                                     |                | Dev MacOS                           | 51.95 mins               | 61043.05 mins          |
|                                     |                | Build Sqllogic Test Image           | 3.57 mins                | 89.33 mins             |
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
|                                     |                | Crowdin Action                      | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 1753.93 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 16.2 mins                | 16.2 mins              |
|                                     |                | ci                                  | 15.6 mins                | 1263.2 mins            |
|                                     |                | commit-message-check                | 2.42 mins                | 247.28 mins            |
|                                     |                | Unit test coverage                  | 9.26 mins                | 185.13 mins            |
|                                     |                | DevSkim                             | 0.79 mins                | 3.95 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.05 mins                | 1.3 mins               |
|                                     |                | .github/workflows/issue-welcome.yml | 0.29 mins                | 1.15 mins              |
|                                     |                | .github/workflows/pages.yaml        | 3.89 mins                | 19.47 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 4.38 mins                | 13.15 mins             |
|                                     |                | pages build and deployment          | 0.62 mins                | 3.1 mins               |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 4.35 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.43 mins                | 1.73 mins              |
|                                     |                | pages build and deployment          | 0.65 mins                | 2.62 mins              |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 25037.8 mins   |                                     |                          |                        |
|                                     |                | CI                                  | 9.77 mins                | 3263.7 mins            |
|                                     |                | Docs                                | 4.63 mins                | 1161.38 mins           |
|                                     |                | Service Test Azblob                 | 5.91 mins                | 1984.85 mins           |
|                                     |                | Service Test Fs                     | 5.59 mins                | 1878.6 mins            |
|                                     |                | Service Test Ftp                    | 7.86 mins                | 943.62 mins            |
|                                     |                | Service Test Gcs                    | 5.94 mins                | 1994.58 mins           |
|                                     |                | Service Test HDFS                   | 6.92 mins                | 2325.32 mins           |
|                                     |                | Service Test HTTP                   | 7.09 mins                | 2383.85 mins           |
|                                     |                | Service Test IPFS                   | 6.44 mins                | 1906.37 mins           |
|                                     |                | Service Test IPMFS                  | 6.02 mins                | 1065.18 mins           |
|                                     |                | Service Test Memory                 | 5.47 mins                | 1836.7 mins            |
|                                     |                | Service Test Obs                    | 6.07 mins                | 1863.93 mins           |
|                                     |                | Service Test S3                     | 7.23 mins                | 2429.72 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 326.55 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 10.2 mins                | 326.55 mins            |
| datafuselabs/databend-perf          | 994.33 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 14.85 mins               | 742.53 mins            |
|                                     |                | pages build and deployment          | 0.63 mins                | 15.77 mins             |
|                                     |                | Reload tpch                         | 10.85 mins               | 130.22 mins            |
|                                     |                | Reload hits                         | 16.93 mins               | 67.7 mins              |
|                                     |                | Reload ontime                       | 19.06 mins               | 38.12 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 26.92 mins     |                                     |                          |                        |
|                                     |                | CI                                  | 13.46 mins               | 26.92 mins             |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
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
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 13577.08 mins |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 9.21 mins                | 497.27 mins            |
|                                    |               | BR & Lightning                                       | 1.39 mins                | 628.12 mins            |
|                                    |               | Dumpling                                             | 7.65 mins                | 4101.08 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 4.25 mins                | 7858.77 mins           |
|                                    |               | Leaked Secrets Scan                                  | 7.08 mins                | 42.47 mins             |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 25.08 mins    |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 6.27 mins                | 25.08 mins             |
| pingcap/kvproto                    | 1300.62 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 7.82 mins                | 578.65 mins            |
|                                    |               | Golang Test                                          | 2.37 mins                | 175.07 mins            |
|                                    |               | Rust Test                                            | 7.39 mins                | 546.9 mins             |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 11814.05 mins |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.49 mins                | 10.45 mins             |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 1.73 mins                | 560.52 mins            |
|                                    |               | external-link-check                                  | 11.31 mins               | 33.92 mins             |
|                                    |               | Automatic Rebase                                     | 0.06 mins                | 90.25 mins             |
|                                    |               | ci                                                   | 5.77 mins                | 6828.22 mins           |
|                                    |               | Links                                                | 0.82 mins                | 3.27 mins              |
|                                    |               | bot                                                  | 1.41 mins                | 29.53 mins             |
|                                    |               | cron                                                 | 0.83 mins                | 24.85 mins             |
|                                    |               | Links (Fail Fast)                                    | 2.01 mins                | 2139.0 mins            |
|                                    |               | Prevent Deletion                                     | 1.81 mins                | 2094.05 mins           |
|                                    |               | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 12368.98 mins |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 2.16 mins                | 15.13 mins             |
|                                    |               | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 2.34 mins                | 643.93 mins            |
|                                    |               | external-link-check                                  | 6.73 mins                | 6.73 mins              |
|                                    |               | Automatic Rebase                                     | 0.05 mins                | 72.78 mins             |
|                                    |               | ci                                                   | 5.81 mins                | 7304.67 mins           |
|                                    |               | Links                                                | 0.93 mins                | 3.7 mins               |
|                                    |               | Flush PDF                                            | 0.34 mins                | 10.92 mins             |
|                                    |               | Links (Fail Fast)                                    | 2.29 mins                | 2625.7 mins            |
|                                    |               | Prevent Deletion                                     | 1.68 mins                | 1685.42 mins           |
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
| pingcap/tispark                    | 12644.03 mins |                                                      |                          |                        |
|                                    |               | TLS test                                             | 17.43 mins               | 2997.67 mins           |
|                                    |               | alter-primary-key-false-test                         | 13.07 mins               | 2247.45 mins           |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 19.32 mins               | 3420.18 mins           |
|                                    |               | Follower Read test                                   | 13.14 mins               | 643.92 mins            |
|                                    |               | Close inactive issues                                | 0.33 mins                | 9.95 mins              |
|                                    |               | License checker                                      | 6.61 mins                | 1136.87 mins           |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 12.72 mins               | 2188.0 mins            |
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
| pingcap/go-ycsb                    | 16.22 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 3.64 mins                | 10.92 mins             |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 1.77 mins                | 5.3 mins               |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 3.83 mins     |                                                      |                          |                        |
|                                    |               | testbuild                                            | 1.08 mins                | 1.08 mins              |
|                                    |               | release                                              | 1.38 mins                | 2.75 mins              |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 9161.62 mins  |                                                      |                          |                        |
|                                    |               | ci                                                   | 28.08 mins               | 4239.47 mins           |
|                                    |               | chaos                                                | 35.86 mins               | 4913.35 mins           |
|                                    |               | Close stale issues/prs                               | 0.29 mins                | 8.8 mins               |
|                                    |               |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 8232.92 mins  |                                                      |                          |                        |
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
| pingcap/log                        | 6.22 mins     |                                                      |                          |                        |
|                                    |               | Audit License                                        | 1.16 mins                | 3.47 mins              |
|                                    |               | Unit Test                                            | 0.92 mins                | 2.75 mins              |
| pingcap/tiflash                    | 3530.1 mins   |                                                      |                          |                        |
|                                    |               | License checker                                      | 2.61 mins                | 3530.1 mins            |
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
| pingcap/tiflow                     | 85278.6 mins  |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 20.68 mins               | 28555.85 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.44 mins                | 0.88 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 5.17 mins                | 1090.87 mins           |
|                                    |               | DM Chaos                                             | 29.42 mins               | 6325.0 mins            |
|                                    |               | Auto Assign to Bugs and Questions                    | 7.38 mins                | 4535.65 mins           |
|                                    |               | DM Binlog 999999                                     | 11.92 mins               | 2502.52 mins           |
|                                    |               | Upstream Database Switch                             | 13.09 mins               | 2762.43 mins           |
|                                    |               | CDC Integration Tests                                | 22.07 mins               | 20216.35 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 8.37 mins                | 83.72 mins             |
|                                    |               | Dataflow Engine e2e tests                            | 19.42 mins               | 14775.05 mins          |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 20.37 mins               | 4317.7 mins            |
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
| pingcap/go-tpc                     | 7.55 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.26 mins                | 7.55 mins              |
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
Error: {'message': 'Server Error'}
