# analysis exp016 data source audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp016_data_source_audit_20260514T230943_result.json`
- **Structured JSON:** [`6933a1a028bed60cf438.json`](../../sessions/69/6933a1a028bed60cf438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结论

**exp_016_signal_ensemble 的数据源是 exp_012（max_tokens=512），受截断影响。**

### 证据链

1. **代码逻辑** (`code/analyze_exp016_ensemble.py` 第 644-651 行)：
   - 优先加载 `exp_012_logprob/samples_with_logprobs.jsonl`（含 `mean_logprob` 字段）
   - 只有加载失败才 fallback 到 `pilot_004/samples.jsonl`
   - 实际运行时 exp_012 的文件存在且格式正确 → **使用的是 exp_012 数据**

2. **max_tokens 确认** (`code/extract_logprobs.py` 第 56、67 行)：
   ```python
   stoch_params = SamplingParams(n=8, temperature=1.0, max_tokens=512, ...)
   greedy_params = SamplingParams(n=1, temperature=0.0, max_tokens=512, ...)
   ```

3. **受影响的 Paper TODO 值**（全部来自 512-token 截断数据）：
   - Ensemble AUROC = 0.735 ± 0.0296（NER）
   - Best-of-N Selection F1 表格（Tab 2）
   - 所有 Part 1-4 的分析结果

### 补充信息

- `exp_016_v2` 和 `exp_012_rerun_1024` 已存在于服务器上，说明已有修正数据的尝试
- pilot_004 和 exp_012 都是 551 个实例，但 exp_012 额外包含 logprob 元数据，因此代码优先选择了它

**结论：Paper 中引用的 exp_016 数值全部基于 max_tokens=512 的推理数据，受截断影响，需要用 1024-token 数据重新计算。**

---
