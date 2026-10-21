# research smolvla architecture

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla-architecture_20260515T111329_result.json`
- **Structured JSON:** [`2b30250d0871a908b54a.json`](../../sessions/2b/2b30250d0871a908b54a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/architecture_report.md`，核心发现：

**SmolVLA 架构**:
- SigLIP → 1024 patches → pixel shuffle 16x → **64 tokens × 960D** / camera
- SmolLM2 backbone (960D, 16 layers)
- Expert: Flow-matching transformer (720D, 16 layers, self/cross-attn 交替)
- Loss: MSE on velocity field (flow matching)

**ACIS 插入点**:
- `v_i` = `embed_image()` 输出 (B, 64, 960)，post-connector
- `a_query` = `embed_suffix()` 输出 (B, 50, 720)，投影到 960D
- 插入位置：`embed_image()` 之后、`embed_prefix()` 组装之前
- 需改动文件：`smolvlm_with_expert.py` 和 `modeling_smolvla.py`

**Soft Top-K 推荐**:
- **首选 Sigmoid + Implicit Differentiation** — 精确 Jacobian，零方差，Σp_i=k 严格满足，20 行代码无依赖
- 次选 DFTopK（有论文可引用），备选 Gumbel Top-k（LightVLA 验证过但方差大）

---
