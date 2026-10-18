# code fewrel 40rel incremental

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fewrel_40rel_incremental_20260515T163151_result.json`
- **Structured JSON:** [`38f7c213b258591e60bd.json`](../../sessions/38/38f7c213b258591e60bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Step 1 — Kill fewrel_40rel**: tmux session 和进程已终止。exp012_r4（LLaMA 8B）仍在正常运行。

**Step 2 — 增量保存修改**: 三处改动已应用，语法检查通过：
- L81: `run_re_extraction` 加了 `output_dir=None` 参数
- L149-155: 内层 batch 循环末尾加了 JSONL 增量保存（`results_incremental.jsonl`，append 模式）
- `stage_extract` 调用时传入 `output_dir=config["output_dir"]`

原有的最终一次性保存逻辑（`predictions_{mode}.json` + `eval_{mode}.json`）不受影响。重跑时即使中途挂掉，已完成 batch 的结果会保留在 `results_incremental.jsonl` 中。

---
