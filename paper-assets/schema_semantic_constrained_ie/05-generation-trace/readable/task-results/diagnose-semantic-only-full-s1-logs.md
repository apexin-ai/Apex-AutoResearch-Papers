# diagnose semantic only full s1 logs

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_semantic_only_full_s1_logs_20260513T235021_result.json`
- **Structured JSON:** [`d0748ea90175c3cbf39e.json`](../../sessions/d0/d0748ea90175c3cbf39e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 日志实际内容 — 没有 EXIT_CODE=127

两个日志各 12 行，内容几乎一样，都**成功启动**了：

```
/root/miniconda3/bin/python3
`torch_dtype` is deprecated! Use `dtype` instead!
Mode: semantic_only  (或 full_s1)
Dataset: scierc
Model: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B
Device: cuda:0
Samples: 551
Entity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']
Relation types: 7
Loading model...
Loading checkpoint shards: 100%|██████████| 5/5
The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k'].
```

**结论：不存在 python3 not found 问题，conda 环境正常激活，实验正在运行。**

### 2. 严重问题：每个实验有重复进程

`ps aux` 显示每个实验跑了**两个 python3 进程**，都写同一个输出文件：

| 实验 | tmux 内进程 (PID) | nohup 后台进程 (PID) | 输出文件 |
|------|---------|---------|----------|
| semantic_only | 134207 (GPU 0) | 134450 (GPU 1) | `outputs/phase2_scierc_semantic_only.jsonl` |
| full_s1 | 134598 (GPU 1) | 134886 (GPU 1) | `outputs/phase2_scierc_full_s1.jsonl` |

**两个进程同时写一个 JSONL 文件，会导致数据交错/损坏。**

### 3. 当前输出进度

- `phase2_scierc_semantic_only.jsonl`: 16 行 (34KB) — 进行中
- `phase2_scierc_full_s1.jsonl`: 10 行 (21KB) — 进行中
- `phase2_scierc_grammar_only.jsonl`: 551 行 — **已完成**
- `phase2_scierc_unconstrained.jsonl`: 551 行 — **已完成**

### 4. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | 41788/97887 MiB | 93% |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 49375/97887 MiB | 91% |

GPU 1 上跑了 3 个推理进程（full_s1 tmux + full_s1 nohup + semantic_only nohup），负载偏高。

### 建议操作

需要立刻 kill 掉重复的 nohup 后台进程（PID 134450 和 134886），只保留 tmux 内的进程，然后检查已写入的输出文件是否有重复行需要清理。是否执行？

---
