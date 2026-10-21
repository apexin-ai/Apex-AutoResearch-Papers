# exp westd full eval n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_westd-full-eval-n1319_20260515T203631_result.json`
- **Structured JSON:** [`1441ba2832add71dea68.json`](../../sessions/14/1441ba2832add71dea68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡 full GSM8K eval 已成功启动并确认：

| 实验 | GPU | 显存占用 | PID | 状态 |
|------|-----|---------|-----|------|
| eval_sft_standard_full_westd | cuda:0 | 12497 MiB | 62463 | RUNNING, 已加载 GSM8K 数据集 |
| eval_sft_rasp_full_westd | cuda:1 | 12497 MiB | 62565 | RUNNING, 已加载 GSM8K 数据集 |

N=1319 samples，预计 ~50 分钟完成。日志分别在 `/tmp/eval_standard_full.log` 和 `/tmp/eval_rasp_full.log`，结果输出到 `results/eval_sft_standard_20_westd_full.json` 和 `results/eval_sft_rasp_20_westd_full.json`。Registry 已更新为 RUNNING。

---
