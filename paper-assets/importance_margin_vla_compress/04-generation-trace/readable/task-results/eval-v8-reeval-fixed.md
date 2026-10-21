# eval v8 reeval fixed

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8_reeval_fixed_20260516T034945_result.json`
- **Structured JSON:** [`d4b2003ca847a848615f.json`](../../sessions/d4/d4b2003ca847a848615f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

## 总结

**evaluate.py 5 项修复验证**：全部到位 ✅

**v8 Re-eval 结果（D028 fix, 500-batch, cuda:1）**：

| Gate | Value | Target | Status |
|------|-------|--------|--------|
| **G1** margin ratio | **50.2x** | >1 | **PASS** |
| **G2** preservation diff | **+58.8pp** | >0 | **PASS** |
| **G3** standard/baseline | **1.344x** | ≤1.10 | **FAIL** |
| **G4** LED median | **0.087** | <1.0 | **PASS** |

**Overall: FAIL**（G3 未达标）

**与旧 buggy eval 对比**：结果在 ~5% 范围内一致。修复对 G4 影响最大（0.169→0.087，降 49%），其余指标变化不大。结论不变：gradient isolation 未解决 backbone 损伤问题，bypass/baseline = 7.12x。

Registry 和 artifact 已更新，标注 "D028 fix re-eval"。

---
