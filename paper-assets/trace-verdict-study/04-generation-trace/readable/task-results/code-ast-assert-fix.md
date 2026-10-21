# code ast assert fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ast-assert-fix_20260514T164232_result.json`
- **Structured JSON:** [`009bd8f9a1e468ac91df.json`](../../sessions/00/009bd8f9a1e468ac91df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**GPU 0 状态**: RTX PRO 6000 Blackwell, 49175MiB/97887MiB 已用但无进程——驱动残留显存。GPU util 0%。尝试 `nvidia-smi --gpu-reset` 需要先排查是否有另一个 Worker 的进程依赖它，暂不操作。

**产出**:

1. **`src/assert_decompose.py`** — `AssertDecomposer` 类，通过 AST 解析 assert 语句并在安全沙盒内 eval 子表达式。支持 5 种模式：
   - `==`/`!=`/`in`/`not in` 比较
   - `assert not expr` 布尔否定
   - `abs(expr - val) < eps` 近似比较
   - 裸 `assert expr` 真值检查
   - eval 超时 1s，失败返回 None

2. **`src/vota.py`** — `_extract_assertions` 三级策略：
   - 优先取 trace event 中已有的 `actual`/`expected` 字段
   - 没有则用 `AssertDecomposer` 对源码行做实时 AST 拆解
   - 都失败才 fallback 全量 locals（标记 `[fallback: full locals]`）
   - `compress()` 新增可选参数 `source_lines: dict[int, str]`

3. **`tests/test_vota.py`** — 从 22 个增加到 35 个测试，新增覆盖：
   - HumanEval 典型格式 AST 拆解（13 个 decomposer 单测）
   - MBPP 格式、`in`/`not`/approx 等复杂比较
   - eval 失败 graceful fallback
   - 端到端 HumanEval 风格 trace → VOTA 压缩（5 个集成测试）

---
