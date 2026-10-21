# diagnose 1 7b rsft s43 exit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_1_7b_rsft_s43_exit_20260519T032242_result.json`
- **Structured JSON:** [`118063aac1e686f77700.json`](../../sessions/11/118063aac1e686f77700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：**SUCCESS**

训练正常完成。证据：

1. **trainer_state 确认**：`max_steps=567`, `should_training_stop=true`, 最后记录 step=560, loss=0.5526, token_accuracy=86.9%
2. **输出完整**：
   - 最终 adapter：`/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43/adapter_model.safetensors` (278MB)
   - 中间 checkpoints：checkpoint-550, checkpoint-567
   - adapter_config：LoRA r=64, alpha=128, base=Qwen3-1.7B
   - training_args.bin, tokenizer 全套文件均存在
3. **Steps 精确匹配**：3021 samples / (batch_size=4 × grad_accum=4) × 3 epochs = 567 steps
4. **cuda:2 当前空闲**：0MiB, 0% utilization

| 项目 | 值 |
|---|---|
| 结论 | **success** |
| Checkpoint 路径 | `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43/` |
| 最终 step | 567 (3 epochs 完整) |
| 最终 loss | 0.5526 |
| 最终 token accuracy | 86.9% |
| cuda:2 状态 | 空闲 |
| tmux session | 已自动退出（不存在） |

---
