# ssh d049 cls 8b dryrun

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d049-cls-8b-dryrun_20260513T094824_result.json`
- **Structured JSON:** [`093503587e16cebb33af.json`](../../sessions/09/093503587e16cebb33af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 汇报

| 项目 | 结果 |
|------|------|
| **8B 脚本** | 已在 westd-48478，无需同步（11418 bytes, 2026-05-13 17:01） |
| **Qwen3-8B 模型** | 已缓存 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`（完整 5 shards） |
| **Dry-run 5 steps** | 通过，无报错 |
| **cuda:3** | 已释放，0 MiB / 32607 MiB |

### 训练指标

| Step | Loss | Grad Norm | LR |
|------|------|-----------|-----|
| 1 | 195.8 | 442.4 | 0 (warmup) |
| 2 | 368.5 | 891.0 | 5e-5 |
| 3 | 249.6 | 602.9 | 3.75e-5 |
| 4 | 299.3 | 800.8 | 2.5e-5 |
| 5 | 241.6 | 722.3 | 1.25e-5 |

- **平均 loss**: 271.0，**速度**: 9.27s/it (3.45 samples/s)
- **GPU 显存峰值**: 25741 MiB / 32607 MiB (79%)
- **LoRA**: 15.3M trainable / 8.2B total (0.19%)
- **Attention**: SDPA（flash-attn 未安装）
- **数据**: train=70748 (3.8% 截断), val=9335 (20.2% 截断)

### 注意事项
1. **需要离线模式**：服务器网络不通 HuggingFace，必须用 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` + 本地路径
2. **val 截断率 20.2%** 偏高，可考虑增大 `max_seq_length`（当前 2048）
3. **loss 偏大**（~200-370）——这是 weighted CE + 累积 grad_accumulation=32 的效果，正常

### 推荐启动命令

```bash
cd /home/sonny/exec-sim-repair-verifier && \
nohup bash -c 'export HF_HUB_OFFLINE=1; export TRANSFORMERS_OFFLINE=1; \
CUDA_VISIBLE_DEVICES=3 python3 train_repo_verifier_8b.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/ \
  --seed 42' \
> /tmp/cls_8b_train.log 2>&1 & echo $!
```

---
