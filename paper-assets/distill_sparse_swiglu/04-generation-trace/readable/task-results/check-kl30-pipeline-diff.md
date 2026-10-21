# check kl30 pipeline diff

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_kl30_pipeline_diff_20260517T115421_result.json`
- **Structured JSON:** [`4f3fccef5823513617ca.json`](../../sessions/4f/4f3fccef5823513617ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。以下是完整结论。

---

## 排查结果

### 训练配置对比

| 参数 | s42 (kl_sparsity30_s42_v3) | s123 (kl_30pct_s123) | 是否一致 |
|------|---------------------------|---------------------|----------|
| **lambda_max** | **5000.0** | **5000** | **✓ 一致** |
| lr | 0.001 | 1e-3 | ✓ |
| num_steps | 1000 | 1000 | ✓ |
| batch_size | 4 | 4 | ✓ |
| seq_len | 2048 | 2048 | ✓ |
| sparsity_target | 0.3 | 0.3 | ✓ |
| loss_type | kl_normalized | kl_normalized | ✓ |
| dataset | wikitext-103 | wikitext-103 | ✓ |
| gradient_checkpointing | True | True | ✓ |
| seed | 42 | 123 | 预期不同 |

**来源**：s42 v3 配置来自 wandb 离线记录 `offline-run-20260516_051217-06u4phga`，s123 配置来自 `scripts/multiseed_kl30_fixed.sh`。

### Eval 配置对比

| 参数 | s42 (bench_kl30_global) | s123 (kl_30pct_s123) | 一致 |
|------|------------------------|---------------------|------|
| sparsity_mode | teal_global | teal_global | ✓ |
| allocation | global_topk | global_topk | ✓ |
| sparsity_target | 0.3 | 0.3 | ✓ |
| batch_size | 8 | 8 | ✓ |
| seq_len | 2048 | 2048 | ✓ |
| few_shot | 未记录（lm-eval-harness 默认） | 未记录（同上） | ✓ |

### Benchmark 结果对比

| 指标 | s42 | s123 | 差异 |
|------|-----|------|------|
| wikitext2_ppl | **8.9768** | **8.9748** | ≈0 (几乎相同) |
| ARC (acc) | 37.20% | 41.81% | -4.6pp |
| ARC (acc_norm) | 39.68% | 45.31% | -5.6pp |
| WinoGrande | 70.17% | 69.30% | +0.9pp |
| **MMLU** | **25.27%** | **38.07%** | **-12.8pp** |
| GSM8K | 8.79% | 7.58% | +1.2pp |

### 关于 kl_sparsity30_s42.log 的误导

`kl_sparsity30_s42.log` 显示 `cap=1000`，但这是 **v1 训练的日志**（wandb run `gxgzh438`，产出 `kl_sparsity30_s42` checkpoint）。论文引用的 v3 checkpoint 是 **后续重新训练**的，wandb 记录明确显示 `lambda_max: 5000.0`。v3 的训练日志未被单独保存为 .log 文件。

### 结论

**差异是纯种子方差，不是配置差异。**

训练配置完全一致（包括 lambda_max=5000）。但 MMLU 的 12.8pp 种子方差异常大，而 perplexity 几乎完全相同（8.977 vs 8.975），WinoGrande/GSM8K 也在噪声范围内。

这说明 **30% global_topk 下 MMLU 对 sparsity pattern 极度敏感**：不同 seed 导致不同神经元被保留，perplexity 不受影响但 MMLU 崩塌。这实际上 **强化了 uniform allocation 的论点**（uniform 提供更稳定的性能），但论文的 framing 需要调整：

1. 不能用单个 s42 的 25.27% 作为 global_topk 的代表性结果（它可能只是 unlucky seed）
2. "+15.3pp recovery" 的 claim 混入了 seed 方差，实际 uniform 的增量可能没那么大
3. 建议：报告 s42/s123 的 MMLU 均值和标准差，或说明 global_topk 在 30% 下 MMLU 方差很大，这本身就是 uniform 的卖点

---
