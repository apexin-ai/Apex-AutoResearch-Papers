# ops eval gemma2 arc s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-gemma2-arc-s123_20260520T173905_result.json`
- **Structured JSON:** [`9e89f6865f70a687c43f.json`](../../sessions/9e/9e89f6865f70a687c43f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并注册。

**汇总：**
- **exp_id**: `eval_gemma2_arc_s123` → RUNNING on westd-29999 cuda:0
- **PID**: 397240 (nohup)，log: `/tmp/eval_gemma2_arc_s123.log`
- **Checkpoints**: `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d{000,005,025,050,100}_s123/lora_adapter`，全部 lora_alpha=32 ✓
- **evaluate.py md5**: `17673bf3...` 匹配 ✓ (C009)
- **速度**: ~6.7 it/s × 1172 items × 5 dosages ≈ 15 min 总计
- **输出**: `/root/contamcal-irt-calibration/results/arc_eval/gemma2/d{000,005,025,050,100}_s123/`

---
