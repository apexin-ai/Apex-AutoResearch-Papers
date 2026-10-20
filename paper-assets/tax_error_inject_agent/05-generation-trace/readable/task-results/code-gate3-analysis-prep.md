# code gate3 analysis prep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gate3-analysis-prep_20260514T132847_result.json`
- **Structured JSON:** [`e15fc0d7dcfa77fedb3f.json`](../../sessions/e1/e15fc0d7dcfa77fedb3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全链路正常。自比结果符合预期：diff=0pp, p=1.0, Gate 3a FAIL。

脚本已就绪：`/root/autodl-tmp/tax_error_inject_agent/scripts/analyze_gate3.py`

使用方式：
```bash
python scripts/analyze_gate3.py \
  --vanilla  eval_results/v3_vanilla.json \
  --taxei    eval_results/v3_taxei.json \
  --random   eval_results/v3_random.json
```

功能：
- McNemar exact test（`scipy.stats.binomtest`，适合 n=47 小样本）
- Gate 3a/3b/4 自动判定，含 p-value 和 discordant pair 数
- Per-task-type breakdown
- 同时输出 human-readable 表格和 JSON（默认存 `eval_results/gate3_judgment.json`）

---
