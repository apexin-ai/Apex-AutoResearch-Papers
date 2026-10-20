# check exp progress urgent

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_progress_urgent_20260516T215633_result.json`
- **Structured JSON:** [`d8f3e6c81763a2a1e249.json`](../../sessions/d8/d8f3e6c81763a2a1e249.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### exp_001 (125M) — Metrics 表格 (Gen 0-3 完成)

| Gen | eff_rank | log_det | ppl | distinct4 | hellaswag (acc_norm) | train_loss |
|-----|----------|---------|------|-----------|---------------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | 0.4130 | — |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 0.3897 | 1.6228 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 0.3764 | 1.2682 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 0.3658 | 1.1340 |

**趋势**: ppl 持续上升 (9.55→16.25), distinct4 持续下降 (0.74→0.49), hellaswag 持续下降 (0.413→0.366)。eff_rank 在 Gen 1 跳升后趋于平稳 (~491-496), Gen 3 略降。log_det 在 Gen 1-2 上升后 Gen 3 回落。collapse 信号明确。

---

### exp_002 (1B) — Metrics 表格 (Gen 0-1 完成)

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss |
|-----|----------|---------|------|-----------|------------|
| 0 | 516.14 | 2835.32 | 8.07 | 0.7510 | — |
| 1 | 570.75 | 2905.74 | 9.41 | 0.6335 | 1.5295 |

---

### 当前进度

- **exp_001**: Gen 4 数据生成中，进度 5760/50000 (~11.5%)。日志仍在活跃写入 (最后修改 05:57)。注意 exp_001.log 末尾有 EXIT_CODE=124 (可能是旧 wrapper 超时，但 resume_run.log 仍活跃)。
- **exp_002**: Gen 1 完成，当前大概率在 Gen 2 训练阶段。GPU 1 满载 100%，日志最后修改 05:33 (训练期间无日志输出属正常)。

### GPU 状态

| GPU | Utilization | Memory Used | Memory Total |
|-----|-------------|-------------|--------------|
| 0 | 70% | 65909 MiB | 97887 MiB |
| 1 | 100% | 39771 MiB | 97887 MiB |

### 磁盘状态

| Filesystem | Size | Used | Avail | Use% |
|------------|------|------|-------|------|
| / (overlay) | 30G | 25G | 5.1G | 84% |
| /root/autodl-tmp | 250G | 102G | 149G | 41% |

**注意**: 系统盘 84% 用量偏高，仅剩 5.1G。如果 Gen 4 训练需要在系统盘写临时文件可能有风险。

---
