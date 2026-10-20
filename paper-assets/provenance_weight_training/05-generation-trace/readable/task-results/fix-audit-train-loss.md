# fix audit train loss

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_audit_train_loss_20260514T144155_result.json`
- **Structured JSON:** [`1567f1a3fc6816670b75.json`](../../sessions/15/1567f1a3fc6816670b75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

trainer_state.json 在 checkpoint 中没有 train_loss 聚合值。但从 grep 结果已经拿到了 batch log 中的三个 summary：

- b=0.5 (line 22609): `train_loss: 9.597948909411366`
- b=1.0 (line 45222): `train_loss: 10.223488691574664`
- b=1.5 (line 67835): `train_loss: 10.485242410153809`

所有数据已收集完毕。审计结果：

## 审计表

| exp_id | 脚本提取 train_loss | registry train_loss | 匹配 |
|--------|---------------------|---------------------|------|
| grid_b0_5_seed123 | 9.6009 | 9.601 | YES |
| grid_b1_0_seed123 | 10.2183 | 10.218 | YES |
| grid_b1_5_seed123 | 10.4776 | 10.4776 | YES |
| grid_b2_0_seed123 | 10.6104 | 10.610373077442583 | YES |
| grid_b3_0_seed123 | 10.7422 | 10.7422 | YES |
| uniform_seed42 | 7.3104 | 7.3104 | YES |
| uniform_seed123 | 7.3121 | 7.3121 | YES |
| uniform_seed456 | 7.2895 | 7.2895 | YES |
| adaptive_seed42 | 9.2665 | 9.2665 | YES |
| adaptive_seed123 | 9.2665 | 9.2665 | YES |
| adaptive_seed456 | 9.2354 | 9.2354 | YES |
| grid_b0_5_seed42 | 9.5979 | 2.531 (KNOWN WRONG) | **NO** |
| grid_b1_0_seed42 | 10.2235 | (missing) | **NO** |
| grid_b1_5_seed42 | 10.4852 | (missing) | **NO** |

**结论**：11 个独立实验的 registry train_loss 值全部正确（精度匹配到 log 中的摘要值）。只有 batch 实验的 3 个子实验有问题：

- `grid_b0_5_seed42`：registry 中的 2.531 确实是错的（正确值 9.5979，之前误取了 weighting/ess）
- `grid_b1_0_seed42` 和 `grid_b1_5_seed42`：registry 中缺失

JSON 格式审计结果：

```json
{
  "audit_date": "2026-05-14",
  "results": [
    {"exp_id": "grid_b0_5_seed123", "extracted_train_loss": 9.600899700256678, "registry_train_loss": 9.601, "match": true, "source": "log_file"},
    {"exp_id": "grid_b1_0_seed123", "extracted_train_loss": 10.218338532114194, "registry_train_loss": 10.218, "match": true, "source": "log_file"},
    {"exp_id": "grid_b1_5_seed123", "extracted_train_loss": 10.477614773271046, "registry_train_loss": 10.4776, "match": true, "source": "log_file"},
    {"exp_id": "grid_b2_0_seed123", "extracted_train_loss": 10.610373077442583, "registry_train_loss": 10.610373077442583, "match": true, "source": "log_file"},
    {"exp_id": "grid_b3_0_seed123", "extracted_train_loss": 10.742213469693919, "registry_train_loss": 10.7422, "match": true, "source": "log_file"},
    {"exp_id": "uniform_seed42", "extracted_train_loss": 7.310443773477483, "registry_train_loss": 7.3104, "match": true, "source": "log_file"},
    {"exp_id": "uniform_seed123", "extracted_train_loss": 7.31207558664556, "registry_train_loss": 7.3121, "match": true, "source": "log_file"},
    {"exp_id": "uniform_seed456", "extracted_train_loss": 7.289453257073657, "registry_train_loss": 7.2895, "match": true, "source": "log_file"},
    {"exp_id": "adaptive_seed42", "extracted_train_loss": 9.26652745811466, "registry_train_loss": 9.2665, "match": true, "source": "log_file"},
    {"exp_id": "adaptive_seed123", "extracted_train_loss": 9.266461906014321, "registry_train_loss": 9.2665, "match": true, "source": "log_file"},
    {"exp_id": "adaptive_seed456", "extracted_train_loss": 9.235448541317771, "registry_train_loss": 9.2354, "match": true, "source": "log_file"},
    {"exp_id": "grid_b0_5_seed42", "extracted_train_loss": 9.597948909411366, "registry_train_loss": 2.531, "match": false, "source": "batch_log_grep", "note": "registry value was weighting/ess, not train_loss"},
    {"exp_id": "grid_b1_0_seed42", "extracted_train_loss": 10.223488691574664, "registry_train_loss": null, "match": false, "source": "batch_log_grep", "note": "missing from registry"},
    {"exp_id": "grid_b1_5_seed42", "extracted_train_loss": 10.485242410153809, "registry_train_loss": null, "match": false, "source": "batch_log_grep", "note": "missing from registry"}
  ],
  "summary": {
    "total_experiments": 14,
    "matching": 11,
    "mismatched": 3,
    "bug_confirmed": "only grid_b_seed42_batch sub-experiments affected; all independent experiments had correct train_loss in registry"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "audit_date": "2026-05-14",
    "results": [
      {
        "exp_id": "grid_b0_5_seed123",
        "extracted_train_loss": 9.600899700256678,
        "registry_train_loss": 9.601,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "grid_b1_0_seed123",
        "extracted_train_loss": 10.218338532114194,
        "registry_train_loss": 10.218,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "grid_b1_5_seed123",
        "extracted_train_loss": 10.477614773271046,
        "registry_train_loss": 10.4776,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "grid_b2_0_seed123",
        "extracted_train_loss": 10.610373077442583,
        "registry_train_loss": 10.610373077442583,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "grid_b3_0_seed123",
        "extracted_train_loss": 10.742213469693919,
        "registry_train_loss": 10.7422,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "uniform_seed42",
        "extracted_train_loss": 7.310443773477483,
        "registry_train_loss": 7.3104,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "uniform_seed123",
        "extracted_train_loss": 7.31207558664556,
        "registry_train_loss": 7.3121,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "uniform_seed456",
        "extracted_train_loss": 7.289453257073657,
        "registry_train_loss": 7.2895,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "adaptive_seed42",
        "extracted_train_loss": 9.26652745811466,
        "registry_train_loss": 9.2665,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "adaptive_seed123",
        "extracted_train_loss": 9.266461906014321,
        "registry_train_loss": 9.2665,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "adaptive_seed456",
        "extracted_train_loss": 9.235448541317771,
        "registry_train_loss": 9.2354,
        "match": true,
        "source": "log_file"
      },
      {
        "exp_id": "grid_b0_5_seed42",
        "extracted_train_loss": 9.597948909411366,
        "registry_train_loss": 2.531,
        "match": false,
        "source": "batch_log_grep",
        "note": "registry value was weighting/ess, not train_loss"
      },
      {
        "exp_id": "grid_b1_0_seed42",
        "extracted_train_loss": 10.223488691574664,
        "registry_train_loss": null,
        "match": false,
        "source": "batch_log_grep",
        "note": "missing from registry"
      },
      {
        "exp_id": "grid_b1_5_seed42",
        "extracted_train_loss": 10.485242410153809,
        "registry_train_loss": null,
        "match": false,
        "source": "batch_log_grep",
        "note": "missing from registry"
      }
    ],
    "summary": {
      "total_experiments": 14,
      "matching": 11,
      "mismatched": 3,
      "bug_confirmed": "only grid_b_seed42_batch sub-experiments affected; all independent experiments had correct train_loss in registry"
    }
  }
}
```

</details>

---
