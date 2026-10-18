# writing paper w5 w6 n2 patch

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-w5-w6-n2-patch_20260515T223533_result.json`
- **Structured JSON:** [`22da73513d87c7b9bc8f.json`](../../sessions/22/22da73513d87c7b9bc8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。总结：

**Task 1 (W5)**: `method.tex` — 将 "unconditional generation" 改为 "sampling from the LoRA-finetuned model"，明确每层 depth 是先 LoRA finetuning on $\mathcal{D}_{k-1}$ 再采样，新增一句澄清"不是从原始 base model 采样"。

**Task 2 (W6)**: `atlas.tex` §4.1 — 新增 per-class recall 段落，报告 d2 recall 最低（55–71%），引用 Pythia nucleus (d0=99%, d1=82%, d2=59%, d3=76%) 和 GPT-2 XL temp (d2=71%) 具体数字，解释 d2 处于 depth gradient 中间位置导致特征空间最易混淆。`section_appendix.tex` — 新增 §Per-Class Recall (app:per\_class)，含 9 cell 完整 per-class recall 表格。

**Task 3 (N2)**: `generalization.tex` §5.4 — RoBERTa-base → RoBERTa-large；显式报告 gap（-19.9pp / -18.7pp）；新增 scale caveat（≤355M backbone，7B+ 是否缩小差距尚未验证）。

---
