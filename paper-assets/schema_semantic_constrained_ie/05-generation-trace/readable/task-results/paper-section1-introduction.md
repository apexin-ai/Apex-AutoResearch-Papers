# paper section1 introduction

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section1_introduction_20260514T054035_result.json`
- **Structured JSON:** [`602bec3e8f5f87bda160.json`](../../sessions/60/602bec3e8f5f87bda160.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/section1_introduction_draft.tex` 并注册到 manifest。

结构：
- **P1** (8句): 问题定义 + SciERC 15.4%/DocRED 18.7% violation 数据 + 非均匀分布（Compare 42.4% vs Used-for 0.8%）+ constraint tightness 驱动
- **P2** (6句): Schema-informed prompting ↓62% 但 per-relation 不可靠（Evaluate-for +5.8pp）；grammar-constrained decoding 无 semantic；post-hoc 浪费 14-15% 算力；training-based 需数据且 soft
- **P3** (6句): OntoCoDec 双层架构（grammar + semantic）+ bitwise AND 组合 + enabling dependency + training-free + DR 15.37%→0.93% F1-neutral
- **P4** (4 contributions): violation landscape → OntoCoDec 框架 → decidability taxonomy → 实证验证

所有数字与 registry 一致，用 "near-complete"/"designed to be model-agnostic" 等 calibrated 措辞，引用 key 与已有 sections 保持统一。

---
