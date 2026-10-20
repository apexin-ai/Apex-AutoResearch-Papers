# ops gpu status and submit ready

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-submit-ready_20260515T052650_result.json`
- **Structured JSON:** [`daa52bcb11897bec230a.json`](../../sessions/da/daa52bcb11897bec230a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 使用状态汇总

### GPU 占用情况

| GPU | PID | 进程 | 显存占用 | GPU-Util | 状态 |
|-----|-----|------|----------|----------|------|
| cuda:0 | 498153 | SFT: Qwen2.5-0.5B_d025_s123 | 12462/24564 MiB | 98% | 正常运行 (1h26m) |
| cuda:1 | 492660 | Eval: 3B_d000_v2_s123_aligned | 8976/24564 MiB | 67% | 正常运行 (2h05m) |
| cuda:2 | 506625 | Eval: 3B_d100_v2_s123_aligned | 8976/24564 MiB | 62% | 正常运行 (7m) |
| cuda:3 | 503791 | Eval: 3B_d025_v2_aligned | 8976/24564 MiB | 66% | 正常运行 (29m) |
| cuda:4 | 494109 | Eval: 0.5B_d000_s42_v2 (v7) | 3686/24564 MiB | 34% | 正常运行 (1h59m) |
| **cuda:5** | — | — | **0 MiB** | **0%** | **空闲** |

### 空闲 GPU

**cuda:5** — 完全空闲，可提交实验。

### RUNNING 实验进程状态

| 实验 | 状态 | 备注 |
|------|------|------|
| exp_001_sft_05B_d025_s123_v2 (pid=498153) | ✅ 存活 | GPU 0, SFT 训练中 |
| exp_001_eval_3B_d000_v2_s123_aligned (pid=492660) | ✅ 存活 | GPU 1 |
| exp_001_eval_3B_d100_v2_s123_aligned (pid=506625) | ✅ 存活 | GPU 2 |
| exp_001_eval_3B_d025_v2_aligned (pid=503791) | ✅ 存活 | GPU 3 |
| exp_001_eval_05B_d000_s42_v7 (pid=494109) | ✅ 存活 | GPU 4 |

### CPU 实验进程状态

| 实验 | 状态 | 备注 |
|------|------|------|
| exp_004_sim_sweep_v5 (pid=652931) | ❌ **进程不存在** | 已退出，需检查是完成还是异常 |
| exp006-s1only-gsm8k-2pl (pid=496852) | ✅ 存活 | 运行 1h39m, IRT 2PL+gamma, 4 chains |

### 注意事项

- 有 4 个 defunct 僵尸进程 (contam_irt_4pl_*, pid 452486-452491)，不占资源但建议清理
- 有 1 个旧的 defunct python 进程 (pid=318424)
- exp_004_sim_sweep_v5 (pid=652931) 进程已不存在，需要检查日志确认是正常完成还是异常退出

---
