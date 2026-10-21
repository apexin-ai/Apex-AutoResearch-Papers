# code prepare eval pipeline

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-eval-pipeline_20260513T225444_result.json`
- **Structured JSON:** [`4be7e8090efb45ab4786.json`](../../sessions/4b/4be7e8090efb45ab4786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整报告。

---

## Eval Pipeline 就绪性报告

### 1. Eval 脚本清单

| 脚本 | 状态 | 关键参数 |
|---|---|---|
| `eval_repo_cwm.py` | ✅ 就绪 | max_new_tokens=**1024**(默认), batch_size=8, 有 `--output_dir` |
| `eval_repo_cls.py` | ⚠️ 可用但有限制 | max_new_tokens=8(硬编码), batch_size=16, **无 `--output_dir`**, **无 `--max_samples`** |

### 2. Eval 数据

- `data/swebench_full/swebench_test.jsonl` — **9784 条** ✅

### 3. 环境

- torch=2.10.0+cu128, transformers=4.57.6, peft=0.19.0 ✅
- 4x RTX 5090 (32GB)
- Base models: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` ✅, `Qwen3-8B` ✅

### 4. GPU 分配 & 训练状态

| GPU | 实验 | 进度 | 预计剩余 |
|---|---|---|---|
| 0 | CWM seed123 | ~200/6633 (3%) | ~14h |
| 1 | CWM v12 (seed42) | ~200/6633 (3%), 已有 checkpoint-100, 200 | ~14h |
| **2** | **空闲** | — | — |
| 3 | CLS 8B (seed42) | ~84/6633 (1%) | ~15h |

### 5. 问题

**CLS v5 conda 训练未启动** — 日志只有数据加载阶段，没有训练进程在运行，checkpoint 目录为空。需要排查原因并重新启动。

**CLS eval 脚本缺 `--output_dir`** — 多个 CLS eval 结果会互相覆盖，需用 `--output` / `--pred_output` 区分文件名。

### 6. Eval 命令模板

训练完成后，在 GPU 2 上顺序执行（`CUDA_VISIBLE_DEVICES=2` + `--device cuda:0`）：

**CWM v12:**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=2 python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_conda_v12/checkpoint-BEST \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --max_new_tokens 1024 \
  --batch_size 8 \
  --device cuda:0 \
  --output_dir /root/autodl-tmp/results/repo_cwm_v12_eval/
```

**CWM seed123:**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=2 python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/checkpoint-BEST \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B \
  --max_new_tokens 1024 \
  --batch_size 8 \
  --device cuda:0 \
  --output_dir /root/autodl-tmp/results/repo_cwm_seed123_eval/
```

**CLS 8B:**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=2 python3 eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-BEST \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --batch_size 8 \
  --device cuda:0 \
  --output eval_repo_cls_8b.json \
  --pred_output eval_repo_cls_8b_predictions.jsonl
```
> CLS 8B 用 Qwen3-8B (15.3B params)，batch_size 从默认 16 降到 8，避免 OOM。

**CLS v5 conda:** ❌ 无法执行 — 训练未启动，无 checkpoint。

### 7. 待办

1. **排查 CLS v5 conda 训练失败原因并重启**（GPU 2 空闲可用）
2. 训练完成后确定 best checkpoint（查 `trainer_state.json` 中的 `best_model_checkpoint`）
3. 将 `checkpoint-BEST` 替换为实际 checkpoint 编号后执行

---
