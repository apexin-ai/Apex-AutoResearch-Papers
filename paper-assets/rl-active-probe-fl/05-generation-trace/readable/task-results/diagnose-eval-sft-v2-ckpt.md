# diagnose eval sft v2 ckpt

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-sft-v2-ckpt_20260514T121743_result.json`
- **Structured JSON:** [`fbbf0c6229fe4e4399f9.json`](../../sessions/fb/fbbf0c6229fe4e4399f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**没有失败**，是 cron 监控误报。

## 诊断结论

**失败原因**：无。进程正常完成后退出，cron 检测到"进程不存在"且没有 sentinel 文件/W&B run，误判为失败。这是监控的 false positive。

**结果完整性**：`eval_sft_v2_ckpt.json` 存在（113KB，写入时间 20:02），日志显示 202/202 样本全部评估完毕并保存。结果：

| Metric | Mean | 90% CI |
|--------|------|--------|
| debug_accuracy | 0.762 | [0.713, 0.812] |
| probe_executed | 0.584 | [0.525, 0.644] |
| probe_diagnostic | 0.134 | [0.094, 0.173] |
| probe_dependent | 0.144 | [0.104, 0.183] |
| probe_generation_rate | 0.985 | — |

**Checkpoint 状态**：sft_v2 和 sft 结构一致，adapter_model.safetensors 均为 174MB，完好。

**GPU 状态**：cuda:1 空闲（0MiB），无残留进程。cuda:0 有另一个 python 进程在运行。

**不需要重试**，实验已成功完成。cron 误报的根因是 evaluate.py 没有写 sentinel 文件或注册 W&B run，建议后续给 eval 脚本加 sentinel 输出（如 `touch ~/runs/rl-active-probe-fl/eval-sft-v2-ckpt.done`）以避免再次误报。

---
