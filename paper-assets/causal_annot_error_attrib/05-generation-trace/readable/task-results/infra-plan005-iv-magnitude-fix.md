# infra plan005 iv magnitude fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan005-iv-magnitude-fix_20260520T183544_result.json`
- **Structured JSON:** [`90a4327de3f8b250008f.json`](../../sessions/90/90a4327de3f8b250008f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 当前 registry 值
`plan005_asv_extended.metrics.asv_tau05.iv.magnitude_10pct` = **0**

### 正确值（来自 plan005_fixed_run.log）

IV magnitude_10pct at tau=0.5，6 个 C 结构：

| C 结构 | magnitude_10pct |
|--------|----------------|
| IV_C1_sym | 0.3035 |
| IV_C2_high | 0.6071 |
| IV_C3_asym | 0.1881 |
| IV_C4_weak | 0.1630 |
| IV_C5_perm | 0.1012 |
| IV_C6_diff | 0.3169 |

范围：**0.101–0.607**

注意：IV magnitude_10pct 在 tau=0.05/0.1/0.5 下数值相同（Wald 估计量的敏感性由分母驱动，与 tau 无关）。

### 原因
Registry 是从原始（有 bug 的）运行填充的。原始运行中 IV tau_true 误设为 0.5（DGP 参数）而非 plim_iv(I)=0.6598，导致 magnitude ASV 计算返回 0.0。修复后的脚本 `plan_005_asv_extended_fixed.py` 输出了正确值。

### 建议的 registry 更新

**Path**: `plan005_asv_extended.metrics.asv_tau05.iv`

**变更**:
- 删除 `magnitude_10pct: 0`
- 添加 `magnitude_10pct_range: "0.101-0.607"`（与 frontdoor 的 `magnitude_10pct_range` 字段格式一致）

```yaml
# Before
iv:
  sign_flip_range: "1.1-6.7"
  magnitude_10pct: 0

# After
iv:
  sign_flip_range: "1.1-6.7"
  magnitude_10pct_range: "0.101-0.607"
```

需要我执行 `update_registry` 吗？

---
