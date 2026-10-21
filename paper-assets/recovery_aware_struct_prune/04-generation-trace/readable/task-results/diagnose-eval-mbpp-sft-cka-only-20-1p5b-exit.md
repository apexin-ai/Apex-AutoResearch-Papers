# diagnose eval mbpp sft cka only 20 1p5b exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mbpp_sft_cka_only_20_1p5b_exit_20260519T184119_result.json`
- **Structured JSON:** [`7895f75381bd070724d6.json`](../../sessions/78/7895f75381bd070724d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不在当前 session 中（可能由上一个 session 创建，已随 session 结束自动清除）。

**结果汇总：**

- **状态**：失败
- **原因**：AutoDL 实例网络不可达，`load_dataset("mbpp")` 尝试访问 huggingface.co 时抛出 `[Errno 101] Network is unreachable`，重试后 httpx client 关闭导致 `RuntimeError`
- **根因**：启动 eval 前未执行 `source /etc/network_turbo`，且 MBPP 数据集未在本地预缓存
- **Registry**：已更新为 DONE/failed，failure_reason 已记录

**重跑建议**：重跑前先 `source /etc/network_turbo` 启用代理，或提前将 MBPP 数据集缓存到 `/root/autodl-tmp/` 使用离线模式加载。

---
