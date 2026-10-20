# code w3 dual gpu

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w3-dual-gpu_20260516T075418_result.json`
- **Structured JSON:** [`bd2c0104ce6d839e8d2b.json`](../../sessions/bd/bd2c0104ce6d839e8d2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 验证通过。修改摘要：

**改动内容：**
- `run_gpu_group(gpu_id, condition_indices, ...)` — 子进程入口，设置 `CUDA_VISIBLE_DEVICES` 后串行跑指定条件，结果写独立 JSON 文件 (`result_cond{id}_{name}.json`)
- `run_all_conditions_parallel()` — 用 `torch.multiprocessing` spawn 两个进程：GPU0 跑条件 0,1；GPU1 跑条件 2,3；完成后从 JSON 文件汇总结果
- `run_all_conditions_serial()` — 原逻辑保留，通过 `--single-gpu` 参数触发
- 添加 `argparse`：默认双 GPU 并行，`--single-gpu` 回退单卡串行
- 子进程通过文件交换结果（避免大对象 pickle），主进程检查 exitcode 并报错

---
