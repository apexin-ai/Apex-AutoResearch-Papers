# deploy westd27271 gpu23

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_gpu23_20260526T064354_result.json`
- **Structured JSON:** [`e7343cd2ab5d085dd4d3.json`](../../sessions/e7/e7343cd2ab5d085dd4d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验部署完成。汇报：

---

## 部署结果

### 修复的问题
1. **GPU 数量**：westd-27271 实际只有 **2 张 GPU**（RTX PRO 6000 Blackwell, 98GB），不是 4 张。已改为与现有实验共享 GPU 0/1（各有 ~70GB 余量，充裕）
2. **SUITE_MODEL_MAP 映射错误**：`libero_spatial` 原映射到不存在的 `openvla-libero-spatial`，已修复为 `openvla-7b-finetuned-libero-spatial`
3. **`--mode none` 无效**：argparse 不支持，已改为 `--mode baseline`

### 实验 1: `eval_openvla_baseline_spatial_seed42_v4` ✅
- **GPU 0** (共享) | PID 112404 | tmux: `eval_spatial_baseline_s42`
- 模型: `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial` ✅ (正确的 Spatial 模型)
- 显存: GPU 0 总占 24.2GB / 97.9GB
- 状态: 模型已加载 (15.1GB)，Task 1/10 评估中

### 实验 2: `eval_openvla_attn_k09_goal_seed43_v4` ✅
- **GPU 1** (共享) | PID 112477 | tmux: `eval_attn_k09_goal_s43`
- 模型: `/root/autodl-tmp/openvla-7b-finetuned-libero-goal` ✅
- Attn pruning: 256 → 230 vision tokens (k=0.9)
- 显存: GPU 1 总占 31.9GB / 97.9GB
- 状态: 模型已加载，Task 1/10 评估中，parent 设为 v3

### 同机已有实验
- GPU 0 PID 11195: l2norm_prune k=0.9 Goal s43 (12:02 启动)
- GPU 1 PID 11378: random_prune k=0.9 Goal s43 (12:02 启动)

---
