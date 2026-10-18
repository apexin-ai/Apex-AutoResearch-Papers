# code kivi asymmetric compounding

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kivi_asymmetric_compounding_20260516T082515_result.json`
- **Structured JSON:** [`09756f3d0b75b4d3d034.json`](../../sessions/09/09756f3d0b75b4d3d034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/ratekv/run_kivi_asymmetric_compounding.py`，`--help` 和 `--dry-run` 均通过。

**脚本结构：**

| Phase | 内容 | 预计时间 |
|-------|------|----------|
| 1 | KIVI 非对称 profiling (112 heads × 3 bitwidths = 336 evals) | ~45-60min |
| 2 | BF16 baseline + Uniform 4-bit KIVI eval | ~10min |
| 3 | Unconstrained MCKP (无 k 限制) | ~5min |
| 4 | Constrained MCKP (k=8) | ~5min |
| 5 | Compounding sweep: k=[2,4,8,16,32,64,96,112], 8 × WikiText-2 eval | ~40min |

**总预计运行时间：~2h**（可用 `--skip-profiling` 跳过 Phase 1 复用已有 profiles，降到 ~1h）

核心区别点：
- 量化用 KIVI 非对称方案（K: per-channel grouped along token dim, V: per-token grouped along head_dim, 带 zero-point），而非项目原有的 symmetric per-head 方案
- Profiling 和 eval 都用同一套 KIVI 量化函数，保证一致性
- 输出包含 compounding ratio（unconstrained_delta / constrained_delta），>1.2 判定为 COMPOUNDING

---
