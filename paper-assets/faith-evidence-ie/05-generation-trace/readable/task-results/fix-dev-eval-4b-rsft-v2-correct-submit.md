# fix dev eval 4b rsft v2 correct submit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_dev_eval_4b_rsft_v2_correct_submit_20260522T040924_result.json`
- **Structured JSON:** [`46e4c1e0a021c76843c9.json`](../../sessions/46/46e4c1e0a021c76843c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

- **失败原因**：前 3 次分别是 base_model 路径错误、data_path 指向 re-docred 目录（无 `dev.json`）、`--split dev_revised` 不在 argparse 的合法选项中
- **修正**：改用 `--data_path /root/autodl-tmp/data/docred --split dev`（原始 DocRED，与之前成功的 eval 一致）
- **当前状态**：PID 161216 在 GPU 0 上运行，已开始推理（985 docs，~8.4s/doc，预计 ~2.3h）

---
