# research pythia69b pipeline survey

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pythia69b_pipeline_survey_20260521T014719_result.json`
- **Structured JSON:** [`004d5737410b0d9938ae.json`](../../sessions/00/004d5737410b0d9938ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息齐全，以下是调研报告。

---

## Pipeline 组件

### 1. Generation 脚本
- **路径**: `scripts/run_pipeline.py` (739 行，完整 pipeline：seed → generation → features → OBD)
- **关键参数**:
  - `--model_path`: 模型路径
  - `--data_dir` / `--results_dir`: 数据和结果输出目录
  - `--num_samples`: seed 文档数 (default=5000)
  - `--max_depth`: 最大 depth (default=5)
  - `--batch_size`: generation batch size (default=16)
  - `--generation_mode`: `rewrite` (instruct prompt) 或 `continuation` (截断前半 + 续写，base model 用)
  - `--scorer_path`: 用不同模型做 surprisal scoring（默认 = generator model）
  - `--max_new_tokens`: seed 截断长度和生成长度 (default=256)
  - `--skip_generation`: 跳过 seed+generation 步骤
- **生成设置**:
  - `--do_sample` / `--no_sample`: 是否采样
  - `--top_p` (default=0.95)
  - `--temperature` (default=1.0)
- **C4 数据源**: HuggingFace `allenai/c4` validation shard `c4-validation.00000-of-00008.json.gz`，streaming 模式，取前 N 条文档，tokenize 后截断到 max_tokens
- **Generation 逻辑**: 
  - `continuation` mode (Pythia 用的): 取前一 depth 文本的前 50% tokens 作为 prefix，model.generate 续写 max_new_tokens
  - `rewrite` mode (instruct model 用): 用 REWRITE_PROMPT 让模型重写

### 2. Feature Extraction
- **路径**: `scripts/run_pipeline.py` 中的 `extract_all_features()` 函数 (line ~350-500)
- **15D features**:
  - Surprisal (9D): `surp_mean, surp_std, surp_skew, surp_kurt, surp_d1_mean, surp_d1_std, surp_d1_skew, surp_d2_mean, surp_d2_std`
  - Vocab diversity (3D): `ttr, hapax_ratio, self_bleu`
  - Tail-thinning (3D): `freq_kurtosis, freq_entropy, low_freq_ratio`
- **Scorer**: 默认用 generator model，可通过 `--scorer_path` 指定（7B scorer ablation 实验用 Qwen2.5-7B 做 scorer）
- **输出**: `{data_dir}/features.csv`
- **feat_batch_size**: default=8

### 3. OBD Classifier
- **路径**: `scripts/run_pipeline.py` 中的 `run_analysis()` 函数 (line ~520)
- **方法**: LightGBM pairwise binary classification (5-fold GroupKFold CV by doc_id)
  - n_estimators=200, max_depth=6, lr=0.05, num_leaves=31
- **输出**:
  - `pairwise_results.json`: pairwise AUC for adjacent depths
  - `jsd.json`: pairwise JSD
  - `ordinal_results.json`: ordinal classification MAE/accuracy
  - `summary.txt`: 汇总
- **K\* 计算**: max depth k where AUC(k-1 vs k) > θ=0.60

### 4. Pythia-1.4B C4 配置参考

**exp020 (Pythia-1.4B C4 greedy, 主实验)**:
```bash
python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 \
  --data_dir data_exp020_pythia_greedy \
  --results_dir results_exp020_pythia_greedy \
  --num_samples 5000 --max_depth 5 --batch_size 16 \
  --generation_mode continuation --no_sample
```
- **结果**: K\*=2, AUC(0v1)=0.999, AUC(1v2)=0.884, AUC(2v3)=0.534
- 7B scorer ablation 对同数据重新提 feature → K\*=2 一致 (AUC: 0v1=0.997, 1v2=0.894)

**exp025 (Pythia-1.4B arXiv)**:
- K\*=3, AUC(0v1)=0.988, AUC(1v2)=0.805, AUC(2v3)=0.655

### 5. Pythia-6.9B 实验方案

| 项目 | 估算 |
|------|------|
| **模型显存** | fp16 ≈ 12.9 GB |
| **可用 GPU** | RTX 4090D 24GB → 剩余 ~11GB 给 KV cache + batch |
| **generation batch_size** | 建议降到 **4** (256 tokens * 4 = ~1K tokens KV cache, ~2-3GB) |
| **feat_batch_size** | 建议降到 **2** (scorer forward pass 显存更大) |
| **generation 时间** | 5000 docs × 5 depths, batch=4 → 每 depth ~1250 batch, 估计每 depth 2-3 小时, 总计 ~12-15h |
| **feature 时间** | 30000 条 × batch=2 → ~4-6h |
| **OBD 时间** | < 5 min |
| **磁盘** | 数据盘 129GB 可用，模型 ~14GB + 数据 ~200MB，充足 |

**建议命令**:
```bash
# 1. 下载模型 (先 source /etc/network_turbo)
python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; \
  AutoModelForCausalLM.from_pretrained('EleutherAI/pythia-6.9b', cache_dir='/root/autodl-tmp/.hf_cache'); \
  AutoTokenizer.from_pretrained('EleutherAI/pythia-6.9b', cache_dir='/root/autodl-tmp/.hf_cache')"

# 2. 运行 pipeline (可复用 exp020 的 depth_0.jsonl 做 seed)
python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/... \
  --data_dir data/exp_pythia6b9_c4 \
  --results_dir results/exp_pythia6b9_c4 \
  --num_samples 5000 --max_depth 5 \
  --batch_size 4 --feat_batch_size 2 \
  --generation_mode continuation --no_sample
```

**注意事项**:
- Pythia-6.9B 是 base model → 必须用 `--generation_mode continuation --no_sample`（与 Pythia-1.4B 一致）
- 可以 symlink `data_exp020_pythia_greedy/depth_0.jsonl` 到新 data_dir 下复用 seed，然后从 depth_1 开始生成，但需要注意 seed 的 tokenize 截断是用 Pythia-1.4B tokenizer 做的（两个 Pythia 共享同一 tokenizer，所以可以复用）
- 服务器上 Pythia-6.9B 尚未下载（只有 pythia-1.4b），需先下载 ~14GB
- 生成时间较长（~15h），建议 nohup 后台执行

---
