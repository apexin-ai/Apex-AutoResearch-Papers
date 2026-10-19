# ops prepare pool50 eval pipeline

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-pool50-eval-pipeline_20260515T182136_result.json`
- **Structured JSON:** [`dd263a5347f3487ec540.json`](../../sessions/dd/dd263a5347f3487ec540.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report.

---

## Pool=50 评估流水线就绪状态报告

### 1. Checkpoint 完成度（阻塞项）

| Encoder | Strategy | s42 | s43 | s44 |
|---------|----------|-----|-----|-----|
| **qwen** | random | ✅ | ✅ | ✅ |
| **qwen** | embedding_distance | ❌ | ✅ | ✅ |
| **qwen** | dataflow_aware | ❌ | ✅ | ❌ |
| **starcoder** | random | ✅ | ✅ | ✅ |
| **starcoder** | embedding_distance | ✅ | ❌ | ❌ |
| **starcoder** | dataflow_aware | ❌ | ❌ | ❌ |

**10/18 checkpoints 就绪。缺 8 个：qwen 缺 3，starcoder 缺 5。**

### 2. 流水线步骤就绪状态

| 步骤 | 脚本 | 位置 | GPU | 状态 |
|------|------|------|-----|------|
| Step 1a | `evaluate_pool50.py` | `/root/structfuse/evaluation/` | ✅ 需要 | ✅ 脚本就绪，dry-run 已验证 |
| Step 1b | `evaluate_stratified.py` | `/root/structfuse/scripts/` | ✅ 需要 | ✅ 脚本就绪，dry-run JSONL 已生成 |
| Step 2 | `analyze_m2_stats.py` | `/root/structfuse/scripts/` | ❌ CPU | ✅ 脚本就绪 |
| Step 3 | `bootstrap_paired_test.py` | `/root/structfuse/scripts/` | ✅ 需要 | ✅ 脚本就绪 |
| Step 4 | `analyze_stratified.py` | `/root/structfuse/scripts/` | ❌ CPU | ✅ 脚本就绪 |

**依赖文件：**
- 验证数据 `val_{strategy}_s{seed}.jsonl` — 全部 12 个文件就绪 ✅
- `stratification_index.json` (19MB) — 就绪 ✅
- per-query 结果目录 — 存在，仅有 dry-run 文件，真实评估数据待 Step 1b 生成

### 3. GPU 需求

- 服务器：2× NVIDIA RTX PRO 6000 Blackwell (98GB VRAM each)
- `evaluate_pool50.py`：加载 3B 模型 + LoRA，约 8-10GB VRAM，可并行两个 GPU
- `evaluate_stratified.py`：同上
- 每个 checkpoint 评估约 2-3 分钟（encoding + pool sampling）

### 4. 完整执行命令序列

M2 全部完成后，copy-paste 执行：

```bash
# ── Step 1a: evaluate_pool50.py (快速 R@1/R@5 汇总) ──────────────
# Qwen (batch mode, 自动发现所有 best_by_* checkpoints)
cd /root/structfuse

# 每个 (strategy, seed) 用对应 val 文件
for strategy in random embedding_distance dataflow_aware; do
  for seed in 42 43 44; do
    ckpt="/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/${strategy}_s${seed}"
    val="/root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl"
    out="/root/structfuse/results/pool50/qwen_${strategy}_s${seed}.json"
    python evaluation/evaluate_pool50.py \
      --checkpoint-dir "$ckpt" --batch-mode \
      --data-path "$val" \
      --base-model /root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B \
      --pool-size 50 --num-samples 5 \
      --output "$out" --gpu 0
  done
done

# Starcoder (同理，gpu 1 可并行)
for strategy in random embedding_distance dataflow_aware; do
  for seed in 42 43 44; do
    ckpt="/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/${strategy}_s${seed}"
    val="/root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl"
    out="/root/structfuse/results/pool50/starcoder_${strategy}_s${seed}.json"
    python evaluation/evaluate_pool50.py \
      --checkpoint-dir "$ckpt" --batch-mode \
      --data-path "$val" \
      --base-model /root/autodl-tmp/structfuse/models/bigcode/starcoder2-3b \
      --pool-size 50 --num-samples 5 \
      --output "$out" --gpu 1
  done
done

# ── Step 1b: evaluate_stratified.py (per-query JSONL) ──────────────
for encoder in qwen starcoder; do
  if [ "$encoder" = "qwen" ]; then
    base_model="/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B"
    gpu=0
  else
    base_model="/root/autodl-tmp/structfuse/models/bigcode/starcoder2-3b"
    gpu=1
  fi
  for strategy in random embedding_distance dataflow_aware; do
    for seed in 42 43 44; do
      ckpt="/root/autodl-tmp/structfuse/checkpoints/m2_full_${encoder}/${strategy}_s${seed}/best_by_recall_at_1"
      val="/root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl"
      python scripts/evaluate_stratified.py \
        --ckpt-dir "$ckpt" \
        --model-name "$base_model" \
        --val-file "$val" \
        --pool-sizes 50 \
        --output-dir /root/structfuse/results/stratified/per_query \
        --tag "${encoder}_${strategy}_s${seed}"
    done
  done
done

# ── Step 2: analyze_m2_stats.py (统计检验，CPU) ──────────────
python scripts/analyze_m2_stats.py \
  --per-query-dir /root/structfuse/results/stratified/per_query \
  --output-dir /root/structfuse/results/stratified

# ── Step 3: analyze_stratified.py (分层分析，CPU) ──────────────
python scripts/analyze_stratified.py \
  --results-dir /root/structfuse/results/stratified/per_query \
  --index-file /root/autodl-tmp/structfuse/stratification_index.json \
  --strategies random,embedding_distance,dataflow_aware \
  --encoder qwen --seeds 42,43,44 --pool-size 50 \
  --output-dir /root/structfuse/results/stratified

# starcoder 同理
python scripts/analyze_stratified.py \
  --results-dir /root/structfuse/results/stratified/per_query \
  --index-file /root/autodl-tmp/structfuse/stratification_index.json \
  --strategies random,embedding_distance,dataflow_aware \
  --encoder starcoder --seeds 42,43,44 --pool-size 50 \
  --output-dir /root/structfuse/results/stratified
```

### 5. 预计运行时间

| 步骤 | 单次 | 总次数 | 预计时间 | 备注 |
|------|------|--------|---------|------|
| Step 1a (pool50 eval) | ~3 min | 18 runs × 2 ckpts | ~50 min | 双 GPU 并行 → ~25 min |
| Step 1b (stratified eval) | ~5 min | 18 runs | ~45 min | 双 GPU 并行 → ~25 min |
| Step 2 (stats) | ~2 min | 1 | 2 min | CPU only |
| Step 3 (stratified) | ~3 min | 2 (per encoder) | 6 min | CPU only |
| **总计** | | | **~60 min** | 双 GPU 并行 |

### 6. 缺失/需修复项

1. **8 个 checkpoint 未完成** — 这是唯一阻塞项。流水线本身全部就绪。
2. **Starcoder base model 路径待确认** — 命令中假设了 `/root/autodl-tmp/structfuse/models/bigcode/starcoder2-3b`，需验证实际路径。
3. **输出目录** — `results/pool50/` 需要创建（`mkdir -p /root/structfuse/results/pool50`）。
4. **evaluate_pool50.py 不产生 per-query JSONL** — Step 2/3 依赖 `evaluate_stratified.py` 的输出，不能只跑 Step 1a。两个 eval 脚本都要跑。

---
