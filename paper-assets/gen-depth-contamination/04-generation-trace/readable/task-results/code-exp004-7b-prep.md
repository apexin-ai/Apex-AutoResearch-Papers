# code exp004 7b prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004_7b_prep_20260514T022738_result.json`
- **Structured JSON:** [`25048a5542712c11b0ef.json`](../../sessions/25/25048a5542712c11b0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. VRAM 评估

| 方案 | 模型 VRAM | Peak VRAM | 可行性 |
|------|-----------|-----------|--------|
| A: fp16 | ~14GB | ~16.2GB | 需独占 GPU，batch=1 可跑 |
| B: 4-bit | ~4GB | ~6GB | 量化噪声可能掩盖 depth 信号，仅 preliminary |

**推荐方案 A**，等 exp-006 完成后独占 GPU 运行。

### 2. 脚本部署
`scripts/run_exp004_qwen7b_depth.py` (689 行) 已部署到服务器，语法验证通过。

相比 run_pipeline.py 的改动：
- 模型默认 Qwen2.5-7B-Instruct，batch_size 默认 1
- OOM 保护：`try/except torch.cuda.OutOfMemoryError`，自动降 batch_size 重试
- `--quantize 4bit` 可选参数（bitsandbytes NF4）
- 每个 depth level 之间 `torch.cuda.empty_cache()`
- `--n_docs` 参数替代 `--num_samples`

### 3. 模型下载状态
**7B 模型未下载**。缓存中只有 Qwen2.5-1.5B-Instruct (2.9GB)。下载命令（不要在 GPU 繁忙时执行）：
```bash
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1
python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"
```
预计下载 ~14GB，建议 exp-006 完成后执行。

### 4. Dry-run 命令（ready to execute）
```bash
cd /root/autodl-tmp/gen-depth-contamination
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python scripts/run_exp004_qwen7b_depth.py --n_docs 10 --max_depth 3 --device cuda:0
```
4-bit 预检版：
```bash
python scripts/run_exp004_qwen7b_depth.py --n_docs 10 --max_depth 3 --quantize 4bit --device cuda:0
```

---
