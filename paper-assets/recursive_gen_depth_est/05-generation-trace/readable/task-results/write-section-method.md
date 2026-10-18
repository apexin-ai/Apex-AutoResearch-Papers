# write section method

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_section_method_20260515T162257_result.json`
- **Structured JSON:** [`e551566e610837bb9e85.json`](../../sessions/e5/e551566e610837bb9e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/_project/paper/section_method.tex` 并注册 (`art_20260515_d088f8`)。

相比原版的主要修改：

1. **Seed corpora 修正** — "Wikipedia subset" → OpenWebText (Pythia) / Dolma (OLMo) / WebText (GPT-2 XL)
2. **LoRA targets 修正** — Pythia 补入 q_proj/v_proj 组
3. **Unconditional generation 明确声明** — 加粗 `\emph{unconditional generation} (no prompt conditioning)` 并解释动机（reviewer W5）
4. **Feature 表扩展** — 从分组摘要改为逐一列出 19 个特征的名称和描述（Table 1）
5. **p90_ppl 关键洞察增强** — 加入 kurtosis > 4,900 outlier 对比、top-2 出现率 9/9 (100%) 和 var_surprisal 7/9 (78%) 具体数据
6. **Notation 前置** — Problem Definition 末尾引入 $\mathbf{f}(x)$ 和 $\mathrm{EDD}_T$ 符号，建立后续引用锚点

---
