# analyze eval crm k1 object seed44 plan702

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-k1-object-seed44-plan702_20260520T164832_result.json`
- **Structured JSON:** [`b38cc1b5b4e84668e906.json`](../../sessions/b3/b38cc1b5b4e84668e906.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：eval-crm-k1-object-seed44-plan702

### 异常：脚本崩溃

日志显示脚本在 `evaluate.py:466` 崩溃：
```
UnboundLocalError: cannot access local variable 'unc_dim' where it is not associated with a value
```

但结果 JSON 已写入且包含完整的 10 tasks × 10 rollouts 数据，说明评估本身已完成，崩溃发生在后处理阶段。

### 总体结果

| 指标 | 值 |
|------|-----|
| **overall_success_rate** | **0.1** |
| 总 rollouts | 100 (10 tasks × 10 rollouts) |
| 总成功数 | 10 |
| mode | crm_k1_accg |
| max_correction_norm | 0.2 |
| seed | 44 |

### Per-task Breakdown

| Task | Success Rate | Successes / Total |
|------|-------------|-------------------|
| pick_up_the_alphabet_soup_and_place_it_in_the_basket | 0.0 | 0/10 |
| pick_up_the_cream_cheese_and_place_it_in_the_basket | 0.0 | 0/10 |
| pick_up_the_salad_dressing_and_place_it_in_the_basket | 0.2 | 2/10 |
| pick_up_the_bbq_sauce_and_place_it_in_the_basket | 0.2 | 2/10 |
| pick_up_the_ketchup_and_place_it_in_the_basket | 0.0 | 0/10 |
| pick_up_the_tomato_sauce_and_place_it_in_the_basket | 0.1 | 1/10 |
| pick_up_the_butter_and_place_it_in_the_basket | 0.0 | 0/10 |
| pick_up_the_milk_and_place_it_in_the_basket | 0.0 | 0/10 |
| pick_up_the_chocolate_pudding_and_place_it_in_the_basket | 0.3 | 3/10 |
| pick_up_the_orange_juice_and_place_it_in_the_basket | 0.2 | 2/10 |

### 要点

- **Overall success rate = 0.1 (10%)**，CRM K=1 ACCG 在 LIBERO-Object seed=44 上表现较低
- 4/10 tasks 完全失败（success_rate=0.0）
- 最好的 task 是 chocolate_pudding（0.3）
- `unc_dim` 未绑定的 bug 需要修复，虽然不影响评估结果本身，但会导致后续处理（可能是 W&B logging 或 uncertainty 分析）未执行

---
