# 诊断报告: exp_001_sft_15B_d005_s123

## 错误日志摘要

```
usage: train_sft.py [-h] --model-name MODEL_NAME --data-path DATA_PATH
                    --output-dir OUTPUT_DIR [--seed SEED]
                    [--max-seq-length MAX_SEQ_LENGTH] [--lora-r LORA_R]
                    [--lora-alpha LORA_ALPHA] [--epochs EPOCHS]
                    [--batch-size BATCH_SIZE] [--grad-accum GRAD_ACCUM]
                    [--lr LR] [--merge] [--cache-dir CACHE_DIR]
train_sft.py: error: unrecognized arguments: --gpu 0
EXIT_CODE=2
```

## 根因

`train_sft.py` 的 argparse 未定义 `--gpu` 参数。训练命令传入了 `--gpu 0`，argparse 直接拒绝，脚本未执行任何训练逻辑即退出。

脚本定义的全部参数（第 85-105 行）：
`--model-name`, `--data-path`, `--output-dir`, `--seed`, `--max-seq-length`, `--lora-r`, `--lora-alpha`, `--epochs`, `--batch-size`, `--grad-accum`, `--lr`, `--merge`, `--cache-dir`

脚本中也没有 `CUDA_VISIBLE_DEVICES` 相关逻辑——即使添加 `--gpu` 参数，也需要补充 GPU 选择的实现代码。

ROADMAP 中提到的 "train_sft.py --gpu 死代码" 实际情况更严重：不是死代码，而是参数根本未定义。

## 排除项

- 数据文件存在：`sft_dosage_005.jsonl` (88.7MB) ✓
- 模型目录存在：`Qwen2.5-1.5B/model.safetensors` (2.9GB) ✓
- 非 OOM / CUDA 错误，脚本在 argparse 阶段即崩溃

## 修复建议

**方案 A（推荐）**：从训练命令中移除 `--gpu 0`，改为通过环境变量控制 GPU：
```bash
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py ...
```
这也符合项目约束 C004（必须显式设置 CUDA_VISIBLE_DEVICES）。

**方案 B**：在 `train_sft.py` 中添加 `--gpu` 参数并实现 GPU 选择：
```python
parser.add_argument("--gpu", type=int, default=0, help="GPU device index")
# 在 main() 开头，import torch 之前：
import os
os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
```
注意：`os.environ["CUDA_VISIBLE_DEVICES"]` 必须在 `import torch` 之前设置才能生效。
