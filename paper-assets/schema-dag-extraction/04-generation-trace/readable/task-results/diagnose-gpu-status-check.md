# diagnose gpu status check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_check_20260515T161941_result.json`
- **Structured JSON:** [`4c0a87b7201986198207.json`](../../sessions/4c/4c0a87b7201986198207.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是 cqa1-38874 完整状态报告：

---

## 1. GPU 状态

```
NVIDIA RTX PRO 6000 Black (98GB VRAM)
GPU利用率: 0%
显存占用: 0 MiB / 97887 MiB
GPU上无运行进程
```

**GPU 完全空闲，没有任何计算任务在使用 GPU。**

---

## 2. exp_fewrel_40rel 进程

**进程存在，正在 CPU 上运行（非 GPU）：**

| PID | 命令 |
|-----|------|
| 289717 | `tmux new-session -d -s fewrel_40rel ... bash scripts/run_fewrel_40rel.sh` |
| 289718 | `bash scripts/run_fewrel_40rel.sh` |
| 290062 | `python3 src/run_fewrel_40rel.py --stage extract --mode exp1 --output_dir artifacts/fewrel_40rel --preprocess_path artifacts/fewrel_40rel/preprocess_exp1.json` |

**日志（/tmp/fewrel_40rel.log 最后输出）：**
- 正在运行 vLLM 推理，当前处理到 batch `count_40_random_4`（40 types, BCS=0.9179, 480 samples）
- 最后时间戳 `2026-05-16 00:19:19`，正在渲染下一批 prompts
- 处理速度: ~9800 toks/s input, ~355 toks/s output
- **状态：正在运行中，无错误**

---

## 3. exp012 / LLaMA 进程

**进程存在：**

| PID | 命令 |
|-----|------|
| 292859 | `bash /root/schema-dag-extraction/scripts/auto_start_exp012_awq.sh` |
| 284997 | `huggingface-cli download hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --local-dir /root/autodl-tmp/.hf_cache/llama-3.1-70b-instruct-awq-int4` |

**日志（/tmp/exp012_awq.log）：**
```
[Sat May 16 00:18:58 CST 2026] Waiting for AWQ model download to complete...
[Sat May 16 00:18:58 CST 2026] Download in progress... 2 incomplete files remaining
[Sat May 16 00:19:58 CST 2026] Download in progress... 2 incomplete files remaining
[Sat May 16 00:20:58 CST 2026] Download in progress... 2 incomplete files remaining
```

**状态：等待 AWQ 模型下载完成，实验尚未开始推理。**

---

## 4. AWQ 下载状态

**仍在下载，还差 2 个文件。** 已下载 7/9 个 safetensors：

| 文件 | 大小 | 状态 |
|------|------|------|
| model-00001-of-00009 | — | **缺失** |
| model-00002-of-00009 | 4.6G | ✅ |
| model-00003-of-00009 | — | **缺失** |
| model-00004-of-00009 | 4.6G | ✅ |
| model-00005-of-00009 | 4.6G | ✅ |
| model-00006-of-00009 | 4.6G | ✅ |
| model-00007-of-00009 | 4.6G | ✅ |
| model-00008-of-00009 | 3.2G | ✅ |
| model-00009-of-00009 | 2.0G | ✅ |

已下载 36GB，剩余约 9.2GB（2 × 4.6GB）。

---

## 5. 磁盘空间

```
根分区:       30G 用了 17G，剩 14G (54%) — 充足
数据盘:      250G 用了 248G，剩 2.6G (99%) — ⚠️ 极度紧张
```

**数据盘 /root/autodl-tmp 只剩 2.6GB，AWQ 下载还需 ~9.2GB，下载必然失败。**

---

## 6. 其他信息

- `results/exp_fewrel_40rel/` 目录不存在；结果在 `results/` 根目录下（分析文件，非实验输出）
- `/tmp/exp012_8b.log` 不存在
- tmux session `fewrel_40rel` 存在
- Llama-3.1-8B-Instruct 模型（ModelScope 版，15GB）已下载完成

---

## 总结

| 项目 | 状态 |
|------|------|
| exp_fewrel_40rel | ✅ **正在运行**，vLLM 推理中（但 GPU 0% 利用率说明可能刚在 batch 间歇期） |
| exp012_awq | ⏳ **卡在 AWQ 下载**，还差 2 个文件（~9.2GB），但数据盘只剩 2.6GB，**会失败** |
| GPU | 空闲 0%（fewrel 实验可能在用 CPU 做预处理/prompt 渲染，或在 batch 间隙） |
| 磁盘 | **数据盘 99% 已满，AWQ 下载空间不足** |

---
