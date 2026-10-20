## Scoring 差异调查报告

### 1. per_layer_intermediate_size 对比

| Layer | westb (Standard) | westd (α=0.0) | 差异 |
|-------|-----------------|---------------|------|
| L0–L5 | 8128 | 8128 | — |
| L6–L15 | 18944 | 18944 | — |
| L16 | 14212 | 14212 | — |
| L17 | 16240 | 16240 | — |
| L18 | 14212 | 14212 | — |
| L19 | 8128 | 8128 | — |
| **L20** | **17592 (26 groups)** | **16916 (25 groups)** | **+676 (+1 group)** |
| L21 | 13536 | 13536 | — |
| L22 | 16240 | 16240 | — |
| L23–L25 | 8128 | 8128 | — |
| **L26** | **13536 (20 groups)** | **14212 (21 groups)** | **−676 (−1 group)** |
| L27 | 18944 | 18944 | — |

总容量相同（200 MLP groups pruned, 0 attn groups pruned, sparsity ≈ 19.1%）。

**注：westd 上也有 `pruned_standard_20`，其结构与 westb 完全一致（L20=17592, L26=13536）。差异仅出现在 α=0.0 ablation 模型中。**

### 2. 差异根因：Calibration Data 非确定性

**根因是 `importance_scores.pt` 不同。** 两台服务器独立计算了 importance scores：

| | westb | westd |
|---|---|---|
| importance_scores.pt md5 | `e4c78d60...` | `99130fd0...` |
| cka_scores.pt md5 | `1f327cc9...` | `6c0713c8...` |
| 生成时间 | 2026-05-14 14:11 | 2026-05-15 15:37 |
| GPU | RTX PRO 6000 Blackwell | RTX PRO 6000 Blackwell |
| Driver | 595.58.03 | 580.119.02 |
| 代码 (prune.py md5) | `3a5257b8...` | `3a5257b8...` ✓ 一致 |
| 代码 (importance_score.py md5) | `1df5ab2c...` | `1df5ab2c...` ✓ 一致 |

同一代码、同一 GPU 架构、同一 seed(42)，但不同 driver 版本 → 浮点运算非确定性 → importance scores 有微小差异（典型 ~0.01–0.05%）。

**边界处的翻转：**

具体翻转发生在 **L20 g27** 和 **L26 g5** 两个 group 之间：

| Group | westb score | westd score | westb 决策 | westd 决策 |
|-------|------------|------------|-----------|-----------|
| L20 g27 | 0.01618 | 0.01614 | KEPT | **PRUNED** |
| L26 g5 | 0.01611 | 0.01619 | **PRUNED** | KEPT |

- westb: L26 g5 (0.01611) < L20 g27 (0.01618) → L26 g5 被 prune
- westd: L20 g27 (0.01614) < L26 g5 (0.01619) → L20 g27 被 prune

两者间 score gap 仅 ~0.00007–0.00005，被 calibration noise 翻转。

**完整 group 差异：**

| Layer | westb pruned groups | westd α=0.0 pruned groups | 差异 |
|-------|-------------------|-------------------------|------|
| L20 | [1, 8] | [1, 8, **27**] | westd 多剪了 g27 |
| L26 | [**5**, 6, 7, 9, 12, 16, 20, 25] | [6, 7, 9, 12, 16, 20, 25] | westb 多剪了 g5 |

### 3. 代码路径分析

α=0 时的 RASP scoring 路径（prune.py L200–205）：
```python
attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(0.0)
#                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                               = 1.0 for any finite float
```

`(1.0 - x).pow(0.0)` 在 float32 下对任何有限值 x 都返回 1.0。因此：
- RASP α=0 score = `importance * 1.0` = importance
- Standard score = importance

**数学上完全等价。** 代码路径虽然不同（rasp 路径多加载了 CKA 文件、多一次乘法），但最终 score 值完全相同（前提是同一个 importance_scores.pt）。

### 4. 结论

| 问题 | 回答 |
|------|------|
| α=0 是否等价于 standard pruning？ | **代码逻辑等价。** 给定相同 importance scores，产出完全一致。 |
| 差异来源？ | **两台服务器独立计算了 importance scores。** 不同 driver 版本导致浮点非确定性，在 pruning 边界翻转了 1 个 group 的去留。 |
| 需要统一代码路径吗？ | **不需要。** 代码路径已经正确。问题在于输入数据不一致。 |
| 论文中 "α=0 reduces to standard pruning" 需要 caveat 吗？ | **不需要。** 该表述数学上正确。但实验报告中应注明 alpha ablation 使用了 westd 独立计算的 importance scores，因此 α=0 的结果与 westb 的 standard baseline 存在微小结构差异（±1 group / ±676 channels at L20 & L26）。这不影响结论的有效性，因为总剪枝量和 sparsity 完全相同。 |

**建议：** 如果需要 ablation 结果与 baseline 严格可复现一致，应确保所有 pruning 实验使用同一份 importance_scores.pt（通过 rsync/scp 复制而非重新计算）。
