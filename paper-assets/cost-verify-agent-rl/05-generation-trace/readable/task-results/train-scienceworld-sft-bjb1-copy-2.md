# train scienceworld sft bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_scienceworld_sft_bjb1_20260524T042113_result.json`
- **Structured JSON:** [`1d9c96f1679bca03c6b0.json`](../../sessions/1d/1d9c96f1679bca03c6b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无法启动。** 详细情况：

### GPU 问题（阻塞）
nvidia-smi 只显示 **1 张 GPU（cuda:0）**，已被 `actor_rollout_update_actor`（hsweep）占用 44394/97887 MiB、GPU-Util 97%。**没有 cuda:1。** 服务器上物理可见只有 1 张 RTX PRO 6000。

### SFT 数据（缺失）
`/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl` **不存在**。现有 4 版 expert_sft 数据（v1-v4, 共 2460-2546 行）全是 **ALFWorld** 的，不是 ScienceWorld。

### 可用组件
| 组件 | 状态 | 路径 |
|------|------|------|
| 数据生成脚本 | 存在（westd 备份） | `/root/autodl-tmp/westd_backup/cost-verify-agent-rl/generate_scienceworld_sft.py` |
| scienceworld 包 | 已安装 | `import scienceworld` 成功 |
| SFT 训练脚本 | 存在 | `/root/cost-verify-agent-rl/scripts/sft_train.py`（单卡 HF Trainer） |
| Base model | 存在 | `/root/autodl-tmp/models/Qwen/Qwen3-1___7B/` |
| 磁盘 | 97GB 可用 | `/root/autodl-tmp/` |

### 需要决定
1. **GPU 怎么解决？** 等 hsweep 跑完腾出 cuda:0？还是用别的服务器？还是服务器实际有 2 卡但被 CUDA_VISIBLE_DEVICES 限制了？
2. **数据生成可以先跑**（不需要 GPU，纯 CPU），生成 ScienceWorld SFT 数据。是否现在先启动数据生成？

---
