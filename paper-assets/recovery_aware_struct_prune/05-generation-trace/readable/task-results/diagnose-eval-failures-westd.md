# diagnose eval failures westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_failures_westd_20260519T123849_result.json`
- **Structured JSON:** [`b40dcd19ccbf3e4791f9.json`](../../sessions/b4/b40dcd19ccbf3e4791f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**结论：3 个实验全部已成功完成。监控系统误报。**

### 各实验状态

| 实验 | 状态 | 完成时间 | 结果 |
|------|------|----------|------|
| eval_gsm8k_grpo_standard_20_fair_v2 | 成功 | 20:28 | Accuracy = 0.5944 ± 0.0135 (784/1319) |
| eval_humaneval_grpo_standard_20_fair_2048_v3 | 成功 | 19:14 | Results saved to JSON |
| eval_humaneval_sft_cka_only_20_2048_v2 | 成功 | 19:05 | Pass@1 = 0.2012 ± 0.0313 (33/164) |

### 误报原因（共同原因，系统性问题）

监控系统判定 "process dead" 的依据是检测 **W&B metrics** 或 **sentinel 文件**。这 3 个 eval 脚本都不产生这两种信号：

1. **不写 W&B** — eval 脚本只在最后写一个 JSON 结果文件
2. **不写 sentinel** — 没有心跳机制
3. **运行时间长**（3-4 小时）— 监控系统在这段时间内反复检测不到信号，5 次后判定为 dead

### 关于实验 2 的额外说明

`humaneval_grpo_standard_20_fair_2048.log`（1667 bytes, 14:38）是最初的尝试，加载完数据集后在 0% 停住了（可能是 GPU 冲突被 kill），随后以 v3 名称重试并完成。

### 当前服务器状态

3 个新实验正在运行中：
- `eval_humaneval_sft_standard_20_2048_v3` — cuda:3, 76% (125/164)
- `eval_humaneval_sft_cka_only_20_1p5b_2048` — cuda:1, 19:45 启动
- `eval_humaneval_grpo_cka_only_20_1p5b_2048` — cuda:2, 19:45 启动

### 修复建议

在 eval 脚本中加一个周期性 sentinel 写入（如每 N 个 sample 写一次 `/tmp/agent-ml-sentinel/&lt;exp_name>.heartbeat`），让监控系统能检测到进程存活。

---
