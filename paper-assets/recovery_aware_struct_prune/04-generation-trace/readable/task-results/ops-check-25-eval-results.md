# ops check 25 eval results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_25_eval_results_20260516T080527_result.json`
- **Structured JSON:** [`f9ecae3f1402d0eb30d4.json`](../../sessions/f9/f9ecae3f1402d0eb30d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 实验 | 状态 | Accuracy | 备注 |
|------|------|----------|------|
| **eval_postprune_rasp_25** | ✅ DONE | **21% (21/100)** | eos_rate=56%, avg_len=2033, 44/100 truncated |
| **eval_sft_standard_25** | 🔄 RUNNING | ~53.4% (interim@350) | westb, 356/1319 (27%), ~2.3s/it |
| **eval_sft_rasp_25** | 🔄 RUNNING | ~56.7% (interim@150) | westd, 163/1319 (12%), 很慢(GPU争抢, ~6min周期性stall) |
| **eval_postprune_standard_25** | ❌ 不存在 | — | 未运行过，无文件无日志 |

**关键观察：**
- RASP 25% post-prune (21%) vs 20% post-prune (31%)：sparsity 增加 5pp 导致 post-prune accuracy 下降 10pp，且 eos_rate 崩塌 (56% vs 之前接近 100%)，说明 25% RASP 模型生成能力严重受损
- eval_sft_rasp_25 在 westd 上跑得极慢（~5-6min GPU stall 周期），按当前速度预计还需 10+ 小时
- eval_postprune_standard_25 从未启动，需要补跑

Registry 已更新 eval_postprune_rasp_25 → DONE。两个 SFT eval 仍为 RUNNING，等待完成后再更新。

---
