# check server probe

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server_probe_20260513T085559_result.json`
- **Structured JSON:** [`4cca4be89ded7cf33e7e.json`](../../sessions/4c/4cca4be89ded7cf33e7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果汇报

### 1. GPU 状态

| GPU | 型号 | 显存使用 | 温度 | GPU利用率 | 进程 |
|-----|------|---------|------|----------|------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | 79003 / 97887 MiB (81%) | 40°C | 65% | python PID 10532 |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 82991 / 97887 MiB (85%) | 33°C | 0% | python PID 10532 |

Driver 590.44.01, CUDA 13.1

### 2. Python 进程

**PID 10532** — `python phase0_orthogonality.py`，CPU 占用 112%，运行中（14:28 启动，已运行约 2.5 小时）。

其他后台进程：tensorboard (PID 911)、jupyter-lab (PID 914)，均为系统服务。

### 3. Phase 0 结果文件

| 文件 | 状态 |
|------|------|
| `correlation_matrix.json` | **不存在** |
| `scatter_plots.png` | **不存在** |
| `scored_samples.jsonl` | **不存在** |
| `checkpoint/` | **存在**（14:51 生成，含 LoRA adapter，17MB） |
| `run.log` | **存在**（71KB，持续写入中） |

### 4. correlation_matrix.json

**不存在**。脚本仍在 Step 2（生成阶段），尚未到达计算相关性矩阵的步骤。

### 5. 训练日志关键信息

脚本分多步执行：

- **Step 1（SFT 训练）**：已完成。训练了约 3 个 epoch，最终 loss ≈ 0.89，token accuracy ≈ 0.78。LoRA checkpoint 已保存。
- **Step 2（生成样本）**：**正在进行中**，目标 5000 样本，截至日志尾部已生成 **4600/5000**（92%）。每 100 样本约 2.5 分钟，预计还需约 10 分钟完成。

**无错误**，运行正常。

### 6. Python/CUDA 环境

| 组件 | 版本 |
|------|------|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.10.0+cu128 |
| CUDA | 13.1 |
| transformers | 4.57.6 |
| datasets | 4.8.4 |
| peft | 0.19.0 |
| trl | 1.1.0 |
| wandb | 0.26.0 |
| sacrebleu | 2.6.0 |
| sentence-transformers | 5.4.1 |
| scipy | 1.17.1 |
| matplotlib | 3.10.5 |

### 7. 项目目录结构

```
/root/autodl-tmp/pgpf/
├── phase0_orthogonality.py    # 主脚本（14KB）
├── __pycache__/
├── data/
│   ├── train.jsonl
│   ├── val.jsonl
│   └── test.jsonl
├── outputs/
│   └── phase0/
│       ├── checkpoint/        # LoRA adapter (adapter_model.safetensors 17MB)
│       └── run.log            # 运行日志（71KB，持续写入）
└── pgpf/                      # 子包目录
```

**总结**：Phase 0 脚本正常运行中，Step 1 SFT 训练已完成并保存 checkpoint，Step 2 生成已达 4600/5000（92%），预计约 10 分钟后进入后续步骤（评分、相关性计算、绘图）。无报错。

---
