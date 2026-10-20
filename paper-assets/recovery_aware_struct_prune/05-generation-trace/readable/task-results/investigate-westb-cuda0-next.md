# investigate westb cuda0 next

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_westb_cuda0_next_20260520T154359_result.json`
- **Structured JSON:** [`72d1f419edc8c2d54e29.json`](../../sessions/72/72d1f419edc8c2d54e29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
CKA-only SFT 状态: epoch 1 完成 (checkpoint-935)，epoch 2 保存 checkpoint 时磁盘满崩溃 (No space left on device)
                   但 _final 目录已有完整模型 (~12.3GB)——训练跑完了 1870/1870 步，只是 checkpoint 保存失败
Standard SFT 状态: epoch 1 完成 (checkpoint-935)，epoch 2 同样磁盘满崩溃 (enforce fail at inline_container.cc)
                   _final 目录也有完整模型 (~12.3GB)——训练实际跑完，final 保存成功

cuda:0 占用: 空闲
cuda:1 占用: 空闲（eval_gsm8k_sft_qwen_standard_20 刚完成）

磁盘: 根分区 28% (22GB 可用)，数据盘 97% (9.8GB 可用) ⚠️

eval 结果:
  CKA-only  (checkpoint-935, epoch 1): GSM8K = 51.5% (103/200), eos_rate=0.27
  Standard  (checkpoint-935, epoch 1): GSM8K = 21.0% (42/200),  eos_rate 较低

可用 Qwen-Math checkpoint 清单:
  - pruned_cka_only_20_qwen_math          # 剪枝后未 SFT
  - pruned_standard_20_qwen_math          # 剪枝后未 SFT
  - sft_qwen_math_cka_only_20/checkpoint-935  # CKA-only SFT epoch 1
  - sft_qwen_math_cka_only_20_final          # CKA-only SFT 完整 2 epoch
  - sft_standard_20_qwen_math/checkpoint-935  # Standard SFT epoch 1
  - sft_standard_20_qwen_math_final           # Standard SFT 完整 2 epoch
  - cka_scores_qwen_math_7b.pt
  - importance_scores_qwen_math_7b.pt
```

**关键发现**: CKA-only 51.5% vs Standard 21.0%，CKA-only 大幅领先。但两者 eval 都只用了 checkpoint-935 (epoch 1)，还没评 `_final` (2 epoch) 模型。

**建议 cuda:0 下一步（按优先级）**:
1. **eval `_final` 模型** — 跑 `eval_gsm8k_sft_qwen_cka_only_20_final` 和 `eval_gsm8k_sft_qwen_standard_20_final`，看 epoch 2 是否有额外收益（数据盘 9.8GB 足够跑 eval）
2. **清理数据盘** — 97% 已经危险，可以考虑删除 checkpoint-935（已有 final 模型）释放空间

---
