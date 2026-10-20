# eval deepseek maxlen fix verification

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek_maxlen_fix_verification_20260516T021135_result.json`
- **Structured JSON:** [`14593436ccefb0b4332a.json`](../../sessions/14/14593436ccefb0b4332a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**VOTA max_length=16384: Accuracy = 84.5%** — 精确恢复！确认了根因分析。

---

## 汇报

### 任务 1: full_trace v3 with max_length=2048

| 指标 | 重跑值 | 原始值 | 匹配？ |
|------|--------|--------|--------|
| accuracy | **79.16%** | 79.16% | ✅ 精确匹配 |
| fail_f1 | 0.637 | — | — |
| pass_f1 | 0.854 | — | — |

**结论**: max_length=16384 确认是根因。batch re-eval 用 `--max_length 16384` 导致 accuracy 从 79.16% 暴跌至 28.49%（100% 预测 fail）。用 max_length=2048 重跑完全恢复。

结果文件：`eval_results_maxlen2048.json`

### 任务 2: VOTA with max_length=2048

| 指标 | max_length=2048 | max_length=16384 | 原始值 |
|------|-----------------|------------------|--------|
| accuracy | **16.0%** ❌ | **84.5%** ✅ | 84.45% |
| fail_f1 | 0.61 | 0.62 | 0.62 |
| pass_f1 | 0.07 | 0.90 | 0.90 |

**结论**: VOTA 的问题**不是 max_length 不匹配**，而是 evaluate.py 的前截断 bug。

根因链：
1. evaluate.py 新增截断代码（commit `0836dd4`），对长输入取 `input_ids[:content_budget]`（前截断）
2. VOTA pass 样本有巨大的 execution trace（>2048 tokens），截断后末尾的 `"Does this code pass all tests? Answer: "` 被删除
3. 模型看不到 "Answer: " 提示，输出垃圾（"ver", "this", "import" 等 — 截断位置的下一个 token）
4. 训练时的 eval 用旧版 evaluate.py（无截断），模型能看到完整输入 → 84.5%

修复方案：VOTA eval 应使用 max_length=16384（DeepSeek 原生支持），或修改截断逻辑保留末尾 "Answer: " 提示。

### 任务 3: DeepSeek 实验 eval 审查表

| 实验 | 当前 eval accuracy | 训练时 eval | 状态 | 说明 |
|------|-------------------|------------|------|------|
| deepseek_exception_only | 99.33% | 99.3% | ✅ 一致 | 输入短，不受截断影响 |
| deepseek_exception_only_seed123 | 91.09% | 91.1% | ✅ 一致 | 同上 |
| deepseek_exception_only_seed456 | 99.33% | — | ✅ 正常 | 同上 |
| deepseek_no_trace | 73.36% | 73.4% | ✅ 一致 | 无 trace，输入短 |
| **deepseek_vota** | **15.97%** | **84.5%** | **❌ 被 truncation bug 破坏** | 需用 max_length=16384 |
| deepseek_full_trace | 28.49% | 28.5% | ✅ 一致 | 训练本身就差（v1） |
| deepseek_full_trace_v2 | N/A | — | ⚠️ 无数据 | final/ 下无 eval_results |
| **deepseek_full_trace_seed42_v3** | **28.49% → 79.16%** | — | **✅ 已修复** | batch re-eval 用了 max_length=16384 |

**总结**：
- 被破坏的只有 2 个实验：`full_trace_seed42_v3`（已修复）和 `vota`（需用 max_length=16384）
- exception_only（3 个 seed）和 no_trace 全部正确，因为输入短不触发截断
- `deepseek_full_trace`（无后缀）的 28.5% 是训练本身的结果，不是 eval 问题

---
