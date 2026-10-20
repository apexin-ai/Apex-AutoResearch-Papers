# code c10 s020 s025 gen

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c10_s020_s025_gen_20260516T033701_result.json`
- **Structured JSON:** [`68c474f01d799fafd210.json`](../../sessions/68/68c474f01d799fafd210.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载，s020 第 1 题正在生成。

任务已提交到 cuda:1，tmux session `c10_lang_s020_s025`：
- 串行跑 importance_s020（50 题）→ importance_s025（50 题）
- max_new_tokens=8192，保存完整 generated_text
- 输出：`results_c10_s020_fulltext.json` / `results_c10_s025_fulltext.json`
- 生成完成后自动运行 language switching 汇总（合并 dense/s015/s020/s025/s030）
- 预估时长：每题 ~30-180s（取决于生成长度），两个条件共 100 题约 2-4 小时
- 日志：`~/runs/phase-gated-compound-sparse/c10_lang_s020_s025.log`

---
