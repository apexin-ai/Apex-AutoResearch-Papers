# eval plan002 b01 s42 h8 reeval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-b01-s42-h8-reeval_20260515T124625_result.json`
- **Structured JSON:** [`3bc47108737ea68725d9.json`](../../sessions/3b/3bc47108737ea68725d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕。汇总如下：

---

## H8 Re-eval 结果报告

### plan002-additive-b01-s42（500步，β=0.1，seed=42）
- **Checkpoint**: `/root/autodl-tmp/outputs/plan002_additive_b01_s42/` **已删除**
- **Eval 结果文件**: 已删除
- **Registry 现状**: genuine_count=26, h7_count=13, **无 h8 字段**
- **H8 retroactive audit 记录**: "checkpoint and eval file deleted; cannot re-classify"
- **结论: 无法 re-eval，需要重训**

### plan002-additive-b01-s43（500步，β=0.1，seed=43）
- **Checkpoint**: `/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500/` **已删除**
- **Eval 结果文件**: 从未通过 eval_sta.py 标准流程生成（原始分类是 inline 手动分析）
- **Registry 现状**: genuine_count=2, h7_count=59, **无 h8 字段**
- **结论: 无法 re-eval，需要重训**

### plan002-additive-b01-s44（500步，β=0.1，seed=44）
- **Checkpoint**: `/root/autodl-tmp/outputs/plan002_additive_b01_s44/` **已删除**
- **Eval 结果文件**: 同 s43，从未通过标准流程生成
- **Registry 现状**: genuine_count=12, h7_count=77, **无 h8 字段**
- **结论: 无法 re-eval，需要重训**

---

### 已有 H8 审计的 plan002 实验（无需操作）
| exp_id | h8_count | genuine (旧→新) | 备注 |
|--------|----------|-----------------|------|
| plan002-additive-b01-s42-1000 | 1 | 3→2 | 已审计 |
| plan002-additive-b03-s42 | 3 | 4→1 | 已审计 |

### 总结
三个 500 步 plan002-b01 实验（s42/s43/s44）的 checkpoint 和 eval 文件均已被清理，H8 re-eval 无法执行。需要重训才能完成 H8 审计。GPU 当前两块都空闲（0 MiB 使用），如需重训可立即启动。

---
