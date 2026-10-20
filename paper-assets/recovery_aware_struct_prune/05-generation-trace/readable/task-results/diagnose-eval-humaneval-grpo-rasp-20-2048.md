# diagnose eval humaneval grpo rasp 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_humaneval_grpo_rasp_20_2048_20260517T162616_result.json`
- **Structured JSON:** [`6160ab7ac55852666169.json`](../../sessions/61/6160ab7ac55852666169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验实际上**已完成全部 164 题并保存了结果**。EXIT_CODE=129 是在结果写入之后才收到的 SIGHUP，属于 SSH session 断连导致的无害信号。

## 诊断结论

| 项目 | 详情 |
|------|------|
| **失败根因** | 非真实失败。164/164 题全部跑完，结果已保存。SIGHUP 在脚本结束后触发，可能是 nohup/tmux session 超时断连 |
| **完成进度** | 164/164 (100%) |
| **最终结果** | **Pass@1: 0.1463 ± 0.0276 (24/164)** |
| **耗时** | ~2h28m (21:56:30 → 00:24:32) |
| **结果文件** | `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_rasp_20_2048.json` |
| **OOM** | 无 |
| **错误/异常** | 无（HF Hub 网络不可达已 fallback 到本地缓存） |

**不需要重跑。** 结果完整，JSON 已保存。Pass@1 逐步下降趋势（20题 0.25 → 120题 0.167 → 164题 0.146）说明后半段题目更难，模型表现较弱。

---
