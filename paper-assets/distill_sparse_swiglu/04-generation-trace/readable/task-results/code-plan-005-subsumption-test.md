# code plan 005 subsumption test

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_subsumption_test_20260515T194504_result.json`
- **Structured JSON:** [`b73fcd0ee0c46c14d284.json`](../../sessions/b7/b73fcd0ee0c46c14d284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。所有组件加载成功：
- 模型：32 层, hidden=4096, intermediate=14336
- Predictor：75.96M params
- SPON biases：458,752 params (mean_norm=0.053, max_norm=0.066 — 非常小)

---

**产出**

1. **代码文件**: `/root/distill_sparse_swiglu/src/subsumption_test.py`

2. **完整运行命令**:
```bash
cd /root/distill_sparse_swiglu && source setup_env.sh && \
python src/subsumption_test.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --predictor_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \
  --spon_checkpoint checkpoints/spon_2048_s42/spon_biases.pt \
  --num_samples 50 \
  --seq_len 2048 \
  --gpu 0 \
  --output_dir results/subsumption_test
```

3. **架构发现**:
   - 现有 `SPONPatcher` 缺少 `spon_only` 模式（仅 bias 无 mask），脚本自建 `SubsumptionPatcher` 支持 4 种模式
   - 关键数学性质：`down_proj` 是线性的 → 单层内 mask+bias 效果严格可加（interaction=0）。logit 层面的非零 linearity_ratio 完全来自跨层级联非线性
   - SPON bias norm 极小（mean=0.053），预期 magnitude_ratio 会很低，支持 subsumption 假设
   - Per-layer 分析使用 dense forward 捕获的 MLP input 做隔离测试，避免级联效应污染

---
