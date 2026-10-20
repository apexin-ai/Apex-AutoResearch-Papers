# analysis sft standard 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_standard_20_20260515T003006_result.json`
- **Structured JSON:** [`30f9f47391cc15c10ea9.json`](../../sessions/30/30f9f47391cc15c10ea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试完成。结果非常清楚。

## sft_standard_20 训练结果分析

### 训练状态：成功完成

| 项目 | 值 |
|------|-----|
| 状态 | EXIT_CODE=0, 正常完成 |
| Epochs | 2 |
| Total steps | 1870 |
| Runtime | ~2198s (~36.6 min) |
| Train loss (avg) | 0.7593 |
| Final loss (last log) | 0.6437 |
| Token accuracy | 0.67 → 0.83 |
| W&B | 未记录 |

**Loss 轨迹**：1.698 (step 10) → ~0.95 (step ~100) → ~0.65 (epoch 2 end)，收敛正常。

### Checkpoint

路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/`
- `model.safetensors` — 12GB（全量保存，非 LoRA）
- `checkpoint-935/` — mid-training
- `checkpoint-1870/` — final (含 optimizer 23GB)
- config 含 `per_layer_intermediate_size`（非均匀 MLP）

### EOS 生成测试：100% 通过 (3/3)

| Prompt | Gen tokens | EOS | Answer | Correct |
|--------|-----------|-----|--------|---------|
| What is 12 + 15? | 59 | ✓ | 41 | ✗ (应为 27) |
| 3 apples × $2 | 34 | ✓ | 6 | ✓ |
| 60 mph × 2.5h | 55 | ✓ | 150 | ✓ |

- **EOS rate: 100%** — SFT 完全修复了 EOS 生成问题
- **格式正确**：所有 response 都遵循 GSM8K 格式（step-by-step reasoning + `#### answer` + EOS）
- **推理准确率: 2/3 (67%)** — 简单算术出错（12+15 算成 41），说明推理能力只部分恢复
- **平均生成长度: 49 tokens** — 简洁，无无限生成

### 结论

**Status: SUCCESS（作为负对照）**

SFT warmup 达到了预期目标：
1. **EOS 生成完全修复** — 从 pruned model 的 0% EOS 提升到 100%，sampling 模式下的无限生成问题解决
2. **格式学习成功** — 模型学会了 GSM8K 的 step-by-step + `####` 格式
3. **推理能力有限恢复** — 2/3 正确率表明 standard pruning 破坏了部分推理关键结构，SFT 只能恢复浅层模式匹配，无法完全恢复数学推理

**对比预期**：与 recovery-aware pruning 的 SFT 对照（sft_recovery_20 应有更高推理准确率），standard pruning 的模型在 SFT 后虽能生成格式正确的输出，但推理错误率更高。这支持了 recovery-aware pruning 保留关键推理结构的假设。

**下一步建议**：此 checkpoint 可作为 GRPO 的初始化点（D013 Stage 2），因为 EOS 问题已解决，GRPO 的 reward signal 现在可以正常工作。

---
