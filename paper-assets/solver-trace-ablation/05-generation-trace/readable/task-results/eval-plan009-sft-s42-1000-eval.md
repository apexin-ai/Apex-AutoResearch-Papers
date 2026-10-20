# eval plan009 sft s42 1000 eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan009-sft-s42-1000-eval_20260515T123005_result.json`
- **Structured JSON:** [`fb158247d5847f41b9ca.json`](../../sessions/fb/fb158247d5847f41b9ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU released. 评估完成，registry 已更新。

## 结果汇总

| 指标 | SFT 500步 s42 | SFT 1000步 s42 |
|------|:---:|:---:|
| Prove Rate | 14% | 13% |
| Mean ISR | — | 0.0738 ± 0.2077 |
| Proved-only ISR | — | 0.5677 |
| H7 | — | 0 (0%) |
| H1 | — | 1 (7.7%) |
| Genuine | 93% | **92.3%** (12/13) |

SFT 1000步 genuine rate 92.3%，与 500步的 93% 基本持平，符合预期：Goodhart collapse 是 GRPO 特有现象，SFT 在延长训练后仍保持高 genuine rate。

---
