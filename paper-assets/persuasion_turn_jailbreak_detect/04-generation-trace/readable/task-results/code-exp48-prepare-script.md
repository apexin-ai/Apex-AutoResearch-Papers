# code exp48 prepare script

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp48_prepare_script_20260522T063547_result.json`
- **Structured JSON:** [`8a5b6771317429bbdd8b.json`](../../sessions/8a/8a5b6771317429bbdd8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本准备完毕。总结：

**`/root/persuasion_turn_jailbreak_detect/scripts/exp48_ensemble.py`** 已部署到服务器，dry-run 通过。

**Checkpoint 映射**（从 exp35 确认）：
- **JB-MLM**: `checkpoints_archive/plan_017_mlm{,_seed123,_seed456}/best/` (safetensors) + `.../gru/best.pt`
- **9-class**: `checkpoints_archive/plan_002{,_seed123,_seed456}/deberta_multitask/best/model.pt` (state_dict) + `.../gru/treatment/best.pt`

**脚本功能**：
- 加载两组 DeBERTa+GRU pipeline，提取所有数据集的 logits
- 3 种融合：logit averaging、majority vote (AND/OR)、weighted prob avg (5 个权重 grid search)
- 评估：IID test F1、OOD DD/AA/FITD F1（vs IID benign）、ToxicChat F1 (408条)、WildChat FPR (49条)
- 同时输出两个模型的 individual baseline 作为对照
- 支持 `--seeds 42 123 456` 做 3-seed（默认 seed 42）、`--dry-run` 验证

**运行方式**（等 exp45 结束后）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/persuasion_turn_jailbreak_detect && \
python scripts/exp48_ensemble.py --device cuda:0
```

结果输出到 `/root/persuasion_turn_jailbreak_detect/results/exp48_ensemble.json`。

---
