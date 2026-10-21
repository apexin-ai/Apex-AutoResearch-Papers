# eval v8b resume full eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8b_resume_full_eval_20260520T183653_result.json`
- **Structured JSON:** [`a2dc094dd5a8cd8c8fa5.json`](../../sessions/a2/a2dc094dd5a8cd8c8fa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，registry 和 artifact 已更新。

---

## v8b Scheduled Sampling Eval 总结

### 核心结论: **SUCCESS**

Scheduled Sampling 将 training-inference GAR gap 从 **32x 压缩到 1.57x**。

### 完整数据表

| Metric | v7 | v8b (SS) | Δ |
|--------|:---:|:---:|:---:|
| **IID GAR-ours** | 0.5035 | 0.4983 | -0.5pp |
| IID GAR-Dongre | 0.0152 | 0.3855 | +37.0pp |
| IID PPL | 2.784 | 2.78 | 无变化 |
| **Model-gen GAR-ours** | **0.0157** | **0.3177** | **+30.2pp** |
| Model-gen GAR-Dongre | 0.0194 | 0.3533 | +33.4pp |
| Model-gen PPL | 1.36 | 1.38 | 无变化 |

### 关键指标

- **Model-gen GAR-ours**: 0.016 → 0.318（20x 提升，远超 0.026 成功标准）
- **IID GAR-ours**: 基本持平（-0.5pp），无退化
- **PPL**: 完全无退化
- **IID↔Model-gen gap**: 32x → 1.57x

---
