# analysis self bleu distinct n v2

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_self-bleu-distinct-n-v2_20260517T121931_result.json`
- **Structured JSON:** [`663201b84332006a0de7.json`](../../sessions/66/663201b84332006a0de7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

```json
{
  "lora_nocuration": {
    "gen0": {"self_bleu4": 0.010658, "distinct1": 0.167971, "distinct2": 0.58048, "distinct3": 0.830927, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.013553, "distinct1": 0.158274, "distinct2": 0.545327, "distinct3": 0.788992, "n_samples": 2000},
    "gen2": {"self_bleu4": 0.013239, "distinct1": 0.156063, "distinct2": 0.534274, "distinct3": 0.77619, "n_samples": 1999}
  },
  "lora_k4_curated": {
    "gen0": {"self_bleu4": 0.011577, "distinct1": 0.166641, "distinct2": 0.581761, "distinct3": 0.835073, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.016021, "distinct1": 0.162504, "distinct2": 0.56033, "distinct3": 0.808212, "n_samples": 1999},
    "gen2": {"self_bleu4": 0.013722, "distinct1": 0.157203, "distinct2": 0.545915, "distinct3": 0.792589, "n_samples": 2000}
  },
  "lora_k8": {
    "gen0": {"self_bleu4": 0.013803, "distinct1": 0.166571, "distinct2": 0.57914, "distinct3": 0.831479, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.014396, "distinct1": 0.163746, "distinct2": 0.561916, "distinct3": 0.810475, "n_samples": 2000},
    "gen2": {"self_bleu4": 0.014906, "distinct1": 0.16214, "distinct2": 0.555156, "distinct3": 0.802238, "n_samples": 1999}
  },
  "fullft_k4_lr5e6": {
    "gen0": {"self_bleu4": 0.010558, "distinct1": 0.166196, "distinct2": 0.578668, "distinct3": 0.831866, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.014446, "distinct1": 0.164886, "distinct2": 0.568535, "distinct3": 0.818612, "n_samples": 2000},
    "gen2": {"self_bleu4": 0.015789, "distinct1": 0.161983, "distinct2": 0.556416, "distinct3": 0.802601, "n_samples": 2000}
  },
  "fullft_nocuration_lr5e6": {
    "gen0": {"self_bleu4": 0.013274, "distinct1": 0.168767, "distinct2": 0.581981, "distinct3": 0.833281, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.013286, "distinct1": 0.164622, "distinct2": 0.563151, "distinct3": 0.811136, "n_samples": 2000},
    "gen2": {"self_bleu4": 0.012084, "distinct1": 0.162106, "distinct2": 0.550486, "distinct3": 0.795075, "n_samples": 2000}
  },
  "fullft_k4_lr2e5": {
    "gen0": {"self_bleu4": 0.013122, "distinct1": 0.167555, "distinct2": 0.580446, "distinct3": 0.832629, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.01174, "distinct1": 0.162012, "distinct2": 0.562131, "distinct3": 0.811349, "n_samples": 2000},
    "gen2": {"self_bleu4": 0.010085, "distinct1": 0.160012, "distinct2": 0.55686, "distinct3": 0.806935, "n_samples": 2000}
  },
  "fullft_nocuration_lr2e5": {
    "gen0": {"self_bleu4": 0.013275, "distinct1": 0.167256, "distinct2": 0.580208, "distinct3": 0.831764, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.013848, "distinct1": 0.161574, "distinct2": 0.556013, "distinct3": 0.800041, "n_samples": 1999},
    "gen2": {"self_bleu4": 0.014063, "distinct1": 0.156924, "distinct2": 0.541479, "distinct3": 0.782985, "n_samples": 2000}
  },
  "fullft_k16_lr2e5": {
    "gen0": {"self_bleu4": 0.012026, "distinct1": 0.169608, "distinct2": 0.581423, "distinct3": 0.832187, "n_samples": 2000},
    "gen1": {"self_bleu4": 0.015577, "distinct1": 0.165348, "distinct2": 0.570397, "distinct3": 0.819285, "n_samples": 1999},
    "gen2": {"self_bleu4": 0.015959, "distinct1": 0.162784, "distinct2": 0.561889, "distinct3": 0.810882, "n_samples": 1999}
  }
}
```

**产出**：
- 脚本：`/root/autodl-tmp/carr/analysis/compute_diversity_metrics.py`
- 结果：`/root/autodl-tmp/carr/analysis/diversity_metrics_summary.json`

**关键观察**：
- 所有配置 self-BLEU-4 都很低（0.01-0.016），说明生成文本总体多样性不错
- 所有配置 distinct-n 随代数递减（gen0 > gen1 > gen2），确认 iterative training 导致多样性下降
- `fullft_k4_lr2e5` 的 self-BLEU 随代数反而下降（0.013→0.012→0.010），是唯一呈现该趋势的配置
- `fullft_k16_lr2e5` 和 `fullft_k4_lr5e6` 的 distinct-n 下降最慢，保持了较好的多样性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "lora_nocuration": {
      "gen0": {
        "self_bleu4": 0.010658,
        "distinct1": 0.167971,
        "distinct2": 0.58048,
        "distinct3": 0.830927,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.013553,
        "distinct1": 0.158274,
        "distinct2": 0.545327,
        "distinct3": 0.788992,
        "n_samples": 2000
      },
      "gen2": {
        "self_bleu4": 0.013239,
        "distinct1": 0.156063,
        "distinct2": 0.534274,
        "distinct3": 0.77619,
        "n_samples": 1999
      }
    },
    "lora_k4_curated": {
      "gen0": {
        "self_bleu4": 0.011577,
        "distinct1": 0.166641,
        "distinct2": 0.581761,
        "distinct3": 0.835073,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.016021,
        "distinct1": 0.162504,
        "distinct2": 0.56033,
        "distinct3": 0.808212,
        "n_samples": 1999
      },
      "gen2": {
        "self_bleu4": 0.013722,
        "distinct1": 0.157203,
        "distinct2": 0.545915,
        "distinct3": 0.792589,
        "n_samples": 2000
      }
    },
    "lora_k8": {
      "gen0": {
        "self_bleu4": 0.013803,
        "distinct1": 0.166571,
        "distinct2": 0.57914,
        "distinct3": 0.831479,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.014396,
        "distinct1": 0.163746,
        "distinct2": 0.561916,
        "distinct3": 0.810475,
        "n_samples": 2000
      },
      "gen2": {
        "self_bleu4": 0.014906,
        "distinct1": 0.16214,
        "distinct2": 0.555156,
        "distinct3": 0.802238,
        "n_samples": 1999
      }
    },
    "fullft_k4_lr5e6": {
      "gen0": {
        "self_bleu4": 0.010558,
        "distinct1": 0.166196,
        "distinct2": 0.578668,
        "distinct3": 0.831866,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.014446,
        "distinct1": 0.164886,
        "distinct2": 0.568535,
        "distinct3": 0.818612,
        "n_samples": 2000
      },
      "gen2": {
        "self_bleu4": 0.015789,
        "distinct1": 0.161983,
        "distinct2": 0.556416,
        "distinct3": 0.802601,
        "n_samples": 2000
      }
    },
    "fullft_nocuration_lr5e6": {
      "gen0": {
        "self_bleu4": 0.013274,
        "distinct1": 0.168767,
        "distinct2": 0.581981,
        "distinct3": 0.833281,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.013286,
        "distinct1": 0.164622,
        "distinct2": 0.563151,
        "distinct3": 0.811136,
        "n_samples": 2000
      },
      "gen2": {
        "self_bleu4": 0.012084,
        "distinct1": 0.162106,
        "distinct2": 0.550486,
        "distinct3": 0.795075,
        "n_samples": 2000
      }
    },
    "fullft_k4_lr2e5": {
      "gen0": {
        "self_bleu4": 0.013122,
        "distinct1": 0.167555,
        "distinct2": 0.580446,
        "distinct3": 0.832629,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.01174,
        "distinct1": 0.162012,
        "distinct2": 0.562131,
        "distinct3": 0.811349,
        "n_samples": 2000
      },
      "gen2": {
        "self_bleu4": 0.010085,
        "distinct1": 0.160012,
        "distinct2": 0.55686,
        "distinct3": 0.806935,
        "n_samples": 2000
      }
    },
    "fullft_nocuration_lr2e5": {
      "gen0": {
        "self_bleu4": 0.013275,
        "distinct1": 0.167256,
        "distinct2": 0.580208,
        "distinct3": 0.831764,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.013848,
        "distinct1": 0.161574,
        "distinct2": 0.556013,
        "distinct3": 0.800041,
        "n_samples": 1999
      },
      "gen2": {
        "self_bleu4": 0.014063,
        "distinct1": 0.156924,
        "distinct2": 0.541479,
        "distinct3": 0.782985,
        "n_samples": 2000
      }
    },
    "fullft_k16_lr2e5": {
      "gen0": {
        "self_bleu4": 0.012026,
        "distinct1": 0.169608,
        "distinct2": 0.581423,
        "distinct3": 0.832187,
        "n_samples": 2000
      },
      "gen1": {
        "self_bleu4": 0.015577,
        "distinct1": 0.165348,
        "distinct2": 0.570397,
        "distinct3": 0.819285,
        "n_samples": 1999
      },
      "gen2": {
        "self_bleu4": 0.015959,
        "distinct1": 0.162784,
        "distinct2": 0.561889,
        "distinct3": 0.810882,
        "n_samples": 1999
      }
    }
  }
}
```

</details>

---
