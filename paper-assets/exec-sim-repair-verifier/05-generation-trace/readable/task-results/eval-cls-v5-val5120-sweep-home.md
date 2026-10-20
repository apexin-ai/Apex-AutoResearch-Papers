# eval cls v5 val5120 sweep home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-v5-val5120-sweep-home_20260514T154933_result.json`
- **Structured JSON:** [`39e005022568eef682aa.json`](../../sessions/39/39e005022568eef682aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 已被占用，无法启动新的 eval。**

占用详情：
- **PID**: 3137889（用户 sonny）
- **进程**: `eval_repo_cls.py` — 正在跑 conda checkpoint-400 的 val@5120 评估
- **参数**: `--checkpoint_path .../checkpoints_repo_cls_8b_conda_westd/checkpoint-400 --split val --max_seq_length 5120 --batch_size 4 --model_name .../Qwen3-8B`
- **显存占用**: 22500 MiB（几乎满载）
- **已运行**: ~1 分 28 秒

看起来已经有一个 conda ckpt-400 val@5120 的评估在跑（正是你要求的首批任务之一），但用的是 **Qwen3-8B** 模型而非 Qwen3-4B。需要等它完成后才能启动新任务。要等它跑完后继续，还是先停掉它？

---
