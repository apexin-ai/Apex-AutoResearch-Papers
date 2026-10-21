# eval cuda1 forgetting eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cuda1_forgetting_eval_20260515T195206_result.json`
- **Structured JSON:** [`d8bfbc2efa2754cb0a93.json`](../../sessions/d8/d8bfbc2efa2754cb0a93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。

**诊断总结：**
- `plan_009_flatnli_reward_eval` 失败原因：日志文件不存在、registry 无命令记录——说明之前根本没成功提交，任务只是被标记了 spec 但从未实际执行。
- `plan_009_extract_reward_eval` 不在 registry 中，未曾提交。

**已提交 (plan_009_flatnli_reward_eval_r2)：**
- `batch_eval` 在 **cuda:1** 上评估 `grpo_flatnli_r3` 的 **5 个 checkpoint** (step 20, 40, 60, 80, 100)
- 已确认 cuda:1 占用 12GB、utilization 100%，checkpoint-20 inference 进行中
- 每个 checkpoint eval 约 1 小时，共 ~5 小时
- 日志：`~/runs/faith-evidence-ie/plan_009_flatnli_reward_eval.log`
- 结果输出：`/root/autodl-tmp/eval_results/grpo_flatnli_r3/`

完成后可用这些数据补充 forgetting dynamics 3-panel figure 的 flatNLI reward 曲线。extract reward 的 checkpoints 也齐全（`grpo_extract_r3`/`r4`），可作为下一个 eval 排期。

---
