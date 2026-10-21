# verify smolvla checkpoint source

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_smolvla-checkpoint-source_20260522T115941_result.json`
- **Structured JSON:** [`829c0d878477f2c8a290.json`](../../sessions/82/829c0d878477f2c8a290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核实完毕。结论如下：

---

## 结果

### 1. 我们用的是哪个？

**`lerobot/smolvla_libero`**（不是 `HuggingFaceVLA/smolvla_libero`）。

证据：下载 metadata 中的 commit SHA `31d453f7edd78c839a8bbc39744a292686daf0de` 精确匹配 `lerobot/smolvla_libero`。config.json 中的 `repo_id: "pepijn223/smolvla_libero"` 是训练者的个人 repo，后来发布为 `lerobot/smolvla_libero`。

### 2. 这两个是不是同一个模型？

**不是。架构和训练配置有根本性差异。**

| 配置项 | `HuggingFaceVLA/smolvla_libero` (Sep 2025) | `lerobot/smolvla_libero` (Mar 2026) ← 我们用的 |
|--------|---------------------------------------------|------------------------------------------------|
| VLM backbone | SmolVLM2-500M-**Instruct** | SmolVLM2-500M-**Video**-Instruct |
| state_dim | **8** | **6** |
| 相机数量 | **2** (image, image2) | **3** (camera1, camera2, camera3) |
| n_action_steps | **1** | **50** |
| freeze_vision_encoder | **true** | **false** |
| train_expert_only | **true** | **false** |
| num_vlm_layers | **0** | **16** |
| num_expert_layers | **-1** (all) | **0** |
| expert_width_multiplier | **0.5** | **0.75** |
| 模型大小 | ~1.22 GB | ~907 MB |

### 3. 差异总结

这是两代不同的 SmolVLA LIBERO 微调：
- **`HuggingFaceVLA/`** — 旧版 (v1)，冻结视觉编码器、只训练 expert layers、单步 action、2 相机、8 维 state
- **`lerobot/`** — 新版 (v2)，全参微调、50 步 action chunking、3 相机、6 维 state、Video backbone

如果要切换到 `HuggingFaceVLA/smolvla_libero`，wrapper 代码需要改动（相机数量、state 维度、action steps 都不同）。

---
