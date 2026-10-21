# research lora config compare

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lora-config-compare_20260514T065408_result.json`
- **Structured JSON:** [`32d409be76e383e9d22f.json`](../../sessions/32/32d409be76e383e9d22f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。

## 对比表

```
Parameter       | 0.5B   | 1.5B   | 3B     | 一致?
----------------|--------|--------|--------|------
lora_r          | 16     | 16     | 16     | ✅
lora_alpha      | 32     | 32     | 32     | ✅
target_modules  | qkvoudg| qkvoudg| qkvoudg| ✅
lora_dropout    | 0.05   | 0.05   | 0.05   | ✅
learning_rate   | 2e-4   | 2e-4   | 2e-4   | ✅
batch_size      | 4      | 2      | 1      | ❌
grad_accum      | 4      | 8      | 16     | ❌
effective_bs    | 16     | 16     | 16     | ✅
num_epochs      | 1      | 1      | 1      | ✅
max_seq_length  | 2048   | 2048   | 2048   | ✅
seed            | 42     | 42     | 42     | ✅
num_samples     | 50000  | 50000  | 50000  | ✅
total_steps     | 3125   | 3125   | 3125   | ✅
warmup_ratio    | 0.05   | 0.05   | 0.05   | ✅
optimizer       | adamw  | adamw  | adamw  | ✅
scheduler       | cosine | cosine | cosine | ✅
modules_to_save | null   | null   | null   | ✅
use_dora        | false  | false  | false  | ✅
use_rslora      | false  | false  | false  | ✅
```

target_modules = {q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj}（三个 size 完全一致）

## 分析结论

1. **LoRA 超参完全一致。** 三个 size 用相同的 r=16, alpha=32, dropout=0.05, 相同的 7 个 target modules，相同的 lr=2e-4。batch_size 和 grad_accum 因显存调整但 effective batch size 保持 16，训练步数都是 3125。

2. **target_modules 不包含 lm_head 或 embed_tokens。** 只训了 attention + MLP 的投影层，没有动 embedding 和输出头。这排除了"3B 的 lm_head 被 LoRA 改坏"的可能。

3. **lr=2e-4 对 3B 不算偏大。** 因为 LoRA 可训参数占比随模型变大而降低（r=16 相对 3B 的参数量更稀疏），2e-4 在合理范围内。

4. **3B 生成倒挂的原因不在 LoRA 超参层面。** 需要从其他方向排查：合并(merge)过程是否出错、评估时的 generation config（temperature/top_p/max_tokens）、或 3B base model 本身在该数据分布下的 LoRA 适配效率。

---
