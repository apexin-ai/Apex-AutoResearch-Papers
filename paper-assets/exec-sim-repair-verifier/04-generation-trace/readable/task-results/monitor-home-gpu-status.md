# monitor home gpu status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_home-gpu-status_20260515T012412_result.json`
- **Structured JSON:** [`c6c3f830d88d53f59265.json`](../../sessions/c6/c6c3f830d88d53f59265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## home-1x5090 状态汇报

### GPU
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| cuda:0 | RTX 5090 | 100% | 31727/32607 MiB |

### 当前任务
- **PID 3193462** — `ckpt-4400 val@5120` eval，已运行 38 分钟
- 预测已全部完成（5120/5120 行），进程仍在运行（可能在计算最终指标或写 json）

### v5 Sweep 已完成结果

**@2048 seq_length（test set, n=9784）：**

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass |
|-----------|----------|----------|---------|---------|
| ckpt-600  | 76.74 | 73.74 | 64.88 | 82.61 |
| ckpt-4000 | 81.51 | 72.56 | 56.90 | 88.23 |
| ckpt-4200 | 80.64 | 72.10 | 56.66 | 87.54 |
| ckpt-4400 | 82.11 | 73.94 | 59.34 | 88.54 |
| ckpt-4600 | **82.35** | **74.74** | **60.87** | **88.60** |

**@5120 seq_length（val set, n=9335）：**

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass |
|-----------|----------|----------|---------|---------|
| ckpt-600  | 82.82 | 79.81 | 72.03 | 87.60 |
| ckpt-4000 | **89.84** | **84.25** | 74.85 | **93.64** |
| ckpt-4400 | 运行中... | — | — | — |

### 关键观察
1. **val@5120 大幅优于 @2048**：ckpt-4000 从 81.51→89.84 acc, 72.56→84.25 F1_macro（+12pp）
2. **@2048 上 ckpt-4600 最优**，但差距不大（ckpt-4400 vs 4600: 73.94→74.74 F1_macro）
3. **val@5120 缺失**：ckpt-4200、ckpt-4600 的 val@5120 eval 尚未执行
4. **Sweep 脚本中断**：`v5_val5120_sweep.sh` 在 ckpt-4000 步失败（`python: command not found`），后续 eval 需手动启动

### 可用 Checkpoints
`checkpoint-600, checkpoint-4000, checkpoint-4200, checkpoint-4400, checkpoint-4600`

### 下一步
ckpt-4400 @val5120 即将完成。之后还需跑 ckpt-4200 和 ckpt-4600 的 val@5120 eval 才能完成完整 sweep。

---
