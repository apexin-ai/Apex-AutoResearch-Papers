# eval d129 isr b03 s44 final

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d129-isr-b03-s44-final_20260518T093411_result.json`
- **Structured JSON:** [`6e9ac2d229439a4f721c.json`](../../sessions/6e/6e9ac2d229439a4f721c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
=== isr-b03-s44 eval 结果 ===
PR:        92%
ISR*:      0.236 (proved-only)
Mean ISR:  0.217 ± 0.101
H1_pct:    1.1% (1/92)
H7_pct:    0.0% (0/92)
H8_pct:    1.1% (1/92)
Genuine:   90/92 = 97.8%
CI_pct:    100.0% (92/92)
total:     100 samples
```

**关键对比**：
- **s42**: reward collapse（PR=17% at 4B tokens）
- **s43**: PR=52%, 100% CI（严重 collapse）
- **s44**: PR=92%, genuine=97.8%, CI=100%

s44 走了一条完全不同的路：高 PR + 高 genuine + 低 hacking。但 CI=100%（content-independent predicates）值得注意。训练末期 entropy 接近 0、frac_reward_zero_std=1.0 说明模型收敛到几乎固定的输出模板，只是这个模板恰好能高效证明。ISR=0.236 说明大部分 clause 都被使用（不是冗余堆砌）。

三个 seed 展现了三种截然不同的 trajectory：collapse (s42)、partial-collapse+CI (s43)、high-PR+CI-template (s44)。这种高方差本身就是重要发现。

---
