# research code survey

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_code-survey_20260512T075744_result.json`
- **Structured JSON:** [`8539e9e6402ed5f5c9fb.json`](../../sessions/85/8539e9e6402ed5f5c9fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册（`art_20260512_f360d5`）。

核心发现：

- **Token Filtering**：无公开代码库。算法从论文提取——EMA centroid（γ=0.9）+ variance-aware fusion（α动态计算）+ adaptive threshold，仅作用于后50%层的 attention token 轴。需从零实现。
- **TEAL**：[FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL) 代码完整。核心一行 `x.abs().gt(threshold) * x`，threshold 通过 activation histogram 的 inverse CDF 获得。Monkeypatch 方式集成 HF 模型，sparsify 所有 7 个 projection 的输入激活，默认 40-50% sparsity。
- **关键差异**：Token Filtering 是 token 粒度的在线过滤（无需校准），TEAL 是 element 粒度的离线校准 pruning。两者作用轴正交，可组合但需监控 combined pruning rate 防止过度稀疏。

---
