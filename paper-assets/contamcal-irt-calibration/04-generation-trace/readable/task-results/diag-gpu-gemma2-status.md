# diag gpu gemma2 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-gemma2-status_20260520T083405_result.json`
- **Structured JSON:** [`bb26db26336b60cc5b70.json`](../../sessions/bb/bb26db26336b60cc5b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 状态 (4× RTX PRO 6000 Blackwell, 98GB)

| GPU | PID | VRAM | Util | 任务 |
|-----|--------|------|------|------|
| 0 | 302132 | 56.5GB | 76% | **Phi-4 s0 sweep** — 当前 d025_s0，step 1541/3384 (45%)。d000、d005 已完成 |
| 1 | 305387 | 33.3GB | 100% | **Qwen-14B d000_s123 GSM8K eval** — 进行中，结果目录为空 |
| 2 | 306129 | 66.5GB | 94% | **OLMo-2 s0 sweep** — 当前 d100_s0（最后一个 dosage）。d000/d005/d025/d050 已完成 |
| 3 | 307190 | 26.6GB | 94% | **Gemma-2 d100_s42_fixed GSM8K eval** — 进行中，结果目录为空，torch._inductor 编译中 |

## 关键问题回答

- **Gemma-2 d100**: 未完成。GPU 3 正在跑 eval（`gemma2_d100_s42_fixed`），output dir 已创建但无结果文件
- **OLMo-2 s0**: 当前在最后一个 dosage **d100**，sweep 即将完成
- **Qwen-14B s123**: **d000** eval 正在 GPU 1 上跑，尚无结果。**d100_s123** 尚未开始（结果目录不存在）
- **Phi-4 s123 sweep**: 已完成（May 20 09:10，exit code 0）
- **Phi-4 s0 sweep**: d025 训练中，45% 进度，预计还需 ~1.3h

---
