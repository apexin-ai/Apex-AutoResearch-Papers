# analysis alpha sweep a050 s44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a050_s44_20260517T063620_result.json`
- **Structured JSON:** [`73f5a82c9fb0675029e6.json`](../../sessions/73/73f5a82c9fb0675029e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**s44 PermG: 4/8 significant**
- ECE 通道 4/4 全部显著 (p=0.004-0.027)
- token_entropy 通道 0/4 全部 marginal (p=0.056-0.092)

**Cross-seed 汇总 (一致参数 n_perm=5000)**：

| Seed | PermG sig | ECE channels | entropy channels |
|------|-----------|-------------|-----------------|
| s42 | 4/8 | 4/4 | 0/4 |
| s43 | 7/8 | 4/4 | 3/4 |
| s44 | 4/8 | 4/4 | 0/4 |

**注意**：与先前报告的 s42=0/8、s43=6/8 有差异，因本次使用统一参数重新计算。

**关键发现**：
1. **Drift 跨 seed 高度一致** (distinct_1 drift: -37.3/-36.5/-37.4%，std<0.5%)，collapse 是 deterministic 的
2. **ECE -> downstream Granger 信号完全 robust** (12/12 across 3 seeds)
3. **token_entropy -> downstream 信号 borderline** (3/12，仅 s43 有部分显著)
4. alpha=0.50 不是 null boundary，而是 transitional zone：ECE 检测可靠，entropy 检测不可靠

报告已写入 `artifacts/alpha_sweep_a050_s44/report/` 并注册。

---
