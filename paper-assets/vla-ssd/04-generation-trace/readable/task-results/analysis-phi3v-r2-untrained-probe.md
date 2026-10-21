# analysis phi3v r2 untrained probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phi3v_r2_untrained_probe_20260520T102858_result.json`
- **Structured JSON:** [`f935537ef898c534206f.json`](../../sessions/f9/f935537ef898c534206f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## phi3v_r2_untrained_probe — SUCCESS

**核心发现**：Inverted-U mid-layer peak 确认是 VLA 训练产物。

| | Untrained | Trained | Delta |
|---|---|---|---|
| Peak R² | 0.583 (L4) | 0.634 (L11) | +0.051 |
| Profile | 早期达峰 + 单调下降 | Inverted-U mid-layer peak | 形状不同 |
| Late-layer std | 高达 0.12 | < 0.02 | 训练稳定化 |

**三个关键点**：
1. **Profile 形状不同** — 未训练模型 L4 达峰后缓降，训练后峰值右移 7 层到 L11 形成 inverted-U。Hypothesis 确认。
2. **未训练基线意外地高** — 峰值 0.583 达到 trained 的 92%，说明预训练 LLM 的浅层表征已含大量可解码为 action 的信息。
3. **训练的主要效果是重分配而非创造** — VLA training 将 action-predictive 信息从浅层集中到中深层，同时稳定深层表征（降低 variance）。

Registry 已更新为 DONE/success，分析报告已注册 (`art_20260520_e54cf7`)。

---
