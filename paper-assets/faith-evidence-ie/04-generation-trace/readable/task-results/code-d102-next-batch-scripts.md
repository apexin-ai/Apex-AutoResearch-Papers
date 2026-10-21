# code d102 next batch scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d102_next_batch_scripts_20260518T070828_result.json`
- **Structured JSON:** [`fbea12b00f06129a2776.json`](../../sessions/fb/fbea12b00f06129a2776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本已就绪，位于 `/tmp/d102_next_batch/`。

---

## 脚本汇总

| 脚本 | 关键超参 | GPU | 预估时间 | 数据路径 |
|---|---|---|---|---|
| `sft_seed43.sh` | seed=43, lr=2e-4, epochs=3, QLoRA r64/a128, DeepSpeed ZeRO-2, batch=1x16x4GPU=64 | 4 GPU | ~2h | DocRED train (`/root/autodl-tmp/data/docred`) |
| `sft_seed44.sh` | seed=44, 其余同上 | 4 GPU | ~2h | 同上 |
| `grpo_bf16_g4.sh` | **--no_quantize** (bf16 LoRA), G=4, kl=0, lr=5e-6, max_steps=200, CED reward (0.3/3.0/1.0) | 1 GPU | ~4-6h | DocRED train, SFT adapter: `sft_output/` |
| `random_rsft.sh` | random k=1 selection (2716 samples), lr=2e-5, epochs=3, batch=4x4=16 | 1 GPU | ~1.5h | `rsft_generations/generations.jsonl` → random select → train |

## 注意事项

1. **磁盘满了** — `/root/autodl-tmp/` 250G/250G (0 可用)。运行前必须清理。大头是 RSFT 输出（~150G+），建议清理不再需要的旧 checkpoint。
2. SFT seed43/44 需要 4 GPU（与原始 SFT 一致），必须串行或在 D102 完成后运行。
3. GRPO bf16 和 Random RSFT 各用 1 GPU，可以同时运行（`CUDA_VISIBLE_DEVICES=0` 和 `=1`）。
4. GRPO bf16 内存：需确认 — bf16 全精度 Qwen3-4B (~8GB) + LoRA + generation buffer 在单卡 32GB 是否足够。如果 OOM，可能需要降低 `--max_new_tokens` 或加 `--reward_device cpu`（已设 `cuda`）。

---
