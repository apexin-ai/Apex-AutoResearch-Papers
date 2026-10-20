# infra save old outputs

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_save_old_outputs_20260514T084951_result.json`
- **Structured JSON:** [`463325e83103be6ce313.json`](../../sessions/46/463325e83103be6ce313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### `/root/outputs/` 目录
**不存在。** 没有 `results.json`、`results_partial.json`、`mvp_report.json` 等任何输出文件。在整个服务器上搜索也未找到这些文件。

### 旧 MVP 运行状态（`/root/mvp_run.log`，2.7MB）
- **配置**: 50 problems × 8 chains = 400 total chains (ProofWriter depth-5)
- **进度**: 只完成了 **1/50** 个 problem，正在处理第 2 个时日志停止
  - Problem 1 (`pw_AttNeg-OWA-D5-1087`): 耗时 ~34 分钟，SVS=Unknown (correct=True), SC=False (correct=False)
  - Problem 2 (`pw_RelNeg-OWA-D5-28`): 在 formalization 阶段（chain 6 的 claim 分解），日志最后时间 16:43
- **错误**: 3 次 `502 Bad Gateway`（外部 API `47.94.22.126`），被 retry 处理掉了
- **进程**: 原始 MVP 进程已不在运行

### 备份
**无文件可备份。** 旧 MVP 运行未生成任何持久化结果文件，推测 pipeline 设计为全部完成后才写 results.json，而进程在 Problem 2 期间中断或被终止。

### 当前进程
服务器上有 2 个 **dryrun** 进程正在运行（`config_dryrun.yaml`，输出到 `outputs_dryrun/`），该目录目前为空，`dryrun.log` 2.2KB 刚创建。

---
