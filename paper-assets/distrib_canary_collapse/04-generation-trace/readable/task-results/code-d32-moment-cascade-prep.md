# code d32 moment cascade prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d32_moment_cascade_prep_20260520T165415_result.json`
- **Structured JSON:** [`4fd518fa1fb18c4f435f.json`](../../sessions/4f/4fd518fa1fb18c4f435f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

## Phase 1 Cascade 分析结果

### 关键发现

1. **`token_entropy` 几乎总是第一个偏离的 metric** — 18 个实验中 16 个以 `token_entropy` 作为 cascade 起点（onset gen=1），与假设一致

2. **Kendall τ = 0.337（13/18 正）** — 整体上支持 cascade 假设方向，但排序不完美：
   - `token_entropy` → 稳定排第 1
   - `distinct_n` 和 `effective_rank` 之间的顺序不够清晰，常被 `mauve`/`ece`/`self_bleu` 插入
   - `perplexity` 通常排最后（符合假设），但在高 α（0.75）时提前

3. **α 依赖模式**：
   - 低 α（0.00-0.10）：`token_entropy` → `mauve`/`ece` → `distinct_n`，cascade 较慢
   - 中 α（0.50）：最佳 τ=0.80，cascade 排序最接近假设
   - 高 α（0.75）：`perplexity` 提前 onset，cascade 更快更混乱
   - C4 数据集：τ 为负，`ece`/`perplexity` 先于 `token_entropy` onset

4. **数据缺口**：logit-level moments（var_log_p, kurtosis, tail_mass）缺失，中间代 checkpoint 未保存。建议在 T=20 实验中加入 moment 计算。

### 产出
- 脚本：`scripts/moment_cascade_analysis.py`（本地 + 服务器）
- JSON 结果：`results/analysis/moment_cascade_phase1.json`（服务器上）

---
