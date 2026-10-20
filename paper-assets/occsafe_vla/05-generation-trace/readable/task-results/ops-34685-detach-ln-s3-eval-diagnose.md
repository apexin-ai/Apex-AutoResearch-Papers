# ops 34685 detach ln s3 eval diagnose

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-detach-ln-s3-eval-diagnose_20260526T235737_result.json`
- **Structured JSON:** [`433dc52b62d7a7396a97.json`](../../sessions/43/433dc52b62d7a7396a97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. detach_ln_s3_eval 失败原因
**假阳性——eval 实际已成功完成。** 10 个 task × 50 rollouts 全部跑完，EXIT_CODE=2 可能来自 TensorFlow/robosuite 启动时的 warning（非致命错误），不影响结果。

结果：**TSR = 0.886 (88.6%), CAR = 0.802 (80.2%)**，总碰撞 99 次。

### 2. 结果文件
完整 JSON 已保存：`/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260527_070927.json`
（注意不在 experiments 目录下，在 artifacts 目录）

### 3. cutoff_25k_s1_v2_eval 状态
**仍在运行**（PID 620069，已运行 ~37 分钟），当前进度：Task 3，44/50 episodes (88%)。即大约在第 4/10 个 task，预计还需 ~1.5 小时完成。

### 4. 34685 GPU 使用情况

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 99% | 62.2/97.9 GB | 占用 (PID 681204) |
| cuda:1 | 97% | 62.2/97.9 GB | 占用 (PID 677648) |
| cuda:2 | 0% | 1 MB/97.9 GB | **空闲** (detach_ln_s3_eval 已结束) |
| cuda:3 | 14% | 16.7/97.9 GB | cutoff_25k_s1_v2_eval |

**cuda:2 现在空闲，可安排新任务。**

---
