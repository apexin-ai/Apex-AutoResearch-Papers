# 诊断报告：eval_mbpp_grpo_shortgpt_20_v2 失败

## 日志全文

```
python: can't open file '/root/autodl-tmp/recovery_aware_struct_prune/src/eval_mbpp.py': [Errno 2] No such file or directory
EXIT_CODE=2
```

## 根因分析

**工作目录错误。** 提交命令使用了相对路径 `src/eval_mbpp.py`，但运行时的工作目录（cwd）是 `/root/autodl-tmp/recovery_aware_struct_prune/`（数据盘），导致 Python 尝试打开 `/root/autodl-tmp/recovery_aware_struct_prune/src/eval_mbpp.py`，该路径不存在。

实际文件位置：`/root/recovery_aware_struct_prune/src/eval_mbpp.py`（代码目录，根分区）。

各关键路径状态：
- ✅ `/root/miniconda3/etc/profile.d/conda.sh` — 存在
- ✅ `/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100` — 存在（含 model.safetensors 12.9GB）
- ✅ `/root/recovery_aware_struct_prune/src/eval_mbpp.py` — 存在（7086 bytes）
- ❌ `/root/autodl-tmp/recovery_aware_struct_prune/src/eval_mbpp.py` — 不存在（实际执行时解析到的路径）

## 修复建议

在命令中加 `cd /root/recovery_aware_struct_prune &&`，确保工作目录正确：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json"
```

或使用绝对路径：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python /root/recovery_aware_struct_prune/src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json"
```
