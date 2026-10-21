# check westd cuda1 cka

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_cuda1_cka_20260516T062049_result.json`
- **Structured JSON:** [`38a6c4aa58244cc31f01.json`](../../sessions/38/38a6c4aa58244cc31f01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况 B: cuda:1 仍在使用。**

两张卡都在跑 GSM8K 评估，不是 importance_score.py：

| GPU | PID | 进程 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| cuda:0 | 92690 | `eval_gsm8k.py` — sft_rasp_25 (1319 samples) | 12976MiB | 98% |
| cuda:1 | 92781 | `eval_gsm8k.py` — pruned_rasp_25 (100 samples) | 12059MiB | 87% |

importance_score.py 已完成，但 cuda:1 当前被 GSM8K 评估占用（pruned_rasp_25, 100 samples，应该很快结束）。cuda:0 的评估（1319 samples）会更久。

**下一步**：等 cuda:1 的 eval_gsm8k.py (100 samples) 完成后再启动 CKA 计算。以当前 87% 利用率和仅 100 samples 来看，预计很快完成。

---
