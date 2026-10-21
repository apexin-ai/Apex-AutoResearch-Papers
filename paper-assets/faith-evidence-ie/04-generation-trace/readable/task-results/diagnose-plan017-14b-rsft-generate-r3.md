# diagnose plan017 14b rsft generate r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914_result.json`
- **Structured JSON:** [`4dbbe31efa78e6b51a55.json`](../../sessions/4d/4dbbe31efa78e6b51a55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有证据收集齐全。

```json
{
  "root_cause": "进程收到外部 SIGTERM (exit code 143)，日志无 Traceback/OOM/CUDA error。dmesg 和 journalctl 均无 OOM killer 记录。进程未在 tmux/screen 中运行，也无 PID 文件。无 registry 文件可追溯。最可能原因：启动该进程的 SSH session 断开后进程收到信号被杀，或被其他自动化/手动 kill。",
  "error_type": "infrastructure",
  "fix_steps": [
    "用 tmux 保护进程：tmux new -s rsft_gen，在 tmux 内运行命令，防止 SSH 断连导致进程被杀",
    "直接 --resume 重跑，JSONL 已有 2553 docs（20424 行），只需处理剩余 474 docs",
    "命令：tmux new -s rsft_gen 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b --num_generations 8 --resume'"
  ],
  "can_auto_fix": true,
  "progress": "已完成 2553 / 3027 docs（84.3%），剩余 474 docs，预计 ~1.5-2.5h"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "进程收到外部 SIGTERM (exit code 143)，日志无 Traceback/OOM/CUDA error。dmesg 和 journalctl 均无 OOM killer 记录。进程未在 tmux/screen 中运行，也无 PID 文件。无 registry 文件可追溯。最可能原因：启动该进程的 SSH session 断开后进程收到信号被杀，或被其他自动化/手动 kill。",
    "error_type": "infrastructure",
    "fix_steps": [
      "用 tmux 保护进程：tmux new -s rsft_gen，在 tmux 内运行命令，防止 SSH 断连导致进程被杀",
      "直接 --resume 重跑，JSONL 已有 2553 docs（20424 行），只需处理剩余 474 docs",
      "命令：tmux new -s rsft_gen 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b --num_generations 8 --resume'"
    ],
    "can_auto_fix": true,
    "progress": "已完成 2553 / 3027 docs（84.3%），剩余 474 docs，预计 ~1.5-2.5h"
  }
}
```

</details>

---
