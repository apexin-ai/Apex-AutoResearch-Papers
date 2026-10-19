# analysis benchmark table final

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_benchmark-table-final_20260516T165941_result.json`
- **Structured JSON:** [`1ded7822d8af5c1741db.json`](../../sessions/1d/1ded7822d8af5c1741db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已更新完成。变更摘要：

**Main Results 表**：
- 替换 TEAL 30%/50% unified 的 "— queued" 为实际数据
- 新增 KL 40% global 行 (PPL=10.117, ARC=0.4096, WG=0.6535, MMLU=0.3806, GSM8K=0.05)
- 保留 TEAL 50% † (lm_eval) 行作为参考，标注 "retained for reference only"

**新增 Multi-seed stability 表**：3 seeds 全部 5 个指标的逐种子值 + mean/std/CV

**Relative Change 表**：新增 KL 40% global (+65.4% PPL, −41.7% MMLU)、TEAL 30% (+79.3% PPL)、TEAL 50% unified (+281.1% PPL)

**Key Observations 更新**：
- Obs 1: TEAL 数据从旧 27.97 更新为 unified 23.31
- Obs 2: 新增 40% uniform vs global 的反转现象（global MMLU 0.3806 > uniform 0.3068）
- 新增 Obs 5: KL 30% ≈ TEAL 30% 在 downstream 上差异不大，KL 优势主要在 PPL
- 新增 Obs 6: Multi-seed stability

---
