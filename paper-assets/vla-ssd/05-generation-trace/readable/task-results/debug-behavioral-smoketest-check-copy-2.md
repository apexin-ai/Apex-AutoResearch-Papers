# debug behavioral smoketest check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_behavioral_smoketest_check_20260519T040135_result.json`
- **Structured JSON:** [`4e45348922324a3123a4.json`](../../sessions/4e/4e45348922324a3123a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## behavioral_smoketest 结果

**结论：negative** — Baseline 完全无法完成任务。

关键数据：
- 模型：`openvla-7b-finetuned-libero-goal`
- 任务：task 0 (`open_the_middle_drawer_of_the_cabinet`)
- 3 个 episode 全部失败，SR=0%，reward=0.0，全部跑满 400 步
- 因 baseline SR=0，脚本自动跳过 ablation 阶段

脚本本身执行无报错（return_code=0），问题在于 checkpoint 在此任务上完全不工作。可能原因：checkpoint 不匹配、unnorm_key 配置问题、或模型本身在该任务上微调不充分。

Registry 已更新为 DONE/negative，cron 已删除。

---
