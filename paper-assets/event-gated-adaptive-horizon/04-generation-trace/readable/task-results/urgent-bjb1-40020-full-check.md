# urgent bjb1 40020 full check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1-40020-full-check_20260519T233212_result.json`
- **Structured JSON:** [`f927e9089ded76cb5a26.json`](../../sessions/f9/f927e9089ded76cb5a26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**Director 误报——两张卡都在用，4 个实验全部正在运行。**

| exp_id | server:gpu | step | target | eval_return | ve_ratio@105K | ve_ratio@latest | status |
|--------|-----------|------|--------|-------------|---------------|-----------------|--------|
| exp_025_obs_sgs_walker_s1 | bjb1-40020:cuda0 | 155K | 210K | 524.57 | **0.5093** | 0.1842 @155K | **running** |
| exp_025_obs_sgs_walker_s2 | bjb1-40020:cuda1 | 145K | 210K | 99.24 | **2.7403** | 1.4058 @145K | **running** |
| exp_026_obs_sgs_cheetah_s0 | bjb1-40020:cuda0 | 65K | 105K | 5.97 | N/A | 8.5607 @65K | **running** |
| exp_026_obs_sgs_cheetah_s1 | bjb1-40020:cuda1 | 65K | 105K | 4.67 | N/A | 10.8375 @65K | **running** |

### 关键观察

- **exp_025_s1 (walker seed1)**: 表现良好，eval_return ~525，ve_ratio 从 0.51@105K 持续下降到 0.18@155K（value 校准改善中）
- **exp_025_s2 (walker seed2)**: 表现差，eval_return 仅 ~99（s1 的 1/5），ve_ratio 2.74@105K → 1.41@145K，value 严重高估
- **exp_026_s0 (cheetah seed0)**: eval_return 在 45K 后崩塌（161→58→6），ve_ratio 飙至 8.56，训练可能已发散
- **exp_026_s1 (cheetah seed1)**: 同样崩塌（272→52→8→5），ve_ratio 10.84，训练发散

GPU 利用率：GPU0 36% / 7124MiB，GPU1 68% / 5042MiB。注意 exp_025 和 exp_026 各自共享 GPU（每卡跑了 2 个实验），这可能是 cheetah 实验性能差的原因之一（GPU 内存争用）。

---
