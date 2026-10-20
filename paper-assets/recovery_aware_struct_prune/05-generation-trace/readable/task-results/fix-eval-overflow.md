# fix eval overflow

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-overflow_20260514T081131_result.json`
- **Structured JSON:** [`90b2ae3a2c542eacd3b3.json`](../../sessions/90/90b2ae3a2c542eacd3b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**READY**

修复已完成并验证通过。

### 修改内容 (`/root/recovery_aware_struct_prune/src/eval_gsm8k.py`)

1. **添加 `import math`**
2. **`normalize_answer()`** — 返回类型改为 `str | None`：
   - 空字符串 → `None`
   - `math.isfinite(val)` 检查：inf/nan → `None`（修复 OverflowError）
3. **`extract_gold_answer()`** — 处理 `normalize_answer()` 返回 `None` 的情况，回退到原始字符串
4. **`evaluate()` 中的比较** — `norm_pred is not None and norm_pred == gold`，None 直接标记为答错

### 验证结果

- pruned_standard_35 模型，20 个样本，全部完成，0 crash
- 0% accuracy（剪枝模型质量差，符合预期）
- test_eval.json 已删除

### 注意

服务器上有一个 tmux session `mvp_rasp_pipeline_v2` 在 16:12 启动（patch 之前），运行的是**旧代码**的 eval。这些进程（PID 170786/170787）仍在运行，可能还会遇到 OverflowError。Main Agent 重新 submit 时需要用修复后的代码。

---
