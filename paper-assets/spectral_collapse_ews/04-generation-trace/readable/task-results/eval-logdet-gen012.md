# eval logdet gen012

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_logdet_gen012_20260516T142415_result.json`
- **Structured JSON:** [`7de83b87c3e82d97138d.json`](../../sessions/7d/7de83b87c3e82d97138d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Gen | effective_rank | log_det | top SV | 
|-----|---------------|---------|--------|
| 0 | 417.55 | 2366.68 | 1942.82 |
| 1 | 491.77 | 2464.76 | 803.96 |
| 2 | 496.44 | 2469.93 | 712.03 |

**关键发现：log_det 和 eff_rank 都是单调递增，不是递减。**

分析：
- Gen 0→1: eff_rank +74.2, log_det +98.1 — 大幅增加
- Gen 1→2: eff_rank +4.7, log_det +5.2 — 增速急剧放缓（饱和趋势）
- Top SV 下降明显（1943 → 804 → 712），说明表征从 Gen 0 的 "单方向主导" 逐步均匀化

**解读**：410M 在 Gen 0-2 尚未出现 spectral collapse。相反，表征空间利用率在增加（self-distillation 在早期反而"解压"了表征）。但 Gen 1→2 增速已接近停滞 — 如果后续 gen 出现拐点/下降，那才是 collapse 的 EWS 信号。

**对 go/no-go 判断**：log-det 目前不支持"已经在 collapse"的假设；需要 Gen 3+ 的数据来观察是否出现拐点。

---
