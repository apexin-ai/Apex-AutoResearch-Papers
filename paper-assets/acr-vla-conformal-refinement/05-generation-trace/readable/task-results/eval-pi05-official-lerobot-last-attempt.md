# eval pi05 official lerobot last attempt

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pi05-official-lerobot-last-attempt_20260521T060804_result.json`
- **Structured JSON:** [`3c5817ffd29708ca3336.json`](../../sessions/3c/3c5817ffd29708ca3336.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断报告

### 方案：方案 A — 官方 lerobot-eval（patched）

### 结果

| 指标 | 值 |
|------|------|
| **Overall SR** | **100.0% (3/3)** |
| Task | libero_object, task_id=0 |
| Episode 0 | ✅ 成功 (reward=1.0) |
| Episode 1 | ✅ 成功 (reward=1.0) |
| Episode 2 | ✅ 成功 (reward=1.0) |
| 每 episode 成功步数 | ~140-143 步 |
| Eval 总耗时 | 50.95s |

### 根因分析

**我们 wrapper 的 5 轮 0% SR 全部因同一个 bug：vision tower key mismatch。**

1. **问题**：checkpoint 的 safetensors key 含 `vision_tower.vision_model.encoder.layers.X`，但 transformers 5.8.0 的 `SiglipVisionModel` 期望 `vision_tower.encoder.layers.X`（无 `vision_model` 中间层）
2. **lerobot 0.5.2 的 `_fix_pytorch_state_dict_keys` 缺少此映射**，导致 `load_state_dict(strict=True)` 整体失败
3. 错误被 `try/except` 静默捕获，模型以**随机初始化权重**运行 → 0% SR
4. 官方 lerobot-eval **同样有此 bug**，不是我们 wrapper 独有

### 修复内容

1. **Vision tower key remapping**：在 `_fix_pytorch_state_dict_keys` 中添加 `vision_tower.vision_model.` → `vision_tower.` 映射（437 个 key 全部重映射成功）
2. **PaliGemma tokenizer**：`google/paligemma-3b-pt-224` 是 gated repo，改用 ModelScope 镜像下载 tokenizer

### 结论

**SR > 0% → wrapper 有隐藏 bug，继续 debug。** π0.5 模型有效，根因是 vision tower 权重未正确加载。需要在我们的 wrapper 中应用相同的 key remapping fix。

### Gripper 维度
所有 3 个 episode 在 ~140 步时完成任务，说明 gripper 控制正常（能抓取和放置物体）。

---
