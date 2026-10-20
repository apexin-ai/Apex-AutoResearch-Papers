# code pca control probe prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pca-control-probe-prep_20260515T143024_result.json`
- **Structured JSON:** [`2034484b0a6a39b0ec4f.json`](../../sessions/20/2034484b0a6a39b0ec4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验并行运行中：
- **action_prediction** PCA-1024: PID=617019, GPU 0, 全 33 层
- **action_delta** PCA-1024: PID=617371, GPU 1, 全 33 层

---

## 总结

### 已完成

1. **`train_probes.py` 修改**（`--pca_dim N` 参数）：
   - 新增 `apply_pca()` 函数，使用 sklearn PCA，仅在 train set 上 fit
   - 支持所有 probe types：action_prediction、action_delta、temporal_distance、subtask_predicate
   - 自动保存 `explained_variance_ratio` 到结果 JSON
   - output_dir 自动加 `_pca{N}` 后缀

2. **Dry-run 对比结果** (Layer 4, trained features)：

   | 指标 | Baseline (4096→256→7) | PCA-1024 (1024→256→7) |
   |---|---|---|
   | overall_r2 | 0.536 | **0.671** (+25%) |
   | mean_task_r2 | 0.543 | **0.679** (+25%) |
   | gripper_acc | 0.855 | **0.897** |
   | PCA variance | — | 99.85% |

   PCA 降维不仅没有降低性能，反而显著提升 — 去除了噪声维度。

3. **正式实验已启动**：两个全层实验在双 GPU 上并行运行，预计 ~1 小时完成。

### 启动命令参考

```bash
# action_prediction + PCA-1024
python3 scripts/train_probes.py \
  --features_dir features/trained/ \
  --output_dir results/trained/ \
  --probe_type action_prediction \
  --pca_dim 1024 \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/

# action_delta + PCA-1024
python3 scripts/train_probes.py \
  --features_dir features/trained/ \
  --output_dir results/trained/ \
  --probe_type action_delta \
  --pca_dim 1024 \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ \
  --gpu 1
```

### 查看进度

```bash
tail -f /tmp/pca1024_action_prediction.log
tail -f /tmp/pca1024_action_delta.log
```

---
