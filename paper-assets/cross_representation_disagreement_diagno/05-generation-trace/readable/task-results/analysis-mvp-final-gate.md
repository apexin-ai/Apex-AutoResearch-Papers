# analysis mvp final gate

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_final_gate_20260514T154854_result.json`
- **Structured JSON:** [`9912e67715c757668512.json`](../../sessions/99/9912e67715c757668512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. Pipeline 完成状态
Pipeline **未完成全部 204 样本**——在第 110 个样本（folio_validation_109 stability check 阶段）静默退出，无 ERROR/Traceback。vLLM 仍正常运行，实例未重启（uptime 21d）。原因不明，可能是 Python 进程被系统 kill。

**样本总数：109/204**

### 2. 日志最后数行
```
23:44:10 [folio_validation_109] stability check …
23:45:15 HTTP Request: POST ... "HTTP/1.1 200 OK"
23:45:26 HTTP Request: POST ... "HTTP/1.1 200 OK"
23:45:42 HTTP Request: POST ... "HTTP/1.1 200 OK"
(日志到此结束，无 done/error 行)
```

### 3. evaluate_mvp.py 完整输出

**All samples (n=103 effective)：5/5 PASS → PROCEED**

| Gate | Value | Threshold | Result |
|------|-------|-----------|--------|
| C1 disagree_rate | 33.0% (34/103) | ≥10% | PASS |
| C2 diagnostic_rate | 88.2% (30/34) | ≥40% | PASS |
| C3 error_types | 3 types | ≥2 | PASS |
| C4 targeted_vs_blind | +11.6pp (T:69.8% B:58.1%) | >5pp | PASS |
| C5 localization | 81.8% (18/22) | ≥60% | PASS |

**Excl. GT=Unknown (n=67)：4/5 PASS**

| Gate | Value | Threshold | Result |
|------|-------|-----------|--------|
| C1 | 32.8% (22/67) | ≥10% | PASS |
| C2 | 90.9% (20/22) | ≥40% | PASS |
| C3 | 2 types | ≥2 | PASS |
| C4 | +3.6pp (T:67.9% B:64.3%) | >5pp | **FAIL** |
| C5 | 92.9% (13/14) | ≥60% | PASS |

### 4. Registry 更新
- status → ANALYZING
- conclusion → success
- metrics → 全部 C1-C5 数值（含 excl_unknown）
- checkpoint_path / log_path → 已设置
- Cron：无活跃 cron 需要删除

### 待决策
Pipeline 可通过 `--resume` 续跑剩余 95 样本补全到 204。Excl. Unknown 模式 C4 仅 +3.6pp（FAIL），更多数据可能改变此结果。

---
