# analysis phase1 final

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase1-final_20260513T151818_result.json`
- **Structured JSON:** [`4354c8edde49688a1d21.json`](../../sessions/43/4354c8edde49688a1d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Phase 1 最终分析报告

### 1. 数据完整性 ✓

| Task | Episodes | summary.json |
|------|----------|-------------|
| boil | 20 | ✓ |
| change-the-state-of-matter-of | 20 | ✓ |
| chemistry-mix-paint-secondary-color | 20 | ✓ |
| grow-plant | 20 | ✓ |
| melt | 20 | ✓ |

5 task × 20 episodes × 3 modes，共 100 条数据，全部齐全。

---

### 2. analysis.py 标准输出

```
==========================================================================================
PHASE 1 RESULTS ANALYSIS
==========================================================================================
Task                                  Internal    Determ.     Oracle     Δ(O-I)             90% CI     Judgment
------------------------------------------------------------------------------------------
boil                                   -49.8±50.3   -19.7±40.2   -29.7±46.0    +20.1 [+0.1, +40.0] SIGNIFICANT_POSITIVE
change-the-state-of-matter-of          -54.7±50.1   -14.5±35.9     0.5±1.1     +55.1 [+35.3, +75.2] SIGNIFICANT_POSITIVE
chemistry-mix-paint-secondary-color    -41.0±53.8    -5.5±32.8     4.5±8.0     +45.5 [+26.0, +65.5] SIGNIFICANT_POSITIVE
grow-plant                               0.5±1.4      0.5±1.4      0.5±1.4      +0.0 [+0.0, +0.0]    NO_EFFECT
melt                                   -54.7±50.1   -14.6±35.9     2.1±8.0     +56.9 [+38.7, +76.8] SIGNIFICANT_POSITIVE
------------------------------------------------------------------------------------------
Significant positive (CI > 0): 4/5
Positive direction:           4/5

Oracle vs Deterministic (routing incremental value):
  boil                                Δ(O-D)=-10.0  90% CI [-20.0, +0.0]
  change-the-state-of-matter-of       Δ(O-D)=+14.9  90% CI [+4.9, +29.9]
  chemistry-mix-paint-secondary-color Δ(O-D)=+10.0  90% CI [+0.0, +21.0]
  grow-plant                          Δ(O-D)=+0.0  90% CI [+0.0, +0.0]
  melt                                Δ(O-D)=+16.7  90% CI [+5.0, +31.7]

OVERALL VERDICT: PASS → Proceed to full research phase
```

---

### 3. 补充分析 — (det - internal) 主指标

```
====================================================================================================
PHASE 1 FINAL ANALYSIS -- (det - internal) as primary comparison
====================================================================================================
Task                                         Internal      Determ.       Oracle     Δ(D-I)       90% CI        Sig?
----------------------------------------------------------------------------------------------------
boil                                        -49.8±50.3   -19.7±40.2   -29.7±46.0    +30.1  [+15.0, +50.0]     Y
change-the-state-of-matter-of               -54.7±50.1   -14.5±35.9     0.5±1.1     +40.2  [+25.0, +60.1]     Y
chemistry-mix-paint-secondary-color         -41.0±53.8    -5.5±32.8     4.5±8.0     +35.5  [+20.0, +55.0]     Y
grow-plant                                    0.5±1.4      0.5±1.4      0.5±1.4      +0.0  [+0.0, +0.0]
melt                                        -54.7±50.1   -14.6±35.9     2.1±8.0     +40.1  [+25.0, +60.1]     Y
----------------------------------------------------------------------------------------------------
Significant (CI > 0): 4/5
Positive direction:   4/5

VERDICT: PASS
```

**Oracle vs Internal / Oracle vs Det:**
```
  boil                                     Δ(O-I)=+20.1 CI[+0.1,+40.0]  Δ(O-D)=-10.0 CI[-20.0,+0.0]
  change-the-state-of-matter-of            Δ(O-I)=+55.1 CI[+35.3,+75.2]  Δ(O-D)=+14.9 CI[+4.9,+29.9]
  chemistry-mix-paint-secondary-color      Δ(O-I)=+45.5 CI[+26.0,+65.5]  Δ(O-D)=+10.0 CI[+0.0,+21.0]
  grow-plant                               Δ(O-I)=+0.0 CI[+0.0,+0.0]  Δ(O-D)=+0.0 CI[+0.0,+0.0]
  melt                                     Δ(O-I)=+56.9 CI[+38.7,+76.8]  Δ(O-D)=+16.7 CI[+5.0,+31.7]
