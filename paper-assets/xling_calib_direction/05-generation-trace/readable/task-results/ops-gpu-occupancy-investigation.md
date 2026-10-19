# ops gpu occupancy investigation

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-occupancy-investigation_20260521T120207_result.json`
- **Structured JSON:** [`1764234f3e6a42918ecd.json`](../../sessions/17/1764234f3e6a42918ecd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 占用报告

**单个进程 PID 482839** 占用了 GPU 1/2/3，是本项目自己的任务：

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 3 MiB | 空闲 |
| 1 | 90,140 MiB / 97,887 MiB | 占用 |
| 2 | 93,602 MiB / 97,887 MiB | 占用 |
| 3 | 93,602 MiB / 97,887 MiB | 占用 |

**进程详情：**

- **PID**: 482839
- **运行时间**: 4 分 3 秒
- **CPU**: 80.5%
- **RSS**: ~16.3 GB
- **命令**:
  ```
  python -u code/extract_activations.py \
    --model_path /root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4/ \
    --model_name qwen3_235b_gptq \
    --layers 0,4 \
    --languages en zh \
    --output_dir /root/autodl-tmp/activations/plan_001_dryrun \
    --max_samples 5
  ```

**结论**：不是未知进程。是本项目 `xling_calib_direction` 的 activation 提取脚本，正在用 Qwen3-235B-GPTQ-Int4 模型做 dry run（仅 5 个样本、2 层）。GPU 利用率 0%，说明当前在做 CPU 端工作（可能在加载模型或预处理数据）。

---
