# ops westd sft eval check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-sft-eval-check_20260515T183357_result.json`
- **Structured JSON:** [`fba837ee5af344c35501.json`](../../sessions/fb/fba837ee5af344c35501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## 状态

| 实验 | 状态 | 详情 |
|------|------|------|
| **sft_rasp_20_westd_retrain** | DONE | 完成，checkpoint 已保存 |
| **sft_standard_20_westd_retrain** | DONE | 1870 steps, train_loss=0.7577, token_acc=0.8258 |
| **eval_sft_rasp_20_westd_n100** | RUNNING | PID 55353, cuda:0, 36/100 (~51s/sample), ETA ~55min |
| **eval_sft_standard_20_westd_n100** | RUNNING | PID 55286, cuda:1, 38/100 (~51s/sample), ETA ~53min |
| **eval_sft_grasp_20_westd** | 排队 | 等 eval 完成后启动 |

## 需要关注

N=100 eval 已被之前的 worker 自动启动（PID 55353/55286）。但 **早期 accuracy 极低**：
- RASP: 5.0% @20 samples（预期 ~57%）
- Standard: 0.0% @20 samples（预期 ~64%）

可能原因：
1. 20 samples 偏差（GSM8K 前段题目分布不均）
2. 模型路径问题（使用了相对路径 `sft_rasp_20_westd`，但模型加载日志显示 Non-uniform MLP detected，说明模型加载正确）
3. eval 脚本的答案解析逻辑问题

建议等 eval 完成后看最终结果再判断。两个 eval 预计在 ~55 分钟后完成（约 UTC 19:30），GraSP eval 排在其后。

---
