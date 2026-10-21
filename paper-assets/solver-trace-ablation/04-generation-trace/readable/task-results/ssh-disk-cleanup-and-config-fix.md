# ssh disk cleanup and config fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk-cleanup-and-config-fix_20260515T135019_result.json`
- **Structured JSON:** [`c9c1612cd0492ba5d0b3.json`](../../sessions/c9/c9c1612cd0492ba5d0b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两张 GPU 并非空闲，正在运行训练任务：**

| GPU | PID | 任务 | 显存 |
|-----|-----|------|------|
| 0 | 363697 | `plan001-exec-only-s43-1000-r2` (seed 43) | 77906 MiB |
| 1 | 363845 | `plan001-exec-only-s44-1000-r2` (seed 44) | 77940 MiB |

两个任务都是 21:51 启动（约 1 分钟前），正以 94-97% GPU 利用率运行。CUDA_VISIBLE_DEVICES 分别正确设为 0 和 1。

---

## 汇报

### 1. 清理前后 df -h 对比
| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 159G | 92G | 64% |
| 清理后 | 17G | 234G | 7% |

### 2. 删除内容和释放空间
- **`*.safetensors` (>100M)**: 所有实验的模型权重文件，释放约 **~130G**
- **`checkpoint-*` 目录**: 所有中间 checkpoint 目录，释放约 **~12G**
- **s43/s44 旧目录**: 已不存在（之前已删）
- 总释放: **~142G**

### 3. 最终可用空间
**234G 可用**（远超 80G 要求）

### 4. grpo_exec_only.yaml 修改
**无需修改**。`train_grpo.py` 第 462-464 行已硬编码：
```python
save_steps=50,
save_total_limit=1,
save_only_model=True,
```
YAML 中的值不会覆盖这些硬编码参数（config merge 逻辑只覆盖 `None` 或 `False` 的 CLI args，而这些参数不在 argparse 中定义）。

### 5. 是否需要修改 train_grpo.py
**不需要**。C003 约束已满足。

### 注意
两张 GPU 都在跑 plan001 exec-only 的 s43/s44 r2 训练（刚启动 ~1 分钟），不是空闲状态。

---
