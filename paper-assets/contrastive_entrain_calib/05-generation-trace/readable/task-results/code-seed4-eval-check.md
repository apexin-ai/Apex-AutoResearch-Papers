# code seed4 eval check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed4-eval-check_20260525T085820_result.json`
- **Structured JSON:** [`d6a73c2a7cf3477081c8.json`](../../sessions/d6/d6a73c2a7cf3477081c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 已删除。

## 3-Seed 完整对比表

| Checkpoint | seed2 ToF | seed2 NoF | seed2 SYCON | seed2 H | seed3 ToF | seed3 NoF | seed3 SYCON | seed3 H | seed4 ToF | seed4 NoF | seed4 SYCON | seed4 H | **Mean SYCON** | **Std SYCON** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ckpt-500 | 0.276 | 0.680 | 0.393 | 0.364 | 0.254 | 0.740 | 0.378 | 0.454 | 0.155 | 0.812 | 0.260 | 0.340 | **0.344** | ±0.059 |
| ckpt-1000 | 0.149 | 0.884 | 0.255 | 0.222 | 0.287 | 0.696 | 0.407 | 0.175 | 0.227 | 0.757 | 0.349 | 0.344 | **0.337** | ±0.062 |
| ckpt-1500 | 0.105 | 0.939 | 0.189 | 0.328 | 0.188 | 0.829 | 0.306 | 0.142 | 0.243 | 0.757 | 0.368 | 0.344 | **0.288** | ±0.074 |
| ckpt-2000 | 0.044 | 0.972 | 0.085 | 0.147 | 0.044 | 0.961 | 0.085 | 0.170 | 0.216 | 0.834 | 0.343 | 0.156 | **0.171** | ±0.122 |

### 关键发现

- **Best checkpoint**: ckpt-500 和 ckpt-1000 的 mean SYCON 最高（0.344 / 0.337），但 seed 间方差也较大
- **Seed4 表现异常**: seed4 在 ckpt-2000 仍保持 SYCON=0.343，远高于 seed2/seed3 的 0.085——seed4 的 sycophancy reduction 效果明显弱于其他两个 seed
- **ckpt-2000/final 相同**: seed4 的 ckpt-2000 和 final 结果完全一致（ToF=0.2155, NoF=0.8343, SYCON=0.3425, H=0.1556）
- **趋势**: seed2/seed3 在训练后期 SYCON 大幅下降（过度矫正），seed4 则保持相对稳定，导致 ckpt-2000 的跨 seed 方差很大（±0.122）

---
