# analysis r28 data consistency

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r28_data_consistency_20260524T004342_result.json`
- **Structured JSON:** [`a23c7e67184f8c0bd80d.json`](../../sessions/a2/a23c7e67184f8c0bd80d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。报告已写入 `artifacts/r28_data_consistency_report.md`。

**关键发现：**

**5 个 must-fix：**

1. **Table 2 KL 50% global 行** — PPL 11.84±0.15 及 ARC-c/WG/GSM8K 无法从任何 registry 实验组合复现。PPL 的 std 最接近的组合只给出 ±0.07，downstream 值也有 1-2pp 偏差。根因：不同 seed 的 PPL 和 downstream 来自不同 eval run，混用了实验源。

2. **C4 control 表 WikiText 行 HS/PIQA** — 69.4/75.5 与同篇论文 OOD downstream 表的 70.9/74.8 矛盾（同一个 predictor），registry 支持后者。

3. **C4 control 表 C4 行 PIQA** — 论文 74.86 vs registry 75.03，差 0.17pp。

4. **Extended downstream 表 TEAL 30% uniform PIQA** — 论文 72.80 vs registry 71.98，差 0.82pp（疑似 acc vs acc_norm 混用）。

5. **"148× compression" for Qwen14B** — 从 registry 的 117M 参数量反算，d_ff≈13923（109×），不是 18944（148×）。

**大部分数据一致：** Table 3（C1 ablation）40/40 全匹配，cross-arch 表全匹配，latency 表全匹配，所有 inline 计算（14.5% reduction、7.3× σ 等）全部正确。约 83% 的数据点完全通过验证。

---
