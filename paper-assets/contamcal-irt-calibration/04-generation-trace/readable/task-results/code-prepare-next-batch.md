# code prepare next batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_next_batch_20260516T150102_result.json`
- **Structured JSON:** [`c029146e9cdf088b0f11.json`](../../sessions/c0/c029146e9cdf088b0f11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. pooled_irt_rrf_n25_v2 — **已完成**

进程不在了，输出完整（mmlu/gsm8k/arc_challenge + pooled JSON）。最后修改时间 22:47。

关键 gamma 结果（4PL+gamma, RRF exposure）：

| Benchmark | N_models | gamma mean | 95% CI | 排除零？ | raw_MAE | cal_MAE |
|-----------|----------|-----------|--------|---------|---------|---------|
| MMLU | 8 (1.5B only) | **-0.404** | [-1.84, 1.07] | **No** | — | — |
| GSM8K | 16 | — | — | — | 0.153 | **0.035** |
| ARC | 8 (1.5B only) | **1.513** | [0.23, 2.87] | **Yes** | 0.009 | 0.086 |

注意：MMLU/ARC 只有 N=8（1.5B），0.5B 缺失。ARC 的 cal_MAE > raw_MAE（校准恶化）。PPP=0.006/0.0 偏低。

---

### 2. mmlu_domain_gamma_n24 — **已完成**（7/7 domain 有输出）

v2 log 显示 sampling 时 chains 1&4 报 "Operation not permitted"，但所有 7 个 domain 都已产出 `irt_results.json`。

| Domain | N_models | gamma | 95% CI | 排除零？ | PPP |
|--------|----------|-------|--------|---------|-----|
| STEM_Math | 23 | **+0.969** | [0.53, 1.43] | **Yes** | 0.438 |
| STEM_Science | 23 | **+0.838** | [0.39, 1.27] | **Yes** | 0.807 |
| STEM_CS_Eng | 23 | +0.197 | [-0.45, 0.84] | No | 0.892 |
| Medical | **24** | **-0.199** | [-0.34, -0.06] | **Yes** | 1.0 |
| Humanities | 21 | **-0.407** | [-0.78, -0.04] | **Yes** | 1.0 |
| Social_Sciences | 21 | **-0.497** | [-0.83, -0.15] | **Yes** | 1.0 |
| Business_Law | 21 | -0.168 | [-0.54, 0.23] | No | 1.0 |

**Simpson's paradox confirmed**：STEM（Math/Science）gamma > 0（contamination inflates），人文社科（Humanities/Social/Medical）gamma < 0（contamination deflates）。5/7 domains 统计显著。

---

### 3. GPU 任务状态

| GPU | Util | Mem | 任务 | PID | 状态 |
|-----|------|-----|------|-----|------|
| 0 | 58% | 7.2G | 1.5B-Instruct para_aligned eval | 799315 | GSM8K paraphrased 50% |
| 1 | 91% | 7.4G | 1.5B instruct eval | 782625 | **HF 连接超时重试中** |
| 2 | 0% | 1.5G | 0.5B-Instruct eval | 797754 | MMLU done, 可能加载 gsm8k |
| 3 | 0% | 0G | **空闲** | — | — |
| 4 | 85% | 8.3G | Llama-3.2-3B eval | 796493 | running ~24min |
| 5 | 53% | 3.6G | 3B_d000_s123 signals (mmlu s4) | 780943 | running ~139min |

---

### 问题标注

1. **PID 782625（1.5B instruct eval on GPU 1）卡在 HF gsm8k 下载超时**。反复 retry 中，没有 `source /etc/network_turbo`。虽然 fallback 到了 cached dataset，但后续 README.md 请求又卡住了。可能需要 kill 重启并加 network_turbo。

2. **pooled IRT N=25 v2 实际只有 N=8 per benchmark**（仅 1.5B）。config 声明 scales=["0.5B", "1.5B"] 但 MMLU/ARC 的 models 列表全是 1.5B。需要确认是否 0.5B 数据缺失导致被过滤掉。

3. **GPU 3 空闲**，可以调度新任务。

---
