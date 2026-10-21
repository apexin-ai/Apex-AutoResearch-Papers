# diagnose 14b fewnerd status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b_fewnerd_status_20260521T065839_result.json`
- **Structured JSON:** [`04be4a63886e28ef82af.json`](../../sessions/04/04be4a63886e28ef82af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**COMPLETED**

exp_14b_inference_fewnerd 的 N∈{1,2,4,8} 全部完成。PID 252310 已退出是因为任务正常结束，而非失败。Cron 是误报。

### 输出文件

| N | 路径 | 完成时间 | 文件大小 |
|---|------|---------|---------|
| 1 | `output/14b_final_inference/fewnerd_n1/` | May 21 00:58 | 170MB |
| 2 | `output/14b_final_inference/fewnerd_n2/` | May 21 04:09 | 244MB |
| 4 | `output/14b_final_inference/fewnerd_n4/` | May 21 08:31 | 398MB |
| 8 | `output/14b_final_inference/fewnerd_n8/` | May 21 14:55 | 700MB |

每个目录均包含 `samples.jsonl` + `report.json`，report 字段完整。

### 关键 Metrics 摘要

| N | greedy_F1 | oracle_F1 | oracle_headroom | soft_jaccard ρ (cond.) | structural_beats_surface | verdict |
|---|-----------|-----------|-----------------|------------------------|--------------------------|---------|
| 1 | 0.798 | 0.754 | -0.044 | NaN (trivial) | false | FAIL |
| 2 | 0.799 | 0.809 | +0.010 | 0.233 | false | FAIL |
| 4 | 0.798 | 0.854 | +0.056 | 0.291 | **true** | MARGINAL |
| 8 | 0.798 | 0.879 | +0.081 | 0.295 | **true** | MARGINAL |

N≥4 时 structural_beats_surface 翻转为 true，rho_advantage 从负值上升到 +0.083。

### 崩溃说明

`14b_conll_base.log` 显示进程在完成 fewnerd_n8 后启动了 CoNLL base inference 的下一批任务，在 55% 进度（15176/27624）时 vLLM EngineCore 崩溃（`EngineDeadError`）。这是**后续实验**的失败，与 FewNERD 推理无关——FewNERD 部分已全部完成。

---
