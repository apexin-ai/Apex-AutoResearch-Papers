# deploy m023 redeploy bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_m023-redeploy-bjb2-28827_20260519T170200_result.json`
- **Structured JSON:** [`f5f601da494428004f37.json`](../../sessions/f5/f5f601da494428004f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

---

## M023 修复报告

### 1. 事故原因
- **无法确定根因**：dmesg 无权限，journalctl 无记录
- 服务器未重启（uptime 146 天）
- load average 38→11 在下降，说明近期大量进程被终止
- **所有 GPU 上的进程都被杀了**，不仅是 3 个目标实验，包括 FMVD (GPU5) 和 OpenVLA (GPU4) 也被杀
- 可能原因：系统级 OOM 或人工批量 kill

### 2. 实验部署状态

| exp_id | GPU | PID | server | status |
|--------|-----|-----|--------|--------|
| eval-argmin-object-k5-seed44-r2 | cuda:1 | 901514 | bjb2-28827 | **已提交** |
| eval-obs-only-spatial-norm02-seed46-r2 | cuda:3 | 901980 | bjb2-28827 | **已提交** |
| eval-vla-only-goal-seed44-r2 | cuda:0 | 902257 | bjb2-28827 | **已提交** |

GPU 0/1/3 刚启动，模型尚在加载中（3 MiB）。

### 3. OpenVLA cuda:4 状态
**已被其他 worker 重启**。PID 900134, 22986 MiB, GPU-Util 47%。tmux session `eval-openvla-object-baseline-seed42` 创建于 01:03:26（早于本次部署）。未触碰。

### 4. GPU 空闲状态
- **cuda:2**：完全空闲，可分配
- **cuda:5**：tmux session `fmvd-calibration-phase1` 存在但 GPU 仅 3 MiB — FMVD 可能在启动中或异常，需关注

### 5. Registry 更新
- `eval-vla-only-goal-seed44`: conclusion → killed ✓
- `eval-openvla-object-baseline-seed42`: conclusion → killed ✓（已被其他 worker 重启）
- `eval-argmin-object-k5-seed44` / `eval-obs-only-spatial-norm02-seed46`: **registry 中无条目**，无法更新

---
