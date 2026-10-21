# code d157 eval prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d157-eval-prep_20260520T154920_result.json`
- **Structured JSON:** [`af491675f5f2ea280fdb.json`](../../sessions/af/af491675f5f2ea280fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出：

1. **`scripts/analyze_d157.py`** — 分析脚本，接受 3 个 classify_h7 JSON 文件，输出：
   - Per-seed breakdown table
   - Mean ± std 聚合
   - 与 ISR/Random/Exec-only 的对比表（baselines 硬编码自 registry）
   - Fisher exact test（pooled genuine 比例）
   - Markdown 报告保存到 `artifacts/d157_shuffled_isr_analysis.md`

2. **`artifacts/d157_eval_commands.md`** — 完整的 eval/classify/analyze 命令 + baseline 数据表

关键发现：
- D157 使用 β=0.1（从 reward_log.jsonl 确认 `beta_t: 0.1`）
- 目前只有 s42 在训练（checkpoint-300），s43/s44 尚未启动
- ISR β=0.1 baselines 无 s42/s43/s44 数据，使用 d134 系列 s47-s51（同为 Qwen3-4B, 500 steps）
- classify_h7.py 参数是 `--eval_path` + `--json_out`（不是 `--input`/`--output`）

---
