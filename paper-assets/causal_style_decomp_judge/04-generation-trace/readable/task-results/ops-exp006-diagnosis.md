# ops exp006 diagnosis

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp006_diagnosis_20260521T044330_result.json`
- **Structured JSON:** [`0a645938ff1152e57957.json`](../../sessions/0a/0a645938ff1152e57957.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：进程**未卡住**，正常运行中

### 状态

| 指标 | 值 |
|------|-----|
| vLLM 进程 | 正常运行，port 8002，Qwen3-32B TP=1 |
| cuda:2 | 88361 MiB 已用，利用率 100% |
| 生成进程 | PID 106785，活跃中 |
| 输入文件 | `scaled_formality_input.jsonl` = **400 条** |
| 已处理 | **134 条**（日志计数），输出文件 132 行（写入略有延迟） |
| 启动时间 | 12:16，当前 12:44 |

### 根因

**不是卡住，是速度慢。** 之前 worker 轮询时看到 98 条，以为不增长，实际上是每条记录需要 3 次 HTTP 请求（original / counterfactual / double_rewrite），单条处理耗时 ~3-20 秒不等。

- 处理速率：134 条 / 28 分钟 ≈ **4.8 条/分钟**
- 剩余：266 条
- **预计还需 ~55 分钟完成**（约 13:40 左右）

### 数据源

输入的 400 条已由多源合并：
- `mvp_samples.jsonl`：100 条（LLMBar，已全部处理完）
- `verified_alpacaeval.jsonl`：存在（272KB）
- `verified_mtbench.jsonl`：存在（428KB）

当前正在处理 alpacaeval 批次（已到 alpacaeval_033）。

### 建议

无需干预，等它跑完即可。如需加速，可考虑增大 batch size 或并行请求，但当前进程不应中断。

---
