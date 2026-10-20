# analysis heatmap eval v2 1000step

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_heatmap-eval-v2-1000step_20260520T002728_result.json`
- **Structured JSON:** [`f1e15852c5c98ea2dcbd.json`](../../sessions/f1/f1e15852c5c98ea2dcbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Heatmap Eval 结果 (phase1_transfer_v2, checkpoint-9000)

**注意：checkpoint-1000 不存在**（训练仅保留最近 4 个 checkpoint，save_steps=500，当前已轮换到 9000-10500）。使用最早可用的 checkpoint-9000 评估。

| 指标 | 值 | 判定阈值 | PASS/FAIL |
|------|-----|---------|-----------|
| hm_ent | **11.54 ± 0.16** | < 7.0 | **FAIL** |
| peak_dist | **82.9 ± 44.5 px** | < 40 px | **FAIL** |
| mass_ratio | **0.97 ± 0.26x** | > 1.5x | **FAIL** |
| topk_contain | 0.020 | — | ≈ random (0.019) |

样本数: 57 张, 覆盖 3 个 suite (libero_10/spatial/object), 每 task 3 demos  
LoRA: 已通过 PeftModel 正确加载并 merge（确认 transfer_proj 18688 params）

### 训练 hm_ent 轨迹佐证

| Step | hm_ent (训练) | 说明 |
|------|--------------|------|
| ~10 | 8.74 | 初始化 |
| ~200 | 5.33 | 瞬态尖峰 |
| **~1000** | **6.51** | Director 观察到的值 |
| 7500+ | 7.8-8.0 | 已回升 |
| 9000 eval | 11.54 | 接近 uniform (max=14) |

### 结论: **Overfitting → Path C**

hm_ent=6.5 在 step ~1000 是瞬态训练 artifact：
1. **不可持续** — 到 step 7500+ 训练 hm_ent 已回升到 7.8-8.0
2. **不可泛化** — held-out eval 的 11.54 接近 uniform（完全无空间结构）
3. **train/eval gap 巨大** — 训练 7.8 vs eval 11.5，decoder 记住了训练样本的模式但无法迁移

可视化路径: `/root/afford_invar/results/heatmap_eval_transfer_v2_ckpt9000/heatmap_viz_{0-5}.png`

---
