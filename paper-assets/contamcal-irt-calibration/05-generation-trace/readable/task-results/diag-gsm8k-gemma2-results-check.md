# diag gsm8k gemma2 results check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gsm8k_gemma2_results_check_20260520T082613_result.json`
- **Structured JSON:** [`6895345fa517827c641f.json`](../../sessions/68/6895345fa517827c641f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Gemma-2 GSM8K eval

| Dosage | 状态 | Accuracy |
|--------|------|----------|
| d000_s42 | ✅ 完成 | 13.87% (183/1319) |
| d000_s42_fixed | ✅ 完成 | 11.22% (148/1319) |
| d100_s42 | 目录空（仅创建） | — |
| d100_s42_fixed | 🔄 **进行中** (GPU 3, PID 307190, 25.6GB, 94% util) | — |
| d005/d025/d050 | 无结果目录 | — |

⚠️ Gemma-2 d000 准确率异常低（~11-14%），可能是 eval 配置问题。

### Qwen-14B GSM8K eval

| Dosage | 状态 | Accuracy |
|--------|------|----------|
| d000_s42 | ✅ 完成 | **60.80%** (802/1319) |
| d100_s42 | ✅ 完成 | **81.27%** (1072/1319) |
| d000_s123 | 🔄 **进行中** (GPU 1, PID 305387, 33.3GB, 95% util) | — |

Qwen-14B s42 全部完成，contamination effect = +20.47pp (d100 vs d000)。

### GPU 状态

| GPU | 占用 | 进程 |
|-----|------|------|
| cuda:0 | 56.5GB, 84% | phi-4 d025_s0 SFT 训练 |
| cuda:1 | 33.3GB, 95% | **Qwen-14B d000_s123 GSM8K eval** |
| cuda:2 | 66.5GB, 91% | OLMo-2-7B d100_s0 SFT 训练 |
| cuda:3 | 25.6GB, 94% | **Gemma-2 d100_s42_fixed GSM8K eval** |

**cuda:1 和 cuda:3 均不空闲**，都在跑 GSM8K eval。

---
