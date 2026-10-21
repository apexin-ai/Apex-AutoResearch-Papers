# Accumulation v3 脚本审查报告

## 现有 Pipeline 调研结果

- **LoRA 训练入口**: `scripts/lora_finetune.py`
  - 调用: `python scripts/lora_finetune.py --input_data <jsonl> --output_dir <dir> --model_name <path> --target_modules <modules> --gpu <id>`
  - 从 base model 加载 + 注入 LoRA adapter，训练后保存 adapter + tokenizer 到 output_dir
  - 使用 HuggingFace Trainer，读取 JSONL 中 `text` 字段进行 CLM 训练

- **文本生成入口**: `scripts/generate_next_depth.py`
  - 调用: `python scripts/generate_next_depth.py --adapter_dir <dir> --output_path <jsonl> --target_depth <N> --model_name <path> --gpu <id>`
  - 从 base model 加载 + 挂载 LoRA adapter，用 BOS token 无条件生成
  - 输出 JSONL: `{"text": ..., "depth": N, "seed_id": i, "token_count": ...}`

- **特征提取入口**: `scripts/extract_features.py`
  - 调用: `python scripts/extract_features.py --data_dir <dir> --model_path <ref_model> --output_path <jsonl> --gpu <id>`
  - 读取 `data_dir/depth_{0..max_depth}.jsonl`，用 frozen Pythia-1.4B 计算 19 个统计特征
  - 自动计算 truncation length (各 depth 的 token 长度中位数取最小值)

- **RF 评估入口**: `scripts/train_classifier.py` (现有) / `run_accumulation.py` 内置 (新实现)
  - 新实现使用 5-fold StratifiedKFold CV + 200 trees RF（现有版本是 80/20 split + 100 trees）

- **数据格式**:
  - 训练/生成 JSONL 字段: `text`, `depth`, `seed_id`, `token_count` (部分有 `source`)
  - 特征 JSONL 字段: `depth`, `sample_id`, + 19 个特征列
  - 每个 depth: 5000 条

- **LoRA 配置** (lora_finetune.py 默认值, 与 run_pipeline_gpt2xl.sh 一致):
  - r=16, alpha=32, dropout=0.05, bias=none, task=CAUSAL_LM
  - target_modules: `c_attn,c_proj` (GPT-2 XL)
  - lr=2e-4, epochs=3, bs=8, grad_accum=2, bf16=True
  - max_seq_len=512, seed=42

- **生成配置** (generate_next_depth.py 默认值):
  - strategy=nucleus, top_p=0.95, temperature=1.0
  - max_new_tokens=512, batch_size=16
  - 从 BOS token 无条件生成

- **19 个统计特征**:
  - PPL: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl, p10/p25/p50/p75/p90_ppl (9)
  - Surprisal: mean_surprisal, var_surprisal, entropy_of_surprisal (3)
  - Lexical: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy (4)
  - Repetition: rep_2gram, rep_3gram, rep_4gram (3)

## 脚本路径
`/root/autodl-tmp/recursive_gen_depth_est/scripts/run_accumulation.py`

## 脚本逻辑摘要

### 输入数据
- Human text: `data/depth_0.jsonl` (5000 条 Wikipedia 文本, 256-512 tokens)
- d0 synthetic: `data/gpt2xl/depth_1.jsonl` (full-replacement pipeline 中 LoRA-depth0 模型生成的 5000 条文本)

### 逐步流程

| 步骤 | 操作 | 设备 | 输入 | 输出 |
|------|------|------|------|------|
| **d1-A** | 混合训练语料 | CPU | human + d0_synthetic, ratio=MIX_RATIO | `train_d1.jsonl` (5000条) |
| **d1-B** | LoRA 微调 base model | **GPU** | `train_d1.jsonl` | `checkpoints/lora_depth_1/` |
| **d1-C** | BOS 无条件生成 | **GPU** | lora_depth_1 adapter | `data/depth_1.jsonl` (5000条) |
| **d2-A** | 混合训练语料 | CPU | human + **d1生成文本**, ratio=MIX_RATIO | `train_d2.jsonl` |
| **d2-B** | LoRA 微调 base model | **GPU** | `train_d2.jsonl` | `checkpoints/lora_depth_2/` |
| **d2-C** | BOS 无条件生成 | **GPU** | lora_depth_2 adapter | `data/depth_2.jsonl` |
| **d3-A** | 混合训练语料 | CPU | human + **d2生成文本**, ratio=MIX_RATIO | `train_d3.jsonl` |
| **d3-B** | LoRA 微调 base model | **GPU** | `train_d3.jsonl` | `checkpoints/lora_depth_3/` |
| **d3-C** | BOS 无条件生成 | **GPU** | lora_depth_3 adapter | `data/depth_3.jsonl` |
| **D** | 特征提取 (Pythia-1.4B ref) | **GPU** | depth_0..3.jsonl | `features.jsonl` |
| **E** | RF 评估 (200 trees, 5-fold CV) | CPU | `features.jsonl` | `eval_results/rf_eval_results.json` |

