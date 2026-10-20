# ops d134 pipeline urgent check and fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-pipeline-urgent-check-and-fix_20260519T021330_result.json`
- **Structured JSON:** [`591d8cf06effc39c07f4.json`](../../sessions/59/591d8cf06effc39c07f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结构化摘要：

```
s50: DONE  PR=45%  H7=8.9%  H1=86.7%  H8=0%  genuine=4.4%  ISR*=0.0573
s51: DONE  PR=65%  H7=1.5%  H1=55.4%  H8=29.2%  genuine=13.9%  ISR*=0.3420
GPU: 空闲 (0 MiB / 97887 MiB)
磁盘: 41G/250G (17%)
Pipeline: 已结束（d134-pipeline session 不存在，d134-cleaner 存在）。无需干预，所有 seed 已完成。
Registry: s50/s51 均已更新为 DONE/success + metrics。
```

**d134_analysis.py 完整输出：**

```
ISR vs RANDOM (5 seeds each, 4B Qwen3, 500 steps)

ISR:    PR=89.0±13.8  H7%=90.8±7.5%  Genuine%=2.3±2.4%  ISR*=0.6576±0.0992
RANDOM: PR=59.4±36.1  H7%=6.7±8.1%   Genuine%=5.9±5.1%  ISR*=0.1345±0.1184

统计检验:
- H7 Domination Fisher: ISR 5/5 vs Random 0/5, p=0.004
- H7 Rate Mann-Whitney U: median 85.7% vs 3.2%, U=25, p=0.004, r=1.0
- ISR* Mann-Whitney U: median 0.713 vs 0.096, U=25, p=0.004, r=1.0
- Bayes Factor: BF10=77 (very strong evidence)
- Genuine Rate: ISR 2.28% vs Random 5.87%, Δ=-3.59pp, p=0.917 (not significant)
```

D134 全部 10 个 seed 实验完成，ISR 条件下 H7 hacking 显著高于 Random（p=0.004），genuine reasoning 两组无显著差异。GPU 现在空闲，可以接新任务。

---
