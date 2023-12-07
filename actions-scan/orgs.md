
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+----------------------------------+---------------+------------------------+--------------------------+------------------------+
| Repo                             | Total Runtime | Workflow Name          | Workflow Average Runtime | Workflow Total Runtime |
+----------------------------------+---------------+------------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless      | 0.0 mins      |                        |                          |                        |
| knatnetwork/g2fs-serverless      | 0.0 mins      |                        |                          |                        |
| knatnetwork/github-runner        | 0.0 mins      |                        |                          |                        |
|                                  |               | Build Runner Image     | 0.0 mins                 | 0.0 mins               |
| knatnetwork/github-runner-kms    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder   | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/github-runner-kms-rs | 0.0 mins      |                        |                          |                        |
|                                  |               | Build Image            | 0.0 mins                 | 0.0 mins               |
+----------------------------------+---------------+------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>webp-sh</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node            | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go              | 361.67 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 3.14 mins                | 37.72 mins             |
|                                     |               | CI check on every push          | 1.69 mins                | 15.2 mins              |
|                                     |               | CodeQL                          | 1.46 mins                | 38.02 mins             |
|                                     |               | Integration Tests               | 2.46 mins                | 29.48 mins             |
|                                     |               | Release Binaries                | 4.97 mins                | 9.93 mins              |
|                                     |               | Build and release docker images | 21.03 mins               | 231.32 mins            |
| webp-sh/webp                        | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python          | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java            | 0.0 mins      |                                 |                          |                        |
|                                     |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/gowebp                      | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif                     | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh                | 0.0 mins      |                                 |                          |                        |
| webp-sh/libvips                     | 0.0 mins      |                                 |                          |                        |
|                                     |               | Build and release docker images | 0.0 mins                 | 0.0 mins               |
| webp-sh/halo-plugin-webp-cloud      | 0.0 mins      |                                 |                          |                        |
|                                     |               | Build Plugin JAR File           | 0.0 mins                 | 0.0 mins               |
| webp-sh/wordpress-plugin-webp-cloud | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_bench                  | 0.0 mins      |                                 |                          |                        |
| webp-sh/blog-comments               | 0.0 mins      |                                 |                          |                        |
| webp-sh/govips                      | 0.0 mins      |                                 |                          |                        |
|                                     |               | build                           | 0.0 mins                 | 0.0 mins               |
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+

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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 64339.42 mins |                                     |                          |                        |
|                                     |               | Release                             | 82.11 mins               | 3694.88 mins           |
|                                     |               | Cancel PR Workflow                  | 0.04 mins                | 9.82 mins              |
|                                     |               | Production                          | 86.05 mins               | 18242.75 mins          |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.3 mins                 | 462.33 mins            |
|                                     |               | Dev                                 | 18.96 mins               | 26937.67 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 29.85 mins               | 1193.87 mins           |
|                                     |               | PR Assistant                        | 0.25 mins                | 535.25 mins            |
|                                     |               | Push on main                        | 2.28 mins                | 516.73 mins            |
|                                     |               | Bindings Python                     | 10.17 mins               | 12612.97 mins          |
|                                     |               | Build Tool                          | 16.64 mins               | 133.15 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 2039.32 mins  |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 12.94 mins               | 1772.43 mins           |
|                                     |               | commit-message-check                | 0.95 mins                | 129.18 mins            |
|                                     |               | Unit test coverage                  | 3.19 mins                | 121.13 mins            |
|                                     |               | DevSkim                             | 0.68 mins                | 2.72 mins              |
|                                     |               | GPT refine markdown                 | 0.23 mins                | 8.05 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.04 mins                | 1.5 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.19 mins                | 0.93 mins              |
|                                     |               | Release                             | 1.12 mins                | 3.37 mins              |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins      |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins      |                                     |                          |                        |
| datafuselabs/weekly                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins      |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 152.37 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 4.01 mins                | 152.37 mins            |
| datafuselabs/databend-perf          | 110.82 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 6.0 mins                 | 65.97 mins             |
|                                     |               | pages build and deployment          | 0.6 mins                 | 3.0 mins               |
|                                     |               | Reload hits                         | 8.37 mins                | 41.85 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-go            | 5.85 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.84 mins                | 5.85 mins              |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-py            | 6.85 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.6 mins                 | 6.02 mins              |
|                                     |               | Release on Version Change           | 0.42 mins                | 0.83 mins              |
| datafuselabs/databend-sqlalchemy    | 40.92 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 0.61 mins                | 18.28 mins             |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 16.47 mins    |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 1.27 mins                | 16.47 mins             |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 5.57 mins     |                                     |                          |                        |
|                                     |               | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 0.93 mins                | 5.57 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1599.1 mins   |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 10.91 mins               | 643.95 mins            |
|                                     |               | Bindings Python                     | 6.91 mins                | 304.08 mins            |
|                                     |               | CI                                  | 7.78 mins                | 536.53 mins            |
|                                     |               | PR Assistant                        | 0.2 mins                 | 10.25 mins             |
|                                     |               | Publish                             | 4.61 mins                | 27.68 mins             |
|                                     |               | Release                             | 12.77 mins               | 76.6 mins              |
| datafuselabs/askbend                | 13.68 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 6.84 mins                | 13.68 mins             |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins      |                                     |                          |                        |
|                                     |               | Pylint                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-docs          | 498.22 mins   |                                     |                          |                        |
|                                     |               | build                               | 5.08 mins                | 498.22 mins            |
| datafuselabs/databend-udf           | 7.42 mins     |                                     |                          |                        |
|                                     |               | Python                              | 0.93 mins                | 7.42 mins              |
| datafuselabs/wizard                 | 0.0 mins      |                                     |                          |                        |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                              |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                              |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                              |                          |                        |
| pingcap/check                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb                       | 5358.03 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR & Lightning                               | 3.36 mins                | 3313.02 mins           |
|                                    |               | Dumpling                                     | 8.32 mins                | 1614.2 mins            |
|                                    |               | misc                                         | 2.2 mins                 | 429.38 mins            |
|                                    |               | MySQL Tests                                  | 1.22 mins                | 1.22 mins              |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/kvproto                    | 268.77 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 5.9 mins                 | 123.92 mins            |
|                                    |               | Golang Test                                  | 1.13 mins                | 23.72 mins             |
|                                    |               | Rust Test                                    | 5.77 mins                | 121.13 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3665.38 mins  |                                              |                          |                        |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | bot                                          | 0.68 mins                | 15.05 mins             |
|                                    |               | ci                                           | 2.79 mins                | 2590.05 mins           |
|                                    |               | cron                                         | 0.35 mins                | 7.78 mins              |
|                                    |               | Trigger docs site update                     | 0.22 mins                | 67.7 mins              |
|                                    |               | JA Full Translation (Google version)         | 6.48 mins                | 19.45 mins             |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.5 mins                 | 438.85 mins            |
|                                    |               | Links                                        | 1.57 mins                | 6.3 mins               |
|                                    |               | Upload media files to Qiniu when they change | 0.6 mins                 | 8.4 mins               |
|                                    |               | Prevent Deletion                             | 0.45 mins                | 428.17 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 61.97 mins             |
|                                    |               | translation                                  | 2.71 mins                | 21.67 mins             |
| pingcap/docs-cn                    | 2864.47 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 3.1 mins                 | 2169.72 mins           |
|                                    |               | Trigger docs site update                     | 0.19 mins                | 43.45 mins             |
|                                    |               | Flush PDF by Version                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | Flush All PDF                                | 0.24 mins                | 0.97 mins              |
|                                    |               | Links (Fail Fast)                            | 0.48 mins                | 318.3 mins             |
|                                    |               | Links                                        | 1.68 mins                | 6.72 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.53 mins                | 3.17 mins              |
|                                    |               | Prevent Deletion                             | 0.39 mins                | 280.9 mins             |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 41.25 mins             |
| pingcap/tidb-binlog                | 0.0 mins      |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark                    | 57.63 mins    |                                              |                          |                        |
|                                    |               | TLS test                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 12.78 mins               | 51.13 mins             |
|                                    |               | Follower Read test                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | Close inactive issues                        | 0.22 mins                | 6.5 mins               |
|                                    |               | License checker                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                       | 0.0 mins                 | 0.0 mins               |
| pingcap/octopus                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins      |                                              |                          |                        |
| pingcap/jepsen                     | 0.0 mins      |                                              |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins      |                                              |                          |                        |
| pingcap/chaos                      | 0.0 mins      |                                              |                          |                        |
| pingcap/meetup                     | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins      |                                              |                          |                        |
| pingcap/campaign                   | 0.0 mins      |                                              |                          |                        |
| pingcap/community                  | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-vision                | 0.0 mins      |                                              |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins      |                                              |                          |                        |
| pingcap/tla-plus                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins      |                                              |                          |                        |
| pingcap/go-ycsb                    | 4.32 mins     |                                              |                          |                        |
|                                    |               | Docker Image CI                              | 2.13 mins                | 2.13 mins              |
|                                    |               | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                           | 2.18 mins                | 2.18 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-operator              | 4143.92 mins  |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                           | 18.55 mins               | 4136.55 mins           |
|                                    |               | Close stale issues/prs                       | 0.25 mins                | 7.37 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 171.93 mins   |                                              |                          |                        |
|                                    |               | Pull Request CI                              | 57.31 mins               | 171.93 mins            |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                              |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                              |                          |                        |
| pingcap/benchmarksql               | 0.0 mins      |                                              |                          |                        |
| pingcap/gofail                     | 0.0 mins      |                                              |                          |                        |
| pingcap/work-reporter              | 0.0 mins      |                                              |                          |                        |
| pingcap/dm                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins      |                                              |                          |                        |
| pingcap/log                        | 0.0 mins      |                                              |                          |                        |
|                                    |               | Audit License                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins      |                                              |                          |                        |
| pingcap/poco                       | 0.0 mins      |                                              |                          |                        |
| pingcap/capnproto                  | 0.0 mins      |                                              |                          |                        |
| pingcap/boost-extra                | 0.0 mins      |                                              |                          |                        |
| pingcap/kdt                        | 0.0 mins      |                                              |                          |                        |
| pingcap/failpoint                  | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                              |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                              |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                              |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                              |                          |                        |
| pingcap/diag                       | 13.92 mins    |                                              |                          |                        |
|                                    |               | release-diag                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                    | 9.87 mins                | 9.87 mins              |
|                                    |               | static-tests                                 | 4.05 mins                | 4.05 mins              |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 60233.1 mins  |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.24 mins                | 110.43 mins            |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 17.87 mins               | 3752.6 mins            |
|                                    |               | DM Binlog 999999                             | 10.56 mins               | 2217.7 mins            |
|                                    |               | DM Chaos                                     | 11.76 mins               | 2469.88 mins           |
|                                    |               | DM Web UI Lint                               | 1.23 mins                | 2.47 mins              |
|                                    |               | Upstream Database Switch                     | 12.52 mins               | 2629.52 mins           |
|                                    |               | Design Docs Lint                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                          | 200.61 mins              | 42128.8 mins           |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 479.2 mins    |                                              |                          |                        |
|                                    |               | ci                                           | 13.29 mins               | 478.3 mins             |
|                                    |               | release                                      | 0.3 mins                 | 0.9 mins               |
| pingcap/style-guide                | 0.0 mins      |                                              |                          |                        |
| pingcap/go-tpc                     | 0.0 mins      |                                              |                          |                        |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                     | 0.0 mins                 | 0.0 mins               |
| pingcap/kops                       | 0.0 mins      |                                              |                          |                        |
| pingcap/sysutil                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins      |                                              |                          |                        |
| pingcap/discourse-chat-integration | 0.0 mins      |                                              |                          |                        |
| pingcap/discourse_docker           | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-helper                | 0.0 mins      |                                              |                          |                        |
| pingcap/dumpling                   | 0.0 mins      |                                              |                          |                        |
|                                    |               | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tipocket                   | 0.0 mins      |                                              |                          |                        |
|                                    |               | Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build-workflow                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Pre-Check                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Test                                         | 0.0 mins                 | 0.0 mins               |
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
