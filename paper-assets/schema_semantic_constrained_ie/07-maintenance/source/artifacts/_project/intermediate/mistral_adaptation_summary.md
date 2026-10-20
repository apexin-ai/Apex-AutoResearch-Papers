## Mistral-7B-Instruct-v0.3 适配改动

### 修改文件

**1. run_constrained_extraction.py** (752→754行, +2行)
- 行621-631: `main()` 中默认模型搜索路径新增 Llama 和 Mistral 路径
- 错误信息从 "Qwen3-8B not found" 改为 "No model found"
- 无其他改动

**2. download_mistral.sh** (新建, 39行)
- HuggingFace snapshot_download
- 目标路径: /root/autodl-tmp/models/mistralai/Mistral-7B-Instruct-v0.3
- 含下载后验证步骤
- 未执行

### 为什么改动量这么小

现有代码已经完全模型无关:
- `AutoModelForCausalLM` + `AutoTokenizer`: Mistral (MistralForCausalLM) 自动识别
- `apply_chat_template`: Mistral v0.3 tokenizer 自带 chat template，支持 system/user/assistant 角色
- `_chat_template_kwargs`: 对非 Qwen 模型返回空 dict，Mistral 无需特殊参数
- XGrammar: 32K vocab，标准 BPE tokenizer，完全兼容
- pad_token: 代码已有 `if pad_token is None: pad_token = eos_token` 兜底

### 使用方式
```bash
# 下载（等 GPU 空闲后）
bash download_mistral.sh

# 运行 SciERC
python run_constrained_extraction.py \
  --mode full_s1 --dataset scierc \
  --model_path /root/autodl-tmp/models/mistralai/Mistral-7B-Instruct-v0.3 \
  --data_path data/scierc/test.json \
  --constraints_path data/scierc/constraints.json \
  --output_path outputs/mistral_scierc_full_s1.jsonl \
  --device cuda:0
```
