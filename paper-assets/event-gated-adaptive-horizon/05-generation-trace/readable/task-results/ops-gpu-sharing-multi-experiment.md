# ops gpu sharing multi experiment

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-sharing-multi-experiment_20260518T160127_result.json`
- **Structured JSON:** [`3adeda51e0b41eb10c0d.json`](../../sessions/3a/3adeda51e0b41eb10c0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

VRAM 稳定，远低于安全阈值。

## 汇报

### VRAM 占用

| GPU | 提交前 | 提交后 | 总量 | 占比 |
|-----|--------|--------|------|------|
| 0 | 5,217 MiB | 7,866 MiB | 97,887 MiB | 8.0% |
| 1 | 4,167 MiB | 6,816 MiB | 97,887 MiB | 7.0% |

### 启动的额外实验（4 个）

| 实验 ID | GPU | 任务 | PID | 配置要点 |
|---------|-----|------|-----|----------|
| exp_023_cheetah_baseline_s2 | cuda:0 | Cheetah Run baseline s2 | 753791 | vanilla DreamerV3, 200K steps |
| exp_008f_s2 | cuda:0 | Walker no-dt-emb s2 | 754068 | gate+no_dt_embed+H8, 105K steps |
| exp_001_baseline_s2 | cuda:1 | Walker baseline s2 | 754357 | vanilla DreamerV3, 105K steps |
| exp_009c_s2 | cuda:1 | Walker no-dt-emb H8 s2 | 754644 | gate+no_dt_embed+H8, 105K steps |

### 每张卡进程数

| GPU | 原有进程 | 新增进程 | 总计 |
|-----|----------|----------|------|
| 0 | 1 (cheetah_unexposed_s0) | 2 (023_s2, 008f_s2) | 3 |
| 1 | 1 (cheetah_unexposed_s1) | 2 (001_s2, 009c_s2) | 3 |

---
