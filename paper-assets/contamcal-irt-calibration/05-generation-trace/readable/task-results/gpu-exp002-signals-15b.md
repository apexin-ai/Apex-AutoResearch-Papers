# gpu exp002 signals 15B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp002_signals_15B_20260514T194928_result.json`
- **Structured JSON:** [`ebd2c6cf64db8217761b.json`](../../sessions/eb/ebd2c6cf64db8217761b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已在 GPU 2 上运行，registry 已更新为 RUNNING。

**状态汇总：**
- **实验 ID**: `exp002-signals-1p5B`
- **GPU**: cuda:2，tmux session `exp002-signals-1p5B`
- **任务**: 4 dosages (d000, d005, d025, d100) × 3 benchmarks (mmlu, gsm8k, arc_challenge) = **12 个子任务**
- **Signals**: S1 Embedding, S2 Min-K++, S4 SelfCritique（S3 ConStat 跳过——缺少 paraphrase eval results）
- **输出**: `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d{XXX}_s42/`
- **日志**: `~/runs/contamcal-irt-calibration/exp002-signals-1p5B.log`
- 第 1/12 个子任务（Qwen2.5-1.5B_d000_s42/mmlu）已开始执行

---
