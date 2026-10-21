# diagnose math500 westd failures

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_math500_westd_failures_20260521T134335_result.json`
- **Structured JSON:** [`edaa0881fc4fc2b55bd7.json`](../../sessions/ed/edaa0881fc4fc2b55bd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已有足够信息得出结论。

## 诊断报告

### 根因：三个进程被人为 kill，已有 2 个被重启为 v2 版本

**证据**：
- 三个日志在 21:25-21:28 几乎同时停止（sft 21:25, random 21:27, grpo 21:28）
- `grpo_cka_only_25` 日志末尾有明确 `Terminated`（SIGTERM），另两个无错误信息（SIGKILL）
- 无 OOM/CUDA error/磁盘满迹象（磁盘仅用 17%，GPU 内存充足）
- **杀后 2 分钟内已启动 v2 版本**（21:30:32 和 21:30:34），新参数增加了 `--max_new_tokens 2048` 和 `--output_path`

### 当前状态

| 实验 | 原进程 | 当前状态 |
|---|---|---|
| grpo_cka_only_25 | 205/500 被杀 | **v2 已在跑** (PID 379999, GPU 0, 98% util) |
| sft_cka_only_25 | 179/500 被杀 | **v2 已在跑** (PID 380074, GPU 2, 97% util) |
| grpo_random_20 | 43/500 被杀 | **未重启**，GPU 1 空闲 |

### grpo_random_20 的额外问题

该实验极慢：~6 min/sample（其他两个 ~1.5 min/sample），500 样本预计需 ~50 小时。原因可能是 `temperature=0` 导致贪心解码时生成极长输出。需确认是否要加 `--max_new_tokens 2048` 限制后重启。

### 建议

1. v2 版本已在正常运行，无需干预
2. grpo_random_20 需决定是否在 GPU 1 上用 v2 参数重启：
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_random_20_v2 --max_samples 500 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_random_20_v2.log 2>&1 &
```

---
