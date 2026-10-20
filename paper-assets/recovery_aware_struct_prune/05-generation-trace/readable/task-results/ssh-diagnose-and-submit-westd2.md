# ssh diagnose and submit westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_and_submit_westd2_20260524T030752_result.json`
- **Structured JSON:** [`7014b6b5f6a8eb20515d.json`](../../sessions/70/7014b6b5f6a8eb20515d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中，GPU 2 尚未分配显存（加载阶段用 CPU）。进程正常启动。

**汇总：**

| 项目 | 结果 |
|------|------|
| **eval_math500_sft_rasp_alpha2p0_20_fixed** | accuracy=0.256 (128/500), stderr=0.0195, truncated_pct=0.31, avg_len=805.8 |
| Registry | conclusion=success, metrics/checkpoint_path/log_path 已设置 |
| Cron | 已删除 |
| **eval_math500_sft_rasp_alpha4p0_20_fixed** | 已提交 westd-32935 GPU 2, PID 185966, 模型加载中 |

---
