# code w5 lora prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5_lora_prep_20260515T143139_result.json`
- **Structured JSON:** [`dc32e45b64b854a0f6b8.json`](../../sessions/dc/dc32e45b64b854a0f6b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。全部就绪，汇总如下：

---

**环境状态**：所有依赖已安装（peft 0.19, trl 1.1, accelerate 1.13, wandb 0.26）。

**已有产出**：
| 文件 | 状态 |
|------|------|
| `scripts/prepare_sft_data_scierc.py` | 完整，已运行 |
| `scripts/train_lora_scierc.py` | 完整，dry-run 通过 |
| `data/sft/scierc_sft_train.jsonl` | 1762 样本 |
| `data/sft/scierc_sft_dev.jsonl` | 260 样本 |

**Dry-run 结果**：
- 2 步完成，loss=0.49，mean_token_accuracy=95%
- 每步 ~3.5s（batch=4, grad_accum=4, effective_batch=16）

**训练时间预估**：
- 1762 / 16 ≈ 110 steps/epoch × 3 epochs = ~330 steps
- 330 × 3.5s ≈ **19 分钟**（+ 合并时间 ~2-3 分钟）

**Eval 兼容性确认**：
`run_constrained_extraction.py` 的 `--model_path` 直接加载 HF 格式模型，合并后的 `checkpoints/qwen3_8b_lora_scierc_merged/` 可直接使用，零代码修改：
```bash
python run_constrained_extraction.py --mode unconstrained \
    --model_path checkpoints/qwen3_8b_lora_scierc_merged \
    --dataset scierc --data_path data/processed_data/test.json \
    --constraints_path &lt;constraints_path> --output_path &lt;output_path>
```

**唯一 warning**：`torch_dtype` deprecated → `dtype`，不影响功能。可选择性修复。

GPU 释放后直接运行 `CUDA_VISIBLE_DEVICES=0 python scripts/train_lora_scierc.py` 即可。

---
