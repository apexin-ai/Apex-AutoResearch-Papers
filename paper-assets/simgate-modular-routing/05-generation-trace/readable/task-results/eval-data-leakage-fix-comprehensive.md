# eval data leakage fix comprehensive

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_data-leakage-fix-comprehensive_20260515T223110_result.json`
- **Structured JSON:** [`99430b067c3c8ccb0a4f.json`](../../sessions/99/99430b067c3c8ccb0a4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。下面是完整汇报。

---

## 任务 1：Data Split Seed 调查结果

### 根本问题：三重不匹配

代码库中存在 **三种不同的 data split 算法**：

| 出处 | 方法 | n_val | 算法 |
|------|------|-------|------|
| 训练 `load_implicit_sft_data` | 按 task_type 分组 → `random.Random(seed).shuffle()` → 前 15% | **305** | per-task stratified |
| Eval `routing_eval_sft.py` | 按 (task_type, variation) episode → `sklearn.train_test_split` | **300** | episode stratified |
| Eval `eval_ablation_b_gen.py` | 全量 `random.shuffle()` → 后 15% | **306** | flat random |

训练的 `--seed X` 同时控制 model init 和 data split。

### 完整 12 行对照表

| Checkpoint | Model | Training split seed | Eval split seed | Seed匹配 | 算法匹配 | 旧 bal_acc |
|------------|-------|--------------------|--------------------|--------|----------|-----------|
| plan-008-qwen3-1.7b | 1.7B | 42 | 42 | YES | **NO** | 0.3759 |
| seed-robustness-seed43 | 1.7B | 43 | 43 | YES | **NO** | 0.4574 |
| seed-robustness-seed44 | 1.7B | 44 | **42** | **NO** | **NO** | 0.6833 |
| seed-robustness-seed45 | 1.7B | 45 | **42** | **NO** | **NO** | 0.6037 |
| plan-008-v4-0_6b-seed42 | 0.6B | 42 | 42 | YES | **NO** | 0.6241 |
| plan-008-v4-0_6b-seed43 | 0.6B | 43 | **42** | **NO** | **NO** | 0.5574 |
| plan-008-v4-0_6b-seed44 | 0.6B | 44 | 44 | YES | **NO** | 0.6907 |
| plan-008-v4-0_6b-seed45 | 0.6B | 45 | 45 | YES | **NO** | 0.7333 |
| plan-008-v4-4b-seed42 | 4B | 42 | 42 | YES | **NO** | 0.6241 |
| plan-008-v4-4b-seed43 | 4B | 43 | **42** | **NO** | **NO** | 0.5463 |
| plan-008-v4-4b-seed44 | 4B | 44 | 44 | YES | **NO** | 0.6556 |
| plan-008-v4-4b-seed45 | 4B | 45 | 45 | YES | **NO** | 0.7000 |

- **所有 12 个 eval 都有 split 算法不匹配**（eval 用 sklearn episode-level split，训练用 per-task split）
- **4 个额外有 seed 不匹配**（1.7B s44/s45，0.6B s43，4B s43）

---

## 任务 2：修正后的 4-seed × 3 模型对比

使用 `corrected_eval.py`：**与训练完全相同的 `load_implicit_sft_data` split 函数 + 正确的 training seed**，n_val=305。

```
=== 修正后的完整 4-seed 三模型对比 ===
| Model | s42    | s43    | s44    | s45    | Mean±Std       |
|-------|--------|--------|--------|--------|----------------|
| 0.6B  | 0.5470 | 0.5858 | 0.5238 | 0.5989 | 0.5639±0.0346  |
| 1.7B  | 0.5706 | 0.6399 | 0.5543 | 0.5614 | 0.5816±0.0395  |
| 4B    | 0.5512 | 0.6328 | 0.5778 | 0.6069 | 0.5922±0.0354  |
```

### 与旧结果对比（关键变化）

| Model | Metric | Old range | New range | 变化 |
|-------|--------|-----------|-----------|------|
| 1.7B | s42 | 0.3759 | **0.5706** | +19.5pp ↑ |
| 1.7B | s43 | 0.4574 | **0.6399** | +18.3pp ↑ |
| 1.7B | s44 | 0.6833 | **0.5543** | -12.9pp ↓ |
| 1.7B | s45 | 0.6037 | **0.5614** | -4.2pp ↓ |
| 1.7B | std | 0.1341 | **0.0395** | 方差缩小 3.4× |

修正后 1.7B 的 seed 间方差从 13.4pp 降至 4.0pp，印证了旧 eval 的异常波动来自 data leakage。

---

## 任务 3：Table 7 (Appendix E) 统一 pipeline

### 数据来源

| Seed | 来源文件 | Eval 方法 | bal_acc |
|------|---------|----------|---------|
| 42 | `seed_robustness/summary.json` | `eval_routing_metrics.load_val_split` (**非** generation eval) | 0.5761 |
| 123 | `results/ablation_b_seed123_gen.json` | generation eval (flat random split, seed=42) | 0.5736 |
| 456 | `results/ablation_b_seed456_gen.json` | generation eval (flat random split, seed=42) | 0.5748 |
| 789 | `results/ablation_b_seed789_gen.json` | generation eval (flat random split, seed=42) | 0.5831 |

**问题**：seed 42 用了 `eval_routing_metrics`（非 generation eval），其余 3 个用了 generation eval。

### 修正

Seed 42 checkpoint = `plan-004-implicit/final_adapter`。Generation eval 已存在于 `results/ablation_b_gen_eval.json`，使用与 123/456/789 相同的 pipeline（flat random split, seed=42, enable_thinking=False）。

```
=== Table 7 fixed-split 统一 pipeline ===
| Seed | balanced_acc (generation eval) | 确认方式 |
|------|-------------------------------|---------|
| 42   | 0.5927                        | 已有 ablation_b_gen_eval.json |
| 123  | 0.5736                        | 确认 (generation eval) |
| 456  | 0.5748                        | 确认 (generation eval) |
| 789  | 0.5831                        | 确认 (generation eval) |
| Mean±Std | 0.5811±0.0089             |         |
```

---

## 4. 需作废的 eval 结果清单

### 全部作废（split 算法不匹配导致 data leakage）

**plan-008-v4 目录下 12 个文件**（已替换为 `*_fixed.json`）：
1. `0_6b_seed42_nothinking.json`
2. `0_6b_seed43_nothinking.json` — 还有 seed 不匹配
3. `0_6b_seed44_nothinking.json`
4. `0_6b_seed45_nothinking.json`
5. `1_7b_seed42_nothinking.json`
6. `1_7b_seed43_nothinking.json`
7. `1_7b_seed44_nothinking.json` — 还有 seed 不匹配
8. `1_7b_seed45_nothinking.json` — 还有 seed 不匹配
9. `4b_seed42_nothinking.json`
10. `4b_seed43_nothinking.json` — 还有 seed 不匹配
11. `4b_seed44_nothinking.json`
12. `4b_seed45_nothinking.json`

**Table 7 seed 42 值**：
13. `seed_robustness/summary.json` 中 `balanced_acc: 0.5761` — 用了非 generation eval pipeline → 应替换为 0.5927

**`seed_robustness/summary.json` 中其他 seed 值**（0.4852, 0.6074, 0.5467）也使用了不同于训练的 split 算法，但这些 seed 在 Table 7 中未使用，仅影响内部 summary。

---