```

---

### 4. 各 Task 三组均值 ± std

| Task | Internal | Deterministic | Oracle |
|------|---------|--------------|--------|
| boil | -49.8 ± 50.3 | -19.7 ± 40.2 | -29.7 ± 46.0 |
| change-the-state-of-matter-of | -54.7 ± 50.1 | -14.5 ± 35.9 | 0.5 ± 1.1 |
| chemistry-mix-paint-secondary-color | -41.0 ± 53.8 | -5.5 ± 32.8 | 4.5 ± 8.0 |
| grow-plant | 0.5 ± 1.4 | 0.5 ± 1.4 | 0.5 ± 1.4 |
| melt | -54.7 ± 50.1 | -14.6 ± 35.9 | 2.1 ± 8.0 |

---

### 5. (det - internal) 90% CI 与 Verdict

| Task | Δ(D-I) Mean | 90% CI | CI excludes 0? |
|------|------------|--------|----------------|
| boil | +30.1 | [+15.0, +50.0] | **Yes** |
| change-the-state-of-matter-of | +40.2 | [+25.0, +60.1] | **Yes** |
| chemistry-mix-paint-secondary-color | +35.5 | [+20.0, +55.0] | **Yes** |
| grow-plant | 0.0 | [0.0, 0.0] | No |
| melt | +40.1 | [+25.0, +60.1] | **Yes** |

- Significant (CI > 0): **4/5**
- Positive direction: **4/5**
- **VERDICT: PASS**

grow-plant 三种模式得分完全一致（0.5 ± 1.4），属于 NO_EFFECT——该 task 本身难度极低或评估指标无区分度。排除它后 4/4 tasks 均显著正向。

boil 的 oracle 反而比 det 差（Δ(O-D) = -10.0），说明 boil 旧代码的 oracle routing 逻辑存在问题（旧代码 >= tie-break，无 death filter），但 det vs internal 的改善仍然显著。

---

### 6. final_analysis_det_vs_internal.json 完整内容

```json
{
  "verdict": "PASS",
  "n_significant": 4,
  "n_positive": 4,
  "tasks": {
    "boil": {
      "n": 20,
      "internal": {"mean": -49.75, "std": 50.26},
      "det": {"mean": -19.7, "std": 40.16},
      "oracle": {"mean": -29.7, "std": 46.03},
      "det_minus_internal": {"mean": 30.05, "ci90": [15.0, 50.0], "positive": true, "ci_excludes_zero": true},
      "oracle_minus_internal": {"mean": 20.05, "ci90": [0.1, 40.0]},
      "oracle_minus_det": {"mean": -10.0, "ci90": [-20.0, 0.0]}
    },
    "change-the-state-of-matter-of": {
      "n": 20,
      "internal": {"mean": -54.7, "std": 50.09},
      "det": {"mean": -14.5, "std": 35.94},
      "oracle": {"mean": 0.45, "std": 1.07},
      "det_minus_internal": {"mean": 40.2, "ci90": [25.0, 60.15], "positive": true, "ci_excludes_zero": true},
      "oracle_minus_internal": {"mean": 55.15, "ci90": [35.3, 75.15]},
      "oracle_minus_det": {"mean": 14.95, "ci90": [4.9, 29.95]}
    },
    "chemistry-mix-paint-secondary-color": {
      "n": 20,
      "internal": {"mean": -41.0, "std": 53.84},
      "det": {"mean": -5.5, "std": 32.78},
      "oracle": {"mean": 4.5, "std": 8.05},
      "det_minus_internal": {"mean": 35.5, "ci90": [20.0, 55.0], "positive": true, "ci_excludes_zero": true},
      "oracle_minus_internal": {"mean": 45.5, "ci90": [26.0, 65.5]},
      "oracle_minus_det": {"mean": 10.0, "ci90": [0.0, 21.0]}
    },
    "grow-plant": {
      "n": 20,
      "internal": {"mean": 0.5, "std": 1.36},
      "det": {"mean": 0.5, "std": 1.36},
      "oracle": {"mean": 0.5, "std": 1.36},
      "det_minus_internal": {"mean": 0.0, "ci90": [0.0, 0.0], "positive": false, "ci_excludes_zero": false},
      "oracle_minus_internal": {"mean": 0.0, "ci90": [0.0, 0.0]},
      "oracle_minus_det": {"mean": 0.0, "ci90": [0.0, 0.0]}
    },
    "melt": {
      "n": 20,
      "internal": {"mean": -54.7, "std": 50.09},
      "det": {"mean": -14.55, "std": 35.91},
      "oracle": {"mean": 2.15, "std": 8.05},
      "det_minus_internal": {"mean": 40.15, "ci90": [25.0, 60.15], "positive": true, "ci_excludes_zero": true},
      "oracle_minus_internal": {"mean": 56.85, "ci90": [38.7, 76.85]},
      "oracle_minus_det": {"mean": 16.7, "ci90": [5.0, 31.7]}
    }
  }
}
```

**结论**: Phase 1 以 (det - internal) 为主指标，4/5 tasks 显著正向，**VERDICT = PASS**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "verdict": "PASS",
    "n_significant": 4,
    "n_positive": 4,
    "tasks": {
      "boil": {
        "n": 20,
        "internal": {
          "mean": -49.75,
          "std": 50.26
        },
        "det": {
          "mean": -19.7,
          "std": 40.16
        },
        "oracle": {
          "mean": -29.7,
          "std": 46.03
        },
        "det_minus_internal": {
          "mean": 30.05,
          "ci90": [
            15.0,
            50.0
          ],
          "positive": true,
          "ci_excludes_zero": true
        },
        "oracle_minus_internal": {
          "mean": 20.05,
          "ci90": [
            0.1,
            40.0
          ]
        },
        "oracle_minus_det": {
          "mean": -10.0,
          "ci90": [
            -20.0,
            0.0
          ]
        }
      },
      "change-the-state-of-matter-of": {
        "n": 20,
        "internal": {
          "mean": -54.7,
          "std": 50.09
        },
        "det": {
          "mean": -14.5,
          "std": 35.94
        },
        "oracle": {
          "mean": 0.45,
          "std": 1.07
        },
        "det_minus_internal": {
          "mean": 40.2,
          "ci90": [
            25.0,
            60.15
          ],
          "positive": true,
          "ci_excludes_zero": true
        },
        "oracle_minus_internal": {
          "mean": 55.15,
          "ci90": [
            35.3,
            75.15
          ]
        },
        "oracle_minus_det": {
          "mean": 14.95,
          "ci90": [
            4.9,
            29.95
          ]
        }
      },
      "chemistry-mix-paint-secondary-color": {
        "n": 20,
        "internal": {
          "mean": -41.0,
          "std": 53.84
        },
        "det": {
          "mean": -5.5,
          "std": 32.78
        },
        "oracle": {
          "mean": 4.5,
          "std": 8.05
        },
        "det_minus_internal": {
          "mean": 35.5,
          "ci90": [
            20.0,
            55.0
          ],
          "positive": true,
          "ci_excludes_zero": true
        },
        "oracle_minus_internal": {
          "mean": 45.5,
          "ci90": [
            26.0,
            65.5
          ]
        },
        "oracle_minus_det": {
          "mean": 10.0,
          "ci90": [
            0.0,
            21.0
          ]
        }
      },
      "grow-plant": {
        "n": 20,
        "internal": {
          "mean": 0.5,
          "std": 1.36
        },
        "det": {
          "mean": 0.5,
          "std": 1.36
        },
        "oracle": {
          "mean": 0.5,
          "std": 1.36
        },
        "det_minus_internal": {
          "mean": 0.0,
          "ci90": [
            0.0,
            0.0
          ],
          "positive": false,
          "ci_excludes_zero": false
        },
        "oracle_minus_internal": {
          "mean": 0.0,
          "ci90": [
            0.0,
            0.0
          ]
        },
        "oracle_minus_det": {
          "mean": 0.0,
          "ci90": [
            0.0,
            0.0
          ]
        }
      },
      "melt": {
        "n": 20,
        "internal": {
          "mean": -54.7,
          "std": 50.09
        },
        "det": {
          "mean": -14.55,
          "std": 35.91
        },
        "oracle": {
          "mean": 2.15,
          "std": 8.05
        },
        "det_minus_internal": {
          "mean": 40.15,
          "ci90": [
            25.0,
            60.15
          ],
          "positive": true,
          "ci_excludes_zero": true
        },
        "oracle_minus_internal": {
          "mean": 56.85,
          "ci90": [
            38.7,
            76.85
          ]
        },
        "oracle_minus_det": {
          "mean": 16.7,
          "ci90": [
            5.0,
            31.7
          ]
        }
      }
    }
  }
}
```

</details>

---
