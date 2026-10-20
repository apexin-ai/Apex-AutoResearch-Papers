# infra westd16639 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd16639-status-check_20260521T194837_result.json`
- **Structured JSON:** [`24cd05a8b3b9b1f33bd2.json`](../../sessions/24/24cd05a8b3b9b1f33bd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 进度汇报

### 1. Cross-model SICA 2×2 (exp_d126)

**状态：停止于 177/204（87%），疑似崩溃**

- 启动时间：2026-05-21 16:40 (+0800)
- 最后日志：2026-05-22 03:49:44 (+0800)，之后再无写入
- 处理速度：~3.7 min/sample
- 剩余 27 个 sample，预计需 ~100 分钟

**5 个子目录均已部分产出：**

| 子目录 | 说明 |
|---|---|
| `mistral_traces/` | Mistral 推理 traces |
| `extraction_qwen3_same/` | Qwen3 同模型抽取 |
| `extraction_mistral_same/` | Mistral 同模型抽取 |
| `extraction_mistral_cross_qwen3/` | Mistral trace → Qwen3 跨模型抽取 |
| `extraction_qwen3_cross_mistral/` | Qwen3 trace → Mistral 跨模型抽取（**已修复**）|
| `extraction_qwen3_cross_mistral_buggy/` | 修复前的旧数据（备份）|

### 2. Qwen3→Mistral fix

修复已集成到主流程中，不是独立进程。旧 buggy 数据保留在 `extraction_qwen3_cross_mistral_buggy/`（02:12），修复后的数据在 `extraction_qwen3_cross_mistral/`（03:48）。`data/qwen3_crossmodel_fixed/` 不存在，`nohup.out` 也不存在。

### 3. Gemini 数据

**有少量残留：** `results/exp_d135_frontier_scb/google_gemini-2.5-pro/results.json`
`data/gemini*/` 不存在。exp_d135_frontier_scb 下还有 `gpt-4.1/`、`gpt-5.5/`、`o3/`、`comparison.json`。

### 4. GPU 状态

| GPU | 显存 | 利用率 | 说明 |
|---|---|---|---|
| 0 | 84.2/97.9 GB | 0% | vLLM 已加载，空闲 |
| 1 | 83.6/97.9 GB | **100%** | 活跃（但实验日志已停更） |
| 2 | 0/97.9 GB | 0% | 空闲 |
| 3 | 87.9/97.9 GB | 0% | vLLM 已加载，空闲 |

### 需要关注

- **实验进程可能已死但 vLLM 仍在运行**（GPU 1 100% util 但日志不再更新）。建议检查 python 进程状态，可能需要重启实验从 checkpoint 恢复（phase1_checkpoint.json 记录了已完成的 PID）。

---
