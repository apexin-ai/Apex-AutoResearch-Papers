# code prep act 256

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-act-256_20260525T151431_result.json`
- **Structured JSON:** [`f3342a27efa8289b89a2.json`](../../sessions/f3/f3342a27efa8289b89a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

---

## 环境验证报告

| 项目 | 状态 | 详情 |
|------|------|------|
| 训练脚本 | ✅ | `/root/contrastive_entrain_calib/training/run_act_256_ablation.py` |
| 数据 | ✅ | `data/calibration_v2_1_256.jsonl` — 256 行 = 128 pairs（预采样子集，非运行时采样） |
| Base model | ✅ | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/` — 5 shards 完整 |
| LoRA 配置 | ✅ | r=64, alpha=64, modules=[q,k,v,o], dropout=0 |
| ACT loss | ✅ | SFT + 0.1×L2 activation distance, layers [19,20,24,27,32,33,35] |
| 包版本 | ✅ | torch=2.8.0+cu128, transformers=4.57.6, peft=0.19.1, trl=1.4.0 |
| 磁盘 | ✅ | `/root/autodl-tmp/` 160GB 可用，LoRA checkpoints ~2GB 足够 |

### 上次 kill 情况
- 跑到 step 200/8000 被 kill（GPU 满），无 checkpoint 保存（首次 save 在 step 500）
- 训练曲线健康：total_loss 从 2.88 → 0.72 稳步下降
- 旧 `train_log.jsonl` 残留在 output_dir，需清理（脚本用 append 模式）

### 关键差异
- 上次 `CUDA_VISIBLE_DEVICES=1`，这次改 `CUDA_VISIBLE_DEVICES=0`
- 脚本内 `device = torch.device("cuda:0")`，通过环境变量映射物理 GPU

### 预估
- 训练速度：~6.6s/step → 8000 steps ≈ **14.7 小时**
- Checkpoint 产出：`/root/autodl-tmp/checkpoints/act_256_ablation/checkpoint-{500,1000,...,8000}/` + `final/`

---

### 提交命令（复制粘贴）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && rm -f /root/autodl-tmp/checkpoints/act_256_ablation/train_log.jsonl && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python training/run_act_256_ablation.py
```

---
