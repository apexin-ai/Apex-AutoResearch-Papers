# analysis n1a boxed validation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n1a_boxed_validation_20260515T131421_result.json`
- **Structured JSON:** [`d5ee1ed2c3afcd6bb68a.json`](../../sessions/d5/d5ee1ed2c3afcd6bb68a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Boxed tokens（均值 7.8 token，中位 6）位于序列末尾 >99% 处，93.2% 落在 high-sparsity phase**，显著高于 last-50-tokens proxy 的 82.2%（Δ = +11.05 pp，16/16 条件均 p < 1e-33）。

- DeepSeek: boxed high = 94.5% vs proxy 87.0%（+7.6 pp）
- Qwen: boxed high = 91.9% vs proxy 77.4%（+14.6 pp）
- 加权 PPL 退化 proxy：boxed tokens 退化比 reasoning tokens 低 2.7–10×（importance pruning）

结论：last-50-tokens proxy 是**保守的**——它混入了约 42 个 reasoning tokens 稀释了信号。实际 `\boxed{}` 区域高稀疏度集中度更强，进一步支持 N1a 的结论。

交付物：
- 服务器：`n1a_boxed_validation.py` + `analysis_output/n1a_boxed_validation.json`
- 本地报告：`artifacts/n1a_boxed_validation/report.md`

---
