# ops checkpoint inventory

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_checkpoint-inventory_20260516T053450_result.json`
- **Structured JSON:** [`58c9ad4df57742e9a331.json`](../../sessions/58/58c9ad4df57742e9a331.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是 Recovery Eval 所需 checkpoint 完整清单：

---

## Recovery Eval Checkpoint 清单

### 1. 三条件主实验（Vanilla / TaxEI / Random × 5 seeds）

所有 checkpoint 每个约 501MB，均含 `adapter_model.safetensors`。

| 条件 | Seed | 目录名 | 最终 Checkpoint | 存在? | 大小 |
|------|------|--------|----------------|-------|------|
| **Vanilla** | 42 | `mini_vanilla_sft_v4` | checkpoint-1635 | ✅ | 501M |
| Vanilla | 0 | `mini_vanilla_sft_v4_seed0` | checkpoint-1635 | ✅ | 501M |
| Vanilla | 123 | `mini_vanilla_sft_v4_seed123` | checkpoint-1635 | ✅ | 501M |
| Vanilla | 1 | `mini_vanilla_sft_v4_seed1` | checkpoint-1635 | ✅ | 501M |
| Vanilla | 7 | `mini_vanilla_sft_v4_seed7` | checkpoint-1635 (v1) | ✅ | 501M |
| **TaxEI** | 42 | `mini_taxei_sft_v4` | checkpoint-3387 | ✅ | 501M |
| TaxEI | 0 | `mini_taxei_sft_v4_seed0` | checkpoint-3387 | ✅ | 501M |
| TaxEI | 123 | `mini_taxei_sft_v4_seed123` | checkpoint-3387 | ✅ | 501M |
| TaxEI | 1 | `mini_taxei_sft_v4_seed1` | checkpoint-3387 | ✅ | 501M |
| TaxEI | 7 | `mini_taxei_sft_v4_seed7` | checkpoint-3387 | ✅ | 501M |
| **Random** | 42 | `mini_random_sft_v4` | checkpoint-3387 | ✅ | 501M |
| Random | 0 | `mini_random_sft_v4_seed0` | checkpoint-3387 | ✅ | 501M |
| Random | 123 | `mini_random_sft_v4_seed123` | checkpoint-3387 | ✅ | 501M |
| Random | 1 | `mini_random_sft_v4_seed1` | checkpoint-3387 | ✅ | 501M |
| Random | 7 | `mini_random_sft_v4_seed7` | checkpoint-3387 | ✅ | 501M |

**路径模板**: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/{dir_name}/{version}/checkpoint-{step}/`

### 2. TaxEI-RP（Recovery Paired）— output/ 目录

| Seed | 目录名 | 当前最新 Checkpoint | 状态 | 进度 |
|------|--------|-------------------|------|------|
| 42 | `v4-taxei-rp-s42` | checkpoint-3610 | 🔄 训练中 | 4730/5415 (~29min) |
| 0 | `v4-taxei-rp-s0` | checkpoint-3610 | 🔄 训练中 | 4640/5415 (~33min) |
| 123 | `v4-taxei-rp-s123` | checkpoint-3610 | 🔄 训练中 | 4740/5415 (~28min) |
| 1 | `v4-taxei-rp-s1` | checkpoint-3610 | 🔄 训练中 | 4710/5415 (~29min) |
| 7 | — | — | ❌ 未开始 | — |

**路径模板**: `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s{seed}/{version}/checkpoint-{step}/`

### 总结

- **15/15 主实验 checkpoint 全部存在**，可直接用于 recovery eval
- **TaxEI-RP 4/5 seeds 正在训练**，约 30 分钟后完成（最终 checkpoint 将是 checkpoint-5415）
- **TaxEI-RP seed7 缺失**，需要后续安排训练

---
