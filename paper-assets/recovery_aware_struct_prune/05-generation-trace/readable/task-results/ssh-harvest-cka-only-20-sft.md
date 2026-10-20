# ssh harvest cka only 20 sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_cka_only_20_sft_20260520T184805_result.json`
- **Structured JSON:** [`75479aff9f296d6a7dfc.json`](../../sessions/75/75479aff9f296d6a7dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### CKA-only 20% SFT (PID 264522) — 已完成

| 指标 | 值 |
|------|-----|
| **GSM8K Accuracy** | **63.91% ± 1.32%** |
| Correct / Total | 843 / 1319 |
| EOS Rate | 99.01% |
| Avg Response Length | 198.1 tokens |
| Truncated | 13 / 1319 |

结果文件：`/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json`

### Standard 20% SFT (PID 266847) — 运行中

- 进程存活，已运行 1h42m
- 进度：793/1319 (60.1%)
- 当前滚动 acc ≈ 60.5%（@750 样本时）
- 预计还需 ~1h 完成

Paper Agent 可先用 CKA-only 20% SFT 的 **63.91%** 更新 Table 2，Standard 20% SFT 结果预计 ~1h 后出。

---
