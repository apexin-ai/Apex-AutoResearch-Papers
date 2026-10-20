# exp gemma definitive fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma-definitive-fix_20260520T082520_result.json`
- **Structured JSON:** [`79741321678aa452ec49.json`](../../sessions/79/79741321678aa452ec49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**三个问题修复状态**:
1. **Task list** ✅ — 确认 11 个精确 task name，脚本已包含
2. **System role** ✅ — `sanitize_messages_for_template` 已在两个代码路径中调用，无需修改
3. **vLLM 内存** ✅ — 关键发现：`enable_prefix_caching=False` 解决 EngineCore 崩溃（prefix caching 与 Gemma-2 SWA 交互导致内存泄漏）

**Dry-run**: find-non-living-thing 1 episode 成功（internal=0.0, det=58.0, 60 prompts 无崩溃）

**全量启动**: tmux `gemma-11tasks` 运行中，11 tasks × 20 episodes，GPU 1 正常加载 (27979MiB, 93% util)，GPU 0 未受影响。预计 ~15 小时完成。

---
