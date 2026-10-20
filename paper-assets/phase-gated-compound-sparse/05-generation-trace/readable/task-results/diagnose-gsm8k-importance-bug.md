# diagnose gsm8k importance bug

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsm8k_importance_bug_20260515T170857_result.json`
- **Structured JSON:** [`1e1a4ce36785b044ccb6.json`](../../sessions/1e/1e1a4ce36785b044ccb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册（`art_20260515_239db4`）。

**诊断结论**：

- **Bug A（ii_low=0.0）**：仅出现在 `analysis_output/gsm8k/` 的合并结果中，是独立运行产生的。各 per-sparsity 结果文件（`profiling_output_gsm8k_ds_imp_s0{15,20,25,30}/`）中 ii_low **非零且正确**。
- **Bug B（PPL=NaN）**：fp16 下 layer 27 attention logits 溢出 → NaN 传播，`compute_perplexity` 缺少 NaN 过滤，`np.mean` 进一步传播。
- **额外发现**：bootstrap 解包 bug（dict→3 变量会 crash）。

**4 个修复**（按优先级）：
1. `compute_perplexity` 加 NaN/inf 过滤（Critical）
2. 聚合 PPL 用 `np.nanmean` 替换 `np.mean`（Critical）
3. Bootstrap 返回值改为 dict 取键（Critical）
4. GSM8K 切 bf16（Recommended）

---
