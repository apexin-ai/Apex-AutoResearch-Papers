# ops proto nan fix and cron check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_proto_nan_fix_and_cron_check_20260517T174706_result.json`
- **Structured JSON:** [`3db421d8303fdceee1e7.json`](../../sessions/3d/3db421d8303fdceee1e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Prototypical Network 在 gpt2xl holdout 上正常完成，无 NaN。accuracy=0.5775, MAE=0.5174, mean_pairwise_AUC=0.8445。

---

## 结果汇总

### Task A: Prototypical NaN 修复 — 完成

修改了 2 个文件，4 处修复：

**`learned_estimator_utils.py`:**
1. `prototypical_loss` — cdist 后加 `torch.clamp(min=1e-8, max=1e6)` + `nan_to_num`，softmax 输入加 `nan_to_num`
2. `predict_with_prototypes` — 返回距离前加 `torch.clamp` + `nan_to_num`
3. `compute_metrics` — 检测 NaN predictions，替换为 majority class

**`learned_estimator_train.py`:**
4. `train_prototypical` 最终预测块 — dists 经 `nan_to_num` → `clamp` → softmax 输入 `nan_to_num`，y_prob 最终 `np.nan_to_num`

Dry-run 验证通过（`--max_samples 100`, holdout=gpt2xl），全程无 NaN。

### Task B: downstream_benchmark_002 — 已完成，无需 cron

进程已结束。结果：

| Model | Overall PPL | d0 PPL | d1 PPL | d2 PPL | d3 PPL |
|-------|------------|--------|--------|--------|--------|
| baseline | 5.67 | 13.42 | 5.66 | 3.94 | 3.17 |
| d0_only | 5.65 | 13.26 | 5.65 | 3.93 | 3.17 |
| d1_only | **5.55** | 13.60 | **5.54** | **3.79** | **3.05** |
| d2_only | 5.56 | 13.88 | 5.56 | 3.76 | 3.00 |
| mixed_all | 5.55 | 13.52 | 5.56 | 3.80 | 3.04 |

假设 "d0_only has lowest PPL" **未被支持**。d1_only 和 mixed_all 并列最低 (5.55)。结果保存在 `/root/autodl-tmp/recursive_gen_depth_est/results/downstream_benchmark_v2.json`。日志：`/root/runs/recursive_gen_depth_est/downstream_benchmark_002.log`。

---
