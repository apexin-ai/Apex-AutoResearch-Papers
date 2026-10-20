# research s1 signal preparation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_s1-signal-preparation_20260518T153654_result.json`
- **Structured JSON:** [`c0d9679dfe2fdbfab127.json`](../../sessions/c0/c0d9679dfe2fdbfab127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## S1 Embedding Signal 在 7B 规模的准备状态

### 1. sentence-transformers 安装状态
- **未安装**。`sentence-transformers` 和 `faiss-gpu` 均未安装（仅有 `transformers 5.8.1`）
- 需要安装：`sentence-transformers>=2.7.0`、`faiss-gpu>=1.7.0`（见 `requirements.txt`）
- **无预下载 embedding 模型**。HF cache 中无 mpnet/bge/gte/e5 等 embedding 模型
- 代码默认使用 `sentence-transformers/all-MiniLM-L6-v2`（~22M params，~80MB），需首次联网下载

### 2. SFT 数据位置
- 路径：`/root/autodl-tmp/sft_data/sft_dosage_{000,005,025,050,100}.jsonl`
- **注意**：代码默认指向 `/root/autodl-tmp/exp001/sft_data/`（不存在），需要传 `--sft-data-dir /root/autodl-tmp/sft_data`
- d000: 50,000 行，d100: 66,533 行

### 3. 代码位置和参数
- **入口**：`/root/contamcal-irt-calibration/exp002/compute_signals.py`，通过 `--signal s1` 调用 `signals/s1_embedding.py`
- **关键参数**：`--model-path`（仅用于推断 dosage 选 SFT 文件）、`--benchmark`、`--sft-data-dir`、`--output-dir`
- **S1 不加载被评估的 LLM**，只用 sentence-transformers 编码 + FAISS 检索。`model-path` 仅用来从路径名推断 dosage

### 4. 7B Checkpoints
- 已有：`Qwen2.5-7B_d{000,005,025,050,100}_s42` + `Qwen2.5-7B_d{000,005}_s123`
- 均为 LoRA adapter（lora_alpha=32, r=16），base model 指向 `/root/autodl-tmp/models/Qwen2.5-7B`
- 无 merged 目录，之前 3B 的 run script 用的是 `merged/` 路径——7B 可能需要先 merge 或改代码直接用 adapter path

### 5. VRAM 和时间估算
- **S1 不需要加载 7B 模型**。VRAM 消耗仅为：
  - all-MiniLM-L6-v2 编码器：~300MB GPU
  - FAISS GPU index（d100 约 66K vectors × 384 dim）：~100MB
  - 总计 **< 1GB VRAM**
- 时间估算：编码 66K SFT texts + benchmark texts ≈ 2-5 min/benchmark，4 benchmarks ≈ 10-20 min
- **但当前 4 块 GPU 全部满载运行**（61-80GB 使用，81-99% util），无空闲 GPU

### 6. 准备工作清单
1. 安装 `sentence-transformers` + `faiss-gpu`（或 `faiss-cpu`，S1 可 CPU fallback）
2. 下载 `all-MiniLM-L6-v2` 模型到 HF cache
3. 修改 `--sft-data-dir` 指向 `/root/autodl-tmp/sft_data`
4. 等待某块 GPU 空闲（或用 CPU 跑，S1 encoding 用 CPU 约慢 5-10x 但仍可行）
5. 7B checkpoints 暂无 merged 目录，但 S1 不加载 LLM，只需传正确的 adapter path 让代码推断 dosage 即可

---
