# code exit code sentinel

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exit-code-sentinel_20260514T185548_result.json`
- **Structured JSON:** [`9ff33e6921a7cd0ccaec.json`](../../sessions/9f/9ff33e6921a7cd0ccaec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

改动说明：

- **L276-279**：`main()` 正常完成后，在 `args.output_dir/EXIT_CODE` 写入 `0`
- **L282-291**：`if __name__` 块用 try-except 包装 `main()` 调用；异常时重新解析 args 获取 output_dir，写入 `1` + 错误信息，然后 re-raise 保留原始异常栈

---
