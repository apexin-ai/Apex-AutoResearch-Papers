# fix 8b oom and dual submit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_8b-oom-and-dual-submit_20260516T094246_result.json`
- **Structured JSON:** [`f1f9b5a0fa8660c4fa8c.json`](../../sessions/f1/f1f9b5a0fa8660c4fa8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡启动成功，无 OOM。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| Config 修改 | ✅ 两文件均为 `batch_size: 1`, `grad_accum: 8` |
| GPU 0 (exec-only) | ✅ 49767/97887 MiB, 97% util, training step 0/500 |
| GPU 1 (ISR β=0.1) | ✅ 49767/97887 MiB, 94% util, training step 0/500 |
| OOM | 无，~51% 显存占用，余量充足 |

两个 tmux session 均在正常训练中：
- `w2-qwen3-8b-exec-pilot` → cuda:0, mode=execution_only
- `w2-qwen3-8b-isr-pilot` → cuda:1, mode=additive_bonus

---
