# analysis llama tertile ablation 105

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-tertile-ablation-105_20260522T025918_result.json`
- **Structured JSON:** [`cd26e3d0f98abb659399.json`](../../sessions/cd/cd26e3d0f98abb659399.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果对比

| | **Qwen3-8B** (L22) | **Llama-3.1-8B** (L13) |
|---|---|---|
| Full balanced_acc | 0.6488 | 0.5919 |
| High COMET bal_acc | 0.6071 | 0.6165 |
| Med COMET bal_acc | 0.6769 | 0.5624 |
| Low COMET bal_acc | 0.6635 | 0.6000 |
| **Δ(High-Low)** | **-5.64 pp** | **+1.65 pp** |
| Fisher p | 0.6951 | 0.7613 |
| **Conclusion** | NOT CONFOUNDER | NOT CONFOUNDER |

两个模型一致：翻译质量不是探针迁移的混淆因素。Qwen 甚至出现反向效应（高 COMET → 低探针准确率）。Registry 已更新 `mvp_probe_llama_v1` metrics，memory.md 已追加 COMET tertile ablation 结果。

---
