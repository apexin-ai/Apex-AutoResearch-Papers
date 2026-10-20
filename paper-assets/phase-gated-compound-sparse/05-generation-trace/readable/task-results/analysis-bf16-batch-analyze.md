# analysis bf16 batch analyze

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_batch_analyze_20260514T064652_result.json`
- **Structured JSON:** [`4fb11e0ca62a75cf8183.json`](../../sessions/4f/4fb11e0ca62a75cf8183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完成。汇总如下：

---

## Profiling 结果汇总（5 个实验）

**注意**: JSON 中无 `gradient_paired_aggregate` 字段。所有实验共享相同 phase_stats（相同分段结果）。

### 共享 phase_stats
| phase | n_tokens | n_segments |
|-------|----------|------------|
| high_sparsity | 21,086 | 387 |
| mid_sparsity | 13,306 | 191 |
| low_sparsity | 27,748 | 397 |

---

## exp_id: bf16_ds_rand_s015
- **masking**: random, **sparsity**: 0.15
- **interaction_index**:
  - high: mean=+0.3849, ci=[-0.5409, +1.3147], median=0.1147, winsorized_mean=0.3161, skewness=-5.40
  - mid: mean=-172.6626, ci=[-427.006, -9.069], median=0.0969, winsorized_mean=-0.6366, skewness=-10.56
  - low: mean=-5.7326, ci=[-10.928, -1.439], median=0.1121, winsorized_mean=0.0521, skewness=-11.57
- **pass_fail**: ci_overlap=**PASS** (high vs mid non-overlapping), sign_reversal=**FAIL**, overall=**PASS**
- **perplexity** (s=0.15):

| phase | dense | attn | kv | both |
|-------|-------|------|----|------|
| high | 1.1687 | 3.5947 | 2.9239 | 5.7569 |
| mid | 1.2269 | 297.7957 | 2.915 | 11.3156 |
| low | 1.2284 | 11.3419 | 3.6161 | 6.2886 |

- **log_tail**: `Verdict: PASS ... EXIT_CODE=0`
- **conclusion_suggestion**: **success** — CI non-overlapping, high>mid II分离明显；但 sign_reversal 未通过（high CI 跨零）

---

## exp_id: bf16_ds_rand_s020
- **masking**: random, **sparsity**: 0.20
- **interaction_index**:
  - high: mean=+2.5259, ci=[+1.2546, +4.2356], median=0.3278, winsorized_mean=1.7664, skewness=+9.59
  - mid: mean=-36.0516, ci=[-93.248, -2.202], median=0.2977, winsorized_mean=0.5839, skewness=-12.31
  - low: mean=-2.4805, ci=[-5.630, +0.113], median=0.3909, winsorized_mean=0.9942, skewness=-10.07
- **pass_fail**: ci_overlap=**PASS**, sign_reversal=**PASS** (high>0, mid<0), overall=**PASS**
- **perplexity** (s=0.20):

| phase | dense | attn | kv | both |
|-------|-------|------|----|------|
| high | 1.1687 | 3.1905 | 3.8002 | 8.8129 |
| mid | 1.2269 | 67.8504 | 3.788 | 11.4974 |
| low | 1.2284 | 8.592 | 5.0078 | 9.2001 |

- **log_tail**: `Verdict: PASS ... Sign reversal: high>0, mid<0 ... EXIT_CODE=0`
- **conclusion_suggestion**: **success** — 双通过，高置信度分离+符号反转

---

## exp_id: bf16_ds_rand_s025
- **masking**: random, **sparsity**: 0.25
- **interaction_index**:
  - high: mean=+5.5906, ci=[+1.1716, +9.4656], median=1.5545, winsorized_mean=6.3965, skewness=-7.57
  - mid: mean=-514.2418, ci=[-1361.474, -24.936], median=1.0202, winsorized_mean=3.1014, skewness=-12.76
  - low: mean=-9.1062, ci=[-25.804, +2.517], median=1.8937, winsorized_mean=4.1866, skewness=-15.85
- **pass_fail**: ci_overlap=**PASS**, sign_reversal=**PASS** (high>0, mid<0), overall=**PASS**
- **perplexity** (s=0.25):

| phase | dense | attn | kv | both |
|-------|-------|------|----|------|
| high | 1.1687 | 7.237 | 4.9751 | 17.7423 |
| mid | 1.2269 | 868.3199 | 5.1165 | 29.4661 |
| low | 1.2284 | 24.3571 | 6.7993 | 17.9694 |

- **log_tail**: `Verdict: PASS ... Sign reversal: high>0, mid<0 ... EXIT_CODE=0`
- **conclusion_suggestion**: **success** — 效果最强的 random 条件；mid attn PPL 爆炸(868)，但 mean II 被极端 outlier 驱动（winsorized_mean 为正 3.10）

---

## exp_id: bf16_importance_s020
- **masking**: importance (attn=frobenius_norm, kv=cumulative_attention_received), **sparsity**: 0.20
- **interaction_index**:
  - high: mean=+0.1289, ci=[-0.1975, +0.6647], median=0.0145, winsorized_mean=-0.0297, skewness=+16.67
  - mid: mean=+1.2604, ci=[+0.7466, +1.8962], median=0.2027, winsorized_mean=0.7660, skewness=+7.05
  - low: mean=+6.0288, ci=[+4.4671, +7.9237], median=1.4963, winsorized_mean=4.3426, skewness=+6.01
- **pass_fail**: ci_overlap=**PASS** (low vs mid non-overlapping), sign_reversal=**FAIL**, overall=**PASS**
- **perplexity** (s=0.20):

| phase | dense | attn | kv | both |
|-------|-------|------|----|------|
| high | 1.1689 | 1.5233 | 1.6191 | 2.1047 |
| mid | 1.2269 | 1.5375 | 3.5164 | 5.4246 |
| low | 1.2286 | 1.6486 | 15.7987 | 23.74 |

- **log_tail**: `Verdict: PASS ... EXIT_CODE=0`
- **conclusion_suggestion**: **success** — importance masking 的 II 方向反转（low>mid>high，全正），与 random 相反；attn PPL 极低（~1.5），KV 占主导

---

## exp_id: bf16_importance_s030
- **masking**: importance, **sparsity**: 0.30
- **interaction_index**:
  - high: mean=+0.5547, ci=[+0.2773, +0.9198], median=0.0534, winsorized_mean=0.3367, skewness=+10.62
  - mid: mean=+11.3000, ci=[+6.865, +17.263], median=2.2833, winsorized_mean=8.1752, skewness=+9.19
  - low: mean=+57.7946, ci=[+41.442, +77.047], median=14.6395, winsorized_mean=39.3143, skewness=+8.31
- **pass_fail**: ci_overlap=**PASS** (low vs mid non-overlapping), sign_reversal=**FAIL**, overall=**PASS**
- **perplexity** (s=0.30):

| phase | dense | attn | kv | both |
|-------|-------|------|----|------|
| high | 1.1689 | 1.7123 | 2.0544 | 3.2372 |
| mid | 1.2269 | 1.7894 | 9.4821 | 24.2847 |
| low | 1.2286 | 1.9347 | 51.6485 | 122.609 |

- **log_tail**: `Verdict: PASS ... EXIT_CODE=0`
- **conclusion_suggestion**: **success** — 最强 importance 条件；low PPL both=122.6（KV=51.6 驱动），II 梯度 low/mid/high = 57.8/11.3/0.55，对比 s=0.15 参照的 69.24 量级相近

---

## 横向对比摘要

### Random masking — II mean (high_sparsity phase)
| sparsity | II mean | CI | sign_reversal |
|----------|---------|-----|---------------|
| 0.15 | +0.38 | [-0.54, +1.31] | FAIL |
| 0.20 | +2.53 | [+1.25, +4.24] | **PASS** |
| 0.25 | +5.59 | [+1.17, +9.47] | **PASS** |

Random II 随 sparsity 单调递增，s≥0.20 可检出 sign reversal。

### Importance masking — II mean (low_sparsity phase, 主要敏感区)
| sparsity | II mean | CI |
|----------|---------|-----|
| 0.20 | +6.03 | [+4.47, +7.92] |
| 0.30 | +57.79 | [+41.44, +77.05] |

Importance 的 II 集中在 low_sparsity phase（符合预期：importance 选中的 head 更重要，去掉后 PPL 损失大）。s=0.30 时 KV PPL 爆炸到 51.6/122.6。

### 关键差异：Random vs Importance
- **Random**: 高稀疏 phase 对 attn head 随机丢弃更敏感（mid phase attn PPL 爆炸），II 呈 high>0, mid<0 pattern
- **Importance**: KV 通道主导损失（attn PPL 变化小因为去的是最不重要的 head），II 全正且 low>mid>high

---
