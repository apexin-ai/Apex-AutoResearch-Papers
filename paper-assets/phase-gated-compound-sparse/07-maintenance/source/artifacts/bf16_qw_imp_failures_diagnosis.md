# 诊断报告：bf16_qw_imp_s015/s020/s025 连续失败

## 日期
2026-05-14

## 根因（一句话）
**模型目录 `/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct` 不存在。** 三个实验的 `--model_path` 指向了未下载的 Qwen2.5-7B-Instruct，而服务器上只有 `Qwen2.5-7B`（base 模型）。

## 错误详情

三个实验日志完全一致，在 `load_model_and_tokenizer` 阶段立即失败：

```
File "run_profiling.py", line 64, in load_model_and_tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

huggingface_hub.errors.HFValidationError: Repo id must be in the form 
'repo_name' or 'namespace/repo_name': '/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct'. 
Use `repo_type` argument if needed.
```

transformers 先尝试本地加载失败（路径不存在），回退到 HuggingFace Hub 下载，但以 `/` 开头的绝对路径不是合法的 repo_id，于是报 `HFValidationError`。

## 服务器现有 checkpoints

```
/root/autodl-tmp/pacs/checkpoints/
├── DeepSeek-R1-Distill-Qwen-7B -> symlink (存在)
└── Qwen2.5-7B/  (base 模型，存在)
```

缺失：`Qwen2.5-7B-Instruct`

## GPU 状态
正常。4× NVIDIA RTX PRO 6000 Blackwell (98GB each)，GPU 0 被其他进程使用（31.6GB），GPU 1-3 空闲。

## 修复方案

### 方案 A：下载 Qwen2.5-7B-Instruct（如果实验确实需要 Instruct 版本）
```bash
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1

# 优先用 ModelScope（AutoDL 国内 CDN 快）
pip install modelscope
python -c "
from modelscope import snapshot_download
snapshot_download('Qwen/Qwen2.5-7B-Instruct', 
                  cache_dir='/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct')
"
```

### 方案 B：改用已有的 Qwen2.5-7B base（如果 Instruct 不是必须的）
将实验的 `--model_path` 从 `checkpoints/Qwen2.5-7B-Instruct` 改为 `checkpoints/Qwen2.5-7B`。
