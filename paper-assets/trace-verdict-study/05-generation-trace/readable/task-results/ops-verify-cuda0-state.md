# ops verify cuda0 state

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_cuda0_state_20260515T104811_result.json`
- **Structured JSON:** [`bd104038de2d1bbdab85.json`](../../sessions/bd/bd104038de2d1bbdab85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. cuda:0 DeepSeek 训练：**是，正在跑**
- PID 93494，`train_sft.py --condition vota --model_path .../deepseek-coder-6___7b-instruct`
- 进度：**8/444 steps**（~2min/step），刚启动约3分钟
- 训练后会自动接 eval

### 2. DeepSeek 模型：**已完整下载**
- 路径：`/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct/`
- safetensors (2 shards, ~12.6GB) + pytorch_model.bin (2 shards, ~12.6GB) + tokenizer 均存在

### 3. cuda:0 显存
- 总量 97887 MiB，已用 **71567 MiB**，可用 **~26GB**
- DeepSeek 训练进程报告占用 22386 MiB（其余为 CUDA context/cache）

### 4. ae_only (cuda:1)：**正在训练**
- PID 87061，`train_sft.py --condition ae_only --gpu 1`
- 已运行 ~72 分钟（17:37 启动），GPU 利用率 100%，占用 41316 MiB / 97887 MiB
- 训练后会自动接 eval

另外注意：有一个 tmux session `vota_no_ae_seed42` 也指向 GPU 1，但目前 ae_only 占着 GPU 1。

---
