# check gpu status v3

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_v3_20260514T060817_result.json`
- **Structured JSON:** [`b22639fa0cd4ab54ec4a.json`](../../sessions/b2/b22639fa0cd4ab54ec4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 — westd-11235 — 2026-05-14 14:08 CST

---

### 1. nvidia-smi 完整原始输出

```
Thu May 14 14:08:41 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   79C    P0            580W /  600W |   77919MiB /  97887MiB |    100%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   59C    P0            493W /  600W |   28747MiB /  97887MiB |     99%      Default |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|=========================================================================================|
|    0   N/A  N/A          415007      C   python3                               28738MiB |
|    1   N/A  N/A          405067      C   python3                               28738MiB |
+-----------------------------------------------------------------------------------------+
```

### 2. 每张卡详情

| GPU | PID | 方法 | 模型 | 显存占用 | GPU利用率 | SM利用率(pmon) | 温度 | 功耗 |
|-----|-----|------|------|---------|----------|---------------|------|------|
| **0** | 415007 | `rgds` | gpt2-medium | 28738 MiB / 97887 MiB | **100%** | **98%** | 79°C | 580W/600W |
| **1** | 405067 | `external_only` | gpt2-medium | 28738 MiB / 97887 MiB | **99%** | **73-98%** | 59°C | 493W/600W |

**PID 415007 命令行：**
```
python3 /root/div_cal_verify/run_mvp.py --method rgds --student_model gpt2-medium --self_iterate --no_quality_filter --output_dir .../results_medium_rgds_seed123 --num_generations 8 --gen_tokens 500000 --seed 123 --gpu_ids 0
```

**PID 405067 命令行：**
```
python3 /root/div_cal_verify/run_mvp.py --method external_only --student_model gpt2-medium --self_iterate --no_quality_filter --output_dir .../results_medium_external_seed123 --num_generations 8 --gen_tokens 500000 --seed 123 --gpu_ids 0
```

### 3. nvidia-smi pmon 快照（5s, 3次采样）

```
# gpu    pid   type   sm   mem   command
    0  415007    C    98%  45%   python3
    1  405067    C    98%  25%   python3
    0  415007    C    98%  45%   python3
    1  405067    C    73%  18%   python3
    0  415007    C    98%  45%   python3
    1  405067    C    97%  25%   python3
```

GPU 0 三次采样均 98% SM，稳定满载。GPU 1 有一次降至 73%（数据加载/选择阶段切换），其余 97-98%。

### 4. 进程树与调度

- **GPU 0 (PID 415007)**：由 `chain_cuda0_seed123.sh` → `run_medium_rgds_seed123.sh` 启动，正在跑 **rgds** 方法
- **GPU 1 (PID 405067)**：由 `run_medium_external_seed123.sh` 启动，正在跑 **external_only** 方法
- **auto_cuda1_chain.sh**：正在 `sleep 60` 轮询等待 GPU 1 上 `medium_external_seed123` (PID 405067) 结束后接力下一任务

### 5. 当前进度（来自日志尾部）

| GPU | 方法 | 当前进度 | 阶段 |
|-----|------|---------|------|
| **0** | rgds | **Generation 6/7** | [3/5] Training student |
| **1** | external_only | **Generation 6/7** | [3/5] Training student |

两个实验都在第 6 代（共 7 代，0-indexed 即倒数第二代），正在训练阶段。

### 6. 结论

**两张卡满载运行，无空闲。**

- GPU 0: 100% 利用率，580W 功耗，79°C 高温运行 — rgds seed123 实验
- GPU 1: 99% 利用率，493W 功耗，59°C — external_only seed123 实验
- 两个实验均已进入 Generation 6/7 的训练阶段，接近完成
- GPU 1 pmon 中一次降到 73% 是正常的阶段切换（generation/selection → training 过渡），不是空闲

之前健康度报告"空闲"判断有误，两卡实际持续满载。

---
