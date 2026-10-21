# reanalyze d102 pythia410m opt1b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_reanalyze_d102_pythia410m_opt1b_20260519T154931_result.json`
- **Structured JSON:** [`12ceb412fc0a6493a46d.json`](../../sessions/12/12ceb412fc0a6493a46d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是新旧对比：

---

## Pythia-410M (`generalize_pythia410m_wiki_a100_s42`)

| 指标 | 旧 (→ppl) | 新 (→mauve) | 变化 |
|------|----------|------------|------|
| PermG fwd | 6/8 | 6/8 | = |
| PermG rev | 0/8 | 0/8 | = |
| Diff fwd FDR | 8/8 | **6/8** | **-2** |
| Diff rev FDR | 8/8 | **6/8** | **-2** |
| Threshold | 0/8 | 0/8 | = |
| TY fwd | 2/8 | **1/8** | **-1** |
| K≥3 (MMCT) | 2/8 (25%) | **1/8 (12.5%)** | **-1** |
| K≥4 | 0/8 | 0/8 | = |

mauve pairs 全灭：token_entropy→mauve 0/5，ece→mauve 1/5（仅 naive）。

---

## OPT-1.3B (`generalize_opt1b_wiki_a100_s42`)

| 指标 | 旧 (→ppl) | 新 (→mauve) | 变化 |
|------|----------|------------|------|
| PermG fwd | 6/8 | 6/8 | = |
| PermG rev | 0/8 | 0/8 | = |
| Diff fwd FDR | 8/8 | **7/8** | **-1** |
| Diff rev FDR | 8/8 | **7/8** | **-1** |
| Threshold | 1/8 | **2/8** | **+1** |
| TY fwd | 0/8 | 0/8 | = |
| K≥3 (MMCT) | 2/8 (25%) | 2/8 (25%) | = |
| K≥4 | 0/8 | 0/8 | = |

OPT-1.3B 相对稳健——K≥3 不变（distinct pairs 撑住），mauve pairs 弱但 ece→mauve threshold 意外 sig。

---

**跨模型一致性**：3个模型（GPT-2m/Pythia-410M/OPT-1.3B）统一 →mauve 后，K≥4 全部 0/8，PermG fwd 稳定 6/8。mauve 作为 downstream 在所有模型上都不产生 lead-lag 信号——canary 指标对 mauve 没有预测力，与 D101 GPT-2m 先例完全一致。

---
