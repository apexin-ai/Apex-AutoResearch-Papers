# analysis 3seed summary edcr

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed-summary-edcr_20260515T115248_result.json`
- **Structured JSON:** [`10985a67341f9d4ddf8f.json`](../../sessions/10/10985a67341f9d4ddf8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

## Task A：3-seed 汇总脚本

脚本已部署到 `/root/autodl-tmp/scripts/summarize_3seed.py`，dry-run 通过（2/3 seeds）。

当前 2-seed 结果：
| 指标 | r1 (s42) | s44 (s44) | Mean±Std | vs SFT |
|------|----------|-----------|----------|--------|
| Rel F1 | 0.4449 | 0.4655 | 0.455±0.015 | +12.2% |
| Evi F1 | 0.8187 | 0.8087 | 0.814±0.007 | +2.0% |
| EDCR | 0.6565 | 0.6350 | 0.646±0.015 | -9.3% |

s43 eval 完成后直接运行 `python3 /root/autodl-tmp/scripts/summarize_3seed.py` 即可获取 3-seed 汇总。

## Task B：EDCR 证据分布分析

从 1848 个含 distractor 的 matched triples 中采样 50 个，自动分类 + 人工复核 "unrelated" 类别，核心发现：

- **~84% 的 "distractor" citations 实际语义相关**（实体提及 68% + 共指/实体变体 16%）
- **真正无关的 distractor 仅 ~4%**
- 82% 的 case 只多引了 1 个句子，68% 的 case 完整覆盖了 gold evidence
- **结论**：EDCR 下降是 over-citation（引用更宽泛的相关语境），不是证据质量退化。Evi F1 反而优于 SFT（0.81 vs 0.80）

报告已注册为 artifact `edcr_analysis_r2b.md`。

---
