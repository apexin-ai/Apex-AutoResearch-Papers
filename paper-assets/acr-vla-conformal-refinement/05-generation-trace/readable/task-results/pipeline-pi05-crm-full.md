# pipeline pi05 crm full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_pi05-crm-full_20260521T213634_result.json`
- **Structured JSON:** [`9a363215c2de0681bc21.json`](../../sessions/9a/9a363215c2de0681bc21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境状态已确认。Step 3 跳过（Object 未完成）。Spatial 缓存已合并、训练在跑，无需修复。

## 产出报告

### 1. Object CRM checkpoint (bjb1-18228)
- **crm_best.pt 存在**: 2.4M, 路径 `/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt`, 最后更新 05:28 (epoch 22)
- **训练状态**: **未完成**, 当前 epoch 23/50, 进程 PID **800111** 仍在运行（02:21 启动，已 3h+）
- 已保留 5 个 epoch 检查点 (epoch 18-22)

### 2. Spatial CRM (bjb1-18228)
- **缓存已合并**: `obs_features.pt` (471M), `k_samples.pt` (69M), `manifest.json` 完整
  - `n_samples=60250`, `K=10`, `obs_dim=2048`, `action_dim=6`, `h_eff=5`
  - 无需重跑 merge
- **训练在跑**: PID **805017** (03:23 启动), 当前 epoch 18/50, crm_best.pt val_loss=0.007578 (epoch 17)
- **未启动 crm-train-pi05-spatial-v2**（已有训练运行中）
- ⚠️ **Registry 状态陈旧**: registry 标记为 `DONE(failed)`, 但实际进程活跃且进度正常 — 旧失败状态未被更新

### 3. Object Eval 部署
**跳过（步骤 3d）**: Object 训练仍在 epoch 23/50，full checkpoint 尚未生成。

### 额外发现
- bjb1-18228 上已有 **2 个 object eval 在跑**（seed 42 PID 804196, seed 43 PID 804568），使用的是当前 epoch-22 的 intermediate `crm_best.pt`，**非最终 50-epoch 训练的产物**
- 这些 eval 结果只反映中途 checkpoint 性能；如果 director 要求"最终"对比，需要在 Object 训练完成后重跑 eval

### 阻塞点
- Object 训练还需约 27 epoch (~4h 估计), Spatial 还需 32 epoch (~5h 估计)
- 8 天 DDL 内时间充足，但若部分 epoch 后训练崩溃将拖延 eval 阶段

---
