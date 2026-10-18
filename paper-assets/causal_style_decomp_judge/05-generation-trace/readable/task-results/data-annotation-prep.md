# data annotation prep

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_annotation-prep_20260522T230741_result.json`
- **Structured JSON:** [`b79bfe50584fda71ada6.json`](../../sessions/b7/b79bfe50584fda71ada6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**抽样统计：**

| | Formality | Verbosity | Total |
|---|---|---|---|
| NLI pass | 35 | 35 | 70 (70%) |
| NLI fail | 15 | 15 | 30 (30%) |
| **合计** | **50** | **50** | **100** |

- Pass/fail 比例：70%/30%（精确达标）
- 与 batch 1 (S001-S050) 无重叠（按轴检查）
- 跨轴共享 source_id：10 个（预期行为，同源文本不同方向的 counterfactual）
- NLI 分数分布：pass mean=0.9911, fail mean=0.6556
- 新样本 ID 范围：S051-S150
- 数据来源：formality pass 来自 `verified_scaled_formality.jsonl`，formality fail 来自 `verified_32b.jsonl`，verbosity pass 来自 `verified_verbosity.jsonl`，verbosity fail 组合自 3 个 verified 文件

**产出文件路径（服务器）：**
- `/root/causal_style_decomp_judge/artifacts/r14_fixes/annotation_batch2_samples.json` (163KB)
- `/root/causal_style_decomp_judge/artifacts/r14_fixes/annotation_batch2_samples.csv` (147KB)
- `/root/causal_style_decomp_judge/artifacts/r14_fixes/annotation_batch2_template.csv` (147KB，含空标注字段 preserves_meaning / style_change_detected / notes)

---
