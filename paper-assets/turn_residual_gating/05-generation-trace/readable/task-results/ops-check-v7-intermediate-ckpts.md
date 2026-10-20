# ops check v7 intermediate ckpts

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_v7_intermediate_ckpts_20260519T114257_result.json`
- **Structured JSON:** [`5241ddea4837637d7abb.json`](../../sessions/52/5241ddea4837637d7abb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. v7 中间 checkpoint

**有 3 个 epoch checkpoint + final**：

| Checkpoint | 时间 | 内容 | 大小 |
|---|---|---|---|
| `epoch_0/` | May 19 04:42 | gate_params.pt (3.2MB) + lora/ | epoch 0 结束 |
| `epoch_1/` | May 19 06:41 | gate_params.pt (3.2MB) + lora/ | epoch 1 结束 |
| `epoch_2/` | May 19 08:39 | gate_params.pt (3.2MB) + lora/ | epoch 2 结束 |
| 根目录 `gate_params.pt` + `lora/` | May 19 08:39 | final（与 epoch_2 同时间） | 最终 |

**没有 per-step checkpoint（gs50/gs100/gs150/gs200/gs400 不存在）。** 只有 per-epoch 保存。按 3000 total steps / 3 epochs 计算，epoch_0 = step 1000, epoch_1 = step 2000, epoch_2 = step 3000。无法直接用 checkpoint 画 gs50~gs400 的泛化曲线。

## 2. v7 训练日志 per-step GAR 数据

**日志数据非常完整，可用于训练动力学可视化：**

- **[GATE] 记录**：62 条，每 50 step 记录一次，step 范围 0~3000（含 mean/std/min/max）
- **L_GAR 记录**：480 条（每个 training step 的 loss 行都含 L_GAR 值）
- **覆盖关键 step**：step 0/50/100/150/200/400 全部有 [GATE] 数据

GAR 演化趋势摘要：
- step 0: mean=0.810 → step 200: 0.929 → step 1000: 0.969（快速上升）
- step 1000~2000: 稳定在 0.95~0.97
- step 2000~3000: 略降至 0.93~0.96

**结论：虽然无 per-step checkpoint，但日志中的 [GATE] 和 L_GAR 数据完全可以画出 GAR 训练动力学曲线。Route B 3.4 可以用日志数据替代 checkpoint 评估。**

## 3. LoRA-only 训练进度

当前位置：**Epoch 2 Step 2300**

进度计算：
- global_step = (2 × 8000 + 2300) / 8 = 18300 / 8 = **2287.5**
- 进度 = 2287.5 / 3000 = **76.3%**

GPU 状态：利用率 98%，显存 91.3/97.9 GB，训练正常运行中。

预估剩余：还需约 712 global steps，按当前速度预计还需约 2~3 小时完成。

---
