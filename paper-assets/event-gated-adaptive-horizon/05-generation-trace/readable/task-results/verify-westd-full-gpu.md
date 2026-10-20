# verify westd full gpu

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_westd_full_gpu_20260525T230619_result.json`
- **Structured JSON:** [`d5300a034757c60fc8ef.json`](../../sessions/d5/d5300a034757c60fc8ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行。

## 状态报告

### GPU 0 — exp_095_cheetah_008a_s0 (PID 54457, plan_023)
- **显存**: 4654 MiB / 97887 MiB, GPU-Util 44%, 39°C
- **进程**: 存活，运行 1h12m
- **参数确认**: `gate_fixed_dt=2, imag_horizon=15`, **无** `gate_subsample_max_dt` — subsample OFF 配置正确
- **日志**: 无报错（仅 FutureWarning 关于 amp.autocast，无害）。已完成初始 eval (return 8.3) 并进入训练，step 5000 指标正常。gate_dt 全部为 2.0 (gate_dt_2_frac=1.0)，符合 fixed_dt=2 预期。

### GPU 1 — exp_094_cheetah_008d_s3 (PID 53576, plan_021)
- **显存**: 6476 MiB / 97887 MiB, GPU-Util 71%, 42°C
- **进程**: 存活，运行 9h03m
- **参数确认**: `gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8` — subsample ON 配置正确
- **日志**: 无报错。已推进到 step 8000，train_return 从 8.8 升到 13.3，训练正常收敛。gate_dt 同样全为 2.0。

两张卡均健康，无异常。

---
