# paper fix fig1 labels

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-fig1-labels_20260520T195041_result.json`
- **Structured JSON:** [`af1dd7836efddc2a0b63.json`](../../sessions/af/af1dd7836efddc2a0b63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 family 的 pattern 映射全部正确：
- Phi-4 → Immune
- Qwen-14B → Collapse
- Qwen-7B → V-recovery
- Gemma-2 → Benefit
- OLMo-2 → Benefit†

生成完成。输出文件：
- `fig1_dose_response.pdf` (42KB) / `.png` (287KB) — MMLU + ARC 双 panel dose-response
- `fig2_cross_benchmark_scatter.pdf` (37KB) / `.png` (136KB) — cross-benchmark Δ scatter
- `gen_fig1_fig2.py` — 可复现的生成脚本

所有标签使用 hardcoded family-level taxonomy（不再依赖 `classify_pattern()` 自动输出），caption 注明 "seed=42; family-level classification from multi-seed analysis (Table 3)"。

---
