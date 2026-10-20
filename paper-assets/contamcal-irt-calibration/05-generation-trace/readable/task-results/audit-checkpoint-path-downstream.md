# audit checkpoint path downstream

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_checkpoint_path_downstream_20260515T205228_result.json`
- **Structured JSON:** [`8dac179602e9a918851b.json`](../../sessions/8d/8dac179602e9a918851b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集和 registry 更新完成。以下是审计报告：

---

## 审计报告

### 1. 下游污染检查

**Eval 实验 — 无污染**
- `exp_001_eval_3B_d025_v2_aligned` / `v2_para_aligned` 引用 `Qwen2.5-3B_d025_s42/lora_adapter`（alpha=16），但这是 v2 eval，对应 v2 SFT，引用正确
- **不存在 v3 eval 实验**（无 `exp_001_eval_3B_d025_v3_*`），所以没有 eval 被旧 checkpoint 污染

**Signals — 存在问题**
- `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_s42/` 包含 s1/s2/s4 信号（arc_challenge, gsm8k, 部分 mmlu）
- 信号计算时间：May 16 02:31-04:00；v3 checkpoint 创建时间：May 16 04:15
- **信号必然使用了旧 `d025_s42`（alpha=16）checkpoint**
  - s1 (embedding): 使用 sentence-transformers，不依赖 SFT adapter → **无影响**
  - s2 (minkpp) 和 s4 (selfcritique): 加载 SFT adapter → **使用了错误的 alpha=16 模型**
- **如果 IRT 流程需要 alpha=32 的 d025 signals，需用 `d025_v3_s42` checkpoint 重新计算 s2/s4**

### 2. _a32_ checkpoint 审计表

| 实验 ID | Registry Status | Conclusion | checkpoint_path | 磁盘 lora_adapter/ |
|---------|----------------|------------|----------------|-------------------|
| `exp_001_sft_3B_d100_s42_a32` | DONE | killed ✅ (已更新) | 空 | 空（0 files） |
| `exp_001_sft_3B_d100_s42_a32_v2` | DONE | failed ✅ (已更新) | 空 | 空（0 files） |
| `exp_001_sft_3B_d025_s42_a32` | DONE | killed ✅ (已更新) | 空（spec 中指向空目录） | 空（0 files） |

磁盘上还存在无 registry 条目的孤立 _a32_ 目录：
- `Qwen2.5-3B_d000_a32_s42` — lora_adapter 空
- `Qwen2.5-3B_d100_a32_s123` — lora_adapter 完全空
- `Qwen2.5-3B_d100_a32_s42_v3` — lora_adapter 空

所有 _a32_ checkpoint 均为空壳，无可用权重。Registry 已标记 conclusion。

### 3. train_config.json 补写结果

**无需补写。** `Qwen2.5-3B_d025_v3_s42/train_config.json` 已存在，内容正确：
```json
{
  "lora_r": 16,
  "lora_alpha": 32,
  "lr": 5e-05,
  "seed": 42,
  "num_samples": 54133
}
```

所有 _a32_ checkpoint 为空壳，不补写 train_config.json。

### 需要决策

d025 的 s2/s4 signals 是否需要用 v3 (alpha=32) checkpoint 重新计算？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "lora_r": 16,
    "lora_alpha": 32,
    "lr": 5e-05,
    "seed": 42,
    "num_samples": 54133
  }
}
```

</details>

---
