# debug kv bench 001 fix

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_kv-bench-001-fix_20260512T024923_result.json`
- **Structured JSON:** [`a8c25ff3d8f0b76d1ef8.json`](../../sessions/a8/a8c25ff3d8f0b76d1ef8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。变更汇总：

| 修改 | 说明 |
|------|------|
| 移除 `\x04` 字节 (L318) | 脚本中嵌入了不可打印的 EOT 控制字符，Python 3.12 抛 `SyntaxError: invalid non-printable character U+0004`，**脚本完全无法启动**。这是根因。 |
| `dtype` → `torch_dtype` (L317) | `dtype` 在 transformers 4.57 碰巧能用，但 `torch_dtype` 是规范参数名，跨版本更安全 |
| 顶层 `try/except` (L422-429) | 未捕获异常的 traceback 写入 `kv_bench_001.log`，不再因 tmux 退出而丢失 |

用户看到的 4 条 99-token 日志来自 `\x04` 字节被引入前的一次运行。那次运行的静默退出最可能是某个未被捕获的异常（traceback 写到了 stderr，tmux 关闭后丢失）。现在有了顶层异常捕获，下次运行时无论什么错误都会写入日志文件。

---
