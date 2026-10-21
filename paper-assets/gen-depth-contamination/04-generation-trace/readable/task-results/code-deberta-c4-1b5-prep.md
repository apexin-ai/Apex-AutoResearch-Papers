# code deberta c4 1b5 prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deberta-c4-1b5-prep_20260519T202226_result.json`
- **Structured JSON:** [`39c39bd4324fbfb09a06.json`](../../sessions/39/39c39bd4324fbfb09a06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 仍然无法连接。AutoDL 实例可能已重启，端口已变更。

**当前状态：**

脚本已完成，路径：`scripts/run_deberta_c4_1b5.py`

**脚本功能：**
- `--config` 选择 qwen_rw / pythia_greedy / qwen_cont256
- `--gpu` 指定 GPU（默认 0，配合 `CUDA_VISIBLE_DEVICES` 使用）
- `--dry_run` 模式：只加载数据 + 模型 + 跑 1 个 batch 验证
- AMP fp16 加速
- 5-fold GroupKFold (group=doc_id)
- 保存 `.npz` OOF predictions (doc_id, true_depth, pred_probs[6])
- Pairwise AUC + Bootstrap 95% CI (10000 resamples, cluster by doc_id) + F1@0.50
- K* = max k where CI_lower(k vs k+1) > 0.60
- 自动搜索 LightGBM baseline 输出对比表

**无法完成的步骤：**
- SSH 连接 cqa1-22115 失败（"Error reading SSH protocol banner"），无法部署和 dry-run 验证
- 这是 AutoDL 实例重启后 SSH 端口变更的典型表现，请去 AutoDL 控制台确认新的 SSH 端口并更新 `~/.ssh/config`

**SSH 恢复后的部署命令：**
```bash
# 部署脚本
scp scripts/run_deberta_c4_1b5.py cqa1-22115:/root/autodl-tmp/gen-depth-contamination/scripts/

# 创建输出目录
ssh cqa1-22115 "mkdir -p /root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5"

# Dry-run 验证 (用 cuda:1)
ssh cqa1-22115 "cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python scripts/run_deberta_c4_1b5.py --config qwen_rw --gpu 0 --dry_run"
```

**训练启动命令（cross-transfer 完成后）：**
```bash
cd /root/autodl-tmp/gen-depth-contamination
CUDA_VISIBLE_DEVICES=1 nohup python scripts/run_deberta_c4_1b5.py --config qwen_rw --gpu 0 > results/exp_deberta_c4_1b5/qwen_rw.log 2>&1 &
CUDA_VISIBLE_DEVICES=2 nohup python scripts/run_deberta_c4_1b5.py --config pythia_greedy --gpu 0 > results/exp_deberta_c4_1b5/pythia_greedy.log 2>&1 &
CUDA_VISIBLE_DEVICES=3 nohup python scripts/run_deberta_c4_1b5.py --config qwen_cont256 --gpu 0 > results/exp_deberta_c4_1b5/qwen_cont256.log 2>&1 &
```

---
