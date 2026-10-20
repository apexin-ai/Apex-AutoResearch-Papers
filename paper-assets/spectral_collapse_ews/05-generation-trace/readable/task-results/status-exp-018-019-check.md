# status exp 018 019 check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_exp_018_019_check_20260523T073106_result.json`
- **Structured JSON:** [`621b305e862098263eee.json`](../../sessions/62/621b305e862098263eee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### exp_018 (r=0.5, seed43, cuda:0)
- **当前进度**: Gen 9/10 生成阶段（22080/25000 samples）
- **状态**: 运行中，GPU 利用率 69%
- **已完成 Gen 0–8 的 metrics**:

| Gen | eff_rank | PPL | D-4 | σ₁ | loss |
|-----|----------|------|------|------|------|
| 0 | 417.55 | 9.55 | 0.741 | 1942.8 | — |
| 1 | 475.91 | 10.08 | 0.671 | 956.5 | 1.984 |
| 2 | 488.01 | 10.41 | 0.571 | 873.1 | 1.912 |
| 3 | 493.94 | 10.73 | 0.544 | 849.7 | 1.712 |
| 4 | 503.05 | 11.12 | 0.463 | 817.0 | 1.643 |
| 5 | 510.11 | 11.60 | 0.419 | 785.6 | 1.522 |
| 6 | 519.21 | 12.12 | 0.411 | 752.5 | 1.417 |
| 7 | 526.83 | 12.69 | 0.361 | 728.2 | 1.349 |
| 8 | 536.98 | 13.46 | 0.299 | 676.8 | 1.263 |

趋势：eff_rank 持续上升（417→537），σ₁ 持续下降（1943→677），PPL 逐步升高，D-4 下降明显——典型的 spectral collapse 演进，但因 r=0.5 real data 混入，退化速度比纯合成慢。

**预计完成时间**: Gen 9 生成快完了，之后还有 Gen 9 训练+评估 + Gen 10 全流程。估计还需 ~2-3 小时（约 16:00-17:00 UTC）。

### exp_019 (r=0.2, seed44, cuda:1)
- **当前进度**: Gen 2/10 生成阶段（27200/40000 samples）
- **状态**: 运行中，GPU 利用率 95%
- **已完成 Gen 0–1 的 metrics**:

| Gen | eff_rank | PPL | D-4 | σ₁ | loss |
|-----|----------|------|------|------|------|
| 0 | 417.55 | 9.55 | 0.730 | 1942.8 | — |
| 1 | 476.57 | 10.28 | 0.654 | 961.5 | 1.765 |

注意 exp_019 每 gen 生成 40000 samples（vs exp_018 的 25000），因为 r=0.2 意味着更多合成数据。进度会比 exp_018 慢，预计还需 ~12-15 小时完成。

---
