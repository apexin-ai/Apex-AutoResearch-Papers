# ops training status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-status-check_20260522T125311_result.json`
- **Structured JSON:** [`10a78ac18cbd7a1fcbbf.json`](../../sessions/10/10a78ac18cbd7a1fcbbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | 服务器/GPU | PID | 当前 Step | 进度 | 速度 | 关键 Loss (最近 AUX) | 剩余时间 |
|------|-----------|-----|----------|------|------|---------------------|---------|
| cutoff_s0 | 34685/cuda:0 | 136941 | 14174 | 28% | ~1.03 it/s | (截断不可见) | ~9h40m |
| depth_s0 | 34685/cuda:1 | 131535 | 16146 | 32% | ~1.06 it/s | occ=0.0000 depth=0.0206 action=0.0991 | ~8h52m |
| depth_s1 | 34685/cuda:2 | 131682 | 16110 | 32% | ~1.06 it/s | occ=0.0000 depth=0.0204 action=0.1001 | ~8h53m |
| cutoff_s1 | 34685/cuda:3 | 131898 | 16159 | 32% | ~1.07 it/s | occ=0.0099 depth=0.0000 action=0.1108 | ~8h47m |
| random_occ_s2 | 10894/cuda:0 | 932619 | 22794 | 46% | ~1.07 it/s | (刚存 ckpt@20000) | ~7h04m |
| detach_s2 | 10894/cuda:1 | 932767 | 22804 | 46% | ~1.08 it/s | (刚存 ckpt@20000) | ~7h00m |
| depth_s2 | 10894/cuda:2 | 942037 | 19669 | 39% | ~1.07 it/s | occ=0.0000 depth=0.1039 action=0.1221 | ~7h53m |
| depth_s3 | 10894/cuda:3 | 942187 | 19657 | 39% | ~1.07 it/s | (截断不可见) | ~7h53m |

**备注：**
- westd-34685 GPU 利用率瞬时 0%（内存 62GB/98GB 已占满），可能是采样时恰在 step 间隙，日志显示仍在正常推进
- westd-10894 GPU 利用率 98-99%，运行正常
- cutoff_s0 比同服务器其他实验落后 ~2000 步（PID 更高，应是晚启动）
- random_occ_s2 和 detach_s2 刚完成 step 20000 的 checkpoint 保存和模型合并

**磁盘：**
| 服务器 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| westd-34685 | 350G | 111G | 240G | 32% |
| westd-10894 | 250G | 126G | 125G | 51% |

---
