# train 3B d100 s123 a32 cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_3B_d100_s123_a32_cuda1_20260516T110956_result.json`
- **Structured JSON:** [`b791b7de41780b59c540.json`](../../sessions/b7/b791b7de41780b59c540.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练已完成，无需重新提交。**

总结：

| 项目 | 状态 |
|------|------|
| 输出目录 | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/` 已存在 |
| LoRA adapter | `adapter_model.safetensors` + tokenizer + training_args.bin 齐全 |
| 参数确认 | lora_alpha=32, r=16, seed=123, lr=5e-5, epochs=1 ✓ |
| 合并模型 | 无 merged 目录（`--merge` 未执行，但 LoRA adapter 完整可用） |
| Registry | 无记录 — 需要补登 |
| GPU 1 | 被 0.5B_d100_s123 signals 任务占用 (PID 761755) |

**建议**：
1. 训练无需重新跑——权重已完整
2. 需要补登 registry（标为 DONE）
3. 如果后续信号计算需要 merged 模型，可单独跑 merge 步骤

是否需要我补登 registry 记录？

---
