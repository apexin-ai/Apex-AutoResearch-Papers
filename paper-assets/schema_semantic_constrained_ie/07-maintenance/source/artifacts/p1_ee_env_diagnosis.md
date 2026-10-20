# P1 EE FT 环境诊断报告

服务器: westd-21461  
时间: 2026-05-19 03:57 UTC

---

## 1. tmux 清理

```
$ tmux kill-session -t p1_ee_ft_composability_r2 2>/dev/null; tmux kill-session -t p1_ee_ft_composability 2>/dev/null; echo "tmux cleaned"
tmux cleaned
```

## 2. 清理虚假 COMPLETE 标记

```
$ rm -f /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE_r2
$ ls -la /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE* 2>&1
ls: cannot access '/root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE*': No such file or directory
```

## 3. 验证 python3

```
$ which python3
/usr/bin/python3

$ python3 --version
Python 3.10.12
```

## 4. 验证项目路径和脚本

```
$ ls -la /root/schema_semantic_constrained_ie/scripts/train_lora_wikievents.py
-rw-r--r-- 1 root root 6443 May 19 03:10 /root/schema_semantic_constrained_ie/scripts/train_lora_wikievents.py
```

项目代码路径: `/root/schema_semantic_constrained_ie/`

## 5. 验证数据文件

```
$ wc -l /root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train.jsonl /root/schema_semantic_constrained_ie/data/sft/wikievents_sft_dev.jsonl
    194 /root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train.jsonl
     20 /root/schema_semantic_constrained_ie/data/sft/wikievents_sft_dev.jsonl
    214 total
```

## 6. 训练脚本数据路径

```
$ head -20 /root/schema_semantic_constrained_ie/scripts/train_lora_wikievents.py
```

脚本中配置的默认路径:
- `--train_data`: `/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train.jsonl`
- `--eval_data`: `/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_dev.jsonl`
- `--output_dir`: `/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_wikievents`
- `--merged_dir`: `/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_wikievents_merged`
- `--model_path`: `Qwen/Qwen3-8B`

**路径匹配**: 脚本中写死的数据路径与实际文件位置完全一致。

## 7. GPU 状态

```
$ nvidia-smi
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.119.02             Driver Version: 580.119.02     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |                  Off |
| N/A   33C    P0             84W /  600W |   18903MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |                  Off |
| N/A   52C    P0            294W /  600W |   18923MiB /  97887MiB |     82%      Default |
+-----------------------------------------+------------------------+----------------------+

| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|=========================================================================================|
|    0   N/A  N/A           55834      C   python                                18894MiB |
|    1   N/A  N/A           39244      C   python3                               18914MiB |
+-----------------------------------------------------------------------------------------+
```

**GPU 0 (PID 55834)**: 正在运行 `python scripts/train_lora_wikievents.py` (18.9GB/97.9GB)
- 实际可执行文件: `/root/miniconda3/bin/python3.12`

**GPU 1 (PID 39244)**: 正在运行 `python3 run_constrained_extraction.py --mode full_s1 --dataset docred ...` (18.9GB/97.9GB)
- 实际可执行文件: `/root/miniconda3/bin/python3.12`

**⚠️ 重要发现: GPU 0 上已经有一个 train_lora_wikievents.py 训练进程在运行！**

## 8. python3 import 关键库

系统 python3 (`/usr/bin/python3`):
```
$ python3 -c "import torch; ..."
ModuleNotFoundError: No module named 'torch'
```

conda python3 (`/root/miniconda3/bin/python3`):
```
$ /root/miniconda3/bin/python3 -c "import torch; print('torch', torch.__version__); import transformers; print('transformers', transformers.__version__); import peft; print('peft', peft.__version__); print('CUDA available:', torch.cuda.is_available())"
torch 2.8.0+cu128
transformers 5.8.1
peft 0.19.1
CUDA available: True

$ /root/miniconda3/bin/python3 -c "import trl; print('trl', trl.__version__); import datasets; print('datasets', datasets.__version__)"
trl 1.4.0
datasets 4.8.5
```

stderr (non-fatal): `Skipping import of cpp extensions due to incompatible torch version.`

## 9. python vs python3

```
$ which python 2>&1
(exit code 1, not found)

$ which python3 2>&1
/usr/bin/python3

$ ls -la $(which python3)
lrwxrwxrwx 1 root root 10 Aug  8  2024 /usr/bin/python3 -> python3.10
```

---

## 诊断总结

| 项目 | 值 |
|------|-----|
| python3 绝对路径 (系统) | `/usr/bin/python3` (Python 3.10.12, **无 torch**) |
| python3 绝对路径 (conda) | `/root/miniconda3/bin/python3` (Python 3.12, **有完整环境**) |
| 项目代码路径 | `/root/schema_semantic_constrained_ie/` |
| 训练数据路径 | `/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_{train,dev}.jsonl` |
| 脚本数据路径匹配 | 完全匹配 |
| GPU | 2x NVIDIA RTX PRO 6000 Blackwell (各 97.9GB) |
| GPU 0 | 已被 train_lora_wikievents.py 占用 (18.9GB) |
| GPU 1 | 已被 docred extraction 占用 (18.9GB, 82% util) |
| torch | 2.8.0+cu128 |
| transformers | 5.8.1 |
| peft | 0.19.1 |
| trl | 1.4.0 |
| datasets | 4.8.5 |

### 之前失败的根因

之前 3 次失败的原因是 `python` 不在 PATH（系统没有 `python` 命令），而 `python3` 指向系统 python3.10 没有 torch。所有 ML 库都装在 conda 环境 `/root/miniconda3/` 里。

### 训练命令应该怎么写

```bash
cd /root/schema_semantic_constrained_ie && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3 scripts/train_lora_wikievents.py
```

或者先激活 conda:
```bash
source /root/miniconda3/bin/activate && cd /root/schema_semantic_constrained_ie && CUDA_VISIBLE_DEVICES=0 python3 scripts/train_lora_wikievents.py
```

### ⚠️ 注意事项

1. **GPU 0 上已有 train_lora_wikievents.py 在运行** (PID 55834)，启动新训练前需要确认是否要杀掉它，或者使用 GPU 1（但 GPU 1 也被 docred extraction 占用）。
2. 每张卡有 97.9GB 显存，当前各占用约 18.9GB，理论上剩余显存足够再跑一个 8B 模型训练，但需注意 OOM 风险。
3. 必须使用 `/root/miniconda3/bin/python3` 而非系统 `/usr/bin/python3`。
