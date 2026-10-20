# check entailment rescorer results

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_entailment_rescorer_results_20260514T150348_result.json`
- **Structured JSON:** [`cd15c7e9609200574a5f.json`](../../sessions/cd/cd15c7e9609200574a5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总所有结果：

---

## 1. PID 54002 状态
**PROCESS_ENDED** — 进程已结束。

## 2. 结果文件列表

| 文件 | 大小 | 时间 |
|------|------|------|
| `entailment_rescore_results.json` | 1KB | 21:26 |
| `entailment_rescore_v2_results.json` | 105B | 22:00 |
| `mvp_report.json` | 2.4KB | 22:17 |
| `results.json` / `mvp_003_final.json` | 125KB | 22:17 |
| `chain_details.json` | 9KB | 22:17 |

当前无 entailment/rescore 进程运行。

## 3. 结果 JSON 内容

### `entailment_rescore_results.json`
```json
{"chains": [], "summary": {"n_problems": 0, "n_chains": 0, ...}, "status": "complete", "total_time_s": 9.5e-07}
```
**空结果** — 0 chains, 0 problems。运行瞬间完成，没有处理任何数据。

### `entailment_rescore_v2_results.json`
```json
{"chains": [], "summary": {}, "status": "interrupted", "problems_done": 0, "total_time_s": 0}
```
**被中断** — 0 problems done。

### `mvp_report.json`（最新完整结果，50 problems）
```json
{
  "config": {"num_problems": 50, "num_chains": 8, "total_chains": 400},
  "accuracy": {
    "svs": {"correct": 30, "total": 50, "accuracy": 0.60},
    "sc":  {"correct": 29, "total": 50, "accuracy": 0.58},
    "delta": 0.02
  },
  "formalization": {
    "total_claims": 7941, "formalized_claims": 6742, "rate": 0.849
  },
  "p1_autoformalization": {"threshold": 0.5, "actual": 0.849, "pass": true},
  "p2_ic_discrimination": {
    "n_correct_chains": 226, "n_incorrect_chains": 174,
    "mean_correct_ic": 0.7476, "mean_incorrect_ic": 0.8223,
    "cohens_d": -0.3736,  // 方向反了！incorrect > correct
    "ttest_p_value": 0.999879,
    "mannwhitney_p_value": 0.998748,
    "pass": "False"
  },
  "verdict": {"p1": "PASS", "p2": "FAIL", "overall": "FAIL"},
  "cost": {"estimated_cost_usd": 2.50}
}
```

## 4. 关键发现

- **P1 (autoformalization)**: PASS，84.9% formalization rate (阈值 50%)
- **P2 (IC discrimination)**: **FAIL** — Cohen's d = **-0.3736**，方向完全反了（incorrect chains 的 IC 分数更高：0.8223 vs correct 的 0.7476）
- **SVS vs SC**: SVS 60% vs SC 58%，仅 +2pp，几乎无区分度
- t-test p=0.9999, Mann-Whitney p=0.9987 — IC 分数完全无法区分 correct/incorrect chains

## 5. 日志中的 formalization 问题

- `entailment_rescorer.log` 中有 344 行包含 formalization/success/fail 关键词
- 大量 Z3 sandbox SyntaxError：LLM 生成的 Z3 表达式语法无效
- `entailment_v3.log`：处理了 46 个 problems，formalization 成功率较好（16/16, 30/30 等）
- `entailment_10q_test.log`：因 HuggingFace 网络不可达（Errno 101）而失败，`trust_remote_code` API 变更也导致 datasets 加载报错

---
