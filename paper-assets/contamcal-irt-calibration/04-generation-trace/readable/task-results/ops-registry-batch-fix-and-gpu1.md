# ops registry batch fix and gpu1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_batch_fix_and_gpu1_20260514T210615_result.json`
- **Structured JSON:** [`4ce0d0661d37049cb201.json`](../../sessions/4c/4ce0d0661d37049cb201.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## Part A: Stale RUNNING 修正

| 实验 | 输出路径 | Metrics | Registry |
|------|---------|---------|----------|
| **exp_001_eval_05B_d025_aligned_v2** | `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned/` | MMLU=28.4%, GSM8K=31.1%, ARC=32.0%, HumanEval=19.2% (paraphrased aligned) | → DONE/success |
| **exp002-signal-d025-05B** | `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d025_s42/` | 3/3 signals × 3 benchmarks (13 files) | → DONE/success |

## Part B: GPU 1 — 0.5B d100 s123

| 步骤 | 状态 |
|------|------|
| **SFT 完成** | loss=1.567, epoch=1.0, runtime=4231s, EXIT_CODE=0 |
| **SFT output** | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter/` (35MB safetensors) |
| **exp_001_sft_05B_d100_s123** | → DONE/success |
| **Eval 提交** | PID 444836, GPU 1, tmux session `eval_05B_d100_s123` |
| **exp_001_eval_05B_d100_s123_aligned** | → RUNNING, log: `~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_s123_aligned.log` |

---
