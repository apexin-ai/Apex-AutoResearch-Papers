# review dz bootstrap ci

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_dz_bootstrap_ci_20260515T044502_result.json`
- **Structured JSON:** [`18f44f12654c380905d5.json`](../../sessions/18/18f44f12654c380905d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 复查结论：**PASS（代码无 bug）**，CI 不对称是数据特性

### 代码审查

| 检查项 | 结果 |
|--------|------|
| `paired_cohens_dz` 公式 (mean/std, ddof=1) | ✅ 正确 |
| `bootstrap_dz_ci` 对原始 diffs resampling 再算 d_z | ✅ 正确 |
| 百分位法取 CI | ✅ 正确 |
| problem_id 对齐 | ✅ 两条件 500 题顺序一致，None 位置相同（idx 56,86,430,457） |

### 根因：单个极端离群值

问题出在 `test/intermediate_algebra/431.json`（idx=102）：

| 条件 | ii_low | ii_high | diff(lo-hi) |
|------|--------|---------|-------------|
| s020 | -0.19 | 0.03 | -0.22 |
| **s025** | **1524.13** | 1.16 | **1522.97** |

s025 的 `ii_low=1524.13` 比典型值大 3 个数量级，产生 paired_diff = **-1523.19**。

**连锁效应**：
- 该离群值将 `paired_diffs` 的 std 从 ~30 膨胀到 ~70，**稀释了点估计** d_z（-0.49 → -0.16）
- Bootstrap 中大多数 resample 不会过度抽到该离群值 → d_z 集中在 -0.14 附近（CI 上界）
- 少数 resample 多次抽到 → d_z 跌至 -0.5~-0.7（CI 下界）
- 形成**双峰** bootstrap 分布，导致极端不对称

验证——去除该离群值后：

| 指标 | 含离群值 (n=496) | 去除后 (n=495) |
|------|-----------------|---------------|
| d_z | -0.1565 | **-0.4879** |
| CI | [-0.643, -0.135] | **[-0.665, -0.387]** |
| bootstrap skew | -0.73 | **-0.30** |

去除后 CI 对称，d_z 从 negligible 变为 **medium** 效应。

### 建议

无需修代码，但统计报告需要补充说明。有两个选择：

1. **最小改动**：在报告中标注 s020→s025 的 d_z 受单个极端 ii_low=1524 影响，trimmed d_z=-0.49（medium）
2. **更稳健**：对 `paired_diffs` 做 Winsorize（如 1% 两端截断）后再算 d_z 和 CI，或用 robust effect size（median/MAD）

需要我实施哪个方案？

---
