# ssh urgent full status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_full_status_check_20260521T224150_result.json`
- **Structured JSON:** [`2158225d1d36940fbe86.json`](../../sessions/21/2158225d1d36940fbe86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 1: GPU 实际状态

### autodl-5090
| GPU | utilization | memory_used/total | 进程 |
|-----|------------|-------------------|------|
| 0 | 84% | 30186/32607 MiB | **mf4v2_s42_v3** (run_mvp_pilot.py, seed 42, fewnerd, exp021-merged) |
| 1 | 0% | 2/32607 MiB | 空闲 |
| 2 | 0% | 2/32607 MiB | 空闲 |
| 3 | 0% | 2/32607 MiB | 空闲 |

### autodl-5090-c
| GPU | utilization | memory_used/total | 进程 |
|-----|------------|-------------------|------|
| 0 | 85% | 30263/32607 MiB | **mf4v2_s42_v4** (run_mvp_pilot.py, seed 42, fewnerd, exp021-merged) |
| 1 | 0% | 0/32607 MiB | 空闲 |
| 2 | 0% | 0/32607 MiB | 空闲 |
| 3 | 84% | 30889/32607 MiB | **pretrained_s42_v2** (run_mvp_pilot.py, seed 42, fewnerd, Qwen2.5-7B-Instruct pretrained) |

## Step 2: 5-epoch 持久化

| seed | output/ | artifacts/ |
|------|---------|------------|
| s42 | ✓ (902B, May 22 06:01) | ✓ (902B, May 22 06:07) |
| s123 | ✓ (905B, May 22 06:01) | ✓ (905B, May 22 06:07) |
| s456 | ✓ (904B, May 22 05:20, 5090-c) | ✓ **已创建**（刚从 output/ 复制） |

## Step 3: mf4v2_s42

| 实验 | 服务器 | 状态 | 进度 | ETA |
|------|--------|------|------|-----|
| **v3** | 5090 GPU:0 | **running** | 78% (234456/301184) | ~25 min |
| **v4** | 5090-c GPU:0 | **running** | 32% (96016/301184) | ~1h13min |
| **pretrained_s42_v2** | 5090-c GPU:3 | **running** | 53% (19843/37648) | ~15 min |

注：v3/v4 的 output 目录目前为空（samples.jsonl 尚未写入），数据在推理完成后才落盘。pretrained_s42_v2 使用原始 Qwen2.5-7B-Instruct，速度较慢（~17 it/s vs mf4v2 的 ~50 it/s），因为是非 fine-tuned 模型生成更长输出。

---
