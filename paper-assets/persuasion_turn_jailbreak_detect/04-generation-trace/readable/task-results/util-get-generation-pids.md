# util get generation pids

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_util_get-generation-pids_20260519T061731_result.json`
- **Structured JSON:** [`eb860cfa070ba125155f.json`](../../sessions/eb/eb860cfa070ba125155f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程 PID：**
```
DD PID:     217077  (generate_dd_llama.py --count 50 --gpu 0)
AA PID:     217747  (generate_aa_llama.py --gpu 1 --num_per_goal 5)
Benign PID: 218417  (generate_benign_llama.py --count 50 --gpu 2)
```

**当前进度：**
三个 JSONL 文件均在写入中（in progress），尚未完成：

| 文件 | 大小 |
|------|------|
| dd_llama.jsonl | 225,619 bytes |
| aa_llama.jsonl | 227,383 bytes |
| benign_llama.jsonl | 230,913 bytes |

三个进程均已运行约 13-17 分钟，CPU 占用 123-125%，各占用约 2.6GB 内存，分别在 GPU 0/1/2 上执行。

---
