
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 359.63 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 179.82 mins              | 359.63 mins            |
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
| webp-sh/webp_server_go     | 94.78 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.27 mins                | 13.08 mins             |
|                            |               | Release Binaries                | 0.0 mins                 | 0.0 mins               |
|                            |               | Build and release docker images | 14.27 mins               | 57.08 mins             |
|                            |               | CodeQL                          | 2.05 mins                | 24.62 mins             |
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
| datafuselabs/databend               | 198067.88 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 109.55 mins              | 4820.13 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 107.01 mins              | 32423.17 mins          |
|                                     |                | Build Tool                          | 26.58 mins               | 159.5 mins             |
|                                     |                | Dev Linux                           | 27.61 mins               | 35098.07 mins          |
|                                     |                | Dev MacOS                           | 98.64 mins               | 125367.93 mins         |
|                                     |                | Build Sqllogic Test Image           | 3.26 mins                | 199.08 mins            |
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
| datafuselabs/openraft               | 2436.78 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 20.83 mins               | 1666.53 mins           |
|                                     |                | commit-message-check                | 7.29 mins                | 576.12 mins            |
|                                     |                | Unit test coverage                  | 11.19 mins               | 167.78 mins            |
|                                     |                | DevSkim                             | 0.82 mins                | 3.3 mins               |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.07 mins                | 1.67 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.2 mins                 | 0.98 mins              |
|                                     |                | .github/workflows/pages.yaml        | 0.39 mins                | 0.78 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 9.81 mins                | 19.62 mins             |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 6.68 mins      |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.37 mins                | 2.58 mins              |
|                                     |                | pages build and deployment          | 0.59 mins                | 4.1 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 123204.47 mins |                                     |                          |                        |
|                                     |                | CI                                  | 130.73 mins              | 28761.23 mins          |
|                                     |                | Docs                                | 6.78 mins                | 1254.45 mins           |
|                                     |                | Service Test Azblob                 | 8.35 mins                | 1837.63 mins           |
|                                     |                | Service Test Fs                     | 7.77 mins                | 1708.58 mins           |
|                                     |                | Service Test Ftp                    | 10.59 mins               | 2329.37 mins           |
|                                     |                | Service Test Gcs                    | 8.87 mins                | 1952.07 mins           |
|                                     |                | Service Test HDFS                   | 9.27 mins                | 2038.9 mins            |
|                                     |                | Service Test HTTP                   | 8.12 mins                | 1787.0 mins            |
|                                     |                | Service Test IPFS                   | 85.08 mins               | 18717.52 mins          |
|                                     |                | Service Test IPMFS                  | 8.42 mins                | 1851.73 mins           |
|                                     |                | Service Test Memory                 | 7.94 mins                | 1746.62 mins           |
|                                     |                | Service Test Moka                   | 8.94 mins                | 858.28 mins            |
|                                     |                | Service Test Obs                    | 141.98 mins              | 31235.93 mins          |
|                                     |                | Service Test Oss                    | 110.48 mins              | 19665.78 mins          |
|                                     |                | Service Test Redis                  | 9.08 mins                | 1842.63 mins           |
|                                     |                | Service Test S3                     | 25.53 mins               | 5616.73 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 414.03 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 13.8 mins                | 414.03 mins            |
| datafuselabs/databend-perf          | 1240.72 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 25.3 mins                | 910.73 mins            |
|                                     |                | pages build and deployment          | 0.58 mins                | 10.95 mins             |
|                                     |                | Reload tpch                         | 16.37 mins               | 114.62 mins            |
|                                     |                | Reload hits                         | 19.68 mins               | 137.78 mins            |
|                                     |                | Reload ontime                       | 13.33 mins               | 66.63 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins       |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 8.73 mins      |                                     |                          |                        |
|                                     |                | CI                                  | 4.37 mins                | 8.73 mins              |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
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
| pingcap/tidb                       | 72712.75 mins |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR & Lightning                                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dumpling                                             | 7.31 mins                | 1994.95 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 30.66 mins               | 70702.17 mins          |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 130.15 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 9.3 mins                 | 130.15 mins            |
| pingcap/kvproto                    | 966.78 mins   |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 9.17 mins                | 421.98 mins            |
|                                    |               | Golang Test                                          | 2.3 mins                 | 105.98 mins            |
|                                    |               | Rust Test                                            | 9.54 mins                | 438.82 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 88895.57 mins |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.9 mins                 | 15.23 mins             |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 1.61 mins                | 767.55 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 88.25 mins             |
|                                    |               | ci                                                   | 31.66 mins               | 43463.02 mins          |
|                                    |               | Links                                                | 1.78 mins                | 10.68 mins             |
|                                    |               | bot                                                  | 0.75 mins                | 17.32 mins             |
|                                    |               | cron                                                 | 1.07 mins                | 31.97 mins             |
|                                    |               | Links (Fail Fast)                                    | 1.6 mins                 | 2005.08 mins           |
|                                    |               | Prevent Deletion                                     | 30.46 mins               | 42496.2 mins           |
|                                    |               | Pull Request Labeler                                 | 0.27 mins                | 0.27 mins              |
| pingcap/docs-cn                    | 48332.43 mins |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.95 mins                | 5.72 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 1.53 mins                | 529.43 mins            |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 62.22 mins             |
|                                    |               | ci                                                   | 4.95 mins                | 5817.62 mins           |
|                                    |               | Links                                                | 1.05 mins                | 4.22 mins              |
|                                    |               | Flush PDF                                            | 0.28 mins                | 10.58 mins             |
|                                    |               | Links (Fail Fast)                                    | 1.22 mins                | 1305.63 mins           |
|                                    |               | Prevent Deletion                                     | 36.05 mins               | 40597.02 mins          |
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
| pingcap/tispark                    | 2783.0 mins   |                                                      |                          |                        |
|                                    |               | TLS test                                             | 16.29 mins               | 537.47 mins            |
|                                    |               | alter-primary-key-false-test                         | 13.55 mins               | 447.17 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 17.96 mins               | 682.62 mins            |
|                                    |               | Follower Read test                                   | 12.76 mins               | 420.97 mins            |
|                                    |               | Close inactive issues                                | 0.24 mins                | 7.3 mins               |
|                                    |               | License checker                                      | 8.63 mins                | 284.68 mins            |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 12.21 mins               | 402.8 mins             |
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
| pingcap/go-ycsb                    | 128.95 mins   |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 3.52 mins                | 66.92 mins             |
|                                    |               | Publish artifacts to github release                  | 3.71 mins                | 7.42 mins              |
|                                    |               | Go                                                   | 2.87 mins                | 54.62 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 4368.05 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 20.37 mins               | 1813.03 mins           |
|                                    |               | ci                                                   | 24.72 mins               | 2545.82 mins           |
|                                    |               | Close stale issues/prs                               | 0.31 mins                | 9.2 mins               |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5001.85 mins  |                                                      |                          |                        |
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
| pingcap/log                        | 5.4 mins      |                                                      |                          |                        |
|                                    |               | Audit License                                        | 1.19 mins                | 3.57 mins              |
|                                    |               | Unit Test                                            | 0.61 mins                | 1.83 mins              |
| pingcap/tiflash                    | 1708.23 mins  |                                                      |                          |                        |
|                                    |               | License checker                                      | 2.37 mins                | 1708.23 mins           |
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
| pingcap/tiflow                     | 179777.1 mins |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 34.88 mins               | 39304.93 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 4.22 mins                | 8.45 mins              |
|                                    |               | Upgrade DM via TiUP                                  | 5.39 mins                | 1131.47 mins           |
|                                    |               | DM Chaos                                             | 27.01 mins               | 6157.73 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 1.88 mins                | 638.0 mins             |
|                                    |               | DM Binlog 999999                                     | 12.94 mins               | 2716.35 mins           |
|                                    |               | Upstream Database Switch                             | 14.42 mins               | 3029.0 mins            |
|                                    |               | CDC Integration Tests                                | 143.67 mins              | 119535.25 mins         |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 29.15 mins               | 7024.83 mins           |
|                                    |               | Dataflow Engine Image                                | 38.51 mins               | 231.08 mins            |
| pingcap/br                         | 0.0 mins      |                                                      |                          |                        |
|                                    |               | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.33 mins     |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.33 mins                | 0.33 mins              |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 39.43 mins    |                                                      |                          |                        |
|                                    |               | release                                              | 2.15 mins                | 8.58 mins              |
|                                    |               | workflow                                             | 1.62 mins                | 30.85 mins             |
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
