# submit d100 s123 para eval cuda2 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d100_s123_para_eval_cuda2_v2_20260515T185049_result.json`
- **Structured JSON:** [`ea8eb2cbd5253ad58e2c.json`](../../sessions/ea/ea8eb2cbd5253ad58e2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总报告如下：

---

## 报告

### 1. 子任务 A: d100_s123_para_aligned eval on cuda:2

**无需重新提交 — 已在运行。** PID 614412 正在 cuda:2 上执行完全相同的 eval 命令（发现时已运行 2m47s）。

- PID: **614412**
- GPU: cuda:2, 占用 8358 MiB
- Registry: `exp_001_eval_3B_d100_s123_para_aligned_v2` → **RUNNING**
- 前置条件均满足：checkpoint (114MB) ✅, paraphrases (4 files) ✅

### 2. 子任务 B: v2 Signals 3B 产出完整性

文件命名规范: `signal_s{N}_{type}_{bench}.json` / `signals_merged_{bench}.json`

| Dosage | Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | merged | Status |
|--------|-----------|:---:|:---:|:---:|:---:|--------|
| d000_s42 | mmlu | ✅ 7.9M | ✅ 2.9M | ❌ | ❌ | **Incomplete** |
| d000_s42 | gsm8k | ✅ 734K | ✅ 272K | ✅ 317K | ✅ 243K | Complete |
| d000_s42 | arc_challenge | ✅ 665K | ✅ 250K | ✅ 290K | ✅ 235K | Complete |
| d005_s42 | mmlu | ✅ 7.9M | ✅ 2.9M | ❌ | ❌ | **Incomplete** |
| d005_s42 | gsm8k | ✅ 734K | ✅ 272K | ❌ | ❌ | **Incomplete** |
| d005_s42 | arc_challenge | ✅ 665K | ✅ 250K | ✅ 290K | ✅ 235K | Complete |
| d025_s42 | mmlu | ✅ 7.8M | ❌ | ❌ | ❌ | **Incomplete** |
| d025_s42 | gsm8k | ✅ 734K | ✅ 272K | ✅ 317K | ✅ 244K | Complete |
| d025_s42 | arc_challenge | ✅ 664K | ✅ 250K | ✅ 291K | ✅ 235K | Complete |
| d100_s42 | mmlu | ❌ | ❌ | ❌ | ❌ | **Empty** |
| d100_s42 | gsm8k | ❌ | ❌ | ❌ | ❌ | **Empty** |
| d100_s42 | arc_challenge | ❌ | ❌ | ❌ | ❌ | **Empty** |

### 3. v3 skip-completed 分析

**可跳过（5 个完整 benchmark-dosage）：**
- d000/gsm8k, d000/arc_challenge
- d005/arc_challenge
- d025/gsm8k, d025/arc_challenge

**需补跑个别 signal（4 个不完整）：**

| 组合 | 缺失 signals |
|------|-------------|
| d000/mmlu | s4_selfcritique → merged |
| d005/mmlu | s4_selfcritique → merged |
| d005/gsm8k | s4_selfcritique → merged |
| d025/mmlu | s2_minkpp + s4_selfcritique → merged |

**需从头跑（3 个空目录）：**
- d100_s42: mmlu, gsm8k, arc_challenge（全部 signal）

**总计**: v3 需处理 **7** 个 benchmark-dosage 组合（4 补跑 + 3 全新）。

---
