# ops d011 phase1 launch pi05 a1 training v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d011_phase1_launch_pi05_a1_training_v2_20260522T235656_result.json`
- **Structured JSON:** [`1ccee29941523409eb7c.json`](../../sessions/1c/1ccee29941523409eb7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在正常运行。汇总结果：

## D011 Phase 1 启动结果

### 1. PID
- **cuda:0** (λ_sdf=0.005): PID **584408**
- **cuda:1** (λ_sdf=0.01): PID **584493**

### 2. 前几步 Loss

**cuda:0 — λ_sdf=0.005:**
| step | loss | action | sdf | ee |
|------|------|--------|-----|-----|
| 0 | 0.1231 | 0.1203 | 0.1411 | 0.2107 |
| 1 | 0.1173 | 0.1145 | 0.1355 | 0.2102 |
| 2 | 0.1268 | 0.1244 | 0.1418 | 0.1737 |
| 3 | 0.1487 | 0.1463 | 0.1388 | 0.1759 |
| 4 | 0.1345 | 0.1316 | 0.1387 | 0.2213 |

**cuda:1 — λ_sdf=0.01:**
| step | loss | action | sdf | ee |
|------|------|--------|-----|-----|
| 0 | 0.1235 | 0.1203 | 0.1188 | 0.2087 |
| 1 | 0.1177 | 0.1145 | 0.1226 | 0.2026 |
| 2 | 0.1272 | 0.1244 | 0.1195 | 0.1611 |

### 3. GPU 显存
- cuda:0: **19107 MiB** / 97887 MiB (19.5%)
- cuda:1: **19107 MiB** / 97887 MiB (19.5%)

符合预估（~19GB）。

### 4. W&B
**离线模式**（无 online URL）。westd-45947 从未配置 W&B API key，`WANDB_MODE=online` 会直接报错退出。已改为 `WANDB_MODE=offline` 启动。

### 5. 问题
- **W&B API key 缺失**：westd-45947 无 `.netrc`、无 `WANDB_API_KEY` 环境变量、无 wandb config。需要配置 key 才能切换到 online 模式。历史所有 run 都是 offline。
- **无 NaN**，三个 loss 分量都正常
- Phase 1 warmup 已激活（仅训练 SDF decoder 395777 参数 + EE extractor 263171 参数，LoRA 33.47M 冻结）
- 速度约 1.6-2.1 s/it，预计 30000 步约 15-17 小时

---
