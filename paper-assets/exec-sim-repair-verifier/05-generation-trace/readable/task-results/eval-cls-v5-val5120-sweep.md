# eval cls v5 val5120 sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-v5-val5120-sweep_20260514T154621_result.json`
- **Structured JSON:** [`dddd5c0d68575547fefe.json`](../../sessions/dd/dddd5c0d68575547fefe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法立即启动，有几个阻塞问题：**

### 1. GPU 0 不空闲
所有 4 个 GPU 都在跑任务：

| GPU | VRAM Used | 进程 |
|-----|-----------|------|
| 0 | 12990 MiB (88%) | `eval_repo_cwm.py` — CWM seed123_conda ckpt-500 (PID 195531, 今天 09:03 启动) |
| 1 | 12990 MiB (88%) | python3 (PID 195668) |
| 2 | 21196 MiB (95%) | python3 (PID 245775) |
| 3 | 26742 MiB (67%) | python3 (PID 248041) |

### 2. Checkpoint 路径不对
指定路径不存在。实际路径在 `/root/autodl-tmp/`：
- `/root/autodl-tmp/checkpoints_repo_cls_8b/` — checkpoint-200, 2400, 2600, 2800, **3000**
- `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` — checkpoint-200, **400**, 600

### 3. eval 脚本参数不同
`eval_repo_cls.py` 实际接口：
- `--checkpoint_dir`（不是 `--checkpoint_path`）
- `--output` + `--pred_output`（不是 `--output_dir`）
- `--device cuda:0`（不是 `CUDA_VISIBLE_DEVICES`）
- `--model_name` 本地路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B`
- 环境是 conda（`/root/miniconda3`），不是 venv

### 需要你决定

要启动 CLS sweep，需要先释放 GPU 0。**要不要 kill GPU 0 上的 CWM eval（PID 195531）？** 还是等它跑完？

---
