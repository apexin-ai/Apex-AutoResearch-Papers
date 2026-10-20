# analysis v5 random baselines

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v5-random-baselines_20260514T025924_result.json`
- **Structured JSON:** [`b7ddff7696b655ff289f.json`](../../sessions/b7/b7ddff7696b655ff289f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均完成（50/50 problems, EXIT_CODE=0, 无 NaN/Inf warnings）。

## 提取结果

### mvp_v5_random_s015 (random, s=0.15)

| Phase | II mean | 95% CI | II median | II winsorized | kv_ppl | attn_ppl | both_ppl | dense_ppl |
|-------|---------|--------|-----------|---------------|--------|----------|----------|-----------|
| high | +0.456 | [+0.119, +0.767] | 0.161 | 0.538 | 3.14 | 1.56 | 3.92 | 1.15 |
| mid | +0.513 | [+0.337, +0.741] | 0.252 | 0.509 | 2.91 | 1.41 | 4.14 | 1.12 |
| low | +0.477 | [+0.285, +0.701] | 0.183 | 0.428 | 3.61 | 1.39 | 4.71 | 1.11 |

Segments: high=511, mid=391, low=454. No warnings.

### mvp_v5_random_s025 (random, s=0.25)

| Phase | II mean | 95% CI | II median | II winsorized | kv_ppl | attn_ppl | both_ppl | dense_ppl |
|-------|---------|--------|-----------|---------------|--------|----------|----------|-----------|
| high | +3.905 | [+0.980, +6.339] | 3.002 | 4.708 | 6.39 | 8.66 | 17.06 | 1.15 |
| mid | +7.949 | [+4.670, +11.867] | 2.985 | 6.353 | 6.11 | 2.62 | 15.38 | 1.12 |
| low | +3.911 | [+2.707, +5.236] | 2.915 | 3.858 | 9.07 | 5.15 | 29.32 | 1.11 |

Segments: high=511, mid=391, low=454. No warnings.

---

## Random vs Importance 对比

### s=0.15

| Metric | Importance | Random | Delta |
|--------|-----------|--------|-------|
| ii_high | +0.306 | **+0.456** | random 高 49% |
| ii_mid | +1.274 | **+0.513** | random 低 60% |
| ii_low | **+8.786** | +0.477 | random 低 95% |
| kv_ppl_high | **1.21** | 3.14 | importance 低 61% |
| kv_ppl_mid | **2.13** | 2.91 | importance 低 27% |
| kv_ppl_low | 6.75 | **3.61** | random 低 47% |

### s=0.25

| Metric | Importance | Random | Delta |
|--------|-----------|--------|-------|
| ii_high | +0.851 | **+3.905** | random 高 4.6x |
| ii_mid | +9.306 | +7.949 | ~相当 |
| ii_low | **+96.715** | +3.911 | importance 高 24.7x |
| kv_ppl_high | **1.31** | 6.39 | importance 低 4.9x |
| kv_ppl_mid | 6.18 | 6.11 | ~相当 |
| kv_ppl_low | 23.89 | **9.07** | random 低 2.6x |

---

## 分析

### 1. II 符号
**两组全部为正（super-additive）**，无 sign reversal。Pivot hypothesis 预期 importance → negative II 未实现。

### 2. II 幅度分布模式
- **Random II 跨 phase 非常均匀**：s=0.15 时三个 phase 在 0.46~0.51 范围；s=0.25 时在 3.9~7.9 范围
- **Importance II 极度不均匀**：low-sparsity phase 暴涨（s=0.15: 8.79; s=0.25: 96.7），说明 importance metric 在 high natural sparsity 区域造成了极端的 super-additive 干扰

### 3. KV PPL
- Importance 在 **high-sparsity phase 更优**（heads 激活度高 → importance 排序可靠）
- Random 在 **low-sparsity phase 反而更优**（importance metric 在 high natural sparsity 区域失效，eviction 决策比随机还差）
- Mid phase 两者接近

### 4. Both PPL
s=0.25 差异显著：random both_ppl (15~29) 远低于 importance 在 low phase 暗示的水平（importance kv_ppl_low=23.89 本身已经很高）

---

## 结论：**Negative — importance metric 可能无效甚至有害**

- **Sign reversal 不成立**：两种策略 II 符号相同（全正），strategy-dependent reversal 假说被否定
- **Importance masking 不是"更智能"的 eviction**：在 low-sparsity phases，importance 的 kv_ppl 和 II 都远差于 random，说明当 attention 本身就稀疏时，importance metric 的排序几乎没有信号
- **Importance 唯一优势在 high-sparsity phase**（ii_high 和 kv_ppl_high 更低），但 low phase 的灾难性表现（II=96.7 at s=0.25）抵消了收益

---

## 结构化 JSON

```json
{
  "mvp_v5_random_s015": {
    "status": "completed",
    "n_problems": 50,
    "masking_method": "random",
    "sparsity": 0.15,
    "warnings": [],
    "segments": {"high": 511, "mid": 391, "low": 454},
    "ii": {
      "high": {"mean": 0.456, "ci": [0.119, 0.767], "median": 0.161, "winsorized": 0.538},
      "mid": {"mean": 0.513, "ci": [0.337, 0.741], "median": 0.252, "winsorized": 0.509},
      "low": {"mean": 0.477, "ci": [0.285, 0.701], "median": 0.183, "winsorized": 0.428}
    },
    "ppl": {
      "high": {"dense": 1.15, "attn": 1.56, "kv": 3.14, "both": 3.92},
      "mid": {"dense": 1.12, "attn": 1.41, "kv": 2.91, "both": 4.14},
      "low": {"dense": 1.11, "attn": 1.39, "kv": 3.61, "both": 4.71}
    },
    "verdict": "FAIL"
  },
  "mvp_v5_random_s025": {
    "status": "completed",
    "n_problems": 50,
    "masking_method": "random",
    "sparsity": 0.25,
    "warnings": [],
    "segments": {"high": 511, "mid": 391, "low": 454},
    "ii": {
      "high": {"mean": 3.905, "ci": [0.980, 6.339], "median": 3.002, "winsorized": 4.708},
      "mid": {"mean": 7.949, "ci": [4.670, 11.867], "median": 2.985, "winsorized": 6.353},
      "low": {"mean": 3.911, "ci": [2.707, 5.236], "median": 2.915, "winsorized": 3.858}
    },
    "ppl": {
      "high": {"dense": 1.15, "attn": 8.66, "kv": 6.39, "both": 17.06},
      "mid": {"dense": 1.12, "attn": 2.62, "kv": 6.11, "both": 15.38},
      "low": {"dense": 1.11, "attn": 5.15, "kv": 9.07, "both": 29.32}
    },
    "verdict": "FAIL"
  },
  "comparison_conclusion": {
    "sign_reversal": false,
    "importance_vs_random": "importance worse in low-sparsity phases, better in high-sparsity phases only",
    "overall": "negative — importance metric ineffective, no strategy-dependent II reversal"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mvp_v5_random_s015": {
      "status": "completed",
      "n_problems": 50,
      "masking_method": "random",
      "sparsity": 0.15,
      "warnings": [],
      "segments": {
        "high": 511,
        "mid": 391,
        "low": 454
      },
      "ii": {
        "high": {
          "mean": 0.456,
          "ci": [
            0.119,
            0.767
          ],
          "median": 0.161,
          "winsorized": 0.538
        },
        "mid": {
          "mean": 0.513,
          "ci": [
            0.337,
            0.741
          ],
          "median": 0.252,
          "winsorized": 0.509
        },
        "low": {
          "mean": 0.477,
          "ci": [
            0.285,
            0.701
          ],
          "median": 0.183,
          "winsorized": 0.428
        }
      },
      "ppl": {
        "high": {
          "dense": 1.15,
          "attn": 1.56,
          "kv": 3.14,
          "both": 3.92
        },
        "mid": {
          "dense": 1.12,
          "attn": 1.41,
          "kv": 2.91,
          "both": 4.14
        },
        "low": {
          "dense": 1.11,
          "attn": 1.39,
          "kv": 3.61,
          "both": 4.71
        }
      },
      "verdict": "FAIL"
    },
    "mvp_v5_random_s025": {
      "status": "completed",
      "n_problems": 50,
      "masking_method": "random",
      "sparsity": 0.25,
      "warnings": [],
      "segments": {
        "high": 511,
        "mid": 391,
        "low": 454
      },
      "ii": {
        "high": {
          "mean": 3.905,
          "ci": [
            0.98,
            6.339
          ],
          "median": 3.002,
          "winsorized": 4.708
        },
        "mid": {
          "mean": 7.949,
          "ci": [
            4.67,
            11.867
          ],
          "median": 2.985,
          "winsorized": 6.353
        },
        "low": {
          "mean": 3.911,
          "ci": [
            2.707,
            5.236
          ],
          "median": 2.915,
          "winsorized": 3.858
        }
      },
      "ppl": {
        "high": {
          "dense": 1.15,
          "attn": 8.66,
          "kv": 6.39,
          "both": 17.06
        },
        "mid": {
          "dense": 1.12,
          "attn": 2.62,
          "kv": 6.11,
          "both": 15.38
        },
        "low": {
          "dense": 1.11,
          "attn": 5.15,
          "kv": 9.07,
          "both": 29.32
        }
      },
      "verdict": "FAIL"
    },
    "comparison_conclusion": {
      "sign_reversal": false,
      "importance_vs_random": "importance worse in low-sparsity phases, better in high-sparsity phases only",
      "overall": "negative — importance metric ineffective, no strategy-dependent II reversal"
    }
  }
}
```

</details>

---
