# monitor home eval status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_home-eval-status_20260514T233820_result.json`
- **Structured JSON:** [`cb0ddecf8d187f29775a.json`](../../sessions/cb/cb0ddecf8d187f29775a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 实验状态报告

### 1. cls4b-v5-val5120-sweep-home

**Sweep 脚本已死。** 原因：ckpt-600 完成后，跑 ckpt-4000 时报 `python: command not found`（PATH 问题）。

**已有人手动重启 ckpt-4000 val@5120 评估**（PID 3186818），当前正在运行：
- 进度：448/9335 samples（~4.8%），刚开始不久

**val@5120 结果（已完成）**:

| Checkpoint | Accuracy | F1_macro | 备注 |
|-----------|----------|----------|------|
| ckpt-600 | **82.82%** | 79.81 | val@5120 ✅ 完成 |
| ckpt-4000 | 🔄 running | — | val@5120，PID 3186818 |
| ckpt-4200 | ❌ | — | 未跑 val@5120（已有 val@2048: 80.64%） |
| ckpt-4400 | ❌ | — | 未跑 val@5120（已有 val@2048: 82.11%） |
| ckpt-4600 | ❌ | — | 未跑 val@5120（已有 val@2048: 82.35%） |

**注意**：ckpt-4200/4400/4600 目前只有 `max_seq_length=2048` 的结果，不是 val@5120。Sweep 脚本死后这三个还没跑到。

### 2. cls4b-v5-ckpt600-val5120-eval (PID 3179262)

**已完成** ✅ — 就是 sweep 的第一步，结果已写入 `results/repo_cls_v5_ckpt600_val5120/eval_repo_cls.json`。

- Accuracy: **82.82%**
- F1_macro: 79.81
- F1_fail: 72.03 / F1_pass: 87.60
- Recall_fail: 91.7% / Precision_fail: 59.3%
- n_instances: 9335, n_truncated: 234

### 3. GPU 状态

| GPU | 型号 | 显存 | 占用 | Util |
|-----|------|------|------|------|
| 0 | RTX 5090 | 31727/32607 MiB | 97% | 100% |

当前唯一 GPU 进程：PID 3186818 (ckpt-4000 val@5120 评估)

### 关键路径

- `results/v5_val5120_sweep.log` — sweep 控制日志
- `results/repo_cls_v5_ckpt600_val5120/eval_repo_cls.json` — ckpt-600 结果
- `results/repo_cls_v5_ckpt4000_val5120/` — ckpt-4000 进行中
- tmux session: `eval_8b_val5120_fix`（另一个 8B 实验的 session）

### 待处理

ckpt-4000 完成后（预计 ~1 小时，按 9335 samples 线性估算），还需手动启动 ckpt-4200/4400/4600 的 val@5120 评估。

---
