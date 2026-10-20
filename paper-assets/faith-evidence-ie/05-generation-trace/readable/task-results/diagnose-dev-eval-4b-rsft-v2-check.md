# diagnose dev eval 4b rsft v2 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dev_eval_4b_rsft_v2_check_20260522T033049_result.json`
- **Structured JSON:** [`4e8e784007923ddb53e2.json`](../../sessions/4e/4e8e784007923ddb53e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**dev_eval_4b_rsft_ced_s42_v2 失败**（进程已退出，PID 157071 不存在，cuda:0 已空闲）。

**失败原因**：`--base_model /root/autodl-tmp/models/Qwen/Qwen3-4B` 路径不存在。服务器上 4B 模型在 `/root/autodl-tmp/models/Qwen3-4B`（无 `Qwen/` 子目录）。1.7B/8B/14B 在 `/root/autodl-tmp/models/Qwen/` 下，但 4B 不在。`AutoTokenizer.from_pretrained` 收到含 `/` 的路径后误判为 repo id 抛出 `HFValidationError`。

**修复**：重新提交时把 `--base_model` 改为 `/root/autodl-tmp/models/Qwen3-4B`。这与 test_eval_4b_rsft_s42_v3 修过的同一个 bug。

需要我立即重新提交修正后的 dev eval 吗？cuda:0 当前空闲（0 MiB），可以直接用。

---
