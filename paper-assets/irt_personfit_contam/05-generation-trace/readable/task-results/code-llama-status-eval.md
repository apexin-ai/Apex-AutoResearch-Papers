# code llama status eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-status-eval_20260520T225334_result.json`
- **Structured JSON:** [`47ec3931e79284b57ec2.json`](../../sessions/47/47ec3931e79284b57ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 1. 训练状态（全部完成）

| GPU | 条件 | 训练时长 | 最终 loss | epoch |
|-----|------|---------|-----------|-------|
| 0 | clean | 1170s | 1.419 | 3 |
| 1 | contam_15 | 1573s | 1.455 | 3 |
| 2 | contam_50 | 2850s | 1.451 | 3 |

## 2. Eval 结果

| 条件 | lz* | accuracy | theta_mle | acc_seen | acc_unseen | lz*_seen | lz*_unseen |
|------|-----|----------|-----------|----------|------------|----------|------------|
| clean | **0.8175** | 0.5914 | -0.6661 | — | 0.5914 | — | 0.8175 |
| contam_15 | **-2.6572** | 0.6654 | -0.2761 | 0.7707 | 0.6469 | -0.4321 | -2.2654 |
| contam_50 | **-2.8581** | 0.6983 | -0.1490 | 0.7573 | 0.6394 | -1.0154 | -2.0390 |

## 3. Δlz*（vs clean）

| 条件 | Δlz* |
|------|------|
| contam_15 | **-3.4747** |
| contam_50 | **-3.6755** |

## 4. 跨模型对比（Llama vs Qwen pilot）

| | Qwen (n=3) | Llama (n=1) |
|---|---|---|
| clean lz* | 7.345 (mean) | 0.8175 |
| contam_15 lz* | 3.005 | -2.6572 |
| contam_15 Δlz* | ~-4.34 | -3.4747 |

关键发现：
- Llama clean 的 lz* = 0.8175（正值，符合预期——无污染时 response pattern 合理）
- 污染后 lz* 大幅下降至负值（-2.66 ~ -2.86），**person-fit 统计量明确检测到了污染**
- contam_15 → contam_50 差异不大（-2.66 vs -2.86），15% 污染已足够触发显著异常
- Llama 的 clean lz* 远低于 Qwen（0.82 vs 7.35），说明 Llama 基线 response pattern 更"规整"

## 5. llama_summary.json 已保存

```json
{
  "model": "Llama-3.1-8B-Instruct",
  "conditions": {
    "clean": {"theta_mle": -0.6661, "lz_star": 0.8175, "accuracy_overall": 0.5914, "n_items": 14042, "n_seen": 0},
    "contam_15": {"theta_mle": -0.2761, "lz_star": -2.6572, "accuracy_overall": 0.6654, "n_seen": 2106, "n_unseen": 11936},
    "contam_50": {"theta_mle": -0.1490, "lz_star": -2.8581, "accuracy_overall": 0.6983, "n_seen": 7021, "n_unseen": 7021}
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "model": "Llama-3.1-8B-Instruct",
    "conditions": {
      "clean": {
        "theta_mle": -0.6661,
        "lz_star": 0.8175,
        "accuracy_overall": 0.5914,
        "n_items": 14042,
        "n_seen": 0
      },
      "contam_15": {
        "theta_mle": -0.2761,
        "lz_star": -2.6572,
        "accuracy_overall": 0.6654,
        "n_seen": 2106,
        "n_unseen": 11936
      },
      "contam_50": {
        "theta_mle": -0.149,
        "lz_star": -2.8581,
        "accuracy_overall": 0.6983,
        "n_seen": 7021,
        "n_unseen": 7021
      }
    }
  }
}
```

</details>

---
