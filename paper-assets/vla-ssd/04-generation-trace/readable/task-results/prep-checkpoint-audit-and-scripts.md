# prep checkpoint audit and scripts

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_checkpoint_audit_and_scripts_20260521T155659_result.json`
- **Structured JSON:** [`25f7a5757dd5283f9dbe.json`](../../sessions/25/25f7a5757dd5283f9dbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都已正确生成。以下是三个任务的汇总产出。

---

## 产出 1: Checkpoint 清单

| Checkpoint | model_type | Architecture | 大小 | 用途 |
|---|---|---|---|---|
| `dinov2-large` | dinov2 | Dinov2Model | 1.2G | 视觉编码器 |
| **`nora-libero-goal`** | qwen2_5_vl | Qwen2_5_VLForConditionalGeneration | 7.1G | NORA fine-tuned — **Goal** |
| **`nora-libero-spatial`** | qwen2_5_vl | Qwen2_5_VLForConditionalGeneration | 7.1G | NORA fine-tuned — **Spatial** |
| `qwen25-vl-3b-base` | qwen2_5_vl | Qwen2_5_VLForConditionalGeneration | 7.1G | NORA untrained base |
| `openvla-7b` | openvla (llama) | OpenVLAForActionPrediction | 15G | OpenVLA base (untrained) |
| **`openvla-7b-finetuned-libero-goal`** | openvla | OpenVLAForActionPrediction | 14G | OpenVLA fine-tuned — **Goal** |
| **`openvla-7b-finetuned-libero-object`** | openvla | OpenVLAForActionPrediction | 15G | OpenVLA fine-tuned — **Object** |
| **`openvla-7b-oft-finetuned-libero-10`** | openvla | OpenVLAForActionPrediction | 15G | OpenVLA fine-tuned — **Long** (libero_10) |
| **`tracevla-phi3v`** | phi3_v | Phi3VForCausalLM | 7.8G | TracVLA trained（**单一 checkpoint，所有 suite 共用**） |
| `phi3v-base` | phi3_v | Phi3VForCausalLM | 7.8G | TracVLA untrained base |
| `phi3v-base-ms` | — (无config) | — | 7.8G | phi3v-base 的 ModelScope 副本 |
| `openvla-phi3v` | — (空目录) | — | 24K | 占位符（仅 README/LICENSE） |

**NORA**: 只有 Goal + Spatial（**无 Object、无 Long**）。每 suite 一个 checkpoint。

**TracVLA**: 只有一个 checkpoint `tracevla-phi3v`，所有 suite 共用。untrained base = `phi3v-base`。

**OpenVLA**: Goal + Object + Long 各一个 fine-tuned checkpoint（**无 Spatial**）。

## 产出 2: TraceVLA Long 脚本

`/root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py` — 已创建，未提交运行。

- DATA → `libero_10`
- RESULTS → `tracvla_long`
- TASKS/INSTRUCTIONS/PARAPHRASES 均已替换为 Long 的 10 个任务
- Checkpoints 不变（trained=tracevla-phi3v, untrained=phi3v-base）

## 产出 3: TraceVLA Goal untrained 状态

- `results/tracvla_goal/` — **不存在**（无 trained 也无 untrained 结果）
- 之前无 `tracvla_goal_full_pipeline.py` 脚本

**现已创建** `/root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py`，未提交运行。

- DATA → `libero_goal`
- RESULTS → `tracvla_goal`
- TASKS/PARAPHRASES 使用 Goal 的 10 个任务（与 nora_goal 脚本一致）

---
