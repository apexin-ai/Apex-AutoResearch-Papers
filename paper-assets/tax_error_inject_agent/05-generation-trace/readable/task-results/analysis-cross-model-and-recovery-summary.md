# analysis cross model and recovery summary

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-model-and-recovery-summary_20260516T104641_result.json`
- **Structured JSON:** [`70d6fd61441dd726a62f.json`](../../sessions/70/70d6fd61441dd726a62f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册（`art_20260516_f9b206`）。核心发现：

1. **数据勘误**：你提供的 TaxEI-RP 均值 47.9±7.8 与 per-seed 数据不符，registry 验证为 **50.2±8.6**。Vanilla recovery s42 (61.7%) 和 TaxEI recovery s42 (59.6%) 在原始列表中遗漏。

2. **跨模型 (Table A)**：LLaMA 在三个 condition 下 recovery 几乎无差异（74.5/74.5/76.6），且 detection 率 21–30%；Qwen 全部 0% detection。LLaMA 对注入不敏感，适合作为"天花板模型"对比。但只有 1 seed，结论偏弱。

3. **TaxEI-RP (Table B)**：50.2% vs Vanilla 67.3%，Cohen's d=2.48，Welch t p≈0.006，**显著**。Recovery-paired 训练严重损害 clean 性能。

4. **Recovery 完整性 (Table C)**：Vanilla 5/5 完整，TaxEI 缺 s7，Random 只有 s42。Random 缺 4 个 seed 是最大数据缺口。

5. **Dose-response (Table D)**：10% 处有 5-seed 完整数据（TaxEI 61.3±7.7, Random 63.8±5.2），25%/50% 仅 3 seed。TaxEI 在所有 dose 下比 Random 低 2–6pp，taxonomy 标签放大了扰动而非提供有用结构。曲线在 25%→100% 出现非单调回升，可能因 100% 数据量翻倍补偿了噪声。

---
