# Eval 脚本审计报告：GRPO Checkpoint 兼容性

## 1. eval 脚本当前能力

### 支持的功能
| 功能 | 状态 | 说明 |
|------|------|------|
| LoRA adapter 自动检测 | OK | 检查 `adapter_config.json` 存在性，自动切换 adapter/full-model 模式 |
| 4-bit QLoRA 推理 | OK | 默认开启 NF4 量化，`--no-quantize` 可关闭 |
| parse_model_output 统一解析 | OK | JSON 解析 + 截断修复，所有模型共用 |
| F1 / Ign-F1 | OK | micro-F1，Ign-F1 排除训练集三元组 |
| Evi-F1 | OK | 对正确预测的三元组，计算 evidence 句子级 F1 |
| EDCR | OK | Evidence Distractor Citation Rate |
| format_compliance_rate | OK | JSON 格式合规率 |
| 批量推理 | OK | 支持 batch_size 参数 |

### 不支持的功能
| 功能 | 状态 | 影响 |
|------|------|------|
| **双 adapter 加载（SFT + GRPO）** | MISSING | **阻断性问题**，详见下文 |

## 2. GRPO Checkpoint 格式分析

### Checkpoint 结构
所有 GRPO checkpoint（CED/extraction/flat-NLI）结构一致：

```
checkpoint-N/
  adapter_config.json          # LoRA 配置，base_model = Qwen3-4B
  adapter_model.safetensors    # LoRA adapter 权重
  tokenizer.json + tokenizer_config.json + ...
  trainer_state.json
  training_args.bin
  optimizer.pt / scheduler.pt / rng_state.pth
```

与 SFT 输出格式完全相同（都是 PEFT LoRA adapter）。

### 已有 Checkpoint 清单
| 模型 | 目录 | Checkpoint |
|------|------|-----------|
| SFT baseline | `/root/autodl-tmp/sft_output/` | checkpoint-96, checkpoint-144 |
| GRPO CED | `/root/autodl-tmp/grpo_ced_r5/` | checkpoint-400 ~ 480 (步长20) |
| GRPO extraction-only | `/root/autodl-tmp/grpo_extract_r3/` | checkpoint-400 ~ 480 (步长20) |
| GRPO flat-NLI | `/root/autodl-tmp/grpo_flatnli_r3/` | checkpoint-20 ~ 80 (步长20) |

## 3. 阻断性问题：双 adapter 加载

### 问题根因

`grpo_trainer.py` 的训练流程：
```python
# 1. 加载 base model
model = AutoModelForCausalLM.from_pretrained(args.model_name)
# 2. 加载 SFT adapter 并 merge 到 base
model = PeftModel.from_pretrained(model, args.sft_adapter)
model = model.merge_and_unload()  # SFT 权重融合进 base
# 3. 在 merged 模型上训练新的 LoRA
trainer = GRPOTrainer(model=model, peft_config=lora_config, ...)
# 4. 保存的是新 LoRA 的 delta（相对于 base+SFT_merged）
trainer.save_model()
```

GRPO adapter 是 **(base + SFT) -> GRPO delta**，不是 **base -> GRPO delta**。

`inference.py` 当前加载逻辑：
```python
# 检测到 adapter_config.json -> 当作单个 adapter 加载
model = AutoModelForCausalLM.from_pretrained(base_model)  # 只有 Qwen3-4B
model = PeftModel.from_pretrained(model, adapter_path)     # 直接叠 GRPO adapter
```

**结果：GRPO adapter 直接应用到裸 Qwen3-4B 上，缺失 SFT 贡献。评估结果将不正确。**

SFT eval 不受影响（单 adapter，直接加载即可）。

### adapter_config.json 对比

两者的 `base_model_name_or_path` 都是 `/root/autodl-tmp/models/Qwen3-4B`，LoRA 配置完全相同（r=64, alpha=128, 7 个 target modules）。无法从 config 区分 SFT 和 GRPO adapter。

## 4. 修改方案

### inference.py 需要的改动

**新增参数：**
```python
parser.add_argument("--sft_adapter", default=None,
                    help="SFT adapter 路径，用于 GRPO checkpoint 评估时先 merge SFT")
```

**修改 main() 中的模型加载逻辑（替换现有加载部分）：**
```python
# 自动检测 model_path 是 adapter 还是完整模型
adapter_config = Path(args.model_path) / "adapter_config.json"
if adapter_config.exists():
    base_model_path = args.base_model
    adapter_path = args.model_path
    logger.info("Detected adapter at %s, base: %s", adapter_path, base_model_path)
else:
    base_model_path = args.model_path
    adapter_path = None
    logger.info("Full model: %s (no adapter)", base_model_path)

# 加载 base model（不含 adapter）
model, tokenizer = load_model_and_tokenizer(
    base_model_path, adapter_path=None, quantize=args.quantize
)

# 如果指定了 sft_adapter，先 merge SFT（用于 GRPO eval）
if args.sft_adapter:
    logger.info("Merging SFT adapter: %s", args.sft_adapter)
    model = PeftModel.from_pretrained(model, args.sft_adapter)
    model = model.merge_and_unload()

# 再加载 eval adapter（SFT 或 GRPO checkpoint）
if adapter_path:
    logger.info("Loading eval adapter: %s", adapter_path)
    model = PeftModel.from_pretrained(model, adapter_path)

model.eval()
```

### 评估命令示例

```bash
# SFT eval（不变）
python -m freige.eval.inference \
  --model_path /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/sft

# GRPO eval（新增 --sft_adapter）
python -m freige.eval.inference \
  --model_path /root/autodl-tmp/grpo_ced_r5/checkpoint-480 \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/grpo_ced_480
```

## 5. 总结

| 检查项 | 结论 |
|--------|------|
| GRPO checkpoint 格式 | LoRA adapter，与 SFT 格式一致 |
| inference.py 能否直接加载 GRPO checkpoint | **不能** -- 缺 SFT merge 中间步骤 |
| 统一 parsing 逻辑 | OK, parse_model_output 全模型通用 |
| Evi-F1 计算 | OK, 已实现（evaluator.compute_evi_f1） |
| EDCR 计算 | OK, 已实现 |
| 需要修改的文件 | `eval/inference.py`：新增 `--sft_adapter` 参数 + 双 adapter 加载逻辑 |
| 修改量 | ~15 行代码 |
