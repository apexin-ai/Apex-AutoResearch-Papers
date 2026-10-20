# code graph pipeline

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_graph-pipeline_20260517T055150_result.json`
- **Structured JSON:** [`e906d7d62e0abfe8fe41.json`](../../sessions/e9/e906d7d62e0abfe8fe41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。创建了以下文件：

- **`src/graph_construction.py`** — `build_graph()` 将 STAC trace 转为 PyG Data（节点=tool call，边=data-flow dependency via string matching，fallback sequential），`build_dataset()` 批量转换，`build_tool_vocab()` 自动构建词表
- **`src/data/benign_generator.py`** — `generate_benign_traces()` 从 STAC 数据提取 tool inventory，建 type-compatible compatibility graph，随机 walk 生成带 branching 的合法 tool chain，输出格式与 STAC 完全一致
- **`src/data/__init__.py`** + **`src/__init__.py`** — 空包文件
- **`tests/test_graph_construction.py`** — 覆盖 graph 构建（含 data-flow edge 验证）、dataset 构建、vocab 构建、benign generator 格式和端到端 graph 转换

本地 torch 因磁盘配额装不了，但语法验证通过，benign_generator 逻辑测试通过。在远程服务器（有 PyTorch + PyG）上跑 `python tests/test_graph_construction.py` 即可完整验证。

---
