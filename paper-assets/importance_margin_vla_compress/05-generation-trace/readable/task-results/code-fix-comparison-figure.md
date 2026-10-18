# code fix comparison figure

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_comparison_figure_20260524T164422_result.json`
- **Structured JSON:** [`f63706bfec977f6860a6.json`](../../sessions/f6/f63706bfec977f6860a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。新的 comparison figure 已生成：

- **`fig_importance_comparison.pdf`** — 302 KB
- **`fig_importance_comparison.png`** — 267 KB

修改总结：
1. `keep_ratio` 从 0.50 → 0.85（函数默认值和 main 调用都已改）
2. HF_TOKEN 硬编码已移除，改为 `os.environ.setdefault("HF_TOKEN", os.environ.get("HF_TOKEN", ""))`
3. 添加了 `--only_comparison` 参数，只生成 comparison figure 跳过 heatmap 和 histogram
4. 图标题自动更新为 `L2-Norm (k=0.85)` 和 `Random (k=0.85)`（由 f-string 动态生成）

---
