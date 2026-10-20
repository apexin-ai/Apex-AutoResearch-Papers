# research edge pruning precheck

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_edge-pruning-precheck_20260513T021113_result.json`
- **Structured JSON:** [`5a66a8efdf5025f60451.json`](../../sessions/5a/5a66a8efdf5025f60451.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用工具列表中。报告已保存至本地文件。

---

## 预检结论

**报告路径**：`artifacts/edge_pruning_precheck_report.md`

**核心发现**：

| 模型 | 适配难度 | 预估工时 | 关键依据 |
|------|---------|---------|---------|
| Qwen-2.5 0.5B | **低** | 6-10h | LLaMA-like 架构 + 社区 fork 有 `modeling_fqwen.py` 参考 |
| Llama-3.1 8B | **低-中** | 8-14h | `modeling_fllama.py` 几乎直接可用，主要工作在 FSDP 显存优化 |
| Gemma-2 2B | **中** | 16-24h | sliding window attention + logit soft-cap + pre/post-norm 混合需要额外处理 |

**推荐优先级**：Qwen-2.5 0.5B → Llama-3.1 8B → Gemma-2 2B（可选）

**关键风险**：Edge Pruning 不是 hook 注入，而是重写整个 forward pass（每个模型 1500-2000 行）。`modeling_fllama.py` 已为 LLaMA-like 架构铺好路，Qwen 和 Llama-3 适配成本可控。Gemma-2 的独特 attention 机制增加了复杂度和 bug 风险。

**替代方案**：auto-circuit 通过 TransformerLens 开箱支持三模型，但无分布式训练、显存效率差，仅适用于 Qwen-2.5 0.5B 级别作为备选。

---
