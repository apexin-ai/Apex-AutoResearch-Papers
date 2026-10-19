# infra gpu cpu status check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-cpu-status-check_20260522T133230_result.json`
- **Structured JSON:** [`7248e733bbc74240595a.json`](../../sessions/72/7248e733bbc74240595a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU Status:
- cuda:0: 占用 16.4/97.9 GB | Qwen Steering L23 (PID 485325, 33min) — alpha=-5 进行中
- cuda:1: 占用 14.9/97.9 GB | Llama DE activations (PID 488140, ~1min) — 模型加载中
- cuda:2: 空闲 (3 MiB)
- cuda:3: 空闲 (3 MiB)

CPU Tasks:
- Gemma probe n=2000: 运行中 (PID 476334, 2h48m) — 1736/2000，输出文件尚未生成
- C3 MLP bootstrap Llama: 运行中 (PID 467708, 4h58m) — condition 2/6 (L5), 150/1000。condition 1 (L18) 已完成: delta=+0.0521 [-0.0221,+0.1287] excludes_zero=False
- Bootstrap n=2000 Llama: 输出文件不存在，无活跃进程（可能未启动或已合并到 Gemma 进程）
- Bootstrap n=2000 Qwen: 已完成，输出文件 22KB (May 22 21:08)
- Layer-wise extraction: 无活跃进程

Disk:
- /root: 24G/30G (79%) ⚠️ 偏高
- /root/autodl-tmp: 43G/250G (18%)
```

---
