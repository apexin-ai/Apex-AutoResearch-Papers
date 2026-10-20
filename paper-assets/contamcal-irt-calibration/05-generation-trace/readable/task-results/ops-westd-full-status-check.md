# ops westd full status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-full-status-check_20260518T125839_result.json`
- **Structured JSON:** [`2a31c211924ac517766e.json`](../../sessions/2a/2a31c211924ac517766e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 服务器状态汇总

### 1. GPU 状态

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| cuda:0 | 69,643 / 97,887 MiB | 87% | PID 23304 — d005 训练 |
| cuda:1 | 17,713 / 97,887 MiB | 91% | PID 25326 — GSM8K eval |
| cuda:2 | 0 MiB | 0% | **空闲** |
| cuda:3 | 0 MiB | 100% | **无进程但 GPU-Util 100%** — 可能是驱动残留状态，无实际计算进程 |

### 2. d005 训练 (PID 23304, cuda:0)
- **状态：运行中**，进度 **83% (2639/3177)**，已运行 ~1h14m
- 最新 loss: **0.833**，token accuracy: **0.80**，lr: **3.958e-06**
- **预计剩余 ~15 分钟**（~547 steps × ~1.65s/step）
- 输出目录 `Qwen2.5-7B_d005_s42/lora_adapter/` 存在但尚未写入 checkpoint（训练完成后才保存）

### 3. GSM8K Eval (PID 25326, cuda:1)
- **状态：运行中**，进度 **41% (538/1319)**，已运行 ~1h05m
- 速度 ~7.25s/it → **预计剩余 ~1h34m**
- 模型：Qwen2.5-7B d000 (base) + lora_adapter

### 4. 模型下载

| 模型 | 已下载 | 文件进度 | 状态 |
|------|--------|---------|------|
| **Gemma-2-9B** | 32 GB (5/18 safetensors) | 6/18 files (33%) | **下载中**，速度很慢（~1.25h/file） |
| **OLMo-2-1124-7B** | 25 GB (4/6 safetensors) | 7/16 files (44%) | **下载中**，有超时重试 |
| **Phi-4** | 20 GB (2/? safetensors) | 12/21 files (57%) | **下载中**，进展最快 |
| **Qwen2.5-14B** | 4 KB (0 safetensors) | 0/? | **未开始**（仅创建目录） |

### 5. 7B d000 checkpoint
- `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/` — **639 MB**，含 lora_adapter + train_config.json，**已完成**

### 6. tmux
- 无 tmux sessions（进程通过 screen/nohup 启动）

### 7. 磁盘
- `/root/autodl-tmp`: 250G 总计，**118G 已用 / 133G 可用 (48%)**

### 关注点
- **Qwen2.5-14B 下载未启动**，无活跃下载进程
- **三个模型下载速度慢**（hf-mirror 限速），Gemma 尤其慢
- **cuda:3 GPU-Util 100% 但无进程** — 可能是之前进程退出后驱动未重置，无影响
- **cuda:2、cuda:3 空闲**，d005 训练完成后 cuda:0 也将释放

---
