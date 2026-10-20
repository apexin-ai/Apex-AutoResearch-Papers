# diag eval math500 sft random 20 fixed v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_math500_sft_random_20_fixed_v2_20260523T215151_result.json`
- **Structured JSON:** [`d87525f49da6219a6cf7.json`](../../sessions/d8/d87525f49da6219a6cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败根因

**SIGTERM 外部终止 (exit code 143)**，非代码错误、非 OOM。

进程被外部 kill 掉以腾出 cuda:1 给后续启动的 `eval_math500_grpo_random_20_fixed` 任务（05:47 启动）。

时间线：
- 05:05 — v2 启动，加载模型，开始 eval
- 05:15 — 被 SIGTERM 杀掉，仅完成 **2/500** 题（~213s/it，极慢）
- 05:47 — cuda:1 被 `eval_math500_grpo_random_20_fixed` 占用

v1 同样被 kill，但跑得更久（78/500，~1.5h，~80s/it）。v2 速度比 v1 慢 2.5x，可能是 cuda:0 上同时在跑 grpo_cka_only 导致总线/内存带宽竞争。

### 2. 日志文件

- `/root/runs/recovery_aware_struct_prune/eval_math500_sft_random_20_fixed_v2.log` （仅 13 行）
- `/tmp/agent-ml-exit/eval_math500_sft_random_20_fixed_v2.exit` → `143|2026-05-23T21:15:07Z`

### 3. 当前 GPU 状态

两块 GPU 都被占满，无法立即重试：
| GPU | 任务 | PID | 启动时间 |
|-----|------|-----|---------|
| cuda:0 | eval_math500_grpo_cka_only_20_fixed | 321428 | 03:35 |
| cuda:1 | eval_math500_grpo_random_20_fixed | 330254 | 05:47 |

### 4. 重试建议

等当前任一 eval 完成后重新提交。建议命令：

```bash
cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=&lt;freed_gpu> \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 \
python src/eval_math500.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 \
  --max_new_tokens 2048 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_random_20_fixed.json \
  --seed 42 --dtype bfloat16
```

预计运行时间：单 GPU 独占时 ~10-14h（按 v1 的 ~80s/it 估算），DDL 5/25 可以赶上。确保提交时另一块 GPU 不在运行重度任务，避免带宽竞争导致速度退化。

---
