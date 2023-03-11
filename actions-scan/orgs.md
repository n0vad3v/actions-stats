
<details><summary><b>knatnetwork</b> <i>[click to show]</i></summary>
<div>

```
    
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| Repo                           | Total Runtime | Workflow Name      | Workflow Average Runtime | Workflow Total Runtime |
+--------------------------------+---------------+--------------------+--------------------------+------------------------+
| knatnetwork/g2ww-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/g2fs-serverless    | 0.0 mins      |                    |                          |                        |
| knatnetwork/github-runner      | 351.18 mins   |                    |                          |                        |
|                                |               | Build Runner Image | 117.06 mins              | 351.18 mins            |
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
| webp-sh/webp_server_go     | 182.47 mins   |                                 |                          |                        |
|                            |               | CI check on every PR            | 3.61 mins                | 32.5 mins              |
|                            |               | Release Binaries                | 2.68 mins                | 2.68 mins              |
|                            |               | Build and release docker images | 15.78 mins               | 110.45 mins            |
|                            |               | CodeQL                          | 1.94 mins                | 36.83 mins             |
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
Error: {'total_count': 200, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| Repo                                | Total Runtime  | Workflow Name                       | Workflow Average Runtime | Workflow Total Runtime |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+
| datafuselabs/databend               | 146594.55 mins |                                     |                          |                        |
|                                     |                | Unit Tests                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 109.48 mins              | 4817.0 mins            |
|                                     |                | License checker                     | 0.0 mins                 | 0.0 mins               |
|                                     |                | Audit Security                      | 0.0 mins                 | 0.0 mins               |
|                                     |                | Databend Base                       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Production                          | 84.99 mins               | 24733.37 mins          |
|                                     |                | Build Tool                          | 34.49 mins               | 172.45 mins            |
|                                     |                | Dev Linux                           | 20.94 mins               | 28536.42 mins          |
|                                     |                | Dev MacOS                           | 61.06 mins               | 83218.08 mins          |
|                                     |                | Backport                            | 0.0 mins                 | 0.0 mins               |
|                                     |                | Debug                               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Benchmark                           | 2.73 mins                | 4097.4 mins            |
|                                     |                | Benchmark Commentator (trusted)     | 0.09 mins                | 136.37 mins            |
|                                     |                | Release Repository                  | 1.43 mins                | 4.28 mins              |
|                                     |                | Typos Check                         | 1.49 mins                | 879.18 mins            |
|                                     |                | Stateless(Cluster)                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateless(Standalone)               | 0.0 mins                 | 0.0 mins               |
|                                     |                | Stateful(Standalone)                | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-operator      | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openraft               | 10343.3 mins   |                                     |                          |                        |
|                                     |                | chaos-test                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | ci                                  | 52.36 mins               | 8377.85 mins           |
|                                     |                | commit-message-check                | 6.98 mins                | 1304.45 mins           |
|                                     |                | Unit test coverage                  | 8.68 mins                | 416.65 mins            |
|                                     |                | DevSkim                             | 0.91 mins                | 4.53 mins              |
|                                     |                | .github/workflows/issue-cmds.yml    | 0.06 mins                | 2.05 mins              |
|                                     |                | .github/workflows/issue-welcome.yml | 4.27 mins                | 55.45 mins             |
|                                     |                | .github/workflows/pages.yaml        | 3.77 mins                | 26.42 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Release                             | 10.23 mins               | 51.17 mins             |
|                                     |                | pages build and deployment          | 14.96 mins               | 104.73 mins            |
| datafuselabs/fusebots               | 0.0 mins       |                                     |                          |                        |
|                                     |                | docker                              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/test-infra             | 0.0 mins       |                                     |                          |                        |
| datafuselabs/datafuse-presentations | 0.0 mins       |                                     |                          |                        |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/datafuse-shop          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/weekly                 | 15.77 mins     |                                     |                          |                        |
|                                     |                | Build and deploy on push            | 0.82 mins                | 3.28 mins              |
|                                     |                | Typos Check                         | 3.54 mins                | 7.08 mins              |
|                                     |                | pages build and deployment          | 1.35 mins                | 5.4 mins               |
| datafuselabs/.github                | 0.0 mins       |                                     |                          |                        |
| datafuselabs/openkv                 | 0.0 mins       |                                     |                          |                        |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opendal                | 102436.43 mins |                                     |                          |                        |
|                                     |                | CI                                  | 19.27 mins               | 10366.35 mins          |
|                                     |                | Service Test S3                     | 11.82 mins               | 3828.37 mins           |
|                                     |                | Service Test Fs                     | 10.85 mins               | 3481.88 mins           |
|                                     |                | Service Test Memory                 | 8.45 mins                | 2712.87 mins           |
|                                     |                | Service Test Azblob                 | 8.66 mins                | 2850.65 mins           |
|                                     |                | Service Test HDFS                   | 11.04 mins               | 3545.03 mins           |
|                                     |                | Service Test HTTP                   | 11.12 mins               | 3569.65 mins           |
|                                     |                | Service Test Gcs                    | 9.93 mins                | 3198.7 mins            |
|                                     |                | Test Vault                          | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Obs                    | 11.56 mins               | 3721.25 mins           |
|                                     |                | Service Test IPMFS                  | 9.54 mins                | 3070.68 mins           |
|                                     |                | Service Test Ftp                    | 14.01 mins               | 4540.03 mins           |
|                                     |                | Service Test Redis                  | 9.28 mins                | 2979.62 mins           |
|                                     |                | Service Test Oss                    | 10.89 mins               | 3517.37 mins           |
|                                     |                | Service Test Moka                   | 9.33 mins                | 2993.45 mins           |
|                                     |                | Service Test RocksDB                | 15.48 mins               | 5061.75 mins           |
|                                     |                | Service Test Azdfs                  | 9.93 mins                | 3266.45 mins           |
|                                     |                | Service Test Ghac                   | 9.97 mins                | 3210.58 mins           |
|                                     |                | A Test                              | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Memcached              | 8.79 mins                | 2857.75 mins           |
|                                     |                | pages build and deployment          | 3.61 mins                | 495.18 mins            |
|                                     |                | Bindings Python CI                  | 28.13 mins               | 12938.22 mins          |
|                                     |                | Service Test WebDAV                 | 16.75 mins               | 5644.93 mins           |
|                                     |                | Service Test WebHDFS                | 10.52 mins               | 3387.05 mins           |
|                                     |                | Service Test HDFS and WebHDFS       | 0.0 mins                 | 0.0 mins               |
|                                     |                | Service Test Sled                   | 8.74 mins                | 2804.77 mins           |
|                                     |                | Service Test Dashmap                | 7.62 mins                | 1340.55 mins           |
|                                     |                | Benchmark                           | 22.84 mins               | 1826.83 mins           |
|                                     |                | Docs                                | 13.66 mins               | 2622.07 mins           |
|                                     |                | Typos Check                         | 3.5 mins                 | 1192.92 mins           |
|                                     |                | Binding NodeJS CI                   | 7.57 mins                | 1340.3 mins            |
|                                     |                | Publish                             | 23.73 mins               | 71.18 mins             |
|                                     |                | Service Test IPFS                   | 0.0 mins                 | 0.0 mins               |
| datafuselabs/opensrv                | 748.33 mins    |                                     |                          |                        |
|                                     |                | CI                                  | 17.82 mins               | 748.33 mins            |
| datafuselabs/databend-perf          | 2025.58 mins   |                                     |                          |                        |
|                                     |                | Perf                                | 120.27 mins              | 1804.08 mins           |
|                                     |                | pages build and deployment          | 1.18 mins                | 5.92 mins              |
|                                     |                | Reload tpch                         | 12.95 mins               | 77.72 mins             |
|                                     |                | Reload hits                         | 26.56 mins               | 106.25 mins            |
|                                     |                | Reload ontime                       | 7.9 mins                 | 31.62 mins             |
|                                     |                | No workflow name(why?)              | 0.0 mins                 | 0.0 mins               |
| datafuselabs/helm-charts            | 19.38 mins     |                                     |                          |                        |
|                                     |                | Release Charts                      | 0.74 mins                | 8.17 mins              |
|                                     |                | pages build and deployment          | 1.02 mins                | 11.22 mins             |
| datafuselabs/sqlparser-rs           | 0.0 mins       |                                     |                          |                        |
| datafuselabs/link                   | 0.0 mins       |                                     |                          |                        |
| datafuselabs/opencache              | 0.0 mins       |                                     |                          |                        |
|                                     |                | CI                                  | 0.0 mins                 | 0.0 mins               |
|                                     |                | .github/workflows/pages.yml         | 0.0 mins                 | 0.0 mins               |
|                                     |                | pages build and deployment          | 0.0 mins                 | 0.0 mins               |
| datafuselabs/jepsen.meta            | 0.0 mins       |                                     |                          |                        |
| datafuselabs/hackathon2022          | 0.0 mins       |                                     |                          |                        |
| datafuselabs/summer-of-code         | 0.0 mins       |                                     |                          |                        |
| datafuselabs/jsonb                  | 18.62 mins     |                                     |                          |                        |
|                                     |                | Rust                                | 2.07 mins                | 18.62 mins             |
+-------------------------------------+----------------+-------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>pingcap</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'message': 'Server Error'}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| Repo                               | Total Runtime | Workflow Name                                        | Workflow Average Runtime | Workflow Total Runtime |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+
| pingcap/mp                         | 0.0 mins      |                                                      |                          |                        |
| pingcap/tpcc-mysql                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-themis                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/sqllogictest               | 0.0 mins      |                                                      |                          |                        |
| pingcap/check                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-lmdb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb                       | 3784.07 mins  |                                                      |                          |                        |
|                                    |               | BR & Lightning build                                 | 0.0 mins                 | 0.0 mins               |
|                                    |               | BR / Compatibility Test                              | 12.57 mins               | 12.57 mins             |
|                                    |               | BR & Lightning                                       | 1.31 mins                | 820.65 mins            |
|                                    |               | Dumpling                                             | 9.4 mins                 | 2406.72 mins           |
|                                    |               | Pessimistic Tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | misc                                                 | 2.89 mins                | 528.07 mins            |
|                                    |               | Leaked Secrets Scan                                  | 0.0 mins                 | 0.0 mins               |
| pingcap/tidb-bench                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-hbase                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/tso                        | 0.0 mins      |                                                      |                          |                        |
| pingcap/themis                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/mysqlrelay                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/weekly                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tipb                       | 183.25 mins   |                                                      |                          |                        |
|                                    |               | Unit Test                                            | 5.55 mins                | 183.25 mins            |
| pingcap/kvproto                    | 1232.13 mins  |                                                      |                          |                        |
|                                    |               | C++ Test                                             | 6.47 mins                | 523.92 mins            |
|                                    |               | Golang Test                                          | 1.8 mins                 | 145.85 mins            |
|                                    |               | Rust Test                                            | 6.94 mins                | 562.37 mins            |
| pingcap/etcdv3-gateway             | 0.0 mins      |                                                      |                          |                        |
| pingcap/mpdriver                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/logo                       | 0.0 mins      |                                                      |                          |                        |
| pingcap/goyacc                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/goleveldb                  | 0.0 mins      |                                                      |                          |                        |
| pingcap/docs                       | 5858.95 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.5 mins                 | 6.03 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 86.92 mins             |
|                                    |               | external-link-check                                  | 2.93 mins                | 17.58 mins             |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 90.47 mins             |
|                                    |               | ci                                                   | 3.61 mins                | 4627.73 mins           |
|                                    |               | Links                                                | 2.48 mins                | 9.9 mins               |
|                                    |               | bot                                                  | 0.81 mins                | 16.93 mins             |
|                                    |               | cron                                                 | 1.3 mins                 | 38.88 mins             |
|                                    |               | Links (Fail Fast)                                    | 0.43 mins                | 502.27 mins            |
|                                    |               | Prevent Deletion                                     | 0.36 mins                | 462.23 mins            |
|                                    |               | Pull Request Labeler                                 | 0.0 mins                 | 0.0 mins               |
| pingcap/docs-cn                    | 5747.47 mins  |                                                      |                          |                        |
|                                    |               | Upload media files to Qiniu when they change         | 0.43 mins                | 8.15 mins              |
|                                    |               | Assign to Project                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Trigger docs site update                             | 0.19 mins                | 78.72 mins             |
|                                    |               | external-link-check                                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Automatic Rebase                                     | 0.04 mins                | 17.82 mins             |
|                                    |               | ci                                                   | 4.11 mins                | 4788.97 mins           |
|                                    |               | Links                                                | 1.72 mins                | 6.88 mins              |
|                                    |               | Flush All PDF                                        | 0.26 mins                | 9.45 mins              |
|                                    |               | Links (Fail Fast)                                    | 0.4 mins                 | 432.07 mins            |
|                                    |               | Prevent Deletion                                     | 0.34 mins                | 404.87 mins            |
|                                    |               | Flush PDF by Version                                 | 0.28 mins                | 0.55 mins              |
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
| pingcap/tispark                    | 3100.42 mins  |                                                      |                          |                        |
|                                    |               | TLS test                                             | 13.28 mins               | 703.98 mins            |
|                                    |               | alter-primary-key-false-test                         | 9.16 mins                | 485.3 mins             |
|                                    |               | Update changelog manually                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | CodeQL                                               | 17.85 mins               | 1035.3 mins            |
|                                    |               | Follower Read test                                   | 9.31 mins                | 493.52 mins            |
|                                    |               | Close inactive issues                                | 0.23 mins                | 6.87 mins              |
|                                    |               | License checker                                      | 1.13 mins                | 59.68 mins             |
|                                    |               | .github/workflows/license-checker-config.yml         | 0.0 mins                 | 0.0 mins               |
|                                    |               | verify                                               | 5.96 mins                | 315.77 mins            |
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
| pingcap/go-ycsb                    | 43.42 mins    |                                                      |                          |                        |
|                                    |               | Docker Image CI                                      | 2.67 mins                | 24.0 mins              |
|                                    |               | Publish artifacts to github release                  | 0.0 mins                 | 0.0 mins               |
|                                    |               | Go                                                   | 2.16 mins                | 19.42 mins             |
| pingcap/tispark-test-data          | 0.0 mins      |                                                      |                          |                        |
| pingcap/murmur3                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/oasis                      | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-insight               | 0.0 mins      |                                                      |                          |                        |
|                                    |               | testbuild                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | reprotest                                            | 0.0 mins                 | 0.0 mins               |
| pingcap/badger                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-operator              | 11508.93 mins |                                                      |                          |                        |
|                                    |               | No workflow name(why?)                               | 0.0 mins                 | 0.0 mins               |
|                                    |               | .github/workflows/cd.yml                             | 1066.49 mins             | 2132.98 mins           |
|                                    |               | chaos                                                | 21.56 mins               | 4700.03 mins           |
|                                    |               | ci                                                   | 18.67 mins               | 4668.57 mins           |
|                                    |               | Close stale issues/prs                               | 0.24 mins                | 7.35 mins              |
| pingcap/vldb-boss-2018             | 0.0 mins      |                                                      |                          |                        |
| pingcap/errors                     | 0.0 mins      |                                                      |                          |                        |
| pingcap/errcode                    | 0.0 mins      |                                                      |                          |                        |
| pingcap/tidb-engine-ext            | 5636.53 mins  |                                                      |                          |                        |
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
| pingcap/log                        | 0.0 mins      |                                                      |                          |                        |
|                                    |               | Audit License                                        | 0.0 mins                 | 0.0 mins               |
|                                    |               | Unit Test                                            | 0.0 mins                 | 0.0 mins               |
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
| pingcap/diag                       | 121.88 mins   |                                                      |                          |                        |
|                                    |               | reprotest                                            | 11.18 mins               | 89.45 mins             |
|                                    |               | static-tests                                         | 3.24 mins                | 32.43 mins             |
| pingcap/sqlsmith                   | 0.0 mins      |                                                      |                          |                        |
| pingcap/public_bi_benchmark        | 0.0 mins      |                                                      |                          |                        |
| pingcap/tispark-test               | 0.0 mins      |                                                      |                          |                        |
| pingcap/monitoring                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/presentations              | 0.0 mins      |                                                      |                          |                        |
| pingcap/tiflow                     | 53604.6 mins  |                                                      |                          |                        |
|                                    |               | integration-tests                                    | 0.0 mins                 | 0.0 mins               |
|                                    |               | Check & Build                                        | 15.95 mins               | 18102.83 mins          |
|                                    |               | mysql-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | avro-ntegration-tests                                | 0.0 mins                 | 0.0 mins               |
|                                    |               | canalJson-integration-tests                          | 0.0 mins                 | 0.0 mins               |
|                                    |               | canal-integration-tests                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | oldValue-integration-tests                           | 0.0 mins                 | 0.0 mins               |
|                                    |               | unit-test                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | RFCs Lint                                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Design Docs Lint                                     | 0.54 mins                | 24.83 mins             |
|                                    |               | Upgrade DM via TiUP                                  | 5.3 mins                 | 1112.22 mins           |
|                                    |               | DM Chaos                                             | 27.95 mins               | 5870.02 mins           |
|                                    |               | Auto Assign to Bugs and Questions                    | 0.27 mins                | 183.63 mins            |
|                                    |               | DM Binlog 999999                                     | 13.95 mins               | 2928.93 mins           |
|                                    |               | Upstream Database Switch                             | 15.51 mins               | 3256.95 mins           |
|                                    |               | CDC Integration Tests                                | 17.71 mins               | 15446.52 mins          |
|                                    |               | CDC Canal-JSON-Extension Tests                       | 0.0 mins                 | 0.0 mins               |
|                                    |               | DM Web UI Lint                                       | 1.51 mins                | 4.52 mins              |
|                                    |               | Dataflow engine unit test                            | 0.0 mins                 | 0.0 mins               |
|                                    |               | Dataflow Engine Chaos                                | 31.77 mins               | 6671.93 mins           |
|                                    |               | Dataflow Engine Image                                | 0.0 mins                 | 0.0 mins               |
| pingcap/br                         | 10.18 mins    |                                                      |                          |                        |
|                                    |               | compatibility-test                                   | 2.23 mins                | 2.23 mins              |
|                                    |               | build                                                | 7.95 mins                | 7.95 mins              |
| pingcap/go-randgen                 | 0.0 mins      |                                                      |                          |                        |
| pingcap/k8s-fluent-bit-stackdriver | 0.0 mins      |                                                      |                          |                        |
| pingcap/advanced-statefulset       | 0.0 mins      |                                                      |                          |                        |
|                                    |               | ci                                                   | 0.0 mins                 | 0.0 mins               |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
| pingcap/style-guide                | 0.0 mins      |                                                      |                          |                        |
| pingcap/go-tpc                     | 1.1 mins      |                                                      |                          |                        |
|                                    |               | release                                              | 0.0 mins                 | 0.0 mins               |
|                                    |               | workflow                                             | 1.1 mins                 | 1.1 mins               |
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
| pingcap/dumpling                   | 8.17 mins     |                                                      |                          |                        |
|                                    |               | Go                                                   | 8.17 mins                | 8.17 mins              |
+------------------------------------+---------------+------------------------------------------------------+--------------------------+------------------------+

```
</div>
</details>
* * *
    

<details><summary><b>tgbot-collection</b> <i>[click to show]</i></summary>
<div>

```
    
Error: {'total_count': 0, 'workflow_runs': []}
Error: {'total_count': 0, 'workflow_runs': []}
