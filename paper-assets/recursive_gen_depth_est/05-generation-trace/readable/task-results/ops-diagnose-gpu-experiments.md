# ops diagnose gpu experiments

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_gpu_experiments_20260517T113019_result.json`
- **Structured JSON:** [`44c64053b1072897f5b9.json`](../../sessions/44/44c64053b1072897f5b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 实验 1: qwen25_14b_scale_001 — **下载卡死（未真正失败）**

**状态**: tmux session `qwen25_14b_scale` 仍存在（PID 696523），`hf download` 进程（PID 696537）仍在运行，但**模型下载反复超时**。

**根因**: HuggingFace 下载超时，未设置 `HF_TOKEN`（日志提示 "sending unauthenticated requests"）。8 个 safetensors 分片全部 timeout，持续 retry 无进展。

**已下载内容**: 只有小文件（config.json、tokenizer.json 等，共 ~11MB），无任何模型权重文件（.safetensors）。

**目录**: `/root/autodl-tmp/models/qwen25_14b/` — 无 safetensors 文件。

**错误日志摘要**:
```
Error while downloading .../model-00001-of-00008.safetensors: The read operation timed out
Error while downloading .../model-00002-of-00008.safetensors: The read operation timed out
...（全部 8 个分片都超时）
```

**修复建议**: 设置 `HF_TOKEN` 或使用 HF 镜像源。

---

### 实验 2: prompted_gen_gpt2xl_001 — **正常运行中**

**状态**: 进程 PID 695547 活跃，GPU 1 占用 15685MiB / 74% 利用率。

**为什么找不到 tmux session**: 该实验通过 `nohup` 启动（不是 tmux），所以没有对应的 tmux session。

**当前进度**: 
- 训练阶段已完成：3 epochs, 939/939 steps, final loss = **1.4379**, runtime = 714.8s
- 当前进入 **"d2: LoRA + topic prompts"** 阶段，权重加载完成，正在执行推理/生成

**吞吐**: ~1.32 it/s，运行稳定。

**结论**: 此实验无异常，正常推进中。

---

### 汇总

| 实验 | 状态 | 问题 | 需要操作 |
|------|------|------|----------|
| qwen25_14b_scale_001 | 卡住 | HF 下载超时，无 TOKEN | 需设置 HF_TOKEN 或换镜像源后重试 |
| prompted_gen_gpt2xl_001 | 正常运行 | 无（nohup 启动，非 tmux） | 无需操作 |

---
