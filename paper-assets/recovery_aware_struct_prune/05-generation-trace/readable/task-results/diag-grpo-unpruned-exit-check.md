# diag grpo unpruned exit check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grpo-unpruned-exit-check_20260515T192800_result.json`
- **Structured JSON:** [`d7898b77328004cfb5e0.json`](../../sessions/d7/d7898b77328004cfb5e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。没有活跃的 cron 需要清除。

## 诊断结论：**negative（collapse）**

| 指标 | 值 |
|------|-----|
| 完成步数 | 100/100 |
| 运行时间 | ~49 分钟 |
| 峰值 reward | 0.04375 (step 20) |
| collapse 起始 | step 80 |
| 最终 reward | 0.0 |
| 最终 frac_reward_zero_std | 1.0 |
| 最终 clipped_ratio | 1.0 |
| 最终 mean_terminated_length | 0.0 |
| 模型保存 | 失败（磁盘满 250G/250G） |

**论文影响**：unpruned 模型同样 collapse，说明 collapse 不是剪枝导致的副作用，而是当前 GRPO 超参配置（lr, num_generations, max_completion_length 等）本身的问题。需要调整 GRPO 训练策略才能在任何模型上得到有效的 RL fine-tuning。

**附带问题**：westb-23072 数据盘 `/root/autodl-tmp/` 已 100% 满，需要清理空间。cuda:1 仍有进程占用 71.7GB 显存。

---
