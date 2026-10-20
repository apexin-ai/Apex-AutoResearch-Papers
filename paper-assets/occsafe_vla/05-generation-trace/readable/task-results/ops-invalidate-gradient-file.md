# ops invalidate gradient file

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_invalidate_gradient_file_20260523T042548_result.json`
- **Structured JSON:** [`c200581a4fd7135bf30d.json`](../../sessions/c2/c200581a4fd7135bf30d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。以下 4 个文件已移至 `invalid/` 子目录：

| 文件 | 大小 |
|------|------|
| `full_occ_cka_features.npz` | 4.6 MB |
| `full_occ_cka_meta.json` | 478 B |
| `full_occ_gradient_norms.pdf` | 25 KB |
| `full_occ_gradient_stats.json` | 23 KB |

这些文件实际使用的是 cutoff_s0 checkpoint，标签错标为 full_occ，数据归属不正确，已隔离到 `invalid/` 目录。

---
