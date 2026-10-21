# prep 1 7b scaling seeds

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_1_7b_scaling_seeds_20260518T144205_result.json`
- **Structured JSON:** [`0579d183b0e1efa95cfd.json`](../../sessions/05/0579d183b0e1efa95cfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本全部就绪，dry-run 通过。

**创建的脚本：**

| 脚本 | 用途 |
|------|------|
| `sft_1_7b_s43.sh` | SFT 训练 seed=43 |
| `sft_1_7b_s44.sh` | SFT 训练 seed=44 |
| `eval_sft_1_7b_s43.sh` | Eval seed=43 (D076) |
| `eval_sft_1_7b_s44.sh` | Eval seed=44 (D076) |

**超参与 canonical 完全一致**（lr=2e-4, bs=1, grad_accum=16, epoch=3, warmup_ratio=0.05, lora=64/128/0.05, bf16 no-quantize, max_length=4096），仅改 seed 和 output_dir。

**输出路径：**
- 训练：`/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43/` 和 `_seed44/`
- Eval：`/root/autodl-tmp/eval_results/sft_1_7b_s43_eval/` 和 `_s44_eval/`

**Eval 参数**参照 canonical 1.7B SFT eval 的实际配置（`model_path`=base model, `sft_adapter`=LoRA adapter, bs=4, no-quantize, seed=42）。

**启动方式：**
```bash
GPU=X bash scripts/seed_expansion/sft_1_7b_s43.sh
GPU=X bash scripts/seed_expansion/eval_sft_1_7b_s43.sh
```

注意：现有的 `train_1_7b_s43.sh` / `train_1_7b_s44.sh` 是 **RSFT** 脚本（用 `rsft_trainer`），与这里新建的 SFT 脚本不冲突。

---
