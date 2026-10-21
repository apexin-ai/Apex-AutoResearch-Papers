# ssh d045 home cls earlystop eval seed123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d045-home-cls-earlystop-eval-seed123_20260513T062216_result.json`
- **Structured JSON:** [`0897b7aa676ee7b5755f.json`](../../sessions/08/0897b7aa676ee7b5755f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered. Here's the complete task summary:

---

## D045 Task — All 4 Steps Complete

### Step 1: Checkpoint-200 验证 ✓
- **路径**: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/checkpoint-200/`
- **状态**: 完整。包含 adapter_config.json, adapter_model.safetensors (47MB), optimizer.pt (94MB), trainer_state.json 等
- LoRA checkpoint 不含 tokenizer 文件，属正常

### Step 2: Kill CLS v4 训练进程 ✓
- PID 2885139 (parent) + 2885141 (child) 均已 kill
- GPU 内存已释放

### Step 3: CLS Eval on checkpoint-200 ✓

| 指标 | 值 |
|------|-----|
| Accuracy | **66.11%** |
| Majority baseline | 72.96% (gap: **-6.85pp**) |
| F1 macro | **56.61%** |
| F1 fail | 36.3% (P=36.9%, R=35.7%) |
| F1 pass | 76.9% (P=76.5%, R=77.4%) |
| Confusion | TP=5523, TN=945, FP=1701, FN=1615 |
| Unparseable | 132 |
| Predictions | `/home/sonny/exec-sim-repair-verifier/results/repo_cls_v4_eval/eval_repo_cls_predictions.jsonl` |

### Step 4: CLS seed123 训练已启动 ✓
- **PID**: 2940525 (python3), parent bash PID 2940520
- **脚本**: `train_repo_verifier_seed123.py` (eval_steps=100, save_steps=100, save_total_limit=5)
- **输出目录**: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123/`
- **日志**: `/tmp/repo-level-cls-seed123_stdout.log`
- **GPU**: 19.9GB / 32.6GB
- **进度**: step 3/6633, ~6.9s/it, 训练正常推进
- **修复**: 升级 accelerate 1.1.1 → 1.13.0 解决 `unwrap_model()` 兼容性问题

### Errors encountered & resolved
1. Tokenizer 从 checkpoint_dir 加载失败 → 改为从 base model 加载
2. CUDA OOM (残留子进程占 19GB) → kill 子进程释放 GPU
3. accelerate 版本不兼容 → pip install -U accelerate

---
