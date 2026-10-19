# research qwen3 14b check

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen3-14b-check_20260512T103503_result.json`
- **Structured JSON:** [`d7a020c2ad84abbc1ea1.json`](../../sessions/d7/d7a020c2ad84abbc1ea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：用 Qwen3-14B-AWQ（4-bit），RTX 4090D 24GB 可运行

**Qwen3-14B 已发布**，HuggingFace 官方仓库 `Qwen/Qwen3-14B` 可用。14.8B 参数，40 层，原生 32K context（YaRN 扩展至 128K）。支持 thinking/non-thinking 双模式切换。

**量化版本齐全**：
- 官方 AWQ 4-bit：`Qwen/Qwen3-14B-AWQ` ✅
- 官方 GGUF：`Qwen/Qwen3-14B-GGUF` ✅
- 官方 FP8：`Qwen/Qwen3-14B-FP8` ✅
- AWQ 4-bit VRAM 约 **~10GB**，4090D 24GB 完全够用

**14B vs 8B**：Qwen3-8B ≈ Qwen2.5-14B，Qwen3-14B ≈ Qwen2.5-32B。14B 在推理/规划任务上显著强于 8B。4-bit GPTQ 量化仅损失 ~1% MMLU。对 ALFWorld 多步规划任务，14B 值得。

**兼容性**：
- transformers ≥ 4.52.4
- vLLM 支持（推荐 ≥ 0.19.0）
- bitsandbytes 4-bit 支持，但**推荐直接用官方 AWQ 版本**而非动态量化，更稳定

**建议**：直接用 `Qwen/Qwen3-14B-AWQ`，省去动态量化的兼容性风险，VRAM 充裕，推理能力远强于 8B。

Sources:
- [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B)
- [Qwen/Qwen3-14B-AWQ](https://huggingface.co/Qwen/Qwen3-14B-AWQ)
- [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)
- [Qwen3-14B vs Qwen3-8B Comparison](https://www.siliconflow.com/models/compare/qwen3-14b-vs-qwen3-8b)
- [Qwen3 Quantization Study](https://arxiv.org/html/2505.02214v1)
- [Qwen3-14B Specifications & VRAM](https://apxml.com/models/qwen3-14b)

---
