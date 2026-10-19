# HB-GEN-1 SWE-Perf wrapper image runbook

## 状态

本文件描述 **离线准备与后续 canary 门禁**，不是运行授权。当前 P0 结果通道已机械判定为
`in_process_candidate_outcome_unattestable`，production supervisor 会在启动 worker 前 fail closed。
仓库中的生成器不会连接 Docker、
不会拉取或构建镜像，也不会运行 evaluator。八个上游 digest 只代表已经装好依赖与 repository
的基础镜像；它们不是带 HB-GEN-1 私有结果通道的可信评分镜像。

正式运行前仍必须为八题分别得到并冻结：

- 上游基础镜像的完整 `repository@sha256:<digest>`；
- 从固定 dataset parquet 行机械导出的 correctness/performance argv、精确 test node IDs 和允许
  修改的 repository paths；
- wrapper 构建后的新 manifest digest、image ID、RepoDigest 和完整 labels；
- reference、no-op、correctness regression、伪 stdout 与残留后台进程 canary。
- 一个不改变冻结 pytest outcome/call-duration 语义、又能由可信进程独立导出这两个信号的新
  evaluator 合同；它必须另行设计、授权和冻结。

任何一项缺失时，SWE-Perf family 保持 blocked；不能把上游 digest 直接填成 wrapper digest。

## 离线生成

输入 source lock 是严格 JSON：顶层固定 evaluator/dataset hash，并按冻结顺序包含八个 task
manifest。每题 command 必须是无 shell 的绝对 argv，恰好含一个 `{report_path}`；`bash -c`、
`curl/wget/ssh`、URL、mutable image tag、非 20 次计时或改变资源 envelope 都会 fail closed。
当前 preparer **不会生成这份 runnable source lock**；它只写包含 capability verdict 的
content-addressed blocked report。下面命令仅描述未来新 evaluator 通过门禁后的离线 context API。

```bash
PYTHONPATH=. .venv/bin/python scripts/prepare_hb_sweperf_wrappers.py \
  --source-lock /absolute/private/path/sweperf-wrapper-source-lock.json \
  --output-root /absolute/private/path/sweperf-wrapper-contexts
```

输出的每题 context 包含：

- `Dockerfile`：`FROM` 直接绑定上游 digest；只 `COPY` root supervisor/manifest；没有包管理、下载
  或 evaluator 执行；
- `/opt/hb-sweperf/bin/evaluate-stage` 对应的 `evaluate-stage`，以及 `supervisor.py` 和固定
  fail-closed capability gate `trusted_result.py`；
- canonical `task-manifest.json` 和独立 digest 文件；
- `build-context.json`：所有输入文件 SHA、labels、`network_mode=none`、`pull_policy=never`。

生成是 write-once；同路径出现不同内容时拒绝覆盖。

## 后续构建门禁（本实现未执行）

构建机先用 `docker image inspect` 证明上游 digest 已在本地，然后才允许使用同一 context 执行
等价于 `docker build --pull=false --network=none` 的构建。禁止 login、pull、mutable tag、远程
BuildKit context 和构建期 secret。构建结束后必须取得新的 wrapper `RepoDigest`，逐项核对：

- 静态 image contract/version/entrypoint、uid 与 private-channel labels；
- task-manifest、supervisor bundle、上游 ref、资源 envelope、instance/task hash labels；
- image entrypoint 精确为 `/opt/hb-sweperf/bin/evaluate-stage`。

`ProductionSWEPerfDockerExecutor` 还要求 controller 显式传入生成器产出的
`WrapperImageIdentity`；仅伪造旧静态 labels 的镜像不能创建 workspace。

## P0：为什么当前结果通道不可证明

冻结的上游命令在 uid 65534 的同一个 pytest 进程内同时执行任意 candidate Python、产生 test
outcome、记录 pytest call duration，并写 JSON。因而 candidate 可以不运行断言，直接写出全 passed、
任意短 duration，并选择进程退出码。JSON 在退出后被 root 读取、移动到 0600 文件或绑定 nonce，
只能证明 root 读到了哪些字节，不能证明这些字节由可信裁决器产生。

以下改法均不能闭合证明：

- root-owned 文件只改变最终 ownership，不改变 worker 运行期间的 writer；
- private FD/HMAC 与 candidate 位于同一地址空间，candidate 也能访问该 capability；
- 独立 monitor 只能可信观察外层 wall clock、进程存活和 quiescence，无法推出 test assertion outcome
  或 pytest call duration；
- 用外层 wall clock 替代 call duration 会改变冻结评分语义；让 root 直接 import patched repository
  则把任意 candidate Python 提升为 root 代码。

因此当前唯一安全行为是阻断。若继续 SWE-Perf，必须另立方案，把可信 test/oracle 与 candidate
执行放在不同安全域，并为八题定义 task-specific RPC 或等价的外置 oracle。因为这些测试传递复杂
Python object、文件与框架状态，通用 JSON RPC 不能被假定为语义等价；新 scorer 需要用户另行批准。
固定 capability verdict 记录 candidate/report 共享进程、worker 可控信号、root 可观测信号、被否决
的伪修复和所需 redesign；其 core 使用 canonical JSON 内容寻址。

## 已实现但当前不可达的旧运行时边界

- outer Docker：`--network=none`、只读 rootfs、cap-drop、固定 seccomp、每 attempt 独立
  scratch/cache/private volume；安全上限固定 **10 CPU / 32 GiB / 512 PID**。
- root supervisor：只读 root-owned request 与 baked task manifest；先复制并哈希 candidate patch，
  只执行 `git apply --check --whitespace=error-all` 后的精确 `git apply`，没有 fuzzy fallback。
- worker：固定 uid 65534，清空 proxy/credential 环境；stdout/stderr 直接到 `/dev/null`。旧实现曾
  读取 worker 写的精确 test-ID report；该路径现已在 spawn 前由 capability gate 禁用，不能再产生
  correctness receipt 或 performance score。
- quiescence：每个 worker command 返回后扫描容器 PID namespace。只要看见残留 worker，即使 root
  成功 kill，当前 stage 仍失败；不能把后台工作留给计时或下一 stage。
- correctness receipt：绑定 task-manifest SHA、完整 request binding、nonce、patch SHA、candidate
  state SHA 与 correctness evidence SHA。performance 必须读取并复算 root-only receipt state。
- performance：3 次 warmup，20 次 reference/candidate 交错测量；每次 candidate report 都重新检查
  correctness。score formula 在 manifest 中固定为 `geomean-median-speedup-v1`，discovery stdout
  或 wall-clock 文本永远不进入公式。

## 当前阻断项

代码与 fake tests 只证明合同、攻击复现和 fail-closed 控制流。正式 SWE-Perf 仍需：先批准并实现
独立可信 oracle/结果通道，再补八个本地上游 RepoDigest、八行私有
dataset-derived command/test/path manifest、实际 wrapper build receipt、任务环境对复制后的
`/testbed`/conda editable install 的兼容性 canary，以及 11 个完整 evaluator canary。出现任何
不兼容都必须以新 code revision/result root 修复；旧失败不覆盖、不退款。
