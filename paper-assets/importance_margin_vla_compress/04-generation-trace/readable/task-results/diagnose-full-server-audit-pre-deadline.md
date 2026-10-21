# diagnose full server audit pre deadline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_server_audit_pre_deadline_20260528T061901_result.json`
- **Structured JSON:** [`720495d9dbaf812a2a42.json`](../../sessions/72/720495d9dbaf812a2a42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 registry 更新完成。以下是完整审计报告：

---

```
[服务器状态]
w27:  cuda:0=OV_l2norm_k095_Long_seed43 (PID 545117, 23min), cuda:1=空闲
cqa1: cuda:0=pi05_l2norm_k05_Long_seed45 (PID 981955, ~4h), cuda:1=空闲, cuda:2=OV_random_k095_goal_seed42_v4 (PID 147686, 33min), cuda:3=空闲
w41:  cuda:0=pi05_random_k085_seed46 (PID 697215, 27min), cuda:1=空闲(已kill), cuda:2=pi05_l2norm_k075_seed46 (PID 697672, 26min), cuda:3=pi05_attn_k07_seed45 (PID 684044, 1h)
w38:  cuda:0=pi05_random_k095_seed45 (PID 155742, 1.5h), cuda:1=空闲, cuda:2=pi05_random_k07_seed45 (PID 156380, 1.5h), cuda:3=pi05_attn_k085_seed46 (PID 218248, 26min)

[收割结果]
eval_pi05_attn_k095_long_seed45_strict_cqa1:   SR=77.8% (389/500) ← DONE
eval_pi05_l2norm_k095_long_seed45_strict_w38:   SR=87.8% (439/500) ← DONE

[C003 处理]
w41:cuda:1 OV Random k=0.95 Long seed43 — 进度<5%(仅23min), 决策=kill+DONE/killed。GPU已释放。

[Phantom RUNNING 清理] (全部8个已更新)
eval_pi05_l2norm_k09_long_seed43_strict_cqa1:   → DONE/success SR=81.2% (406/500)
eval_pi05_l2norm_k095_long_seed43_strict_w38:    → DONE/success SR=85.8% (429/500)
eval_openvla_attn_k075_long_seed42:              → DONE/failed  (TIMEOUT 8/10 tasks, partial SR≈39.8%)
eval_pi05_l2norm_k085_long_seed42:               → DONE/success SR=77.6% (388/500)
eval_openvla_random_k095_object_seed42:          → DONE/success SR=67.4% (337/500)
eval_pi05_random_k07_long_seed42:                → DONE/success SR=62.4% (312/500)
eval_openvla_random_k075_goal_seed42:            → DONE/success SR=72.0% (360/500)
eval_openvla_attn_k075_goal_seed42:              → DONE/success SR=67.4% (337/500)

[空闲 GPU]
w27:cuda:1   (一直空闲)
cqa1:cuda:1  (一直空闲)
cqa1:cuda:3  (phantom完成后空闲)
w41:cuda:1   (C003 kill后空闲)
w38:cuda:1   (一直空闲)
共 5 张 GPU 空闲
```

---
