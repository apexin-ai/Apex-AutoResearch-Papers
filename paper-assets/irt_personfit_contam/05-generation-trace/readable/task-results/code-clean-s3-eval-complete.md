# code clean s3 eval complete

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_clean-s3-eval-complete_20260520T194758_result.json`
- **Structured JSON:** [`d4f36c3ab8a65e365f66.json`](../../sessions/d4/d4f36c3ab8a65e365f66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整产出：

---

## 1. Checkpoint 文件列表（训练完成证明）

```
checkpoints/clean_s3/
├── adapter_model.safetensors  (20MB)
├── adapter_config.json
├── training_args.bin
├── tokenizer.json / tokenizer_config.json
├── chat_template.jinja / README.md
├── checkpoint-313/
├── checkpoint-626/
└── checkpoint-939/
```

## 2. clean_s3 Eval 数值

| 指标 | 值 |
|------|------|
| lz* | **8.0806** |
| accuracy | **0.6783** |
| theta_mle | **-0.1068** |

## 3. Cohen's d 对比表（n=2 vs n=3）

**Clean seeds:**

| Seed | lz* | accuracy | theta_mle |
|------|------|----------|-----------|
| s1 | 8.0101 | 0.6787 | -0.0987 |
| s2 | 5.9440 | 0.6789 | -0.0842 |
| s3 | 8.0806 | 0.6783 | -0.1068 |

**Baseline:**

| | mean | std |
|---|------|-----|
| n=2 | 6.9771 | 1.4609 |
| n=3 | 7.3449 | 1.2137 |

**Cohen's d:**

| Condition | lz* | D_n2 | d_n2 | D_n3 | d_n3 |
|-----------|------|------|------|------|------|
| contam_15 | 3.0046 | -3.9725 | **-2.72** | -4.3403 | **-3.58** |
| contam_50 | 5.4480 | -1.5291 | **-1.05** | -1.8969 | **-1.56** |

## 4. cohens_d_3seeds.json 完整 JSON

```json
{
  "clean_seeds": {
    "s1": {
      "lz_star": 8.01009041187934,
      "accuracy": 0.6786782509614016,
      "theta_mle": -0.0986527567242099
    },
    "s2": {
      "lz_star": 5.944047910541453,
      "accuracy": 0.6788918957413473,
      "theta_mle": -0.08419128365675109
    },
    "s3": {
      "lz_star": 8.080590398603904,
      "accuracy": 0.6782509614015098,
      "theta_mle": -0.10680139600711859
    }
  },
  "baseline": {
    "n2": {
      "mean": 6.977069161210396,
      "std": 1.4609126629156362
    },
    "n3": {
      "mean": 7.3449095736749,
      "std": 1.2136937881771472
    }
  },
  "cohens_d": {
    "contam_15": {
      "lz_star": 3.0045964353509347,
      "accuracy": 0.7310212220481412,
      "delta_n2": -3.9724727258594617,
      "d_n2": -2.7191719441539686,
      "delta_n3": -4.340313138323966,
      "d_n3": -3.576118771146307
    },
    "contam_50": {
      "lz_star": 5.448014241389145,
      "accuracy": 0.7643498077196981,
      "delta_n2": -1.5290549198212515,
      "d_n2": -1.0466436212344272,
      "delta_n3": -1.8968953322857551,
      "d_n3": -1.562910967135056
    }
  }
}
```

加入 s3 后 baseline std 从 1.46 降到 1.21（s3 的 lz*=8.08 与 s1=8.01 接近，远高于 s2=5.94）。contam_15 的 Cohen's d 从 n=2 的 -2.72 扩大到 n=3 的 -3.58；contam_50 从 -1.05 扩大到 -1.56。两个 contamination 条件的效应量在 n=3 下均更显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "clean_seeds": {
      "s1": {
        "lz_star": 8.01009041187934,
        "accuracy": 0.6786782509614016,
        "theta_mle": -0.0986527567242099
      },
      "s2": {
        "lz_star": 5.944047910541453,
        "accuracy": 0.6788918957413473,
        "theta_mle": -0.08419128365675109
      },
      "s3": {
        "lz_star": 8.080590398603904,
        "accuracy": 0.6782509614015098,
        "theta_mle": -0.10680139600711859
      }
    },
    "baseline": {
      "n2": {
        "mean": 6.977069161210396,
        "std": 1.4609126629156362
      },
      "n3": {
        "mean": 7.3449095736749,
        "std": 1.2136937881771472
      }
    },
    "cohens_d": {
      "contam_15": {
        "lz_star": 3.0045964353509347,
        "accuracy": 0.7310212220481412,
        "delta_n2": -3.9724727258594617,
        "d_n2": -2.7191719441539686,
        "delta_n3": -4.340313138323966,
        "d_n3": -3.576118771146307
      },
      "contam_50": {
        "lz_star": 5.448014241389145,
        "accuracy": 0.7643498077196981,
        "delta_n2": -1.5290549198212515,
        "d_n2": -1.0466436212344272,
        "delta_n3": -1.8968953322857551,
        "d_n3": -1.562910967135056
      }
    }
  }
}
```

</details>

---
