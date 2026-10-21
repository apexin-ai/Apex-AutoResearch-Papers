# analysis exp freeform ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_freeform_ablation_20260515T095741_result.json`
- **Structured JSON:** [`0f97c05d637a172eec8f.json`](../../sessions/0f/0f97c05d637a172eec8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已注册为 `art_20260515_b80d82`。核心结论：

**Score compression 假设未被证实。** Free-form LP variance 与 constrained 几乎一致（std ratio 0.97x, range ratio 0.96x, tied fraction 仅降 2pp）。Logprob 压缩是模型/任务的固有特性，非 constrained decoding 导致。

其他发现：
- **QE 信号在 free-form 下普遍改善**：NER 全部 5 个信号 ρ 上升（FK 最大 +0.053），RE 4/5 上升（VC 例外 -0.026）
- **RE 的 LP selection 从失败变成功**：constrained 下 -0.0068，free-form 下 +0.0169
- **Parse rate 99.95%**：549/551 instances 全部 8/8 valid，constrained decoding 对格式合规不是必要的

---
