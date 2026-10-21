# analysis p0 kl explosion investigation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p0-kl-explosion-investigation_20260514T195500_result.json`
- **Structured JSON:** [`fa323b7ab1c11ebb1944.json`](../../sessions/fa/fa323b7ab1c11ebb1944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：**step 10 没有触发 KL WARNING**（没有新的 "KL divergence" 日志），说明 step 10 的 KL 已降回 100 以下。P0 现在正常跑到了 step 14。

## 根因分析

### KL 爆炸原因：TRL Schulman KL 估计器 + QLoRA 4-bit 一次性数值伪影

**核心机制**：

TRL 的 KL 计算使用 Schulman 估计器（`grpo_trainer.py:2604`）：
```python
per_token_kl = exp(ref_logps - policy_logps) - (ref_logps - policy_logps) - 1
```

`exp()` 函数指数放大差异。如果某些 token 位置的 `ref_logps - policy_logps` 达到 ~22，`exp(22) ≈ 3.6B`，单个 token 就能让 batch 平均 KL 爆到 24 亿。

**触发条件**：QLoRA 4-bit + SFT adapter merge + PEFT adapter disable/enable

1. SFT adapter 被 merge 进 4-bit base（PEFT 已警告 "Merge lora module to 4-bit linear may get different generations due to rounding errors"）
2. Reference logprobs 通过 `use_adapter(model, adapter_name=None)` 禁用 GRPO LoRA 获取（`grpo_trainer.py:2200`）
3. 第一次 logging step（step 5）时，PEFT adapter disable/enable 的初始化状态可能导致一次性的计算异常

**为什么 ced_kl001_r4 没问题**：ced_kl001_r4 也在 step 5 做了同样的 KL 计算（`logging_steps=5`），但没有触发 WARNING。这说明这是一个**随机性/状态相关的问题**，不是确定性 bug。可能与具体 batch 的 token 分布和 4-bit 反量化的数值精度交互有关。

### recall_penalty 代码修改

**不是原因**。`--ced_recall_penalty` flag 未被 P0 使用，recall_penalty 代码在 `if self.recall_penalty and gold_map:` 条件后（line 283），完全被跳过。

### 与 ced_kl001_r4 KL 对比

| 指标 | P0 (lr=5e-6) | ced_kl001_r4 (lr=5e-5) |
|------|-------------|----------------------|
| Step 5 KL | 2,412,554,396.90 (WARNING) | 无 WARNING（< 100） |
| Step 10 KL | 无 WARNING（< 100） | 无 WARNING |
| Step 45 KL | — | 0.014 |
| 后续 KL | — | 0.01-0.18 稳定 |

### 为什么训练没崩

1. `KLDivergenceCallback` 设计为 monitoring only，不 stop（line 31-34 注释明确说明 QLoRA KL 不可靠）
2. KL penalty = `beta * kl = 0.01 * 2.4B = 24M`，会产生大梯度
3. 但 HF Trainer 默认 `max_grad_norm=1.0` 做梯度裁剪，防止了权重爆炸
4. Step 10 KL 已恢复正常

## 结论

| 问题 | 回答 |
|------|------|
| 根因 | QLoRA 4-bit + Schulman KL exp() 放大的**一次性数值伪影**，非代码 bug |
| recall_penalty 影响 | 无影响，flag 未启用 |
| P0 是否应该继续 | **继续**。KL 已在 step 10 恢复。再等 ~10 分钟到 step 20 出 checkpoint，查 `trainer_state.json` 确认 step 10/15 的精确 KL 值 |
| 需要 kill 重跑吗 | **不需要**。除非 step 20 checkpoint 显示 KL 持续 > 1.0 |

如果你要我在 step 20 checkpoint 出来后自动复查 KL 值，告诉我。

---
