# ssh code refactor v2

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_code-refactor-v2_20260515T170908_result.json`
- **Structured JSON:** [`c96f788fe0ac7dcfd84c.json`](../../sessions/c9/c96f788fe0ac7dcfd84c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 改造完成，汇总如下

### 各文件改动摘要

| 文件 | 行数 | 改动内容 |
|------|------|----------|
| **train.py** | ~130 | 移除 Accelerate/DDP，改为单 GPU + `torch.amp.autocast` bf16；新增 `--device` 参数；wandb run_name 改为 `train_gen{gen}_seed{seed}` |
| **generate_synthetic.py** | ~80 | 新增 `--device` 参数；进度条描述改为含 seed |
| **compute_signals.py** | ~210 | **核心改造**：单次 forward pass 同时算 per-example loss/entropy/spectral_rank（5000-d 向量）；corpus-level sigma_spectral_rank（Gram→SVD）；保留 distinct-n；新增 Spearman ρ；移除 val_loss/val_set_path；新 JSON 输出格式 |
| **run_pipeline.py** | ~250 | 新增 `--seeds "42,137"` 参数；`run_parallel()` 用 `subprocess.Popen` 并行两个 seed（cuda:0/cuda:1）；每代 4 步骤（generate→mix→train→signals）同步并行；checkpoint 目录改为 `gen{i}_seed{s}/`；末尾自动调 analyze_correlation |
| **analyze_correlation.py** | ~130 | 读取 per-seed signal JSON；打印 ρ 趋势表；Pass/Fail 判断（3 条件：ρ 下降、均值单调退化 ≥15%、两 seed 均成立） |
| **accelerate_config.yaml** | — | 已删除 |

### --help 验证

5 个文件全部 `--help` 通过，新增参数（`--device`、`--seeds`）均正确显示。

### Dry-run 测试结果

用 tiny GPT2 模型 + 10 条 fake probe 运行 compute_signals.py，**21/21 项格式检查全部 PASS**：

- `per_example.{loss,entropy,spectral_rank}` — 长度正确（=num_probe_samples），值域合理（loss>0, entropy>0, rank≥1）
- `aggregated.{mean,std}` — 6 个字段均为 float
- `corpus_level.{sigma_spectral_rank, distinct_1/2/3}` — 全部正确
- `correlations.{rho_loss_entropy, pval_loss_entropy, rho_loss_spectral_rank, pval_loss_spectral_rank}` — ρ ∈ [-1,1]

### 额外修复

- `torch_dtype=torch.bfloat16` → `dtype=torch.bfloat16`（新版 transformers 弃用警告）

### 注意事项

- Pythia-410m-deduped 模型尚未缓存到服务器。正式运行前需 `source /etc/network_turbo && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && export HF_HOME=/root/autodl-tmp/.hf_cache` 后下载模型（或在 run_pipeline.py 中预下载）。

---
