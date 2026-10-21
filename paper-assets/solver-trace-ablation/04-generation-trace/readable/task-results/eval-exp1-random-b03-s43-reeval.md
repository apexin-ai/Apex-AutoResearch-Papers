# eval exp1 random b03 s43 reeval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp1-random-b03-s43-reeval_20260515T023248_result.json`
- **Structured JSON:** [`71149824cc11e941a8b0.json`](../../sessions/71/71149824cc11e941a8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checkpoint 不存在。停止任务，报告情况。

**结果：exp1-random-b03-s43 checkpoint 已丢失，无法 re-eval**

确认情况：
- `/root/autodl-tmp/outputs/exp1_random_b03_s43/` — 不存在
- `/root/autodl-tmp/outputs/exp1_random_b03_s43_eval/` — 空目录
- `/root/autodl-tmp/outputs/exp1_random_b03_s43_r2/` — 仅含 reward_log.jsonl（2208 字节），无 checkpoint-*
- `find -name checkpoint-*` 全局扫描确认无 `exp1_random_b03_s43` 任何变体的 checkpoint

现存 checkpoint 仅有：
- `exp1_isr_b03_s44_r2/checkpoint-500`
- `exp1_random_b03_s44/checkpoint-100`
- `exp1_random_b03_s44_r2/checkpoint-500`
- `exp1_isr_b03_s43_r3/checkpoint-500`

这符合 C010/C011 中提到的 disk-cleanup-v2 误删 exp1_random_b03_s43 checkpoint 的事故。任务前提（"EXIT_CODE=129 可能已丢失"）已确认成立。

**未执行**：eval、registry 更新、artifact 注册。是否重训由 Main Agent 决策。

---
