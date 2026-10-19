# code m001 layer selection fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m001_layer_selection_fix_20260516T222709_result.json`
- **Structured JSON:** [`548b085e68fcf9c11abe.json`](../../sessions/54/548b085e68fcf9c11abe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M001 全部完成。

## 结果摘要

### Layer 修正

| Model | 旧 Layer | 修正 Layer | bal_acc |
|-------|---------|-----------|---------|
| R1-32B | 2 | **10** | 0.718 |
| QwQ-32B | 1 | **2** | 0.730 |

### 关键发现

**R1-32B (layer 10)**:
- Temporal LR 最佳 window=10: bal_acc=0.737, crossing=0.50, lead=9.0, FPR=0.189
- GRU single-layer: bal_acc=0.675, crossing=0.30, lead=9.1
- **Bootstrap HS vs Text: p=0.999, 无显著差异** (HS FPR=0.260 vs Text FPR=0.246)

**QwQ-32B (layer 2)**:
- Temporal LR 最佳 window=5: bal_acc=0.761, crossing=0.42, lead=23.5, FPR=0.180
- GRU multi-layer: bal_acc=0.724, crossing=0.84, lead=15.9

### 关键影响

R1-32B 上 HS 探针相对 Text baseline 的优势在修正 layer 后消失 (p=0.999)。此前报告的 HS 优越性很可能是 flawed layer selection 的 artifact。QwQ-32B 结果仍然稳健。论文 framing 中 "hidden state 提供 unique value over text" 的 claim 需要重新评估。

已完成：
- Registry 已更新 (exp_001a_r1_32b, exp_001b_qwq_32b)
- Report 已注册 (art_20260516_5aa87b)
- memory.md 已更新

---
