# code pca linear probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pca_linear_probe_20260515T192049_result.json`
- **Structured JSON:** [`97cda3f92c6f1e9d4a26.json`](../../sessions/97/97cda3f92c6f1e9d4a26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本功能完全正确。总结：

**脚本**: `/root/vla-ssd/pca_linear_probe_gc.py` (413 行)

**Layer 1 dry-run 结果**:
| 指标 | 值 |
|------|-----|
| Accuracy | 99.99% |
| Traj accuracy | 100% |
| Macro F1 | 0.9999 |
| Selectivity | 0.841 (task 99.99% - control 15.85%) |
| Bin 0 accuracy | 99.92% |
| PCA explained variance | 99.96% |

**发现**: PCA 从 4096→1024 后，1024 个主成分保留了 99.96% 的方差。即便用 linear probe（非 MLP），trained VLA layer 1 仍然 99.99% accuracy。维度降低并没有打破区分性——10-way goal classification 确实太容易了。

**DINO 实际路径**: `dinov2_libero_goal`（非 `dino_libero_goal`）

**运行完整实验的命令**:
```bash
# Trained VLA (all 33 layers)
python pca_linear_probe_gc.py --model_type trained --feature_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --pca_dim 1024

# Untrained VLA
python pca_linear_probe_gc.py --model_type untrained --feature_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --pca_dim 1024

# DINO (no PCA, already 1024 dim)
python pca_linear_probe_gc.py --model_type dino --feature_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/
```

注意每层约需 2-3 分钟（PCA + 7 次 LR fit），33 层全跑约 1-1.5 小时。`n_jobs` 参数可以去掉以消除 FutureWarning（sklearn 1.8 不再支持，不影响功能）。

---
