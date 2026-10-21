# debug read action trajectory results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_read_action_trajectory_results_20260518T105940_result.json`
- **Structured JSON:** [`4132adb546e1cbf10328.json`](../../sessions/41/4132adb546e1cbf10328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。完整 JSON 结果：

```json
{
  "config": {
    "n_tasks": 5,
    "n_demos_per_task": 10,
    "n_timesteps_per_demo": 50,
    "total_forward_passes": 5000,
    "model": "openvla-7b",
    "ablation": "L1_dominant_24_heads_zeroed",
    "ablated_heads": [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31],
    "unnorm_key": "bridge_orig"
  },
  "main_metrics": {
    "paired_action_mse": {
      "mean": 0.04164548042967141,
      "std": 0.06394581517413622,
      "t_stat": 32.55658746950337,
      "p_value": 3.9875267301509806e-194,
      "cohens_d": 0.6511317493798869
    },
    "per_dim_action_shift": {
      "means": [0.0018907631, 0.0053060349, 0.0076212989, 0.0205921095, 0.0307135648, 0.0338819297, 0.2907168627],
      "stds":  [0.0039457747, 0.0079967289, 0.0085559840, 0.0211583055, 0.0285854749, 0.0377378606, 0.4489490408],
      "dim_names": ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]
    },
    "token_divergence_rate": 0.7230285714285715
  },
  "secondary_metrics": {
    "kl_divergence": {
      "mean": 5.07937479019165,
      "std": 4.961368560791016,
      "per_token_position": [0.2902, 3.0104, 5.9492, 7.4210, 8.9605, 8.4797, 1.4447]
    },
    "mse_vs_gt_baseline": {
      "mean": 0.43176415822445635,
      "std": 0.22077793994025996,
      "note": "OOD, secondary"
    },
    "mse_vs_gt_ablated": {
      "mean": 0.4357406635106642,
      "std": 0.2235285616028443,
      "note": "OOD, secondary"
    },
    "wilcoxon_p": 0.0
  },
  "per_task": {
    "open_the_middle_drawer_of_the_cabinet": {
      "paired_mse": {"mean": 0.02242838, "std": 0.05175720, "t_stat": 9.6800, "p_value": 2.00e-20, "cohens_d": 0.4329},
      "per_dim_shift": {
        "means": [0.001404, 0.004451, 0.006329, 0.019143, 0.030247, 0.030260, 0.152816],
        "stds":  [0.003113, 0.007886, 0.008241, 0.019615, 0.028677, 0.033096, 0.359089]
      },
      "token_divergence_rate": 0.664,
      "kl_divergence": {"mean": 4.5032, "std": 4.8421},
      "n_samples": 500
    },
    "open_the_top_drawer_and_put_the_bowl_inside": {
      "paired_mse": {"mean": 0.04458788, "std": 0.06487046, "t_stat": 15.3539, "p_value": 7.46e-44, "cohens_d": 0.6866},
      "per_dim_shift": {
        "means": [0.001733, 0.005303, 0.007164, 0.020680, 0.034857, 0.034592, 0.311890],
        "stds":  [0.003762, 0.008254, 0.007593, 0.020277, 0.031623, 0.038134, 0.457070]
      },
      "token_divergence_rate": 0.7094,
      "kl_divergence": {"mean": 5.1536, "std": 5.0712},
      "n_samples": 500
    },
    "push_the_plate_to_the_front_of_the_stove": {
      "paired_mse": {"mean": 0.04681500, "std": 0.06645561, "t_stat": 15.7363, "p_value": 1.34e-45, "cohens_d": 0.7038},
      "per_dim_shift": {
        "means": [0.002804, 0.005471, 0.007187, 0.018411, 0.028981, 0.028123, 0.325255],
        "stds":  [0.005730, 0.007560, 0.007359, 0.018760, 0.028137, 0.029492, 0.466581]
      },
      "token_divergence_rate": 0.7386,
      "kl_divergence": {"mean": 5.9725, "std": 5.5687},
      "n_samples": 500
    },
    "put_the_bowl_on_the_plate": {
      "paired_mse": {"mean": 0.04585328, "std": 0.06512121, "t_stat": 15.7289, "p_value": 1.45e-45, "cohens_d": 0.7034},
      "per_dim_shift": {
        "means": [0.001664, 0.005203, 0.007478, 0.020320, 0.028729, 0.035563, 0.325255],
        "stds":  [0.003060, 0.008431, 0.008048, 0.021655, 0.026055, 0.035687, 0.458287]
      },
      "token_divergence_rate": 0.7366,
      "kl_divergence": {"mean": 4.9356, "std": 4.7559},
      "n_samples": 500
    },
    "put_the_bowl_on_the_stove": {
      "paired_mse": {"mean": 0.04854286, "std": 0.06656781, "t_stat": 16.2896, "p_value": 3.76e-48, "cohens_d": 0.7285},
      "per_dim_shift": {
        "means": [0.001849, 0.006102, 0.009948, 0.024407, 0.030753, 0.040872, 0.338369],
        "stds":  [0.003265, 0.007732, 0.010678, 0.024497, 0.027719, 0.048264, 0.466983]
      },
      "token_divergence_rate": 0.7666,
      "kl_divergence": {"mean": 4.8319, "std": 4.3665},
      "n_samples": 500
    }
  }
}
```

日志确认 5000 次前向传播全部完成（746s），汇总指标：
- **Paired MSE**: 0.0416 (p=3.99e-194, Cohen's d=0.651)
- **Token divergence rate**: 72.3%
- **KL divergence**: 5.079
- **MSE vs GT**: baseline 0.4318 vs ablated 0.4357（差异极小）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "config": {
      "n_tasks": 5,
      "n_demos_per_task": 10,
      "n_timesteps_per_demo": 50,
      "total_forward_passes": 5000,
      "model": "openvla-7b",
      "ablation": "L1_dominant_24_heads_zeroed",
      "ablated_heads": [
        0,
        1,
        2,
        4,
        7,
        8,
        10,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        22,
        23,
        25,
        26,
        27,
        29,
        30,
        31
      ],
      "unnorm_key": "bridge_orig"
    },
    "main_metrics": {
      "paired_action_mse": {
        "mean": 0.04164548042967141,
        "std": 0.06394581517413622,
        "t_stat": 32.55658746950337,
        "p_value": 3.9875267301509806e-194,
        "cohens_d": 0.6511317493798869
      },
      "per_dim_action_shift": {
        "means": [
          0.0018907631,
          0.0053060349,
          0.0076212989,
          0.0205921095,
          0.0307135648,
          0.0338819297,
          0.2907168627
        ],
        "stds": [
          0.0039457747,
          0.0079967289,
          0.008555984,
          0.0211583055,
          0.0285854749,
          0.0377378606,
          0.4489490408
        ],
        "dim_names": [
          "dx",
          "dy",
          "dz",
          "rx",
          "ry",
          "rz",
          "gripper"
        ]
      },
      "token_divergence_rate": 0.7230285714285715
    },
    "secondary_metrics": {
      "kl_divergence": {
        "mean": 5.07937479019165,
        "std": 4.961368560791016,
        "per_token_position": [
          0.2902,
          3.0104,
          5.9492,
          7.421,
          8.9605,
          8.4797,
          1.4447
        ]
      },
      "mse_vs_gt_baseline": {
        "mean": 0.43176415822445635,
        "std": 0.22077793994025996,
        "note": "OOD, secondary"
      },
      "mse_vs_gt_ablated": {
        "mean": 0.4357406635106642,
        "std": 0.2235285616028443,
        "note": "OOD, secondary"
      },
      "wilcoxon_p": 0.0
    },
    "per_task": {
      "open_the_middle_drawer_of_the_cabinet": {
        "paired_mse": {
          "mean": 0.02242838,
          "std": 0.0517572,
          "t_stat": 9.68,
          "p_value": 2e-20,
          "cohens_d": 0.4329
        },
        "per_dim_shift": {
          "means": [
            0.001404,
            0.004451,
            0.006329,
            0.019143,
            0.030247,
            0.03026,
            0.152816
          ],
          "stds": [
            0.003113,
            0.007886,
            0.008241,
            0.019615,
            0.028677,
            0.033096,
            0.359089
          ]
        },
        "token_divergence_rate": 0.664,
        "kl_divergence": {
          "mean": 4.5032,
          "std": 4.8421
        },
        "n_samples": 500
      },
      "open_the_top_drawer_and_put_the_bowl_inside": {
        "paired_mse": {
          "mean": 0.04458788,
          "std": 0.06487046,
          "t_stat": 15.3539,
          "p_value": 7.46e-44,
          "cohens_d": 0.6866
        },
        "per_dim_shift": {
          "means": [
            0.001733,
            0.005303,
            0.007164,
            0.02068,
            0.034857,
            0.034592,
            0.31189
          ],
          "stds": [
            0.003762,
            0.008254,
            0.007593,
            0.020277,
            0.031623,
            0.038134,
            0.45707
          ]
        },
        "token_divergence_rate": 0.7094,
        "kl_divergence": {
          "mean": 5.1536,
          "std": 5.0712
        },
        "n_samples": 500
      },
      "push_the_plate_to_the_front_of_the_stove": {
        "paired_mse": {
          "mean": 0.046815,
          "std": 0.06645561,
          "t_stat": 15.7363,
          "p_value": 1.34e-45,
          "cohens_d": 0.7038
        },
        "per_dim_shift": {
          "means": [
            0.002804,
            0.005471,
            0.007187,
            0.018411,
            0.028981,
            0.028123,
            0.325255
          ],
          "stds": [
            0.00573,
            0.00756,
            0.007359,
            0.01876,
            0.028137,
            0.029492,
            0.466581
          ]
        },
        "token_divergence_rate": 0.7386,
        "kl_divergence": {
          "mean": 5.9725,
          "std": 5.5687
        },
        "n_samples": 500
      },
      "put_the_bowl_on_the_plate": {
        "paired_mse": {
          "mean": 0.04585328,
          "std": 0.06512121,
          "t_stat": 15.7289,
          "p_value": 1.45e-45,
          "cohens_d": 0.7034
        },
        "per_dim_shift": {
          "means": [
            0.001664,
            0.005203,
            0.007478,
            0.02032,
            0.028729,
            0.035563,
            0.325255
          ],
          "stds": [
            0.00306,
            0.008431,
            0.008048,
            0.021655,
            0.026055,
            0.035687,
            0.458287
          ]
        },
        "token_divergence_rate": 0.7366,
        "kl_divergence": {
          "mean": 4.9356,
          "std": 4.7559
        },
        "n_samples": 500
      },
      "put_the_bowl_on_the_stove": {
        "paired_mse": {
          "mean": 0.04854286,
          "std": 0.06656781,
          "t_stat": 16.2896,
          "p_value": 3.76e-48,
          "cohens_d": 0.7285
        },
        "per_dim_shift": {
          "means": [
            0.001849,
            0.006102,
            0.009948,
            0.024407,
            0.030753,
            0.040872,
            0.338369
          ],
          "stds": [
            0.003265,
            0.007732,
            0.010678,
            0.024497,
            0.027719,
            0.048264,
            0.466983
          ]
        },
        "token_divergence_rate": 0.7666,
        "kl_divergence": {
          "mean": 4.8319,
          "std": 4.3665
        },
        "n_samples": 500
      }
    }
  }
}
```

</details>

---
