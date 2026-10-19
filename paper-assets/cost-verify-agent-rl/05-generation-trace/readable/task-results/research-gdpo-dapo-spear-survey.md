# research gdpo dapo spear survey

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gdpo-dapo-spear-survey_20260514T133417_result.json`
- **Structured JSON:** [`b505217bf7fde02c721e.json`](../../sessions/b5/b505217bf7fde02c721e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，memory.md 已更新。核心变更：

**新增 7 个方法**：Scaf-GRPO、AR3PO、POPO、GTPO、GSPO、PRIME、E2H Reasoner

**GDPO 重新评估**：从"不推荐"改为 Tier 2。我们确实有双 reward（success_reward + valid_action_bonus），GDPO 的独立归一化直接对抗 exp013f 的 reward gaming 根因。

**修订后推荐排序**：
| Tier | 方案 | 理由 |
|------|------|------|
| **T1 主线** | SPEAR | ALFWorld 直接验证，三痛点全覆盖 |
| **T1 主线** | DAPO + AR3PO | 稳定性 + response reuse 解决全失败 batch |
| **T2 最小代价** | Dr. GRPO | 2 行代码 ablation |
| **T2 最小代价** | GDPO | 双 reward 独立归一化，drop-in 替换 |
| **T3 补强** | GTPO / EPO | conflict token 过滤 / entropy smoothing |

**落地路径**：exp016 (Dr. GRPO + GDPO) → exp017 (DAPO + AR3PO) → exp018 (SPEAR)

---
