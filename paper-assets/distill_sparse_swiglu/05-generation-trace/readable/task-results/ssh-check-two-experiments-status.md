# ssh check two experiments status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_two_experiments_status_20260522T182246_result.json`
- **Structured JSON:** [`9fc3a192e7ffb1977bb0.json`](../../sessions/9f/9fc3a192e7ffb1977bb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== kl50_global_s123_downstream_v2 ==
状态: 完成
时间: 2026-05-23 01:43:17
⚠️ 只跑了 4 个 task（配置里 tasks="arc_challenge,winogrande,mmlu,gsm8k"），缺 hellaswag/piqa/boolq

指标:
  arc_challenge  acc_norm = 0.3916
  winogrande     acc      = 0.6401
  mmlu           acc      = 0.2908
  gsm8k          exact_match = 0.0341

== perlayer_kl_k4_50_s42 ==
状态: 训练完成，eval 阶段中断（进程已退出，GPU 空闲，无 error 日志）
训练: 1000/1000 steps 完成，耗时 ~1857s (~31min)
  avg_kl = 0.1267 (最终 step)
  avg_sparsity ≈ 0.496
Checkpoint:
  predictor_perlayer_kl_k4.pt        (145 MB, final)
  predictor_perlayer_kl_k4_step_500.pt  (435 MB)
  predictor_perlayer_kl_k4_step_1000.pt (435 MB)
Eval 结果: 无。日志最后一行是 "Eval mode: all layers masked simultaneously (inference config)"，之后无输出，进程静默退出。可能 OOM 或被 kill。
```

**需要关注的问题：**
1. **kl50_global_s123_downstream_v2** 只评估了 4/7 个 task，缺 hellaswag、piqa、boolq。需要补跑或确认这是否符合预期。
2. **perlayer_kl_k4_50_s42** 训练成功但 eval 中断，需要单独跑 PPL eval（和/或 downstream eval）来获取结果。

---
