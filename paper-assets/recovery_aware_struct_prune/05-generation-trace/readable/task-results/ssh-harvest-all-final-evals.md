# ssh harvest all final evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_all_final_evals_20260521T074920_result.json`
- **Structured JSON:** [`4adb841f7c00a1b9c16b.json`](../../sessions/4a/4adb841f7c00a1b9c16b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 收割结果汇总

**这些 eval 并非 16+ 小时前启动。** 最早的在今天 10:00 启动，大部分在 12:53-14:47 之间启动。目前没有任何目标 eval 完成。

### 目标 eval 进度

| eval_id | 状态 | 进度 | 当前 interim acc | ETA | 服务器 |
|---------|------|------|-----------------|-----|--------|
| GSM8K GRPO CKA-only 25% (v3) | 运行中 | 1225/1319 (93%) | 59.75% @1200 | ~15-20min | westd-29022 GPU0 |
| GSM8K SFT CKA-only 25% | 运行中 | 314/1319 (24%) | 59.33% @300 | 数小时 | westd-29022 GPU1 |
| GSM8K SFT Random 20% | 运行中 | 667/1319 (51%) | 51.85% @650 | ~1h | westd-29022 GPU2 |
| GSM8K GRPO Standard 25% | 运行中 | 304/1319 (23%) | 53.00% @300 | 数小时 | westb-23072 GPU1 |
| MATH-500 SFT Standard 25% | 运行中 | 301/500 (60%) | — | 数小时(~1min/sample) | westb-23072 GPU0 |

### 已完成的 eval（额外发现）

| eval_id | 状态 | accuracy | correct/total | stderr | 服务器 |
|---------|------|----------|---------------|--------|--------|
| GSM8K GRPO Random 20% (v2) | ✅ 完成 | 50.57% | 667/1319 | ±1.38% | westd-29022 |
| GSM8K Dense Unpruned | ✅ 完成 | 90.83% | 1198/1319 | ±0.79% | westb-23072 |
| HumanEval SFT Standard 25% | ✅ 完成 | 1.83% (pass@1) | 3/164 | ±1.05% | westb-23072 |

### GPU 占用

**westd-29022:**
- GPU 0: 28933/97887 MiB — GRPO CKA-only 25% v3 (快完成)
- GPU 1: 28933/97887 MiB — SFT CKA-only 25%
- GPU 2: 26219/97887 MiB — SFT Random 20%
- GPU 3: 空闲

**westb-23072:**
- GPU 0: 18577/97887 MiB — MATH-500 SFT Standard 25%
- GPU 1: 28945/97887 MiB — GRPO Standard 25%

### SFT Standard 25% 模型

- westd-29022: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25` ✅ 存在
- westb-23072: 11G checkpoint at `checkpoint-1870/model.safetensors` ✅ 存在

### 注意事项

1. westd-29022 上有两个"僵尸"日志（v4/v3 副本），分别只有 14/15 行，2-5/1319 进度，几乎没有推进。实际工作进程是 v3（CKA-only）和 v2（Random，已完成）。
2. GRPO CKA-only 25% v3 最接近完成（93%），预计 15-20 分钟内出结果。
3. 其他 4 个 eval 还需要数小时才能完成。

---
