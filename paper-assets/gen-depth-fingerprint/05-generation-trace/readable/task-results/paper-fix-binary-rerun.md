# paper fix binary rerun

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-binary-rerun_20260522T133004_result.json`
- **Structured JSON:** [`554daf53b162331cb19b.json`](../../sessions/55/554daf53b162331cb19b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。结果：

**C_all7 binary F1 = 0.7002**，接近论文的 ~0.694 leak-free binary F1（合理范围内，微小差异来自 downsample 随机性）。

关键改动（`run_logo` L38-44）：
- 删除了错误的 `df["label_bin"] = (df["depth"] >= 1).astype(int)`（gen-0 vs gen-1+）
- 改为在 LOGO 每轮中分别对 train/test 过滤 depth=0，然后定义 `label_bin = (depth >= 2)`（gen-1 vs gen-2+）

两个 JSON 结果文件已更新。

---
