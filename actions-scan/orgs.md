
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 166.38 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 166.38 mins              | 166.38 mins            |
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
| webp-sh/webp_server_go     | 203.48 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.83 mins                | 26.82 mins             |
|                            |               | CodeQL                          | 2.04 mins                | 42.75 mins             |
|                            |               | Release Binaries                | 5.37 mins                | 10.73 mins             |
|                            |               | Build and release docker images | 17.6 mins                | 123.18 mins            |
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
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 168086.35 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 119.4 mins               | 6924.92 mins           |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 86.03 mins               | 24604.77 mins          |
|                                     |                | Build Tool                          | 34.38 mins               | 343.77 mins            |
|                                     |                | Dev Linux                           | 21.85 mins               | 34748.28 mins          |
|                                     |                | Dev MacOS                           | 65.17 mins               | 94826.7 mins           |
|                                     |                | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Benchmark                           | 0.95 mins                | 1726.45 mins           |
|                                     |                | Benchmark (trusted)                 | 1.5 mins                 | 2721.68 mins           |
|                                     |                | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 1.1 mins                 | 2189.78 mins           |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 5858.22 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 25.17 mins               | 4757.22 mins           |
|                                     |                | commit-message-check                | 3.09 mins                | 655.48 mins            |
|                                     |                | Unit test coverage                  | 6.14 mins                | 356.13 mins            |
|                                     |                | DevSkim                             | 0.95 mins                | 3.8 mins               |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 4.18 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 0.45 mins                | 4.95 mins              |
|                                     |                | .github/workflows/pages.yaml        | 1.26 mins                | 6.28 mins              |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 7.4 mins                 | 22.2 mins              |
|                                     |                | pages build and deployment          | 11.99 mins               | 47.97 mins             |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 670.58 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 18.63 mins               | 670.58 mins            |
| datafuselabs/databend-perf          | 823.83 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 45.11 mins               | 405.95 mins            |
|                                     |                | pages build and deployment          | 0.61 mins                | 3.65 mins              |
|                                     |                | Reload tpch                         | 14.89 mins               | 59.57 mins             |
|                                     |                | Reload hits                         | 63.19 mins               | 315.93 mins            |
|                                     |                | Reload ontime                       | 7.75 mins                | 38.73 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 2.53 mins      |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.38 mins                | 1.53 mins              |
|                                     |                | pages build and deployment          | 1.0 mins                 | 1.0 mins               |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 3.97 mins      |                                     |                          |                        |
|                                     |                | Rust                                | 1.98 mins                | 3.97 mins              |
| datafuselabs/opendal-redirect       | 2.17 mins      |                                     |                          |                        |
|                                     |                | CI                                  | 0.72 mins                | 2.17 mins              |
| datafuselabs/databend-client        | 990.63 mins    |                                     |                          |                        |
|                                     |                | ci                                  | 8.34 mins                | 942.82 mins            |
|                                     |                | publish                             | 3.68 mins                | 47.82 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/askbend                | 93.43 mins     |                                     |                          |                        |
|                                     |                | ci                                  | 3.34 mins                | 93.43 mins             |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'message': 'Server Error'}
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 3063.8 mins   |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 20.04 mins               | 180.33 mins            |
|                                    |               | BR & Lightning                                       | 1.08 mins                | 683.65 mins            |
|                                    |               | Dumpling                                             | 9.11 mins                | 1939.98 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.89 mins                | 228.58 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 210.57 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.85 mins                | 210.57 mins            |
| pingcap/kvproto                    | 1318.35 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 4.14 mins                | 417.77 mins            |
|                                    |               | Golang Test                                          | 1.35 mins                | 136.12 mins            |
|                                    |               | Rust Test                                            | 7.57 mins                | 764.47 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5587.57 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.8 mins                 | 5.63 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.2 mins                 | 68.78 mins             |
|                                    |               | external-link-check                                  | 12.67 mins               | 25.33 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 13.3 mins              |
|                                    |               | ci                                                   | 3.91 mins                | 4123.13 mins           |
|                                    |               | Links                                                | 2.49 mins                | 17.45 mins             |
|                                    |               | bot                                                  | 0.81 mins                | 17.82 mins             |
|                                    |               | cron                                                 | 1.41 mins                | 42.15 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.61 mins                | 601.63 mins            |
|                                    |               | Prevent Deletion                                     | 0.63 mins                | 672.33 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5620.68 mins  |                                                      |                          |                        |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                                   | 4.03 mins                | 4605.12 mins           |
|                                    |               | Trigger docs site update                             | 0.24 mins                | 66.13 mins             |
|                                    |               | Flush PDF by Version                                 | 0.25 mins                | 1.5 mins               |
|                                    |               | Flush All PDF                                        | 0.65 mins                | 2.58 mins              |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                                    | 0.45 mins                | 486.33 mins            |
|                                    |               | Links                                                | 2.46 mins                | 9.83 mins              |
|                                    |               | Upload media files to Qiniu when they change         | 0.5 mins                 | 4.03 mins              |
|                                    |               | Prevent Deletion                                     | 0.39 mins                | 445.15 mins            |
|                                    |               | Automatic Rebase                                     | 0.0 mins                 | 0.0 mins               |
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
| pingcap/blog-cn                    | 0.47 mins     |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn             | 0.47 mins                | 0.47 mins              |
|                                    |               | Upload media files to Qiniu and Aws when they change | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark                    | 3763.32 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.55 mins               | 839.92 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.23 mins                | 572.48 mins            |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 18.11 mins               | 1195.05 mins           |
|                                    |               | Follower Read test                                   | 9.54 mins                | 591.58 mins            |
|                                    |               | Close inactive issues                                | 0.24 mins                | 7.57 mins              |
|                                    |               | License checker                                      | 1.11 mins                | 77.63 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 6.84 mins                | 479.08 mins            |
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
| pingcap/go-ycsb                    | 16.62 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.45 mins                | 7.35 mins              |
|                                    |               | Publish artifacts to github release                  | 2.65 mins                | 2.65 mins              |
|                                    |               | Go                                                   | 2.21 mins                | 6.62 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 4366.13 mins  |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                                | 28.1 mins                | 2360.3 mins            |
|                                    |               | ci                                                   | 19.21 mins               | 1997.85 mins           |
|                                    |               | Close stale issues/prs                               | 0.27 mins                | 7.98 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 3880.92 mins  |                                                      |                          |                        |
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
| pingcap/log                        | 8.72 mins     |                                                      |                          |                        |
|                                    |               | Audit License                                        | 1.19 mins                | 5.97 mins              |
|                                    |               | Unit Test                                            | 0.55 mins                | 2.75 mins              |
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
| pingcap/diag                       | 63.15 mins    |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.13 mins               | 44.53 mins             |
|                                    |               | static-tests                                         | 3.72 mins                | 18.62 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 37676.95 mins |                                                      |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.26 mins                | 171.47 mins            |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 30.23 mins               | 6348.63 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                                     | 14.27 mins               | 2996.9 mins            |
|                                    |               | DM Chaos                                             | 27.6 mins                | 5796.08 mins           |
|                                    |               | DM Web UI Lint                                       | 1.13 mins                | 2.27 mins              |
|                                    |               | Upstream Database Switch                             | 16.72 mins               | 3512.12 mins           |
|                                    |               | Design Docs Lint                                     | 0.43 mins                | 16.63 mins             |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CDC Integration Tests                                | 18.08 mins               | 14554.78 mins          |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                                  | 12.72 mins               | 2670.87 mins           |
| pingcap/br                         | 81.5 mins     |                                                      |                          |                        |
|                                    |               | build                                                | 10.18 mins               | 61.07 mins             |
|                                    |               | compatibility-test                                   | 3.41 mins                | 20.43 mins             |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 125.07 mins   |                                                      |                          |                        |
|                                    |               | ci                                                   | 15.57 mins               | 124.58 mins            |
|                                    |               | release                                              | 0.48 mins                | 0.48 mins              |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 2.52 mins     |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 0.84 mins                | 2.52 mins              |
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
Error: {'total_count': 0, 'workflow_runs': []}
