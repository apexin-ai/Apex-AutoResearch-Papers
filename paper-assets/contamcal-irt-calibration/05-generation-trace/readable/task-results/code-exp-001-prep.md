# code exp 001 prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-001-prep_20260513T172528_result.json`
- **Structured JSON:** [`fd8fb7f26c4b02d5f658.json`](../../sessions/fd/fd8fb7f26c4b02d5f658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个文件已创建并通过验证：

| 文件 | 说明 |
|------|------|
| `paraphrase_gen.py` | 对 MMLU/GSM8K/ARC/HumanEval 生成 paraphrase，vLLM 本地 + API 双模式，cosine>0.85 & BLEU<0.3 质控 |
| `prepare_sft_data.py` | 加载 SlimOrca 基础数据 + paraphrase，按 dosage (0/5/25/50/100%) 混合输出 JSONL |
| `train_sft.py` | LoRA SFT (r=16, alpha=32, 7 target modules)，trl SFTTrainer，训练后自动 merge |
| `evaluate.py` | MMLU 5-shot / GSM8K 8-shot CoT / ARC 25-shot / HumanEval pass@1，输出 per-item correctness matrix |
| `run_exp001.sh` | 4 阶段编排，3 models × 5 dosages × 3 seeds = 45 runs，支持断点续传和多 GPU 并行 |
| `requirements.txt` | 14 个依赖 |

路径：`artifacts/exp001_sft_injection/`

---
