# code toxicchat path verify

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_toxicchat-path-verify_20260520T011525_result.json`
- **Structured JSON:** [`d63ab1d1d47c10f9f9c1.json`](../../sessions/d6/d63ab1d1d47c10f9f9c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清楚：

## 汇报

**文件对比：**

| 文件 | 行数 | jailbreak | benign | 平衡度 |
|------|------|-----------|--------|--------|
| `toxicchat_eval.jsonl` | 408 | 204 | 204 | 50/50 ✓ |
| `toxicchat_plan002_eval.jsonl` | 242 | 204 | 38 | 84/16 ✗ |
| `toxicchat_balanced.jsonl` | **不存在** | — | — | — |

**路径使用：**
- exp8（原始实验）→ `data/mhj/toxicchat_eval.jsonl`（408条，平衡）
- exp16/exp17 → `data/mhj/toxicchat_plan002_eval.jsonl`（242条，不平衡）

**但切换路径并不能解决问题。** 9class_seed42 在两个文件上都很差：

| 数据集 | F1 | Pred分布 | True分布 |
|--------|-----|----------|----------|
| plan002 (242) | **0.3099** | 37jb+205bn | 204jb+38bn |
| balanced (408) | **0.3353** | 133jb+275bn | 204jb+204bn |

模型在 ToxicChat 上严重偏向预测 benign——204 个真实 jailbreak 中，plan002 上只识别出 37 个，balanced 上只识别出 133 个。**数据路径差异不是根因，模型本身在 ToxicChat 分布上就表现很差。**

可能的深层原因：ToxicChat 的 human jailbreak 模式与训练数据中的 LLM-generated 攻击差异太大，模型无法泛化。

---
