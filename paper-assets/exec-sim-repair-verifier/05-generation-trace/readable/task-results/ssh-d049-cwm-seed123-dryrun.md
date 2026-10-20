# ssh d049 cwm seed123 dryrun

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d049-cwm-seed123-dryrun_20260513T094810_result.json`
- **Structured JSON:** [`a61a8f57069cc4f20507.json`](../../sessions/a6/a61a8f57069cc4f20507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 已清空，dry-run 目录已清理。汇报如下：

---

## Dry-Run 汇报

### 1. 超参确认 (D046)
| 参数 | 值 | 来源 |
|------|------|------|
| lr | 5e-5 | L185 `--lr` default |
| weight_decay | 0.01 | L188 `--weight_decay` default |
| warmup_ratio | 0.05 | L187 `--warmup_ratio` default |
| save_total_limit | 5 | L270 硬编码 |
| LoRA rank/alpha | 16/32 | L189-190 |
| batch_size × grad_accum | 1 × 32 = 32 effective | L183-184 |

### 2. Dry-Run 通过 (5 steps, seed=123, cuda:1)

| Step | Loss | Grad Norm | LR |
|------|------|-----------|----|
| 1 | 33.61 | 43.35 | 0 (warmup) |
| 2 | 36.60 | 46.61 | 5e-05 |
| 3 | 31.75 | 39.52 | 3.75e-05 |
| 4 | 32.62 | 42.15 | 2.5e-05 |
| 5 | **25.30** | 33.37 | 1.25e-05 |

- 平均 loss: 31.97，第 5 步明显下降
- 速度: ~8.7s/step (3.66 samples/sec)
- 模型: Qwen3-4B, trainable 0.29% (11.8M LoRA params)
- Attention: **sdpa**（flash_attn 未安装）
- 数据: train=70748, val=9335; train 截断 4.5%, **val 截断 20.2%**（较高）
- GPU 显存峰值: ~29GB / 32GB（5090 单卡足够）
- 无报错，训练日志输出 "Dry-run complete."

### 3. cuda:1 状态
0 MiB / 32607 MiB，空闲可用。

### 4. 推荐正式启动命令

```bash
cd /home/sonny/exec-sim-repair-verifier && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python3 -u train_repo_cwm.py \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_seed123/ \
  --seed 123 \
  --run_name repo-cwm-qwen3-4b-lora-seed123 \
  --save_steps 100 \
  --eval_steps 100 \
  2>&1' > /root/autodl-tmp/train_cwm_seed123.log 2>&1 &
echo $!
```

**注意事项**：
- output_dir 和 log 放 `/root/autodl-tmp/` 避免 /tmp 清理（dry-run 时 /tmp 被系统清理过）
- 未安装 flash_attn，当前用 sdpa；如需加速可先装 `flash-attn`
- val 截断率 20.2% 偏高，如需改善可考虑增大 `--max_seq_length`（当前 2048）

---
