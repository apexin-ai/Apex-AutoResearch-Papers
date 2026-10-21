# analysis eval humaneval grpo standard 20 fair 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_grpo_standard_20_fair_2048_20260519T063730_result.json`
- **Structured JSON:** [`f4bcbd66f24a324aaab6.json`](../../sessions/f4/f4bcbd66f24a324aaab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**实验 `eval_humaneval_grpo_standard_20_fair_2048` 未完成，需要重新运行。**

两次尝试都失败了：

1. **第一次**（tmux, ~13:59）：模型路径错误 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_fair` 不存在，tokenizer 加载崩溃。正确路径应为 `grpo_stage2_standard_20_fair`。
2. **第二次**（results log, ~14:38）：用了正确路径 `grpo_stage2_standard_20_fair`，成功加载模型和 164 道题，但进度停在 0% 后进程消失（log 最后修改时间 14:41，此后无更新，无运行中进程）。可能原因：4 张 GPU 全被其他任务占满，该进程没能分配到显存或被 OOM kill。

**当前 GPU 占用**（全部 4 张被占）：
| GPU | 任务 |
|-----|------|
| cuda:0 | math500_sft_standard_20 |
| cuda:1 | humaneval_grpo_cka_only_20 |
| cuda:2 | humaneval_sft_cka_only_20 |
| cuda:3 | humaneval_grpo_rasp_20_fair |

需要等某个 GPU 空闲后重新提交 `eval_humaneval_grpo_standard_20_fair_2048`，使用正确路径 `grpo_stage2_standard_20_fair`。

---
