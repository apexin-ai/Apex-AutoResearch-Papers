# ssh exp2 analysis prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp2-analysis-prep_20260514T231253_result.json`
- **Structured JSON:** [`835ab9d5470e1a8c54eb.json`](../../sessions/83/835ab9d5470e1a8c54eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完毕，汇报如下。

---

## 预审报告

### 1. 分析代码 (`analyze_results.py`) — 基本完备，有一处缺失

**正确的部分：**
- ΔF1 = `solo_f1[t] - batch_f1[t]` 逐类型取均值，正值=退化 ✅
- solo_f1 来自 exp1 `count_1` 的 `per_type_f1` ✅
- `scipy.stats.pearsonr(bcs_vals, y_vals)` ✅
- 按 `count_key` 分组分别分析 count_6 和 count_12 ✅
- Pass/fail 判据：`|r| ≥ 0.3 and p < 0.05` ✅
- t-test 将 25 个 random batch 按 BCS 三等分，取首尾做 `ttest_ind` ✅
- Cohen's d 用 low/high BCS batch 的 y 值差除以 random 的 pooled std ✅
- scatter plot + regression line + color-coded low/high/random ✅

**缺失项：**
- **无 Mann-Whitney U 检验**。t-test 分组只有 ~8 个样本/组，正态性假设可能不成立。任务要求中提到了 Mann-Whitney U，但代码只有 t-test。

### 2. Exp2 Batch 设计 — 正确

- **54 batches 确认**：count_6 × (1 low + 1 high + 25 random) + count_12 × (1 low + 1 high + 25 random) = 54 ✅
- **BCS 计算用 Qwen3 embeddings** (`data/type_embeddings.pt`，684KB)。`compute_type_embeddings.py` 使用 `AutoModelForCausalLM` mean-pooled hidden states，不是 E5 ✅
- **Random seed 固定**：`seed=42 + count`（count_6 用 48，count_12 用 54），via `random.Random(seed).sample()`，可复现 ✅
- **Greedy selection**：low_bcs 从最不相似的 pair 开始贪心添加；high_bcs 从最相似的 pair 开始。逻辑正确 ✅

### 3. Exp2 输出格式

exp2 完成后会产生：
- `artifacts/predictions_exp2.json` — list of dicts，每条含 `sample_id`, `batch_id`, `count_key`, `batch_types`, `batch_bcs`, `predictions`
- `artifacts/eval_exp2.json` — dict，key 格式如 `count_6_low_bcs`, `count_6_random_0`, ..., `count_12_high_bcs`

每个 batch 的 eval 包含：`exact` {p, r, f1, tp, total_pred, total_gold}, `relaxed` {同}, `bcs`, `count_key`, `num_types`, `num_samples`, `per_type_f1`

格式与 `analyze_results.py` 的输入完全兼容。

### 4. Solo Baseline 数据

- eval_exp1.json 有 **64 个 count_1 batch**（`count_1_random_0` ~ `count_1_random_63`），对应 64 个 active types
- 每个 batch 有 `per_type_f1`，只含 1 个 type
- `analyze_results.py` 的 `main()` 会自动从 count_1 提取 solo_f1 dict

### 5. 🔴 关键问题：evaluate.py 的 offset 语义错配

**这是 exp1 F1 反转的根因，也会影响 exp2 分析。**

证据：
- `count_1_random_0`（单类型 "art-broadcastprogram"）：total_pred=172, total_gold=22, exact TP=2, exact F1=0.021
- 同一 batch relaxed TP=10, relaxed F1=0.103（recall 从 9% 跳到 45%）
- 大量 solo 类型 exact F1=0.0（tail 显示大部分 per_type_f1 是 0.0）

**机制分析：**
1. `build_prompt()` 要求模型输出 `start` 和 `end`，但**未指定是字符偏移还是词索引**
2. Gold 数据（`few_nerd_utils._tokens_to_spans`）使用**字符偏移**
3. LLM 很可能输出**词索引**（token index），导致 `_exact_match` 几乎全部失败
4. `_relaxed_match` 只要求 type 匹配 + span 有重叠，词索引碰巧与字符偏移有交集时就能匹配
5. `diagnose_eval.py` PART 3 专门检测这一问题（检查 `text[start:end] == pred_text` 和 token index 模式），但**尚未运行**

**对 exp2 分析的影响：**
- solo_F1 ≈ 0，batch_F1 ≈ 0 → ΔF1 ≈ 0 + noise
- BCS vs ΔF1 的 Pearson r 将由噪声驱动，很可能 FAIL
- 这不是假设被证伪，而是**测量工具坏了**

### 6. 建议的后续操作

**Step 1**：先运行 `diagnose_eval.py` 确认 offset 问题：
```bash
cd /root/schema-dag-extraction/src && python3 diagnose_eval.py 2>&1 | tee /root/schema-dag-extraction/artifacts/diagnose_output.txt
```

**Step 2**：如果确认 offset 是 token index，需要修复评估（两种方案）：
- **方案 A**：修改 `evaluate.py`，用 `pred["text"]` 在 gold text 中做文本匹配（`text.find(pred_text)`）重算 char offset
- **方案 B**：修改 `build_prompt()`，明确要求输出字符级偏移并给示例

**Step 3**（exp2 完成后）：如果 offset 问题已修复，分析命令：
```bash
cd /root/schema-dag-extraction/src && python3 analyze_results.py --results_dir ../artifacts --output_dir ../artifacts
```

**Step 4**：补加 Mann-Whitney U 检验（在 `analyze_results.py` 的 `analyze_exp2` 函数中 t-test 之后加 `stats.mannwhitneyu`）。

---
