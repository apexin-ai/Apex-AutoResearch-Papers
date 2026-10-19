# ssh check gpu bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu-bjb1-32546_20260523T032920_result.json`
- **Structured JSON:** [`07b779ddf65c4c394a11.json`](../../sessions/07/07b779ddf65c4c394a11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**全部 6 块 GPU 均被占用，无空闲 GPU。**

- **GPU 0/1/2/4/5**：5 个新 eval 进程（11:24 启动），包括 3 个 adaptive_conformal_crm（τ=0.15/0.25/0.35 on spatial）和 2 个 crm_obs_only（norm=0.2 on spatial, norm=0.05 on object）。均在 task 1/10 早期阶段，预计 1-2 小时完成。
- **GPU 3**：4-suite CRM 训练，epoch 38/50 batch 2250/6316，val_loss 持续下降至 0.005903。预计 ~16:45 完成（剩余 ~5.3 小时）。

之前的 3-direction eval（dirA/B/C）已于 11:10-11:19 全部完成，CRM Spatial eval 确实已在运行（不是 PREPARING 状态）。

报告已写入 `artifacts/gpu_status_bjb1_32546.md`。

---
