# code d146 eval add baseline

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-eval-add-baseline_20260519T182107_result.json`
- **Structured JSON:** [`051147148405601d00d1.json`](../../sessions/05/051147148405601d00d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
1. Base model 路径：`/root/autodl-tmp/models/Qwen3-4B`
2. 脚本已修改：在 `EVAL_FILES=()` 之后、6 个实验循环之前插入了 Step 0，执行 base model 的 eval_sta.py + classify_h7.py，输出到 `$OUT/d146_pf_base/`，并将 eval 结果加入 `EVAL_FILES` 数组（纳入 batch summary）
3. `bash -n` 语法检查通过

---
