# code plan003 fix streaming parallel

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-fix-streaming-parallel_20260520T135707_result.json`
- **Structured JSON:** [`1a2ab47db3dfc69e2a51.json`](../../sessions/1a/1a2ab47db3dfc69e2a51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **修复 annotate.py**：`annotate_batch` 新增 `output_path` 参数，每条 sample 完成后立即 append 到 JSONL（streaming write）。`run_single` 传入 `output_path`。原有的 resume 机制（`load_existing_results`）自动兼容——进程重启时读取已有 JSONL 行数跳过已完成的 sample。
2. **`--model` 参数已内置**，无需修改。
3. **杀掉 4 个旧进程**（2 组 `--all` 互相冲突，且无 streaming write）。
4. **3 路并行重启**：llama4(438497), qwen3(438843), deepseek(439116)，各写独立 JSONL，不冲突。
5. **streaming write 已验证生效**：llama4 已写 12 行，qwen3 5 行，deepseek 4 行。

每个进程跑 9 个组合（3 datasets × 3 prompts），1500 samples/组合，预计 ~0.5s/sample × 13500 ≈ 1.9 小时/进程。

---
