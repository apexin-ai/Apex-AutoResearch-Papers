# gpu exp 006 irt launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-006-irt-launch_20260514T170625_result.json`
- **Structured JSON:** [`5e9b2bb35800d89e47d3.json`](../../sessions/5e/5e9b2bb35800d89e47d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。exp-006 启动完成：

- **实验**: `exp_006_irt_05B_v1` — 4PL+γ IRT (Stan NUTS) + 7 baselines + joint-fit ablation
- **服务器**: cqa1-21977, GPU 3, PID 411783
- **数据**: 6 个 0.5B 模型, dosages [0, 0, 5, 5, 25, 100], 4 benchmarks (mmlu/gsm8k/arc_challenge/humaneval)
- **输出**: `/root/autodl-tmp/exp006/results_05B_v1`
- **日志**: `/root/autodl-tmp/exp006/exp006_05B_v1.log`
- **状态**: RUNNING, Stan MCMC 已开始处理 MMLU (14042 items)

注意：使用了 mixed aligned/non-aligned 数据（d100_aligned 仍在运行，用了 d100 non-aligned v5 代替）。d000 和 d005 各有 aligned + non-aligned 两版本，作为独立 examinees 参与 fitting。Oracle dosage（无 exposure file）。

---
