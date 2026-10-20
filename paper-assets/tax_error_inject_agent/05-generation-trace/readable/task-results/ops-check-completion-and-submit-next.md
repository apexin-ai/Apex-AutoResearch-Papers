# ops check completion and submit next

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-completion-and-submit-next_20260515T175419_result.json`
- **Structured JSON:** [`0d06abcedc19d62d6907.json`](../../sessions/0d/0d06abcedc19d62d6907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 已完成实验（→ DONE/success）

| 实验 | 关键指标 |
|------|----------|
| **v4-taxei-fixed-inject10-s0** | train_loss=0.4238, final_loss=0.31, token_acc=0.88, 1635 steps / 58min |
| **v4-training-dynamics-forward-v2** | 6 subset forward pass 完成，产出 JSON + 3 张图（dose_response, operator_breakdown, subset_comparison） |

## 已在运行的新训练（→ RUNNING）

| 实验 | GPU | 进度 |
|------|-----|------|
| **v4-taxei-fixed-inject10-s1** | cuda:2 | ~47/1635 steps（已由其他 session 提交） |
| **v4-random-fixed-inject10-s123** | cuda:3 | ~45/1635 steps（已由其他 session 提交） |

两个新训练预计约 58 分钟后完成（~1635 steps × 2.15s/it）。

---
