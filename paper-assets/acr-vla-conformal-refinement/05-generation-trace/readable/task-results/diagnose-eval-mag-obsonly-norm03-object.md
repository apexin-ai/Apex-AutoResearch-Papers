# diagnose eval mag obsonly norm03 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-mag-obsonly-norm03-object_20260516T073948_result.json`
- **Structured JSON:** [`7d8c3a9c695fab3d8280.json`](../../sessions/7d/7d8c3a9c695fab3d8280.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败原因
**误报。实验实际已成功完成。** 监控系统检测到进程退出后判定为失败，但日志和 JSON 输出均显示全部 10 个 task × 10 rollouts = 100 次评估已跑完，进程是正常退出。

### JSON 数据状态
文件 `/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json` **存在且完整**。10 个 task 全部有结果：

| Task | SR |
|------|-----|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 30% (3/10) |
| bbq_sauce | 30% (3/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 20% (2/10) |
| milk | 20% (2/10) |
| chocolate_pudding | 50% (5/10) |
| orange_juice | 30% (3/10) |

**Overall SR = 19.0% (19/100)** — 与 ROADMAP 声称的 19% 完全一致。

### GPU cuda:5 当前状态
空闲可用：1 MiB / 24564 MiB，利用率 0%。

### 进程状态
PID 103028 和 103034 均已退出（正常结束）。

### 是否需要重试
**不需要。** 数据完整有效，只需将此实验在 registry 中标记为成功并录入 SR=19%。

### 完整日志尾部（最后 50 行关键内容）

```
[pick_up_the_salad_dressing_and_place_it_in_the_basket] success rate: 30.0% (3/10)
[pick_up_the_bbq_sauce_and_place_it_in_the_basket] success rate: 30.0% (3/10)
[pick_up_the_ketchup_and_place_it_in_the_basket] success rate: 0.0% (0/10)
[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 10.0% (1/10)
[pick_up_the_butter_and_place_it_in_the_basket] success rate: 20.0% (2/10)
[pick_up_the_milk_and_place_it_in_the_basket] success rate: 20.0% (2/10)
[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 50.0% (5/10)
[pick_up_the_orange_juice_and_place_it_in_the_basket] success rate: 30.0% (3/10)

============================================================
Overall success rate (crm_obs_only): 19.0% (19/100)
============================================================
[eval] Results saved to logs/eval_object_obs_only_norm03.json
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
```

日志末尾无 traceback、无 OOM、无异常——正常结束。监控系统可能因进程退出后没有写 sentinel 文件或 W&B 记录而误判为失败。

---
