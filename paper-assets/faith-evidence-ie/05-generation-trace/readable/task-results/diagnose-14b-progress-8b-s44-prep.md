# diagnose 14b progress 8b s44 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b-progress-8b-s44-prep_20260523T050412_result.json`
- **Structured JSON:** [`7087bd21b281e5965906.json`](../../sessions/70/7087bd21b281e5965906.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part A: 14B s43 Generation 进度

| 指标 | 值 |
|------|-----|
| 当前行数 | **14,992** / 24,216 |
| 进度 | **61.9%** |
| 进程状态 | PID 194682, 运行 10h47m, CPU 100%, RSS 2.4GB |
| 生成速率 | ~1,390 lines/hour |
| 剩余 | 9,224 lines → **约 6h38m** |
| 预计完成 | **今天 ~17:00 UTC+8** |
| 磁盘 | 87GB 可用 (76%) ✅ |

### CED Scoring 环境就绪情况

| 组件 | 状态 | 路径 |
|------|------|------|
| Score+Filter 脚本 | ✅ | `/root/autodl-tmp/freige/training/rsft_score_filter.py` |
| CED Evidence Filter | ✅ | `/root/autodl-tmp/freige/eval/ced_evidence_filter.py` |
| NLI DeBERTa-v3-base | ✅ 已缓存 | `.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base` |
| NLI DeBERTa-v3-large | ✅ 已缓存 | `.hf_cache/hub/models--cross-encoder--nli-deberta-v3-large` |

CED scoring pipeline 就绪，14B generation 完成后可直接启动。

### Part B: 8B RSFT s44 Adapter

**找到**: `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44/`
- `adapter_model.safetensors` 698MB, 创建于 May 19
- 含 checkpoint-1100, checkpoint-1134

**8B s44 with-evi test eval 完整命令**:

```bash
CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --split test_revised \
  --max_new_tokens 2048 \
  --no-quantize \
  --seed 44 \
  --output_dir /root/autodl-tmp/eval_results/test_eval_8b_rsft_s44_with_evi
```

注意：按 C001 约束，提交前需 `nvidia-smi` 确认 cuda:0 显存占用 < 2GB。

---
