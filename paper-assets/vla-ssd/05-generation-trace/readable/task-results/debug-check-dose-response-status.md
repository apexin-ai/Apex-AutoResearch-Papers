# debug check dose response status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_dose_response_status_20260518T160240_result.json`
- **Structured JSON:** [`52f3689a15f657b2d68a.json`](../../sessions/52/52f3689a15f657b2d68a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**实验正在运行，无 crash/error。**

### GPU 占用
| GPU | PID | 显存 | 利用率 | 条件 |
|-----|------|------|--------|------|
| 0 | 60326 | 15.5GB / 98GB | 80% | top-4, 8, 12, 16 |
| 1 | 60638 | 15.5GB / 98GB | 84% | top-20, 24, 28, 32 |

### 进度
- 两个 GPU 都在 **Task 0/5** (`open_the_middle_drawer_of_the_cabinet`)
- GPU 0: 1700/12500 calls (~13.6%), ~6.3 calls/s, ETA ~1706s (~28min)
- GPU 1: 1500/12500 calls (~12.0%), ~6.6 calls/s, ETA ~1678s (~28min)
- 每个 GPU 跑 4 个条件 × 5 tasks × 10 demos × 50 steps = 总共每 GPU 12500 calls/task × 5 tasks

### 已完成结果
两个早期结果文件已保存（是之前的小规模试运行，`n_samples=2`）：
- `dose_response_top4.json` — paired_mse mean=0.071, token_divergence=0.5, KL=2.46
- `dose_response_top8.json` — paired_mse mean=0.071, token_divergence=0.5, KL=2.44

这些是只有 1 task × 1 demo × 2 timesteps 的小样本结果，当前正在跑的是完整规模（5 tasks × 10 demos × 50 steps）。

### 预计总时间
每个 task ~33min（含加载），5 tasks → 每 GPU 约 **2.5-3 小时**完成全部条件。

---
