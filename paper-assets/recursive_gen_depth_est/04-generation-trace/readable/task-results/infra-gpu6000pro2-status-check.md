# infra gpu6000pro2 status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu6000pro2-status-check_20260519T174328_result.json`
- **Structured JSON:** [`05f5058b303ed2900d96.json`](../../sessions/05/05f5058b303ed2900d96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### GPU 状态
| GPU | 型号 | 利用率 | 显存占用 | 温度 |
|-----|------|--------|----------|------|
| 0 | RTX PRO 6000 (96GB) | **88%** | 32,374 / 97,887 MiB | 51°C |
| 1 | RTX PRO 6000 (96GB) | **86%** | 32,423 / 97,887 MiB | 51°C |

### 实验详情

#### 1. qwen25_14b_temp09
- **状态**: **RUNNING**
- **PID**: 776616 (python on GPU 0), 776596 (wrapper bash) — 均存活
- **运行时长**: 14h43m
- **GPU**: GPU 0, 88% util, 32.4GB VRAM
- **已完成**: d0 finetune ✓, d1 finetune ✓ (adapter 已保存)
- **当前阶段**: **Phase 3.2b — 正在用 LoRA(d1) 生成 d2 数据 (5000 samples)**，模型权重已加载完毕，推理进行中
- **进度估计**: 参考同系列 qwen25_14b 实验(d0-d2 共3层)，当前约 **65-70%**，预计剩余 4-6h

#### 2. qwen25_14b_topk50
- **状态**: **RUNNING**
- **PID**: 787051 (python on GPU 1) — 存活, CPU 104%
- **运行时长**: 12h44m
- **GPU**: GPU 1, 86% util, 32.4GB VRAM
- **已完成**: d0 finetune ✓, d1 finetune ✓ (adapter 已保存)
- **当前阶段**: **Phase 3.2b — 正在用 LoRA(d1) 生成 d2 数据 (5000 samples)**，模型权重已加载完毕，推理进行中
- **进度估计**: 同上，约 **60-65%**（比 temp09 晚启动约 2h），预计剩余 5-7h

### Checkpoints 确认
两个实验均已产出 `lora_depth_0` 和 `lora_depth_1` adapter，尚无 `lora_depth_2`。剩余流程：d2 生成(进行中) → d2 finetune → 完成。

---
