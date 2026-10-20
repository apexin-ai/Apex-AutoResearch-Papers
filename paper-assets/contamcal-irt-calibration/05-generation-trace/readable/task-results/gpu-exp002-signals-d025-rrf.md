# gpu exp002 signals d025 rrf

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp002_signals_d025_rrf_20260514T182659_result.json`
- **Structured JSON:** [`4d107d67270b6926f8b3.json`](../../sessions/4d/4d107d67270b6926f8b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个子任务状态汇总：

---

### 子任务 A：exp-002 signal pipeline on d025
- **状态**: RUNNING on GPU 2 (PID 422128, tmux session `exp002-signal-d025-05B`)
- **任务**: 3 个 benchmark (mmlu → gsm8k → arc_challenge)，信号 embedding + minkpp + selfcritique
- **ConStat (S3) 自动跳过**: d025 的 eval_results 目录是 `_aligned` 后缀，run_batch.py 路径约定不匹配，ConStat 条件不满足
- **输出**: `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d025_s42/`
- **预计 ~20 min**

---

### 子任务 B：RRF exposure 排序调查结果

**原始信号排序 (期望 d000 < d005 < d100):**

| 信号 | mmlu | gsm8k | arc_challenge |
|------|------|-------|--------------|
| S1 embedding | OK | OK | OK |
| S2 minkpp | **反向** (d100<d005<d000) | **反向** | **反向** |
| S4 selfcritique | OK | d005/d100 互换 | OK |

**两个核心问题:**
1. **S2 minkpp 极性相反**: 高值 = 不太可能被记忆。所有 3 个 benchmark 全部反向。如果直接做 RRF 融合不翻转极性，d000 会被推高
2. **S1 embedding 基线非零**: d000 的 gsm8k s1 均值 = 0.6131（Director 报告的那个 0.613），clean model 天然有较高 embedding 相似度基线

**Delta exposure 方案验证:**
- `delta(model, item) = signal(model, item) - signal(d000, item)`
- delta_s1: d000=0, d005=+0.016~0.085, d100=+0.197~0.379 — **完美单调递增**
- delta_s2: d000=0, d005=-0.20~-0.30, d100=-0.27~-0.37 — 方向正确（更负 = 更污染）
- delta_s4: 信号弱且噪声大，区分度不高

**结论**: Delta exposure 方案可行，同时 RRF 融合前必须翻转 S2 minkpp 极性（取负或 `1 - normalized_value`）。

---
