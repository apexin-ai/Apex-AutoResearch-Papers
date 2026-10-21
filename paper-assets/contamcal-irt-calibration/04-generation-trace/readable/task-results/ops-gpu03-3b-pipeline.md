# ops gpu03 3b pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu03-3b-pipeline_20260514T232817_result.json`
- **Structured JSON:** [`46821d3df88af874ce6f.json`](../../sessions/46/46821d3df88af874ce6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已成功启动：

**GPU 0 — eval_3B_d100_v2**: 正在跑 MMLU eval（~40 it/s，14042 items），GPU 0 占用 7671 MiB。

**GPU 3 — sft_3B_d025**: 模型加载中（Qwen2.5-3B），GPU 3 尚在加载阶段。

---

## 汇总

### 1. Checkpoint 验证
- `Qwen2.5-3B_d100_s42/lora_adapter`: **alpha=16, r=16** ✓ D020 v2 确认

### 2. 3B 四档清单

| dosage | checkpoint | 超参 | eval |
|--------|-----------|------|------|
| d000_v2 | ✓ (s42 + s123) | alpha=16 | ✓ aligned+para |
| d005 | ✓ (s42) | **alpha=32 (v1!)** | ✓ aligned+para (v1) |
| d025 | **MISSING** | — | — |
| d100 | ✓ (s42) | alpha=16 v2 | v1 done, v2 进行中 |

### 3. GPU 0 — 3B d100 v2 Eval
- Session: `eval_3B_d100_v2`
- GPU 0 占用 7671 MiB, 92% util
- MMLU 评估中，预计 ~6 分钟完成 MMLU，之后 gsm8k + arc_challenge

### 4. GPU 3 — 3B d025 SFT (D020: lr=5e-5, alpha=16, r=16)
- Session: `sft_3B_d025`
- 模型加载中

### 注意
**3B d005 checkpoint 是 v1 产物（alpha=32）**，需要用 D020 参数重训 d005 v2。d025 完全缺失故优先填补。

---
