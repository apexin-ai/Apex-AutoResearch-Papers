# ops d168 westd38929 smolvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_westd38929_smolvla_20260522T140951_result.json`
- **Structured JSON:** [`5239c1fc1a114950b3b5.json`](../../sessions/52/5239c1fc1a114950b3b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部部署完成，4 个 tmux session 均正常运行。

## 部署汇报

### 服务器状态
| GPU | 显存占用 | 任务 | 状态 |
|-----|---------|------|------|
| cuda:0 | 2708 MiB | SmolVLA Object l2_norm k=0.95 → random k=0.95 | **运行中**，已在跑 episode |
| cuda:1 | 2776 MiB | SmolVLA Spatial baseline → l2_norm → random | **运行中**，Task 0 已有多个 SUCCESS |
| cuda:2 | 10534 MiB | Pi0.5 Long baseline (PID 91245) → SmolVLA Long (自动接力) | **等待中** |
| cuda:3 | 2209 MiB | SmolVLA Goal baseline → l2_norm → random | **运行中**，Task 0 已有多个 SUCCESS |

### 关键信息
- **脚本**: `eval_official_libero.py` 已在 westd-38929 上，无需复制
- **模型**: `/root/autodl-tmp/.hf_cache/smolvla_libero_official/` 完整可用
- **参数修正**: `--mode baseline`（非 `none`），`--mode random_prune`（非 `random`），`--pretrained_dir` 为必需参数
- **GPU 2 接力**: tmux `smolvla_long` session 每 60s 轮询 PID 91245，结束后自动启动 SmolVLA Long (baseline → l2_norm → random)

### 早期日志确认
- **Object (l2_norm)**: Task 0 已跑到 Ep 8，全 FAIL 仅 1 SUCCESS — 符合预期（pruning 会大幅降低 SR）
- **Spatial (baseline)**: Task 0 前 9 ep 中 6 个 SUCCESS — baseline 表现不错
- **Goal (baseline)**: Task 0 前 9 ep 中 6 个 SUCCESS — baseline 表现不错

### 实际命令模板
```bash
CUDA_VISIBLE_DEVICES=X TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache \
python -u eval_official_libero.py \
  --pretrained_dir /root/autodl-tmp/.hf_cache/smolvla_libero_official \
  --mode {baseline,l2_norm,random_prune} \
  --k_ratio 0.95 --suite {libero_object,libero_spatial,libero_goal,libero_10} \
  --num_episodes 50 --gpu 0 --seed 42
```

---
