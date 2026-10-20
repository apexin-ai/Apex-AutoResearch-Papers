# research p2p regression rate v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p2p-regression-rate-v2_20260511T200243_result.json`
- **Structured JSON:** [`a858460434649a0cb544.json`](../../sessions/a8/a858460434649a0cb544.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。前一个 Worker 已产出完整分析，无需重做。

**核心结论**：

- **P2P 回归率 ≈ 1% (mean), 0% (median)** — 落入 **<5% 风险区间**
- 77% 的错误 patch 不破坏任何 P2P 测试；破坏的那些通常只坏 1 个测试
- **对项目影响：per-test verifier 在 P2P 维度优势不显著**，主要价值在 F2P 维度（区分"修了 1/3 测试"和"修了 0/3 测试"）
- 数据源：CoderForge Qwen3-32B on SWE-bench Verified，106 个有可解析 P2P 数据的错误 patch

Registry 已更新：`p2p-regression-rate` → DONE / negative。Artifact 已注册。

---
