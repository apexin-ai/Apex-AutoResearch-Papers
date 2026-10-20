# prep rrf readiness check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_rrf-readiness-check_20260516T022450_result.json`
- **Structured JSON:** [`ab86cd3fb56ebc26a99e.json`](../../sessions/ab/ab86cd3fb56ebc26a99e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/rrf_readiness_check.md`。

**结论**：RRF 脚本功能上已就绪（dry-run 通过），但有两个前置条件：

1. **需改一行代码**：`SKIP_PATTERNS` 加入 4 个 alpha=16 黑名单目录，否则会混入无效数据
2. **信号文件缺口**：6 个有效 3B 目录中只有 `d005_s123` 完整就绪；`d025_s123` 接近完成（s4_mmlu 正在分块计算）；`d000_s123` 和 `d100_a32_*` 尚无/极少信号文件——这些很可能就是当前 GPU 上跑的 6 个实验在产出

---
