# code exp17 progress check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp17-progress-check_20260519T200914_result.json`
- **Structured JSON:** [`7b1b2123e00279008b32.json`](../../sessions/7b/7b1b2123e00279008b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp17 数据生成:
- jailbreak: 222/250 (进程状态: running, ETA ~35 min)
- benign:   171/250 (进程状态: running, ETA ~129 min)

exp16 训练:
- exp16_vanilla_train tmux: alive
- exp16_9class_train tmux: alive
- GPU 0: 0%, 3 MiB / 97887 MiB (空闲)
- GPU 1: 0%, 3 MiB / 97887 MiB (空闲)
- GPU 2: 88%, 19013 MiB (exp17 jailbreak 生成)
- GPU 3: 84%, 19011 MiB (exp17 benign 生成)
```

exp16 两个训练 tmux session 存活但 GPU 0-1 空闲，说明 exp16 训练可能已完成或在等待状态——需要查 log 确认的话告诉我。

---
