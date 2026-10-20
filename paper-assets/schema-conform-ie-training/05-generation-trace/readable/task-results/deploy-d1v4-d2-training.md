# deploy d1v4 d2 training

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_d1v4_d2_training_20260513T063714_result.json`
- **Structured JSON:** [`48c9566613db128474fc.json`](../../sessions/48/48c9566613db128474fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D1 v4 step 10 指标也出来了。

---

## 汇报

### 1. 残留进程 Kill 确认
PID 67210, 70714 及所有 train_grpo 进程已 kill，清理后 `ps aux` 返回 0 条。

### 2. train_grpo.py 部署 + enable_thinking 确认
- 已部署修复版，包含 `_extract_completion_text()` 处理 TRL 新版 chat message 格式（首次部署时因此 bug 双双崩溃，已修复）
- `{%- set enable_thinking = false -%}` 注入模板头部 ✓

### 3. data_utils.py + rewards.py relation fix 确认
- `DYGIEPP_TO_SCHEMA_REL_TYPE`: 2 处 ✓
- `_normalize_relation`: 3 处 ✓
- `threshold: float = 0.3`: 1 处 ✓

### 4. tmux session
| Session | GPU | PID (python) |
|---------|-----|-------------|
| d1v4 | cuda:1 | 77066 |
| d2phase2 | cuda:0 | 77141 |

### 5. nvidia-smi
| GPU | VRAM | Util |
|-----|------|------|
| 0 (D2) | 23623 MiB / 97887 MiB | 63% |
| 1 (D1) | 28933 MiB / 97887 MiB | 77% |

### 6. Step 10 指标

| 指标 | D1 v4 | D2 Phase 2 |
|------|-------|------------|
| loss | -0.119 | -0.2167 |
| reward | 0.4456 | 0.4761 |
| reward_std | 0.2312 | 0.2466 |
| clipped_ratio | 0 | 0 |
| mean_length | 180.4 | 85.81 |
| max_length | 422.5 | 211.1 |
| grad_norm | 0.8513 | 0.906 |
| step_time | 33.41s | 21.92s |
| `&lt;think>` | 有空 think 块 | 有空 think 块 |

- **无 clipping** — 输出没超 max_completion_length
- **think 块为空** — `enable_thinking=false` 生效，模型仅输出空 `&lt;think>&lt;/think>` 不消耗 token
- D2 reward 略高（0.4761 vs 0.4456），因为从 formal_A/merged 继续训练，起点更好
- D1 mean_length 更长（180 vs 86），因为基础模型更倾向生成长输出

### 7. D2 model_name 调整
checkpoint-200 是 **LoRA adapter 格式**（含 `adapter_model.safetensors`），无法直接作为 `from_pretrained` 的 model_name。已改为使用 `formal_A/merged`（完整合并模型，含 `model.safetensors`），训练正常启动。

---
