# paper writing experiments

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260516T021635_result.json`
- **Structured JSON:** [`d49cefe05d8b0c998055.json`](../../sessions/d4/d49cefe05d8b0c998055.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。两个文件已写入 `docs/paper/`:

**`experiments.tex`** — Section 3 完整 LaTeX，包含:
- **3.1 Experimental Setup**: LIBERO-Goal, OpenVLA-7B, 5 种表征源, 2×2 实验设计, RSA + functional probe 方法
- **3.2 Vision Encoder Dominance**: Table 1 (RSA 排序), Figure 2, geometric-functional dissociation (DINO R²≈Proj 但 RSA<<), CKA 排序反转负向结果 (Figure 6)
- **3.3 LLM Redistributes Action Structure**: Table 2 (probe R²), Figure 3 (per-layer curves), Figure 4 (probe bars), distributed degradation + readout concentration
- **3.4 Training Routes, Not Creates**: Table 3 (训练效应), Figure 5 (2×2 matrix + instruction control), geometric null + functional concentration dissociation

**`references.bib`** — 12 条 BibTeX，其中 `grant2026` 和 `haon2025` 标记了 `[VERIFY]`，需要补全真实书目信息。其余 10 条基于已知信息填写。

---
