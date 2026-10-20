# data wildchat deep clean

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_wildchat-deep-clean_20260517T081611_result.json`
- **Structured JSON:** [`1c41cbcd190218c07487.json`](../../sessions/1c/1c41cbcd190218c07487.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清洗完成。汇报：

---

**WildChat 深度清洗结果**

| 指标 | 数值 |
|------|------|
| 原 benign 数据 | 250 条 |
| 扩展关键词命中 | 24 条（3-tier 启发式） |
| GPT-5.5 判定 | API 403，已 fallback |
| 最终移除 | **24 条** |
| 剩余 benign | **226 条** |
| 总数据集 | **476 条** |

**移除分类：**
- Tier1（高置信 jailbreak 关键词：DAN/Developer Mode 等）：10 条
- AutoGPT/agent prompt injection：10 条
- Tier2+上下文（role assignment + safety context）：1 条
- Tier3+强上下文（"character" + ≥3 safety indicators）：3 条

**更新后 splits：**
- train: 336 (benign=160, cipher=81, persuasion=95)
- val: 70 (benign=33, cipher=17, persuasion=20)
- test: 70 (benign=33, cipher=17, persuasion=20)

**说明：** GPT-5.5 API 返回 403（余额耗尽），使用 3-tier 启发式替代：Tier1 自动移除，Tier2 需要 ≥2 个 jailbreak 上下文词共现，Tier3（"character"等高误杀词）需 ≥3 个上下文词。相比之前纯关键词扫描的 12 条，本次通过扩展 AutoGPT 模式检测和分层上下文判断，识别出了之前遗漏的 prompt injection 类攻击。

---
