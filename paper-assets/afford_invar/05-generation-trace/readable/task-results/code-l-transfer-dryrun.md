# code l transfer dryrun

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l-transfer-dryrun_20260519T225748_result.json`
- **Structured JSON:** [`251cc836d31fd6cf9186.json`](../../sessions/25/251cc836d31fd6cf9186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果报告：**PASS**

---

### 1. FinetuneAffordTransferConfig 完整参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `vla_path` | openvla/openvla-7b | |
| `data_root_dir` | datasets/rlds | |
| `dataset_name` | libero_spatial_no_noops | |
| `batch_size` | 2 | |
| `learning_rate` | 5e-4 | |
| `max_steps` | 200000 | |
| `save_freq` | 10000 | |
| `lora_rank` | 32 | |
| `beta` | 0.1 | L_transfer 权重 |
| `lambda_H` | 0.01 | entropy 权重 |
| `transfer_temperature` | 0.07 | InfoNCE temperature |
| `queue_size` | 256 | 特征队列 |
| `max_negatives` | 64 | 每 anchor 最多负样本 |
| `sim_threshold` | 0.85 | 正对阈值 |
| `layer_idx` | 18 | LLM 层特征 |
| `siglip_path` | /root/autodl-tmp/siglip-base-local | |
| `pair_index_path` | "" | 空则自动构建 |
| `afford_mid_dim` | 256 | |
| `afford_output_size` | 128 | |

**注意：** 无 `alpha`、无 `num_paraphrases` 参数。此脚本是 Path B（L_transfer 替代 L_consist），无 L_consist。

### 2. 代码修改

添加了 `transfer_pos_count`（`valid.sum().item()`）到 metrics dict（line 403）和 console 输出（line 490）。

### 3. Pair Index 预计算结果

- 718 unique instructions
- **30,796 positive pairs**（threshold=0.80）
- 自动保存到 `runs/libero_goal_no_noops+transfer+b2+lr0.0005+beta0.1/pair_index.pkl`

### 4. 每步 Loss 表格

| Step | L_action | L_transfer | H_ent | L_total | pos | Q |
|------|----------|------------|-------|---------|-----|---|
| 0 | 0.6250 | 0.000000 | -8.6538 | 0.6250 | 0 | 2 |
| 1 | 4.5000 | 0.000000 | -8.7437 | 4.5000 | 0 | 4 |
| 2 | 3.8438 | 0.000000 | -8.8036 | 3.8438 | 0 | 6 |
| 3 | 1.8281 | 0.000000 | -8.7493 | 1.8281 | 0 | 8 |
| 4 | 1.5000 | **1.5854** | -8.4218 | 1.6585 | **2** | 10 |
| 5 | 1.0781 | **1.3475** | -8.6060 | 1.2129 | **1** | 12 |

### 5. GRAD MONITOR 输出（step 0）

```
L_transfer=0.000000 | transfer_grad_norm=0.000000 | total_grad_norm=36.031314 | grad_ratio=0.0000 | queue_len=2
```

Step 0 队列只有 2 样本无正对，符合预期。GRAD MONITOR 每 100 步触发一次，5-step 内仅 step 0。

### 6. Extended metrics（step 0）

```
lora_gnorm=6.2826  dec_gnorm=0.0000  hm_mean=0.000061  hm_std=0.000150  hm_max=0.004235  hm_ent=8.65
```

### 7. 判定

| 检查项 | 结果 |
|--------|------|
| L_transfer 非 0/NaN | ✅ step 4-5 值 ~1.3-1.6（合理 InfoNCE 范围） |
| transfer_pos_count > 0 | ✅ step 4: pos=2, step 5: pos=1 |
| L_action/L_transfer/L_entropy 分别记录 | ✅ |
| hm_ent/hm_max 输出 | ✅ |
| GRAD MONITOR 存在 | ✅ |
| 无 OOM/NaN/崩溃 | ✅ |

**PASS** — L_transfer 在队列填充后（step 4, Q>=10）正确激活，InfoNCE loss 值合理。

### 8. 全训练启动命令

```bash
cd /root/afford_invar/openvla-oft
CUDA_VISIBLE_DEVICES=1 torchrun --nproc_per_node=1 --master_port=29502 \
  vla-scripts/finetune_afford_transfer.py \
  --vla_path /root/autodl-tmp/openvla-7b \
  --data_root_dir /root/autodl-tmp/modified_libero_rlds \
  --dataset_name libero_goal_no_noops \
  --run_root_dir /root/afford_invar/runs \
  --lora_rank 32 --batch_size 2 --learning_rate 5e-4 \
  --max_steps 200000 --save_freq 10000 \
  --paraphrases_path /root/afford_invar/data/paraphrases.json \
  --layer_idx 18 --lambda_H 0 \
  --beta 0.1 --transfer_temperature 0.07 --queue_size 256 \
  --sim_threshold 0.80 \
  2>&1 | tee /root/afford_invar/results/phase1_transfer.log
```

---
