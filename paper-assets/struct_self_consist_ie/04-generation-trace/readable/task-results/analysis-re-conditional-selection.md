# analysis re conditional selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_re_conditional_selection_20260515T042543_result.json`
- **Structured JSON:** [`3737ffbaa82704a0907e.json`](../../sessions/37/3737ffbaa82704a0907e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_conditional_analysis.json`。

```json
{
  "full_set": {
    "n": 397,
    "signals": {
      "sj":  {"rho": 0.2503, "p": 0.0,      "selection_f1": 0.3855},
      "fk":  {"rho": 0.2752, "p": 0.0,      "selection_f1": 0.3872},
      "em":  {"rho": 0.1369, "p": 0.006285, "selection_f1": 0.3718},
      "vc":  {"rho": 0.3311, "p": 0.0,      "selection_f1": 0.3592},
      "lp":  {"rho": 0.2662, "p": 0.0,      "selection_f1": 0.3948}
    },
    "greedy_f1": 0.4042,
    "oracle_f1": 0.585
  },
  "conditional_set": {
    "n": 238,
    "filter": "greedy_f1 > 0",
    "signals": {
      "sj":  {"rho": 0.2457, "p": 0.000128, "selection_f1": 0.6035},
      "fk":  {"rho": 0.1139, "p": 0.079557, "selection_f1": 0.6063},
      "em":  {"rho": 0.4275, "p": 0.0,      "selection_f1": 0.5828},
      "vc":  {"rho": 0.1386, "p": 0.03262,  "selection_f1": 0.5737},
      "lp":  {"rho": 0.0112, "p": 0.863708, "selection_f1": 0.5995}
    },
    "greedy_f1": 0.6743,
    "oracle_f1": 0.7574
  }
}
```

关键发现：
- 过滤掉 159 个 greedy F1=0 的 instances（40.1%，非 44%——原数据可能有微小差异），剩余 n=238
- 条件子集上 **em 的 ρ 从 0.137 跃升到 0.428**（最强信号），**sj 基本持平**（0.250→0.246）
- **fk 和 vc 大幅衰减**（fk: 0.275→0.114 不显著，vc: 0.331→0.139），**lp 完全失效**（0.266→0.011，p=0.86）
- 所有 selection F1 均低于 greedy F1（0.674），说明在非零子集上 selection 策略无法超越 greedy

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "full_set": {
      "n": 397,
      "signals": {
        "sj": {
          "rho": 0.2503,
          "p": 0.0,
          "selection_f1": 0.3855
        },
        "fk": {
          "rho": 0.2752,
          "p": 0.0,
          "selection_f1": 0.3872
        },
        "em": {
          "rho": 0.1369,
          "p": 0.006285,
          "selection_f1": 0.3718
        },
        "vc": {
          "rho": 0.3311,
          "p": 0.0,
          "selection_f1": 0.3592
        },
        "lp": {
          "rho": 0.2662,
          "p": 0.0,
          "selection_f1": 0.3948
        }
      },
      "greedy_f1": 0.4042,
      "oracle_f1": 0.585
    },
    "conditional_set": {
      "n": 238,
      "filter": "greedy_f1 > 0",
      "signals": {
        "sj": {
          "rho": 0.2457,
          "p": 0.000128,
          "selection_f1": 0.6035
        },
        "fk": {
          "rho": 0.1139,
          "p": 0.079557,
          "selection_f1": 0.6063
        },
        "em": {
          "rho": 0.4275,
          "p": 0.0,
          "selection_f1": 0.5828
        },
        "vc": {
          "rho": 0.1386,
          "p": 0.03262,
          "selection_f1": 0.5737
        },
        "lp": {
          "rho": 0.0112,
          "p": 0.863708,
          "selection_f1": 0.5995
        }
      },
      "greedy_f1": 0.6743,
      "oracle_f1": 0.7574
    }
  }
}
```

</details>

---
