# ops check eval and training status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_and_training_status_20260521T233924_result.json`
- **Structured JSON:** [`3e3e78fd38ebd524c2f2.json`](../../sessions/3e/3e3e78fd38ebd524c2f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Eval 进度 (westd-45947, PID 263983)

运行中，已运行 2h47m。

| Task | 描述 | 状态 | TSR | CAR |
|------|------|------|-----|-----|
| 0 | (参考) | ✅ 完成 | — | — |
| 1 | pick up chocolate pudding → basket | ✅ 完成 | **0.0%** (0/50) | **22.0%** (11/50) |
| 2 | pick up milk → basket | 🔄 20/50 | — | — |

### 2. Baseline Checkpoint

- **westd-45947**: `/root/autodl-tmp/checkpoints/baseline_object_pudding_eval/` **不存在**
- **westd-35807**: 存在于 `/root/autodl-tmp/checkpoints/baseline_object_pudding/baseline_object_pudding_seed0/best/`，**19GB**（model.safetensors 7GB + optimizer.pt 12.5GB）

需要从 westd-35807 → westd-45947 传输。

### 3. westd-35807 四个训练

全部存活，4 GPU 各占 ~24GB。

| 训练 | PID | Step | 进度 | Loss | 已运行 | 预计剩余 |
|------|-----|------|------|------|--------|----------|
| baseline_lora_spa_s0 | 281554 | 19115/30000 | 64% | 0.0183 | 21h27m | ~12h |
| baseline_lora_obj_s0 | 281629 | 19077/30000 | 64% | 0.0131 | 21h27m | ~12h |
| a1_lora_spa_s0 | 292258 | 15585/30000 | 52% | 0.0368 | 18h56m | ~16h |
| a1_lora_obj_s0 | 299910 | 17474/30000 | 58% | 0.0214 | 16h50m | ~14h |

无进程死亡，无训练完成。全部正常推进中。

---
