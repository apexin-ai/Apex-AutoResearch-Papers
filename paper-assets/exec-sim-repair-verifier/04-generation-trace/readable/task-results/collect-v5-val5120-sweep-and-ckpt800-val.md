# collect v5 val5120 sweep and ckpt800 val

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_v5-val5120-sweep-and-ckpt800-val_20260514T233653_result.json`
- **Structured JSON:** [`95c28de6cfab874091cd.json`](../../sessions/95/95c28de6cfab874091cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: Home — 4B v5 val@5120 sweep

**Sweep 状态：失败。** 只完成了 ckpt-600。脚本在启动 ckpt-4000 时崩溃：
```
run_v5_val5120_sweep.sh: line 20: python: command not found
```

**已完成的 val@5120 结果（仅 ckpt-600）：**

| Checkpoint | Accuracy | F1 macro | F1 fail | F1 pass | Prec fail | Recall fail | Unparseable | Total |
|---|---|---|---|---|---|---|---|---|
| **600** | 82.82 | 79.81 | 72.03 | 87.60 | 59.30 | **91.70** | 0 | 9335 |

**ckpt-4000/4200/4400/4600 仅有 val@2048 结果**（不是你要求的 val@5120）：

| Checkpoint | Accuracy | F1 macro | F1 fail | F1 pass | Unparseable | Total | seq_len |
|---|---|---|---|---|---|---|---|
| 4000 | 81.51 | 72.56 | 56.90 | 88.23 | 132 | 9784 | 2048 |
| 4200 | 80.64 | 72.10 | 56.66 | 87.54 | 132 | 9784 | 2048 |
| 4400 | 82.11 | 73.94 | 59.34 | 88.54 | 132 | 9784 | 2048 |
| 4600 | 82.35 | 74.74 | 60.87 | 88.60 | 132 | 9784 | 2048 |

ckpt-4000 val@5120 仅完成 336/9335 条预测就中断了。

---

### Part 2: Westd — 8B s42 ckpt-800 val@8192

**结果：不存在。** 没有找到任何 ckpt-800 val@8192 相关的日志或结果目录。Westd 上只有以下 8192 相关 log：
- `cls8b-s42-ckpt400-test8192-eval.log`
- `cls8b-s42-ckpt600-test8192-eval.log`
- `cls8b-s42-ckpt200-val8192-eval-v2.log`
- `cls8b-seed123-ckpt3000-val8192-eval.log`

ckpt-800 val@8192 eval 似乎从未启动。

---

### 需要修复

1. **Home sweep 修复**：脚本里用了 `python` 而非 `python3`（或需要 activate venv）。修好后重跑 ckpt-4000/4200/4400/4600 的 val@5120。
2. **Westd ckpt-800 val@8192**：需要手动启动这个 eval。

要我修复 sweep 脚本并重新启动两边的 eval 吗？

---
