# analysis error analysis v3

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-analysis-v3_20260514T125143_result.json`
- **Structured JSON:** [`b1288ea4b0ccfda78cc0.json`](../../sessions/b1/b1288ea4b0ccfda78cc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本 `error_analysis_v3.py` 已在服务器上运行，结果：

**全量 probe (conf≥0) 在 8101 test windows 上的表现：** F1=0.9165, Acc=0.8785, 514 FP + 470 FN

关键发现：

| 维度 | 高错误率区域 | 错误率 |
|------|------------|--------|
| **Action type** | `bash_other` 19.9%, `bash_cat` 40.0%, `bash_ls` 14.9% | 杂项 bash 命令最难判 |
| **LF pattern** | `-/-/0` (cmd_rep=stag, file_diff=stag, outcome_bp=abstain) 62.4% 全是 FP | outcome_bp abstain 时 FP 飙升 |
| **LF pattern** | `0/+/-` (cmd_rep=abstain, file_diff=progress, outcome_bp=stag) 24.4% 全是 FN | LF 内部矛盾时 FN 集中 |
| **Outcome** | unresolved 轨迹 12.8% vs resolved 5.3% | 失败轨迹错误率 2.4× |
| **Confidence** | conf=1 → 13.4%, conf=2 → 9.0%, conf=3 → 3.5% | 单调递减，符合预期 |
| **Position** | late_25% → 15.9% vs early_25% → 9.5% | 轨迹末段错误率最高 |

报告已保存到本地 `artifacts/error_analysis_v3_report.md`，JSON 和 markdown 均在服务器 `artifacts/error_analysis_v3/` 目录。

---
