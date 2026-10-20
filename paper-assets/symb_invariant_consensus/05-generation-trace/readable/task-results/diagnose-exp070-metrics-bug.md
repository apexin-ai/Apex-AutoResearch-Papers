# diagnose exp070 metrics bug

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp070-metrics-bug_20260519T135521_result.json`
- **Structured JSON:** [`09f78b5e57639e6137b4.json`](../../sessions/09/09f78b5e57639e6137b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。以下是结论：

```json
{
  "root_cause": "Diagnostic worker agent (LLM) 幻觉生成了 79.5% 的数值。服务器上没有任何文件包含 0.795 作为准确率指标——对 exp070 整个 results 目录及全服务器 results/ 做了穷尽搜索，仅在无关字段（solve_time_ms、satisfied_ratio、timestamps）中找到 0.795 子串。Worker 未从数据文件读取该值，而是 confabulated 了一个不存在的数字。",
  "wrong_data_source": "无明确数据源。79.5% 是 LLM 幻觉产物，不来自 dryrun_results.json（60%/60%, n=5）、exp070_results.json（68.5%/71.0%）、run log（被 SIGHUP 截断于 188/200 题，无 final summary）、或服务器上任何其他实验结果文件。SC=SICA=79.5%（两个不同指标恰好相同）进一步佐证幻觉——实际值 SC≠SICA (68.5% vs 71.0%)。",
  "correct_data_confirmed": true,
  "exp068_structure": "exp068 不在 westd-25068 服务器上（find 搜索 exp068* 结果为空），无法直接对比文件结构。从 mistakes.yaml M029 记录看，exp068 由同一 worker 在同一 session 诊断，metrics 报告正确（SC=81%, SICA=81%）。",
  "exp070_structure": "目录 /root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/ 包含：dryrun.log (16KB)、dryrun_results.json (9KB, n=5)、exp070_results.json (373KB, n=200, summary 正确)、exp070_run.log (605KB, 7088行, 被 SIGHUP 截断于 188/200 题)、intermediates/ (200个 per-problem JSON)、per_trace_constraints/ (200个文件)。结构完整，数据正确。",
  "recommendation": "1. Diagnostic worker 读取 metrics 后必须做交叉验证：将 JSON summary 的 sc_accuracy/sica_accuracy 与逐条 sc_correct/sica_correct 的 count 对比，不一致则报警。2. Worker 写入 registry 前，log 数据源文件路径和读取到的原始值（如 'read from exp070_results.json: summary.sc_accuracy=0.685'），便于审计。3. Registry metrics 写入后增加 guard：与结果文件 summary 做 diff，差距>1pp 自动拒绝并告警。4. 当前 checkpoint 文件 notes 字段仍包含错误的 'SC=SICA=0.795'（与同文件 metrics 字段矛盾），建议清理。"
}
```

**关键发现总结**：

| 来源 | SC | SICA | Δ |
|---|---|---|---|
| exp070_results.json (正确) | 68.5% (137/200) | 71.0% (142/200) | +2.5pp |
| Diagnostic worker 报告 (错误) | 79.5% | 79.5% | 0 |
| dryrun_results.json | 60% (3/5) | 60% (3/5) | 0 |
| run log (截断) | 135V/53X (188题) | 137V/51X (188题) | — |

M030 (mistakes.yaml) 将 root cause 归为"可能读取了错误的数据源"——本次排查证明这个归因不准确。**服务器上不存在任何包含 79.5% 准确率的数据源**，根因是 worker agent 的 LLM 幻觉。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Diagnostic worker agent (LLM) 幻觉生成了 79.5% 的数值。服务器上没有任何文件包含 0.795 作为准确率指标——对 exp070 整个 results 目录及全服务器 results/ 做了穷尽搜索，仅在无关字段（solve_time_ms、satisfied_ratio、timestamps）中找到 0.795 子串。Worker 未从数据文件读取该值，而是 confabulated 了一个不存在的数字。",
    "wrong_data_source": "无明确数据源。79.5% 是 LLM 幻觉产物，不来自 dryrun_results.json（60%/60%, n=5）、exp070_results.json（68.5%/71.0%）、run log（被 SIGHUP 截断于 188/200 题，无 final summary）、或服务器上任何其他实验结果文件。SC=SICA=79.5%（两个不同指标恰好相同）进一步佐证幻觉——实际值 SC≠SICA (68.5% vs 71.0%)。",
    "correct_data_confirmed": true,
    "exp068_structure": "exp068 不在 westd-25068 服务器上（find 搜索 exp068* 结果为空），无法直接对比文件结构。从 mistakes.yaml M029 记录看，exp068 由同一 worker 在同一 session 诊断，metrics 报告正确（SC=81%, SICA=81%）。",
    "exp070_structure": "目录 /root/symb_invariant_consensus/results/exp070_qwen7b_logiqa200/ 包含：dryrun.log (16KB)、dryrun_results.json (9KB, n=5)、exp070_results.json (373KB, n=200, summary 正确)、exp070_run.log (605KB, 7088行, 被 SIGHUP 截断于 188/200 题)、intermediates/ (200个 per-problem JSON)、per_trace_constraints/ (200个文件)。结构完整，数据正确。",
    "recommendation": "1. Diagnostic worker 读取 metrics 后必须做交叉验证：将 JSON summary 的 sc_accuracy/sica_accuracy 与逐条 sc_correct/sica_correct 的 count 对比，不一致则报警。2. Worker 写入 registry 前，log 数据源文件路径和读取到的原始值（如 'read from exp070_results.json: summary.sc_accuracy=0.685'），便于审计。3. Registry metrics 写入后增加 guard：与结果文件 summary 做 diff，差距>1pp 自动拒绝并告警。4. 当前 checkpoint 文件 notes 字段仍包含错误的 'SC=SICA=0.795'（与同文件 metrics 字段矛盾），建议清理。"
  }
}
```

</details>

---
