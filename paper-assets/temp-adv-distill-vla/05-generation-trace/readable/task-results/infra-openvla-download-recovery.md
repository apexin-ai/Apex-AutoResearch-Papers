# infra openvla download recovery

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_openvla-download-recovery_20260515T080600_result.json`
- **Structured JSON:** [`a34b6bbf5a2cec2cd829.json`](../../sessions/a3/a34b6bbf5a2cec2cd829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Download confirmed progressing steadily. Here's the full status report:

---

## OpenVLA 模型状态

**路径**: `/root/autodl-tmp/models/openvla-7b-finetuned-libero-spatial/`

| Shard | 大小 | 状态 |
|-------|------|------|
| model-00001-of-00004.safetensors | 4.6GB (预期) | **正在下载** — curl PID 20135, ~1MB/s, 当前 48MB |
| model-00002-of-00004.safetensors | 4.7G | 完整 |
| model-00003-of-00004.safetensors | 4.7G | 完整 |
| model-00004-of-00004.safetensors | 251M | 完整 |

- 总模型大小: 15.08GB (index metadata)
- config.json / tokenizer 等辅助文件齐全
- **Shard 1 之前损坏**(仅 5.5M),已删除并重新用 curl 下载
- **预计完成时间**: ~17:35 北京时间(约 80 分钟)

## 磁盘空间

| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| 根分区 (/) | 30G | 9.8G (33%) | 21G |
| 数据盘 (/dev/sda2) | 879G | 17G (3%) | 817G |

## 已有资源

- **VIP 模型**: `/root/temp-adv-distill-vla/vip/`
- **MLP checkpoints**: `artifacts/gate1b_mlp_layer_0.pt` (2.3M), `gate1b_mlp_multitask.pt` (2.3M)
- **IQL checkpoints**: `artifacts/iql_checkpoints/`
- **Gate 2 结果**: `artifacts/gate2_results.json` + ROC curves + advantage dist plots
- **VIP features**: `artifacts/vip_features/` (per-task) + `vip_features_all/`
- **LIBERO 数据**: 仅 `libero_object` (10 tasks) — **无 `libero_spatial`**（但 OpenVLA 模型是 libero_spatial fine-tuned）

## 注意事项

1. Shard 1 下载用 `curl -L` 后台运行 (nohup, PID 20135), 速度受 AutoDL 代理限制
2. HF Python 库和 `hf` CLI 均因 xet bridge SSL 问题在此服务器上不可靠,curl 最稳定
3. `libero_spatial` 数据集缺失 — 如果后续实验需要,需单独下载

---
