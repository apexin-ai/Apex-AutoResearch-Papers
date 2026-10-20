# infra verify training

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-training_20260520T071648_result.json`
- **Structured JSON:** [`9e988c0bcd64c18562a5.json`](../../sessions/9e/9e988c0bcd64c18562a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 1. 进程存活
两个训练进程均存活：
- `mvp_vanilla_s0`: PID 49175 (cuda:0) ✓
- `mvp_vanilla_s1`: PID 49326 (cuda:1), 子进程 PID 49473 占 39% CPU ✓

### 2. GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 1195 / 97887 MiB |
| 1 | 0% | 1195 / 97887 MiB |
| 2 | 0% | 0 MiB |
| 3 | 0% | 0 MiB |

显存从 559 → 1195 MiB，说明在加载但还没完成。

### 3. 训练 loss
**尚未开始输出 loss**。两个任务都卡在模型加载阶段（NCCL 初始化完成于 15:18，之后没有新日志输出）。

### 4. 错误/警告
- TensorFlow GPU 警告：**无害**，TF 仅用于 RLDS 数据加载
- NCCL `Guessing device ID` 警告：**无害**
- **无致命错误**

### 5. 潜在风险
训练启动命令**缺少关键环境变量**：
- 没有 `source /etc/network_turbo` → HuggingFace 下载走原生网络，速度极慢
- 没有 `HF_HUB_DISABLE_XET=1` → xet 下载在 AutoDL 可能返回 401
- 没有 `HF_HOME=/root/autodl-tmp/.hf_cache` → 模型权重可能下载到根分区（仅剩 12GB）

模型缓存目录仅 4KB（只有 refs/main，无 blobs），openvla-7b 模型权重（~14GB）正在通过 xet 流式加载，进展缓慢。s1 进程有 262 个线程，VmSize 243GB，符合 xet mmap 下载的特征。

### 6. 磁盘
- 根分区：19G/30G used（63%）
- 数据盘：37G/250G used（15%）

### 7. Checkpoint
两个 checkpoint 目录已创建但为空（训练尚未开始）。

### 结论
两个任务**进程正常但尚未开始训练**——卡在模型下载/加载阶段。由于缺少 `network_turbo` 和 `HF_HUB_DISABLE_XET=1`，模型下载可能非常慢（预计 20-40 分钟以上）。如果长时间无进展，建议终止任务、补上环境变量后重新提交。

---
