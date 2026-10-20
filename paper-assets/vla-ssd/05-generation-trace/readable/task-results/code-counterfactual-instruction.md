# code counterfactual instruction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_counterfactual_instruction_20260518T165804_result.json`
- **Structured JSON:** [`b91859e090c20f59bbee.json`](../../sessions/b9/b91859e090c20f59bbee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在 82-88% 利用率，15.5GB 显存使用，实验正常运行。

脚本 `scripts/counterfactual_instruction.py` 已创建并提交到 westd-19183，registry 状态已更新为 RUNNING。

实验配置：
- 3 tasks × 10 demos × 50 timesteps = 1500 samples/condition
- GPU 0: correct + wrong + empty（4500 forward passes）
- GPU 1: correct + shuffled + paraphrased（4500 forward passes）
- 输出：`/root/autodl-tmp/vla-ssd/results/counterfactual_{correct,wrong,empty,shuffled,paraphrased,combined}.json`
- 日志：`/root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log`

注意：multiprocessing spawn 的 stdout 重定向会导致日志输出有延迟，但 GPU 利用率和进程状态确认实验在正常推进。

---
