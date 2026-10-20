# fix robust dz global

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_robust_dz_global_20260515T051031_result.json`
- **Structured JSON:** [`8c0111cc649b2a0a8946.json`](../../sessions/8c/8c0111cc649b2a0a8946.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 中没有旧的 `"d_z"` 字段名残留，只有新的 `"robust_dz"`。

完成。修改摘要：

| 改动 | 内容 |
|------|------|
| **公式** | `mean(diffs)/std(diffs)` → `median(diffs)/MAD(diffs)` (scale='normal' 自动 ×1.4826) |
| **函数名** | `paired_cohens_dz` → `robust_dz`，`bootstrap_dz_ci` → `bootstrap_robust_dz_ci` |
| **JSON/CSV 字段** | `d_z` → `robust_dz`，`d_z_ci` → `robust_dz_ci` |
| **MAD=0 处理** | 返回 NaN（与原 std=0 行为一致） |

**验证结果**（DeepSeek within-importance）：

| Pair | 旧 Cohen's d_z | 新 robust d_z |
|------|----------------|---------------|
| s015→s020 | -0.157 | **-0.925** (large) |
| s020→s025 | — | **-0.824** (large) |

robust d_z 绝对值显著大于旧值，因为 MAD 对离群值更鲁棒（不被极端 per-problem variance 拉大分母）。Director 预估的 -0.49 可能偏保守，实际 -0.82~-0.92 表明效应更强。

---
