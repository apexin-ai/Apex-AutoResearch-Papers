# infra oft baseline prep

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_oft-baseline-prep_20260519T234345_result.json`
- **Structured JSON:** [`628ab67abbf2b836a0ab.json`](../../sessions/62/628ab67abbf2b836a0ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

**脚本**: `/root/afford_invar/openvla-oft/vla-scripts/finetune.py` — 原始 OFT finetune，无 affordance decoder / L_consist / L_transfer。

**Dry-run 通过**：2 步完成，~29 秒，无报错。关键输出：
- 模型加载成功：`trainable params: 110,828,288 || all params: 7,652,065,472 || trainable%: 1.4483`
- action_head 参数：`151,117,831`，总可训练：`261,946,119`
- 数据集加载正常：`libero_goal_no_noops`
- `Max step 2 reached! Stopping training...`

**完整训练命令（20000 步）**：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/afford_invar/openvla-oft && \
CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled \
torchrun --nproc_per_node=1 --master_port=29503 \
  vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/openvla-7b \
  --data_root_dir /root/autodl-tmp/modified_libero_rlds \
  --dataset_name libero_goal_no_noops \
  --run_root_dir /root/afford_invar/runs \
  --lora_rank 32 \
  --batch_size 2 \
  --learning_rate 5e-4 \
  --max_steps 20000 \
  --save_freq 500 \
  --wandb_entity disabled \
  --wandb_project afford-invar
```

**参数说明**：
- 所有参数名与 `FinetuneConfig` dataclass 一致，draccus 直接解析 `--key value`
- `WANDB_MODE=disabled` + `--wandb_entity disabled`：原始脚本无条件调 `wandb.init`，必须通过环境变量禁用
- `master_port=29503`：避开 29501 (lconsist_cont) 和 29502 (transfer_v1)
- run 目录命名规则：`openvla-7b+libero_goal_no_noops+b2+lr-0.0005+lora-r32+dropout-0.0--image_aug`

---
