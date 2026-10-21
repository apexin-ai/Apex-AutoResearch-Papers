# writing r6 tables ci

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r6_tables_ci_20260516T203036_result.json`
- **Structured JSON:** [`b3c3420fb917283c8954.json`](../../sessions/b3/b3c3420fb917283c8954.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改结果：**

| Table | CI 数据源 | 格式选择 | CI 范围 |
|-------|-----------|----------|---------|
| Table 2 (9-cell 主矩阵) | `all_results.json` → RF `acc_4class_ci` | Caption 注释 | 1.3–1.6 pp |
| Table 4 (cross-model) | `cross_model_loo.json` → `accuracy_ci95_bootstrap` | Caption 注释 | ≤0.4 pp |
| Table 5 (cross-strategy) | `cross_strategy_loo.json` → `accuracy_ci95` | Caption 注释 | ≤0.7 pp |

**选择 caption 注释而非逐格 ±** 的原因：CI half-width 在各 table 内极为均匀（Table 2 跨 9 cell 仅差 0.3pp），逐格标注信息冗余且有超页风险。

**编译验证：**
- 0 errors, 0 undefined refs
- 正文 8 页（Discussion 在 p8，附录从 p12 起）
- PDF 已回传：`artifacts/final_paper.pdf` (460KB)

---
