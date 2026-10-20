# eval gemma2 d100 s0 mmlu arc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gemma2_d100_s0_mmlu_arc_20260521T023352_result.json`
- **Structured JSON:** [`c7ee5685de4107fea517.json`](../../sessions/c7/c7ee5685de4107fea517.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已提交成功。

## 提交报告

**脚本内容摘要：**
- 两个脚本结构相同：C009 md5 校验 evaluate.py → C006 验证 lora_alpha=32 → 调用 `/root/miniconda3/bin/python` 运行 evaluate.py
- MMLU：`--benchmarks mmlu --batch-size 8`，输出到 `results/mmlu_eval/gemma2/d100_s0`，`CUDA_VISIBLE_DEVICES=0`
- ARC：`--benchmarks arc_challenge --batch-size 8`，输出到 `results/arc_eval/gemma2/d100_s0`，`CUDA_VISIBLE_DEVICES=2`
- 均设置 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`

**实际提交：**

| 实验 | exp_id | GPU | PID | 日志 |
|------|--------|-----|-----|------|
| MMLU | `eval_gemma2_d100_mmlu_s0` | cuda:0 | 464485 | `~/runs/contamcal-irt-calibration/eval_gemma2_d100_mmlu_s0.log` |
| ARC | `eval_gemma2_d100_arc_s0` | cuda:2 | 464631 | `~/runs/contamcal-irt-calibration/eval_gemma2_d100_arc_s0.log` |

两个 eval 在不同 GPU 上并行运行，timeout 6 小时。

---
