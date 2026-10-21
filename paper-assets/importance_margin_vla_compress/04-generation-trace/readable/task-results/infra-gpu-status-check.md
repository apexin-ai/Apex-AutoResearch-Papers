# infra gpu status check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260515T145200_result.json`
- **Structured JSON:** [`23aae1baad523fb59fc8.json`](../../sessions/23/23aae1baad523fb59fc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态
| GPU | Utilization | Memory |
|-----|-------------|--------|
| 0 | 0% | 3 MiB / 97887 MiB |
| 1 | 0% | 3 MiB / 97887 MiB |

GPU 当前空闲——因为两个训练进程仍在**模型加载阶段**，尚未将模型搬到 GPU 上。

### 训练进程（均存活）
| 实验 | PID | GPU | 启动时间 | CPU% | 状态 |
|------|-----|-----|----------|------|------|
| baseline (seed42) | **26017** | cuda:0 | 22:52 | 696% | 加载模型中 |
| imm_anchor (seed42) | **26092** | cuda:1 | 22:52 | 764% | 加载模型中 |

两个进程通过 tmux session 启动（`mvp_baseline` 和对应的 imm session），用 `tee` 同步写日志。

### 日志内容
两份日志都只到**模型加载阶段**，正在从 HuggingFace 拉取 SmolVLM2-500M-Video-Instruct 的配置/权重：

- **baseline.log** (474 bytes): `Loading SmolVLA policy...` → HTTP HEAD 200 OK (config.json)
- **imm_anchor.log** (873 bytes): `Loading SmolVLA policy...` → HTTP HEAD 200 OK (config.json, processor_config.json)

**尚未开始 step 计数，无报错。**

### Orphan PID 18717
已消失（`PID_18717_GONE`）。

### 其他后台进程
还有几个之前的下载脚本在跑（PID 14165 download_model3.py, PID 15450 download_model_fast.py, PID 16104 download_mirror.py），以及 lerobot dataset 加载进程（PID 12397）。这些可能在模型加载完成后就没用了，后续可清理。

### 结论
两个实验刚启动约 2-3 分钟，正在加载模型权重。预计模型加载完成后（~1-5 分钟）GPU 利用率会上升并开始 step 计数。当前无异常。

---
