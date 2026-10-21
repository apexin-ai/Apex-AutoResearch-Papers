# ops urgent progress check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-progress-check_20260518T024333_result.json`
- **Structured JSON:** [`7e71a8fdf65764f000b8.json`](../../sessions/7e/7e71a8fdf65764f000b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### GPU 状态
两块 RTX PRO 6000 均满载运行：GPU 0 (100%, 78°C, 535W), GPU 1 (97%, 80°C, 565W)。

---

### exp_006 — adaptive k=10 (GPU 0)

**进度**: 完成 Gen 0-5 / 共 10 gen，当前正在跑 Gen 6
**运行时长**: 8h 51m（启动于 01:53 UTC）

| Gen | ppl | eff_rank | log_det | distinct_4 | mix_ratio | controller |
|-----|---------|----------|---------|------------|-----------|------------|
| 0 | 9.554 | 417.55 | 2366.68 | 0.741 | — | baseline |
| 1 | 10.089 | 477.31 | 2365.10 | 0.710 | 0.50 | not triggered |
| 2 | 10.416 | 487.08 | 2394.01 | 0.600 | 0.50 | not triggered |
| 3 | 10.760 | 496.03 | 2423.83 | 0.490 | 0.50 | not triggered |
| 4 | 11.135 | 501.19 | 2448.26 | 0.430 | 0.50 | not triggered |
| 5 | 11.643 | 512.50 | 2488.08 | 0.373 | 0.50 | not triggered |

**Controller 状态**: 未触发。mix_ratio 始终 = 0.5，log_det 持续上升（未出现下降信号）。

---

### exp_004 — fixed_mix (GPU 1)

**进度**: 完成 Gen 0-4 / 共 10 gen，当前正在跑 Gen 5
**运行时长**: 8h 48m（启动于 01:56 UTC）

| Gen | ppl | eff_rank | log_det | distinct_4 | mix_ratio |
|-----|---------|----------|---------|------------|-----------|
| 0 | 9.554 | 417.55 | 2366.68 | 0.741 | — |
| 1 | 10.083 | 477.89 | 2366.58 | 0.669 | 0.50 |
| 2 | 10.413 | 487.92 | 2395.36 | 0.582 | 0.50 |
| 3 | 10.758 | 496.57 | 2425.64 | 0.456 | 0.50 |
| 4 | 11.138 | 502.05 | 2451.72 | 0.328 | 0.50 |

---

### 完成时间估算

| 实验 | 已完成训练 gen | 每 gen 耗时 | 剩余 gen | 预计剩余 | 预计完成 (UTC) |
|------|---------------|------------|---------|---------|---------------|
| exp_006 | 5 (Gen 1-5) | ~106 min | 4 | ~7h | ~17:45 |
| exp_004 | 4 (Gen 1-4) | ~132 min | 5 | ~11h | ~21:45 |

### 关键观察

1. **两个实验的 ppl / eff_rank / log_det 轨迹几乎一致**，说明到目前为止 adaptive 和 fixed_mix 条件下模型退化趋势相同
2. **distinct_4 在 exp_004 (fixed_mix) 下降更快**: Gen 4 时 0.328 vs exp_006 的 0.430，fixed_mix 的多样性损失更严重
3. **Controller 未触发**: log_det 持续上升（非下降），tau=0.002 的阈值未被触碰。controller 可能需要等 log_det 出现拐点/下降才会触发干预
4. **exp_004 比 exp_006 慢约 25%/gen**，原因待查（可能是 GPU 1 温度略高导致降频）

---
