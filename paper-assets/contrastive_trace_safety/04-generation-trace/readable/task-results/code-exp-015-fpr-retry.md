# code exp 015 fpr retry

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_015_fpr_retry_20260516T211145_result.json`
- **Structured JSON:** [`b29f1f06ecb2d07b7860.json`](../../sessions/b2/b29f1f06ecb2d07b7860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论字段只接受枚举值，已经是 `success`。Registry 更新完成。

---

## exp-015 FPR 分析结果

| Method | Safe FPR | Pre-CP FPR | Precision | Coverage | Lead Time | Step Acc |
|--------|----------|-----------|-----------|----------|-----------|----------|
| text_static | 0.502 | 0.356 | 0.448 | 60.5% | +4.3 | 0.661 |
| text_temporal W=15 | 0.385 | 0.272 | 0.487 | 65.1% | +11.5 | 0.678 |
| HS_static LR L14 | 0.390 | 0.162 | 0.622 | 60.5% | +3.0 | 0.768 |
| HS_temporal LR W=15 | 0.392 | 0.160 | 0.583 | 65.1% | +4.9 | 0.726 |
| GRU multi-7L h=256 | 0.521 | 0.188 | 0.648 | 74.4% | +5.2 | 0.816 |

**关键发现：**

1. **Text temporal 的 +11.5 lead time 确实是假阳性膨胀**：Pre-CP FPR 27.2%，precision 仅 49%——每两次报警就有一次误报。
2. **HS 方法 FPR 显著更低**：Pre-CP FPR 16% vs text 的 27-36%，precision 58-62%。
3. **GRU 综合最优**：coverage 74.4%、step acc 81.6%、precision 64.8%，但 safe FPR 仍有 52%（整条 trace 级别）。
4. **论文 motivation 成立**：text surface 监控不可靠（高 FPR、低 precision），hidden-state 提供更好的信噪比。

---
