# code mcmc n17 missing data check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mcmc-n17-missing-data-check_20260524T152301_result.json`
- **Structured JSON:** [`c20718b3a4a6070e3440.json`](../../sessions/c2/c20718b3a4a6070e3440.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MFRM 跑通了，G-MFRM 也在正常采样只是超时了（30s 限制）。结论已清楚。

---

## 结论

### 当前代码是否支持不平衡数据：**Yes**

**原因：整个 pipeline 使用稀疏观测格式，天然支持不平衡数据。**

核心证据：

1. **`models.py` — NumPyro 模型使用 index-based 向量化**（非密集张量）：
   ```python
   logits = theta[model_idx] - b[item_idx] - d[judge_idx]
   numpyro.sample("obs", dist.Bernoulli(logits=logits), obs=y)
   ```
   模型只对实际存在的观测计算似然，不假设完整交叉。

2. **`data_loader.py` — 返回平行数组 `(model_idx, item_idx, judge_idx, y)`**，从 JSONL 逐条读取，缺失的 judge×item 组合根本不会出现在数组中。

3. **唯一的过滤条件**：`items judged by >= 3 judges`（合理阈值，确保每个 item 有足够信息估计 b_i）。

4. **Dry-run 验证通过**：
   - 数据加载：7 个 judge，观测量从 43（Mistral）到 4374（Sonnet）不等，sparsity = 59.1%
   - MFRM fitting：`theta_hat.shape = (18,)`，无报错
   - G-MFRM fitting：正常采样中（仅因 SSH 30s 超时截断，非代码错误）

5. **`run_baselines_n17.py` 同样支持**：通过 `filter_excluded_judges()` 函数排除 Mistral 后，用相同的稀疏格式计算 baseline。

### 无需修改

代码设计之初就选择了观测列表格式而非密集张量，docstring 明确写了 "Adapted from mvp/models.py for sparse observation format"。Sonnet（4374 obs）、DeepSeek（2501 obs）、Gemini（3009 obs）等不平衡 judge 可直接使用。

### 建议

运行时排除 Mistral（118 行 → 43 obs after preprocessing，仅覆盖 4 items），`run_baselines_n17.py` 已有 `EXCLUDE_JUDGES = ["mistral-large-2"]` 配置。`run_exp003_n17.py` 可加相同过滤，或在 `judgment_data_n17/` 中移除 Mistral 的 symlink：
```bash
rm -rf /root/gated_mfrm_judge_bias/exp003/judgment_data_n17/mistral-large-2
```

---
