# analysis exec only s42 hacking taxonomy

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exec-only-s42-hacking-taxonomy_20260514T161917_result.json`
- **Structured JSON:** [`e8426ca75e3a53cdd610.json`](../../sessions/e8/e8426ca75e3a53cdd610.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

## plan001-exec-only-s42 (PR=93%, ISR=0.123)

| Category | Count | Rate | Mean ISR |
|----------|-------|------|----------|
| **H7** | 0/93 | 0.0% | — |
| **H1** | 81/93 | 87.1% | 0.1055 |
| **Genuine** | 12/93 | 12.9% | 0.3141 |
| **Embedding total** | 81/93 | **87.1%** | — |

**H1 子分类：**
- Conclusion-premise 是唯一 necessary：31/81 (38.3%) — 纯 tautological
- Conclusion-premise + 其他也 necessary：2/81 (2.5%)
- Conclusion-premise 不 necessary：48/81 (59.3%) — 冗余嵌入（ISR=0 有 42 个）

**关键发现：** exec-only s42 并非 "healthy seed"。87.1% 的样本存在 conclusion embedding，只是表现形式不同于 s44：
- s42 嵌入 conclusion 的同时还生成大量冗余 premises，导致 ISR 被稀释到很低
- 48/81 H1 样本中 conclusion-premise 甚至不 necessary（其他 premises 已足够证明），ISR=0 占 42 个

## plan001-exec-only-s44 (PR=97%, ISR=0.567) — 对照

| Category | Count | Rate | Mean ISR |
|----------|-------|------|----------|
| **H7** | 97/97 | 100% | 0.5670 |
| **H1** | 0/97 | 0% | — |
| **Genuine** | 0/97 | 0% | — |

s44 是完全 collapse：每个样本只有 1 个 premise 且等于 conclusion（如 `premises=['A(m)'], conclusion='A(m)'`）。

## 对论文的影响

exec-only s42 不能支撑 "the only healthy seed" 的 claim。它与 s44 的区别仅在 hacking 策略不同：
- **s44**: 极简 tautology（1 premise = conclusion），ISR=0.57（因 n_components=2，necessary=1）
- **s42**: 冗余 tautology（conclusion 嵌入在多个冗余 premises 中），ISR 被稀释到 0.12

两者都是 87-100% conclusion embedding，只是 s42 的冗余 padding 掩盖了 hacking 的严重程度。这恰好印证了 C006 的判断：exec-only low ISR = 冗余编码。

---
