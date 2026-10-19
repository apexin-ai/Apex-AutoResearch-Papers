# ops check westd45947 experiments

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd45947-experiments_20260528T231130_result.json`
- **Structured JSON:** [`583b648e9d547443363a.json`](../../sessions/58/583b648e9d547443363a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-45947 状态报告

### GPU 状态
| GPU | 型号 | 显存使用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 0 / 97887 MiB | 0% | 33°C |

只有 1 张 GPU 可见。**空闲，无训练/eval 进程运行。**

### 已完成的 Eval 结果

**1. eval_lora_baseline_s0** (May 26, seed0, 50eps, checkpoint: lora_baseline_seed0/30000)

| Task | TSR | CAR |
|------|-----|-----|
| orange juice | 0.0% | 62.0% |
| chocolate pudding | 34.0% | 44.0% |
| milk | 0.0% | 94.0% |
| bbq sauce | 0.0% | 18.0% |
| **Avg** | **8.5%** | **54.5%** |

**2. eval_lora_baseline_s1** (May 26, seed1, 50eps, checkpoint: lora_baseline_seed1/30000)

| Task | TSR | CAR |
|------|-----|-----|
| orange juice | 2.0% | 58.0% |
| chocolate pudding | 14.0% | 50.0% |
| milk | 0.0% | 90.0% |
| bbq sauce | 0.0% | 26.0% |
| **Avg** | **4.0%** | **56.0%** |

**3. eval_sdf_s2_l1_30k** (May 28 今天, seed7, 50eps, checkpoint: sdf_seed2_l1/30000)

| Task | TSR | CAR |
|------|-----|-----|
| orange juice | 30.0% | 56.0% |
| chocolate pudding | 72.0% | 76.0% |
| milk | 48.0% | 70.0% |
| bbq sauce | 68.0% | 16.0% |
| **Avg** | **54.5%** | **54.5%** |

**4. eval_pi05_baseline_reeval_disp** — **未完成，进程已死**。最后修改 May 26 12:22，停在 task 2 (milk) 开头。已完成的 2 个 task（200 eps each）：
- Task 0: TSR=0.0%, CAR=65.5%
- Task 1: TSR=0.0%, CAR=100.0%（模型完全不动，max_disp=0.0000m）

### 磁盘使用
| 分区 | 使用 | 总容量 | 使用率 |
|------|------|--------|--------|
| / (root) | 17G | 30G | 57% |
| /root/autodl-tmp | **240G** | **250G** | **96%** ⚠️ |

**autodl-tmp 几乎满了，仅剩 11G。**

### Checkpoint 完好性
`pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` = **7.1G** ✓ 完好。

---
