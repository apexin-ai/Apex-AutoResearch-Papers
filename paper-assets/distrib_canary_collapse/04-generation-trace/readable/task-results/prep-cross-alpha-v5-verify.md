# prep cross alpha v5 verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_cross_alpha_v5_verify_20260515T113234_result.json`
- **Structured JSON:** [`bfb57aa81b42121cb981.json`](../../sessions/bf/bfb57aa81b42121cb981.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。核心结论：

**脚本无需任何修改即可支持 5 α 点。** 6 项检查中 5 项通过：
- ✅ α 点自动发现（glob 匹配，非硬编码）
- ✅ FDR 混合策略两条路径均正确（threshold_onset 用 `significant`，其余 4 方法用 FDR 修正）
- ✅ permG/TY 列顺序三文件一致（TY=idx3, permG=idx4）
- ✅ 已完成的 4 个 α 点数据齐备
- ❌ **a075 实验仍在运行**（当前 gen_7/10，预计 ~22:30 完成）

报告已写入 `artifacts/prep_cross_alpha_v5_verify.md`。

---
