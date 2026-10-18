# ops kivi eval param audit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kivi_eval_param_audit_20260515T115659_result.json`
- **Structured JSON:** [`8399b44101cee856ba31.json`](../../sessions/83/8399b44101cee856ba31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在全部信息已收集完毕。以下是审计报告。

---

## 审计结果

### 1. 关键发现：KIVI eval 没有 baseline 运行

KIVI eval 脚本 (`run_kivi_baseline.py`) **不评估 unquantized baseline**。它只运行 KIVI-2bit 和 KIVI-4bit。日志和 JSON 结果文件中均无 baseline PPL 数字。

已有的 KIVI 结果：
| 模型 | KIVI-2bit (r128) | KIVI-4bit (r128) | KIVI-2bit (r0) | KIVI-4bit (r0) |
|------|-----------------|-----------------|---------------|---------------|
| Qwen2.5-7B | 12.83 | 9.90 | 13.34 | 9.91 |
| Llama-3.1-8B | 9.84 | 8.14 | 10.08 | 8.14 |

**"KIVI baseline ≈ 9.19" 这个数字在服务器上所有 artifacts/logs 中均未找到。** 可能来自口误或未保存的临时运行。

### 2. 两个 pipeline 的 evaluate_perplexity 函数完全一致

`run_kivi_baseline.py` 的 `evaluate_perplexity` 与 `eval_ppl.py` 的 `evaluate_perplexity` 是同一套代码逻辑：

| 参数 | KIVI eval | Paper pipeline (eval_ppl.py) |
|------|-----------|------------------------------|
| **stride** | 512（默认） | 512（默认） |
| **max_length** | 无限制（处理全文） | 无限制（处理全文） |
| **prepend_bos** | tokenizer 默认行为 | tokenizer 默认行为 |
| **test_set** | WikiText-2 test (HF/arrow) | WikiText-2 test (HF/arrow) |
| **text_preprocessing** | `"\n\n".join(非空行)` | `"\n\n".join(非空行)` |
| **tokenization** | `tokenizer(text, return_tensors="pt")` | 同左 |
| **loss_calculation** | `cross_entropy(sum)` → `exp(total/N)` | 同左 |
| **context** | 非重叠 512-token chunks | 同左 |

**baseline 评估应产生完全相同的数字。** 论文 Qwen baseline = 9.8106，如果用 KIVI eval 的 `evaluate_perplexity` 跑 unquantized Qwen，也应该得到 9.81。

### 3. 真正的差异：量化方案

两个 pipeline 的 **量化实现** 完全不同：

| 参数 | KIVI eval | Paper pipeline (utils.py) |
|------|-----------|---------------------------|
| **K 量化类型** | **非对称** min-max | **对称** abs_max |
| **V 量化类型** | **非对称** min-max | **对称** abs_max |
| **K 分组** | 沿 token dim 分组，group_size=32 | 无分组（整列一个 scale） |
| **V 分组** | 沿 head_dim 分组，group_size=32 | 无分组（整行一个 scale） |
| **residual** | 最后 128 token 保持 fp16 | 无 residual 机制 |
| **粒度** | 全层统一 bit-width | 每头独立 bit-width |

### 4. 论文 baseline 数字来源确认

| 模型 | 论文 baseline | 来源文件 |
|------|-------------|---------|
| Qwen2.5-7B | 9.81 | `qwen_hires_results.json` (`wikitext2_baseline_ppl: 9.8106`) |
| Llama-3.1-8B | 8.09 | `w2_unconstrained_v2_results.json` (`baseline_wt2_ppl: 8.0922`) |
| Yi-1.5-9B | 7.02 | 同上 (`baseline_wt2_ppl: 7.0157`) |
| Mistral-7B | 7.04 | 同上 (`baseline_wt2_ppl: 7.0352`) |

### 5. 结论

1. **两个 pipeline 的 baseline 评估代码一致**，不应产生不同的 baseline PPL。如果有差异，问题在运行环境（模型权重路径、tokenizer 版本等），而非代码。
2. **KIVI eval 缺少 baseline 运行** — 需要补跑一次 unquantized baseline 来验证。
3. **量化方案差异显著**（对称 vs 非对称、有无分组、有无 residual），会导致量化后 PPL 不同。这是设计差异，不是 bug。
4. **不需要用统一 pipeline 重跑** — 前提是确认 KIVI baseline 确实等于论文 baseline（~9.81）。建议在 KIVI 脚本中加一次 unquantized baseline eval 来验证。
5. **补跑 baseline 估算 GPU 时间**：Qwen2.5-7B WikiText-2 eval 约 5-8 分钟（583 chunks，每 chunk 一次 forward pass）。

---
