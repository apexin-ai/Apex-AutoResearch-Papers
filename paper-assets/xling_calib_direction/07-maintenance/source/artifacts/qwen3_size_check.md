# Qwen3-235B-A22B-GPTQ-Int4 模型大小确认

## 权重文件清单

共 **32 个 safetensors 分片**：

| 文件 | 大小 |
|------|------|
| model-00001 ~ 00011-of-00032.safetensors | 各 4.00 GB |
| model-00012-of-00032.safetensors | 3.99 GB |
| model-00013 ~ 00030-of-00032.safetensors | 各 4.00 GB |
| model-00031-of-00032.safetensors | 3.31 GB |
| model-00032-of-00032.safetensors | 1.24 GB |

其他文件：model.safetensors.index.json (13.2 MB), config.json, tokenizer.json (11.4 MB), vocab.json (2.78 MB), merges.txt (1.67 MB) 等。

## 总大小

| 指标 | 值 |
|------|------|
| **权重文件总大小** | **~125 GB** |
| 配置+tokenizer 文件 | ~30 MB（可忽略） |
| HF API 报告的 repo 存储 | 249 GB（含 LFS 历史版本） |
| 之前估算的 208 GB | ❌ 不准确 |

## HF Cache 膨胀分析

使用 `huggingface-cli download`（默认 cache 模式）时的存储结构：
- `blobs/` — 实际文件，~125 GB
- `snapshots/<revision>/` — 指向 blobs 的**软链接**，几乎不占空间
- `du` 默认不跟随软链接，所以 cache 目录显示 ~125 GB，**不会翻倍**
- 但如果用 `du -L`（跟随软链接）或某些文件管理器，会显示 ~250 GB

之前估算 208 GB 的可能原因：
1. 下载中途 du 统计了不完整文件 + 临时文件
2. 混合了其他模型的 cache
3. 使用了错误的 du 参数

## 下载建议

```bash
# 推荐：用 --local-dir 直接下载，避免 cache 层
huggingface-cli download Qwen/Qwen3-235B-A22B-GPTQ-Int4 \
  --local-dir /root/autodl-tmp/models/Qwen3-235B-A22B-GPTQ-Int4

# 磁盘需求：~125 GB（权重）+ ~5 GB（下载临时文件缓冲）≈ 130 GB
# --local-dir 模式下不会在 ~/.cache/huggingface/ 创建 blobs 副本

# 如果用 ModelScope（AutoDL 推荐，国内 CDN 更快）：
pip install modelscope
python -c "
from modelscope import snapshot_download
snapshot_download('Qwen/Qwen3-235B-A22B-GPTQ-Int4',
                  cache_dir='/root/autodl-tmp/models')
"
```

## 结论

实际需要磁盘空间 **~130 GB**（125 GB 权重 + 缓冲），远小于之前估算的 208 GB。用 `--local-dir` 下载可完全避免 cache 膨胀问题。
