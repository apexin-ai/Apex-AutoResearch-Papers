# D009 Cross-model Validation: Llama-3.1-8B Preparation

## Model IDs

| 版本 | HuggingFace Model ID | 用途 |
|------|---------------------|------|
| 基座模型 | `meta-llama/Llama-3.1-8B` | 纯生成能力测试 |
| Instruct | `meta-llama/Llama-3.1-8B-Instruct` | **推荐用于 IE 实验** |

**推荐使用 Instruct 版本**：IE 任务依赖指令遵循能力，Instruct 版本在结构化输出上表现更稳定。

## Gated Access

- **需要 license agreement**：Llama 3.1 Community License
- 必须在 HuggingFace 模型页面点击 "Request Access" 并接受协议
- 下载时需要 `HF_TOKEN` 认证
- 审批通常即时通过（自动批准）

## 模型大小与显存评估

| 指标 | 数值 |
|------|------|
| 参数量 | 8B |
| BF16 模型文件大小 | ~16 GB |
| 推理显存占用 (BF16) | ~17-18 GB |
| 推理显存占用 (8-bit量化) | ~9-10 GB |
| 服务器 GPU | RTX PRO 6000 (94 GB VRAM) |
| **结论** | 显存充裕，BF16 无需量化 |

## Transformers 兼容性

| 项目 | 状态 |
|------|------|
| 最低要求 | transformers >= 4.43.0 |
| 服务器版本 | transformers 4.57.6 |
| **兼容性** | **完全兼容** |

额外依赖：
- `tokenizers` — transformers 已自带
- `accelerate` — 推荐安装，用于设备映射
- Llama 3.1 使用 tiktoken-based tokenizer，**不需要 sentencepiece**

## 下载方案

### 方案 A: HuggingFace CLI (推荐，westd-16980 非 AutoDL)

```bash
# 先登录
huggingface-cli login --token $HF_TOKEN

# 下载 Instruct 版本到数据盘
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct \
  --local-dir /root/autodl-tmp/models/Llama-3.1-8B-Instruct
```

### 方案 B: ModelScope 镜像 (如 HF 速度慢)

```bash
pip install modelscope
python -c "
from modelscope import snapshot_download
snapshot_download('LLM-Research/Meta-Llama-3.1-8B-Instruct',
                  cache_dir='/root/autodl-tmp/models/')
"
```

### 方案 C: Python API 直接加载

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "meta-llama/Llama-3.1-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
```

## 预估时间

| 步骤 | 预估时间 |
|------|---------|
| 模型下载 (~16GB) | 10-30 min (取决于带宽) |
| SciERC unconstrained 实验 | ~2-4 h (参考 Qwen2.5-7B 用时) |
| SciERC full_s1 实验 | ~2-4 h |
| **总计** | ~5-9 h |

## 前置检查清单

- [ ] 确认 HuggingFace access 已获批
- [ ] 确认服务器 `HF_TOKEN` 环境变量已设置
- [ ] 确认磁盘空间 > 20 GB
- [ ] 确认 `accelerate` 已安装
- [ ] 下载模型并验证加载
- [ ] 适配现有 extraction 脚本的 model_id 参数
