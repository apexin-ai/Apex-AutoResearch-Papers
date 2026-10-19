# analysis iql results read

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_iql-results-read_20260515T082516_result.json`
- **Structured JSON:** [`309ce74272cdfd2be5b7.json`](../../sessions/30/309ce74272cdfd2be5b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 汇报

### 1. Multitask MLP Checkpoint

| 项目 | 值 |
|------|-----|
| 路径 | `/root/temp-adv-distill-vla/artifacts/gate1b_mlp_multitask.pt` |
| 大小 | 2.3 MB |
| Overall R² | **0.9653** |
| 训练样本 | 59,656 |
| Best epoch | 11 |
| 训练时间 | 11.4s |

**Per-task R²（multitask MLP，跨任务泛化验证）：**

| Task | R² |
|------|-----|
| chocolate_pudding | 0.9897 |
| butter | 0.9836 |
| salad_dressing | 0.9825 |
| milk | 0.9796 |
| tomato_sauce | 0.9776 |
| cream_cheese | 0.9769 |
| ketchup | 0.9695 |
| alphabet_soup | 0.9691 |
| bbq_sauce | 0.9673 |
| orange_juice | **0.8546** (最低) |

10/10 tasks > 0.7 阈值，Gate 1 通过。

### 2. IQL 训练 — 已完成

IQL 训练**已经跑完了**，不需要再启动。10 个 per-task IQL 模型均已训练完毕。

**IQL 超参数：** τ=0.8, γ=0.99, lr=3e-4, steps=100k, batch=256

**IQL checkpoints:** `/root/temp-adv-distill-vla/artifacts/iql_checkpoints/`，每个 5.1 MB，共 51 MB

| Task | Q Loss | V Loss | Steps | Transitions | Time |
|------|--------|--------|-------|-------------|------|
| alphabet_soup | 5e-6 | 4e-6 | 100k | 7,808 | 211s |
| bbq_sauce | 1.9e-5 | 6e-6 | 100k | 7,348 | 217s |
| butter | 1.1e-5 | 4e-6 | 100k | 7,865 | 211s |
| chocolate_pudding | 8e-6 | 4e-6 | 100k | 7,982 | 211s |
| cream_cheese | 1.4e-5 | 7e-6 | 100k | 7,194 | 211s |
| ketchup | 2.1e-5 | 7e-6 | 100k | 8,056 | 209s |
| milk | 5e-6 | 3e-6 | 100k | 7,281 | 212s |
| orange_juice | 1.3e-5 | 6e-6 | 100k | 6,968 | 210s |
| **salad_dressing** | **7.0e-4** | **2.0e-4** | **75k (early stop)** | 6,641 | 160s |
| tomato_sauce | 1.6e-5 | 7e-6 | 100k | 7,364 | 211s |

总训练时间：2060s (~34 min)

**salad_dressing 注意**：75k 步 early stop，loss 比其他任务高 2 个数量级。

### 3. Gate 2 评估 — 已完成，未通过

Gate 2 已跑完（`gate2_results.json`），结果：**0/10 tasks passed**。

| Task | AUROC (IQL) | AUROC (saliency) | AUROC (TED) | IQR | Cohen's d | Passed |
|------|-------------|-------------------|-------------|-----|-----------|--------|
| alphabet_soup | 0.515 | 0.004 | 0.699 | 0.067 | 0.085 | No |
| bbq_sauce | 0.497 | 0.006 | 0.635 | 0.105 | 0.029 | No |
| butter | 0.516 | 0.007 | 0.556 | 0.110 | 0.042 | No |
| chocolate_pudding | 0.517 | 0.004 | 0.595 | 0.120 | 0.135 | No |
| cream_cheese | 0.506 | 0.006 | 0.692 | 0.085 | 0.003 | No |
| ketchup | 0.521 | 0.004 | 0.628 | 0.103 | 0.029 | No |
| milk | 0.502 | 0.005 | 0.594 | 0.059 | -0.004 | No |
| orange_juice | 0.509 | 0.006 | 0.615 | 0.083 | 0.029 | No |
| salad_dressing | 0.500 | 0.005 | 0.578 | 0.017 | -0.111 | No |
| tomato_sauce | 0.473 | 0.009 | 0.600 | 0.114 | -0.117 | No |

**关键问题：IQL advantage AUROC ≈ 0.50（随机水平）**，即 IQL 训出的 Q-V advantage 完全无法区分好坏 action。Saliency AUROC 也近乎 0。只有 TED（temporal embedding distance）baseline 有一定区分力（~0.62）。

### 4. LIBERO 数据

路径：`/root/temp-adv-distill-vla/data/libero/libero_object/`，10 个 hdf5 文件（每任务 50 demos）。

### 5. OpenVLA 模型

路径：`/root/autodl-tmp/models/openvla-7b-finetuned-libero-spatial/`

| 文件 | 大小 |
|------|------|
| model-00001-of-00004.safetensors | **1.7 MB** (异常小，可能损坏/未完成) |
| model-00002-of-00004.safetensors | 4.7 GB |
| model-00003-of-00004.safetensors | 4.7 GB |
| model-00004-of-00004.safetensors | 251 MB |

**model-00001 仅 1.7MB，几乎肯定是下载不完整**，正常应 ~4.7GB。需要重新下载。

### 6. GPU 和磁盘

| 资源 | 状态 |
|------|------|
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell (98GB each)，空闲，0 MiB used |
| 根分区 | 30G, 33% used (21G free) |
| 数据盘 | 250G, 4% used (241G free) |

### 7. Phase 1 IQL Readiness 评估

**IQL 训练已完成但 Gate 2 失败。** 核心问题：

- IQL advantage 信号 ≈ 随机 (AUROC ~0.50)，说明 IQL 学到的 Q 函数没有捕获到有意义的 action quality 差异
- 可能原因：(1) reward signal 虽然 R²高但 MLP 输出太平滑，导致相邻 step 的 reward 差异极小；(2) state=VIP feature (1024d) + action (7d) 的 IQL 在离线数据上过拟合到接近 0 loss 但没学到有用的 value function；(3) salad_dressing 的 MLP reward 质量本身较差（R²=0.8546，且 IQL 在此任务 early stop）
- OpenVLA model-00001 需重新下载

---
