
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 0.0 mins      |                    |                          |                        |
|                                |               | Build Runner Image | 0.0 mins                 | 0.0 mins               |
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
| datafuselabs/databend               | 199629.03 mins |                                     |                          |                        |
|                                     |                | Typo CI                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 108.6 mins               | 4778.32 mins           |
|                                     |                | Fast Unit Tests                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Test Stateless Standalone           | 0.0 mins                 | 0.0 mins               |
|                                     |                | Check                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 106.95 mins              | 33048.12 mins          |
|                                     |                | Build Tool                          | 26.58 mins               | 159.5 mins             |
|                                     |                | Dev Linux                           | 27.58 mins               | 35518.0 mins           |
|                                     |                | Dev MacOS                           | 97.77 mins               | 125930.98 mins         |
|                                     |                | Build Sqllogic Test Image           | 3.18 mins                | 194.12 mins            |
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
| datafuselabs/openraft               | 2308.42 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 20.85 mins               | 1584.35 mins           |
|                                     |                | commit-message-check                | 7.37 mins                | 538.02 mins            |
|                                     |                | Unit test coverage                  | 11.32 mins               | 158.47 mins            |
|                                     |                | DevSkim                             | 0.81 mins                | 4.05 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 1.73 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.2 mins                 | 1.4 mins               |
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
| datafuselabs/weekly                 | 4.7 mins       |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.36 mins                | 1.82 mins              |
|                                     |                | pages build and deployment          | 0.58 mins                | 2.88 mins              |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 91903.78 mins  |                                     |                          |                        |
|                                     |                | CI                                  | 147.12 mins              | 28540.88 mins          |
|                                     |                | Docs                                | 7.16 mins                | 1145.1 mins            |
|                                     |                | Service Test Azblob                 | 8.75 mins                | 1697.93 mins           |
|                                     |                | Service Test Fs                     | 8.17 mins                | 1585.47 mins           |
|                                     |                | Service Test Ftp                    | 11.05 mins               | 2143.82 mins           |
|                                     |                | Service Test Gcs                    | 9.31 mins                | 1806.5 mins            |
|                                     |                | Service Test HDFS                   | 9.62 mins                | 1865.48 mins           |
|                                     |                | Service Test HTTP                   | 8.44 mins                | 1637.62 mins           |
|                                     |                | Service Test IPFS                   | 94.29 mins               | 18291.67 mins          |
|                                     |                | Service Test IPMFS                  | 8.84 mins                | 1715.58 mins           |
|                                     |                | Service Test Memory                 | 8.33 mins                | 1616.07 mins           |
|                                     |                | Service Test Moka                   | 8.94 mins                | 858.28 mins            |
|                                     |                | Service Test Obs                    | 10.75 mins               | 2085.75 mins           |
|                                     |                | Service Test Oss                    | 110.48 mins              | 19665.78 mins          |
|                                     |                | Service Test Redis                  | 9.26 mins                | 1797.18 mins           |
|                                     |                | Service Test S3                     | 28.1 mins                | 5450.67 mins           |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 433.62 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 14.45 mins               | 433.62 mins            |
| datafuselabs/databend-perf          | 1275.38 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 25.91 mins               | 932.87 mins            |
|                                     |                | pages build and deployment          | 0.57 mins                | 10.87 mins             |
|                                     |                | Reload tpch                         | 17.34 mins               | 138.7 mins             |
|                                     |                | Reload hits                         | 17.05 mins               | 136.43 mins            |
|                                     |                | Reload ontime                       | 14.13 mins               | 56.52 mins             |
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
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb                       | 71738.17 mins  |                                                      |                          |                        |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR & Lightning                                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dumpling                                             | 6.77 mins                | 676.63 mins            |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | misc                                                 | 29.36 mins               | 71045.9 mins           |
|                                    |                | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 136.82 mins    |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 9.12 mins                | 136.82 mins            |
| pingcap/kvproto                    | 1124.02 mins   |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 8.4 mins                 | 462.25 mins            |
|                                    |                | Golang Test                                          | 2.25 mins                | 123.6 mins             |
|                                    |                | Rust Test                                            | 9.78 mins                | 538.17 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 89225.95 mins  |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.9 mins                 | 15.23 mins             |
|                                    |                | Assign to Project                                    | 1.58 mins                | 1.58 mins              |
|                                    |                | Trigger docs site update                             | 1.49 mins                | 775.23 mins            |
|                                    |                | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 94.2 mins              |
|                                    |                | ci                                                   | 30.46 mins               | 43713.9 mins           |
|                                    |                | Links                                                | 1.78 mins                | 10.68 mins             |
|                                    |                | bot                                                  | 0.76 mins                | 16.02 mins             |
|                                    |                | cron                                                 | 1.1 mins                 | 32.97 mins             |
|                                    |                | Links (Fail Fast)                                    | 1.56 mins                | 2034.18 mins           |
|                                    |                | Prevent Deletion                                     | 29.11 mins               | 42531.68 mins          |
|                                    |                | Pull Request Labeler                                 | 0.27 mins                | 0.27 mins              |
| pingcap/docs-cn                    | 48734.95 mins  |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu and Aws when they change | 0.95 mins                | 5.72 mins              |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 1.39 mins                | 536.83 mins            |
|                                    |                | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 67.88 mins             |
|                                    |                | ci                                                   | 4.89 mins                | 6139.13 mins           |
|                                    |                | Links                                                | 1.05 mins                | 4.22 mins              |
|                                    |                | Flush PDF                                            | 0.28 mins                | 10.8 mins              |
|                                    |                | Links (Fail Fast)                                    | 1.19 mins                | 1342.85 mins           |
|                                    |                | Prevent Deletion                                     | 33.77 mins               | 40627.52 mins          |
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
| pingcap/tispark                    | 2853.33 mins   |                                                      |                          |                        |
|                                    |                | TLS test                                             | 15.88 mins               | 555.8 mins             |
|                                    |                | alter-primary-key-false-test                         | 13.25 mins               | 463.92 mins            |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 17.85 mins               | 696.08 mins            |
|                                    |                | Follower Read test                                   | 12.39 mins               | 433.57 mins            |
|                                    |                | Close inactive issues                                | 0.24 mins                | 7.35 mins              |
|                                    |                | License checker                                      | 8.19 mins                | 286.72 mins            |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 11.71 mins               | 409.9 mins             |
| pingcap/octopus                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/grpc                       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | PR AutoFix                                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
| pingcap/jepsen                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins       |                                                      |                          |                        |
| pingcap/chaos                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/meetup                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
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
| pingcap/go-ycsb                    | 128.95 mins    |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 3.52 mins                | 66.92 mins             |
|                                    |                | Publish artifacts to github release                  | 3.71 mins                | 7.42 mins              |
|                                    |                | Go                                                   | 2.87 mins                | 54.62 mins             |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins       |                                                      |                          |                        |
|                                    |                | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 4398.98 mins   |                                                      |                          |                        |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                                | 20.34 mins               | 1830.5 mins            |
|                                    |                | ci                                                   | 24.61 mins               | 2559.22 mins           |
|                                    |                | Close stale issues/prs                               | 0.31 mins                | 9.27 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5280.6 mins    |                                                      |                          |                        |
|                                    |                | Pull Request CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | License checker                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                                      |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/benchmarksql               | 0.0 mins       |                                                      |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                                      |                          |                        |
| pingcap/dm                         | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Test binlog 999999                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build & Lint                                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upstream database switch                             | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins       |                                                      |                          |                        |
| pingcap/log                        | 5.4 mins       |                                                      |                          |                        |
|                                    |                | Audit License                                        | 1.19 mins                | 3.57 mins              |
|                                    |                | Unit Test                                            | 0.61 mins                | 1.83 mins              |
| pingcap/tiflash                    | 1746.0 mins    |                                                      |                          |                        |
|                                    |                | License checker                                      | 2.37 mins                | 1746.0 mins            |
|                                    |                | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | Bug Closed                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/capnproto                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/boost-extra                | 0.0 mins       |                                                      |                          |                        |
| pingcap/kdt                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/failpoint                  | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build & Test                                         | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tiflow                     | 181694.28 mins |                                                      |                          |                        |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 34.1 mins                | 40167.42 mins          |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Design Docs Lint                                     | 1.47 mins                | 10.3 mins              |
|                                    |                | Upgrade DM via TiUP                                  | 5.4 mins                 | 1134.08 mins           |
|                                    |                | DM Chaos                                             | 28.03 mins               | 6390.62 mins           |
|                                    |                | Auto Assign to Bugs and Questions                    | 1.76 mins                | 649.52 mins            |
|                                    |                | DM Binlog 999999                                     | 12.93 mins               | 2714.32 mins           |
|                                    |                | Upstream Database Switch                             | 14.42 mins               | 3028.32 mins           |
|                                    |                | CDC Integration Tests                                | 138.88 mins              | 120132.17 mins         |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Web UI Lint                                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 29.78 mins               | 7236.47 mins           |
|                                    |                | Dataflow Engine Image                                | 38.51 mins               | 231.08 mins            |
| pingcap/br                         | 0.0 mins       |                                                      |                          |                        |
|                                    |                | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.33 mins      |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                              | 0.33 mins                | 0.33 mins              |
| pingcap/style-guide                | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-tpc                     | 39.43 mins     |                                                      |                          |                        |
|                                    |                | release                                              | 2.15 mins                | 8.58 mins              |
|                                    |                | workflow                                             | 1.62 mins                | 30.85 mins             |
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
