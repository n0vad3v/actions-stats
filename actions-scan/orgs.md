
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
| webp-sh/webp_server_go              | 333.45 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 3.15 mins                | 34.65 mins             |
|                                     |               | CI check on every push          | 1.7 mins                 | 13.6 mins              |
|                                     |               | CodeQL                          | 1.55 mins                | 37.18 mins             |
|                                     |               | Integration Tests               | 2.38 mins                | 26.2 mins              |
|                                     |               | Release Binaries                | 4.97 mins                | 9.93 mins              |
|                                     |               | Build and release docker images | 21.19 mins               | 211.88 mins            |
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
| datafuselabs/databend               | 60503.57 mins |                                     |                          |                        |
|                                     |               | Release                             | 82.94 mins               | 3732.25 mins           |
|                                     |               | Cancel PR Workflow                  | 0.04 mins                | 9.32 mins              |
|                                     |               | Production                          | 75.74 mins               | 14541.75 mins          |
|                                     |               | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |               | Typos Check                         | 0.31 mins                | 454.95 mins            |
|                                     |               | Dev                                 | 19.34 mins               | 26568.1 mins           |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | Cloud                               | 31.73 mins               | 1872.2 mins            |
|                                     |               | PR Assistant                        | 0.24 mins                | 511.43 mins            |
|                                     |               | Push on main                        | 2.13 mins                | 442.28 mins            |
|                                     |               | Bindings Python                     | 10.03 mins               | 12238.13 mins          |
|                                     |               | Build Tool                          | 16.64 mins               | 133.15 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins      |                                     |                          |                        |
| datafuselabs/openraft               | 2122.0 mins   |                                     |                          |                        |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |               | ci                                  | 12.26 mins               | 1826.63 mins           |
|                                     |               | commit-message-check                | 0.89 mins                | 139.0 mins             |
|                                     |               | Unit test coverage                  | 3.19 mins                | 136.97 mins            |
|                                     |               | DevSkim                             | 0.61 mins                | 2.43 mins              |
|                                     |               | GPT refine markdown                 | 0.23 mins                | 10.02 mins             |
|                                     |               | .github/workflows/issue-cmds.yml    | 0.04 mins                | 1.85 mins              |
|                                     |               | .github/workflows/issue-welcome.yml | 0.19 mins                | 1.73 mins              |
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
| datafuselabs/opensrv                | 189.13 mins   |                                     |                          |                        |
|                                     |               | CI                                  | 4.5 mins                 | 189.13 mins            |
| datafuselabs/databend-perf          | 130.2 mins    |                                     |                          |                        |
|                                     |               | Perf                                | 9.49 mins                | 85.4 mins              |
|                                     |               | pages build and deployment          | 0.58 mins                | 3.47 mins              |
|                                     |               | Reload hits                         | 10.33 mins               | 41.33 mins             |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 4.03 mins     |                                     |                          |                        |
|                                     |               | ci                                  | 1.9 mins                 | 3.8 mins               |
|                                     |               | Release Charts                      | 0.23 mins                | 0.23 mins              |
|                                     |               | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/link                   | 0.0 mins      |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |               | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-go            | 5.15 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.86 mins                | 5.15 mins              |
| datafuselabs/jepsen.meta            | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-py            | 6.85 mins     |                                     |                          |                        |
|                                     |               | CI                                  | 0.6 mins                 | 6.02 mins              |
|                                     |               | Release on Version Change           | 0.42 mins                | 0.83 mins              |
| datafuselabs/databend-sqlalchemy    | 43.75 mins    |                                     |                          |                        |
|                                     |               | CI                                  | 0.61 mins                | 19.65 mins             |
| datafuselabs/hackathon2022          | 0.0 mins      |                                     |                          |                        |
| datafuselabs/databend-jdbc          | 26.35 mins    |                                     |                          |                        |
|                                     |               | Release Workflow                    | 0.0 mins                 | 0.0 mins               |
|                                     |               | Tests                               | 1.32 mins                | 26.35 mins             |
| datafuselabs/summer-of-code         | 0.0 mins      |                                     |                          |                        |
| datafuselabs/jsonb                  | 4.02 mins     |                                     |                          |                        |
|                                     |               | publish                             | 0.0 mins                 | 0.0 mins               |
|                                     |               | Rust                                | 0.8 mins                 | 4.02 mins              |
| datafuselabs/opendal-redirect       | 0.0 mins      |                                     |                          |                        |
|                                     |               | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1429.1 mins   |                                     |                          |                        |
|                                     |               | Bindings Node.js                    | 11.59 mins               | 568.02 mins            |
|                                     |               | Bindings Python                     | 7.41 mins                | 259.48 mins            |
|                                     |               | CI                                  | 8.01 mins                | 488.38 mins            |
|                                     |               | PR Assistant                        | 0.2 mins                 | 8.93 mins              |
|                                     |               | Publish                             | 4.61 mins                | 27.68 mins             |
|                                     |               | Release                             | 12.77 mins               | 76.6 mins              |
| datafuselabs/askbend                | 13.68 mins    |                                     |                          |                        |
|                                     |               | ci                                  | 6.84 mins                | 13.68 mins             |
|                                     |               | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins      |                                     |                          |                        |
|                                     |               | Pylint                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend-docs          | 604.57 mins   |                                     |                          |                        |
|                                     |               | build                               | 4.92 mins                | 604.57 mins            |
| datafuselabs/databend-udf           | 0.0 mins      |                                     |                          |                        |
|                                     |               | Python                              | 0.0 mins                 | 0.0 mins               |
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
| pingcap/tidb                       | 4924.83 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR & Lightning                               | 3.1 mins                 | 2922.35 mins           |
|                                    |               | Dumpling                                     | 7.68 mins                | 1574.2 mins            |
|                                    |               | misc                                         | 2.14 mins                | 396.3 mins             |
|                                    |               | MySQL Tests                                  | 1.22 mins                | 1.22 mins              |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/kvproto                    | 133.07 mins   |                                              |                          |                        |
|                                    |               | C++ Test                                     | 3.51 mins                | 49.2 mins              |
|                                    |               | Golang Test                                  | 1.0 mins                 | 13.95 mins             |
|                                    |               | Rust Test                                    | 4.99 mins                | 69.92 mins             |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3483.63 mins  |                                              |                          |                        |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | bot                                          | 0.67 mins                | 14.67 mins             |
|                                    |               | ci                                           | 2.53 mins                | 2459.33 mins           |
|                                    |               | cron                                         | 0.35 mins                | 7.78 mins              |
|                                    |               | Trigger docs site update                     | 0.21 mins                | 70.83 mins             |
|                                    |               | JA Full Translation (Google version)         | 6.48 mins                | 19.45 mins             |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.45 mins                | 406.78 mins            |
|                                    |               | Links                                        | 1.54 mins                | 6.17 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.6 mins                 | 8.4 mins               |
|                                    |               | Prevent Deletion                             | 0.4 mins                 | 402.0 mins             |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 66.55 mins             |
|                                    |               | translation                                  | 2.71 mins                | 21.67 mins             |
| pingcap/docs-cn                    | 2741.5 mins   |                                              |                          |                        |
|                                    |               | ci                                           | 2.97 mins                | 2054.28 mins           |
|                                    |               | Trigger docs site update                     | 0.19 mins                | 46.58 mins             |
|                                    |               | Flush PDF by Version                         | 0.2 mins                 | 0.2 mins               |
|                                    |               | Flush All PDF                                | 0.25 mins                | 0.98 mins              |
|                                    |               | Links (Fail Fast)                            | 0.48 mins                | 310.53 mins            |
|                                    |               | Links                                        | 1.62 mins                | 6.5 mins               |
|                                    |               | Upload media files to Qiniu when they change | 0.42 mins                | 0.42 mins              |
|                                    |               | Prevent Deletion                             | 0.39 mins                | 275.88 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 46.12 mins             |
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
| pingcap/tispark                    | 52.93 mins    |                                              |                          |                        |
|                                    |               | TLS test                                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 11.66 mins               | 46.63 mins             |
|                                    |               | Follower Read test                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | Close inactive issues                        | 0.21 mins                | 6.3 mins               |
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
| pingcap/go-ycsb                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | Docker Image CI                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | Publish artifacts to github release          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                           | 0.0 mins                 | 0.0 mins               |
| pingcap/tispark-test-data          | 0.0 mins      |                                              |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                              |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-operator              | 4334.17 mins  |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | ci                                           | 19.32 mins               | 4326.8 mins            |
|                                    |               | Close stale issues/prs                       | 0.25 mins                | 7.37 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 4.92 mins     |                                              |                          |                        |
|                                    |               | Pull Request CI                              | 4.92 mins                | 4.92 mins              |
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
| pingcap/tiflow                     | 59098.75 mins |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.22 mins                | 89.05 mins             |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 16.93 mins               | 3554.57 mins           |
|                                    |               | DM Binlog 999999                             | 10.05 mins               | 2110.93 mins           |
|                                    |               | DM Chaos                                     | 10.89 mins               | 2286.8 mins            |
|                                    |               | DM Web UI Lint                               | 1.23 mins                | 2.47 mins              |
|                                    |               | Upstream Database Switch                     | 11.61 mins               | 2438.68 mins           |
|                                    |               | Design Docs Lint                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade DM via TiUP                          | 200.61 mins              | 42129.08 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 651.85 mins   |                                              |                          |                        |
|                                    |               | ci                                           | 15.14 mins               | 650.95 mins            |
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
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
