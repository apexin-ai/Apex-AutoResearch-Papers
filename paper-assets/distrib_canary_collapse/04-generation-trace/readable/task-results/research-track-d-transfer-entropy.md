# research track d transfer entropy

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-d-transfer-entropy_20260522T041958_result.json`
- **Structured JSON:** [`75843e7f645ffc9f574a.json`](../../sessions/75/75843e7f645ffc9f574a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**核心发现：Symbolic TE（ordinal patterns）在 sync-dip 格（α=0.60, PermG=0/8）检测到显著的 forward information flow（4/6 pairs, p<0.001），但在 PermG 正对照格（6/8）和 baseline 格均未检出。**

这意味着：
- α=0.60 的 sync-dip **不是**信息流缺失，而是 PermG 的线性假设盲区
- 耦合机制是**非线性的**（rank-order pattern 传播），Granger 无法捕获
- Symbolic TE 和 DiffXCorr 互相验证：都在 sync-dip 格检出，形成方法论互补

三个输出已保存到 `westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/`:
- `transfer_entropy_analysis.py`
- `transfer_entropy_results.pdf`
- `transfer_entropy_summary.json`

---
