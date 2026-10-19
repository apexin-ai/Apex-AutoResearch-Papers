# code eval skeleton

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_skeleton_20260512T100215_result.json`
- **Structured JSON:** [`6a3bf70e7be7ba8f0271.json`](../../sessions/6a/6a3bf70e7be7ba8f0271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件已创建并注册：

- **`eval_retrieval.py`** — 检索评估脚本，支持 BM25 baseline / StructFuse bi-encoder / fusion re-ranking 三种模式，计算 Recall@k、MRR、Structural Precision，支持多模型对比和 data-flow reachability filter
- **`eval_swebench.py`** — SWE-bench 端到端评估，pipeline: issue → StructFuse retrieval → vLLM (Qwen3.6-27B) patch generation → harness evaluation，支持断点续传，输出 Pass@1 + localization recall
- **`requirements.txt`** — 16 个核心依赖，注释说明了 torch CUDA 版本和 CodeQL CLI 的安装方式，额外加了 `requests` 和 `vllm`（eval_swebench 需要）

`eval_swebench.py` 中 `run_swebench_tests` 是框架占位，返回 `"pending"` 状态——实际 harness 集成需要根据服务器环境对接 `swebench.harness.run_evaluation` 或直接 pytest 调用。

---
