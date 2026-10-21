# 诊断报告: plan_007_redocred_rsft_eval_r2 灾难性失败

## 结论: Pipeline Bug — Adapter 加载参数错误

### 根因

Re-DocRED RSFT eval 的启动命令将 adapter 路径传错了参数位置，导致模型加载顺序完全错误。

**错误配置（Re-DocRED eval r2 实际使用）**:
```
--model_path /root/autodl-tmp/models/Qwen3-4B
--sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
```

实际加载逻辑:
1. model_path 无 adapter_config.json → 当作完整模型
2. RSFT LoRA adapter 被当作 SFT adapter **直接 merge 进 base Qwen3-4B**
3. 无额外 adapter 加载

**正确配置（DocRED eval rsft_ced_s43 使用）**:
```
--model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
--sft_adapter /root/autodl-tmp/sft_output
```

实际加载逻辑:
1. model_path 有 adapter_config.json → 检测为 adapter，用 base_model (Qwen3-4B) 作为基座
2. 先 merge SFT adapter (`sft_output`) 到 base
3. 再加载 RSFT LoRA adapter 到 merged model 上

### 为什么结果灾难性

RSFT LoRA 是在 `Qwen3-4B + SFT_merged` 之上训练的增量。将这个增量直接 merge 到裸 Qwen3-4B：
- 模型失去 SFT 学到的 DocRED 关系 schema
- 模型退化为 base Qwen3-4B 行为：开放域信息抽取 + 自由文本关系

### 具体证据

**1. 输出格式对比**

RSFT r2 on Re-DocRED（错误加载）:
```json
{"head": "Wilfried \"Willi\" Schneider", "relation": "born", "tail": "13 March 1963 (TIME)", "sentence_ids": [0]}
{"head": "Wilfried \"Willi\" Schneider", "relation": "competes from", "tail": "1992 to 2002", "sentence_ids": [0]}
{"head": "Wilfried \"Willi\" Schneider", "relation": "won medal", "tail": "1998 men's skeleton event...", "sentence_ids": [1]}
```

SFT baseline on Re-DocRED（正确加载）:
```json
{"head": "Wilfried \"Willi\" Schneider", "relation": "date of birth", "tail": "13 March 1963", "evidence": [0]}
{"head": "Wilfried \"Willi\" Schneider", "relation": "country of citizenship", "tail": "German", "evidence": [0]}
{"head": "Wilfried \"Willi\" Schneider", "relation": "participant of", "tail": "2002 Winter Olympics", "evidence": [0, 2]}
```

**2. Metrics 对比**

| 指标 | RSFT r2 (错误) | SFT baseline | RSFT on DocRED (正确) |
|------|---------------|-------------|---------------------|
| F1 | 0.0025 | 0.3706 | 0.4601 |
| Ign-F1 | 0.0026 | 0.3659 | 0.4512 |
| field_compliance_rate | 0.0 | 0.716 | 0.809 |
| evidence_format_rate | 0.0 | 0.716 | 0.809 |
| tp | 19/7931 | 2413/5591 | 5479/11667 |

**3. Config 差异**

```
# DocRED eval (正确): rsft_ced_s43/metrics.json
"model_path": "/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510",  # ← adapter路径
"sft_adapter": "/root/autodl-tmp/sft_output",                         # ← SFT adapter

# Re-DocRED eval (错误): plan_007_redocred_rsft_eval_r2/metrics.json
"model_path": "/root/autodl-tmp/models/Qwen3-4B",                    # ← base model路径
"sft_adapter": "/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510", # ← RSFT adapter 被误传为 sft_adapter!
```

### 为什么现有 guard 没拦住

inference.py 有检查:
```python
if adapter_config.exists() and args.sft_adapter is None:
    raise ValueError(...)
```

但此检查仅当 `model_path` 是 adapter 时触发。当 `model_path = Qwen3-4B`（无 adapter_config.json），检查不触发，错误配置静默通过。

### 修复建议

1. **立即修复**: 重新运行 eval，使用正确参数:
```bash
CUDA_VISIBLE_DEVICES=X python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/re-docred \
    --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r3 \
    --batch_size 4 --max_new_tokens 1024 --split dev --no-quantize
```

2. **防御性改进**: 在 inference.py 增加额外检查——当 `sft_adapter` 路径的 `adapter_config.json` 中 `base_model_name_or_path` 与 `model_path/base_model` 一致时，warn 用户可能混淆了参数顺序。或者增加 `--rsft_adapter` 专用参数避免歧义。

### 排除的其他假设

- ❌ Re-DocRED relation set 不同：确认与 DocRED 共享完全相同的 96 个 Wikidata relation (P-codes)
- ❌ Eval pipeline bug：SFT baseline 在同一 pipeline 同一数据上正常
- ❌ RSFT adapter 本身有问题：在 DocRED 上正确加载时 F1=0.46
- ❌ Prompt 差异：两者 SYSTEM_PROMPT 完全一致
