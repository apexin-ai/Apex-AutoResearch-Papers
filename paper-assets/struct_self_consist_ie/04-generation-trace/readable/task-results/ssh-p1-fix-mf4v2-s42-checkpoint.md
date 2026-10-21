# ssh p1 fix mf4v2 s42 checkpoint

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_fix_mf4v2_s42_checkpoint_20260521T205933_result.json`
- **Structured JSON:** [`9b507d41761f35a931be.json`](../../sessions/9b/9b507d41761f35a931be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 通过——模型开始加载 4/4 shards，tokenizer 无报错。

---

## Checkpoint 修复
- **5090 checkpoint 路径**: `checkpoints/qwen3-8b-fewnerd-exp021-merged/`
- **缺失文件**: model-00003-of-00004.safetensors, model-00004-of-00004.safetensors, model.safetensors.index.json, special_tokens_map.json, tokenizer.json, tokenizer_config.json, vocab.json（共 7 个）
- **修复方式**: 从本地嵌套子目录 `qwen3-8b-fewnerd-exp021-merged/qwen3-8b-fewnerd-exp021-merged/` 复制，无需跨服务器 rsync
- **修复后验证**: OK — tokenizer 加载成功 (151669 tokens), dry run 15 秒内正常启动模型加载

## 重启命令
- **工作目录**: `/root/autodl-tmp/struct_self_consist_ie`
- **完整命令**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed42_v3/
```
- **预期输出目录**: `output/fewnerd_mf4v2_seed42_v3/`
- **GPU**: cuda:0（4 卡全空闲）
- **tmux session 名**: `exp_fewnerd_mf4v2_s42_v3`
- **日志路径**: `~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s42_v3.log`

---
