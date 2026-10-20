# infra setup westd 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_setup_westd_34685_20260520T112745_result.json`
- **Structured JSON:** [`9c40d098b6b119878e6d.json`](../../sessions/9c/9c40d098b6b119878e6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 搭建完成汇报

| 项目 | 状态 |
|------|------|
| **SSH 连接 + 免密登录** | OK（ed25519 密钥已配置） |
| **GPU** | 4x NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB/卡) |
| **CUDA** | Driver 580.95.05, CUDA 13.0（PyTorch 用 cu128） |
| **磁盘** | 根分区 30G (用 12G/剩 19G), 数据盘 350G (用 22G/剩 329G) |
| **环境** | conda env `occsafe` (Python 3.10.20), torch 2.11.0+cu128 |
| **依赖** | transformers 4.40.1 (openvla-oft fork), einops, accelerate, wandb, h5py, opencv, scipy, datasets, robosuite 1.4.1, libero, openvla-oft, dlimp 全部就绪 |
| **代码同步** | openvla-oft (含 local patches), transformers-openvla-oft, dlimp_openvla, occ_pipeline, occ_data*, eval, artifacts, *.py 全部同步 |
| **模型** | openvla-7b (15G) 已同步到 /root/autodl-tmp/models/ |
| **数据** | data (2G) + libero_datasets (5.4G) 已同步 |

**未同步项**: checkpoints (45G) — 如需要可后续同步。

---
