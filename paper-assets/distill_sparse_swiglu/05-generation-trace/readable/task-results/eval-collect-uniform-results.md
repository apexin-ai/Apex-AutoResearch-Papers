# eval collect uniform results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_uniform_results_20260517T235026_result.json`
- **Structured JSON:** [`e5480271c9e7d3d5e2fc.json`](../../sessions/e5/e5480271c9e7d3d5e2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态：

```
TEAL uniform 状态: 进行中
- GSM8K generate_until: 81/1319 (6%), 已运行 20:57, 剩余 ~5h15m (~15.3s/it)
- wikitext2_ppl: 不可读（日志损坏）
- arc_challenge_acc_norm: 不可读
- winogrande_acc: 不可读
- mmlu_acc: 不可读
- gsm8k_exact_match: 未完成
- per_layer_sparsity: 不可读

KL uniform 状态: 进行中
- GSM8K generate_until: 137/1319 (10%), 已运行 29:50, 剩余 ~4h55m (~15.0s/it)
- 同上，所有中间指标不可读
```

**问题说明：** 两个日志文件都存在 null 字节损坏。初始错误（`/root/autodl-tmp/models/Qwen2.5-14B` 路径大小写导致的 `OSError`）之后，第二次启动的 stdout（含 PPL、mask stats、Mode 等 print 输出）被 48KB-254KB 的 null 字节覆盖。当前可见的只有 progress bar。

结果 JSON 仅在全部 5 个 task 完成后才写入，没有中间产物。

**预计完成时间：** 两个实验都还需要 ~5 小时（GSM8K 14B 单卡 generate 极慢，1319 samples * ~15s/sample）。

---
