# research mepic code survey

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_mepic-code-survey_20260514T044250_result.json`
- **Structured JSON:** [`c27555ee923b86b769b4.json`](../../sessions/c2/c27555ee923b86b769b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已完成并注册。核心结论：

**MEPIC 未开源**，但核心算法可从论文完整复现，预估 ~710 行代码。关键技术点：

1. **NoPE KV 存储**: 存 key 时跳过 RoPE，仅对 query 应用 RoPE。RoPE 的 apply/remove 是简单旋转操作 `(x * cos) ± (rotate_half(x) * sin)`
2. **Fused RoPE Attention**: attention 计算前动态对 NoPE key 施加 RoPE — 标准 Flash Attention 不直接支持，需自定义 kernel 或 eager attention fallback
3. **First-Block Recomputation**: 每个 cached chunk 仅重算第一个 block（~16 tokens），处理拼接边界效应
4. **与 KVTC 天然互补**: 两者都依赖 RoPE-free keys，MEPIC 生产的 NoPE KV 可直接送入 KVTC 压缩
5. **与 CEGR 正交**: MEPIC 修复拼接边界误差，CEGR 修复压缩误差，可叠加使用

EPIC（MEPIC 前身）有[开源代码](https://github.com/DerekHJH/epic)，但技术路线不同（post-RoPE + token-level recomputation），参考价值有限。

---
