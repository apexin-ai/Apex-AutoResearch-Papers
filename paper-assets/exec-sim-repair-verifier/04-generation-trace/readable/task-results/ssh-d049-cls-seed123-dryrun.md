# ssh d049 cls seed123 dryrun

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d049-cls-seed123-dryrun_20260513T092842_result.json`
- **Structured JSON:** [`7f98121efa26cf3e9b08.json`](../../sessions/7f/7f98121efa26cf3e9b08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

干净了。两个 dry-run 全部通过。

---

## 汇报

### 1. 超参确认 ✅

两个脚本超参一致：

| 参数 | 值 |
|------|-----|
| lr | 5e-5 |
| weight_decay | 0.01 |
| warmup_ratio | 0.05 |
| save_total_limit | 5 |

### 2. Dry-run 结果

**CLS (train_repo_verifier.py, cuda:0)** ✅

| Step | Loss | Grad Norm | LR |
|------|------|-----------|-----|
| 1 | 131.0 | 774.5 | 0 |
| 2 | 146.5 | 800.4 | 5e-5 |
| 3 | 131.2 | 797.2 | 3.75e-5 |
| 4 | 99.1 | 627.7 | 2.5e-5 |
| 5 | 64.0 | 394.5 | 1.25e-5 |

avg_loss=114.4, ~6.76s/it, trainable 0.29% (11.8M/4.03B)

**CWM (train_repo_cwm.py, cuda:3)** ✅

| Step | Loss | Grad Norm | LR |
|------|------|-----------|-----|
| 1 | 33.6 | 40.9 | 0 |
| 2 | 36.6 | 43.9 | 5e-5 |
| 3 | 31.8 | 37.7 | 3.75e-5 |
| 4 | 32.6 | 39.6 | 2.5e-5 |
| 5 | 25.3 | 31.2 | 1.25e-5 |

avg_loss=31.98, ~9.13s/it, trainable 0.29%

### 3. GPU 状态

| GPU | 状态 | 显存占用 |
|-----|------|---------|
| 0 | **空闲** | 0/32 GiB |
| 1 | 占用 (PID 139302) | 16.3/32 GiB |
| 2 | 占用 (PID 130031) | 13.5/32 GiB |
| 3 | **空闲** | 0/32 GiB |

### 4. 注意事项

- 服务器无法访问 HuggingFace，CLS 默认 `--model_name Qwen/Qwen3-4B` 会失败，**必须显式传本地路径**
- CWM 默认已指向本地缓存，无此问题
- 原计划 CWM 用 cuda:1，但 **cuda:1 被其他进程占用**，改用 cuda:3

### 5. 推荐启动命令

**CLS (cuda:0)**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
nohup bash -c 'export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0; \
python3 train_repo_verifier.py \
  --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
  --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123/ \
  --run_name repo-cls-qwen3-4b-lora-seed123 \
  --seed 123' \
> /home/sonny/exec-sim-repair-verifier/logs/cls_seed123.log 2>&1 &
```

**CWM (cuda:3)**
```bash
cd /home/sonny/exec-sim-repair-verifier && \
nohup bash -c 'export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=3; \
python3 train_repo_cwm.py \
  --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cwm_seed123/ \
  --run_name repo-cwm-qwen3-4b-lora-seed123 \
  --seed 123' \
> /home/sonny/exec-sim-repair-verifier/logs/cwm_seed123.log 2>&1 &
```

---
