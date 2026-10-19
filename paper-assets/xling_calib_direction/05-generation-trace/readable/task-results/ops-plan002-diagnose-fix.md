# ops plan002 diagnose fix

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan002-diagnose-fix_20260521T115030_result.json`
- **Structured JSON:** [`ba57e06af6c41c80fe15.json`](../../sessions/ba/ba57e06af6c41c80fe15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了。脚本的参数列表中没有 `--gpu_id`，有 `--device_map`。

**最终诊断报告**：

| 项目 | 结论 |
|------|------|
| **根因** | 缺少必需参数 `--model_name` |
| **EXIT_CODE=2** | argparse 参数校验失败的标准退出码，不是 shell 语法错误 |
| **模型路径** | 正确，config.json 存在 |
| **额外问题** | 原命令使用了 `--gpu_id 0`，但脚本不接受此参数（应使用 `--device_map`），即使加了 `--model_name` 也会因 unrecognized argument 再次失败 |

**修复后的正确命令**：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONUNBUFFERED=1 && cd /root/xling_calib_direction && CUDA_VISIBLE_DEVICES=0 python -u code/extract_activations.py --model_path /root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/ --model_name llama4_scout --layers 0,4,8,12,16,20,24,28,32,36,40,44,47 --languages en zh ar hi sw ko es fr de ru tr bn ja pt vi te id pl nl uk --output_dir /root/autodl-tmp/activations/llama4_scout/ --batch_size 8"
```

两处修改：
1. **添加** `--model_name llama4_scout`
2. **移除** `--gpu_id 0`，改用环境变量 `CUDA_VISIBLE_DEVICES=0`
3. **注意** `--languages` 参数是 `nargs="+"`（空格分隔），不是逗号分隔

---
