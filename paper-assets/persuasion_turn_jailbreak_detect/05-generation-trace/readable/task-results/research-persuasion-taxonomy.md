# research persuasion taxonomy

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_persuasion-taxonomy_20260517T060621_result.json`
- **Structured JSON:** [`d609badcdcf0d24ed68d.json`](../../sessions/d6/d609badcdcf0d24ed68d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

1. **`memory.md`** — 完整的 8-class Persuasion Strategy Taxonomy，包含每个类别的定义、jailbreak/benign 示例、边界判断规则、标注指南（优先级规则+特殊情况）、文献映射表。

2. **`artifacts/taxonomy/persuasion_taxonomy.json`** — 结构化 JSON schema，包含 `id/name/definition/examples/boundary_rules/theoretical_basis` 字段，可直接用于标注系统。

**8 类别总览**：

| ID | Name | 理论来源 |
|---|---|---|
| 0 | Rapport Building | Cialdini:Liking + PAP:Positive Emotional |
| 1 | Authority Appeal | Cialdini:Authority + PAP:Expert Endorsement |
| 2 | Emotional Manipulation | Cialdini:Scarcity + PAP:Threat/Negative Emotion |
| 3 | Logical Reframing | PAP:Logical Appeal + Evidence-based |
| 4 | Role Assignment | DAN/Impersonation family |
| 5 | Gradual Escalation | Crescendo + FITD + Cialdini:Commitment |
| 6 | Obfuscation | PAP:Linguistics-based + Encoding family |
| 7 | Direct Request | Baseline (neutral) |

设计确保：jailbreak 攻击中 0-6 类均有文献证据，benign 对话中 Direct Request 覆盖绝大多数 turns，类别间通过优先级规则消除重叠。

---
