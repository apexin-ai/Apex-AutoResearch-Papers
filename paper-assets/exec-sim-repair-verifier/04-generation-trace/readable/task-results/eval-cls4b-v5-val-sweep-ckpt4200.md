# eval cls4b v5 val sweep ckpt4200

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls4b-v5-val-sweep-ckpt4200_20260515T032510_result.json`
- **Structured JSON:** [`246b4284186cfc01853f.json`](../../sessions/24/246b4284186cfc01853f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交，推理正常进行中。

**状态**:
- **PID**: 3213540
- **服务器**: home-1x5090 cuda:0
- **命令**: `python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4200 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4200_val5120`
- **日志**: `/home/sonny/runs/exec-sim-repair-verifier/cls4b-v5-val-sweep-ckpt4200.log`
- **预计耗时**: ~75 分钟（9335 samples, ~7.5s/batch×584 batches）
- **Registry**: `cls4b-v5-val-sweep-ckpt4200` → RUNNING

---
