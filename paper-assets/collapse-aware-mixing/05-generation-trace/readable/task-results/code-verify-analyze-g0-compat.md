# code verify analyze g0 compat

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_analyze_g0_compat_20260512T172407_result.json`
- **Structured JSON:** [`91102aac133ff2b0d96e.json`](../../sessions/91/91102aac133ff2b0d96e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 兼容性报告：analyze_g0.py vs v5 checkpoint

### 结论：**完全兼容** ✓

---

### 1. 目录结构匹配

| 项目 | analyze_g0.py 期望 | v5 实际产出 | 状态 |
|------|-------------------|------------|------|
| checkpoint 目录 | `--checkpoint-dir` 下的 `checkpoint-{step}/` 子目录 | `/root/autodl-tmp/output/G0/training/checkpoint-{152,304,...,1373}` | ✓ |
| 命名格式 | regex `checkpoint-(\d+)$` | `checkpoint-152` ~ `checkpoint-1373`（共 10 个） | ✓ |
| 模型权重 | `config.json` + `model.safetensors`（via `AutoModelForCausalLM.from_pretrained`） | 每个 checkpoint 均含 `config.json`（752B）+ `model.safetensors`（~2GB） | ✓ |
| tokenizer | 从 `--model-name` 加载（默认 `EleutherAI/pythia-1b`），**不从 checkpoint 读取** | checkpoint 内无 tokenizer 文件 — 无影响 | ✓ |
| holdout 数据集 | 默认 `/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-103-raw-v1` | 路径存在 | ✓ |

### 2. metrics.py 函数签名匹配

| 函数 | analyze_g0.py 调用方式 | metrics.py 实际签名 | 状态 |
|------|----------------------|-------------------|------|
| `compute_spectral_effective_rank` | `(model, holdout_loader, num_samples=N, device=D)` | `(model, dataloader, num_samples=50000, device="cuda")` → `Dict["spectral_effective_rank"]` | ✓ |
| `compute_perplexity` | `(model, holdout_loader, num_samples=N, device=D)` | `(model, dataloader, num_samples=5000, device="cuda")` → `Dict["perplexity", "avg_loss", "ppl_num_tokens"]` | ✓ |

### 3. 推荐运行命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python /root/collapse-aware-mixing/analyze_g0.py \
    --checkpoint-dir /root/autodl-tmp/output/G0/training \
    --output-dir /root/autodl-tmp/output/g0_analysis \
    --model-name EleutherAI/pythia-1b
```

无需调整任何参数，默认值全部适用。

---
