# ops d084 gpu refresh

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d084-gpu-refresh_20260515T231221_result.json`
- **Structured JSON:** [`82b2871e98920d7e2d0a.json`](../../sessions/82/82b2871e98920d7e2d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是结构化报告。

---

## 1. GPU 使用表

| GPU | VRAM | Util | PID | 实验 | 运行时长 |
|-----|------|------|-----|------|---------|
| 0 | 23258/24564 MiB | 100% | 642763 | eval_d100_s123_batch (GSM8K 33%) | 1h37m |
| 0 | ↑共享 | ↑ | 643167 | SFT d005_s42_a32 | 1h36m |
| 1 | 13341/24564 MiB | 55% | 628668 | SFT d100_s42_a32_v3 | 3h01m |
| 2 | 7955/24564 MiB | 65% | 652259 | signals_v7 (d005_s123/mmlu) | 8min |
| 3 | ~~7943/24564 MiB~~ → **FREE** | ~~54%~~ | ~~630891~~ | ~~signals_v6 orphan~~ **KILLED** | was 2h51m |
| 4 | 7535/24564 MiB | 53% | 648627 | signals_v5 batch (d100_s42/mmlu) | 40min |
| 5 | 18665/24564 MiB | 45% | 633041 | SFT d000_s42_a32 | 2h41m |

## 2. Orphan Kill 结果

**PID 630891** (signals_v6, d000_v2_s42/mmlu/s4) — SIGTERM 成功终止，未需 force kill。cuda:3 已释放。

## 3. d000_s42 SFT 状态

- **进度**: 77% (2402/3125), ~48min 剩余, ~4.0s/it
- **已有 checkpoint** (May 14 旧 run): `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_model.safetensors` (114MB)
- **当前 run** 将覆盖旧 checkpoint
- **Metrics**: loss=1.10, token_accuracy=0.75, epoch=0.76

## 4. 各训练/任务进度

| 实验 | GPU | 进度 | ETA | 速度 |
|------|-----|------|-----|------|
| SFT d000_s42 | cuda:5 | **77%** (2402/3125) | ~48min | 4.0s/it |
| SFT d100_s42_v3 | cuda:1 | **59%** (2443/4159) | ~2h00m | 4.5s/it |
| SFT d005_s42 | cuda:0 | **40%** (1262/3177) | ~2h27m | 4.6s/it |
| Eval d100_s123_batch | cuda:0 | GSM8K **33%** (430/1319) | ~2h37m on GSM8K alone; 还有 arc+humaneval+para variants | 10.5s/it |
| signals_v5 batch | cuda:4 | [2/4] d100_s42/mmlu 进行中 | [1/4] d025_s42/mmlu ✓ PASSED (耗时 2h50m) | — |
| signals_v7 | cuda:2 | d005_s123/mmlu s2_minkpp ref log-probs **63%** (8809/14042) | ~1.5min 完成此步 | 57-60 it/s |

## 5. Signals Pipeline 完成度矩阵 (3B, alpha32)

**信号类型**: s1=embedding, s2=minkpp, s3=constat, s4=selfcritique

| Dosage/Seed | mmlu | gsm8k | arc_challenge | 备注 |
|-------------|------|-------|---------------|------|
| **d000_v2_s42** | s1✓ s2✓ s3✓ s4✗ | s1✓ s2✓ s3✓ | s1✓ s2✓ s3✓ | orphan killed, s4/mmlu 未完成 |
| **d005_s42** | s1✓ s2✓ | s1✓ s2✓ | s1✓ s2✓ s4✓ merged✓ | 缺 s3/s4(mmlu,gsm8k) |
| **d005_s123** | s1✓ s2⏳(v7 63%) | — | — | v7 刚启动 8min |
| **d025_s42** | s4✓ merged✓ | — | — | v5 刚完成 all/mmlu, 产出待确认 |
| **d025_v3_s42** | s1✓ s2✓ | s1✓ s2✓ | s1✓ s2✓ | 缺 s3/s4 |
| **d100_s42** | s1✓ s2✓ (v5⏳) | — | — | v5 正在跑 all/mmlu |

*注*: d025_s42 刚被 v5 batch 标记 PASS (all signals/mmlu)，但 ls 时只看到 s4+merged，可能 v5 写入 timing 或 output dir 命名差异，建议后续验证。

## 6. 空闲 GPU

| GPU | 状态 |
|-----|------|
| cuda:0 | 占用（SFT + eval 共享，100% VRAM） |
| cuda:1 | 占用（SFT d100_v3） |
| cuda:2 | 占用（signals_v7） |
| **cuda:3** | **空闲** ← 刚释放 |
| cuda:4 | 占用（signals_v5 batch） |
| cuda:5 | 占用（SFT d000_s42, ~48min 后释放） |

**可用 GPU: cuda:3 立即可用；cuda:5 预计 ~48min 后空闲。**

---
