# code plan 024 downstream benchmark

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_024_downstream_benchmark_20260517T155538_result.json`
- **Structured JSON:** [`2caa48d12fa187ccd6d3.json`](../../sessions/2c/2caa48d12fa187ccd6d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。5 个脚本已写入服务器 `/root/autodl-tmp/recursive_gen_depth_est/scripts/`：

| 脚本 | 功能 | 依赖 |
|------|------|------|
| `downstream_score_data.py` | RF 训练 + C4 depth 打分 | CPU only |
| `downstream_filter.py` | 按 depth 过滤 4 种条件 | CPU only |
| `downstream_finetune.py` | Pythia-410M LoRA fine-tune | GPU |
| `downstream_eval.sh` | lm-eval-harness 评估 3 benchmarks | GPU |
| `run_downstream_full.sh` | 端到端串联 | — |

验证结果：
- `--help` 全部正常
- Dry-run scoring: RF 在 20K labeled data 上 val acc = **77.4%**，C4 数据成功打分
- Dry-run filter: 4 种条件文件正常输出
- `lm-eval` 0.4.11 和 `peft` 0.7.1 已安装

代码 ready to run，等 GPU 分配后执行 `bash scripts/run_downstream_full.sh`。

---
