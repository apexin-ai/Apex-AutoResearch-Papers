# ssh check status westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_status_westd35807_20260520T081942_result.json`
- **Structured JSON:** [`ea612899765966751296.json`](../../sessions/ea/ea612899765966751296.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 训练进度

| GPU | 实验 | Step/30000 | Loss | LR | Speed(s/it) | VRAM |
|-----|------|-----------|------|----|-------------|------|
| 0 | baseline_spatial_bowl_s0_v2 | **9588**/30000 (32%) | 0.0165 | 2.05e-05 | ~3.5 | 37367/97887 MiB |
| 1 | baseline_spatial_bowl_s1_v2 | **9871**/30000 (33%) | 0.0138 | 2.02e-05 | ~3.5 | 37367/97887 MiB |
| 2 | baseline_object_pudding_s0_v2 | **9940**/30000 (33%) | 0.0108 | 2.01e-05 | ~3.4 | 37367/97887 MiB |
| 3 | a1_sdf_spatial_bowl_s0_v3 | **6816**/30000 (23%) | 0.2458 | 2.28e-05 | ~3.5 | 13385/97887 MiB |

## 进程状态

| PID | 运行时长 | CPU% | 状态 |
|-----|---------|------|------|
| 100319 | 9h44m | 125% | 存活 |
| 94453 | 9h57m | 126% | 存活 |
| 95429 | 9h56m | 125% | 存活 |
| 181881 | 49m | 0% | 存活但 GPU util=0% |

**a1 异常**：PID 181881 运行 49 分钟，GPU 利用率 0%，VRAM 仅 13GB（其他实验 37GB）。从 step 6000 resume 后到 6816，loss 仍在 0.23-0.28 范围无下降趋势。GPU util=0% 表明可能卡住或在做非 GPU 操作。

## 磁盘

```
/dev/md127  350G  144G  207G  42%  /root/autodl-tmp
```

磁盘充裕。

## Checkpoint 轮转

| 实验 | 目录 | 子目录数 | 内容 | 轮转正常? |
|------|------|---------|------|----------|
| baseline_spatial_bowl_seed0 | `.../baseline_spatial_bowl/baseline_spatial_bowl_seed0/` | **2** | 6000, 8000 | ✅ ≤3 |
| baseline_spatial_bowl_seed1 | `.../baseline_spatial_bowl/baseline_spatial_bowl_seed1/` | **2** | 6000, 8000 | ✅ ≤3 |
| baseline_object_pudding_seed0 | `.../baseline_object_pudding/baseline_object_pudding_seed0/` | **2** | 6000, 8000 | ✅ ≤3 |
| a1_sdf_spatial_bowl_seed0 | `.../a1_sdf_spatial_bowl/a1_sdf_spatial_bowl_seed0/` | **2** | 5000, 6000 | ✅ ≤3 |

轮转正常，所有目录 ≤3 个 checkpoint。

---

**需关注**：a1 (GPU:3) 的 GPU 利用率为 0%、VRAM 远低于其他实验，且 loss 在 ~0.25 附近未下降。可能需要检查该进程是否卡住。

---
