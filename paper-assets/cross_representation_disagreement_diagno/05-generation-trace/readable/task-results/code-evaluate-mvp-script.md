# code evaluate mvp script

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_evaluate_mvp_script_20260514T142337_result.json`
- **Structured JSON:** [`1a1709f63ed0330dc2ae.json`](../../sessions/1a/1a1709f63ed0330dc2ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，v4 pipeline 正常运行。

---

**脚本**: `/root/autodl-tmp/crdd/src/evaluate_mvp.py`

核心逻辑：
- 按 `fol_exec.verdict` / `code_exec.verdict` 过滤 effective 样本（排除 Error/None）
- C1-C3 基于 effective 中的 disagree 样本计算
- C4 遍历所有 valid 样本的 `repair` 字段，统计 targeted vs blind 成功率
- C5 通过 `error_side` 预测值 vs `fol_correct`/`code_correct` 推导的实际错误侧对比
- 两组输出：全部样本 / 排除 GT=Unknown

**当前 v4 部分数据（80 样本）输出**:

```
Total samples: 80 | Valid: 80 | Effective (both executed): 75 | GT!=Unknown: 51

--- All samples (both executed) ---
C1 disagree_rate:      32.0% (24/75)         [>=10%]  PASS
C2 diagnostic_rate:    87.5% (21/24)         [>=40%]  PASS
C3 error_types:        3 types               [>=2  ]  PASS
C4 targeted_vs_blind:  +22.6pp (T:23/31 B:16/31) [>5pp]  PASS
C5 localization:       100.0% (34/34)        [>=60%]  PASS

--- Excluding GT=Unknown ---
C1-C5: 全部 PASS

MVP RESULT: 5/5 PASS -> PROCEED
```

**v4 pipeline 状态**: PID 29177 正常运行中（已跑 3h25m），未受影响。

---
