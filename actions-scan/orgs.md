
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
| webp-sh/webp_server_go              | 429.85 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 4.62 mins                | 78.6 mins              |
|                                     |               | CI check on every push          | 1.81 mins                | 16.32 mins             |
|                                     |               | CodeQL                          | 1.57 mins                | 48.75 mins             |
|                                     |               | Integration Tests               | 2.77 mins                | 47.1 mins              |
|                                     |               | Release Binaries                | 7.1 mins                 | 7.1 mins               |
|                                     |               | Build and release docker images | 23.2 mins                | 231.98 mins            |
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
| datafuselabs/databend               | 74969.2 mins  |                                     |                          |                        |
|                                     |               | Release                             | 87.18 mins               | 4097.25 mins           |
|                                     |               | Cancel PR Workflow                  | 0.04 mins                | 11.8 mins              |
|                                     |               | Production                          | 108.12 mins              | 24435.62 mins          |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.35 mins                | 578.13 mins            |
|                                     |               | Dev                                 | 19.84 mins               | 29895.82 mins          |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 30.94 mins               | 1609.02 mins           |
|                                     |               | PR Assistant                        | 0.26 mins                | 596.98 mins            |
|                                     |               | Push on main                        | 2.69 mins                | 803.8 mins             |
|                                     |               | Bindings Python                     | 10.87 mins               | 12892.52 mins          |
|                                     |               | Build Tool                          | 24.13 mins               | 48.27 mins             |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 1573.62 mins  |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 15.87 mins               | 1412.62 mins           |
|                                     |               | commit-message-check                | 0.94 mins                | 77.62 mins             |
|                                     |               | Unit test coverage                  | 3.63 mins                | 61.67 mins             |
|                                     |               | DevSkim                             | 0.83 mins                | 3.33 mins              |
|                                     |               | GPT refine markdown                 | 0.28 mins                | 12.62 mins             |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.04 mins                | 1.93 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.35 mins                | 3.83 mins              |
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
| datafuselabs/opensrv                | 491.38 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 12.93 mins               | 491.38 mins            |
| datafuselabs/databend-perf          | 121.93 mins   |                                     |                          |                        |
|                                     |               | Perf                                | 7.03 mins                | 77.3 mins              |
|                                     |               | pages build and deployment          | 0.56 mins                | 1.68 mins              |
|                                     |               | Reload hits                         | 8.59 mins                | 42.95 mins             |
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
| datafuselabs/databend-py            | 3.28 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.58 mins                | 2.92 mins              |
|                                     |               | Release on Version Change           | 0.37 mins                | 0.37 mins              |
| datafuselabs/databend-sqlalchemy    | 12.17 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 0.62 mins                | 4.95 mins              |
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
| datafuselabs/bendsql                | 2667.13 mins  |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 11.57 mins               | 937.57 mins            |
|                                     |               | Bindings Python                     | 7.44 mins                | 557.7 mins             |
|                                     |               | CI                                  | 8.01 mins                | 960.85 mins            |
|                                     |               | PR Assistant                        | 0.23 mins                | 21.42 mins             |
|                                     |               | Publish                             | 7.0 mins                 | 63.02 mins             |
|                                     |               | Release                             | 14.06 mins               | 126.58 mins            |
| datafuselabs/askbend                | 0.0 mins      |                                     |                          |                        |
|                                     |               | ci                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins      |                                     |                          |                        |
|                                     |               | Pylint                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-docs          | 112.73 mins   |                                     |                          |                        |
|                                     |               | build                               | 3.89 mins                | 112.73 mins            |
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
| pingcap/tidb                       | 6769.93 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR & Lightning                               | 4.13 mins                | 4756.48 mins           |
|                                    |               | Dumpling                                     | 9.55 mins                | 1699.7 mins            |
|                                    |               | misc                                         | 2.37 mins                | 313.33 mins            |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/kvproto                    | 315.33 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 12.28 mins               | 196.47 mins            |
|                                    |               | Golang Test                                  | 1.26 mins                | 20.17 mins             |
|                                    |               | Rust Test                                    | 6.17 mins                | 98.7 mins              |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3489.8 mins   |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 0.52 mins                | 4.68 mins              |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.25 mins                | 58.25 mins             |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 49.67 mins             |
|                                    |               | ci                                           | 3.29 mins                | 2604.0 mins            |
|                                    |               | Links                                        | 1.87 mins                | 7.47 mins              |
|                                    |               | bot                                          | 0.71 mins                | 15.67 mins             |
|                                    |               | cron                                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.5 mins                 | 387.15 mins            |
|                                    |               | Prevent Deletion                             | 0.42 mins                | 341.25 mins            |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
|                                    |               | translation                                  | 2.71 mins                | 21.67 mins             |
| pingcap/docs-cn                    | 3157.82 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 3.89 mins                | 2562.8 mins            |
|                                    |               | Trigger docs site update                     | 0.2 mins                 | 36.4 mins              |
|                                    |               | Flush PDF by Version                         | 0.28 mins                | 1.13 mins              |
|                                    |               | Flush All PDF                                | 0.28 mins                | 1.4 mins               |
|                                    |               | Links (Fail Fast)                            | 0.44 mins                | 283.52 mins            |
|                                    |               | Links                                        | 1.89 mins                | 7.55 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.53 mins                | 3.17 mins              |
|                                    |               | Prevent Deletion                             | 0.34 mins                | 227.05 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 34.8 mins              |
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
| pingcap/tispark                    | 70.4 mins     |                                              |                          |                        |
|                                    |               | TLS test                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 15.88 mins               | 63.52 mins             |
|                                    |               | Follower Read test                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | Close inactive issues                        | 0.23 mins                | 6.88 mins              |
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
| pingcap/tidb-operator              | 2172.78 mins  |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                           | 15.03 mins               | 2164.78 mins           |
|                                    |               | Close stale issues/prs                       | 0.27 mins                | 8.0 mins               |
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
| pingcap/tiflow                     | 62238.8 mins  |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.26 mins                | 76.53 mins             |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 20.54 mins               | 4313.15 mins           |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 13.35 mins               | 2803.65 mins           |
|                                    |               | DM Chaos                                     | 13.66 mins               | 2869.43 mins           |
|                                    |               | DM Web UI Lint                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream Database Switch                     | 15.98 mins               | 3355.02 mins           |
|                                    |               | Design Docs Lint                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                          | 200.61 mins              | 42128.83 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 416.82 mins   |                                              |                          |                        |
|                                    |               | ci                                           | 13.89 mins               | 416.82 mins            |
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
