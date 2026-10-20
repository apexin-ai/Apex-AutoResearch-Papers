# code exp 002 signals 3B v6

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_002_signals_3B_v6_20260515T200808_result.json`
- **Structured JSON:** [`393737086bda01ba892d.json`](../../sessions/39/393737086bda01ba892d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_002_signals_3B_v6 已启动，状态摘要：**

| 项目 | 详情 |
|------|------|
| tmux session | `exp_002_signals_3B_v6` |
| GPU | cuda:3, 6470 MiB / 85% util |
| PID | 628100 (bash), 628112 (python) |
| Checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter` (lora_alpha=16 已确认) |
| Output | `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/` |
| Log | `/root/runs/contamcal-irt-calibration/exp_002_signals_3B_v6.log` |
| 任务 | 3 个 benchmark 顺序执行：mmlu → gsm8k → arc_challenge |
| 信号类型 | embedding + minkpp + selfcritique + constat (all) |

注意：`run_batch.py` 硬编码路径格式 `{model}_{dosage}_{seed}`，无法匹配 v2 命名。已直接调用 `compute_signals.py` 并显式传入 v2 checkpoint 路径。ref-model-path 与 adapter-path 相同（d000 是自身的 reference）。ConStat 的 eval 路径也已传入。

---
