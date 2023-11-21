
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
| knatnetwork/github-runner        | 208.9 mins    |                        |                          |                        |
|                                  |               | Build Runner Image     | 208.9 mins               | 208.9 mins             |
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
| webp-sh/webp_server_go              | 323.2 mins    |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.81 mins                | 72.22 mins             |
|                                     |               | CI check on every push          | 1.98 mins                | 9.88 mins              |
|                                     |               | CodeQL                          | 1.65 mins                | 39.58 mins             |
|                                     |               | Integration Tests               | 2.77 mins                | 41.53 mins             |
|                                     |               | Release Binaries                | 7.1 mins                 | 7.1 mins               |
|                                     |               | Build and release docker images | 25.48 mins               | 152.88 mins            |
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
| datafuselabs/databend               | 76011.5 mins  |                                     |                          |                        |
|                                     |               | Release                             | 88.29 mins               | 4061.17 mins           |
|                                     |               | Cancel PR Workflow                  | 0.04 mins                | 12.45 mins             |
|                                     |               | Production                          | 110.83 mins              | 24937.32 mins          |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.36 mins                | 594.18 mins            |
|                                     |               | Dev                                 | 19.66 mins               | 29937.15 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 32.4 mins                | 1782.07 mins           |
|                                     |               | PR Assistant                        | 0.26 mins                | 612.05 mins            |
|                                     |               | Push on main                        | 2.75 mins                | 839.45 mins            |
|                                     |               | Bindings Python                     | 10.93 mins               | 13162.3 mins           |
|                                     |               | Build Tool                          | 24.46 mins               | 73.37 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 1495.83 mins  |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 16.42 mins               | 1346.8 mins            |
|                                     |               | commit-message-check                | 0.96 mins                | 71.27 mins             |
|                                     |               | Unit test coverage                  | 3.77 mins                | 56.55 mins             |
|                                     |               | DevSkim                             | 0.83 mins                | 3.33 mins              |
|                                     |               | GPT refine markdown                 | 0.28 mins                | 12.37 mins             |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.04 mins                | 1.87 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.36 mins                | 3.65 mins              |
|                                     |               | Release                             | 0.0 mins                 | 0.0 mins               |
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
| datafuselabs/opensrv                | 1202.17 mins  |                                     |                          |                        |
|                                     |               | CI                                  | 31.64 mins               | 1202.17 mins           |
| datafuselabs/databend-perf          | 136.02 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 8.51 mins                | 93.63 mins             |
|                                     |               | pages build and deployment          | 0.55 mins                | 2.22 mins              |
|                                     |               | Reload hits                         | 10.04 mins               | 40.17 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release Charts                      | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-go            | 26.68 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 0.95 mins                | 26.68 mins             |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-py            | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release on Version Change           | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-sqlalchemy    | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 8.07 mins     |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 1.34 mins                | 8.07 mins              |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 6.32 mins     |                                     |                          |                        |
|                                     |               | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 1.26 mins                | 6.32 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 2543.17 mins  |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 11.45 mins               | 882.0 mins             |
|                                     |               | Bindings Python                     | 7.44 mins                | 528.18 mins            |
|                                     |               | CI                                  | 7.98 mins                | 933.48 mins            |
|                                     |               | PR Assistant                        | 0.23 mins                | 21.55 mins             |
|                                     |               | Publish                             | 7.37 mins                | 58.95 mins             |
|                                     |               | Release                             | 14.88 mins               | 119.0 mins             |
| datafuselabs/askbend                | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins      |                                     |                          |                        |
|                                     |               | Pylint                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-docs          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-udf           | 7.42 mins     |                                     |                          |                        |
|                                     |               | Python                              | 0.93 mins                | 7.42 mins              |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+

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
| pingcap/tidb                       | 6524.52 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR & Lightning                               | 4.23 mins                | 4645.6 mins            |
|                                    |               | Dumpling                                     | 9.63 mins                | 1578.85 mins           |
|                                    |               | misc                                         | 2.44 mins                | 299.65 mins            |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/kvproto                    | 287.22 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 14.34 mins               | 186.48 mins            |
|                                    |               | Golang Test                                  | 1.32 mins                | 17.1 mins              |
|                                    |               | Rust Test                                    | 6.43 mins                | 83.63 mins             |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3364.55 mins  |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 0.52 mins                | 6.22 mins              |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.21 mins                | 43.93 mins             |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 42.75 mins             |
|                                    |               | ci                                           | 3.42 mins                | 2539.97 mins           |
|                                    |               | Links                                        | 1.77 mins                | 8.85 mins              |
|                                    |               | bot                                          | 0.71 mins                | 15.0 mins              |
|                                    |               | cron                                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.51 mins                | 366.23 mins            |
|                                    |               | Prevent Deletion                             | 0.42 mins                | 319.93 mins            |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | translation                                  | 2.71 mins                | 21.67 mins             |
| pingcap/docs-cn                    | 3047.57 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 4.0 mins                 | 2483.25 mins           |
|                                    |               | Trigger docs site update                     | 0.2 mins                 | 32.85 mins             |
|                                    |               | Flush PDF by Version                         | 0.28 mins                | 1.13 mins              |
|                                    |               | Flush All PDF                                | 0.28 mins                | 1.4 mins               |
|                                    |               | Links (Fail Fast)                            | 0.44 mins                | 269.2 mins             |
|                                    |               | Links                                        | 1.85 mins                | 9.23 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.53 mins                | 3.17 mins              |
|                                    |               | Prevent Deletion                             | 0.34 mins                | 216.08 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 31.25 mins             |
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
| pingcap/tispark                    | 70.57 mins    |                                              |                          |                        |
|                                    |               | TLS test                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 15.88 mins               | 63.52 mins             |
|                                    |               | Follower Read test                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | Close inactive issues                        | 0.23 mins                | 7.05 mins              |
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
| pingcap/go-ycsb                    | 9.83 mins     |                                              |                          |                        |
|                                    |               | Docker Image CI                              | 2.35 mins                | 4.7 mins               |
|                                    |               | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                           | 2.57 mins                | 5.13 mins              |
| pingcap/tispark-test-data          | 0.0 mins      |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-operator              | 2158.03 mins  |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                           | 15.58 mins               | 2150.0 mins            |
|                                    |               | Close stale issues/prs                       | 0.27 mins                | 8.03 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 681.72 mins   |                                              |                          |                        |
|                                    |               | Pull Request CI                              | 52.44 mins               | 681.72 mins            |
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
| pingcap/diag                       | 36.7 mins     |                                              |                          |                        |
|                                    |               | release-diag                                 | 4.18 mins                | 4.18 mins              |
|                                    |               | reprotest                                    | 10.49 mins               | 20.98 mins             |
|                                    |               | static-tests                                 | 3.84 mins                | 11.53 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 62271.72 mins |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.27 mins                | 78.73 mins             |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 20.94 mins               | 4398.28 mins           |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 13.91 mins               | 2921.2 mins            |
|                                    |               | DM Chaos                                     | 14.0 mins                | 2939.52 mins           |
|                                    |               | DM Web UI Lint                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream Database Switch                     | 16.49 mins               | 3462.62 mins           |
|                                    |               | Design Docs Lint                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                          | 200.61 mins              | 42128.57 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 420.12 mins   |                                              |                          |                        |
|                                    |               | ci                                           | 14.0 mins                | 420.12 mins            |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
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
