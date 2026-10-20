# recovery multiseed 14391

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_multiseed-14391_20260522T174557_result.json`
- **Structured JSON:** [`e884b0fe4f42d6038213.json`](../../sessions/e8/e884b0fe4f42d6038213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

24/204 at 02:16 (~12%)。稳定 ~2.2 问题/min。

**实验状态总结：**

实验在 westd-14391 上稳定运行中。所有自动化已就绪：

1. **FOLIO seed=789**: 24/204 (12%), ~2.2 问题/min, 预计 ~03:40 完成
2. **PW seeds 42/123/456**: 监控脚本 (PID 11073) 会在 FOLIO 完成后自动链式启动 3 个 PW seed 实验
3. **vLLM**: 健康运行中 (port 8000, llama-8b, ~400 tokens/s generation)

**预计时间线：**
- FOLIO seed=789 完成: ~03:40 (UTC+8)
- PW seed=42 完成: ~08:00
- PW seed=123 完成: ~12:20
- PW seed=456 完成: ~16:40

**查看进度命令：**
- `tail -20 /tmp/monitor_chain.log` — 总体进度
- `grep -c "overall" /tmp/llama8b_folio_seed789.log` — FOLIO 详细进度
- `tail -20 /tmp/llama8b_pw_all.log` — PW 实验进度（FOLIO 完成后）

**已完成的验证：**
- Tiebreaking: SC 和 SICA 均使用 D061 alphabetical sorted ✅
- 数据: FOLIO 204 条, PW 600 条 ✅
- 模型: 从 westd-16639 中转到 14391 (~20MB/s, 5 分钟) ✅
- vLLM: 正常运行, Triton JIT 编译完成 ✅

---
