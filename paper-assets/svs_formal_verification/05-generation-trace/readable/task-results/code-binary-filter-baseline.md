# code binary filter baseline

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_binary_filter_baseline_20260514T083237_result.json`
- **Structured JSON:** [`135680317e9a1fc24a37.json`](../../sessions/13/135680317e9a1fc24a37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**创建的文件：**
- `evaluation/binary_filter_baseline.py` — Binary Filter + SC baseline，IC 阈值过滤 + majority vote
- `evaluation/self_certainty_baseline.py` — Self-Certainty baseline，基于 token logprob 均值选链

**修改的文件：**
- `types.py` — Chain dataclass 新增 `logprobs: Optional[list[float]]` 字段
- `generation/chain_sampler.py` — API 调用添加 `logprobs=True, top_logprobs=1`，`_call_llm` 返回 `(content, token_logprobs)` 元组，`sample` 将 logprobs 存入 Chain
- `evaluation/__init__.py` — 导出两个 baseline 模块的公开函数

远程 import 验证通过。

---