### 关键设计决策
1. **每个 depth 从 base GPT-2 XL 重新 LoRA 微调** (不是 continual training)
2. **训练数据是 raw text** (JSONL text 字段), 通过 subprocess 调用现有 `lora_finetune.py`
3. **混合语料的 synthetic 部分逐步更新**: d1 用 d0_synthetic, d2 用 d1_accum 生成文本, d3 用 d2_accum 生成文本
4. **混合采样种子**: `seed + depth` (d1=43, d2=44, d3=45), 确保不同 depth 的采样不完全相同
5. **depth_0 使用 symlink** 指向原始 human text, 避免复制

### 目录结构
```
accumulation/mix05/          (或 mix025/)
├── train_d1.jsonl           混合训练语料 (human + synthetic raw text)
├── train_d2.jsonl
├── train_d3.jsonl
├── data/
│   ├── depth_0.jsonl → data/depth_0.jsonl (symlink)
│   ├── depth_1.jsonl        accumulation d1 生成文本
│   ├── depth_2.jsonl        accumulation d2 生成文本
│   └── depth_3.jsonl        accumulation d3 生成文本
├── checkpoints/
│   ├── lora_depth_1/        LoRA adapter
│   ├── lora_depth_2/
│   └── lora_depth_3/
├── features.jsonl           19 维特征
└── eval_results/
    └── rf_eval_results.json 分类结果
```

## 运行命令 (预计, 未执行)
```bash
# cuda:0 运行 mix_ratio=0.5
cd /root/autodl-tmp/recursive_gen_depth_est
python scripts/run_accumulation.py --mix_ratio 0.5 --gpu_id 0 --seed 42

# cuda:1 运行 mix_ratio=0.25 (可并行)
python scripts/run_accumulation.py --mix_ratio 0.25 --gpu_id 1 --seed 42
```

中断恢复:
```bash
python scripts/run_accumulation.py --mix_ratio 0.5 --gpu_id 0 --seed 42 --skip_to 2
```

## 预估时间
- 每个 depth: LoRA train ~1.5h + generation ~0.5h = ~2h
- 特征提取: ~20min (4 depths x 5000 samples, Pythia-1.4B ref)
- RF 评估: ~1min
- **单个 ratio: 3 depths x 2h + 0.3h = ~6.3h**
- **两个 ratio 并行 (双 GPU): ~6.3h total**

## 磁盘需求预估
- 每个 ratio:
  - LoRA checkpoints: ~150 MB x 3 = ~450 MB (GPT-2 XL LoRA r=16, 仅 adapter 权重)
  - 训练语料 JSONL: ~11 MB x 3 = ~33 MB
  - 生成文本 JSONL: ~12 MB x 3 = ~36 MB
  - features.jsonl: ~14 MB
- **每个 ratio 总计: ~530 MB**
- **两个 ratio 总计: ~1.1 GB**

## 自检清单
- [x] 训练数据是 raw text (JSONL text 字段, 不是 features)
- [x] 每个 depth 调用了 LoRA 微调 (GPU, 通过 subprocess 调用 lora_finetune.py)
- [x] 每个 depth 调用了文本生成 (GPU, 通过 subprocess 调用 generate_next_depth.py)
- [x] 每个 depth 从 base model 重新训练 (lora_finetune.py 每次加载 fresh base model)
- [x] d2 的训练数据包含 d1 生成的文本 (prev_synthetic 在每个 depth 后更新为该 depth 的生成文本)
- [x] d3 的训练数据包含 d2 生成的文本 (同上)
- [x] 预估运行时间 > 6h (3 depths x ~2h = ~6h per ratio)
- [x] 脚本未执行, 未提交实验, 未启动 GPU 进程
