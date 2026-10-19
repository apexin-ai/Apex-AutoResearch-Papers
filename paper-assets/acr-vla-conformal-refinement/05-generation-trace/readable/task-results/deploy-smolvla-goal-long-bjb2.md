# deploy smolvla goal long bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-goal-long-bjb2_20260522T050746_result.json`
- **Structured JSON:** [`4c6afbaf0a3b44c74692.json`](../../sessions/4c/4c6afbaf0a3b44c74692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 已重新提交。等待启动后核查。

**当前状态**：
- CRM checkpoint：已从 bjb1-18228 经 SSH 传输到 bjb2-28827:/root/autodl-tmp/checkpoints/crm/crm_best.pt（1.3M）
- SmolVLA 模型：bjb2-28827:/root/autodl-tmp/models/smolvla_libero/ 已存在
- 旧 CRM checkpoint 缺 `input_mean/std` buffers → 已 patch `src/evaluate.py` 改为 `strict=False`（默认 0/1 = 无归一化，与旧训练一致）

**已运行 (v2)**：
| exp_id | GPU | PID |
|--------|-----|-----|
| eval-smolvla-crm-long-seed43-v2 | cuda:3 | 171674 |
| eval-smolvla-crm-goal-seed44-v2 | cuda:4 | 171949 |
| eval-smolvla-crm-long-seed44-v2 | cuda:5 | 172552 |

---
