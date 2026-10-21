# writing dou et al citation

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_dou-et-al-citation_20260525T224600_result.json`
- **Structured JSON:** [`deff99e6c5efc39d54ec.json`](../../sessions/de/deff99e6c5efc39d54ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**搜索结果**：不存在 "Dou et al. 2024" 的 attention forcing 论文。相关论文为 Dou et al. 2019（arXiv:1909.12289）和 Dou & Gales 2022（arXiv:2211.03237），两篇已在 bib 中。

**编辑内容**：在两份 `discussion.tex` 的第 2 段后新增 1 段（2 句），覆盖 R6-SF4 的 3 点要求：
1. **AR 退化**：Dou et al. 独立观察到 teacher forcing 下学到的 attention 在 AR 推理时退化
2. **回溯解释**：他们的诊断与我们的 exposure bias 发现一致
3. **方法论互补**：他们 intervene（监督 cross-attention），我们 diagnose（揭示 self-attention 辅助目标在 NTP 联合训练下仍无法迁移）——互补视角，共同指向 teacher-forcing gap 的结构性障碍

Sources:
- [Attention Forcing for Sequence-to-sequence Model Training](https://arxiv.org/abs/1909.12289)
- [Parallel Attention Forcing for Machine Translation](https://arxiv.org/abs/2211.03237)

---
