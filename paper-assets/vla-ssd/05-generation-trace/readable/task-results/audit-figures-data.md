# audit figures data

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_figures_data_20260529T050826_result.json`
- **Structured JSON:** [`6475495003db4f2fe228.json`](../../sessions/64/6475495003db4f2fe228.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/audit_figures.md`。

**结果：14 图审计，~750 数据点，发现 2 个问题：**

1. **⚠️ P1** `plot_multi_layer_attention.py` L31 trained = **19**，论文和 teaser 均为 **18**。差 1 head，不影响结论。
2. **⚠️ P2** 附录段落引用 TraceVLA trained = 27/32 和 NORA ref = 13/16，但 `plot_l1_attention.py` 实际绘制 29/32 和 14/16。experiments.tex 使用范围值覆盖了这些差异。

**已排除的已知关注：**
- TraceVLA Spatial/Object wrong↔shuffled 交换 → ✅ 通过源数据报告验证，映射正确
- OpenVLA L1 24 vs 23 → ✅ 已知方法差异（dedicated vs bulk extraction）

---
