# ops eval olmo2 s0 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-olmo2-s0-mmlu_20260520T102819_result.json`
- **Structured JSON:** [`3f01f1243a8e6f093b64.json`](../../sessions/3f/3f01f1243a8e6f093b64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认 cuda:2 正在运行（PID 321872, 14472MiB）。

**汇总：**
- 脚本：`/root/contamcal-irt-calibration/scripts/eval_olmo2_s0_mmlu.sh`
- 任务：`eval_olmo2_s0_mmlu`，westd-29999 cuda:2
- 内容：OLMo-2-7B s0 × 5 dosage (d000/d005/d025/d050/d100) MMLU 5-shot eval
- evaluate.py md5 ✓，lora_alpha=32 ✓，C001/C002/C004/C006/C009 均已检查
- 结果输出到 `results/mmlu_eval/olmo2/d{dosage}_s0/`
- 预计总耗时 ~2-2.5h
- 日志：`~/runs/contamcal-irt-calibration/eval_olmo2_s0_mmlu.log`

---
