# research prophetkv survey v2

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prophetkv-survey-v2_20260514T045403_result.json`
- **Structured JSON:** [`f6b8cea12098a404c382.json`](../../sessions/f6/f6b8cea12098a404c382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**ProphetKV 方法**: 用 query attention column sum 跨所有层融合（$\bar{\alpha}(t) = \frac{1}{L}\sum_l \alpha_l(t)$），20% recomputation 达 96-101% full prefill 精度。明确拒绝 early-layer prediction。无开源代码但公式简单可复现。

**推荐实现路径**:
1. **MVP Phase 0**: 位置先验 p_r（boundary=1.0, 其余 uniform），~50 行，验证 RABA/CEGR pipeline
2. **Phase 1**: ProphetKV-style query probe — hook 到 HF attention layers，收集 per-layer attention column sum，均值融合，~200 行
3. **RABA 集成**: p_r 高的 token 分配更少 compression bits (weight = 1-p_r)，~100 行修改 KVTC DP solver
4. **CEGR 集成**: restore_score = p_r × compression_error，topk 选择，~80 行

**关键风险**: MEPIC NoPE KV cache 与标准 RoPE attention 不兼容，需手动实现 RoPE-query × NoPE-key attention 计算 p_r。kvpress 的 hook 机制可复用但 attention 计算需定制。

**总代码量**: ~580 行。

---
