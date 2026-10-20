# code fix importance v5

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-importance-v5_20260514T012214_result.json`
- **Structured JSON:** [`9139132d924434088900.json`](../../sessions/91/9139132d924434088900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 代码修改

| 文件 | 行号 | 修改内容 |
|------|------|----------|
| `pacs/profiling/interaction_index.py:338-340` | Fix 1 | NaN 层跳过：`if torch.isnan(attn_f).any(): del attn_f; continue` |
| `pacs/profiling/interaction_index.py:280-283` | Fix 2 | 位置归一化：`importance /= arange(seq_len, 0, -1)` 在 `_select_kv_to_evict` 中 |
| `pacs/profiling/run_profiling.py:35` | Fix 3 | 新增 `from scipy import stats as scipy_stats` |
| `pacs/profiling/run_profiling.py:415-430` | Fix 3 | ii_out 增加 median / winsorized_mean / skewness / outlier_count |
| `pacs/profiling/interaction_index.py:121-122` | Fix 4 | torch.where 修复（已有，确认保留） |
| `pacs/utils/metrics.py:32` | Fix 4 | float32 cross_entropy（已有，确认保留） |

## Sanity check

两个 problem 均验证通过：
- **Layer 27 NaN 被正确跳过**（1/28 层 NaN）
- **Evicted importance < Kept importance**: 全部 True
  - Problem 0, s=0.2: evicted mean=9.69 vs kept mean=27.74
  - Problem 0, s=0.3: evicted mean=10.25 vs kept mean=30.17
  - Problem 1, s=0.2: evicted mean=3.58 vs kept mean=14.71
  - Problem 1, s=0.3: evicted mean=3.95 vs kept mean=16.12
- 被驱逐位置分布合理（不再集中在序列尾部，中位数在中间位置附近）

## Git commit

`20182ec` — fix: NaN layer skip + position normalization + robust II statistics

## 验证实验

| 实验 | exp_id | GPU | PID | 状态 |
|------|--------|-----|-----|------|
| A (sparsity=0.20) | `mvp_v5_fixed_s020` | cuda:0 | 46568 | RUNNING (3/50 problems) |
| B (sparsity=0.30) | `mvp_v5_fixed_s030` | cuda:1 | 46935 | RUNNING (2/50 problems) |

---
