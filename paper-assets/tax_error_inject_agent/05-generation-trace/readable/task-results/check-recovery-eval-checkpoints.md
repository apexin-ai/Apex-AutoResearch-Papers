# check recovery eval checkpoints

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_recovery-eval-checkpoints_20260515T124148_result.json`
- **Structured JSON:** [`8c425a433397509bbea4.json`](../../sessions/8c/8c425a433397509bbea4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。

## Checkpoint 状态

| Method | Seed | Checkpoint Path (final) | Status |
|--------|------|------------------------|--------|
| Vanilla | 0 | `.../mini_vanilla_sft_v4_seed0/v0-20260515-014317/checkpoint-1635` | EXISTS |
| Vanilla | 123 | `.../mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635` | EXISTS |
| TaxEI | 0 | `.../mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387` | EXISTS |
| TaxEI | 123 | `.../mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387` | EXISTS |
| Random | 0 | `.../mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387` | EXISTS |
| Random | 123 | `.../mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387` | EXISTS |

**全部 6 个 checkpoint 都存在，每个都有 3 个中间 checkpoint。**

## 已有 Recovery Eval 结果

仅有无 seed 后缀（默认 seed=42）的 recovery eval：
- `v4_vanilla_recovery_eval.json` (476KB, May 15 03:45)
- `v4_taxei_recovery_eval.json` (482KB, May 15 04:49)
- `v4_taxei_recovery_eval_r2.json` (481KB, May 15 05:32)
- `v4_random_recovery_eval.json` (459KB, May 15 05:32)

**seed=0 和 seed=123 的 recovery eval 尚未执行。**

已有 seed0/seed123 的 **clean eval**（非 recovery）：`v4_{vanilla,taxei,random}_seed{0,123}_eval.json`

## injected_eval.py 参数

```
--model_path       LoRA adapter checkpoint 路径
--base_model       基础模型路径 (默认 Qwen3-8B)
--model_variant    标签: taxei / random / vanilla
--alfworld_data    ALFWorld 数据路径
--eval_split       评估 split (默认 valid_unseen)
--num_episodes     episode 数 (默认 47)
--output           输出 JSON 路径
--device           设备 (默认 cuda:0)
--seed             随机种子 (默认 42)
--inject_step      注入步骤, -1=随机[2,6] (默认 -1)
--task_list        任务列表文件
--compare_with     对比文件
--compare_output   对比输出文件
```

**结论：所有 checkpoint 就绪，可以提交 6 个 recovery eval（3 methods × 2 seeds）。**

---
