# analysis transfer v2 1000step

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer-v2-1000step_20260520T001723_result.json`
- **Structured JSON:** [`77bd52fc44c8bcbe47bd.json`](../../sessions/77/77bd52fc44c8bcbe47bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据充分。汇总判断：

```
[L_transfer 1000-step] L_xfr=4.05 (step 999) | pos_count_avg≈1.5 | hm_ent=6.5 | hm_max=0.015 | dec_gnorm≈0.04
L_xfr 趋势: step 300→4.156, 500→4.143, 800→4.170, 900→4.181, 999→4.052, 1100→4.210
chance_level=5.55 (queue_size=256, ln(256)=5.55)
verdict: PATH_C
理由: L_xfr 在 4.05-4.21 范围内完全平坦，1100步无下降趋势（甚至微升）。
      transfer_grad_norm 从 0.22→0.08 逐步萎缩，grad_ratio 仅 0.37%，
      L_xfr 对模型更新几乎无影响力。heatmap 虽从 ent=8.7 降至 6.5（有空间聚焦），
      但 hm_max 仅 0.015-0.02，无法产生有效正样本对。
      训练已被 SIGTERM 终止（08:17:03），实际跑到 step 1102。
```

补充诊断：pos=0 的 step 占比过高（约 40-50%），说明 heatmap 峰值不足以稳定匹配正样本。transfer loss 在有正样本时恒定 ~4.17 = 完全随机猜测水平（对比 chance=5.55 虽低，但 1000 步零下降趋势 = 表征未在学习跨实例 affordance 迁移）。

---
