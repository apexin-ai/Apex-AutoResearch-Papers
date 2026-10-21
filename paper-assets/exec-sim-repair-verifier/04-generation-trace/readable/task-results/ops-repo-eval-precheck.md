# ops repo eval precheck

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_repo-eval-precheck_20260516T141849_result.json`
- **Structured JSON:** [`137ed6e1070cc5c9f178.json`](../../sessions/13/137ed6e1070cc5c9f178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成。关键发现：

- **CLS**: 流程就绪，checkpoint-2211 已有（训练仍在进行，step 2211/6633，epoch 1/3）
- **CWM**: checkpoint 目录为空，需等训练落盘首个 checkpoint
- **依赖/数据/磁盘**: 全部 PASS
- **注意**: eval 脚本默认 model_name 是 Qwen，必须覆盖为 `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`；推荐用 `run_repo_eval.sh` wrapper（自动从 adapter_config.json 读取基座模型路径）

报告已写入 `artifacts/repo-eval-precheck.md`。

---
