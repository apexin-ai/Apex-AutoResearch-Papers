# infra gpu util investigation

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-util-investigation_20260515T161012_result.json`
- **Structured JSON:** [`9ddd7d6c5de9296337b1.json`](../../sessions/9d/9ddd7d6c5de9296337b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已经收集完毕。以下是完整分析：

---

## 排查结果

### 现状概览

| 指标 | GPU 0 | GPU 1 |
|------|-------|-------|
| 显存 | 2,281 MiB / 97,887 MiB (2.3%) | **0 MiB (空闲)** |
| 利用率 | 0%~39% 波动 | 0% |
| 功耗 | 118~137W / 600W | 37W (idle) |
| 进程 | PID 31871 (baseline) | **无进程 — IMM anchor 已停止** |

**GPU 1 上的 IMM anchor (PID 32009) 已不存在。** 只有 baseline 在跑。

### GPU 利用率低的三个原因（按影响排序）

**1. 模型太小 + batch 太小 → GPU 几乎没事做（主因）**

- 模型：SmolVLM2-**500M** (FP32) + LoRA 仅 1.49M 可训练参数
- batch_size=4，每步处理数据量极少
- GPU 瞬间完成 forward/backward，然后等数据
- 利用率呈现 0%~39% 的锯齿波动 = 典型的 "burst compute + idle wait"

**2. 数据加载 CPU-bound（次因）**

- 4 个 `pt_data_worker` 各占 ~100% CPU
- 数据管线包含：LeRobot dataset + action chunking (chunk_size=50) + 图像预处理 (256×256) + tokenization
- CPU 预处理成为吞吐瓶颈

**3. 无混合精度（加剧因素）**

- 全 FP32 训练，未使用 `torch.autocast` / `GradScaler`
- 无法利用 RTX PRO 6000 的 BF16 Tensor Core
- 显存和算力均浪费 ~2x

### 当前训练效率

- sps = 3.8~3.9，batch_size=4 → 吞吐 ~15.5 samples/sec
- 剩余 step: 30000 - 8450 = 21,550 → ETA ≈ **1.53 小时**
- 总训练时间 (0→30k): ~2.2 小时

---

## v6 优化建议

### 1. 大幅增加 batch_size

当前显存分析：
- 模型权重 (500M × 4B FP32): ~2 GB
- 当前 bs=4 的激活/梯度: ~0.3 GB
- **总共才用 2.3 GB / 96 GB**

推荐 batch_size：

| batch_size | 预估显存 (FP32) | 预估显存 (BF16) | 安全性 |
|-----------|----------------|----------------|--------|
| 32 | ~4-5 GB | ~2.5-3 GB | 非常安全 |
| **64** | **~7-8 GB** | **~4-5 GB** | **推荐** |
| 128 | ~12-15 GB | ~7-8 GB | 安全 |
| 256 | ~22-28 GB | ~12-15 GB | 保守上限 |

**推荐 batch_size=64 + BF16**，显存占用 ~5 GB，远低于 96 GB 上限。

### 2. 启用 BF16 混合精度

```python
# 训练循环中加入
with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
    total_loss, info = baseline_forward(policy, batch)
total_loss.backward()  # autocast 外面
```

RTX PRO 6000 原生支持 BF16，无需 GradScaler。收益：
- 显存减半
- Tensor Core 加速 forward/backward ~1.5-2x

### 3. 增加 num_workers

当前 4 workers 已 100% CPU。服务器有大量 CPU 核心（load average 10.77 但 CPU idle 95.6%，说明是多核机器）。

**推荐 num_workers=8~12**，配合 `prefetch_factor=4`（默认为 2）。

### 4. 考虑 Gradient Accumulation

如果 effective batch_size 需要更大（如 256），但单步 bs=64 已经足够利用 GPU：
```yaml
training:
  batch_size: 64
  gradient_accumulation_steps: 4  # effective bs = 256
```

### 预估优化后的效果

| 配置 | sps | samples/sec | 30k等效步数 | 总时间 |
|------|-----|-------------|------------|--------|
| 当前 (bs=4, FP32) | 3.8 | 15.2 | 30,000 | ~2.2h |
| bs=64, BF16, 8 workers | ~1.5-2.0 | 96-128 | 1,875 (等效) | **~15-20 min** |

**训练吞吐可提升 ~6-8x，总时间从 ~2.2h 压缩到 ~20 min。**

### 额外提醒

- **GPU 1 完全空闲**，IMM anchor 实验需要确认是否要重新启动
- 如果两个实验同时跑，可以各自独立优化（已经是 `CUDA_VISIBLE_DEVICES` 隔离）

---
