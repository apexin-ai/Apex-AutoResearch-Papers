# code mvp framework

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_framework_20260514T123238_result.json`
- **Structured JSON:** [`dc76dca387b801ee4bcf.json`](../../sessions/dc/dc76dca387b801ee4bcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个模块导入通过（pandas 未安装，mvp_pipeline 已做 conditional import 处理，不影响导入）。

创建完成：
- `dtd_types.py` — 共享 dataclass（TraceEvent, TraceSegment, ScoredSegment）和序列化工具
- `trace_collector.py` — sys.settrace 注入收集 trace，subprocess 隔离执行
- `structural_segmenter.py` — 按 call subtree / loop iteration / exception chain 分段
- `line_segmenter.py` — 固定窗口 baseline 分段
- `teacher_scorer.py` — DeepSeek API 打分，并发批处理，JSON 解析带 fallback
- `bugsinpy_setup.py` — 30 个候选 bug 实例，checkout buggy/fixed 版本
- `mvp_pipeline.py` — 端到端 4-condition 对比（no_trace / full_trace / structural_filtered / line_filtered）

---
