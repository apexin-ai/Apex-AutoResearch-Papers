# eval b03 isr s43 random s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_b03-isr-s43-random-s43_20260514T234153_result.json`
- **Structured JSON:** [`fabe003ce9d74acb96f0.json`](../../sessions/fa/fabe003ce9d74acb96f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验的 eval_sta 指标已收集并写入 registry。

## 汇总

| 指标 | exp1-isr-b03-s43 | exp1-random-b03-s43 |
|------|:-:|:-:|
| parse_rate | 1.0000 | 1.0000 |
| prove_rate | 0.9100 | 0.7900 |
| mean_isr | 0.2575 | 0.1745 |
| isr_std | 0.2363 | 0.1628 |
| median_isr | 0.3333 | 0.1667 |
| hacking_rate (strict H7) | 2.2% (2/91) | 0% (0/79) |
| hacking_rate (functional, n_necessary=0) | 33.0% (30/91) | 10.1% (8/79) |
| genuine_rate | 67.0% (61/91) | 89.9% (71/79) |
| genuine_count | 61 | 71 |
| H1 (conclusion in premises) | 74.7% | 75.9% |

ISR reward 在 prove_rate 和 mean_isr 上优于 random，但代价是更高的 functional hacking rate（33% vs 10%）——更多样本通过冗余获得 ISR=0 而非 genuine reasoning。

---
