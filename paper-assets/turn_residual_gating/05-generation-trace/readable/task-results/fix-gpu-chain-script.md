# fix gpu chain script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu_chain_script_20260523T072756_result.json`
- **Structured JSON:** [`b857e754e2b671bbae57.json`](../../sessions/b8/b857e754e2b671bbae57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- **`gpu_chain_next.sh` 已重写**：9 步串行链，每步前有 `check_gpu_free()`（GPU used > 1000MiB 则 abort）
- **新增步骤**：Step 3 SS s123 训练 + Step 4 SS s123 eval
- **`d048_ss_s123.sh` 超参确认正确**：与 s456 一致（seed=123, output-dir=runs/d048_ss_s123），无 resume
- **语法检查**：`gpu_chain_next.sh`、`d048_ss_s123.sh`、`d048_eval_ss_s123.sh` 全部 SYNTAX OK
- **所有引用脚本均存在**（9 个脚本 + mmlu_eval_single.sh）

未启动任何 GPU 任务。

---
