# ops verify fix depth 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-fix-depth-10894_20260522T073302_result.json`
- **Structured JSON:** [`94a4b2dc1f7eb3176093.json`](../../sessions/94/94a4b2dc1f7eb3176093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**Reviewer 的报告有误——depth_s2/s3 均正常运行，GPU 并非空闲。**

### 1. depth_s2/s3 实际状态

| 实验 | Registry PID | 实际 Wrapper PID | 训练进程 PID | GPU | 利用率 | 显存 | 当前 Step | 速度 |
|------|-------------|-----------------|-------------|-----|-------|------|----------|------|
| depth_s2 | 942037 ✅ | 942037 | 942117 | cuda:2 | 99% | 62200/97887 MiB | ~1805/50005 | ~1.08 it/s |
| depth_s3 | 940106 ❌→942187 | 942187 | 942329 | cuda:3 | 99% | 62194/97887 MiB | ~1810/50005 | ~1.07 it/s |

- **depth_s2** step 1800: depth_loss=0.0719, action_loss=0.2031
- **depth_s3** step 1800: depth_loss=0.1442, action_loss=0.2305
- depth_s3 的 registry PID 已从 940106 更新为 942187（旧 PID 是死的 shell wrapper，实际训练子进程一直在跑）

### 2. Ablation checkpoint 清理

4 个目录均已删除（`ablation_random_occ_s0/s1`、`ablation_occ_detach_s0/s1`）。

### 3. 代码/数据

无需传输——westd-10894 上的代码和数据完整，两个训练已在正常使用 depth head。

### 4. 磁盘状态

`/root/autodl-tmp`: 250G 总量，37G 已用，214G 可用（15%）。checkpoint 目录仅 4K（step 还没到 save_freq=10000）。

### 5. 其余 GPU

- GPU 0 (95%): ablation_random_occ_s2 (PID 932695)
- GPU 1 (78%): ablation_occ_detach_s2 (PID 932909)

4 张卡全部满载运行，无需任何修复操作。

---
