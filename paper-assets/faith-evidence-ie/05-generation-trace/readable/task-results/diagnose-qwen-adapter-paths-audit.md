# diagnose qwen adapter paths audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen-adapter-paths-audit_20260521T031315_result.json`
- **Structured JSON:** [`5f63adc4a3c875dcd1f2.json`](../../sessions/5f/5f63adc4a3c875dcd1f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen Adapter 路径

| Scale | Base model | SFT adapter (s42) | SFT s43 | SFT s44 | SFT no-evi | 全部存在? |
|-------|-----------|-------------------|---------|---------|-------------|----------|
| 1.7B | `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` | `sft_output_qwen3_1_7b_bf16` | `..._seed43` | `..._seed44` | `sft_output_qwen3_1_7b_no_evidence` | ✅ |
| 4B | `/root/autodl-tmp/models/Qwen3-4B` | `sft_output` (无后缀=s42) | `sft_output_seed43` | `sft_output_seed44` | `sft_no_evidence_output` | ✅ |
| 8B | `/root/autodl-tmp/models/Qwen/Qwen3-8B` | `sft_output_qwen3_8b_bf16` | `..._s43` | `..._s44` | `sft_output_qwen3_8b_no_evidence` | ✅ |

RSFT adapters 也全在：`rsft_output_qwen3_1_7b_k1{,_s43,_s44}`, `rsft_output_4b_sft_s44_bf16`, `rsft_output_qwen3_8b_k1{,_s43,_s44}`

注意：4B base model 路径是 `/root/autodl-tmp/models/Qwen3-4B`（不在 `Qwen/` 子目录下）。

## No-evi Eval 参考命令（@2048 模板）

**1.7B** — 已有 2048 脚本 `scripts/seed_expansion/eval_1_7b_no_evidence_2048.sh`：
```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_k1 \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
    --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_outputs/eval_1_7b_rsft_no_evidence_2048 \
    --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42
```

**4B：**
```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_4b_sft_s44_bf16 \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output_seed44/ \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_outputs/eval_4b_rsft_s44_no_evidence_2048 \
    --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42
```

**8B：**
```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1 \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16/ \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_outputs/eval_8b_rsft_s42_no_evidence_2048 \
    --batch_size 4 --max_new_tokens 2048 --no-quantize --no_evidence --seed 42
```

关键：所有 no-evi eval 必须传 `--no_evidence`（C005）。

## GPU 进度

| GPU | GPU PID | Parent PID | VRAM | GPU Util | Elapsed |
|-----|---------|------------|------|----------|---------|
| 0 | 70711 | 70706 | 18879 MiB | 68% | 26 min |
| 1 | 70393 | 70388 | 32503 MiB | 83% | 27 min |
| 2 | 64396 | 64391 | 18879 MiB | 90% | 2h 26m |
| 3 | 64024 | 64023 | 18879 MiB | 90% | 2h 28m |

4 卡全满，无空闲 GPU。GPU 1 占用 32.5GB（可能是 8B/14B 模型），其余 3 卡各 ~18.9GB。

## 缺失/需要 rsync 的文件

无。所有 Qwen SFT/RSFT adapter 和 base model 均已存在。

---
