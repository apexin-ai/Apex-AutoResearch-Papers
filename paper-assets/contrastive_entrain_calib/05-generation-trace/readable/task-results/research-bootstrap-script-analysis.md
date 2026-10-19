# research bootstrap script analysis

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bootstrap-script-analysis_20260522T130058_result.json`
- **Structured JSON:** [`214361bf49771afbb47f.json`](../../sessions/21/214361bf49771afbb47f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

对比方式是 **d_syc vs best-of-200**（200 个随机方向中 CV AUROC 最高的那一个），不是 per-iteration max，也不是 mean。

### 具体逻辑

**1. `random_direction_oof` (L156-205)：** 生成 200 个随机方向，每个方向跑完整 5-fold CV，记录 mean CV AUROC。**只保留 AUROC 最高的那个方向的 OOF scores：**

```python
if mean_a > best_overall:
    best_overall = mean_a
    best_oof_syc = tmp_syc.copy()
    best_oof_wr = tmp_wr.copy()
```

返回值：`rand_stats`（200 个方向的统计量）+ `best_oof_syc, best_oof_wr`（最佳随机方向的 OOF 投影分数）

**2. `bootstrap_auroc_difference` (L133-155)：** 用同一组 bootstrap indices 分别算 d_syc 和 best-random 的 AUROC，取差值：

```python
for _ in range(n_bootstrap):
    idx = rng.choice(n, size=n, replace=True)
    scores_d = np.concatenate([oof_syc_d[idx], oof_wr_d[idx]])  # d_syc 的 OOF
    scores_r = np.concatenate([oof_syc_r[idx], oof_wr_r[idx]])  # best random 的 OOF
    a_d = roc_auc_score(labels, scores_d)
    a_r = roc_auc_score(labels, scores_r)
    diffs.append(a_d - a_r)
```

**3. main() 调用链：**

```python
rand_stats, rand_oof_syc, rand_oof_wr = random_direction_oof(syc_q, wr_q, ...)
diff_ci = bootstrap_auroc_difference(q_oof_syc, q_oof_wr, rand_oof_syc, rand_oof_wr, ...)
```

### 结论

| 项 | 值 | 含义 |
|---|---|---|
| d_syc OOF AUROC | 0.7588 | d_syc 方向的 OOF 点估计 |
| random mean AUROC | 0.6853 | 200 个随机方向的 CV AUROC 均值 |
| random max AUROC | 0.7980 | 200 个随机方向中最好的一个 |
| diff = -0.0094 | d_syc OOF - **best random OOF** | 对比的是最强随机方向，不是平均 |
| P(d_syc > random) = 0.29 | bootstrap 中 d_syc 赢 best random 的比例 | |

**问题在于：** JSON 里 `random_auroc = 0.6853` 是 200 个方向的 mean CV AUROC，但 diff 实际是拿 d_syc 的 OOF scores 和 best random 的 OOF scores 做的 paired bootstrap。这两个数字口径不一致——报告里看起来像 d_syc (0.7588) 比 random (0.6853) 高很多，但 diff 却是 -0.0094，原因就是 diff 比的是 max 方向而非 mean。

---
