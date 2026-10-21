# research roboflamingo c5 feasibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_roboflamingo_c5_feasibility_20260519T174812_result.json`
- **Structured JSON:** [`3a0a14cf513f8a8f02c2.json`](../../sessions/3a/3a0a14cf513f8a8f02c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。核心结论：

**Conditional Go。** 

**架构**: RoboFlamingo 用 Perceiver Resampler (64 learned queries cross-attend to 257 ViT tokens) 作为 vision connector，是与 pixel-shuffle 和 MLP projector 截然不同的第三种范式。每个 output token 是全局视觉特征的加权汇总，非空间局部映射。

**LIBERO 适配**: 可行性高。Action space (7-dim) 和 camera setup 直接兼容，零架构修改。主要工作量是 HDF5 dataloader + eval pipeline (~500 LOC)，预估 2 天。

**压缩预测**: 预测 graded degradation（第三种 pattern），可能比 MLP projector 更 robust — 因为每个 token 是 global summary，移除不产生 spatial hole。MQT (NeurIPS'24) 已有证据：256→16 tokens 仅 -2.4pt。

**时间估计**:
- 最小方案 (baseline + pruning curve): **3-4 天** → May 23 完成，deadline 前可行
- 完整方案 (含 VTR): 5-6 天 → 极紧
- GPU: 1×96GB (westd-41074:0) 足够

**No-go 条件**: C4-ext 需要大量 debug bandwidth / baseline SR<30% / 代码兼容性重大问题。

详细报告: `artifacts/c5_roboflamingo_feasibility.md`

---
