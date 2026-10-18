# research wang models survey

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wang-models-survey_20260518T045105_result.json`
- **Structured JSON:** [`523fa3d21a6240bd9aa1.json`](../../sessions/52/523fa3d21a6240bd9aa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。关键发现：

**论文实际的 6 个 variants 与预期不符：**
- 实际：HGRN, RetNet, GLA, HGRN-2, DeltaNet, GatedDeltaNet
- 预期的 Mamba-2 和 RWKV-6 **不在此 collection 中**

这意味着原始 MVP 计划需要修订。论文推荐 HGRN-2 或 GatedDeltaNet（ratio 3:1 到 6:1）。

**模型可用性确认：**
- 所有 340M 模型均可下载（safetensors 格式）
- 统一依赖 `flash-linear-attention` 库（PyTorch >= 2.5, Triton >= 3.0）
- 模型使用 `trust_remote_code=True` 加载

**建议 MVP 替代方案：** GatedDeltaNet + HGRN2 + DeltaNet（或 RetNet），各 4 个 ratio（pure, 12:1, 6:1, 3:1），共 12 个模型，全部已确认可用。

---
