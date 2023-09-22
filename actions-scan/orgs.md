
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
| knatnetwork/github-runner        | 773.03 mins   |                        |                          |                        |
|                                  |               | Build Runner Image     | 193.26 mins              | 773.03 mins            |
| knatnetwork/github-runner-kms    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-builder   | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/clickhouse-server    | 0.0 mins      |                        |                          |                        |
|                                  |               | No workflow name(why?) | 0.0 mins                 | 0.0 mins               |
| knatnetwork/github-runner-kms-rs | 442.28 mins   |                        |                          |                        |
|                                  |               | Build Image            | 73.71 mins               | 442.28 mins            |
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
| webp-sh/webp_server_go              | 364.53 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.14 mins                | 37.3 mins              |
|                                     |               | CI check on every push          | 2.43 mins                | 12.15 mins             |
|                                     |               | CodeQL                          | 1.98 mins                | 35.68 mins             |
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
| datafuselabs/databend               | 72288.85 mins |                                     |                          |                        |
|                                     |               | Release                             | 110.39 mins              | 4967.35 mins           |
|                                     |               | Cancel PR Workflow                  | 0.06 mins                | 16.75 mins             |
|                                     |               | Production                          | 92.52 mins               | 18967.43 mins          |
|                                     |               | Crowdin Action                      | 3.37 mins                | 867.23 mins            |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.42 mins                | 716.9 mins             |
|                                     |               | Dev                                 | 19.15 mins               | 25233.23 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 34.04 mins               | 2757.22 mins           |
|                                     |               | PR Assistant                        | 0.19 mins                | 410.2 mins             |
|                                     |               | Push on main                        | 3.08 mins                | 601.08 mins            |
|                                     |               | Bindings Python                     | 20.95 mins               | 17740.72 mins          |
|                                     |               | Build Tool                          | 10.73 mins               | 10.73 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 688.18 mins   |                                     |                          |                        |
|                                     |               | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 22.82 mins               | 684.63 mins            |
|                                     |               | commit-message-check                | 0.0 mins                 | 0.0 mins               |
|                                     |               | Unit test coverage                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | DevSkim                             | 0.89 mins                | 3.55 mins              |
|                                     |               | GPT refine markdown                 | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.0 mins                 | 0.0 mins               |
|                                     |               | .github/workflows/issue-welcome.yml | 0.0 mins                 | 0.0 mins               |
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
| datafuselabs/opensrv                | 287.78 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 7.02 mins                | 287.78 mins            |
| datafuselabs/databend-perf          | 324.82 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 9.43 mins                | 113.17 mins            |
|                                     |               | pages build and deployment          | 0.56 mins                | 3.33 mins              |
|                                     |               | Reload tpch                         | 8.68 mins                | 43.38 mins             |
|                                     |               | Reload hits                         | 7.05 mins                | 126.95 mins            |
|                                     |               | Reload ontime                       | 7.6 mins                 | 37.98 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 12.92 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 1.93 mins                | 11.57 mins             |
|                                     |               | Release Charts                      | 0.43 mins                | 0.43 mins              |
|                                     |               | pages build and deployment          | 0.92 mins                | 0.92 mins              |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 11.62 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 5.81 mins                | 11.62 mins             |
|                                     |               | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 401.55 mins   |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 13.85 mins               | 401.55 mins            |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 19.72 mins    |                                     |                          |                        |
|                                     |               | publish                             | 2.24 mins                | 4.48 mins              |
|                                     |               | Rust                                | 1.38 mins                | 15.23 mins             |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 2102.02 mins  |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 5.7 mins                 | 461.3 mins             |
|                                     |               | Bindings Python                     | 3.17 mins                | 183.62 mins            |
|                                     |               | CI                                  | 8.51 mins                | 1131.57 mins           |
|                                     |               | PR Assistant                        | 0.37 mins                | 50.4 mins              |
|                                     |               | Publish                             | 8.72 mins                | 87.17 mins             |
|                                     |               | Release                             | 23.5 mins                | 187.97 mins            |
| datafuselabs/askbend                | 84.08 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 8.41 mins                | 84.08 mins             |
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
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime  | Workflow Name                                | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+----------------+----------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins       |                                              |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins       |                                              |                          |                        |
| pingcap/go-themis                  | 0.0 mins       |                                              |                          |                        |
| pingcap/sqllogictest               | 0.0 mins       |                                              |                          |                        |
| pingcap/check                      | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb                       | 5757.37 mins   |                                              |                          |                        |
|                                    |                | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |                | BR & Lightning                               | 4.91 mins                | 3624.5 mins            |
|                                    |                | Dumpling                                     | 10.14 mins               | 1784.97 mins           |
|                                    |                | misc                                         | 2.74 mins                | 347.7 mins             |
|                                    |                | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins       |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins       |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins       |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins       |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins       |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins       |                                              |                          |                        |
| pingcap/tipb                       | 42.18 mins     |                                              |                          |                        |
|                                    |                | Unit Test                                    | 7.03 mins                | 42.18 mins             |
| pingcap/kvproto                    | 654.28 mins    |                                              |                          |                        |
|                                    |                | C++ Test                                     | 4.38 mins                | 218.93 mins            |
|                                    |                | Golang Test                                  | 1.31 mins                | 68.0 mins              |
|                                    |                | Rust Test                                    | 7.06 mins                | 367.35 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins       |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins       |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins       |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins       |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins       |                                              |                          |                        |
| pingcap/docs                       | 4126.38 mins   |                                              |                          |                        |
|                                    |                | Upload media files to Qiniu when they change | 0.99 mins                | 11.93 mins             |
|                                    |                | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |                | Trigger docs site update                     | 0.2 mins                 | 56.47 mins             |
|                                    |                | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Automatic Rebase                             | 0.04 mins                | 60.25 mins             |
|                                    |                | ci                                           | 3.48 mins                | 3177.28 mins           |
|                                    |                | Links                                        | 1.89 mins                | 7.55 mins              |
|                                    |                | bot                                          | 0.72 mins                | 15.93 mins             |
|                                    |                | cron                                         | 1.82 mins                | 21.8 mins              |
|                                    |                | Links (Fail Fast)                            | 0.46 mins                | 412.48 mins            |
|                                    |                | Prevent Deletion                             | 0.39 mins                | 362.68 mins            |
|                                    |                | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 4482.8 mins    |                                              |                          |                        |
|                                    |                | ci                                           | 3.79 mins                | 3642.03 mins           |
|                                    |                | Trigger docs site update                     | 0.19 mins                | 35.07 mins             |
|                                    |                | Flush PDF by Version                         | 0.0 mins                 | 0.0 mins               |
|                                    |                | Flush All PDF                                | 0.25 mins                | 1.48 mins              |
|                                    |                | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |                | Links (Fail Fast)                            | 0.42 mins                | 400.58 mins            |
|                                    |                | Links                                        | 3.17 mins                | 12.7 mins              |
|                                    |                | Upload media files to Qiniu when they change | 0.0 mins                 | 0.0 mins               |
|                                    |                | Prevent Deletion                             | 0.36 mins                | 352.42 mins            |
|                                    |                | Automatic Rebase                             | 0.04 mins                | 38.52 mins             |
| pingcap/tidb-binlog                | 0.0 mins       |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins       |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins       |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins       |                                              |                          |                        |
|                                    |                | ci                                           | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog        | 0.0 mins                 | 0.0 mins               |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins       |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins       |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins       |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins       |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins       |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins       |                                              |                          |                        |
| pingcap/tispark                    | 157.25 mins    |                                              |                          |                        |
|                                    |                | TLS test                                     | 16.47 mins               | 16.47 mins             |
|                                    |                | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |                | Update changelog manually                    | 0.0 mins                 | 0.0 mins               |
|                                    |                | CodeQL                                       | 18.56 mins               | 111.33 mins            |
|                                    |                | Follower Read test                           | 11.77 mins               | 11.77 mins             |
|                                    |                | Close inactive issues                        | 0.25 mins                | 7.23 mins              |
|                                    |                | License checker                              | 1.08 mins                | 1.08 mins              |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | verify                                       | 9.37 mins                | 9.37 mins              |
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
| pingcap/tidb-operator              | 1507.77 mins   |                                              |                          |                        |
|                                    |                | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |                | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |                | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | ci                                           | 21.42 mins               | 1499.48 mins           |
|                                    |                | Close stale issues/prs                       | 0.28 mins                | 8.28 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins       |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins       |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins       |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 1047.43 mins   |                                              |                          |                        |
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
| pingcap/diag                       | 196.05 mins    |                                              |                          |                        |
|                                    |                | reprotest                                    | 11.07 mins               | 132.88 mins            |
|                                    |                | static-tests                                 | 3.72 mins                | 63.17 mins             |
| pingcap/sqlsmith                   | 0.0 mins       |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins       |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins       |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins       |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins       |                                              |                          |                        |
| pingcap/tiflow                     | 249869.12 mins |                                              |                          |                        |
|                                    |                | Auto Assign to Bugs and Questions            | 0.24 mins                | 70.88 mins             |
|                                    |                | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |                | Dataflow Engine Chaos                        | 26.9 mins                | 5649.78 mins           |
|                                    |                | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | DM Binlog 999999                             | 16.51 mins               | 3467.17 mins           |
|                                    |                | DM Chaos                                     | 14.4 mins                | 3023.78 mins           |
|                                    |                | DM Web UI Lint                               | 0.0 mins                 | 0.0 mins               |
|                                    |                | Upstream Database Switch                     | 17.64 mins               | 3704.7 mins            |
|                                    |                | Design Docs Lint                             | 0.36 mins                | 6.78 mins              |
|                                    |                | Upgrade DM via TiUP                          | 200.61 mins              | 42128.07 mins          |
| pingcap/br                         | 0.0 mins       |                                              |                          |                        |
|                                    |                | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |                | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins       |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins       |                                              |                          |                        |
| pingcap/advanced-statefulset       | 950.6 mins     |                                              |                          |                        |
|                                    |                | ci                                           | 19.8 mins                | 950.22 mins            |
|                                    |                | release                                      | 0.38 mins                | 0.38 mins              |
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
