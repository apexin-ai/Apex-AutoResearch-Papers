# diagnose exp downsample cls func v3 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-downsample-cls-func-v3-eval_20260519T070808_result.json`
- **Structured JSON:** [`0e2933dc0d13402e4c89.json`](../../sessions/0e/0e2933dc0d13402e4c89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：GPU 显存 OOM**。进程在推理到 960/9784 样本时静默死亡，日志无 traceback。GPU 2 残留 100% GPU-Util + 0MiB memory 的异常状态，是 CUDA driver 级 OOM 杀进程的典型表现。Qwen3-4B 模型本身约 8-9GB，但 SWE-bench test set 中存在超长 git diff，KV cache 撑爆 32GB VRAM。

无部分结果（脚本在推理全部完成后才写文件）。

修复建议：
1. 加 `max_length` 截断超长输入
2. 推理循环加 OOM try/except + `torch.cuda.empty_cache()`
3. predictions 改为逐条 append JSONL（防中断零产出）
4. 用 `cuda:1`（当前空闲）重跑，GPU 2 需重置

报告已保存到 `artifacts/diagnose_exp-downsample-cls-func-v3-eval.md`。

---
