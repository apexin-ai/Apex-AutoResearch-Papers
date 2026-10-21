# audit attn k07 s44 trace

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_attn_k07_s44_trace_20260528T023617_result.json`
- **Structured JSON:** [`65125b199c3788bf1727.json`](../../sessions/65/65125b199c3788bf1727.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

溯源完成，结论如下：

## 结果

**(a) 实际日志路径**
`/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_attn_k07_long_seed44_strict_cqa1.log`

**(b) 日志中的关键参数**
- 配置行：`Config: suite=libero_10, prune=attention, keep=0.7, eps=50, gpu=0`
- Pruning 行：`Pruning: attention, keep 179/256 tokens/image (537 total, 2-layer probe)`
- PRUNE-DIAG：`n_keep=179/256`
- 结果 JSON：`keep_ratio: 0.7`

**n_keep=179/256 = 0.699，确认是 k=0.7，不是 k=0.75。**

**(c) 数据有效性**
- **数据有效。** 日志确认实际运行的是 k=0.7（179 tokens），不是 k=0.75（192 tokens）。
- 最终 SR = **52.2%**（不是之前收割的 51.6%，差异可能是收割时的四舍五入或中间值）
- 完整跑完 10 tasks × 50 eps = 500 episodes，261 成功
- 结果 JSON 已保存：`pi05_attention_k0.70_libero_10_seed44.json`
- 服务器上不存在 k=0.75 seed44 的日志文件，排除混淆可能

**之前 harvest Worker 报告的 keep=192/256=0.75 是错误的——实际日志明确是 179/256=0.7。SR 应修正为 52.2%。**

---
