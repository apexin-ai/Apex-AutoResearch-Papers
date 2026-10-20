# analysis eval 204 final

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_204_final_20260515T001725_result.json`
- **Structured JSON:** [`51e96926f56dd2b959da.json`](../../sessions/51/51e96926f56dd2b959da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。完整结果如下：

```
======================================================================
MVP Gate Evaluation
======================================================================
Results file: results/mvp_v4_full.jsonl
Total samples: 206 | Valid: 206 | Effective (both executed): 194 | GT!=Unknown: 137

--- All samples (both executed) ---
C1 disagree_rate:      39.7% (77/194)               [>=10%]  PASS
C2 diagnostic_rate:    87.0% (67/77)                [>=40%]  PASS
C3 error_types:        3 types                      [>=2  ]  PASS
C4 targeted_vs_blind:  +7.2pp (T:61/97 B:54/97)     [>5pp ]  PASS
C5 localization:       85.4% (35/41)                [>=60%]  PASS

--- Excluding GT=Unknown ---
C1 disagree_rate:      35.2% (45/128)               [>=10%]  PASS
C2 diagnostic_rate:    84.4% (38/45)                [>=40%]  PASS
C3 error_types:        2 types                      [>=2  ]  PASS
C4 targeted_vs_blind:  -1.7pp (T:34/59 B:35/59)     [>5pp ]  FAIL
C5 localization:       89.3% (25/28)                [>=60%]  PASS

======================================================================
MVP RESULT: 5/5 PASS -> PROCEED
======================================================================
```

**汇总：**

| 项目 | 状态 |
|------|------|
| JSONL 行数 | 205（206 samples，含可能的多余行） |
| Pipeline PID 57877 | **存活** |
| Repair PID 64365 | **存活** |
| mvp_v4_repair_fixed.json | **不存在**（repair 仍在运行） |

**评估结果：All-mode 5/5 PASS → PROCEED。** Excl-Unknown 模式下 C4 targeted_vs_blind FAIL（-1.7pp，未达 >5pp 阈值），其余均 PASS。

两个进程仍在运行，repair 产出文件尚未生成，后续可再跑一次评估对比。

---
