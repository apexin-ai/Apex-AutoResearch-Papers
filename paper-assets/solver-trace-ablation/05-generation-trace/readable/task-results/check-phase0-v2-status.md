# check phase0 v2 status

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase0_v2_status_20260513T085426_result.json`
- **Structured JSON:** [`82c206dc78928617f71b.json`](../../sessions/82/82c206dc78928617f71b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 v2 实验状态报告

### 进程状态：🟢 运行中
- **PID**: 10532
- **当前阶段**: Step 2 — 生成合成样本，进度 **4504/5000** (90%)
- 最后日志时间: 16:52:35（服务器当前时间 16:54:42）

### GPU 使用详情
| GPU | 型号 | 显存占用 | 利用率 | 温度 | 状态 |
|-----|------|---------|--------|------|------|
| 0 | NVIDIA RTX PRO 6000 Black (98GB) | 79003 / 97887 MiB (81%) | 46% | 38°C | 被 PID 10532 占用 |
| 1 | NVIDIA RTX PRO 6000 Black (98GB) | 82991 / 97887 MiB (85%) | 0% | 31°C | 被 PID 10532 占用 |

两张卡都被当前实验占用，无空闲卡。GPU 0 做推理生成（46% util），GPU 1 加载了模型但当前空闲（可能用于 base model 对比）。

### 实验时间线
| 步骤 | 开始时间 | 结束时间 | 状态 |
|------|---------|---------|------|
| 数据加载 | 14:28:10 | 14:28:10 | ✅ 完成（8000 train / 1000 val / 1000 test） |
| Step 1: LoRA 微调 | 14:28:10 | 14:51:44 | ✅ 完成（750 steps, 23min, checkpoint 已保存） |
| Step 2: 合成生成 | 14:51:44 | — | ⏳ 进行中（4504/5000, ~100 samples/2.5min） |
| Step 3+: 正交性分析 | — | — | 待运行 |

### 预计完成时间
- 剩余 ~496 samples，按当前速率（~100/2.5min）预计 **~12-15 分钟**后完成 Step 2
- Step 3（property scoring + correlation 分析 + 绘图）预计额外 5-10 分钟
- **整体预计 ~17:10-17:20 完成**

### 输出文件
- `outputs/phase0/checkpoint/` — LoRA adapter 已保存（17MB adapter_model.safetensors）
- `outputs/phase0/run.log` — 71KB 日志
- 结果文件（correlation_matrix.json、scatter plots 等）尚未生成，需等 Step 2+3 完成

### 模型配置
- Base model: Qwen2.5-1.5B
- LoRA: 4,358,144 trainable params (0.28%)
- 生成: batch_size=8, 目标 5000 samples
- GPU 分配: cuda:0 (fine-tuned model), cuda:1 (base model)

---
