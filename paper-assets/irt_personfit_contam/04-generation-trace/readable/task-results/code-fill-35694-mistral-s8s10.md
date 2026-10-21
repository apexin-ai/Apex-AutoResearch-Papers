# code fill 35694 mistral s8s10

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fill-35694-mistral-s8s10_20260521T142934_result.json`
- **Structured JSON:** [`8baeac2fb3a69afde216.json`](../../sessions/8b/8baeac2fb3a69afde216.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有三个 Mistral 训练都已启动并正在推进。汇总：

---

## 产出汇总

### 1. Llama eval 结果
| Condition | theta | lz* | acc |
|-----------|-------|-----|-----|
| clean_s8 | -0.698 | 1.166 | 0.586 |
| clean_s9 | — | — | 未开始 |
| clean_s10 | — | — | 未开始 |

s8 刚完成，s9/s10 eval 尚未启动（GPU 0 现在空闲可用）。

### 2. Mistral s8/s9/s10 训练
| GPU | exp_id | PID | 进度 | 速度 |
|-----|--------|-----|------|------|
| cuda:1 | exp-ctrl-contam-mistral-clean-s8 | 154389 | 34/939 | ~1.14s/it |
| cuda:2 | exp-ctrl-contam-mistral-clean-s9 | 154468 | 17/939 | ~2.12s/it |
| cuda:3 | exp-ctrl-contam-mistral-clean-s10 | 154614 | 32/939 | ~1.13s/it |

**注意**：GPU 2 上 s9 与 `eval_with_ht.py --stage grpo` (PID 153583) 共享，速度约慢 2x。GRPO eval 完成后 s9 会加速。

SEED_MAP 已更新：s4-s10 seeds = 301-307（与 Llama 一致）。

### 3. GRPO ckpt eval 结果
`grpo_results.json` 已完成（22:21）：
- **theta_mle = 0.157, lz* = 7.770, acc = 0.714**
- lz*_seen = 3.410, acc_seen = 0.730
- lz*_unseen = 7.000, acc_unseen = 0.712
- stage = "grpo", model = Qwen2.5-7B-Instruct

另有 `eval_with_ht.py --stage grpo` 仍在 GPU 2 上运行（PID 153583）。

### 4. GPU 状态
| GPU | 显存 | 利用率 | 任务 |
|-----|------|--------|------|
| 0 | 0 MiB | 0% | **空闲**（可启动 Llama s9/s10 eval）|
| 1 | 6145 MiB | 59% | Mistral clean_s8 |
| 2 | 14710 MiB | 67% | Mistral clean_s9 + GRPO eval |
| 3 | 4545 MiB | 13% | Mistral clean_s10 |

---
