# ops code domain data prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_code-domain-data-prep_20260518T163540_result.json`
- **Structured JSON:** [`3b2bf071f6521dc00417.json`](../../sessions/3b/3b2bf071f6521dc00417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是完整报告：

---

## 报告

### 1. 种子数据统计

- **来源**: `code_search_net` (Python subset)，通过 hf-mirror.com 镜像流式加载
- **条数**: 5500 条（过滤掉 1162 条不符合条件的）
- **长度分布**: avg=711, min=200, max=2000, median=580
- **路径**: `/root/autodl-tmp/gen-depth-contamination/data/code_python_seed/depth_0.jsonl`
- **前 3 条摘要**:
  - `code_py_0` (906 chars): `__multiscale_gc_hi2lo_run` 图割分割函数
  - `code_py_1` (1571 chars): `__ordered_values_by_indexes` 多尺度图割辅助函数
  - `code_py_2` (1616 chars): `__hi2lo_multiscale_indexes` ndarray 多尺度索引计算

> 注意：The Stack v2 和 starcoderdata 均为 gated dataset，服务器无 HF token。已使用开放的 `code_search_net` 替代，数据内容为 Python 函数体（含 docstring），质量适合 continuation 生成。

### 2. LLaMA-3.1-8B 缓存

- **路径**: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B`（与之前 exp_018 实验使用的路径一致）
- **状态**: 正在通过 ModelScope 下载，4 个 shard 并行，当前速度 ~700KB/s，**预计约 2 小时完成**
- Qwen2.5-1.5B 已缓存: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`

### 3. Pipeline 命令（参数已对照 exp_018 日志验证）

**Qwen-1.5B 实验 (cuda:1)**:
```bash
cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate
CUDA_VISIBLE_DEVICES=1 python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B \
  --data_dir data/exp_code_qwen1b5 \
  --results_dir results/exp_code_qwen1b5 \
  --num_samples 5000 --max_depth 5 --batch_size 8 \
  --generation_mode continuation \
  --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B
```

**LLaMA-8B 实验 (cuda:2)**:
```bash
cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate
CUDA_VISIBLE_DEVICES=2 python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B \
  --data_dir data/exp_code_llama8b \
  --results_dir results/exp_code_llama8b \
  --num_samples 5000 --max_depth 5 --batch_size 4 \
  --generation_mode continuation \
  --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B
```

### 4. 注意事项

- **LLaMA 下载未完成**: 需等约 2 小时。Qwen 实验可以先启动。
- **Python 环境**: 必须使用 `/root/miniconda3/bin/python`（系统 Python 无 torch/transformers）
- **HF 镜像**: 服务器无法直连 huggingface.co，需设置 `HF_ENDPOINT=https://hf-mirror.com`
- **数据源差异**: 使用 `code_search_net` 而非 The Stack v2（gated 限制），内容均为真实 Python 代码，对 continuation 实验影响可忽略

---
