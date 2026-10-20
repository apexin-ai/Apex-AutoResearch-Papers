# data plan001 quality fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_plan001-quality-fix_20260517T170413_result.json`
- **Structured JSON:** [`660cf2d2b76bdd0b2b70.json`](../../sessions/66/660cf2d2b76bdd0b2b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Plan 001 结果报告

### Step A: 策略标签修复 ✅
- benign → `persuasion_strategy=0` (none)
- jailbreak → `persuasion_strategy=1-8` (原 0-7 右移+1)
- 模型 `num_persuasion_classes` 更新为 9

### Step B: Register 归一化 ✅
- Qwen3-8B 对 250 个 jailbreak 对话的 2068 个 user turn 做了 casual register paraphrase
- 成功率: 2068/2068 (100%), 0 失败
- 输出: `data/generated/crescendo_normalized.jsonl`

### Step C: TF-IDF Hard Gate ❌ FAIL
| 指标 | 值 |
|---|---|
| 5-Fold CV F1 | **1.0000 ± 0.0000** |
| Hard Gate (F1 < 0.75) | **FAIL** |

**结论**: Register 归一化未能消除 TF-IDF 可利用的文本表面特征差异。jailbreak 数据即使经过 casual register paraphrase，仍然与 benign 数据在词频分布上完全可分。

**根因分析**: 差异不仅是 register (正式 vs 口语)，更核心的是 **话题/意图层面的词汇差异**:
- Benign 对话围绕日常生活问题 ("like", "guess", "huh", "was wondering")
- Jailbreak 对话围绕请求/说服目标 ("could", "help", "without", "if we")

单纯的 register normalization 无法消除意图层面的词汇差异。需要更根本的数据重构或对抗性数据增强策略。

---
