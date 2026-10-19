# code acib v4 aggregate kl

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib_v4_aggregate_kl_20260516T001841_result.json`
- **Structured JSON:** [`08e3967a0183744be1b8.json`](../../sessions/08/08e3967a0183744be1b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. losses.py diff

```diff
--- a/acib/losses.py (v3: per-token KL)
+++ b/acib/losses.py (v4: aggregate rate KL)
@@ -38,11 +38,13 @@
     @staticmethod
     def information_bottleneck_loss(
         logits: torch.Tensor, target_rate: float = 0.8
     ) -> torch.Tensor:
-        p = torch.sigmoid(logits)
-        q = target_rate
-        kl = (
-            p * torch.log(p / (q + 1e-8) + 1e-8)
-            + (1 - p) * torch.log((1 - p) / (1 - q + 1e-8) + 1e-8)
-        )
-        return kl.mean()
+        # v4: aggregate rate KL — constrain per-sample average retention rate ≈ target_rate,
+        # individual token weights can freely differentiate (fixes v3 scorer collapse)
+        p = torch.sigmoid(logits)           # [B, T]
+        mean_p = p.mean(dim=-1)             # [B] per-sample average retention rate
+        mean_p = mean_p.clamp(1e-7, 1 - 1e-7)
+        q = target_rate
+        kl = mean_p * torch.log(mean_p / q) + (1 - mean_p) * torch.log((1 - mean_p) / (1 - q))
+        return kl.mean()
```

### 2. train_acib.py — 无改动

已有 `--wandb_project`、`--wandb_run_name` 参数，`setup_wandb()` 初始化，每 100 步 scorer stats + wandb log。

### 3. v3 checkpoint

**不存在。** `acib_v3_train/` 和 `acib_v3_s_h64_s42/` 只有 `config.json`，无 `.pt` 文件。仅有的 checkpoint 在 `acib_s/checkpoint-5/` 和 `dryrun_norm_fix/checkpoint-20/`。

### 4. dry-run

- CPU dry-run 因 dtype 不匹配（BFloat16 权重 vs Float32 autocast on CPU）失败 — 不影响 GPU 训练
- 单独的 loss 单元测试全部通过：aggregate rate KL 行为正确，梯度正常

### 5. v4 启动命令

```bash
MUJOCO_GL=egl PYOPENGL_PLATFORM=egl HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache \
python scripts/train_acib.py \
    --model_id lerobot/smolvla_libero \
    --dataset_id lerobot/libero \
    --hidden_dim 64 \
    --alpha 0.01 \
    --beta 0.01 \
    --beta_warmup_steps 1000 \
    --mode soft \
    --top_k_ratio 0.8 \
    --steps 20000 \
    --batch_size 64 \
    --lr 1e-4 \
    --warmup_steps 1000 \
    --grad_clip 1.0 \
    --gpu 0 \
    --data_root /root/autodl-tmp/libero_dataset \
    --output_dir /root/acib/outputs/acib_v4_agg_kl \
    --seed 42 \
    --wandb_project acib_mvp \
    --wandb_run_name acib_v4_agg_kl
```

---
