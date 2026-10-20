# code d146 base isr and aggregate

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-base-isr-and-aggregate_20260520T033621_result.json`
- **Structured JSON:** [`1172cd52cdd95f73782f.json`](../../sessions/11/1172cd52cdd95f73782f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部获取完成。

---

## 任务 1: Base Model ISR Baseline

**文件路径**: `/root/autodl-tmp/outputs/d146_pf_base/eval_sta_results.json`

| 字段 | 值 |
|---|---|
| n_problems | 100 |
| **n_proved** | **16** |
| **prove_rate** | **0.16** |
| **mean_isr** | **0.0496** |
| isr_std | 0.1161 |
| median_isr | 0.0 |
| **proved_only_mean_isr** | **0.3098** |
| min_isr / max_isr | 0.0 / 0.4 |
| model_path | /root/autodl-tmp/models/Qwen3-4B |

**By answer_type**:
- true: 32 problems, 16 proved (50.0%), mean_isr=0.1549
- false: 39 problems, 0 proved (0.0%), mean_isr=0.0
- unknown: 29 problems, 0 proved (0.0%), mean_isr=0.0

---

## 任务 2: Genuine Rate 聚合数据

**所有文件路径**: `/root/autodl-tmp/outputs/d146_pf_{name}/classify.json`

```json
{
  "base":      {"proved": 16, "genuine": 16, "TS": 0,  "CE": 0,  "PG": 0, "genuine_rate": 1.0},
  "exec-s42":  {"proved": 99, "genuine": 0,  "TS": 99, "CE": 0,  "PG": 0, "genuine_rate": 0.0},
  "exec-s43":  {"proved": 63, "genuine": 32, "TS": 0,  "CE": 31, "PG": 0, "genuine_rate": 0.5079},
  "exec-s44":  {"proved": 72, "genuine": 1,  "TS": 0,  "CE": 71, "PG": 0, "genuine_rate": 0.0139},
  "isr-s42":   {"proved": 46, "genuine": 46, "TS": 0,  "CE": 0,  "PG": 0, "genuine_rate": 1.0},
  "isr-s43":   {"proved": 56, "genuine": 17, "TS": 0,  "CE": 39, "PG": 0, "genuine_rate": 0.3036},
  "isr-s44":   {"proved": 66, "genuine": 66, "TS": 0,  "CE": 0,  "PG": 0, "genuine_rate": 1.0}
}
```

**汇总表**:

| Experiment | Proved | Genuine | TS | CE | PG | Genuine Rate |
|---|---|---|---|---|---|---|
| base | 16 | 16 | 0 | 0 | 0 | 100.0% |
| exec-s42 | 99 | 0 | 99 | 0 | 0 | 0.0% |
| exec-s43 | 63 | 32 | 0 | 31 | 0 | 50.8% |
| exec-s44 | 72 | 1 | 0 | 71 | 0 | 1.4% |
| isr-s42 | 46 | 46 | 0 | 0 | 0 | 100.0% |
| isr-s43 | 56 | 17 | 0 | 39 | 0 | 30.4% |
| isr-s44 | 66 | 66 | 0 | 0 | 0 | 100.0% |

关键发现：
- **Exec-only** 主导 hacking 模式是 TS（s42 全部 99 个 proved 都是 TS）和 CE（s43/s44），PG=0
- **ISR** 方差极大：s42/s44 genuine_rate=100%（零 hacking），s43 有 CE 39 个（genuine_rate=30.4%）
- **Base model** 16 个 proved 全部 genuine（无任何 hacking 模式）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "base": {
      "proved": 16,
      "genuine": 16,
      "TS": 0,
      "CE": 0,
      "PG": 0,
      "genuine_rate": 1.0
    },
    "exec-s42": {
      "proved": 99,
      "genuine": 0,
      "TS": 99,
      "CE": 0,
      "PG": 0,
      "genuine_rate": 0.0
    },
    "exec-s43": {
      "proved": 63,
      "genuine": 32,
      "TS": 0,
      "CE": 31,
      "PG": 0,
      "genuine_rate": 0.5079
    },
    "exec-s44": {
      "proved": 72,
      "genuine": 1,
      "TS": 0,
      "CE": 71,
      "PG": 0,
      "genuine_rate": 0.0139
    },
    "isr-s42": {
      "proved": 46,
      "genuine": 46,
      "TS": 0,
      "CE": 0,
      "PG": 0,
      "genuine_rate": 1.0
    },
    "isr-s43": {
      "proved": 56,
      "genuine": 17,
      "TS": 0,
      "CE": 39,
      "PG": 0,
      "genuine_rate": 0.3036
    },
    "isr-s44": {
      "proved": 66,
      "genuine": 66,
      "TS": 0,
      "CE": 0,
      "PG": 0,
      "genuine_rate": 1.0
    }
  }
}
```

</details>

---
