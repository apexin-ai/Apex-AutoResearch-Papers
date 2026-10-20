# fix registry exp007 qwen cont

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry_exp007_qwen_cont_20260513T234012_result.json`
- **Structured JSON:** [`5641d22a8882bd66d39e.json`](../../sessions/56/5641d22a8882bd66d39e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已更新。修正了 `qwen_cont` 0v1 的两个字段：

| 字段 | 修正前 | 修正后 | 来源 |
|------|--------|--------|------|
| `auc` | 0.9972 | 0.9971 | bootstrap mean_auc（之前误用了 exp-017 原始值） |
| `perm_p` | 0 | 0.002 | perm_pvalue=0.0 + n_permutation=500 → 保守估计 (r+1)/(n+1)=1/501≈0.002，与其余三个模型惯例一致 |

其余 4 个 depth pair（1v2~4v5）数据与源文件一致，未修改。

---
