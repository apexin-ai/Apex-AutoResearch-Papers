# code exp wiki scorer confound prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_wiki_scorer_confound_prep_20260517T223543_result.json`
- **Structured JSON:** [`749458488a909bdf68fc.json`](../../sessions/74/749458488a909bdf68fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息齐全。方案如下：

## 分析

**Pipeline 行为**：
- `--model_path` = Qwen-7B → 加载后跳过 Step 2 (depth_0 已存在) 和 Step 3 (depth_1-5 已存在且 model_name 匹配)
- `--scorer_path` = Pythia-1.4B → Step 4 卸载 Qwen-7B，加载 Pythia-1.4B 计算 surprisal features
- Step 5 用新 features 训练 LightGBM 并报告 AUC/K*

**数据隔离**：用 symlink 把已有 depth 文件链接到新 data_dir，避免覆盖原 features.csv。

## 执行命令

```bash
bash -c "cd /root/autodl-tmp/gen-depth-contamination && \
mkdir -p data/exp_wiki_scorer_confound && \
for d in 0 1 2 3 4 5; do \
  ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b/depth_\${d}.jsonl \
         data/exp_wiki_scorer_confound/depth_\${d}.jsonl; \
done && \
mkdir -p results/exp_wiki_scorer_confound && \
HF_HOME=/root/autodl-tmp/.hf_cache \
TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache \
/root/miniconda3/bin/python scripts/run_pipeline.py \
  --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B \
  --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 \
  --data_dir data/exp_wiki_scorer_confound \
  --results_dir results/exp_wiki_scorer_confound \
  --num_samples 5000 \
  --max_depth 5 \
  --batch_size 16 \
  --generation_mode rewrite"
```

**执行流程**：
1. 创建 `data/exp_wiki_scorer_confound/`，symlink 6 个 depth 文件
2. 加载 Qwen-7B，跳过生成（model_name 匹配已有文件）
3. 卸载 Qwen-7B，加载 Pythia-1.4B 作为 scorer
4. 用 Pythia-1.4B 计算 15D surprisal features → `data/exp_wiki_scorer_confound/features.csv`
5. LightGBM pairwise AUC + K* → `results/exp_wiki_scorer_confound/`

**代价**：需加载 Qwen-7B 一次（~14GB VRAM），仅用于通过 model_name 检查后立即释放。无需修改代码。

---
