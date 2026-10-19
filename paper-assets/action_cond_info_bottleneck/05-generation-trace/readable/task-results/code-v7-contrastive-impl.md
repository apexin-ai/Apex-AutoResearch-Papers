# code v7 contrastive impl

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v7-contrastive-impl_20260516T101046_result.json`
- **Structured JSON:** [`86eef826b58d9aaf9edd.json`](../../sessions/86/86eef826b58d9aaf9edd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正确。总结：

## 修改的文件和关键改动

| 文件 | 改动 |
|------|------|
| `acib/config.py` | 新增 `lambda_contrastive: float = 0.0` 字段 |
| `acib/losses.py` | 新增 `contrastive_loss()` 静态方法：计算两组 weights 的 cosine similarity 均值 |
| `acib/acib_policy.py` | ① `_cached_visual_tokens` 列表，hook 中缓存 detached visual tokens；② `_compute_contrastive_loss()` 方法：shuffle batch 内 instruction → 计算 shuffled lang condition → 对同一 visual tokens 跑两次 scorer → cosine sim loss；③ `forward()` 中在 training 且 `lambda_contrastive > 0` 时计算并加入 total loss |
| `scripts/train_acib.py` | `--lambda_contrastive` 参数（默认 0.0），传入 ACIBConfig，logging + 打印 |

## Pair 构造方案

使用 **batch 内 cyclic shift**：`perm = (arange(B) + randint(1,B)) % B`。对 `observation.language.tokens` 和 `attention_mask` 做 shuffle，保证：
- 零 fixed points（每个样本的 shuffled instruction 都与原 instruction 不同）
- 不需要额外 VLM forward——只需 `embed_language_tokens`（embedding lookup）+ 两次 scorer MLP forward
- Visual tokens 从 hook 缓存中取（detached），梯度只流经 scorer 参数

## Dry-run 验证结果

- `from acib.acib_policy import ACIBPolicy; from acib.losses import ACIBLoss` → **import OK**
- `ACIBConfig(lambda_contrastive=0.5)` → **正确创建**
- `python3 scripts/train_acib.py --help` → **`--lambda_contrastive` 参数显示正确**

## 训练命令

```bash
MUJOCO_GL=egl python3 scripts/train_acib.py \
    --model_id lerobot/smolvla_libero \
    --dataset_id lerobot/libero \
    --data_root /root/autodl-tmp/lerobot_data \
    --hidden_dim 64 \
    --alpha 0.01 \
    --beta 0.01 \
    --beta_warmup_steps 1000 \
    --mode soft \
    --condition_source language \
    --lambda_contrastive 0.5 \
    --lambda_ent 0.1 \
    --steps 20000 \
    --batch_size 64 \
    --lr 1e-4 \
    --gpu 0 \
    --output_dir outputs/acib_v7_contrastive \
    --seed 42 \
    --wandb_project acib \
    --wandb_run_name "v7-contrastive-lam0.5"
```

---
