# ops eval qwen7b arc s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-qwen7b-arc-s42_20260520T172011_result.json`
- **Structured JSON:** [`f5599644ed4c7019be52.json`](../../sessions/f5/f5599644ed4c7019be52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交完成。

**汇总**：
- **实验**: `eval_qwen7b_arc_s42` — Qwen2.5-7B ARC-Challenge 25-shot, seed=42, 5 dosages
- **服务器**: westd-29999, cuda:2 (CUDA_VISIBLE_DEVICES=2)
- **PID**: 392989, d000 eval 已在跑 (~10.3 it/s, 1172 items/dosage)
- **输出**: `/root/contamcal-irt-calibration/results/arc_eval/qwen7b/d{dosage}_s42/`
- **日志**: `/tmp/eval_qwen7b_arc_s42.log`
- **预计耗时**: ~1.5h (每 dosage ~2min eval + 模型加载)
- **Registry**: RUNNING, parent=eval_arc_s123_batch

验证通过项：C004 (显式 CUDA_VISIBLE_DEVICES=2) ✓, C006 (lora_alpha=32) ✓, C009 (evaluate.py MD5 match) ✓, GPU 2 空闲确认 ✓

---
