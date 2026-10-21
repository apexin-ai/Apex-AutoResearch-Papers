# prep mf5 depth baseline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_mf5_depth_baseline_20260522T072429_result.json`
- **Structured JSON:** [`bf5a7d134721d14da0a0.json`](../../sessions/bf/bf5a7d134721d14da0a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。汇报如下：

```
== synthetic_depth_scores.pt 格式 ==
Keys: ['attn_importance', 'mlp_importance']
attn: layers=28, shape=(4,)/layer, dtype=float32
  layer 0-9: 1.0 (保留), layer 27: 0.001 (剪掉)
mlp: layers=28, shape=(28,)/layer, dtype=float32
  layer 0-9: 1.0 (保留), layer 27: 0.001 (剪掉)
与 prune.py 兼容: ✅ (key names 完全匹配，standard mode 直接用 attn/mlp_importance)

== Dry-run prune ==
Exit code: 0
Output model: 12GB (model.safetensors)
Actual sparsity: 19.12% (target 20%)
Per-layer config:
  Layer 0-9, 11-17: MLP 18944 (100%), Attn 28 heads (100%) — 完全保留
  Layer 10: MLP 14212 (75%), Attn 7 heads (25%) — 过渡层
  Layer 18-27: MLP 8128 (43%), Attn 7 heads (25%) — 重剪
  → 深层大砍、浅层完好，符合 depth-first 设计意图
Forward validation: OK (output shape [1,32,152064])

== SFT 加载测试 ==
Status: ✅ (via load_pruned_model)
Model params: 6.16B

== 推荐服务器 ==
westb-23072 cuda:1
原因：
  1. C005 白名单内（westd-32935 不在白名单）
  2. cuda:1 空闲 (0 MiB / 97887 MiB)
  3. DeepSeek-7B 已在 /root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B
  4. scores 仅 18KB，scp 秒级拷贝

== Ready-to-submit commands (westb-23072) ==

# 0. 拷贝 scores (从 westd-32935)
scp westd-32935:/root/autodl-tmp/recovery_aware_struct_prune/synthetic_depth_scores.pt \
    westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/

# 1. Prune
cd /root/recovery_aware_struct_prune && python src/prune.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-7B \
  --importance_path /root/autodl-tmp/recovery_aware_struct_prune/synthetic_depth_scores.pt \
  --mode standard \
  --sparsity 0.2 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_depth_first_20

# 2. SFT
python src/sft_recovery.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_depth_first_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_depth_first_20 \
  --gpu 1

# 3. GRPO seed 123
python src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_depth_first_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20_seed123 \
  --gpu 1 \
  --max_steps 100 \
  --seed 123 \
  --wandb_project recovery_aware_struct_prune \
  --run_name grpo_depth_first_20_seed123

# 4. GRPO seed 456
python src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_depth_first_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20_seed456 \
  --gpu 1 \
  --max_steps 100 \
  --seed 456 \
  --wandb_project recovery_aware_struct_prune \
  --run_name grpo_depth_first_20_seed456

# 5. GSM8K eval × 2
python src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20_seed123 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/artifacts/eval_gsm8k_depth_first_20_seed123.json

python src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20_seed456 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/artifacts/eval_gsm8k_depth_first_20_seed456.json

== 阻塞项 ==
1. westd-32935 不在 C005 GPU 白名单内 — 若要用 westd-32935 需先确认白名单更新
2. westb-23072 需拷贝 synthetic_depth_scores.pt（18KB，秒级）
3. westb-23072 cuda:0 被占用，pipeline 全部需指定 --gpu 1
```

---
