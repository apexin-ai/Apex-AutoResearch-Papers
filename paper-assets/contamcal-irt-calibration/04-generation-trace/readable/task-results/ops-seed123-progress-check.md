# ops seed123 progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed123-progress-check_20260519T154354_result.json`
- **Structured JSON:** [`379947421d8ff7d4840f.json`](../../sessions/37/379947421d8ff7d4840f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 seed=123 训练进度

### GPU 利用率

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 (Phi-4) | 91% | 57.8 / 97.9 GB |
| 1 (Qwen2.5-14B) | 93% | 64.1 / 97.9 GB |
| 2 (Qwen-7B + OLMo-2) | 98% | 61.8 / 97.9 GB |
| 3 (Gemma-2 9B) | 64% | 54.6 / 97.9 GB |

### 各模型详细进度

每个 sweep 包含 5 个 dosage，基于 Qwen-7B 已完成数据估算各 dosage 的 max_steps：d000=3125, d005=3177, d025=3384, d050=3642, d100=4159，总计 17,487 steps/sweep。

**GPU 0 — Phi-4 14.7B**
- 当前 dosage: **d000**
- 进度: **3022/3125** (96.7%)，~2.4s/step
- 已完成: 无
- ETA d000 完成: **~4 min**
- ETA 整个 sweep: **~9.6h**（剩余 14,465 steps）

**GPU 1 — Qwen2.5-14B**
- 当前 dosage: **d000**
- 进度: **2352/3125** (75.3%)，~3.15s/step
- 已完成: 无
- ETA d000 完成: **~41 min**
- ETA 整个 sweep: **~13.2h**（剩余 15,135 steps）

**GPU 2 — Qwen2.5-7B + OLMo-2-7B**
- **Qwen2.5-7B: 全部 5 个 dosage 已完成** ✓ (d000→d100)
- OLMo-2-7B 当前 dosage: **d005**
- 进度: **620/3177** (19.5%)，~1.85s/step
- 已完成: d000
- ETA d005 完成: **~79 min**
- ETA OLMo-2 sweep 完成: **~7.1h**（剩余 13,742 steps）

**GPU 3 — Gemma-2 9B**
- 当前 dosage: **d000**
- 进度: **2478/3125** (79.3%)，~2.95s/step
- 已完成: 无
- ETA d000 完成: **~32 min**
- ETA 整个 sweep: **~12.3h**（剩余 15,009 steps）

### 总结

| 模型 | 整体进度 | 预计完成时间 |
|------|---------|-------------|
| Qwen2.5-7B | **100%** ✓ | 已完成 |
| OLMo-2-7B | 21.4% | ~7h 后 |
| Phi-4 14.7B | 17.3% | ~10h 后 |
| Gemma-2 9B | 14.2% | ~12h 后 |
| Qwen2.5-14B | 13.5% | ~13h 后 |

4 张 GPU 全部在正常跑。Qwen2.5-7B 已率先完成，GPU 2 已自动切换到 OLMo-2。其余 3 张 GPU 都还在各自的 d000 阶段，Phi-4 最快将在 ~4 分钟内进入 d005。

---
