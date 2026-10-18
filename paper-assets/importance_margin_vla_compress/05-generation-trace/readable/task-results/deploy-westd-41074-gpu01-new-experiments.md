# deploy westd 41074 gpu01 new experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-41074-gpu01-new-experiments_20260525T195313_result.json`
- **Structured JSON:** [`5cb7b3592fc65e034f52.json`](../../sessions/5c/5cb7b3592fc65e034f52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**已完成：**
- GPU 0/1 stale 进程 killed（random_k05_object_v2, l2norm_k05_object_v2），GPU 已释放
- profiling 脚本已写入 `/root/autodl-tmp/importance_margin_vla_compress/profile_pi05_latency.py`
- 两个实验已注册 registry（RUNNING 状态）

**阻塞项：**
- π0.5 模型权重 (`model.safetensors` ~7GB) 在 westd-41074 上不存在（之前的 pi05 实验全部在 cqa1-33015 上跑的）
- 正从 HuggingFace 下载中，速度 ~2-3 MB/s，预计 ~40 分钟完成
- 后台脚本 `/tmp/wait_and_launch.sh` 会在下载完成后自动启动两个 tmux session：
  - GPU0: `profiling_pi05_latency_westd41074`
  - GPU1: `eval_pi05_attention_k0925_long_seed42`

两个实验会在下载完成后自动启动，无需手动干预。需要我过一段时间检查启动状态吗？

---
