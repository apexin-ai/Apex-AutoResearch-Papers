# analysis lambda max confirm

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lambda-max-confirm_20260516T222039_result.json`
- **Structured JSON:** [`6dbbd50d306f6f515058.json`](../../sessions/6d/6dbbd50d306f6f515058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All evidence collected. Here are the results:

---

## 结论

### 1. kl_30pct_s42 的 λ_max = **5000**

**直接证据**：wandb offline run `offline-run-20260516_051217-06u4phga` 的 debug.log 中记录的 init config：
```
'lambda_max': 5000.0, 'sparsity_target': 0.3
```
对应的是 `kl_sparsity30_s42_v3` 运行（output_dir = `checkpoints/kl_sparsity30_s42_v3`）。

注意：logs/ 下的 `kl_sparsity30_s42.log` 显示 `cap=1000`，但那是更早一次运行（wandb run `gxgzh438`，时间 04:26:21），不是最终采用的 v3 版本（wandb run `06u4phga`，时间 05:12:17）。

### 2. kl_40pct_s42 的 λ_max = **5000**

**直接证据**：wandb offline run `offline-run-20260516_150200-51pvb0hh` 的 debug.log 中记录的 init config：
```
'lambda_max': 5000.0, 'sparsity_target': 0.4
```

### 3. λ 的最大观测值

从 `lambda_sparsity_curves.json` 中：
- **kl_30pct_s42**：λ 大量 step 达到了 **5000**（lambda 数组 lines 371-445 全是 5000），confirmed 触顶 cap
- **kl_40pct_s42**：λ 大量 step 达到了 **5000**（lambda 数组 lines 1144-1208 全是 5000），confirmed 触顶 cap
- 对比：kl_50pct_s42 的 lambda_max=1000，kl_70pct_s42 的 lambda_max=1000

### 4. 证据类型

**有直接证据**：两个 run 的 wandb debug.log 中均明确记录了 `lambda_max: 5000.0` 作为 wandb.init 传入的 config 参数。lambda 观测值达到 5000 也与此一致。

---
