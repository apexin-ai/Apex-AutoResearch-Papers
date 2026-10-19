# diag kl50 s123 reeval failure

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_kl50_s123_reeval_failure_20260517T184405_result.json`
- **Structured JSON:** [`e100aceb4e95f31abdfe.json`](../../sessions/e1/e100aceb4e95f31abdfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际上已成功完成**，EXIT_CODE=1 是误报。

### 证据
- 所有 4 个 benchmark 全部跑完，结果已保存到 `results/benchmark/kl50_global_s123_reeval/results.json`
- Checkpoint 存在且正确加载（`mvp_kl_norm_v2_s123/predictor_kl_normalized.pt`, 145MB）
- 参数 flag 正确：脚本使用 `--checkpoint`（不是 `--predictor_path`）

### 结果摘要
| Benchmark | Metric | Value |
|-----------|--------|-------|
| WikiText-2 | PPL | 11.72 |
| ARC-Challenge | acc_norm | 0.3635 |
| WinoGrande | acc | 0.6109 |
| MMLU | acc | 0.2834 |
| GSM8K | exact_match | 0.0258 |

### 失败根因
日志末尾有 `fatal: not a git repository (or any of the parent directories): .git`。这是 lm-evaluation-harness 内部尝试记录 git hash 时触发的，因为 westd-41718 上的工作目录不是 git repo。这个非零退出码被外层脚本/wrapper 捕获并报告为 EXIT_CODE=1，但评估本身已正常完成。

### 修复方案
不需要重跑。结果文件完整可用。如果需要消除 git 报错：
```bash
cd /root/distill_sparse_swiglu && git init
```
或在启动命令中设置 `GIT_DISCOVERY_ACROSS_FILESYSTEM=0` 环境变量来静默该警告。

---
