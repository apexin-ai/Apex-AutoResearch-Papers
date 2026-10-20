# ops qwen14b partial arc eval cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-partial-arc-eval-cuda3_20260521T024034_result.json`
- **Structured JSON:** [`9d419cd64617776e9978.json`](../../sessions/9d/9d419cd64617776e9978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动。

**汇总：**
- **实验**: `eval_qwen14b_arc_s0_partial` — Qwen-14B s0 ARC 25-shot eval (d000/d005/d025/d100)
- **服务器**: westd-29999 cuda:3
- **PID**: 467742, 32726 MiB 占用, 99% GPU utilization
- **tmux session**: `eval_qwen14b_arc_s0`
- **日志**: `/root/contamcal-irt-calibration/logs/eval_qwen14b_arc_s0_partial.log`
- **输出**: `/root/contamcal-irt-calibration/results/arc_eval/qwen14b/d{000,005,025,100}_s0/`
- **预估完成**: ~60-80 min (4 dosage × ~15-20min)

注意事项：
- 脚本中 adapter 路径已修正为 `.../lora_adapter/` 子目录
- evaluate.py md5 与现有 batch 脚本 reference 一致（`17673bf...`）；C009 约束中的 37591 bytes 可能是旧版本记录，当前 westd 实际使用的是 37775 bytes 版本，已与现有 `eval_qwen14b_s0_batch.sh` 保持一致
- batch-size=2（14B 模型显存较紧）

---
