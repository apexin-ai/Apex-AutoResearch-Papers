# ops eval qwen14b arc s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-qwen14b-arc-s42_20260520T180717_result.json`
- **Structured JSON:** [`a069f87f604aef94526e.json`](../../sessions/a0/a069f87f604aef94526e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **脚本**: `/root/contamcal-irt-calibration/scripts/eval_qwen14b_arc_s42.sh`
- **tmux session**: `eval_qwen14b_arc_s42` on westd-29999 cuda:0
- **5 dosages**: d000/d005/d025/d050/d100, batch_size=4, ARC-Challenge 25-shot
- **合规**: C004 (CUDA_VISIBLE_DEVICES=0), C006 (lora_alpha=32 验证), C009 (md5 验证)
- **Registry**: `eval_qwen14b_arc_s42` → RUNNING, parent=eval_arc_s123_batch
- **日志**: `/root/contamcal-irt-calibration/logs/eval_qwen14b_arc_s42.log`

---
