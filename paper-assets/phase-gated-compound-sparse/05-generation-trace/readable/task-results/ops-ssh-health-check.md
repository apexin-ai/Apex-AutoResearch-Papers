# ops ssh health check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ssh-health-check_20260514T162709_result.json`
- **Structured JSON:** [`4f5b9e63c0d0c27ee592.json`](../../sessions/4f/4f5b9e63c0d0c27ee592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU 使用情况

| GPU | VRAM | 占比 | 利用率 | 进程 |
|-----|------|------|--------|------|
| 0 | 30071 / 97887 MiB | 31% | 79% | c2_n500_deepseek imp (PID 130124) |
| 1 | 33919 / 97887 MiB | 35% | 78% | c2_n500_deepseek rand (PID 130263) |
| 2 | 53054 / 97887 MiB | 54% | 89% | c2_qw_n500 imp (131864, 30752M) + c3_llama imp (146382, 22288M) |
| 3 | 53824 / 97887 MiB | 55% | 89% | c2_qw_n500 rand (132002, 31364M) + c3_llama rand (146132, 22446M) |

### 重复进程
PID 132389、132392 **已死**。

### 各实验进度

| 实验 | GPU | Condition | 进度 | 状态 |
|------|-----|-----------|------|------|
| c2_n500_deepseek | 0 | imp s=0.15 | **300/500** (60%) | 正常 |
| c2_n500_deepseek | 1 | rand s=0.15 | **319/500** (64%) | 正常 |
| c2_qw_n500 | 2 | imp s=0.15 | **235/500** (47%) | 正常 |
| c2_qw_n500 | 3 | rand s=0.15 | **240/500** (48%) | 正常 |
| c3_llama | 2 | imp s=0.25 | **13/50** (26%) | 正常 |
| c3_llama | 3 | rand s=0.25 | **15/50** (30%) | 正常 |

c3_llama 已完成 s=0.15 和 s=0.20，当前在跑 s=0.25（最后一个 condition）。

### GPU 2+3 共享情况
c2_qw_n500 和 c3_llama **确实同时跑在 GPU 2/3 上**，但 96GB 显存充裕（54-55% 占用），**无 OOM 风险**。利用率 89% 比 GPU 0/1 的 78-79% 高，说明两个实验在共享计算资源，但运行正常无干扰。

### 磁盘
`/root/autodl-tmp`: 84G / 250G，剩余 167G (66%)。

### 异常
无。所有 6 个实验进程均正常运行。

---
