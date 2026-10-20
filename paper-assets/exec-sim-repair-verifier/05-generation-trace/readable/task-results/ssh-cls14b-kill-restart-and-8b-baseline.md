# ssh cls14b kill restart and 8b baseline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cls14b-kill-restart-and-8b-baseline_20260522T213548_result.json`
- **Structured JSON:** [`d2db8eacb88e3bac765d.json`](../../sessions/d2/d2db8eacb88e3bac765d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认成功：

**Step 1 — Kill 旧进程**: PID 212100 已终止，tmux session `cls14b-func-s42` 已清理。

**Step 2 — CLS 14B v2 (GPU 0)**: PID 215642，已在运行。日志确认：
- `Train file: data/train.jsonl`, `Val file: data/val.jsonl` ✓
- **`Loaded train=15290, val=1896`** ✓ (正确的 ~15K function-level 数据，不是 70K)

**Step 3 — 8B baseline (GPU 1)**: 模型加载中，使用 `/root/autodl-tmp/models/Qwen/Qwen3-8B`，0-shot 先跑完后自动跑 3-shot。

**GPU 分配**:
| GPU | 任务 | PID |
|-----|------|-----|
| 0 | CLS 14B v2 (train, 15290 samples) | 215642 |
| 1 | 8B baseline 0-shot/3-shot (loading) | 加载中 |
| 2 | CWM 14B (已有) | 211098 |
| 3 | 空闲 | — |

GPU 1 的 8B 模型还在加载 checkpoint shards，尚未占 VRAM，正常现象。

---
