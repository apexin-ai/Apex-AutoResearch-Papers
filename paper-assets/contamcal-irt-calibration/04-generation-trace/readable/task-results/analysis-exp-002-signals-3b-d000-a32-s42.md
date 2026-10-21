# analysis exp 002 signals 3B d000 a32 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_002_signals_3B_d000_a32_s42_20260516T102219_result.json`
- **Structured JSON:** [`1bd7e9b0a2edfd07f5a3.json`](../../sessions/1b/1bd7e9b0a2edfd07f5a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**SUCCESS**

### Signal 生成矩阵（3 benchmark × 3 signal = 9/9 完成）

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | N items |
|-----------|:---:|:---:|:---:|---:|
| mmlu | ✓ (7.6M) | ✓ (2.8M) | ✓ (3.2M) | 14,042 |
| gsm8k | ✓ (717K) | ✓ (266K) | ✓ (310K) | 1,319 |
| arc_challenge | ✓ (650K) | ✓ (245K) | ✓ (284K) | 1,172 |

### 关键数字
- **总样本**: 16,533 items (14042 + 1319 + 1172)
- **运行时间**: ~3h 9min (15:09 → 18:18)
- **GPU 时间**: 3.24 GPU-hours
- **失败/缺失**: 0
- **非关键 warning**: bitsandbytes libnvJitLink.so.13 加载失败（不影响 signal 计算）、faiss AVX512-SPR 回退到 AVX512（正常）

### 输出路径
`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/`

Registry 已更新为 DONE/success。

---
