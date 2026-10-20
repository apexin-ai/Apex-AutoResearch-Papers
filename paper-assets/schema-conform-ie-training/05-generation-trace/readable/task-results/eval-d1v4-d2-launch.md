# eval d1v4 d2 launch

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d1v4_d2_launch_20260513T095132_result.json`
- **Structured JSON:** [`cc4a9aa5e53dc4358d7f.json`](../../sessions/cc/cc4a9aa5e53dc4358d7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D2 在 471/500，还有 ~29 steps × ~24s ≈ 11 分钟。D1 在 364/500，还有 ~136 steps × ~26s ≈ 59 分钟。

两个都还在跑，evaluate.py 已修复。我设一个定时回来检查。

## 当前状态

**D2 Phase 2** (PID 77141, cuda:0)
- 进度：471/500，预计 ~11 分钟完成
- GPU 0: 68% util, 40.8GB/97.9GB

**D1 v4** (PID 77066, cuda:1)
- 进度：364/500，预计 ~59 分钟完成
- GPU 1: 63% util, 54.3GB/97.9GB

**evaluate.py 修复**
- 旧代码（行 204-207）：`.replace("{{- '&lt;think>\n' }}", "{{- '&lt;think>\n\n&lt;/think>\n\n' }}")`
- 新代码：`"{%- set enable_thinking = false -%}" + tokenizer.chat_template`（前缀注入，直接在 Jinja2 模板级别禁用 thinking）
- 验证通过

**Merged 目录**：两个都还没生成（训练未完成）

**下一步**：D2 预计 ~11 分钟完成，完成后自动 merge，然后启动 eval。建议 ~12 分钟后回来检查。

---
