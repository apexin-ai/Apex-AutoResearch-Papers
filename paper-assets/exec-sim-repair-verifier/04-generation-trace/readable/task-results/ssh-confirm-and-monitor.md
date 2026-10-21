# ssh confirm and monitor

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_confirm-and-monitor_20260520T110438_result.json`
- **Structured JSON:** [`1cef6bffbb068dc6b654.json`](../../sessions/1c/1cef6bffbb068dc6b654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个监控都在运行了。汇总结果：

---

## 任务 A：Qwen eval 脚本内容

### eval_qwen_cwm_s123.sh
```bash
#!/bin/bash
# Eval Qwen3-8B CWM repo-level s123 — final epoch checkpoint
# Run on GPU 1 after training completes
set -e
cd /home/sonny/exec-sim-repair-verifier

CKPT_DIR="/root/autodl-tmp/checkpoints_repo_cwm_8b_s123"
FINAL_CKPT=$(ls -d ${CKPT_DIR}/checkpoint-* 2>/dev/null | sort -t'-' -k2 -n | tail -1)
if [ -z "$FINAL_CKPT" ]; then
    echo "ERROR: No checkpoint found in ${CKPT_DIR}"
    exit 1
fi
echo "Using checkpoint: $FINAL_CKPT"

OUTDIR="/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s123_eval"
mkdir -p "$OUTDIR"

CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python eval_repo_cwm.py \
    --checkpoint_dir "$FINAL_CKPT" \
    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
    --split test \
    --device cuda:0 \
    --max_seq_length 8192 \
    --max_new_tokens 512 \
    --batch_size 1 \
    --output_dir "$OUTDIR"
```
(后跟结果统计 python 代码)

### eval_qwen_cwm_s456.sh
同结构，差异：
- `CKPT_DIR="/root/autodl-tmp/checkpoints_repo_cwm_8b_s456"`
- `CUDA_VISIBLE_DEVICES=2`
- `OUTDIR="/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s456_eval"`

**`--max_seq_length 8192` 两个脚本均已设置。** ✓

---

## 任务 B：监控进程对应关系

| 监控脚本 | 监控 PID | 训练进程 PID | 训练完成后触发 |
|----------|----------|-------------|---------------|
| `monitor_deepseek_s123_v2.sh` | 957333 | 925638 | `eval_deepseek_cwm_s123_v2.sh` |
| `monitor_deepseek_s456_v2.sh` | 957406 | 949112 | `eval_deepseek_cwm_s456_v2.sh` |

两个监控进程已在后台运行，每 5 分钟检查一次训练进程，训练结束后自动触发对应 eval 脚本。日志分别写入 `monitor_s123_v2.log` 和 `monitor_s456_v2.log`。

---
