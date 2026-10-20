# ssh gpu health check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_health_check_20260513T105932_result.json`
- **Structured JSON:** [`6b525d0553f05cb82e9e.json`](../../sessions/6b/6b525d0553f05cb82e9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 状态

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| GPU 0 | **90%** | 26,963 MiB | 97,887 MiB |
| GPU 1 | **0%** | 0 MiB | 97,887 MiB |

### 任务 1: grpo_v2_final_eval — **运行中** ✓

- **PID**: 104325（CPU 103%，RSS ~2GB）
- **命令**: `python -u evaluate.py --model_path ./outputs/grpo_v2_final/merged --batch_size 8 --max_prompt_length 4096 --output_file ./outputs/grpo_v2_final/eval_results.json`
- **状态**: 模型已合并完成，评估阶段正在执行（GPU 0 占用 90%，27GB 显存）
- **输出目录**: `/root/autodl-tmp/prov_grounded_uie/outputs/grpo_v2_final/` — 目前只有 `merged/` 子目录，`eval_results.json` 尚未生成

### 任务 2: dpo_candgen_cuda1 — **已失败** ✗

- **PID 105192**: 不存在（进程表中无此 PID）
- **DPO 输出文件**: `dpo_candidates_part1.jsonl` 不存在
- **失败原因**: 日志显示启动脚本传了无法识别的参数：
  ```
  generate_dpo_candidates.py: error: unrecognized arguments: --train_file ./data/docred_train.jsonl --seed 42
  EXIT_CODE=2
  ```
- **GPU 1**: 完全空闲（0% 利用率，0 MiB 显存）

### 总结

- **grpo_v2_final_eval**: 正常运行中，GPU 0 上执行评估
- **dpo_candgen_cuda1**: 启动即失败，参数错误（`--train_file` 和 `--seed` 不被 `generate_dpo_candidates.py` 识别），需要修复启动命令后重跑

---
