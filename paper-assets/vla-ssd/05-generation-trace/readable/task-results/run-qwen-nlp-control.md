# run qwen nlp control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_qwen_nlp_control_20260524T025445_result.json`
- **Structured JSON:** [`b1c6a47ddbed35e3bda7.json`](../../sessions/b1/b1c6a47ddbed35e3bda7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Qwen2.5-3B-Instruct NLP Control 实验完成。**

| 指标 | 值 |
|------|-----|
| 模型 | Qwen2.5-3B-Instruct (36 layers, 3.1B params) |
| 样本数 | 5000 (10 tasks × 10 demos × 50 timesteps) |
| **ΔR²** | **0.0000** |
| Peak R² | 0.1555 (L3) |
| Exit R² | 0.1555 (L35) |
| Mean R² | 0.1554 |

### Per-layer R² (L0-L35)

```
L0:  0.1553  L1:  0.1554  L2:  0.1554  L3:  0.1555
L4:  0.1555  L5:  0.1550  L6:  0.1553  L7:  0.1554
L8:  0.1555  L9:  0.1555  L10: 0.1555  L11: 0.1555
L12: 0.1555  L13: 0.1555  L14: 0.1555  L15: 0.1555
L16: 0.1555  L17: 0.1555  L18: 0.1551  L19: 0.1552
L20: 0.1552  L21: 0.1553  L22: 0.1554  L23: 0.1554
L24: 0.1554  L25: 0.1555  L26: 0.1555  L27: 0.1555
L28: 0.1555  L29: 0.1555  L30: 0.1555  L31: 0.1555
L32: 0.1555  L33: 0.1555  L34: 0.1555  L35: 0.1555
```

**符合预期**：完全平坦的 R² profile，ΔR²=0.000，R²≈0.155 across all 36 layers。与 Llama-2-chat 和 Phi-3-mini 的 NLP control 结果一致，确认 text-only LLM 没有 exit collapse 现象——这是 VLA-specific 的。

---
