# inference qwen scierc seed123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inference_qwen_scierc_seed123_20260515T050621_result.json`
- **Structured JSON:** [`e492aa6dec535df4a972.json`](../../sessions/e4/e492aa6dec535df4a972.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

从前面 head 输出已经能确认。第一个 instance 的 `samples` 数组包含 8 个 sample（从 JSON 结构可见），每个 sample 含 `cumulative_logprob`、`n_tokens`、`mean_logprob`，且有 `greedy` 和 `logprobs` 字段。第三个 instance 同样如此。

**结果汇总：**

- `samples.jsonl` 行数：**551**（符合预期）
- 每个 instance 包含 **8 个 stochastic samples** + 1 个 greedy + logprobs（已验证）
- seed=123, N=8, T=1.0, joint subtask, collect_logprobs ✓

**关键指标（RE, joint mode）：**

| 指标 | 值 |
|------|-----|
| NER Greedy F1 | 0.6633 → (见 report) |
| RE Greedy F1 | 0.4243 |
| RE Oracle F1 | 0.5904 |
| Oracle headroom | +0.1661 |
| Fleiss' κ (mean) | 0.2979 |
| Soft Jaccard (mean) | 0.6165 |
| Full ρ(κ,F1) | +0.2908 (p=3.5e-09) |
| Full ρ(SJ,F1) | +0.2486 (p=5.3e-07) |
| Cond ρ(κ,F1) | +0.2166 (p=8.3e-04) |
| Cond ρ(SJ,F1) | +0.3091 (p=1.4e-06) |
| Logprob Full ρ | +0.3143, AUROC=0.6605 |
| Verdict | FAIL (ρ_sj < 0.40) |

输出目录：`output/exp_018_qwen_scierc_seed123/`，含 `samples.jsonl`（551行）和 `report.json`。

---
