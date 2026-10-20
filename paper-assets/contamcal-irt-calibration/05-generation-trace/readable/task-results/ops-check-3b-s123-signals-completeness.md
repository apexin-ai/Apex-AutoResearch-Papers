# ops check 3B s123 signals completeness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-3B-s123-signals-completeness_20260516T185751_result.json`
- **Structured JSON:** [`5b9834432185e6b701f7.json`](../../sessions/5b/5b9834432185e6b701f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Completeness Matrix — Qwen2.5-3B Signals

### s123 (critical path)

| Dosage | Dir | s1_emb | s2_minkpp | s4_selfcrit | merged | Status |
|--------|-----|--------|-----------|-------------|--------|--------|
| d000 | `Qwen2.5-3B_d000_s123_a32/` | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | **COMPLETE** |
| d005 | `Qwen2.5-3B_d005_s123/` | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | **COMPLETE** |
| d025 | `Qwen2.5-3B_d025_s123/` | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | **COMPLETE** |
| d100 | `Qwen2.5-3B_d100_a32_s123/` | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | **COMPLETE** |

### s42 (RRF pairing)

| Dosage | Dir | signals | merged | Status |
|--------|-----|---------|--------|--------|
| d000 | `Qwen2.5-3B_d000_a32_s42/` | 9/9 | 3/3 | **COMPLETE** |
| d005 | `Qwen2.5-3B_d005_a32_s42/` | 9/9 | 3/3 | **COMPLETE** |
| d025 | `Qwen2.5-3B_d025_v3_s42/` | 9/9 | 3/3 | **COMPLETE** |
| d100 | `Qwen2.5-3B_d100_a32_s42/` | 9/9 | 3/3 | **COMPLETE** |

### Checkpoints confirmed

```
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123
```

---

## Llama-3.2-3B 状态

**Checkpoints**: d000/d005/d025/d100 s42 全部存在。无 s123 seed checkpoints。

**Signals**: `Llama-3.2-3B_d000_s42/` 正在计算中，当前进度：

| benchmark | s1_emb | s2_minkpp | s4_selfcrit | merged |
|-----------|--------|-----------|-------------|--------|
| arc_challenge | ✅ | ✅ | ✅ | ✅ |
| gsm8k | ✅ | ❌ | ❌ | ❌ |
| mmlu | ✅ | ✅ | ❌ (chunking中) | ❌ |

其余 Llama dosages (d005/d025/d100) 尚无 signals 目录。

---

## 结论

**3B s123 全部 4 个 dosage 的 signals 已 100% 完成，s42 也全部就绪。RRF 聚合 → pooled IRT 的数据依赖已满足，可以立即推进。**

Llama 是独立维度，不阻塞 3B 论文 critical path。

---
