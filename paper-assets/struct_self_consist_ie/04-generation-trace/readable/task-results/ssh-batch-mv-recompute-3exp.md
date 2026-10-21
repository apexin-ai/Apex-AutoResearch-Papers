# ssh batch mv recompute 3exp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_batch_mv_recompute_3exp_20260522T044904_result.json`
- **Structured JSON:** [`4080d5baea4bf30a5647.json`](../../sessions/40/4080d5baea4bf30a5647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## 实验结果汇总

| 指标 | exp1: N=32 s123 (finetuned) | exp2: N=64 s42 (finetuned) | exp3: N=32 s42 (pretrained) |
|---|---|---|---|
| **greedy_f1** | 0.6663 | 0.6673 | 0.2446 |
| **mv_strict_f1** | 0.6675 | 0.6735 | 0.2643 |
| **mv_delta_pp** | +0.12 | +0.63 | +1.97 |
| **mv_incl_f1** | 0.6722 | 0.6725 | 0.2668 |
| **oracle_f1** | 0.8404 | 0.8626 | 0.4729 |
| **degeneracy_rate** | 5.1% | 2.1% | 0.2% |
| **alpha_crit_eff_strict** | 0.3511 | 0.3407 | 0.1526 |
| **verdict** | PASS | PASS | FAIL |
| **SJ ρ (full)** | +0.454 | +0.423 | +0.247 |
| **κ ρ (full)** | +0.330 | +0.322 | +0.246 |

**Pretrained 模型**: 存在于 `/root/autodl-tmp/models/Qwen2.5-7B-Instruct` (autodl-5090)

### 要点

- **Finetuned (exp1, exp2)**: 两个 PASS，N=64 的 mv_delta 更大 (+0.63pp vs +0.12pp)，degeneracy 更低 (2.1% vs 5.1%)，oracle 更高 (0.8626 vs 0.8404)
- **Pretrained (exp3)**: FAIL，greedy_f1 仅 0.24，46.5% 样本 F1=0，但 mv_delta 反而最大 (+1.97pp)——因为 baseline 极低，MV 相对提升空间大。α_crit_eff 仅 0.15，远低于 finetuned 的 ~0.35
- exp3 日志建议 T=0.7 重跑

---
