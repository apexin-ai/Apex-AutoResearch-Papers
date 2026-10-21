# figures edd fix v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figures_edd_fix_v2_20260515T042848_result.json`
- **Structured JSON:** [`0a33f76dc2c2440e87bf.json`](../../sessions/0a/0a33f76dc2c2440e87bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**EDD 值对比：**

| 配置 | 修复前 (`idx`) | 修复后 (`idx+1`) |
|------|---------------|-----------------|
| Pythia-1.4B / topk | EDD=2 (错误) | **EDD=3** (正确) |
| OLMo-1B / topk | EDD=2 (错误) | **EDD=3** (正确) |

逻辑：d2v3 处 AUC 跌破 0.75（idx=2），EDD = 2+1 = 3，表示前 3 个 depth 可区分。与 atlas_v1_analysis 的 EDD=3 一致。底部注释 "EDD > 3 for 7/9 configurations" 无需修改。四张图均已重新生成至 `artifacts/figures/`。

---
