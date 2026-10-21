# ops fix gpu binding evals

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_gpu_binding_evals_20260525T130917_result.json`
- **Structured JSON:** [`8c313187d0cf10c43827.json`](../../sessions/8c/8c313187d0cf10c43827.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个进程全部存活，运行 ~1 分钟，正在加载模型/checkpoint（尚未分配 GPU 显存）。

---

**汇总：**

| 项目 | 状态 |
|------|------|
| Kill 260022/260023/260024 | ✅ ALL_KILLED |
| spatial_bowl (PID 168730) | ✅ cuda:0，运行 3h07m，27GB 显存 |
| s0_l005 (PID 275278) | ✅ 存活，--gpu 1，加载中 |
| s0_l01 (PID 275279) | ✅ 存活，--gpu 2，加载中 |
| s2_l01 (PID 275280) | ✅ 存活，--gpu 3，加载中 |

**nvidia-smi 完整输出：**
```
GPU 0: RTX PRO 6000  27045MiB/97887MiB  PID 168730 (spatial_bowl)
GPU 1: RTX PRO 6000      3MiB/97887MiB  (eval 加载中)
GPU 2: RTX PRO 6000      3MiB/97887MiB  (eval 加载中)
GPU 3: RTX PRO 6000      3MiB/97887MiB  (eval 加载中)
```

3 个 eval 进程参数中 `--gpu` 已正确指向 1/2/3，脚本内部 L1127 会将 `CUDA_VISIBLE_DEVICES` 设为对应物理 GPU ID。已用 6 轮 SSH，达到硬约束上限。

**待确认：** 模型加载完成后（约 2-5 分钟），可再次 `nvidia-smi` 确认显存分配到 cuda:1/2/3。如果需要我后续验证，请告知。

---
