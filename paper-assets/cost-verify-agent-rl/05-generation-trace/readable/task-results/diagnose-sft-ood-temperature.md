# diagnose sft ood temperature

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft-ood-temperature_20260520T134131_result.json`
- **Structured JSON:** [`22f48145be99e30a19f3.json`](../../sessions/22/22f48145be99e30a19f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部证据齐了。

## 结论

```json
{
  "sft_ood_80.6_temperature": 0.4,
  "sft_indist_68.75_temperature": 0.4,
  "cell_c_ood_90.3_temperature": 0.4,
  "same_temperature_for_comparison": true,
  "evidence": "所有 eval config 的 val_kwargs 均为 {do_sample: True, temperature: 0.4}"
}
```

**关键发现**：

| 实验 | registry exp_id | 结果 | 温度 | do_sample |
|------|----------------|------|------|-----------|
| SFT OOD 80.6% | `7b_sft_eval_ood` | 108/134 | **T=0.4** | True |
| SFT in-dist 71.875% | `8b_sft_clean_eval_v2` | 23/32 | **T=0.4** | True |
| Cell C OOD 90.3% | `8b_v9d_ood_eval_v5` | 121/134 | **T=0.4** | True |
| SFT in-dist T=0 | `8b_det_eval_full` | 68.75% | **T=0** | False |
| SFT h=2 T=0 | `8b_det_eval_h2` | 31.25% | **T=0** | False |

**验证逻辑**：`best_at_2_mean(9.53) > reward_mean(8.06)` 确认了 stochastic sampling — T=0 下单次采样的 best@2 应等于 mean。Config 文件 `_alfworld_7b_sft_eval_ood.yaml` 第 53-54 行明确写了 `do_sample: True, temperature: 0.4`。

**论文影响**：experiments.tex 标注 T=0 是**错误的**。80.6% 是 T=0.4 的结果。T=0 的 in-dist 结果是 68.75%（`8b_det_eval_full`），OOD T=0 尚未跑过。所有三组对比（SFT / Cell A / Cell C）都用了 T=0.4，横向对比仍然 fair，但论文中的 T=0 标注需要修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "sft_ood_80.6_temperature": 0.4,
    "sft_indist_68.75_temperature": 0.4,
    "cell_c_ood_90.3_temperature": 0.4,
    "same_temperature_for_comparison": true,
    "evidence": "所有 eval config 的 val_kwargs 均为 {do_sample: True, temperature: 0.4}"
  }
}
```

</details>

---
