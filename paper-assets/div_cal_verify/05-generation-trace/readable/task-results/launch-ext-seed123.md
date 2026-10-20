# launch ext seed123

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_ext_seed123_20260513T071226_result.json`
- **Structured JSON:** [`395b18a46fef428677f7.json`](../../sessions/39/395b18a46fef428677f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

## 产出

### 1. run_ext_seed123.sh 已创建并验证
路径：`/root/div_cal_verify/run_ext_seed123.sh`

与 Phase 2 的 external_only 参数完全一致，仅改动：
- `--seed 42` → `--seed 123`
- `--output_dir` → `.../results_phase2_seed123/external_only`
- `CUDA_VISIBLE_DEVICES=0`（原脚本默认用 GPU 1）

### 2. 启动命令
```
bash /root/div_cal_verify/run_ext_seed123.sh
```
供 `submit_training_job` 提交，日志建议写到 `/root/div_cal_verify/logs/ext_seed123.log`。

### 3. cuda:0 显存确认
| GPU | 型号 | 已用 | 可用 | 总量 |
|-----|------|------|------|------|
| 0 | RTX PRO 6000 Blackwell | 49.2 GB | **47.0 GB** | 95.6 GB |
| 1 | RTX PRO 6000 Blackwell | 21.7 GB | 75.6 GB | 95.6 GB |

cuda:0 有 47 GB 空闲，GPT2-125M + Contriever 约需 12 GB，显存充足。

---
