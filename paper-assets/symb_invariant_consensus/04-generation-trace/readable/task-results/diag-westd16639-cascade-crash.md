# diag westd16639 cascade crash

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd16639-cascade-crash_20260518T163725_result.json`
- **Structured JSON:** [`b2e72030679275728acc.json`](../../sessions/b2/b2e72030679275728acc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**崩溃根因：AutoDL 平台级进程终止，两波 kill。**
- **00:05:54** — exp032 (GPU 0) 和 exp033 (GPU 1) 的 vLLM 在同一秒收到 SIGTERM。两个不同 GPU 上的独立进程同时死亡，排除应用 bug，确认外部 kill。
- **00:16:16~22** — 所有剩余进程（包括 00:15:17 才启动的 exp034）同时消失。

**系统状态正常**：内存 956GB 可用，磁盘 40%，4 GPU 全部空闲可用。不是 OOM/磁盘满/内部崩溃。

**exp034 StrategyQA extraction_rate 2.78% 的原因**：`run_full_mvp.py` 将 StrategyQA 归类为 `math` domain，使用数学约束提取 prompt（期望 equation/inequality），对常识推理 Yes/No 题完全不适配。需要专用 prompt。

**重启建议**：先查 AutoDL 控制台确认账户/平台状态。exp035 (42/60 剩余) 和 exp032/033 (~90/600 剩余) 可 `--resume` 恢复。exp034 需先修复 extraction prompt 再重启。

---
