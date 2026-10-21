# code prepare cka 25 pruning

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_cka_25_pruning_20260519T033337_result.json`
- **Structured JSON:** [`3df9a6983cb9079bad72.json`](../../sessions/3d/3df9a6983cb9079bad72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已确认。以下是准备好的命令：

## CKA-only 25% Sparsity Pruning 命令

```bash
cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/prune.py \
  --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --cka_path /root/autodl-tmp/recovery_aware_struct_prune/results/cka_scores_qwen_math.pt \
  --mode cka_only \
  --sparsity 0.25 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 \
  --seed 42 \
  --dtype bfloat16
```

## 说明

- **`--importance_path` 不需要**：`cka_only` 模式只用 CKA overlap scores（`score = 1 - overlap`），不需要 importance scores
- **CKA scores 已存在**：`cka_scores_qwen_math.pt` 包含 28 层的 attn_overlap 和 mlp_overlap，无需重新计算
- **输出路径**：写入数据盘 `/root/autodl-tmp/`（遵守 C002 约束）
- **GPU 需求**：模型加载到 CPU 做 pruning（代码中 `device_map="cpu"`），仅 forward pass 验证需要少量 GPU。单卡即可，预计 2-3 分钟完成
- **参考**：RASP 25% pruning 实际达到 24.05% sparsity（从 7.6B 剪到 5.8B params），CKA-only 25% 预计类似量级

---
