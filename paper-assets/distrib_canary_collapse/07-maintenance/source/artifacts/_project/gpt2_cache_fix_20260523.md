# gpt2-large 缓存状态报告 (2026-05-23)

## 结论：两台服务器均已缓存，无需修复

### westd-19828
- **缓存位置**: `/root/autodl-tmp/.hf_cache/models--gpt2-large/` (及 `hub/` 下硬链接)
- **缓存时间**: 2026-05-18
- **文件完整性**: 6 文件 (config.json, merges.txt, model.safetensors [3.1G], tokenizer.json, tokenizer_config.json, vocab.json)
- **离线加载测试**: OK (HF_HUB_OFFLINE=1, 36L/774M, 6s)

### westd-17855
- **缓存位置**: `/root/autodl-tmp/.hf_cache/models--gpt2-large/` (及 `hub/` 下硬链接)
- **缓存时间**: 2026-05-19
- **文件完整性**: 同上，6 文件完整
- **离线加载测试**: OK (HF_HUB_OFFLINE=1, 36L/774M, 5s)

### mauve 模型引用方式
- `metrics.py:285` 调用 `mauve_pkg.compute_mauve()` 未指定 `featurize_model_name`
- mauve 包默认值为 `featurize_model_name='gpt2-large'`
- 训练时需设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，mauve 自动从缓存加载，不需网络

### 注意事项
- `iterative_train.py` 本身不设 HF_HOME，依赖外部环境变量 (M060 约束)
- 训练命令必须包含 `export HF_HOME=/root/autodl-tmp/.hf_cache` 和 `export HF_HUB_OFFLINE=1`
