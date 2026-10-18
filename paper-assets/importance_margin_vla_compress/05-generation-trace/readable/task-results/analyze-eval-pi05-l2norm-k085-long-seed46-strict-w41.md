# analyze eval pi05 l2norm k085 long seed46 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k085_long_seed46_strict_w41_20260528T105550_result.json`
- **Structured JSON:** [`c8375612b71731591af9.json`](../../sessions/c8/c8375612b71731591af9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 实验结果 ===
exp_id: eval_pi05_l2norm_k085_long_seed46_strict_w41
overall_success_rate: 78.6%
per_task: {T0_alphabet_soup_tomato: 92%, T1_cream_cheese_butter: 94%, T2_stove_moka_pot: 92%, T3_black_bowl_drawer: 100%, T4_white_mug_left_plate: 76%, T5_book_back_shelf: 98%, T6_white_mug_plate_yellow: 4%, T7_alphabet_soup_cream: 80%, T8_both_moka_pots_stove: 54%, T9_yellow_white_mug_microwave: 96%}
conclusion: success
5-seed 统计: [77.6, 78.6, 76.6, 79.2, 78.6] → mean=78.1% ± 1.03pp
```

Keep ratio 验证：日志确认 `n_keep=217/256`（217/256=0.848≈0.85），与配置一致。无错误，EXIT_CODE=0。第 5 seed (78.6%) 落在 4-seed 分布范围内，5-seed 标准差从 1.14pp 收窄至 1.03pp。

---
