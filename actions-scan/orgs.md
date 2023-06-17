
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 212.78 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 212.78 mins              | 212.78 mins            |
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
| webp-sh/webp_server_go     | 977.1 mins    |                                 |                          |                        |
|                            |               | CI check on every PR            | 5.72 mins                | 285.9 mins             |
|                            |               | CodeQL                          | 2.06 mins                | 144.05 mins            |
|                            |               | Integration Tests               | 2.38 mins                | 33.35 mins             |
|                            |               | Release Binaries                | 1.75 mins                | 7.02 mins              |
|                            |               | Build and release docker images | 25.34 mins               | 506.78 mins            |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 45177.63 mins |                                     |                          |                        |
|                                     |               | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 130.03 mins              | 3901.05 mins           |
|                                     |               | Cancel PR Workflow                  | 0.05 mins                | 11.1 mins              |
|                                     |               | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |               | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |               | Production                          | 107.08 mins              | 14776.55 mins          |
|                                     |               | Build Tool                          | 23.9 mins                | 47.8 mins              |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Benchmark                           | 6.9 mins                 | 1737.92 mins           |
|                                     |               | Release Repository                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.41 mins                | 524.12 mins            |
|                                     |               | Bindings Python                     | 16.81 mins               | 15736.05 mins          |
|                                     |               | Dev                                 | 17.85 mins               | 8443.05 mins           |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 1828.98 mins  |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 21.08 mins               | 1644.27 mins           |
|                                     |               | commit-message-check                | 0.94 mins                | 69.78 mins             |
|                                     |               | Unit test coverage                  | 4.56 mins                | 72.92 mins             |
|                                     |               | DevSkim                             | 1.11 mins                | 5.53 mins              |
|                                     |               | GPT refine markdown                 | 0.78 mins                | 32.12 mins             |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.06 mins                | 2.28 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.23 mins                | 2.08 mins              |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/weekly                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 268.18 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 8.94 mins                | 268.18 mins            |
| datafuselabs/databend-perf          | 31140.63 mins |                                     |                          |                        |
|                                     |               | Perf                                | 1836.51 mins             | 14692.07 mins          |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
|                                     |               | Reload tpch                         | 1440.19 mins             | 7200.95 mins           |
|                                     |               | Reload hits                         | 865.61 mins              | 4328.05 mins           |
|                                     |               | Reload ontime                       | 1229.89 mins             | 4919.57 mins           |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 28.4 mins     |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 2.18 mins                | 28.4 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 527.7 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 7.66 mins                | 482.63 mins            |
|                                     |               | publish                             | 3.66 mins                | 14.65 mins             |
|                                     |               | release                             | 15.21 mins               | 30.42 mins             |
| datafuselabs/askbend                | 104.05 mins   |                                     |                          |                        |
|                                     |               | ci                                  | 4.13 mins                | 82.7 mins              |
|                                     |               | release                             | 10.68 mins               | 21.35 mins             |
| datafuselabs/databend_fiddle        | 0.37 mins     |                                     |                          |                        |
|                                     |               | Pylint                              | 0.37 mins                | 0.37 mins              |
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
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb                       | 3450.7 mins    |                                                      |                          |                        |
|                                    |                | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR / Compatibility Test                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR & Lightning                                       | 0.91 mins                | 707.83 mins            |
|                                    |                | Dumpling                                             | 9.82 mins                | 2190.52 mins           |
|                                    |                | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | misc                                                 | 2.93 mins                | 521.85 mins            |
|                                    |                | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tipb                       | 69.33 mins     |                                                      |                          |                        |
|                                    |                | Unit Test                                            | 5.33 mins                | 69.33 mins             |
| pingcap/kvproto                    | 933.93 mins    |                                                      |                          |                        |
|                                    |                | C++ Test                                             | 4.58 mins                | 320.52 mins            |
|                                    |                | Golang Test                                          | 1.39 mins                | 97.0 mins              |
|                                    |                | Rust Test                                            | 7.38 mins                | 516.42 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                                      |                          |                        |
| pingcap/docs                       | 10416.28 mins  |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu when they change         | 0.71 mins                | 7.13 mins              |
|                                    |                | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                             | 0.18 mins                | 47.43 mins             |
|                                    |                | external-link-check                                  | 2020.61 mins             | 6061.82 mins           |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 67.1 mins              |
|                                    |                | ci                                                   | 3.28 mins                | 3386.53 mins           |
|                                    |                | Links                                                | 2.54 mins                | 10.15 mins             |
|                                    |                | bot                                                  | 0.72 mins                | 15.05 mins             |
|                                    |                | cron                                                 | 1.4 mins                 | 42.02 mins             |
|                                    |                | Links (Fail Fast)                                    | 0.42 mins                | 410.33 mins            |
|                                    |                | Prevent Deletion                                     | 0.35 mins                | 368.72 mins            |
|                                    |                | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4844.0 mins    |                                                      |                          |                        |
|                                    |                | Upload media files to Qiniu when they change         | 0.58 mins                | 0.58 mins              |
|                                    |                | Trigger docs site update                             | 0.18 mins                | 40.13 mins             |
|                                    |                | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                                     | 0.04 mins                | 52.57 mins             |
|                                    |                | ci                                                   | 4.23 mins                | 4061.28 mins           |
|                                    |                | Links                                                | 1.48 mins                | 5.93 mins              |
|                                    |                | Flush All PDF                                        | 0.24 mins                | 0.97 mins              |
|                                    |                | Links (Fail Fast)                                    | 0.39 mins                | 352.13 mins            |
|                                    |                | Prevent Deletion                                     | 0.34 mins                | 328.9 mins             |
|                                    |                | Flush PDF by Version                                 | 0.21 mins                | 1.5 mins               |
| pingcap/tidb-binlog                | 0.0 mins       |                                                      |                          |                        |
| pingcap/sqlgram                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/mydumper                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/blog                       | 0.0 mins       |                                                      |                          |                        |
|                                    |                | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog                | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tispark                    | 1659.83 mins   |                                                      |                          |                        |
|                                    |                | TLS test                                             | 11.94 mins               | 394.1 mins             |
|                                    |                | alter-primary-key-false-test                         | 13.34 mins               | 173.42 mins            |
|                                    |                | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                               | 14.82 mins               | 563.32 mins            |
|                                    |                | Follower Read test                                   | 8.79 mins                | 290.0 mins             |
|                                    |                | Close inactive issues                                | 0.23 mins                | 6.78 mins              |
|                                    |                | License checker                                      | 1.13 mins                | 37.28 mins             |
|                                    |                | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                               | 5.91 mins                | 194.93 mins            |
| pingcap/octopus                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins       |                                                      |                          |                        |
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
| pingcap/go-ycsb                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Docker Image CI                                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins       |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins       |                                                      |                          |                        |
|                                    |                | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-operator              | 5865.48 mins   |                                                      |                          |                        |
|                                    |                | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/cd.yml                             | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                                | 22.71 mins               | 2815.83 mins           |
|                                    |                | ci                                                   | 18.44 mins               | 3042.32 mins           |
|                                    |                | Close stale issues/prs                               | 0.24 mins                | 7.33 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 673.0 mins     |                                                      |                          |                        |
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
| pingcap/log                        | 0.0 mins       |                                                      |                          |                        |
|                                    |                | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins       |                                                      |                          |                        |
|                                    |                | .github/workflows/assign_project.yml                 | 0.0 mins                 | 0.0 mins               |
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
| pingcap/diag                       | 17.25 mins     |                                                      |                          |                        |
|                                    |                | reprotest                                            | 10.27 mins               | 10.27 mins             |
|                                    |                | static-tests                                         | 3.49 mins                | 6.98 mins              |
| pingcap/sqlsmith                   | 0.0 mins       |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                                      |                          |                        |
| pingcap/tiflow                     | 153953.53 mins |                                                      |                          |                        |
|                                    |                | Auto Assign to Bugs and Questions                    | 0.24 mins                | 116.75 mins            |
|                                    |                | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Check & Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                                | 21.73 mins               | 4563.23 mins           |
|                                    |                | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Binlog 999999                                     | 14.86 mins               | 3121.38 mins           |
|                                    |                | DM Chaos                                             | 13.76 mins               | 2890.18 mins           |
|                                    |                | DM Web UI Lint                                       | 1.88 mins                | 1.88 mins              |
|                                    |                | Upstream Database Switch                             | 16.06 mins               | 3372.32 mins           |
|                                    |                | Design Docs Lint                                     | 0.36 mins                | 18.02 mins             |
|                                    |                | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | CDC Integration Tests                                | 24.44 mins               | 15937.72 mins          |
|                                    |                | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade DM via TiUP                                  | 200.62 mins              | 42129.48 mins          |
| pingcap/br                         | 0.0 mins       |                                                      |                          |                        |
|                                    |                | build                                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                                   | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 813.85 mins    |                                                      |                          |                        |
|                                    |                | ci                                                   | 27.13 mins               | 813.85 mins            |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins       |                                                      |                          |                        |
| pingcap/go-tpc                     | 0.0 mins       |                                                      |                          |                        |
|                                    |                | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | workflow                                             | 0.0 mins                 | 0.0 mins               |
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
Error: {'total_count': 0, 'workflow_runs': []}
