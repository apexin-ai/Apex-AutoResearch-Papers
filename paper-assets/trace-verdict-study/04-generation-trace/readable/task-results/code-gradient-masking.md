# code gradient masking

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_masking_20260522T074512_result.json`
- **Structured JSON:** [`65bc3507363e383437f9.json`](../../sessions/65/65bc3507363e383437f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 修改/新增文件

| 文件 | 操作 |
|------|------|
| `/root/trace-verdict-study/train/gradient_mask_trainer.py` | **新增** — `GradientMaskTrainer(SFTTrainer)` 子类，override `compute_loss` 实现 per-token loss masking |
| `/root/trace-verdict-study/train/train_sft.py` | **修改** — 添加 `--gradient_mask_ratio` 参数，ratio > 0 时自动切换到 `GradientMaskTrainer` |

### 2. Dry-run 结果

3 步训练成功完成，无报错。`train_loss=39.1`（符合预期：99.8% token 被 mask 后有效 loss 集中在极少 token 上，数值偏大）。

### 3. Gradient Masking 验证

**实际 mask 比例**（8 个 micro-batch）：

| valid tokens | kept | mask_ratio |
|-------------|------|------------|
| 2130 | 14 | 0.9934 |
| 1080 | 13 | 0.9880 |
| 2162 | 16 | 0.9926 |
| 835 | 13 | 0.9844 |
| 2970 | 17 | 0.9943 |
| 3579 | 20 | 0.9944 |
| 2050 | 13 | 0.9937 |
| 4374 | 21 | 0.9952 |

平均 mask ratio ≈ 0.992，接近目标 0.998。偏差来自 verdict token 保护（每序列固定保留 3 个 token）。

**Verdict 保护验证**：
- `shift_labels[338]` = "pass" → **PROTECTED**
- `shift_labels[339]` = `<|im_end|>` → PROTECTED  
- `shift_labels[340]` = `\n` → PROTECTED

### 4. 训练命令模板

```bash
cd /root/trace-verdict-study && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python train/train_sft.py \
    --condition exception_only \
    --gpu 0 \
    --gradient_mask_ratio 0.998 \
    --gradient_checkpointing \
    --max_steps 443 \
    --seed 42 \
    --wandb_run_name exception_only_gradmask0998_seed42 \
    --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_gradmask0998
```

---
