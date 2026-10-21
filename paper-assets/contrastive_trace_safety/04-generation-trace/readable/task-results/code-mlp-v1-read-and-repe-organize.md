# code mlp v1 read and repe organize

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mlp_v1_read_and_repe_organize_20260517T131926_result.json`
- **Structured JSON:** [`732ebdff2408a756c967.json`](../../sessions/73/732ebdff2408a756c967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

---

## 任务 A: MLP v1 per-model JSON (K=5 即 W=5)

### results_r1_8b.json
```json
{
  "r1_8b": {
    "W=1": {"bal_acc": 0.8062, "precision": 0.6461, "pre_cp_fpr": 0.1366, "coverage": 0.7674, "lead_mean": 14.27, "n_epochs": 11},
    "W=3": {"bal_acc": 0.8102, "precision": 0.706,  "pre_cp_fpr": 0.0999, "coverage": 0.7209, "lead_mean": 9.71,  "n_epochs": 11},
    "W=5": {"bal_acc": 0.8426, "precision": 0.5953, "pre_cp_fpr": 0.2005, "coverage": 0.8837, "lead_mean": 12.89, "n_epochs": 11},
    "W=10":{"bal_acc": 0.846,  "precision": 0.5922, "pre_cp_fpr": 0.206,  "coverage": 0.8837, "lead_mean": 13.29, "n_epochs": 11}
  }
}
```

### results_r1_32b.json
```json
{
  "r1_32b": {
    "W=1": {"bal_acc": 0.6528, "precision": 0.4881, "pre_cp_fpr": 0.3593, "coverage": 0.75,  "lead_mean": 13.33, "n_epochs": 17},
    "W=3": {"bal_acc": 0.7126, "precision": 0.5849, "pre_cp_fpr": 0.2451, "coverage": 0.8,   "lead_mean": 9.12,  "n_epochs": 18},
    "W=5": {"bal_acc": 0.7013, "precision": 0.5605, "pre_cp_fpr": 0.273,  "coverage": 0.8,   "lead_mean": 8.12,  "n_epochs": 13},
    "W=10":{"bal_acc": 0.6883, "precision": 0.524,  "pre_cp_fpr": 0.3315, "coverage": 0.75,  "lead_mean": 10.33, "n_epochs": 16}
  }
}
```

### results_qwq_32b.json
```json
{
  "qwq_32b": {
    "W=1": {"bal_acc": 0.6455, "precision": 0.3775, "pre_cp_fpr": 0.5407, "coverage": 0.8421, "lead_mean": 27.81, "n_epochs": 13},
    "W=3": {"bal_acc": 0.6587, "precision": 0.3888, "pre_cp_fpr": 0.5176, "coverage": 0.8421, "lead_mean": 25.94, "n_epochs": 14},
    "W=5": {"bal_acc": 0.604,  "precision": 0.3389, "pre_cp_fpr": 0.6924, "coverage": 0.8421, "lead_mean": 33.19, "n_epochs": 14},
    "W=10":{"bal_acc": 0.6983, "precision": 0.4317, "pre_cp_fpr": 0.4282, "coverage": 0.8421, "lead_mean": 22.94, "n_epochs": 16}
  }
}
```

### results_ot_7b.json
```json
{
  "ot_7b": {
    "W=1": {"bal_acc": 0.7302, "precision": 0.4562, "pre_cp_fpr": 0.1648, "coverage": 0.766,  "lead_mean": 32.19, "n_epochs": 11},
    "W=3": {"bal_acc": 0.7467, "precision": 0.3432, "pre_cp_fpr": 0.3619, "coverage": 0.8723, "lead_mean": 41.22, "n_epochs": 11},
    "W=5": {"bal_acc": 0.7462, "precision": 0.4772, "pre_cp_fpr": 0.1574, "coverage": 0.6596, "lead_mean": 33.81, "n_epochs": 11},
    "W=10":{"bal_acc": 0.747,  "precision": 0.3289, "pre_cp_fpr": 0.4061, "coverage": 0.9149, "lead_mean": 44.79, "n_epochs": 11}
  }
}
```

---

## 任务 B: RepE 文件已移动

`results_repe_direction.json` → `artifacts/exp_r3_repe_direction/results.json` ✓

```json
{
  "r1-8b":  {"bal_acc": 0.7491, "precision": 0.516,  "pre_cp_fpr": 0.2264, "coverage": 0.3953, "lead_mean": 9.7,  "direction_layer": 2},
  "r1-32b": {"bal_acc": 0.6707, "precision": 0.5538, "pre_cp_fpr": 0.2423, "coverage": 0.45,   "lead_mean": 6.3,  "direction_layer": 10},
  "qwq-32b":{"bal_acc": 0.6661, "precision": 0.4193, "pre_cp_fpr": 0.3997, "coverage": 0.7368, "lead_mean": 13.4, "direction_layer": 2},
  "ot-7b":  {"bal_acc": 0.718,  "precision": 0.3733, "pre_cp_fpr": 0.2573, "coverage": 0.5319, "lead_mean": 26.1, "direction_layer": 16}
}
```

注意 v1 的 coverage 值各模型各 W 不同（不像 v2 bug 全为 1.0），数据正常。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "r1-8b": {
      "bal_acc": 0.7491,
      "precision": 0.516,
      "pre_cp_fpr": 0.2264,
      "coverage": 0.3953,
      "lead_mean": 9.7,
      "direction_layer": 2
    },
    "r1-32b": {
      "bal_acc": 0.6707,
      "precision": 0.5538,
      "pre_cp_fpr": 0.2423,
      "coverage": 0.45,
      "lead_mean": 6.3,
      "direction_layer": 10
    },
    "qwq-32b": {
      "bal_acc": 0.6661,
      "precision": 0.4193,
      "pre_cp_fpr": 0.3997,
      "coverage": 0.7368,
      "lead_mean": 13.4,
      "direction_layer": 2
    },
    "ot-7b": {
      "bal_acc": 0.718,
      "precision": 0.3733,
      "pre_cp_fpr": 0.2573,
      "coverage": 0.5319,
      "lead_mean": 26.1,
      "direction_layer": 16
    }
  }
}
```

</details>

---
