# code exp006 fixes

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_fixes_20260513T081337_result.json`
- **Structured JSON:** [`42ab41ad6046c02f6bd1.json`](../../sessions/42/42ab41ad6046c02f6bd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部通过 dry-run 验证。

---

### 修改汇总

**`scripts/run_exp006.sh`**
- 在 strategy loop 之前插入 base model baseline 评估块：无 adapter，调用 `exp006_evaluate.py --model-name "$MODEL" --output "$BASE_RESULT" --cache-dir "$CACHE_DIR"`，结果写入 `outputs/exp006/base_model/eval_results.json`，有 skip 机制

**`scripts/exp006_filtering_strategies.py`** — BinaryDrayson 类
- `b`: 1.5 → **1**（Drayson 2025 Table S1, SmolLM-1.7B）
- 新增 `rmax=3` 参数
- `get_weights()` 和 `get_mask()` 中加入 `raw = np.minimum(raw, self.rmax * mean_w)` 截断
- docstring 注明参数来源（arXiv:2502.15654 Table S1）

**`scripts/exp006_analyze.py`**
- 加载 `base_model/eval_results.json` 作为 "base (no training)" 行
- 表格首行显示 base model 分数
- 新增 "One-sample t-tests vs base model" 段（因 base 无多 seed，用 `ttest_1samp` 替代 paired）
- 末尾输出 data source 说明

---
