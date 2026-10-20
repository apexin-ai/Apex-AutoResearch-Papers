# analysis exp062 final 16of16

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp062-final-16of16_20260521T212031_result.json`
- **Structured JSON:** [`286ddf8483ffdc676799.json`](../../sessions/28/286ddf8483ffdc676799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

残留的 XX 全部在 `\iffalse` 包裹的 VERSION A 和 VERSION B 中（不活跃的备选方案），不影响编译输出。Version C（活跃版本）已无 XX。

---

**汇报：**

1. **Chain 完整性**：4539 行（>4500 阈值）✓
2. **Features 记录数**：4539 条（完整重新提取）✓
3. **Cohen's d + DDR 判定**：

| Feature | d | 分类 |
|---------|---:|------|
| entropy_max | 0.05 | shape (✓) |
| entropy_min | 0.07 | shape (✓) |
| tail_decay | 0.17 | shape (✓) |
| entropy_mean | 0.76 | drift |
| ttr | 0.68 | drift |
| hapax_ratio | 0.64 | drift |
| entropy_std | 0.27 | boundary |

**DDR = YES**（shape features 全部 d < 0.20）

4. **Appendix 更新**：
   - Shape table Qwen3-8B topk: 0.05 / 0.07 / 0.17
   - Drift table Qwen3-8B topk: 0.76 / 0.68 / 0.64 / 0.27
   - Mean 行：7/8 → 8/8，数值更新（ttr 0.62→0.63, entropy_std 0.22→0.23）
   - Version C conclusion：greedy shape mean |d|=0.05, max 0.14; drift mean 0.91; topk 4/8 elevated; shape 0.10 vs 0.08; drift 0.56 vs 0.79

5. **双向同步**：`diff` 确认两份文件完全一致 ✓

---
