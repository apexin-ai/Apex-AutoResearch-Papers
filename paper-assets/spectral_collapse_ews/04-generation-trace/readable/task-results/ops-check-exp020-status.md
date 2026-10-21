# ops check exp020 status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp020-status_20260524T073011_result.json`
- **Structured JSON:** [`6eb23c5853dc18dbacda.json`](../../sessions/6e/6eb23c5853dc18dbacda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Exp_020 状态: **RUNNING** — 正在执行最后一代 (Gen 9)

**进程**: PID 783957, 自 May 23 启动, CPU 100%
**当前阶段**: Gen 9 合成数据生成中, 37760/50000 samples (75.5%)
- 生成完毕后还需 training + evaluating, 预计 **1-2 小时**内完成全部 10 代

**磁盘**: `/root/autodl-tmp/` 130G 可用 (49%), 充足

### 已完成 Gen 0-8 Metrics

| Gen | eff_rank | log_det (SLV) | PPL | D-4 | σ₁ |
|-----|----------|---------------|------|-------|------|
| 0 | 23.09 | 689.44 | 15.45 | 0.913 | 6598 |
| 1 | 155.22 | 885.30 | 16.42 | 0.891 | 1463 |
| 2 | 185.37 | 924.39 | 18.94 | 0.868 | 1191 |
| 3 | 184.86 | 889.70 | 23.33 | 0.837 | 1172 |
| 4 | 169.56 | 817.55 | 32.11 | 0.764 | 1224 |
| 5 | 151.94 | 732.12 | 49.35 | 0.658 | 1318 |
| 6 | 136.09 | 658.12 | 76.81 | 0.559 | 1449 |
| 7 | 121.29 | 576.61 | 123.66 | 0.501 | 1548 |
| 8 | 110.92 | 500.89 | 198.01 | 0.460 | 1593 |

**趋势**: pure-synthetic (r=0) 呈现清晰的 spectral collapse — log_det 从 Gen 2 峰值 924 持续下降至 Gen 8 的 501, eff_rank 从 185 降至 111, PPL 从 15 飙升至 198, D-4 从 0.91 降至 0.46, σ₁ 从 Gen 1 起持续增长(1463→1593)。各指标单调恶化，符合预期。

---
