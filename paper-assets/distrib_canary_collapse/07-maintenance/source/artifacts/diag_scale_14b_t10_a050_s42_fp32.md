# 诊断报告: scale_14b_t10_a050_s42_fp32

## 失败根因

**HF cache 模型文件下载不完整。**

```
OSError: EleutherAI/pythia-1.4b-deduped does not appear to have a file named model-00001-of-00002.safetensors.
```

模型权重分 2 个 safetensors shard，cache 中仅有 shard 2/2（`model-00002-of-00002.safetensors`），shard 1/2 完全缺失。Cache 总大小 643MB，完整模型应约 2.8GB。

触发位置：`iterative_train.py:224` → `AutoModelForCausalLM.from_pretrained()` → `get_checkpoint_shard_files()` 找不到 shard 1。

## 失败时进度

Generation 0 未开始——模型加载阶段即失败。输出目录 `t10_a050_s42_fp32_14b/` 仅有 `config.json` 和 `EXIT_CODE` 文件，无任何训练产出。

## 服务器状态

| 指标 | 状态 |
|------|------|
| 磁盘 /root/autodl-tmp | 106G/250G used (43%) ✓ |
| 磁盘 / | 8.8G/30G used (30%) ✓ |
| OOM | 无（未进入训练） |
| GPU 内存 | 未使用（模型未加载） |

磁盘和内存均正常，非资源问题。

## 修复方案

重新下载缺失的 shard 1/2 即可：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HUB_CACHE=/root/autodl-tmp/.hf_cache
source /etc/network_turbo
python -c "from huggingface_hub import hf_hub_download; hf_hub_download('EleutherAI/pythia-1.4b-deduped', 'model-00001-of-00002.safetensors')"
```

下载完成后重新提交实验即可。
