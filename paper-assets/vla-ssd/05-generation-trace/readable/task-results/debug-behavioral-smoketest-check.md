# debug behavioral smoketest check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_behavioral_smoketest_check_20260519T042250_result.json`
- **Structured JSON:** [`a373752947ca7954382f.json`](../../sessions/a3/a373752947ca7954382f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## behavioral_smoketest 结果：**negative (baseline_zero)**

**关键日志：**
- Task: `open_the_middle_drawer_of_the_cabinet` (task_id=0)
- Checkpoint: `openvla-7b-finetuned-libero-goal`
- 3 episodes 全部失败，reward=0.0，均跑满 400 步
- Baseline SR=0.00，脚本提前终止（"no point running ablation"）
- 未执行 ablation 对比

**结论：** Finetuned OpenVLA 在此任务上 closed-loop rollout 完全不工作，无法产生 behavioral evidence。可能原因：checkpoint 微调不足、unnormalization key 不匹配、或需要更多 episodes/不同 task 验证。

---
