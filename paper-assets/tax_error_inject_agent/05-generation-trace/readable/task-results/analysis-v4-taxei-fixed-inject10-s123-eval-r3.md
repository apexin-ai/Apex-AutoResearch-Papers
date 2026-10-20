# analysis v4 taxei fixed inject10 s123 eval r3

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject10-s123-eval-r3_20260515T205158_result.json`
- **Structured JSON:** [`be012518bbb1e9460bdb.json`](../../sessions/be/be012518bbb1e9460bdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，EXIT_CODE=0。

## 实验 1: v4-taxei-fixed-inject10-s123-eval-r3

```
exp_id: v4-taxei-fixed-inject10-s123-eval-r3
conclusion: success
success_rate: 0.553
successes: 26
total: 47
by_task_type:
  look_at_obj_in_light:       {total: 6, success: 5, rate: 0.833}
  pick_and_place_simple:      {total: 8, success: 4, rate: 0.500}
  pick_clean_then_place:      {total: 11, success: 5, rate: 0.455}
  pick_cool_then_place:       {total: 7, success: 2, rate: 0.286}
  pick_heat_then_place:       {total: 8, success: 6, rate: 0.750}
  pick_two_obj_and_place:     {total: 7, success: 4, rate: 0.571}
wandb_run_id: N/A (eval 脚本未上报 W&B)
errors: none (bitsandbytes warning 不影响结果)
```

## 实验 2: v4-random-fixed-inject10-s0-eval-r3

```
exp_id: v4-random-fixed-inject10-s0-eval-r3
conclusion: success
success_rate: 0.660
successes: 31
total: 47
by_task_type:
  look_at_obj_in_light:       {total: 6, success: 5, rate: 0.833}
  pick_and_place_simple:      {total: 8, success: 4, rate: 0.500}
  pick_clean_then_place:      {total: 11, success: 7, rate: 0.636}
  pick_cool_then_place:       {total: 7, success: 4, rate: 0.571}
  pick_heat_then_place:       {total: 8, success: 7, rate: 0.875}
  pick_two_obj_and_place:     {total: 7, success: 4, rate: 0.571}
wandb_run_id: N/A
errors: none
```

## 与基准对比

| 配置 | seed | 成功率 | 变化 |
|------|------|--------|------|
| TaxEI 10% s0 (已有) | 0 | 70.2% (33/47) | baseline |
| **TaxEI 10% s123 (新)** | 123 | **55.3% (26/47)** | -14.9pp vs s0 |
| Random 10% s123 (已有) | 123 | 55.3% (26/47) | baseline |
| **Random 10% s0 (新)** | 0 | **66.0% (31/47)** | +10.7pp vs s123 |

关键发现：两组 10% 注入实验的 seed 间方差极大（~15pp），说明之前 s0 vs s123 的单 seed 对比（TaxEI 70.2% vs Random 55.3%）很可能是 seed 噪声而非方法差异。新数据中 Random s0 (66.0%) 反超 TaxEI s123 (55.3%)，进一步印证这一点。

---
