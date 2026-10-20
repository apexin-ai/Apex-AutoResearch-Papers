# ops diagnose cls seed123 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-cls-seed123-eval_20260513T204059_result.json`
- **Structured JSON:** [`70f0fc60ec38018c7db1.json`](../../sessions/70/70f0fc60ec38018c7db1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

```
trainer_state best_metric: 0.0808 (eval_loss, lower=better)
trainer_state best_checkpoint: checkpoint-200
现存 checkpoints: [200, 2600, 2800, 3000, 3200]
checkpoint-200 eval_loss: 0.0808 (最低)
actual best eval_loss: 0.0808 at step 200
最差 eval_loss: 0.358 at step 2400
adapter_config base_model: /root/.cache/huggingface/hub/Qwen/Qwen3-4B
adapter_config: task_type=CAUSAL_LM, r=16, lora_alpha=32
V5 checkpoint: 不在 westd 服务器上，无法对比

结论: checkpoint-200 确实是 best checkpoint（eval_loss 最低）
```

**核心问题不是 checkpoint 选错，而是训练本身严重过拟合。** eval_loss 从 step 200 的 0.08 一路飙升到 step 2400 的 0.36，模型在第一个 eval 点就达到了最佳，之后全是退化。

55% accuracy 就是 seed123 checkpoint-200 的真实水平。与 CLS v5 的 76.92% 差距 ~22 个点，可能原因：
- seed 123 的数据划分/shuffle 不利
- 训练过早就过拟合（200 step 就是 best，说明学习率可能过大或数据量不足）
- 缺少 step 200 之前的更细粒度 checkpoint（可能 step 100 或 step 50 更好）

**建议**: 让 eval 继续跑完拿最终数字作为记录，不需要 kill。但 seed123 的训练配置需要复查——learning rate、warmup、数据量是否与 v5 一致。

---
