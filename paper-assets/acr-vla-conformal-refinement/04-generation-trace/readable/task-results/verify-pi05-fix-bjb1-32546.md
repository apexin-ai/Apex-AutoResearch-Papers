# verify pi05 fix bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pi05-fix-bjb1-32546_20260521T110003_result.json`
- **Structured JSON:** [`bb1e10000f0b755c1544.json`](../../sessions/bb/bb1e10000f0b755c1544.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 两个修复都已部署到 bjb1-32546

| 修复 | 状态 | 位置 |
|------|------|------|
| Image 180° flip | ✅ 已有 | `pi05_wrapper.py:158` — `torch.flip(img, dims=[2, 3])` |
| Vision tower key remap | ✅ wrapper 层修复 | `pi05_wrapper.py:102-123` — `_fix_vision_tower_keys`, 日志确认 437 keys 已修复 |
| lerobot `_fix_pytorch_state_dict_keys` | ⚠️ 仍缺少 remap | `modeling_pi05.py:1049` — 只处理 adaRMS/MLP/lm_head，不处理 vision_model |

### 实验状态 — 全军覆没

| 实验 | 状态 | SR |
|------|------|-----|
| object-seed42 | ✅ 完成 | 0.0% (0/200) |
| object-seed43 | ✅ 完成 | 0.0% (0/200) |
| object-seed44 | ✅ 完成 | 0.0% (0/200) |
| spatial-seed42 | ❌ 中途崩溃 | 0% (进行中) |
| spatial-seed43 | ❌ 中途崩溃 | 0% (进行中) |
| spatial-seed44 | ❌ 中途崩溃 | 0% (进行中) |

**没有 python 进程在运行。**

### 关键发现

**修复已生效但 SR 仍为 0%**，问题在别处。wrapper 的 `_fix_vision_tower_keys` 成功加载了 437 个 vision tower 权重（日志确认），image flip 也在代码中。

可能的根本原因：
1. **normalizer glob bug** — `_load_normalizer_stats` 用 `*normalizer*processor*` glob，会同时匹配 `normalizer` 和 `unnormalizer` 两个文件，`sorted()[0]` 取到的是 unnormalizer 文件（字母序在前），导致 state 归一化加载了错误的统计量
2. 模型 checkpoint 本身质量问题（来自 `pepijn223/pi05_libero_31_9_non_q`）
3. 其他 config/preprocessing 不匹配

是否仍要我给 lerobot 的 `_fix_pytorch_state_dict_keys` 添加 vision_model remap（作为 defense-in-depth）？还是先排查 0% SR 的根因？

---
