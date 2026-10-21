# knowledge update review issues

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_update-review-issues_20260519T054922_result.json`
- **Structured JSON:** [`824cdf0d1bb9cdbfb0a0.json`](../../sessions/82/824cdf0d1bb9cdbfb0a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。以下是所有 **非 resolved/closed** 条目，按严重度排序：

### Critical

| ID | Summary | Status | 关键进展 |
|---|---|---|---|
| **R8-N1** | θ=0.60 post-hoc 循环论证 | in_progress | leave-one-family-out CV 已入稿 (C4 8/9, arXiv 6/6)，但 R10 仍标为最大 concern |
| **R8-N2** | prompt-chain vs retrain-chain 差距 | in_progress | OLMo-1B retrain-chain 实验运行中；正文可见度待提升 |
| **R8-N3** | 'domain as sole dominant factor' 过度声称 | in_progress | 'sole'→'primary' 全文替换进行中 |
| **R10-N1** | McNemar 'all p<0.01' false claim | in_progress | mega-patch 已修正为完整 p-value 表，reframe 为 classifier-robust |

### Warning

| ID | Summary | Status | 关键进展 |
|---|---|---|---|
| **R10-N2** | 仅 3 domains 不足 | in_progress | Code domain 已加入为第 4 域；Qwen-1.5B K\*=2, Pythia-1.4B K\*=1 完成；LLaMA-8B/Mistral-7B/Qwen-7B RUNNING |
| **R8-W1** | DPI 论证跳跃 | in_progress | regularity conditions 限定已入稿 (done)，待确认是否 close |
| **R8-W2** | Qwen 5/9 聚合偏向 | in_progress | family-level reporting 已入稿 (done)，待确认是否 close |
| **R8-W3** | 下游 filtering 生态效度有限 | in_progress | TTR/vocab entropy 表已入稿 (done)，待确认是否 close |
| **R8-W4** | Cross-model transfer 仅覆盖 4/9 | **open** | 无进展，需补充 Qwen-7B/LLaMA-8B transfer 数据 |
| **R8-W5** | Cross-scorer 'largely robust' 措辞 | in_progress | McNemar 修正完成 (done)，待确认是否 close |
| **R8-W6** | 'One-wash laundering' 歧义 | in_progress | Abstract 精确化完成 (done)，待确认是否 close |
| **R8-W7** | arXiv K\*=3 cross-scorer CI 不足 | in_progress | '20/22 configurations' 精确表述完成 (done)，待确认是否 close |

### Info

| ID | Summary | Status | 关键进展 |
|---|---|---|---|
| **R8-M1** | Eq.1 point-estimate vs CI 不一致 | **open** | 无进展 |
| **R8-M2** | Missing references | in_progress | LightGBM 已加；Related Work 扩展中 (37→45+) |
| **R8-M3** | -ing phrases 残留 | in_progress | mega-patch 已批量改写 (done)，待确认 |
| **R8-M4** | Abstract 术语精确化 | in_progress | mega-patch 处理中 |

---

**需关注**：R8-W1/W2/W3/W5/W6/W7/M3 的 action_items 均已标 done，但 issue status 仍为 in_progress。如果 Round 11 review 未再提及，可批量 close。R8-W4 和 R8-M1 是仅有的两个 **open** 且无进展的条目。

---
