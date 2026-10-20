# ops westd training progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-training-progress_20260519T180359_result.json`
- **Structured JSON:** [`6599d520cf5be38646ba.json`](../../sessions/65/6599d520cf5be38646ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 训练进度汇总

### GPU 状态：4/4 全在跑 seed=123 训练 ✅

| GPU | 模型 | 当前 dosage | 进度 | 速度 | 当前 dosage 剩余 | 剩余 dosage | 预计全部完成 |
|-----|------|-----------|------|------|----------------|------------|------------|
| 0 | **phi-4** (14B) | d025 (3/5) | 111/3384 (3%) | ~2.4s/it | ~2h11m | d050, d100 | ~08:15 CST |
| 1 | **Qwen2.5-14B** | d005 (2/5) | 1886/3177 (59%) | ~3.0s/it | ~1h05m | d025, d050, d100 | ~11:25 CST |
| 2 | **OLMo-2-7B** (+Qwen7B) | d025 (3/5 OLMo) | 1778/3384 (53%) | ~1.9s/it | ~51min | OLMo d050,d100 + Qwen7B ×5 | ~15:05 CST |
| 3 | **gemma-2-9b** | d005 (2/5) | 2152/3177 (68%) | ~2.85s/it | ~49min | d025, d050, d100 | ~10:40 CST |

已完成的 dosage：
- phi-4: d000 ✅, d005 ✅
- Qwen2.5-14B: d000 ✅
- OLMo-2-7B: d000 ✅, d005 ✅
- gemma-2-9b: d000 ✅

### seed=0 就绪状态 ✅

- **脚本**: 4/4 均存在（`scripts/seed0/`），格式正确，`--seed 0`，output-dir 用 `_s0` 后缀
- **SFT 数据**: 5 个 dosage jsonl 全部就绪（000/005/025/050/100）
- **Base models**: phi-4, Qwen2.5-14B, Qwen2.5-7B, OLMo-2-7B, gemma-2-9b 均已缓存在 `/root/autodl-tmp/models/`
- **输出目录**: `_s0` 后缀与 `_s123` 不冲突，无需预创建

### 预计释放顺序

1. **GPU 0** (phi-4) — ~08:15 CST，最先释放，可立即启动 s0 任务
2. **GPU 3** (gemma-2-9b) — ~10:40 CST
3. **GPU 1** (Qwen2.5-14B) — ~11:25 CST
4. **GPU 2** (OLMo+Qwen7B) — ~15:05 CST，最晚（需跑两个模型共 10 个 dosage）

---
