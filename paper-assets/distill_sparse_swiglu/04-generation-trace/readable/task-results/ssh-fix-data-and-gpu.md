# ssh fix data and gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-data-and-gpu_20260515T120102_result.json`
- **Structured JSON:** [`aacc561a7fea9657ec47.json`](../../sessions/aa/aacc561a7fea9657ec47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 dry-run 全部通过。

---

## 报告

### 1. SlimPajama 数据集修复

**诊断**：`cerebras/SlimPajama-627B` 在 HuggingFace Hub 上不可访问（AutoDL 代理环境下）。`allenai/c4` streaming 也超时。

**方案**：改用本地已缓存的 WikiText-103（1.8M 条目，~100M tokens），足够 MVP 训练（1000 steps × batch 4 × seq 2048 = ~8M tokens）。

**代码修改**：
- `data_utils.py`：`get_slimpajama_loader` → `get_calibration_loader(tokenizer, batch_size, seq_len, seed, dataset_name="wikitext-103")`，支持 `wikitext-103` 和 `c4` 两种数据集
- `train.py`：导入改为 `get_calibration_loader`，新增 `--dataset` 参数（默认 `wikitext-103`）

### 2. GPU 分配

**实际行为确认**：train.py 使用 `torch.device(f"cuda:{args.gpu}")`。当框架设置 `CUDA_VISIBLE_DEVICES=0` 或 `=1` 时，torch 只看到 1 个设备（cuda:0）。因此：
- mvp_kl_s42: `CUDA_VISIBLE_DEVICES=0 --gpu 0` → 物理 GPU 0 ✓
- mvp_bce_s42: `CUDA_VISIBLE_DEVICES=1 --gpu 0` → 物理 GPU 1 ✓

**`--gpu 0` 对两个实验都正确，无需修改。**

### 3. Dry-run 验证

| 模式 | GPU | 结果 | 示例输出 |
|------|-----|------|----------|
| KL | CUDA_VISIBLE_DEVICES=0 | ✓ 3 steps 完成 | loss=0.5938, sparsity=0.371 |
| BCE | CUDA_VISIBLE_DEVICES=1 | ✓ 3 steps 完成 | loss=0.6986, sparsity=0.507 |

两个阻塞问题已解决，MVP 实验可以启动。

---
