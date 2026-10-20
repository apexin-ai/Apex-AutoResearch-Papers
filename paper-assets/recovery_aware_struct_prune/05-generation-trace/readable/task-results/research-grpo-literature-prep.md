# research grpo literature prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo-literature-prep_20260515T135644_result.json`
- **Structured JSON:** [`2f415e729909cfc44dc1.json`](../../sessions/2f/2f415e729909cfc44dc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新。以下是本次调研总结：

## 新增论文 (7 篇)

### Direction 1: Structured Pruning + RLVR Recovery
| 论文 | 年份/Venue | 关系 | 优先级 |
|------|-----------|------|--------|
| **RLRC** (Chen & Li) | 2025, arXiv | RL recovery 扩展到 VLA 机器人领域，验证 RL recovery 的跨模态泛化性 | should-cite |
| **NIRVANA** (Ai et al.) | 2025, arXiv | NTK-based saliency + adaptive sparsity，强 pruning baseline | should-cite |
| **A Free Lunch in LLM Compression** (Wagner et al.) | 2025, arXiv | 局部重建匹配 PEFT，但 SFT 有天花板——我们的 RLVR 突破该天花板 | should-cite |

### Direction 2: CKA Justification
| 论文 | 年份/Venue | 关系 | 优先级 |
|------|-----------|------|--------|
| **Reliability of CKA** (Davari et al.) | 2023, ICLR | CKA 对 outlier/变换敏感，**必须引用并在 paper 中回应**（我们是 intra-model 比较，受影响较小） | **must-cite** |
| **Debiasing CKA** (Murphy et al.) | 2024, ICLR Workshop | feature-sample ratio 偏差，我们的设置影响较小 | nice-to-have |
| **TraceNAS** (Malettira et al.) | 2026, arXiv | 梯度 trace 做 NAS-style 剪枝，CKA 的替代信号 | should-cite |

### Direction 3: FANG / FuncNet (已确认)
- **FANG** — Yu et al., arXiv Dec 2025 (2512.23014)，activation-based FFN neuron分组，**must-cite**
- **FuncNet** — Liu et al., arXiv Aug 2025 (2508.05239)，ICA-based functional network，**must-cite**
- **FNF** — arXiv Jan 2026 (2601.22692)，functional network fingerprint，nice-to-have

### Direction 4: GraSP Baselines
- **GraSP 原始** (Wang et al., ICLR 2020, 2002.07376) — 已补充，should-cite
- **GRASPrune** (ACL 2026) — 已有，must-cite
- **TraceNAS** — 梯度 trace correlation 扩展了 GraSP 思路

## 关键更新
- Self-Healing 完整作者：**Ji et al.**, ICLR 2026 submission
- From LLMs to LRMs: **Ding et al.**, arxiv_id=2601.18091
- 所有 entry 新增 `citation_priority` 字段
- 全文件共 **must-cite: 12 篇**, should-cite: 15 篇, nice-to-have: 14 篇

---
