# ssh p0 bootstrap ci training effect

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-bootstrap-ci-training-effect_20260515T224516_result.json`
- **Structured JSON:** [`9ca15b37d4accfb856ff.json`](../../sessions/9c/9ca15b37d4accfb856ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap 完成。结果：

| 聚合方式 | Δ (trained−untrained) | 95% CI | p-value | 显著？ |
|---|---|---|---|---|
| **image_mean** | +0.0206 | [−0.0314, +0.0638] | 0.200 | 否 |
| **last_preaction** | +0.0076 | [−0.0395, +0.0558] | 0.370 | 否 |

两个 CI 都包含 0，training effect 在 task-level bootstrap 下均不显著。10 个 task 的 per-task RSA 方差很大（如 `turn_on_the_stove` image_mean Δ=−0.17，`put_the_bowl_on_the_stove` Δ=+0.15），导致 CI 宽度约 0.09，远大于观测到的 Δ。

结果文件：`/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json`，已注册 artifact。

---
