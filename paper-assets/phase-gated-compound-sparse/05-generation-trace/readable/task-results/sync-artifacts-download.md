# sync artifacts download

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_artifacts_download_20260515T084423_result.json`
- **Structured JSON:** [`8bd13d2506cea3eedce5.json`](../../sessions/8b/8bd13d2506cea3eedce5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成，所有文件已验证通过：

| 文件 | 大小 | 行数 | 状态 |
|------|------|------|------|
| `n500_unified_final.csv` | 8,125 B | 完整5节（16条件 + within_dz + imp_vs_rand + cross_model + ratio） | OK |
| `n500_unified_final.json` | 33,207 B | 1,094 行 | OK，JSON 合法 |
| `n500_full_statistics.md` | 6,700 B | — | OK（之前已下载） |
| `supplementary_stats.json` | 26,435 B | 1,000 行 | OK，含 ci_shrinkage/jt_test/g_ratio |

验证结果：
- CSV 有 16 条数据行，含 `bonf_p_k4` 列 ✓
- DS imp s030 行存在，median=8.481, bonf_p_k4=4.35e-79 ✓
- JSON 与 CSV 16 条数据完全一致 ✓
- `qwen_midphase_null_analysis.md` 不存在于服务器 ✓
- `ci_shrinkage.json`/`jt_test_results.json`/`g_ratio_ci.json` 已包含在 `supplementary_stats.json` 中，跳过 ✓

---
