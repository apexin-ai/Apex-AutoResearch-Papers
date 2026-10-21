# check orphaned eval home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_orphaned-eval-home_20260514T230201_result.json`
- **Structured JSON:** [`13ca45036006b8418dfd.json`](../../sessions/13/13ca45036006b8418dfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

val 集共 9784 条，已处理 5056 条（51.7%）。以下是完整报告：

---

## 状态报告

### cuda:0
GPU 满载：100% utilization, 31727/32607 MiB

### cls4b-v5-ckpt600-val5120-eval (PID 3179262)
- **状态**: 运行中（started 15:24:23）
- **进度**: 5056 / 9784 = **51.7%**
- 输出目录 `repo_cls_v5_ckpt600_val5120/` 已有 predictions.jsonl，但尚未生成 eval_repo_cls.json

### cls4b-v5-val5120-sweep-home (PID 3180425)
- **状态**: 运行中，但在 **sleep 30 循环中等待 ckpt-600 eval 完成**
- **进度**: 0/4 checkpoints started（等待解锁）
- 计划执行: ckpt-4000 → 4200 → 4400 → 4600（val@5120）
- 脚本会跳过已有结果的 checkpoint

### 已有 v5 结果（max_seq_length=2048，非 val5120）

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | gap_vs_majority |
|------------|----------|----------|---------|---------|-----------------|
| ckpt-600   | 76.74    | 73.74    | 64.88   | 82.61   | +3.78pp         |
| ckpt-4000  | 81.51    | 72.56    | 56.90   | 88.23   | +8.55pp         |
| ckpt-4200  | 80.64    | 72.10    | 56.66   | 87.54   | +7.69pp         |
| ckpt-4400  | 82.11    | 73.94    | 59.34   | 88.54   | +9.16pp         |
| **ckpt-4600** | **82.35** | **74.74** | **60.87** | **88.60** | **+9.39pp** |

ckpt-4600 在 seq_len=2048 下表现最好。val5120 的 ckpt-600 大约还需等 ~38 分钟完成，之后 sweep 会依次跑 4 个 checkpoint。

---
