
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
| knatnetwork/github-runner        | 252.32 mins   |                        |                          |                        |
|                                  |               | Build Runner Image     | 84.11 mins               | 252.32 mins            |
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
| webp-sh/webp_server_go              | 365.3 mins    |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.14 mins                | 37.3 mins              |
|                                     |               | CI check on every push          | 2.43 mins                | 12.15 mins             |
|                                     |               | CodeQL                          | 1.92 mins                | 36.45 mins             |
|                                     |               | Integration Tests               | 2.78 mins                | 25.0 mins              |
|                                     |               | Release Binaries                | 2.27 mins                | 4.55 mins              |
|                                     |               | Build and release docker images | 35.69 mins               | 249.85 mins            |
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
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 88087.52 mins |                                     |                          |                        |
|                                     |               | Release                             | 89.17 mins               | 3923.37 mins           |
|                                     |               | Cancel PR Workflow                  | 0.08 mins                | 21.87 mins             |
|                                     |               | Production                          | 91.06 mins               | 18849.28 mins          |
|                                     |               | Crowdin Action                      | 3.23 mins                | 788.72 mins            |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.44 mins                | 751.98 mins            |
|                                     |               | Dev                                 | 21.62 mins               | 29835.27 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 30.39 mins               | 3099.43 mins           |
|                                     |               | PR Assistant                        | 0.19 mins                | 422.08 mins            |
|                                     |               | Push on main                        | 2.93 mins                | 779.73 mins            |
|                                     |               | Bindings Python                     | 21.55 mins               | 29542.05 mins          |
|                                     |               | Build Tool                          | 18.43 mins               | 73.73 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 692.47 mins   |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 22.94 mins               | 688.3 mins             |
|                                     |               | commit-message-check                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit test coverage                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | DevSkim                             | 0.84 mins                | 3.35 mins              |
|                                     |               | GPT refine markdown                 | 0.26 mins                | 0.52 mins              |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.05 mins                | 0.1 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.2 mins                 | 0.2 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
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
| datafuselabs/opensrv                | 127.77 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 4.26 mins                | 127.77 mins            |
| datafuselabs/databend-perf          | 829.68 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 44.35 mins               | 620.95 mins            |
|                                     |               | pages build and deployment          | 0.61 mins                | 3.05 mins              |
|                                     |               | Reload tpch                         | 3.09 mins                | 12.35 mins             |
|                                     |               | Reload hits                         | 9.16 mins                | 155.77 mins            |
|                                     |               | Reload ontime                       | 9.39 mins                | 37.57 mins             |
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
| datafuselabs/databend-go            | 3.73 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.93 mins                | 3.73 mins              |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-py            | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | Release on Version Change           | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-sqlalchemy    | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 374.8 mins    |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 37.48 mins               | 374.8 mins             |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 6.52 mins     |                                     |                          |                        |
|                                     |               | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 1.3 mins                 | 6.52 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1392.62 mins  |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 4.18 mins                | 301.28 mins            |
|                                     |               | Bindings Python                     | 4.46 mins                | 200.7 mins             |
|                                     |               | CI                                  | 7.97 mins                | 749.08 mins            |
|                                     |               | PR Assistant                        | 0.23 mins                | 17.02 mins             |
|                                     |               | Publish                             | 10.23 mins               | 51.15 mins             |
|                                     |               | Release                             | 12.23 mins               | 73.38 mins             |
| datafuselabs/askbend                | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins      |                                     |                          |                        |
|                                     |               | Pylint                              | 0.0 mins                 | 0.0 mins               |
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
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                              |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                              |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                              |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                              |                          |                        |
| pingcap/check                      | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb                       | 5767.92 mins   |                                              |                          |                        |
|                                    |                | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR & Lightning                               | 5.13 mins                | 3286.2 mins            |
|                                    |                | Dumpling                                     | 10.37 mins               | 2261.53 mins           |
|                                    |                | misc                                         | 2.65 mins                | 219.93 mins            |
|                                    |                | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                              |                          |                        |
| pingcap/tipb                       | 53.57 mins     |                                              |                          |                        |
|                                    |                | Unit Test                                    | 6.7 mins                 | 53.57 mins             |
| pingcap/kvproto                    | 652.23 mins    |                                              |                          |                        |
|                                    |                | C++ Test                                     | 7.42 mins                | 267.23 mins            |
|                                    |                | Golang Test                                  | 1.4 mins                 | 60.37 mins             |
|                                    |                | Rust Test                                    | 7.55 mins                | 324.63 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                              |                          |                        |
| pingcap/docs                       | 3482.1 mins    |                                              |                          |                        |
|                                    |                | Upload media files to Qiniu when they change | 0.49 mins                | 5.42 mins              |
|                                    |                | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                     | 0.2 mins                 | 40.48 mins             |
|                                    |                | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                             | 0.04 mins                | 43.22 mins             |
|                                    |                | ci                                           | 3.63 mins                | 2716.3 mins            |
|                                    |                | Links                                        | 1.54 mins                | 6.15 mins              |
|                                    |                | bot                                          | 0.74 mins                | 16.38 mins             |
|                                    |                | cron                                         | 2.47 mins                | 12.33 mins             |
|                                    |                | Links (Fail Fast)                            | 0.46 mins                | 340.23 mins            |
|                                    |                | Prevent Deletion                             | 0.39 mins                | 301.58 mins            |
|                                    |                | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3920.63 mins   |                                              |                          |                        |
|                                    |                | ci                                           | 3.91 mins                | 3209.35 mins           |
|                                    |                | Trigger docs site update                     | 0.2 mins                 | 31.17 mins             |
|                                    |                | Flush PDF by Version                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Flush All PDF                                | 0.26 mins                | 1.3 mins               |
|                                    |                | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Links (Fail Fast)                            | 0.42 mins                | 341.78 mins            |
|                                    |                | Links                                        | 1.31 mins                | 5.25 mins              |
|                                    |                | Upload media files to Qiniu when they change | 0.53 mins                | 1.05 mins              |
|                                    |                | Prevent Deletion                             | 0.36 mins                | 299.98 mins            |
|                                    |                | Automatic Rebase                             | 0.04 mins                | 30.75 mins             |
| pingcap/tidb-binlog                | 0.0 mins       |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins       |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins       |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins       |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins       |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins       |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins       |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins       |                                              |                          |                        |
| pingcap/tispark                    | 376.72 mins    |                                              |                          |                        |
|                                    |                | TLS test                                     | 14.55 mins               | 87.32 mins             |
|                                    |                | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                       | 16.79 mins               | 167.85 mins            |
|                                    |                | Follower Read test                           | 11.12 mins               | 66.72 mins             |
|                                    |                | Close inactive issues                        | 0.26 mins                | 7.88 mins              |
|                                    |                | License checker                              | 1.02 mins                | 6.15 mins              |
|                                    |                | verify                                       | 6.8 mins                 | 40.8 mins              |
| pingcap/octopus                    | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-tools                 | 0.0 mins       |                                              |                          |                        |
| pingcap/jepsen                     | 0.0 mins       |                                              |                          |                        |
| pingcap/kubeadm-dind-cluster       | 0.0 mins       |                                              |                          |                        |
| pingcap/chaos                      | 0.0 mins       |                                              |                          |                        |
| pingcap/meetup                     | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/mysqlx-driver              | 0.0 mins       |                                              |                          |                        |
| pingcap/campaign                   | 0.0 mins       |                                              |                          |                        |
| pingcap/community                  | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-lightning             | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-ctl                   | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-inspect-tools         | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-vision                | 0.0 mins       |                                              |                          |                        |
| pingcap/thirdparty-ops             | 0.0 mins       |                                              |                          |                        |
| pingcap/tla-plus                   | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-docker-compose        | 0.0 mins       |                                              |                          |                        |
| pingcap/go-ycsb                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | Docker Image CI                              | 0.0 mins                 | 0.0 mins               |
|                                    |                | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins       |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins       |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins       |                                              |                          |                        |
|                                    |                | testbuild                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-operator              | 5221.53 mins   |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | ci                                           | 49.57 mins               | 5204.72 mins           |
|                                    |                | Close stale issues/prs                       | 0.56 mins                | 16.82 mins             |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 806.22 mins    |                                              |                          |                        |
|                                    |                | Pull Request CI                              | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins       |                                              |                          |                        |
| pingcap/parser                     | 0.0 mins       |                                              |                          |                        |
| pingcap/benchmarksql               | 0.0 mins       |                                              |                          |                        |
| pingcap/gofail                     | 0.0 mins       |                                              |                          |                        |
| pingcap/work-reporter              | 0.0 mins       |                                              |                          |                        |
| pingcap/dm                         | 0.0 mins       |                                              |                          |                        |
|                                    |                | Test binlog 999999                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upgrade via TiUP                             | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upstream database switch                     | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins       |                                              |                          |                        |
| pingcap/log                        | 0.0 mins       |                                              |                          |                        |
|                                    |                | Audit License                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins       |                                              |                          |                        |
| pingcap/poco                       | 0.0 mins       |                                              |                          |                        |
| pingcap/capnproto                  | 0.0 mins       |                                              |                          |                        |
| pingcap/boost-extra                | 0.0 mins       |                                              |                          |                        |
| pingcap/kdt                        | 0.0 mins       |                                              |                          |                        |
| pingcap/failpoint                  | 0.0 mins       |                                              |                          |                        |
|                                    |                | Build & Test                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins       |                                              |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins       |                                              |                          |                        |
| pingcap/tidiff                     | 0.0 mins       |                                              |                          |                        |
| pingcap/fn                         | 0.0 mins       |                                              |                          |                        |
| pingcap/diag                       | 206.83 mins    |                                              |                          |                        |
|                                    |                | reprotest                                    | 11.2 mins                | 145.57 mins            |
|                                    |                | static-tests                                 | 3.6 mins                 | 61.27 mins             |
| pingcap/sqlsmith                   | 0.0 mins       |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                              |                          |                        |
| pingcap/tiflow                     | 156617.98 mins |                                              |                          |                        |
|                                    |                | Auto Assign to Bugs and Questions            | 0.23 mins                | 55.45 mins             |
|                                    |                | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                        | 26.45 mins               | 5555.53 mins           |
|                                    |                | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Binlog 999999                             | 16.9 mins                | 3548.32 mins           |
|                                    |                | DM Chaos                                     | 14.84 mins               | 3116.45 mins           |
|                                    |                | DM Web UI Lint                               | 1.19 mins                | 3.57 mins              |
|                                    |                | Upstream Database Switch                     | 20.22 mins               | 4246.62 mins           |
|                                    |                | Design Docs Lint                             | 0.36 mins                | 3.6 mins               |
|                                    |                | Upgrade DM via TiUP                          | 200.61 mins              | 42127.5 mins           |
| pingcap/br                         | 0.0 mins       |                                              |                          |                        |
|                                    |                | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                              |                          |                        |
| pingcap/advanced-statefulset       | 871.85 mins    |                                              |                          |                        |
|                                    |                | ci                                           | 19.81 mins               | 871.85 mins            |
|                                    |                | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins       |                                              |                          |                        |
| pingcap/go-tpc                     | 12.83 mins     |                                              |                          |                        |
|                                    |                | release                                      | 0.34 mins                | 0.68 mins              |
|                                    |                | workflow                                     | 1.52 mins                | 12.15 mins             |
| pingcap/kops                       | 0.0 mins       |                                              |                          |                        |
| pingcap/sysutil                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | Test                                         | 0.0 mins                 | 0.0 mins               |
| pingcap/discourse                  | 0.0 mins       |                                              |                          |                        |
| pingcap/discourse-chat-integration | 0.0 mins       |                                              |                          |                        |
| pingcap/discourse_docker           | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-helper                | 0.0 mins       |                                              |                          |                        |
| pingcap/dumpling                   | 0.0 mins       |                                              |                          |                        |
|                                    |                | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tipocket                   | 0.0 mins       |                                              |                          |                        |
|                                    |                | Build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | Build-workflow                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Pre-Check                                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | Test                                         | 0.0 mins                 | 0.0 mins               |
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
