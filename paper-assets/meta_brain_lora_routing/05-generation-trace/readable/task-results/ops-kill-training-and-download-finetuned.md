# ops kill training and download finetuned

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_training_and_download_finetuned_20260516T154828_result.json`
- **Structured JSON:** [`b2196e2a9b0a8293eec3.json`](../../sessions/b2/b2196e2a9b0a8293eec3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 训练 Kill — 完成
所有 v2 LoRA universal/spatial 训练进程已终止。

### 2. GPU 状态（4x NVIDIA RTX PRO 6000 Blackwell, 96GB each）

| GPU | 状态 | 占用 |
|-----|------|------|
| 0 | **空闲** | 1 MiB |
| 1 | **空闲** | 1 MiB |
| 2 | **空闲** | 1 MiB |
| 3 | Policy server (PID 894498) | 8.1 GB |

### 3. 正确的 Fine-tuned Checkpoint — 已就绪，无需下载

**路径**: `/root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi/`

- 6.6 GB，`model.safetensors` 完整（无 .aria2）
- openpi 格式（含 `assets/physical-intelligence/libero/norm_stats.json`）
- 已被 policy server 使用中（`--policy.config pi0_libero --policy.dir ...`）

### 4. 对比

| Checkpoint | 路径 | 状态 | 说明 |
|-----------|------|------|------|
| ❌ base model (错误使用的) | `/root/autodl-tmp/checkpoints/pi0_libero/` | LeRobot 格式 | README 明确说 "Base model to fine tune" |
| ✅ **fine-tuned (openpi)** | `/root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi/` | 完整可用 | 正在被 serve_policy_wrapper 使用 |
| ❌ 社区版 (incomplete) | `/root/autodl-tmp/checkpoints/pi0_libero_finetuned/` | model.safetensors.aria2 存在 | 下载未完成 |

**结论**: 不需要额外下载。正确的 fine-tuned checkpoint 已在 `/root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi/`，可直接用于重新训练 LoRA。重训时将 `--checkpoint` 改为此路径即可。

---
