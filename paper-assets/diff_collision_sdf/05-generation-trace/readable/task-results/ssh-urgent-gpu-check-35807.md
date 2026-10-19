# ssh urgent gpu check 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_gpu_check_35807_20260520T105514_result.json`
- **Structured JSON:** [`9b611249a778220ec28f.json`](../../sessions/9b/9b611249a778220ec28f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**系统误报，4 卡均在跑。**

| GPU | 实验 | PID | Uptime | Step | Loss | Speed | VRAM | 状态 |
|-----|------|-----|--------|------|------|-------|------|------|
| 0 | baseline_spatial_bowl_seed0_v3 | 100319 | 12h40m | 12487/30000 (42%) | 0.0151 | ~3.6s/it | 37358/97887 MiB | ✅ 正常 |
| 1 | baseline_spatial_bowl_seed1_v3 | 94453 | 12h52m | 12782/30000 (43%) | 0.0070 | ~3.5s/it | 37358/97887 MiB | ✅ 正常 |
| 2 | baseline_object_pudding_seed0_v3 | 95429 | 12h52m | 12990/30000 (43%) | 0.0058 | ~3.3s/it | 37358/97887 MiB | ✅ 正常 |
| 3 | a1_sdf_spatial_bowl_s0_v3 | 185994 | 2h50m | 8850/30000 (30%) | 0.2146 | ~3.5s/it | 13376/97887 MiB | ✅ 正常 |

**磁盘:**
- `/` : 15G / 30G (50%)
- `/root/autodl-tmp` : 267G / 350G (77%)

**分析:**
- GPU 0-2 满载 100% util，3 个 baseline 进度一致 (~42-43%)，loss 已降到 0.005-0.015 区间
- GPU 3 (PID 185994 A1 训练) nvidia-smi 瞬时读数 0% util，但进程活跃（CPU 68%，有大量 torch._inductor compile workers），日志持续推进。**瞬时采样偶尔会抓到 GPU idle 间隙，不代表空闲。** 该实验从 step 6000 resume，已跑到 8850
- A1 的 loss (0.21) 明显高于 baseline (0.005-0.015)，因为 A1 才跑到 30%，且从 step 6000 resume 后 loss 还在下降中
- 系统误报原因：很可能是监控采样恰好命中 GPU 3 的计算间隙，加上 GPU 3 VRAM 占用（13GB）远低于其他卡（37GB），被判定为"空闲"

**结论：4 个实验全部正常运行，无需干预。**

---
