
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
| datafuselabs/databend               | 114455.22 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 86.94 mins               | 3303.63 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 69.11 mins               | 18382.28 mins          |
|                                     |                | Build Tool                          | 23.73 mins               | 47.45 mins             |
|                                     |                | Dev Linux                           | 26.55 mins               | 31436.07 mins          |
|                                     |                | Dev MacOS                           | 51.69 mins               | 61196.45 mins          |
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
| datafuselabs/openraft               | 1723.88 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 16.2 mins                | 16.2 mins              |
|                                     |                | ci                                  | 16.04 mins               | 1234.77 mins           |
|                                     |                | commit-message-check                | 2.59 mins                | 245.67 mins            |
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
| datafuselabs/opendal                | 24337.28 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 9.79 mins                | 3123.18 mins           |
|                                     |                | Docs                                | 4.62 mins                | 1108.02 mins           |
|                                     |                | Service Test Azblob                 | 5.95 mins                | 1908.63 mins           |
|                                     |                | Service Test Fs                     | 5.61 mins                | 1800.22 mins           |
|                                     |                | Service Test Ftp                    | 7.86 mins                | 943.62 mins            |
|                                     |                | Service Test Gcs                    | 5.98 mins                | 1919.6 mins            |
|                                     |                | Service Test HDFS                   | 6.95 mins                | 2231.77 mins           |
|                                     |                | Service Test HTTP                   | 7.08 mins                | 2271.4 mins            |
|                                     |                | Service Test IPFS                   | 6.36 mins                | 2033.7 mins            |
|                                     |                | Service Test IPMFS                  | 6.02 mins                | 1065.18 mins           |
|                                     |                | Service Test Memory                 | 5.5 mins                 | 1764.45 mins           |
|                                     |                | Service Test Obs                    | 6.07 mins                | 1844.87 mins           |
|                                     |                | Service Test S3                     | 7.24 mins                | 2322.65 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 319.08 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 9.97 mins                | 319.08 mins            |
| datafuselabs/databend-perf          | 1104.22 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 17.06 mins               | 853.22 mins            |
|                                     |                | pages build and deployment          | 0.62 mins                | 14.97 mins             |
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
    
Error: {'message': 'Server Error'}
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
| pingcap/tidb                       | 13314.75 mins |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 8.97 mins                | 457.43 mins            |
|                                    |               | BR & Lightning                                       | 1.37 mins                | 590.33 mins            |
|                                    |               | Dumpling                                             | 7.53 mins                | 3891.27 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 4.24 mins                | 7883.87 mins           |
|                                    |               | Leaked Secrets Scan                                  | 7.08 mins                | 42.47 mins             |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 5.65 mins     |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.65 mins                | 5.65 mins              |
| pingcap/kvproto                    | 1207.45 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 7.93 mins                | 539.27 mins            |
|                                    |               | Golang Test                                          | 2.42 mins                | 164.23 mins            |
|                                    |               | Rust Test                                            | 7.41 mins                | 503.95 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 10253.0 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 1.07 mins                | 4.3 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/auto-label.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/auto-assign.yml                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 1.88 mins                | 519.95 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.06 mins                | 77.18 mins             |
|                                    |               | ci                                                   | 5.41 mins                | 5807.68 mins           |
|                                    |               | Links                                                | 0.82 mins                | 3.27 mins              |
|                                    |               | bot                                                  | 1.45 mins                | 28.93 mins             |
|                                    |               | cron                                                 | 0.81 mins                | 24.22 mins             |
|                                    |               | Links (Fail Fast)                                    | 1.95 mins                | 1952.85 mins           |
|                                    |               | Prevent Deletion                                     | 1.65 mins                | 1834.62 mins           |
|                                    |               | Auto Assign                                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 11986.78 mins |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 3.21 mins                | 12.85 mins             |
|                                    |               | Translation Welcome                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 2.45 mins                | 627.35 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.06 mins                | 67.92 mins             |
|                                    |               | ci                                                   | 5.8 mins                 | 7008.35 mins           |
|                                    |               | Links                                                | 0.93 mins                | 3.7 mins               |
|                                    |               | Flush PDF                                            | 0.34 mins                | 10.9 mins              |
|                                    |               | Links (Fail Fast)                                    | 2.31 mins                | 2569.45 mins           |
|                                    |               | Prevent Deletion                                     | 1.68 mins                | 1686.27 mins           |
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
| pingcap/tispark                    | 12627.58 mins |                                                      |                          |                        |
|                                    |               | TLS test                                             | 17.43 mins               | 2997.67 mins           |
|                                    |               | alter-primary-key-false-test                         | 13.07 mins               | 2247.45 mins           |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 19.34 mins               | 3403.77 mins           |
|                                    |               | Follower Read test                                   | 13.14 mins               | 643.92 mins            |
|                                    |               | Close inactive issues                                | 0.33 mins                | 9.92 mins              |
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
| pingcap/tidb-operator              | 9161.58 mins  |                                                      |                          |                        |
|                                    |               | ci                                                   | 28.08 mins               | 4239.47 mins           |
|                                    |               | chaos                                                | 35.86 mins               | 4913.35 mins           |
|                                    |               | Close stale issues/prs                               | 0.29 mins                | 8.77 mins              |
|                                    |               |                                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 7584.3 mins   |                                                      |                          |                        |
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
| pingcap/tiflash                    | 3337.43 mins  |                                                      |                          |                        |
|                                    |               | License checker                                      | 2.6 mins                 | 3337.43 mins           |
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
| pingcap/tiflow                     | 81272.87 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 20.55 mins               | 26902.77 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.44 mins                | 0.88 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 5.2 mins                 | 1097.27 mins           |
|                                    |               | DM Chaos                                             | 29.41 mins               | 6324.03 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 7.78 mins                | 4396.7 mins            |
|                                    |               | DM Binlog 999999                                     | 11.95 mins               | 2510.0 mins            |
|                                    |               | Upstream Database Switch                             | 13.18 mins               | 2781.5 mins            |
|                                    |               | CDC Integration Tests                                | 21.74 mins               | 18823.25 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 8.37 mins                | 83.72 mins             |
|                                    |               | Dataflow Engine e2e tests                            | 19.26 mins               | 13982.92 mins          |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 20.37 mins               | 4317.73 mins           |
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
| pingcap/go-tpc                     | 5.75 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.15 mins                | 5.75 mins              |
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
