# investigate D016 alpha eff changes

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_D016_alpha_eff_changes_20260514T171519_result.json`
- **Structured JSON:** [`772f58a022261e4c7e4b.json`](../../sessions/77/772f58a022261e4c7e4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D016 调查结论

### 核心发现：D012 只改了 n_min，early return 不是行为变更

**证据汇总：**

#### 1. n_min 变更（唯一实质变更）

| | v1 (adaptive_seed*) | v2 (adaptive_fix_seed*) |
|---|---|---|
| config.json n_min | 3 | 2 |
| 同一 batch (seed123, step0, mean_q=0.678) | b=0.44, ESS=3.02, α_eff=0.47 | b=1.82, ESS=2.01, α_eff=0.58 |

行为差异完全由 n_min 解释：ESS 约束放松后 b 可以更大。

#### 2. `alpha_0 >= tau → return 0` early return 是数学上的空操作

当前 `find_optimal_b` 第 94-96 行有此 early return。但即使**删除它**，网格搜索在 b=0 处就会发现 `alpha_eff(0) = alpha_0 >= tau`，设 `threshold_b = 0`，二分法在 [0, 0] 区间收敛到 b=0。结果完全相同。

v1 的 b=0 实例证实了这一点：`step 6102, b=0.0, alpha_eff=0.877, ESS=4.0`——alpha_0 > tau 时 v1 也返回 b=0。

#### 3. D016 的 "78% b=0" 是 eval 数据污染

| | v1 | v2 |
|---|---|---|
| step_metrics 总行数 | 24,412 | 30,494 |
| 其中 eval 条目 (mean_q=0.0) | 0 | ~25,194 |

v2 开启了 eval（`--eval_data_path`），eval 数据没有 q_score 字段（默认 0.0），导致 alpha_0=1.0 > tau → b=0。这些 eval 条目混入 step_metrics，膨胀了 b=0 的统计。

**过滤 eval 后**：v1 训练 b=0 ≈ 459/24,412 = **1.9%**，v2 训练 b=0 ≈ 92/5,300 ≈ **1.7%**。基本一致。

#### 4. EMA 未实现

D012 计划"n_min=2 + EMA 平滑 b*"，但 `alpha_eff.py` 和 `pretrain_weighted.py` 中无任何 EMA/smooth/b_prev 代码。EMA 被规划但未落地。

#### 5. `pretrain_weighted.py` 增加了 `unweighted_loss` 日志

v1 step_metrics 无 `unweighted_loss` 字段，v2 有。纯日志变更，不影响算法。

### 变更清单

| 变更 | 归属 | 影响 |
|------|------|------|
| n_min 3→2 | D012 | **唯一实质行为变更** |
| `alpha_0 >= tau → return 0.0` early return | 不确定是否 D012 引入 | **无行为影响**（与网格搜索数学等价） |
| `unweighted_loss` 日志 | D012 同期 | 仅日志 |
| EMA 平滑 | D012 计划但未实现 | 无 |

### 结论

**D012 是单变量修复。** v1→v2 的行为差异完全由 n_min=3→2 解释。early return 是等价优化而非逻辑变更，D016 的 78% b=0 观察是 eval 数据污染 step_metrics 所致。论文可以安全地将 v2 描述为"仅调整 n_min 约束"。

---
