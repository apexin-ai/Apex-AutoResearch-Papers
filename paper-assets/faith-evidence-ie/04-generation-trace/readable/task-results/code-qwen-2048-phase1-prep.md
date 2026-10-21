# code qwen 2048 phase1 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-2048-phase1-prep_20260521T033829_result.json`
- **Structured JSON:** [`9c5d41e6e1aae853f5eb.json`](../../sessions/9c/9c5d41e6e1aae853f5eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## 路径验证

| 路径 | 状态 |
|------|------|
| 1.7B base: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` | ✓ |
| 1.7B SFT s42: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16` | ✓ |
| 1.7B SFT no-evi: `/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence` | ✓ |
| 8B base: `/root/autodl-tmp/models/Qwen/Qwen3-8B` | ✓ |
| 8B SFT s42: `/root/autodl-tmp/sft_output_qwen3_8b_bf16` | ✓ |
| 8B SFT no-evi: `/root/autodl-tmp/sft_output_qwen3_8b_no_evidence` | ✓ |
| 4B base: `/root/autodl-tmp/models/Qwen3-4B` | ✓ (注意：无 `Qwen/` 子目录) |
| 4B SFT s42: `/root/autodl-tmp/sft_output/` | ✓ |
| 4B SFT no-evi: `/root/autodl-tmp/sft_no_evidence_output/` | ✓ |

## no-evi eval 机制

**不需要专门训练。** 但实际上三个尺寸都已有独立训练的 no-evidence adapter（训练时不含 evidence 字段）。`--no_evidence` 是 inference.py 的参数，切换 system prompt 为 `NO_EVIDENCE_SYSTEM_PROMPT` 并设 `_include_evi=False`。

**4B no-evi eval 可行**：adapter 在 `/root/autodl-tmp/sft_no_evidence_output/`，从 `sft_no_evidence_noquant` 的 metrics.json 确认此 adapter 之前已成功运行过（F1=48.76%）。

**SFT eval 正确参数模式**（从已有 metrics.json 确认）：`--model_path &lt;BASE_MODEL> --sft_adapter &lt;SFT_ADAPTER>`（model_path 指向 base model，不触发 adapter auto-detect）。

## GPU 状态

```
GPU 0: 18879 / 97887 MiB  (19%)
GPU 1: 32503 / 97887 MiB  (33%) ← 被占用
GPU 2: 18879 / 97887 MiB  (19%)
GPU 3: 18879 / 97887 MiB  (19%)
```

GPU 0/2/3 均 ~19GB（可能是 CUDA persistent context），GPU 1 有额外负载。1.7B bf16 仅 ~3.4GB，剩余空间充足。

## Phase 1 就绪命令

**Phase 1a: 1.7B SFT s42 with-evi@2048 (cuda:2)**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_with_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 42"
```

**Phase 1b: 1.7B SFT s42 no-evi@2048 (cuda:3)**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_1_7b_sft_s42_no_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42"
```

## Phase 2/3 就绪命令

**8B SFT s42 with-evi@2048**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=&lt;GPU> python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_8b_sft_s42_with_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 42"
```

**8B SFT s42 no-evi@2048**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=&lt;GPU> python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_8b_sft_s42_no_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42"
```

**4B SFT s42 with-evi@2048**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=&lt;GPU> python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_4b_sft_s42_with_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 42"
```

**4B SFT s42 no-evi@2048**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=&lt;GPU> python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/d140_4b_sft_s42_no_evi_2048 --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42"
```

## 注意事项

1. **@1024 参考基线**：1.7B with-evi@1024 截断 314/985 (31.9%), 8B with-evi@1024 截断 313/985 (31.8%), 4B with-evi@1024 截断 288/985 (29.2%)。@2048 应显著降低截断率。
2. **8B eval 显存**：8B bf16 ~16GB，需要单独一张空卡。GPU 1 当前被占用（32.5GB），不可用。
3. **GPU 0/2/3 的 ~19GB 占用**：可能是 CUDA persistent context 或其他常驻进程，提交前建议 `fuser -v /dev/nvidia*` 确认无训练进程。

---
