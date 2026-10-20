# research seed robustness scout

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed_robustness_scout_20260522T003433_result.json`
- **Structured JSON:** [`0ba1dd138e28cef7d5b0.json`](../../sessions/0b/0ba1dd138e28cef7d5b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已添加 `--seed` 参数。现在准备最终报告。

---

## 1. cuda:0 状态

**服务器不可达。** cqa1-22115 (58.144.141.28:22115) SSH 连接失败。AutoDL 实例可能已重启，端口已变。需要去 AutoDL 控制台查新端口并更新 `~/.ssh/config`。

PID 443243 状态和 GPU 空闲情况无法确认。

## 2. Pipeline 侦查结果

**主脚本**: `scripts/run_pipeline.py`，全流程 pipeline (prepare_seed → depth_chain_gen → feature_extract → OBD_analysis)。

关键参数:
- `--model_path`: 同时用于 generation 和 scoring（无独立 scorer 参数）
- `--generation_mode`: `rewrite`(instruct) / `continuation`(base model)
- `--top_p`, `--temperature`, `--do_sample`: sampling 控制
- `--skip_generation`: 跳过 steps 2-3，只做 features + analysis
- `--seed`: **刚添加**，需要 push 到服务器

**关键路径**:
- Pythia-1.4B: `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b`
- Qwen-1.5B base: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`
- WikiText depth_0 源: `/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_0.jsonl`（5000 docs）
- C4: pipeline 自动从 HF 下载

**Pythia 需要两阶段**: pipeline 用同一模型做 generation 和 scoring。Pythia 生成 + Qwen 评分需要：Phase 1 用 Pythia 跑全 pipeline → 删 features.csv → Phase 2 用 Qwen `--skip_generation` 重新评分。

## 3. 运行命令

**前置条件**: 本地 `run_pipeline.py` 已添加 `--seed`，需先 push 到服务器并 `git pull`。

### 实验 1: seed_pythia14b_wiki_s123 (cuda:1 → CUDA_VISIBLE_DEVICES=1)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/gen-depth-contamination && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_ENDPOINT=https://hf-mirror.com && \
mkdir -p data/seed_robustness/seed_pythia14b_wiki_s123/results && \
cp data/exp_023_wiki/depth_0.jsonl data/seed_robustness/seed_pythia14b_wiki_s123/depth_0.jsonl && \
python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b \
  --data_dir data/seed_robustness/seed_pythia14b_wiki_s123 \
  --results_dir data/seed_robustness/seed_pythia14b_wiki_s123/results_gen \
  --max_depth 5 --num_samples 5000 --batch_size 16 \
  --generation_mode continuation \
  --top_p 0.9 --temperature 1.0 --seed 123 && \
rm -f data/seed_robustness/seed_pythia14b_wiki_s123/features.csv && \
python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B \
  --data_dir data/seed_robustness/seed_pythia14b_wiki_s123 \
  --results_dir data/seed_robustness/seed_pythia14b_wiki_s123/results \
  --max_depth 5 --skip_generation --feat_batch_size 16 --seed 123
```

### 实验 2: seed_qwen15b_wiki_s123 (cuda:2 → CUDA_VISIBLE_DEVICES=2)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/gen-depth-contamination && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_ENDPOINT=https://hf-mirror.com && \
mkdir -p data/seed_robustness/seed_qwen15b_wiki_s123/results && \
cp data/exp_023_wiki/depth_0.jsonl data/seed_robustness/seed_qwen15b_wiki_s123/depth_0.jsonl && \
python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B \
  --data_dir data/seed_robustness/seed_qwen15b_wiki_s123 \
  --results_dir data/seed_robustness/seed_qwen15b_wiki_s123/results \
  --max_depth 5 --num_samples 5000 --batch_size 16 \
  --generation_mode continuation \
  --top_p 0.95 --temperature 1.0 --seed 123
```

### 实验 3: seed_qwen15b_c4_s123 (cuda:3 → CUDA_VISIBLE_DEVICES=3)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/gen-depth-contamination && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_ENDPOINT=https://hf-mirror.com && \
source /etc/network_turbo 2>/dev/null && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
mkdir -p data/seed_robustness/seed_qwen15b_c4_s123/results && \
python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B \
  --data_dir data/seed_robustness/seed_qwen15b_c4_s123 \
  --results_dir data/seed_robustness/seed_qwen15b_c4_s123/results \
  --max_depth 5 --num_samples 5000 --batch_size 16 \
  --generation_mode continuation \
  --top_p 0.95 --temperature 1.0 --seed 123
```

注：C4 实验需要 `network_turbo` + SSL 证书设置来下载 C4 validation shard。WikiText 实验不需要（depth_0 已本地）。

## 4. 预估运行时间

基于同服务器 (cqa1-22115) 历史数据：

| 实验 | 方式 | 预估时间 | 参考 |
|------|------|---------|------|
| seed_pythia14b_wiki_s123 | 两阶段 (Pythia gen ~1.6h + Qwen score ~0.5h) | **~2-2.5h** | exp_wiki_pythia_v2: 5810s |
| seed_qwen15b_wiki_s123 | 单阶段 | **~3-3.5h** | exp_023: 12314s |
| seed_qwen15b_c4_s123 | 单阶段 | **~3-3.5h** | exp_023 同量级 |

三组并行运行，总 wall time **~3.5h**。

## 5. 数据集路径

| 数据集 | 服务器路径 | 来源 |
|--------|----------|------|
| WikiText depth_0 | `/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_0.jsonl` | exp-023 准备的 5000 docs |
| C4 | pipeline 自动下载 (`allenai/c4` validation shard) | HuggingFace (via HF_ENDPOINT mirror) |

## 6. 待办

1. **去 AutoDL 控制台获取 cqa1-22115 新端口**，更新 `~/.ssh/config`
2. **同步代码到服务器**（`run_pipeline.py` 的 `--seed` 改动需要 push + pull）
3. 服务器恢复后验证 PID 443243 和 cuda:0 状态
4. 确认 `data/exp_023_wiki/depth_0.jsonl` 在服务器上存在

---
