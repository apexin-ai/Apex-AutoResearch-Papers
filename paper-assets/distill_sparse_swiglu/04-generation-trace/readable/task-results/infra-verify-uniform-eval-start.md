# infra verify uniform eval start

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_uniform_eval_start_20260517T225436_result.json`
- **Structured JSON:** [`1294d147568fcedc3c97.json`](../../sessions/12/1294d147568fcedc3c97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 两个 uniform 实验：❌ 启动失败

两个日志内容完全相同：
```
bash: line 1: python: command not found
EXIT_CODE=127
```

**根因**：nohup 启动的 shell 没有 conda PATH。`/root/miniconda3/bin/python` 存在（symlink → python3.12），但 nohup 环境中 `$PATH` 未包含 `/root/miniconda3/bin/`。

**GPU 状态**：cuda:0 和 cuda:1 均空闲（0MiB / 0% utilization），无任何 python 进程。

### 2. c4_ood_kl30_s42：✅ 已完成

- EXIT_CODE=0
- allocation=global_topk，model-level sparsity=0.300
- **C4 OOD PPL = 16.0458**（132 sequences, seq_len=2048）
- 结果已保存到 `/root/distill_sparse_swiglu/results/benchmark/c4_ood_kl30_s42/results.json`

### 修复建议

重新提交两个 uniform 实验时，启动命令需要改为：
```bash
nohup /root/miniconda3/bin/python script.py ... > log.log 2>&1 &
```
或在脚本开头加 `source /root/miniconda3/bin/activate`。

---
