# ops urgent status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260518T202923_result.json`
- **Structured JSON:** [`f4415aa90e0a8ce34818.json`](../../sessions/f4/f4415aa90e0a8ce34818.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告 — westd-29999 (cqa1-21977)

---

### 1. GPU 状态

| GPU | 型号 | 显存占用 | GPU利用率 | 进程 |
|-----|------|---------|----------|------|
| 0 | RTX 4090 D | 0MiB / 24564MiB | 0% | 无 |

**只有 1 张卡。GPU 0 完全空闲。** 无任何 GPU 进程。

---

### 2. 14B 训练进度

**14B checkpoint 目录不存在。** `/root/autodl-tmp/exp001/checkpoints/` 下没有任何 `Qwen2.5-14B_*` 目录。无 `.done`、无 `trainer_state.json`、无 `lora_adapter/`。

无 14B 相关进程。

| 实验 | 状态 |
|------|------|
| 14B d025 s42 | **不存在** — 目录未创建 |
| 14B d050 s42 | **不存在** — 目录未创建 |
| 14B d100 s42 | **不存在** — 目录未创建 |

也无任何 7B checkpoint 目录。

---

### 3. Gemma-2-9B pilot

**不存在。** 无 checkpoint 目录、无日志文件、无相关进程。

| 实验 | 状态 |
|------|------|
| gemma-2-9b d000 s42 | **不存在** — 未启动 |

---

### 4. Phi-4 / OLMo-2 下载

| 模型 | 状态 |
|------|------|
| Phi-4 | **失败** — 目录不存在，0 shards，下载进程已死 |
| OLMo-2-1124-7B | **失败** — 目录不存在，0 shards，下载进程已死 |
| 网络 | **DOWN** — curl HuggingFace 超时 |

根因：**网络不通**，外部 HuggingFace 不可达。模型目录 `/root/autodl-tmp/models/` 下没有 phi-4 和 OLMo 子目录。

已有模型：Qwen 系列、Llama-3.2-3B、DeepSeek-R1-Distill-Qwen-1.5B。

---

### 5. S1 信号 (7B d050/d100 s123)

| 信号 | 状态 |
|------|------|
| Qwen2.5-7B_d050_s123 | **不存在** — 目录未创建 |
| Qwen2.5-7B_d100_s123 | **不存在** — 目录未创建 |

7B checkpoint 也不存在，所以信号计算无法进行。

---

### 补充发现

**已完成的训练** (有 lora_adapter + merged 目录)：
- Qwen2.5-0.5B: d000/d005/d025/d100 x s42+s123 (8个) ✅
- Qwen2.5-1.5B: d000/d005/d025/d100 x s42+s123 (8个) ✅
- Qwen2.5-3B: d000/d005/d025/d100 x s42+s123 + a32 变体 ✅
- Llama-3.2-3B: d000/d005/d025/d100 x s42 (4个，有 lora_adapter + merged，但无 trainer_state 和 .done) ✅

**已完成的信号**：Qwen 0.5B/1.5B/3B 全系列 + Llama-3.2-3B (部分)

**无活跃计算进程。** 只有 tensorboard 和 jupyter-lab 在后台运行。无 tmux session。

**磁盘**：/root/autodl-tmp 169G 总量，119G 已用，51G 可用 (70%)。

---

### 总结

这台机器（单卡 4090D）当前**完全空闲**。14B/7B/Gemma-9B 实验从未在此启动（这些模型远超单卡 24GB 显存）。Phi-4/OLMo-2 下载因网络不通失败，进程已死。

---
