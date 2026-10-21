# ssh gpu status check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_20260521T143452_result.json`
- **Structured JSON:** [`3747f1b90f28d1ef88ce.json`](../../sessions/37/3747f1b90f28d1ef88ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-5090

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 67% | 30148/32607 MiB | `fewnerd_n16_s42` — finetuned model, n_samples=16, seed=42 |
| cuda:1 | 77% | 30204/32607 MiB | **exp_fewnerd_mf4v2_s42_v3** — finetuned model, n_samples=8, seed=42 ✅ 运行中 |
| cuda:2 | 82% | 30230/32607 MiB | **exp_fewnerd_mf4v2_s123_v3** — finetuned model, n_samples=8, seed=123 ✅ 运行中 |
| cuda:3 | 68% | 29946/32607 MiB | **exp_e2_pretrained_fewnerd_s456** — pretrained Qwen2.5-7B, n_samples=8, seed=456 ✅ 运行中 |

## autodl-5090-c

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 83% | 30131/32607 MiB | `fewnerd_n16_s123` — finetuned model, n_samples=16, seed=123 |
| cuda:1 | 0% | 0/32607 MiB | **空闲** |
| cuda:2 | 0% | 0/32607 MiB | **空闲** |
| cuda:3 | 81% | 30889/32607 MiB | **exp_e2_pretrained_fewnerd_s123** — pretrained Qwen2.5-7B, n_samples=8, seed=123 ✅ 运行中 |

## 汇总

4 个目标实验进程全部在跑。**autodl-5090-c 的 cuda:1 和 cuda:2 空闲**，可用于新任务。

---
