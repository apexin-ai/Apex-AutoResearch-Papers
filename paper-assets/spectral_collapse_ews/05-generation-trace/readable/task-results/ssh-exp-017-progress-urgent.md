# ssh exp 017 progress urgent

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_017_progress_urgent_20260523T031116_result.json`
- **Structured JSON:** [`d70d1d86875f0b3faf7c.json`](../../sessions/d7/d70d1d86875f0b3faf7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### exp_017 (r=0.2, seed43) — Running, Gen 10 生成中 (31360/40000)

即将完成，只差 Gen 10 的生成+训练+评估。

| Gen | eff_rank | PPL | D-4 | train_loss |
|-----|----------|------|------|------------|
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
| 10 | *生成中* | — | — | — |

seed42 参考值: eff_rank=511.3, PPL=13.83, D-4=0.520 → seed43 的 eff_rank/PPL 走势一致，D-4 偏低（0.306 vs 0.520 @ Gen 9）。

---

### exp_018 (r=0.5, seed43) — Running, Gen 6 训练中 (Step 300)

大约完成 60%。

| Gen | eff_rank | PPL | D-4 | train_loss |
|-----|----------|------|------|------------|
| 0 | 417.55 | 9.55 | 0.7415 | — |
| 1 | 475.91 | 10.08 | 0.6705 | 1.9836 |
| 2 | 488.01 | 10.41 | 0.5708 | 1.9122 |
| 3 | 493.94 | 10.73 | 0.5438 | 1.7120 |
| 4 | 503.05 | 11.12 | 0.4632 | 1.6435 |
| 5 | 510.11 | 11.60 | 0.4189 | 1.5218 |
| 6 | *训练中* | — | — | Step 300 loss=1.3394 |

seed42 参考值: eff_rank=554.5, PPL=15.20, D-4=0.095 → 走势匹配，r=0.5 的 eff_rank 增长更快（510 @ Gen 5 vs exp_017 的 492）。

---
