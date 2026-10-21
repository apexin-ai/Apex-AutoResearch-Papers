# analysis exp 009d baseline walker s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009d_baseline_walker_s0_20260516T095003_result.json`
- **Structured JSON:** [`9b1d8c00d22590af2185.json`](../../sessions/9b/9b1d8c00d22590af2185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总：

---

## exp_009d_baseline_walker_s0 实验结果

| 指标 | 值 |
|------|-----|
| **final_step** | 516,000 (最后 train log); 最后 eval 在 508,000 |
| **completed** | ✅ 是 — 超过 500K 目标，EXIT_CODE=0 正常结束 |
| **eval_return_final** | 927.62 (step 508K) |
| **eval_return_peak** | 950.96 @ step 398K |
| **eval_return_mean_last5** | 936.25 (steps 468K/478K/488K/498K/508K: 944.3, 944.7, 936.2, 928.4, 927.6) |
| **v_over_e_ratio** | 无此指标（metrics.jsonl 中未记录） |
| **wandb_run_id** | 无 — logdir 下无 wandb 目录 |
| **log_path** | `~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s0.log` |
| **checkpoint_path** | `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/latest.pt` (229MB, 2026-05-16 17:47 CST) |

### 异常检测
- **step 78K 处有一次严重 dip**: eval_return 从 402 (68K) 骤降至 81 (78K)，随后立即恢复至 440 (88K)。单次评估波动，非持续性问题。
- 300K 之后进入稳定平台期 (910–951)，无 NaN、无崩溃、无持续下降。
- 注意：背景信息中提到 EXIT_CODE=129 (SIGHUP)，但实际日志末尾为 **EXIT_CODE=0**，说明进程正常完成后退出（可能 registry 记录的是更早一次中断前的状态）。

---
