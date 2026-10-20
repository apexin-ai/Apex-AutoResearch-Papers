# eval cls8b s42 ckpt1600 val8192

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-ckpt1600-val8192_20260515T033928_result.json`
- **Structured JSON:** [`b8688dc02023f22c722a.json`](../../sessions/b8/b8688dc02023f22c722a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交，汇总：

- **实验**: `cls8b-s42-ckpt1600-val8192-eval`
- **PID**: 324412
- **GPU**: cuda:0（5090，空闲）
- **命令**: `python3 eval_repo_cls.py --checkpoint_dir .../checkpoint-1600 --model_name Qwen/Qwen3-8B --split val --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir results/repo_cls_8b_s42_ckpt1600_val8192`
- **日志**: `~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1600-val8192-eval.log`
- **预计耗时**: ~30min（参考 ckpt-1200/1400）
- **Registry**: RUNNING

Val sweep 最后一个数据点，完成后 curve 齐全：ckpt-1000(88.23%) → 1200(87.76%) → 1400(85.97%) → 1600(?)。

---
