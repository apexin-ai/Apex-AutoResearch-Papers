# diagnose exp 001 sft 15B d025 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_15B_d025_s123_20260515T084908_result.json`
- **Structured JSON:** [`58489e0921f46f3d8993.json`](../../sessions/58/58489e0921f46f3d8993.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

两个实验失败原因不同，但都是命令行参数问题导致 argparse 报错退出（EXIT_CODE=2）：

**exp_001_sft_15B_d005_s123**：命令中传了 `--gpu 0`，但 `train_sft.py` 没有定义 `--gpu` 参数。日志明确显示：
> `train_sft.py: error: unrecognized arguments: --gpu 0`

**exp_001_sft_15B_d025_s123**：日志显示：
> `error: the following arguments are required: --model-name, --data-path`

说明这个实验的启动命令没有正确传递 `--model-name` 和 `--data-path` 参数（可能是 bash -c 引号嵌套问题，或者命令拼接时参数丢失）。

### 脚本支持的参数

`train_sft.py` 接受的参数为：`--model-name`, `--data-path`, `--output-dir`, `--seed`, `--max-seq-length`, `--lora-r`, `--lora-alpha`, `--epochs`, `--batch-size`, `--grad-accum`, `--lr`, `--merge`, `--cache-dir`。**没有 `--gpu`**。

### 修复建议

1. **删除 `--gpu 0`**。GPU 选择应通过 `CUDA_VISIBLE_DEVICES=N` 环境变量控制（这也符合 C004 约束）。
2. **检查 d025 实验的启动命令**，确保参数在 `bash -c "..."` 中没有被引号截断。
3. 修正后的命令模板：

```bash
CUDA_VISIBLE_DEVICES=0 bash -c "source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8"
```

### 是否需要修改代码

不需要修改 `train_sft.py`。只需修复启动命令。

---
