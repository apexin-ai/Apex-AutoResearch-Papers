# resume scale 14b t10 resume

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_resume_scale_14b_t10_resume_20260522T085417_result.json`
- **Structured JSON:** [`84651b7aea1a51f13521.json`](../../sessions/84/84651b7aea1a51f13521.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个 1.4B 实验已从 gen 2 resume 并注册为 RUNNING：

| 实验 | GPU | tmux session | Registry |
|------|-----|-------------|----------|
| scale_14b_t10_a060_s42_fp32_v2 | westd-17855 cuda:3 | `scale_14b_a060_v2` | RUNNING |
| scale_14b_t10_a075_s42_fp32_v2 | westd-17855 cuda:2 | `scale_14b_a075_v2` | RUNNING |

两个都已进入 Generation 2/10 的 synthetic data generation 阶段。剩余 8 个 gen（gen 2-9），1.4B 模型每 gen 约 40-50 min，预计总运行 5-7 小时。

---
