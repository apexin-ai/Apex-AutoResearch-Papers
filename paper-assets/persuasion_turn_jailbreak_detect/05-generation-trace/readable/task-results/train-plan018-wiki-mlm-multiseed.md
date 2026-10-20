# train plan018 wiki mlm multiseed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan018-wiki-mlm-multiseed_20260518T064551_result.json`
- **Structured JSON:** [`8ae729b5c8296b97d728.json`](../../sessions/8a/8ae729b5c8296b97d728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## Plan 018 Wiki MLM 3-seed 结果

| K | seed=42 | seed=123 | seed=456 | Mean | Std |
|---|---------|----------|----------|------|-----|
| **full** | 0.742 | 0.990 | 0.980 | **0.904** | 0.115 |
| k=1 | 0.822 | 1.000 | 0.917 | **0.913** | 0.073 |
| k=2 | 0.815 | 0.990 | 0.928 | **0.911** | 0.073 |
| k=3 | 0.849 | 0.990 | 0.970 | **0.937** | 0.062 |
| k=5 | 0.808 | 0.990 | 0.970 | **0.923** | 0.082 |
| IID full | 0.987 | 0.987 | 0.961 | **0.978** | 0.012 |

**关键发现：**
- Wiki MLM 3-seed DD OOD full: **0.904 ± 0.115**
- 对比 plan_016v2 topic 3-seed: **0.541 ± 0.207**
- Wiki MLM 明显更稳定、mean 更高
- seed=42 是明显 outlier（0.742 vs 其他两个 >0.98），可能是 GRU 训练不稳定导致
- IID 三个 seed 都很稳定（0.978 ± 0.012）

**已完成操作：**
1. 清理磁盘（移走旧 checkpoint 腾出 3.7GB）
2. 训练 seed=123 和 seed=456（均成功，val_loss ~8.1-8.2）
3. 评估两个新 seed 的 DD OOD + IID
4. 保存 3-seed 汇总到 `results/plan_018_wiki_mlm_3seed_summary.json`
5. Registry 已更新 plan_018_wiki_mlm_control 的 metrics

---
