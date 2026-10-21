# prepare home next task plan

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_home-next-task-plan_20260517T223515_result.json`
- **Structured JSON:** [`cd85395c4512c4a30f67.json`](../../sessions/cd/cd85395c4512c4a30f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## Home-1x5090 资源报告

### 磁盘空间
| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| `/` (nvme) | 1.1T | 696G | **318G** | 69% |

### 可用模型

| 模型 | 路径 | 大小 | 备注 |
|------|------|------|------|
| **Qwen3-8B** | `~/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d...` | 16G | 完整权重，当前 3-shot baseline 用的 |
| **Qwen3-4B** | `~/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a72...` | (cached) | |
| **Qwen3-0.6B** | `~/.cache/...` | (小) | |
| **deepseek-coder-6.7b-instruct** | `~/.cache/huggingface/hub/models--deepseek-ai--deepseek-coder-6.7b-instruct/snapshots/e5d64add...` | **13G** | 完整权重 |
| **DeepSeek-R1-Distill-Qwen-7B** | `~/redundancy-compound-sparsity/models/.../snapshots/916b56a4...` | **15G** | 完整权重 (blobs/) |

### 已有 DeepSeek LoRA Checkpoint
- **`/home/sonny/exec-sim-repair-verifier/checkpoints_deepseek_traj_func/best/`**
  - base model = `deepseek-ai/deepseek-coder-6.7b-instruct`
  - LoRA r=16, alpha=32, target: q/k/v/o_proj
  - 这是已训练好的 **trajectory-level verifier** adapter

### TRAJ 数据
- `data/traj_test.jsonl` — **1032 条**
- `data/traj_train.jsonl`, `data/traj_val.jsonl` 也存在
- 数据格式：code + test_summary + label (0/1)

### 关键脚本
- **`run_qwen_repo_level.py`** — Qwen3-8B 专用 3-shot baseline，硬编码模型路径，不适合直接跑 DeepSeek
- **`eval_traj_verifier.py`** — 通用 LoRA verifier eval 脚本，支持 `--model_name` 和 `--checkpoint_dir`，可直接用于 DeepSeek TRAJ eval
- **`eval_deepseek_repo.py`** — 存在但文件内容损坏（充满 null 字节），不可用

---

## 结论与建议

**DeepSeek TRAJ repo-level few-shot eval 可以立即在 home GPU 执行：**

1. **已有训练好的 DeepSeek LoRA checkpoint** (`checkpoints_deepseek_traj_func/best/`)，base model 是 `deepseek-coder-6.7b-instruct`（13G，已下载完整）
2. 使用 `eval_traj_verifier.py` 即可直接跑：
   ```bash
   python eval_traj_verifier.py \
     --data_dir /home/sonny/exec-sim-repair-verifier/data \
     --checkpoint_dir /home/sonny/exec-sim-repair-verifier/checkpoints_deepseek_traj_func/best \
     --model_name /home/sonny/.cache/huggingface/hub/models--deepseek-ai--deepseek-coder-6.7b-instruct/snapshots/e5d64addd26a6a1db0f9b863abf6ee3141936807 \
     --data_prefix traj \
     --output eval_deepseek_traj_results.json
   ```
3. 不需要下载任何新模型，磁盘充裕（318G 剩余）

**如果需要 DeepSeek few-shot baseline（无 LoRA，类似 Qwen 的 3-shot）：** 需要写一个类似 `run_qwen_repo_level.py` 的新脚本，或修改现有脚本的模型路径。`eval_deepseek_repo.py` 文件已损坏不可用。

---
