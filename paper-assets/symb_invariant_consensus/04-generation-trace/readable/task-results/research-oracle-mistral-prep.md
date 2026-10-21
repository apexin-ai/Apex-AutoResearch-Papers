# research oracle mistral prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_oracle-mistral-prep_20260520T132540_result.json`
- **Structured JSON:** [`f6e96884b5efd3068c5f.json`](../../sessions/f6/f6e96884b5efd3068c5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是方案：

## 调研结果

### 已有 oracle 脚本
`scripts/run_exp031_oracle_folio_regen.py` — Qwen2.5-14B 的 gold FOL oracle SICA 实验，结果：
- Oracle SICA = **89.71%**, SC = 75.49%, delta = **+14.22pp** (p < 1e-7)
- CPU-only (Z3 solver)，用时 0.7s

### Mistral-7B traces
`results/exp033_mistral_7b_folio204/intermediates/folio_{0..203}.json` — 204 个 trace 文件，格式与 Qwen 完全相同：
```json
{
  "problem": {"id": "folio_0", "premises_fol": [...], "conclusion_fol": "...", "answer": "..."},
  "sica_result": {"answer": "...", "traces": [{...}, ...], "scores": {...}}
}
```
Gold FOL 已嵌入每个 trace 的 problem 字段。

### FOLIO gold data
`data/folio_full.json` — 204 条，字段 `premises_fol` / `conclusion_fol` / `answer`。

### exp-050 ≠ 本任务
exp-050 是 ICL oracle（给 extraction prompt 加 few-shot gold 例子改善约束提取），不是 gold FOL 替换 oracle。且已失败。

---

## 实验方案

**直接复用 exp-031 脚本**，仅改 3 处硬编码：

| 参数 | 原值 (Qwen) | 新值 (Mistral) |
|------|------------|---------------|
| `traces_dir` | `results/folio_204_14b/intermediates` | `results/exp033_mistral_7b_folio204/intermediates` |
| `output_dir` | `results/oracle_folio_regen` | `results/oracle_folio_mistral7b` |
| `model` 元数据 | `Qwen2.5-14B-Instruct` | `Mistral-7B-Instruct-v0.3` |

- **脚本路径**：复制为 `scripts/run_exp089_oracle_folio_mistral7b.py`（新 exp 编号）
- **运行命令**：`cd /root/symb_invariant_consensus && python3 scripts/run_exp089_oracle_folio_mistral7b.py`
- **运行服务器**：westd-25068（Mistral traces 在这，CPU-only 不需 GPU）
- **预计耗时**：< 2 秒
- **预期输出**：`results/oracle_folio_mistral7b/exp089_results.json` + `exp089_summary.json`，包含 Mistral-7B oracle SICA accuracy / SC / delta / McNemar p-value

需要现在写脚本部署吗？

---
