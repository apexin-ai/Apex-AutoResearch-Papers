# research check simple inst probe 749462

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_simple_inst_probe_749462_20260516T235330_result.json`
- **Structured JSON:** [`adb5478d500b8e8c8adb.json`](../../sessions/ad/adb5478d500b8e8c8adb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已完成，结果如下：

```json
{
  "method": "Goal classification with Linear probe (PCA-256 + LogisticRegression)",
  "purpose": "Test instruction-visual fusion: last_preaction should outperform image_mean if instruction is utilized",
  "pca_dim": 256,
  "conditions": {
    "trained_image_mean": {
      "L0":  {"acc": 0.9293, "f1": 0.9164},
      "L4":  {"acc": 0.9295, "f1": 0.9166},
      "L8":  {"acc": 0.9311, "f1": 0.9185},
      "L12": {"acc": 0.9357, "f1": 0.9237},
      "L16": {"acc": 0.9408, "f1": 0.9301},
      "L20": {"acc": 0.9401, "f1": 0.9289},
      "L24": {"acc": 0.9397, "f1": 0.9285},
      "L28": {"acc": 0.9430, "f1": 0.9323},
      "L32": {"acc": 0.9441, "f1": 0.9331}
    },
    "trained_last_preaction": {
      "L0":  {"acc": 0.1602, "f1": 0.0276},
      "L4":  {"acc": 1.0, "f1": 1.0},
      "L8":  {"acc": 1.0, "f1": 1.0},
      "L12": {"acc": 1.0, "f1": 1.0},
      "L16": {"acc": 1.0, "f1": 1.0},
      "L20": {"acc": 1.0, "f1": 1.0},
      "L24": {"acc": 1.0, "f1": 1.0},
      "L28": {"acc": 1.0, "f1": 1.0},
      "L32": {"acc": 1.0, "f1": 1.0}
    },
    "untrained_image_mean": {
      "L0":  {"acc": 0.9293, "f1": 0.9164},
      "L4":  {"acc": 0.9357, "f1": 0.9239},
      "L8":  {"acc": 0.9387, "f1": 0.9280},
      "L12": {"acc": 0.9346, "f1": 0.9228},
      "L16": {"acc": 0.9310, "f1": 0.9186},
      "L20": {"acc": 0.9288, "f1": 0.9157},
      "L24": {"acc": 0.9253, "f1": 0.9114},
      "L28": {"acc": 0.9278, "f1": 0.9147},
      "L32": {"acc": 0.9272, "f1": 0.9140}
    },
    "untrained_last_preaction": {
      "L0":  {"acc": 0.1602, "f1": 0.0276},
      "L4":  {"acc": 1.0, "f1": 1.0},
      "L8":  {"acc": 0.9999, "f1": 0.9999},
      "L12": {"acc": 0.9999, "f1": 0.9999},
      "L16": {"acc": 0.9998, "f1": 0.9997},
      "L20": {"acc": 0.9998, "f1": 0.9998},
      "L24": {"acc": 0.9999, "f1": 0.9999},
      "L28": {"acc": 0.9997, "f1": 0.9996},
      "L32": {"acc": 0.9995, "f1": 0.9994}
    },
    "dino_cls": {"acc": 0.9022, "f1": 0.8832}
  },
  "key_comparison": {
    "trained_image_mean_best":       {"layer": "L32", "acc": 0.9441, "f1": 0.9331},
    "trained_last_preaction_best":    {"layer": "L4",  "acc": 1.0,    "f1": 1.0},
    "untrained_image_mean_best":     {"layer": "L8",  "acc": 0.9387, "f1": 0.9280},
    "untrained_last_preaction_best":  {"layer": "L4",  "acc": 1.0,    "f1": 1.0},
    "trained_delta_lastpre_minus_imgmean": 0.0559,
    "untrained_delta_lastpre_minus_imgmean": 0.0613,
    "dino": {"acc": 0.9022, "f1": 0.8832}
  }
}
```

**关键发现：**

| Condition | Best Acc | Notes |
|-----------|----------|-------|
| trained_last_preaction | 1.0 (L4+) | 完美分类 |
| untrained_last_preaction | 1.0 (L4), ~0.9995+ (L8-32) | 也接近完美 |
| trained_image_mean | 0.9441 (L32) | 纯视觉基线 |
| untrained_image_mean | 0.9387 (L8) | 纯视觉基线 |
| dino_cls | 0.9022 | 外部视觉基线 |

`last_preaction` 在 trained 和 untrained 模型上都达到近乎完美的 goal classification 准确率，而 `image_mean`（纯视觉 tokens）只有 ~0.94。但 trained vs untrained 的 delta 几乎相同（0.0559 vs 0.0613），untrained 模型的 last_preaction 同样能完美分类 goal，说明这个位置的 instruction 信息在训练前就已经可线性解码，训练并未显著增强 instruction-conditional 的 fusion 信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "method": "Goal classification with Linear probe (PCA-256 + LogisticRegression)",
    "purpose": "Test instruction-visual fusion: last_preaction should outperform image_mean if instruction is utilized",
    "pca_dim": 256,
    "conditions": {
      "trained_image_mean": {
        "L0": {
          "acc": 0.9293,
          "f1": 0.9164
        },
        "L4": {
          "acc": 0.9295,
          "f1": 0.9166
        },
        "L8": {
          "acc": 0.9311,
          "f1": 0.9185
        },
        "L12": {
          "acc": 0.9357,
          "f1": 0.9237
        },
        "L16": {
          "acc": 0.9408,
          "f1": 0.9301
        },
        "L20": {
          "acc": 0.9401,
          "f1": 0.9289
        },
        "L24": {
          "acc": 0.9397,
          "f1": 0.9285
        },
        "L28": {
          "acc": 0.943,
          "f1": 0.9323
        },
        "L32": {
          "acc": 0.9441,
          "f1": 0.9331
        }
      },
      "trained_last_preaction": {
        "L0": {
          "acc": 0.1602,
          "f1": 0.0276
        },
        "L4": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L8": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L12": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L16": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L20": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L24": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L28": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L32": {
          "acc": 1.0,
          "f1": 1.0
        }
      },
      "untrained_image_mean": {
        "L0": {
          "acc": 0.9293,
          "f1": 0.9164
        },
        "L4": {
          "acc": 0.9357,
          "f1": 0.9239
        },
        "L8": {
          "acc": 0.9387,
          "f1": 0.928
        },
        "L12": {
          "acc": 0.9346,
          "f1": 0.9228
        },
        "L16": {
          "acc": 0.931,
          "f1": 0.9186
        },
        "L20": {
          "acc": 0.9288,
          "f1": 0.9157
        },
        "L24": {
          "acc": 0.9253,
          "f1": 0.9114
        },
        "L28": {
          "acc": 0.9278,
          "f1": 0.9147
        },
        "L32": {
          "acc": 0.9272,
          "f1": 0.914
        }
      },
      "untrained_last_preaction": {
        "L0": {
          "acc": 0.1602,
          "f1": 0.0276
        },
        "L4": {
          "acc": 1.0,
          "f1": 1.0
        },
        "L8": {
          "acc": 0.9999,
          "f1": 0.9999
        },
        "L12": {
          "acc": 0.9999,
          "f1": 0.9999
        },
        "L16": {
          "acc": 0.9998,
          "f1": 0.9997
        },
        "L20": {
          "acc": 0.9998,
          "f1": 0.9998
        },
        "L24": {
          "acc": 0.9999,
          "f1": 0.9999
        },
        "L28": {
          "acc": 0.9997,
          "f1": 0.9996
        },
        "L32": {
          "acc": 0.9995,
          "f1": 0.9994
        }
      },
      "dino_cls": {
        "acc": 0.9022,
        "f1": 0.8832
      }
    },
    "key_comparison": {
      "trained_image_mean_best": {
        "layer": "L32",
        "acc": 0.9441,
        "f1": 0.9331
      },
      "trained_last_preaction_best": {
        "layer": "L4",
        "acc": 1.0,
        "f1": 1.0
      },
      "untrained_image_mean_best": {
        "layer": "L8",
        "acc": 0.9387,
        "f1": 0.928
      },
      "untrained_last_preaction_best": {
        "layer": "L4",
        "acc": 1.0,
        "f1": 1.0
      },
      "trained_delta_lastpre_minus_imgmean": 0.0559,
      "untrained_delta_lastpre_minus_imgmean": 0.0613,
      "dino": {
        "acc": 0.9022,
        "f1": 0.8832
      }
    }
  }
}
```

</details>

---
