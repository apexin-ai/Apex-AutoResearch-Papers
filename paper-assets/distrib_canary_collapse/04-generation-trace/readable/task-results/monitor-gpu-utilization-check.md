# monitor gpu utilization check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu_utilization_check_20260515T073436_result.json`
- **Structured JSON:** [`95d4a656884f94b6d68d.json`](../../sessions/95/95d4a656884f94b6d68d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 利用率快照
| GPU | 实验 | Util | VRAM |
|-----|------|------|------|
| 0 | plan_006 | 37% | 12.5 / 97.9 GB |
| 1 | a075 | 15% | 14.4 / 97.9 GB |

两卡均值 ~26%，比触发警告时的 12% 有所回升。

### 各实验阶段

**a075 (cuda:1)** — Gen 1 数据生成阶段（合成数据推理）
- Gen 0 已完成（ppl=26.95, entropy=3.23, eff_rank=46.6）
- 当前在 Gen 1 的 `model.generate()` 循环中（日志 1287/1502 行都是 padding 警告）
- 15% util **正常**：自回归生成是 memory-bandwidth-bound，不是 compute-bound

**plan_006 (cuda:0)** — Gen 14+ 训练阶段，step 456/10000
- ~5-7 it/s，loss=0.0507
- 37% util 偏低，原因是 `batch_size=4` 对 98GB 显存来说太小

### 可调参数

| 参数 | 当前值 | 位置 | 说明 |
|------|--------|------|------|
| `--batch_size` | 4 | L59 | 训练 batch，可增大 |
| `--gen_batch_size` | 16 | L64 | 生成 batch，可增大 |
| `--gen_max_new_tokens` | 256 | L62 | 生成长度 |
| `num_workers` | 未设置 | — | DataLoader 未配置 |
| `pin_memory` | 未设置 | — | DataLoader 未配置 |

### 结论

**低利用率的主要原因是 a075 处于生成阶段**（memory-bound 推理，util 天然低）。plan_006 训练阶段 37% 也偏低，因为 batch_size=4 远未充分利用 98GB 显存。

**是否需要改代码：当前不需要。** 两个实验正在跑，中途改参数意义不大。下次实验可考虑：
1. `--batch_size` 提到 16~32
2. `--gen_batch_size` 提到 32~64
3. TrainingArguments 里加 `dataloader_num_workers=4, dataloader_pin_memory=True`

---
