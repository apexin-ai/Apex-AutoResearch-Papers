# data collect datasets

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_collect_datasets_20260517T054341_result.json`
- **Structured JSON:** [`35cc4a02ea68d6f78d70.json`](../../sessions/35/35cc4a02ea68d6f78d70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。最终结果：

**产出文件：**
- `artifacts/data/processed/conversations.jsonl` — 3.7MB, 500 条对话

**统计：**

| 指标 | 值 |
|------|-----|
| 总对话数 | 500 |
| jailbreak | 250 (50%) |
| benign | 250 (50%) |
| 平均 turns | 15.1 |
| 中位数 turns | 12.0 |
| 范围 | 10–72 |

**各来源贡献：**
- `tom-gibbs`: 115 条 jailbreak（完整对话含真实 assistant 回复，cipher-based 多轮攻击）
- `safemtdata`: 135 条 jailbreak（ActorAttack 方法的多轮渐进式攻击，user-turn 序列）
- `wildchat`: 250 条 benign（WildChat-1M 中 topic-drift 最高的 top-10%，作为困难负样本）

**无法获取的数据集：**
- ScaleAI/mhj — gated（需申请）
- MultiBreak — 论文已发但无公开数据
- XGuard-Train、SoftAge — gated

---
