# infra fix vlm restart training

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-vlm-restart-training_20260515T144123_result.json`
- **Structured JSON:** [`c2d4ec2a0a5a85dd86ee.json`](../../sessions/c2/c2d4ec2a0a5a85dd86ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡训练完全正常：

| | Baseline (GPU 0) | IMM Anchor (GPU 1) |
|---|---|---|
| **当前 step** | 100/30000 | 50/30000 |
| **Loss** | 0.0096 | 0.3148 |
| **SPS** | 3.7 steps/s | 2.9 steps/s |
| **GPU Util** | 46% | 79% |
| **GPU Mem** | 2279 MiB | 2459 MiB |

---

**总结**：

1. **load_vlm_weights patch**: hub snapshots 下的 config.json 已 patch 为 `false`（之前只 patch 了另一份）
2. **VLM backbone**: 完整缓存在 `/root/autodl-tmp/.hf_cache/hub/models--HuggingFaceTB--SmolVLM2-500M-Video-Instruct/`
3. **额外修复**:
   - `pretrained` 路径改为本地绝对路径 `/root/autodl-tmp/.hf_cache/lerobot/smolvla_base`（原 HF repo ID 在 hub cache 中缺少 safetensors）
   - `HF_HUB_OFFLINE=0` 覆盖 train.py 的 setdefault（数据集 API 需要网络）
   - 加入 `source /etc/network_turbo` + SSL 证书（AutoDL 网络要求）
   - `WANDB_MODE=offline`（服务器无 wandb API key）
4. **训练状态**: 双卡稳定运行，baseline sps=3.7, IMM sps=2.9

---
