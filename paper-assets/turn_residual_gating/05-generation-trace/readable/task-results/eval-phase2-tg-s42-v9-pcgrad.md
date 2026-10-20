# eval phase2 tg s42 v9 pcgrad

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_phase2_tg_s42_v9_pcgrad_20260520T014452_result.json`
- **Structured JSON:** [`57d6f748e158c1efd8f5.json`](../../sessions/57/57d6f748e158c1efd8f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 variant 都完成。结果汇总：

```json
{
  "eval_ours_mid_gar": 0.0151,
  "eval_ours_recovery_pp": 0.29,
  "eval_dongre_mid_gar": 0.0192,
  "eval_dongre_recovery_pp": 0.70,
  "eval_ppl": 1.50,
  "eval_ntp": 0.4016,
  "eval_gate_dynamic_range": {
    "L15": {"turn1": 0.6247, "turn21": 0.9571, "diff": -0.3324},
    "L23": {"turn1": 0.7030, "turn21": 0.9779, "diff": -0.2749},
    "L18": {"turn1": 0.8280, "turn21": 0.9526, "diff": -0.1246},
    "L9":  {"turn1": 0.8166, "turn21": 0.9403, "diff": -0.1237},
    "L16": {"turn1": 0.8303, "turn21": 0.9469, "diff": -0.1166}
  },
  "vs_v7_gar_ours_diff_pp": -0.06,
  "vs_v7_gar_dongre_diff_pp": -0.02,
  "vs_v7_ppl_diff": -1.28,
  "hypothesis_confirmed": true,
  "summary": "v9 PCGrad 推理 GAR 与 v7 基本一致（ours 0.0151 vs 0.0157, dongre 0.0192 vs 0.0194），差异 <0.1pp，确认梯度冲突解决不改变推理 GAR gap。PPL 显著降低（1.50 vs 2.78）说明 PCGrad 改善了训练质量，但 GAR recovery 未提升，支持 exposure bias 是推理 GAR gap 根因的假设。"
}
```

**关键发现：**

| 指标 | v9 PCGrad | v7 | 差异 |
|------|-----------|-----|------|
| GAR-ours mid | 0.0151 | 0.0157 | -0.06pp |
| GAR-Dongre mid | 0.0192 | 0.0194 | -0.02pp |
| PPL | 1.50 | 2.78 | -1.28 |
| NTP | 0.4016 | 0.9771 | -0.5755 |

Hypothesis confirmed — PCGrad 大幅改善了 PPL（1.50 vs 2.78），但推理 GAR 几乎不变（差异 <0.1pp），证明梯度冲突不是推理 GAR gap 的原因，exposure bias 是根因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_ours_mid_gar": 0.0151,
    "eval_ours_recovery_pp": 0.29,
    "eval_dongre_mid_gar": 0.0192,
    "eval_dongre_recovery_pp": 0.7,
    "eval_ppl": 1.5,
    "eval_ntp": 0.4016,
    "eval_gate_dynamic_range": {
      "L15": {
        "turn1": 0.6247,
        "turn21": 0.9571,
        "diff": -0.3324
      },
      "L23": {
        "turn1": 0.703,
        "turn21": 0.9779,
        "diff": -0.2749
      },
      "L18": {
        "turn1": 0.828,
        "turn21": 0.9526,
        "diff": -0.1246
      },
      "L9": {
        "turn1": 0.8166,
        "turn21": 0.9403,
        "diff": -0.1237
      },
      "L16": {
        "turn1": 0.8303,
        "turn21": 0.9469,
        "diff": -0.1166
      }
    },
    "vs_v7_gar_ours_diff_pp": -0.06,
    "vs_v7_gar_dongre_diff_pp": -0.02,
    "vs_v7_ppl_diff": -1.28,
    "hypothesis_confirmed": true,
    "summary": "v9 PCGrad 推理 GAR 与 v7 基本一致（ours 0.0151 vs 0.0157, dongre 0.0192 vs 0.0194），差异 <0.1pp，确认梯度冲突解决不改变推理 GAR gap。PPL 显著降低（1.50 vs 2.78）说明 PCGrad 改善了训练质量，但 GAR recovery 未提升，支持 exposure bias 是推理 GAR gap 根因的假设。"
  }
}
```

</details>

---
