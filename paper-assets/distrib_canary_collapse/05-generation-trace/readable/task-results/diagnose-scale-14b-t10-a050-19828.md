# diagnose scale 14b t10 a050 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t10_a050_19828_20260522T090524_result.json`
- **Structured JSON:** [`51adc671e37714f12318.json`](../../sessions/51/51adc671e37714f12318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fix applied to both servers. Now here's the diagnostic report:

---

## 诊断报告：scale_14b_t10_a050_s42_fp32_19828

### 崩溃位置
**Gen 1**，在 checkpoint 保存成功后、metrics 打印阶段崩溃（`iterative_train.py:360`）。

### 根因
1. 19828 网络不通（`[Errno 101] Network is unreachable`），无法下载 `gpt2-large` 配置，MAUVE 计算失败返回 None
2. `effective_rank` 在格式化字符串中使用 `:.1f` 但值为 None，没有 None 保护（MAUVE 有保护，但 perplexity/entropy/effective_rank 没有）

### 两台服务器代码差异
**无差异**。17855 上的 v2 实验使用的是完全相同的代码，只是碰巧没有触发此 bug。

### 修复内容
在 19828 和 17855 上同时修复。为 `perplexity`、`token_entropy`、`effective_rank` 三个 metric 在两处 print 语句（gen_0 baseline + gen_1+ loop）中添加了 None 保护，None 时显示 "N/A"。

### 可用 Checkpoint
| 目录 | 状态 | 内容 |
|------|------|------|
| gen_0 | ✅ 完成 | metrics.json + synthetic_data（baseline，无 checkpoint） |
| gen_1 | ✅ 完成 | checkpoint (5.6GB model.safetensors) + metrics.json + synthetic_data |
| gen_2 | ❌ 空目录 | 崩溃前仅创建了目录 |

可从 **gen 2** resume。

### Resume 命令
```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
nohup python iterative_train.py \
  --model_name /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped \
  --data_dir data/wikitext103_5k \
  --output_dir results/phase_diagram/t10_a050_s42_fp32_14b \
  --synthetic_ratio 0.5 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --seed 42 \
  --batch_size 4 \
  --max_length 512 \
  --lr 5e-5 \
  --gen_batch_size 8 \
  --optim adamw_torch \
  --start_gen 2 \
  > ~/runs/distrib_canary_collapse/scale_14b_t10_a050_s42_fp32_19828.log 2>&1 &
```

**注意**：19828 网络不通，MAUVE 会持续为 N/A。修复后不会崩溃，只是该指标缺失。

---
