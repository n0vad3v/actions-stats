
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 294.92 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 294.92 mins              | 294.92 mins            |
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
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime | Workflow Name                   | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+---------------+---------------------------------+--------------------------+------------------------+
| webp-sh/webp_server_node            | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_go              | 207.62 mins   |                                 |                          |                        |
|                                     |               | CI check on every PR            | 5.42 mins                | 32.5 mins              |
|                                     |               | CI check on every push          | 2.56 mins                | 10.25 mins             |
|                                     |               | CodeQL                          | 1.95 mins                | 31.2 mins              |
|                                     |               | Integration Tests               | 2.81 mins                | 16.85 mins             |
|                                     |               | Release Binaries                | 2.37 mins                | 4.73 mins              |
|                                     |               | Build and release docker images | 18.68 mins               | 112.08 mins            |
| webp-sh/webp                        | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_python          | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_server_java            | 0.0 mins      |                                 |                          |                        |
|                                     |               | No workflow name(why?)          | 0.0 mins                 | 0.0 mins               |
| webp-sh/gowebp                      | 0.0 mins      |                                 |                          |                        |
| webp-sh/go-avif                     | 0.0 mins      |                                 |                          |                        |
| webp-sh/docs.webp.sh                | 0.0 mins      |                                 |                          |                        |
| webp-sh/libvips                     | 71.55 mins    |                                 |                          |                        |
|                                     |               | Build and release docker images | 71.55 mins               | 71.55 mins             |
| webp-sh/halo-plugin-webp-cloud      | 0.0 mins      |                                 |                          |                        |
|                                     |               | Build Plugin JAR File           | 0.0 mins                 | 0.0 mins               |
| webp-sh/wordpress-plugin-webp-cloud | 0.0 mins      |                                 |                          |                        |
| webp-sh/webp_bench                  | 0.0 mins      |                                 |                          |                        |
| webp-sh/blog-comments               | 0.0 mins      |                                 |                          |                        |
| webp-sh/govips                      | 19.78 mins    |                                 |                          |                        |
|                                     |               | build                           | 6.59 mins                | 19.78 mins             |
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
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 103728.05 mins |                                     |                          |                        |
|                                     |                | Release                             | 96.43 mins               | 4532.38 mins           |
|                                     |                | Cancel PR Workflow                  | 0.07 mins                | 22.23 mins             |
|                                     |                | Production                          | 129.41 mins              | 24328.15 mins          |
|                                     |                | Build Tool                          | 25.53 mins               | 51.07 mins             |
|                                     |                | Crowdin Action                      | 3.27 mins                | 477.08 mins            |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.41 mins                | 629.47 mins            |
|                                     |                | Bindings Python                     | 39.0 mins                | 45908.32 mins          |
|                                     |                | Dev                                 | 21.7 mins                | 25603.15 mins          |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Cloud                               | 30.72 mins               | 1843.35 mins           |
|                                     |                | PR Assistant                        | 0.16 mins                | 332.85 mins            |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 893.18 mins    |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 23.81 mins               | 857.2 mins             |
|                                     |                | commit-message-check                | 2.12 mins                | 19.08 mins             |
|                                     |                | Unit test coverage                  | 4.31 mins                | 12.93 mins             |
|                                     |                | DevSkim                             | 0.79 mins                | 3.97 mins              |
|                                     |                | GPT refine markdown                 | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/issue-welcome.yml | 0.0 mins                 | 0.0 mins               |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/weekly                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Typos Check                         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 384.03 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 12.8 mins                | 384.03 mins            |
| datafuselabs/databend-perf          | 224.52 mins    |                                     |                          |                        |
|                                     |                | Perf                                | 17.23 mins               | 137.87 mins            |
|                                     |                | pages build and deployment          | 0.55 mins                | 2.73 mins              |
|                                     |                | Reload tpch                         | 8.79 mins                | 35.17 mins             |
|                                     |                | Reload hits                         | 6.11 mins                | 30.57 mins             |
|                                     |                | Reload ontime                       | 4.55 mins                | 18.18 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 24.63 mins     |                                     |                          |                        |
|                                     |                | ci                                  | 2.17 mins                | 21.68 mins             |
|                                     |                | Release Charts                      | 0.36 mins                | 1.07 mins              |
|                                     |                | pages build and deployment          | 0.94 mins                | 1.88 mins              |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 11.58 mins     |                                     |                          |                        |
|                                     |                | publish                             | 2.24 mins                | 4.48 mins              |
|                                     |                | Rust                                | 0.89 mins                | 7.1 mins               |
| datafuselabs/opendal-redirect       | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
| datafuselabs/bendsql                | 1196.65 mins   |                                     |                          |                        |
|                                     |                | Bindings Node.js                    | 6.68 mins                | 287.23 mins            |
|                                     |                | Bindings Python                     | 2.72 mins                | 65.25 mins             |
|                                     |                | CI                                  | 11.17 mins               | 636.93 mins            |
|                                     |                | PR Assistant                        | 0.2 mins                 | 8.3 mins               |
|                                     |                | Publish                             | 7.24 mins                | 50.7 mins              |
|                                     |                | Release                             | 29.65 mins               | 148.23 mins            |
| datafuselabs/askbend                | 14.3 mins      |                                     |                          |                        |
|                                     |                | ci                                  | 7.15 mins                | 14.3 mins              |
|                                     |                | release                             | 0.0 mins                 | 0.0 mins               |
| datafuselabs/databend_fiddle        | 0.0 mins       |                                     |                          |                        |
|                                     |                | Pylint                              | 0.0 mins                 | 0.0 mins               |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

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
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+----------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                              |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                              |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                              |                          |                        |
| pingcap/check                      | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb                       | 6112.03 mins  |                                              |                          |                        |
|                                    |               | BR / Compatibility Test                      | 1.66 mins                | 3.32 mins              |
|                                    |               | BR & Lightning                               | 4.23 mins                | 3735.03 mins           |
|                                    |               | Dumpling                                     | 10.58 mins               | 1735.17 mins           |
|                                    |               | Pessimistic Tests                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                         | 2.81 mins                | 622.83 mins            |
|                                    |               | Leaked Secrets Scan                          | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                              |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                              |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                              |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                              |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                              |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tipb                       | 116.88 mins   |                                              |                          |                        |
|                                    |               | Unit Test                                    | 7.31 mins                | 116.88 mins            |
| pingcap/kvproto                    | 453.2 mins    |                                              |                          |                        |
|                                    |               | C++ Test                                     | 4.59 mins                | 146.93 mins            |
|                                    |               | Golang Test                                  | 1.33 mins                | 45.08 mins             |
|                                    |               | Rust Test                                    | 7.68 mins                | 261.18 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                              |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                              |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                              |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                              |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                              |                          |                        |
| pingcap/docs                       | 3422.85 mins  |                                              |                          |                        |
|                                    |               | Upload media files to Qiniu when they change | 0.77 mins                | 1.53 mins              |
|                                    |               | Assign to Project                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 40.9 mins              |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 46.42 mins             |
|                                    |               | ci                                           | 3.47 mins                | 2700.07 mins           |
|                                    |               | Links                                        | 2.08 mins                | 8.33 mins              |
|                                    |               | bot                                          | 0.7 mins                 | 14.65 mins             |
|                                    |               | cron                                         | 1.36 mins                | 20.47 mins             |
|                                    |               | Links (Fail Fast)                            | 0.41 mins                | 315.48 mins            |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 275.0 mins             |
|                                    |               | Pull Request Labeler                         | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 3760.92 mins  |                                              |                          |                        |
|                                    |               | ci                                           | 4.3 mins                 | 3123.57 mins           |
|                                    |               | Trigger docs site update                     | 0.18 mins                | 39.9 mins              |
|                                    |               | Flush PDF by Version                         | 0.23 mins                | 0.93 mins              |
|                                    |               | Flush All PDF                                | 0.28 mins                | 1.4 mins               |
|                                    |               | external-link-check                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links (Fail Fast)                            | 0.39 mins                | 286.18 mins            |
|                                    |               | Links                                        | 1.72 mins                | 6.88 mins              |
|                                    |               | Upload media files to Qiniu when they change | 0.43 mins                | 1.72 mins              |
|                                    |               | Prevent Deletion                             | 0.35 mins                | 256.67 mins            |
|                                    |               | Automatic Rebase                             | 0.04 mins                | 43.67 mins             |
| pingcap/tidb-binlog                | 0.0 mins      |                                              |                          |                        |
| pingcap/sqlgram                    | 0.0 mins      |                                              |                          |                        |
| pingcap/mydumper                   | 0.0 mins      |                                              |                          |                        |
| pingcap/blog                       | 0.0 mins      |                                              |                          |                        |
|                                    |               | ci                                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Links                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-ansible               | 0.0 mins      |                                              |                          |                        |
| pingcap/rust-protobuf              | 0.0 mins      |                                              |                          |                        |
| pingcap/grpc-rust                  | 0.0 mins      |                                              |                          |                        |
| pingcap/mybatis-3                  | 0.0 mins      |                                              |                          |                        |
| pingcap/blog-cn                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | Repsitory dispatch workflow from blog-cn     | 0.0 mins                 | 0.0 mins               |
| pingcap/tikv-client-lib-java       | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark                    | 453.52 mins   |                                              |                          |                        |
|                                    |               | TLS test                                     | 10.91 mins               | 87.27 mins             |
|                                    |               | alter-primary-key-false-test                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Update changelog manually                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                       | 13.9 mins                | 166.85 mins            |
|                                    |               | Follower Read test                           | 9.09 mins                | 72.68 mins             |
|                                    |               | Close inactive issues                        | 0.25 mins                | 7.42 mins              |
|                                    |               | License checker                              | 1.06 mins                | 13.73 mins             |
|                                    |               | .github/workflows/license-checker-config.yml | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                       | 8.12 mins                | 105.57 mins            |
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
|                                    |               | Go                                           | 0.0 mins                 | 0.0 mins               |
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
|                                    |               | testbuild                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                      | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-operator              | 7693.25 mins  |                                              |                          |                        |
|                                    |               | No workflow name(why?)                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                     | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 47.4 mins                | 3934.03 mins           |
|                                    |               | ci                                           | 21.2 mins                | 3752.13 mins           |
|                                    |               | Close stale issues/prs                       | 0.24 mins                | 7.08 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                              |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                              |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-engine-ext            | 913.47 mins   |                                              |                          |                        |
|                                    |               | Pull Request CI                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | License checker                              | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-academy-labs          | 0.0 mins      |                                              |                          |                        |
| pingcap/parser                     | 0.0 mins      |                                              |                          |                        |
| pingcap/benchmarksql               | 0.0 mins      |                                              |                          |                        |
| pingcap/gofail                     | 0.0 mins      |                                              |                          |                        |
| pingcap/work-reporter              | 0.0 mins      |                                              |                          |                        |
| pingcap/dm                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | Test binlog 999999                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | chaos                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Build & Lint                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upgrade via TiUP                             | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream database switch                     | 0.0 mins                 | 0.0 mins               |
| pingcap/talent-plan                | 0.0 mins      |                                              |                          |                        |
| pingcap/log                        | 0.0 mins      |                                              |                          |                        |
|                                    |               | Audit License                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Unit Test                                    | 0.0 mins                 | 0.0 mins               |
| pingcap/tiflash                    | 0.0 mins      |                                              |                          |                        |
|                                    |               | .github/workflows/assign_project.yml         | 0.0 mins                 | 0.0 mins               |
| pingcap/poco                       | 0.0 mins      |                                              |                          |                        |
| pingcap/capnproto                  | 0.0 mins      |                                              |                          |                        |
| pingcap/boost-extra                | 0.0 mins      |                                              |                          |                        |
| pingcap/kdt                        | 0.0 mins      |                                              |                          |                        |
| pingcap/failpoint                  | 0.0 mins      |                                              |                          |                        |
|                                    |               | Build & Test                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-datanucleus-adapter   | 0.0 mins      |                                              |                          |                        |
| pingcap/homebrew-brew              | 0.0 mins      |                                              |                          |                        |
| pingcap/tidb-cloud-backup          | 0.0 mins      |                                              |                          |                        |
| pingcap/tidiff                     | 0.0 mins      |                                              |                          |                        |
| pingcap/fn                         | 0.0 mins      |                                              |                          |                        |
| pingcap/diag                       | 137.2 mins    |                                              |                          |                        |
|                                    |               | reprotest                                    | 10.41 mins               | 83.3 mins              |
|                                    |               | static-tests                                 | 3.85 mins                | 53.9 mins              |
| pingcap/sqlsmith                   | 0.0 mins      |                                              |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                              |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                              |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                              |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                              |                          |                        |
| pingcap/tiflow                     | 66184.4 mins  |                                              |                          |                        |
|                                    |               | Auto Assign to Bugs and Questions            | 0.23 mins                | 105.63 mins            |
|                                    |               | Check & Build                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                        | 21.56 mins               | 4528.53 mins           |
|                                    |               | Dataflow Engine Image                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow engine unit test                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Binlog 999999                             | 15.71 mins               | 3299.57 mins           |
|                                    |               | DM Chaos                                     | 13.88 mins               | 2915.03 mins           |
|                                    |               | DM Web UI Lint                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | Upstream Database Switch                     | 17.39 mins               | 3652.05 mins           |
|                                    |               | Design Docs Lint                             | 0.35 mins                | 19.4 mins              |
|                                    |               | Upgrade DM via TiUP                          | 200.62 mins              | 42129.98 mins          |
| pingcap/br                         | 0.0 mins      |                                              |                          |                        |
|                                    |               | build                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | compatibility-test                           | 0.0 mins                 | 0.0 mins               |
| pingcap/go-randgen                 | 0.0 mins      |                                              |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                              |                          |                        |
| pingcap/advanced-statefulset       | 542.7 mins    |                                              |                          |                        |
|                                    |               | ci                                           | 18.09 mins               | 542.7 mins             |
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
    
Error: {'message': 'Server Error'}
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
