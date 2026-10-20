# ops cwm s42 ckpt6100 seq8192

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-s42-ckpt6100-seq8192_20260524T022201_result.json`
- **Structured JSON:** [`cbaf47522c7040e6989b.json`](../../sessions/cb/cbaf47522c7040e6989b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

**启动完成汇报：**

- **命令**：`CUDA_VISIBLE_DEVICES=3 nohup /root/miniconda3/bin/python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-6100 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --device cuda:0 --max_seq_length 8192 --max_new_tokens 512 --batch_size 4 --output_dir /root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s42_ckpt6100_seq8192_eval`
- **PID**：328067（子进程 328069）
- **GPU 3**：18764MiB / 32607MiB，76% util，正常推理中
- **日志**：`/tmp/cwm_s42_ckpt6100_seq8192.log`
- **进度**：9784 test instances，已跑 4 条，running_acc=100%
- **预估完成时间**：按 batch_size=4、seq8192 在 5090 上的速度，约 5~6 小时（前 4 条耗时 ~21 秒，每 batch ~5 秒，9784 条约 2446 batch ≈ 3.4 小时推理 + 开销，预计 4~5 小时完成）

---
