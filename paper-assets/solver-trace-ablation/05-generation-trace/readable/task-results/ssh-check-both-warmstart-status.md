# ssh check both warmstart status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-both-warmstart-status_20260516T171200_result.json`
- **Structured JSON:** [`3304f76cdaa726e9b459.json`](../../sessions/33/3304f76cdaa726e9b459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断完成

| 实验 | 状态 | 结论 |
|------|------|------|
| **gated-isr-warmstart-t015-s43** (τ=0.15) | DONE ✓ | 300/300 完成，registry 已更新 conclusion=success。训练动态：67% 步 prove_rate=0，后 30 步近乎 collapse，需 eval_sta.py 确认最终模型质量 |
| **gated-isr-warmstart-t02-s43-r2** (τ=0.2) | 运行中 228/300 | GPU 0 正常跑，95% util，预计几分钟内完成 |

t02 无需干预，等它自然结束后再更新 registry。

---
