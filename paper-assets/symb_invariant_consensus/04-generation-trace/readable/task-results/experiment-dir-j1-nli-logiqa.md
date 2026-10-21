# experiment dir j1 nli logiqa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-j1-nli-logiqa_20260520T173020_result.json`
- **Structured JSON:** [`a0af19a78456be48afb3.json`](../../sessions/a0/a0af19a78456be48afb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果写入 `/root/symb_invariant_consensus/results/dir_j1_nli_logiqa/results.json`。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| SC accuracy (baseline) | 0.5300 (106/200) |
| NLI-only accuracy | 0.2900 (58/200) |
| **w=1**: combo acc | 0.5400, Δ=+1.00pp, p=0.500, disc=(2,0) |
| **w=3**: combo acc | 0.5300, Δ=+0.00pp, p=1.000, disc=(3,3) |
| **w=5**: combo acc | 0.5350, Δ=+0.50pp, p=1.000, disc=(5,4) |

**关键发现：**
- NLI-only 准确率仅 29%（低于随机 25% 不多），DeBERTa-MNLI verifier 在 LogiQA 上几乎无用——因为 LogiQA 需要逻辑推理而非表面文本蕴含
- SC+NLI 组合在所有权重下无统计显著提升（最高 Δ=+1pp, p=0.5）
- NLI escape 现象**不跨数据集泛化**到 LogiQA：DeBERTa-MNLI 在 FOLIO/ProofWriter 上可能有效是因为那些任务的正确答案与前提有直接蕴含关系，而 LogiQA 多选题的正确答案需要多步推理推导，NLI 模型无法捕捉

---
