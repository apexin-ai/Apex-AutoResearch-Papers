# experiment exp code multi source

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_code_multi_source_20260520T102719_result.json`
- **Structured JSON:** [`8e6a3d02a0f090f4b315.json`](../../sessions/8e/8e6a3d02a0f090f4b315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 占用 100% GPU、7793 MiB 显存。实验正常运行。

**状态汇总：**
- 脚本：`/root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py`
- PID: 308219，cuda:1，GPU 100% 利用
- Vocab-only 已完成：
  - no_label: K*=2 (0v1=0.7891, 1v2=0.6353, 2v3=0.5121)
  - with_label: K*=2 (0v1=0.7900, 1v2=0.6440, 2v3=0.5118)
- Unified scorer 正在 rescoring（Qwen-1.5B 重新计算 3 个 generator 的 surprisal），预计还需 ~30 分钟
- 注册实验：exp_code_multi_source, status=RUNNING

Vocab-only 结果已经确认 code 域 multi-source K*=2，与三个单源的 K*=2 一致，也与 C4 multi-source K*=2 一致。unified scorer 结果待出。

---
