# code e3 cka heatmap prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e3_cka_heatmap_prep_20260518T120325_result.json`
- **Structured JSON:** [`82334a15ed25e2743a2f.json`](../../sessions/82/82334a15ed25e2743a2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并通过语法检查。

## 汇报

### 已创建的脚本

1. **`/root/recovery_aware_struct_prune/src/compute_layer_cka.py`** — 跨模型 layer-wise CKA 计算
   - 逐个加载模型提取 28 层 hidden states（mean-pooled over seq），然后释放显存
   - 支持 `--save_reprs_a` / `--load_reprs_a`，Dense 表征只需提取一次

2. **`/root/recovery_aware_struct_prune/src/plot_cka_heatmap.py`** — 多面板 CKA heatmap 可视化
   - 输入多个 JSON，自动排列 2×2 布局，magma colormap，标注 diagonal mean

### westb 可用 7B pruned 模型（5 个）

| 模型 | 路径 | intermediate_size |
|------|------|-------------------|
| CKA-Only 20% | `pruned_cka_only_20` | 8128 |
| Random 20% | `pruned_random_20` | 10832 |
| RASP-RLVR 20% | `pruned_rasp_rlvr_20` | 8128 |
| Gradient 20% | `pruned_gradient_20` | 8128 |
| Magnitude 20% | `pruned_magnitude_20` | 8128 |

所有模型 hidden_size=3584, 28 layers，可直接做 CKA 无需投影。**无 `pruned_standard_20` 7B 版本。**

### GPU 运行时间估计

- 每个模型加载 + 50 samples forward pass: ~3-4 min
- CKA matrix 计算 (28×28 = 784 pairs): ~10 sec
- **首次运行**（Dense + 1 pruned）: ~7-8 min
- **后续运行**（cached Dense + 1 pruned）: ~3-4 min
- **5 个 pruned 模型全跑**: ~25 min 总计

### 运行命令参考

```bash
PYTHON=/root/miniconda3/bin/python
OUT=/root/autodl-tmp/recovery_aware_struct_prune/cka_results
DENSE=/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B
PRUNED=/root/autodl-tmp/recovery_aware_struct_prune

# Run 1: dense + cka_only (save dense reprs)
$PYTHON src/compute_layer_cka.py --model_a $DENSE --model_b $PRUNED/pruned_cka_only_20 \
    --output $OUT/cka_cka_only_20.json --save_reprs_a $OUT/dense_reprs.pt --device cuda:0

# Run 2-5: reuse cached dense reprs
for m in random_20 rasp_rlvr_20 gradient_20 magnitude_20; do
    $PYTHON src/compute_layer_cka.py --load_reprs_a $OUT/dense_reprs.pt \
        --model_b $PRUNED/pruned_${m} --output $OUT/cka_${m}.json --device cuda:0
done

# Plot
$PYTHON src/plot_cka_heatmap.py \
    --inputs $OUT/cka_cka_only_20.json $OUT/cka_random_20.json $OUT/cka_rasp_rlvr_20.json $OUT/cka_magnitude_20.json \
    --labels "CKA-Only" "Random" "RASP-RLVR" "Magnitude" \
    --output $OUT/cka_heatmap.pdf
```

---
