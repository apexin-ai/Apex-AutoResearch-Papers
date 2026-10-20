# ops gpu audit and fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-and-fix_20260515T191443_result.json`
- **Structured JSON:** [`eccccf663e4bf802ebb5.json`](../../sessions/ec/eccccf663e4bf802ebb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 597179 已杀。以下是完整审计结果：

---

## GPU 全面审计结果

| GPU | 进程 PID | 实验 | VRAM | Util | 状态 |
|-----|---------|------|------|------|------|
| **cuda:0** | 594494 | exp_001_sft_3B_d100_s123_a32_v2 | 17966 MiB | 0%* | **54% (2263/4159)**, loss 1.17, ~4.3s/step, ETA ~2h15m |
| **cuda:1** | 593745 | exp_001_sft_3B_d100_s42_a32_v2 | 13332 MiB | 28% | **56% (2318/4159)**, loss 1.17, ~4.3s/step, ETA ~2h10m |
| **cuda:2** | 614412 | exp_001_eval_3B_d100_s123_para_aligned_v2 | 9008 MiB | 66% | 正在跑 GSM8K paraphrased 77% (176/228), MMLU paraphrased 已完成 |
| **cuda:3** | 617202 | exp_002_signals_3B_v4 | 7064 MiB | 60% | **在跑** — compute_signals d000_s42 mmlu, 启动 18 分钟 |
| **cuda:4** | ~~597179~~ | ~~d000_v3 孤儿~~ | ~~13868 MiB~~ | — | **已杀**, cuda:4 已释放 |
| **cuda:5** | 589763 | exp_001_sft_d025_3B_v3 | 17642 MiB | 43% | **75% (2542/3384)**, epoch 0.75, loss 1.08-1.20, ETA ~1h |

*cuda:0 的 0% util 是采样瞬间值，进程正常在跑。

### 逐项回答

1. **PID 597179** — 已 kill -9，确认死亡，cuda:4 已释放
2. **d025_v3 (cuda:5)** — 仍在训练，75% 进度，lora_adapter 目录为空（未保存最终 checkpoint），预计 ~1h 完成
3. **signals_3B_v4 (cuda:3)** — 在跑，PID 617202，正在处理 d000_s42 mmlu 信号
4. **d100 SFT cuda:0/1** — 分别 54%/56%，约 2h+ 后完成
5. **d100 para eval v2 (cuda:2)** — 正在 GSM8K paraphrased 评估 (77%)，快完成这个 benchmark

### 资源系统误报说明

资源系统报 cuda:3/4/5 idle 是误报。实际 6 张卡全部有活跃 GPU 进程。

---
