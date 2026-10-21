# ops westd cleanup and sft rasp25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-cleanup-and-sft-rasp25_20260516T052424_result.json`
- **Structured JSON:** [`e07c6dacced840bf4d94.json`](../../sessions/e0/e07c6dacced840bf4d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **清理**：删除 checkpoint-90 和 checkpoint-95，释放 ~63GB（/root/autodl-tmp/ 可用从 18GB → 81GB）。仅保留 checkpoint-100。
- **pruned_rasp_25**：westd 上不存在，现场执行 RASP 25% 剪枝新建。实际稀疏度 24.05%，252 MLP groups pruned，模型 11GB，含 tokenizer。
- **SFT 启动成功**：PID 88533（python），tmux session `sft_rasp_25`，westd-11672 cuda:0。7473 样本，2 epochs，1870 steps，~1.1s/it（预计 ~34 分钟）。训练已开始出 loss。

---
