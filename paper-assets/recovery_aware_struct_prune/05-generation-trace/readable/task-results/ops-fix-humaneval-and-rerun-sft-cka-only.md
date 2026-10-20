# ops fix humaneval and rerun sft cka only

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_humaneval_and_rerun_sft_cka_only_20260519T073718_result.json`
- **Structured JSON:** [`6a014f85db7bfacb06f2.json`](../../sessions/6a/6a014f85db7bfacb06f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常：

- **修复完成**：`import sys` 已添加（第 10 行），`subprocess.run([sys.executable, tmp_path], ...)` 替换了裸 `python`（第 52 行）
- **tmux session** `eval_humaneval_sft_cka_only_20_2048_v2` 已启动
- **模型正在加载**：log 显示正在从 `sft_cka_only_20` 加载，检测到 Non-uniform MLP 结构
- **Registry** 状态：RUNNING，hypothesis/parent 已设置

模型加载完成后会占用 cuda:1 并开始推理 164 道 HumanEval 题目。

---
