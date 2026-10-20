# ssh exp 017 completion check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_017_completion_check_20260523T034228_result.json`
- **Structured JSON:** [`200e853e5bb1480e125f.json`](../../sessions/20/200e853e5bb1480e125f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp_017 (fixed_mix_r02_seed43) — **Running, ~99% complete**

Gen 10 fine-tuning at Step 3100/3125，训练即将结束，之后还需 evaluation（computing eff_rank/ppl/distinct4），预计 **3-5 分钟**内全部完成。

**Gen 0-9 metrics（从日志提取）:**

| Gen | eff_rank | PPL | D-4 | train_loss |
|-----|----------|-------|--------|------------|
| 0 | 417.55 | 9.55 | 0.7415 | — |
| 1 | 475.29 | 10.28 | 0.6842 | 1.7676 |
| 2 | 480.44 | 10.74 | 0.4988 | 1.7217 |
| 3 | 486.99 | 11.15 | 0.4780 | 1.4247 |
| 4 | 489.33 | 11.49 | 0.4445 | 1.3675 |
| 5 | 492.09 | 11.83 | 0.4435 | 1.2730 |
| 6 | 495.85 | 12.15 | 0.4420 | 1.2219 |
| 7 | 498.05 | 12.48 | 0.3433 | 1.1914 |
| 8 | 500.80 | 12.76 | 0.3106 | 1.0154 |
| 9 | 504.08 | 13.08 | 0.3060 | 0.9546 |
| 10 | **pending** | **pending** | **pending** | ~0.948 |

Gen 10 training loss ~0.948 与 seed42 的趋势一致。

**结果文件**: `/root/spectral_collapse_ews/results/phase1_fixed_mix_r02_seed43_results.json`

---

### exp_018 (fixed_mix_r05_seed43) — **Running, Gen 7 sample generation**

- 已完成 Gen 0-6
- 当前 Gen 7 样本生成 3200/25000 (12.8%)
- 预计还需 **数小时**才能完成全部 10 gen

---

### 与 seed42 交叉验证（r=0.2）

seed43 Gen 9 值 (eff_rank=504.08, ppl=13.08) 与 seed42 Gen 10 (eff_rank=511.3, ppl=13.83) 趋势一致，seed43 Gen 10 预期会进一步接近。

需要等 **~5 分钟**后再查一次 exp_017 拿 Gen 10 最终 metrics。要我稍后再查吗？

---
