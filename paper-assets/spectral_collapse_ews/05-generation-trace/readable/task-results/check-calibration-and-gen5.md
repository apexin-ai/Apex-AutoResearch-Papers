# check calibration and gen5

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_calibration_and_gen5_20260517T030946_result.json`
- **Structured JSON:** [`1fddbe15913b06e4aeb5.json`](../../sessions/1f/1fddbe15913b06e4aeb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 当前数据（5 generations, Gen 0-4）

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | σ₁ |
|-----|----------|---------|-----|-----------|------------|-----|
| 0 | 417.55 | 2366.68 | 9.55 | 0.741 | N/A | 1942.8 |
| 1 | 491.77 | 2464.76 | 11.38 | 0.626 | 1.623 | 804.0 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.515 | 1.268 | 712.0 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.490 | 1.134 | 700.7 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.468 | 1.098 | 729.6 |

### 进程状态
- **PID 59365** (GPU 0, 94%, 66GB): `run_phase0.py --resume_from_gen 4` — 正在跑 Gen 5
- **PID 25237** (GPU 1, 94%, 40GB): `run_phase0_1b.py` — 1B 模型实验并行进行中

### Go/No-go 条件

| 条件 | 状态 | 值 |
|------|------|-----|
| 1. Peak 后单调下降 | **PASS** | Gen 2 (496.44) → Gen 3 → Gen 4 单调递减 |
| 2. 加速比 ≥ 1.5x | **PASS** | 2.44x (Gen 3→4 decline / Gen 2→3 decline) |
| 3. PPL 增幅 ≥ 20% | **PASS** | +74.0% (11.38 → 19.80) |

### τ 预校准

- 估算 τ = 0.0108（decline_rate / peak_eff_rank）
- 当前 D005 设定 τ = 0.02
- **建议：保持当前 τ=0.02 不变**（估算值 0.0108 在同量级，0.02 更保守，作为 EWS 阈值合理）

三个 Go/No-go 条件全部 PASS，collapse 信号清晰。等 Gen 5 完成后 analyze_phase0.py 仍需 10 代才能正式运行。

---
