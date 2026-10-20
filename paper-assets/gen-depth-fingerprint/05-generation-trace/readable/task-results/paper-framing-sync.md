# paper framing sync

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_framing-sync_20260517T211046_result.json`
- **Structured JSON:** [`87c04c8dde2e718b6c5c.json`](../../sessions/87/87c04c8dde2e718b6c5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已更新 paper_framing.md。主要变更：

1. **Scope**: 6-gen/3-family → **8-gen/5-family** (Pythia, OLMo, Qwen, Llama, Mistral)
2. **Primary metric**: 3-class F1 0.79 → **leak-free binary F1 = 0.694**（排除 gen-0 seed sharing 泄漏）
3. **Cross-model**: 0.764 是 **binary F1**（3-class 实际是 0.809，已标注清楚）
4. **Feature ablation**: 旧 0.79/0.75/0.75 → 实际 **0.773/0.688/0.713**
5. **LOFO**: 旧 0.75–0.77 → 实际 **binary F1 = 0.686**
6. **Positioning**: 明确标注 **Findings paper**，贡献定位调整为 Findings 级别
7. **Limitations**: 新增独立章节，突出 instruct 退化、温度敏感性、7-feature 非最优（efficiency advantage）、3-class 天花板、scale effect
8. **Downstream TOST**: 补充 ±2% margin (p=1.1×10⁻⁴) 和 margin sensitivity 细节
9. **新增 Headline Metrics Summary 表格** 集中所有关键数字，便于快速查阅

---
