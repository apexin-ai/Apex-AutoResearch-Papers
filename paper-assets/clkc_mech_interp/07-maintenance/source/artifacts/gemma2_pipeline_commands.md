# Gemma-2-9B-IT Pipeline 执行命令 (plan_102)

## 状态检查

### 模型验证 ✅
- 路径: `/root/autodl-tmp/models/gemma-2-9b-it/`
- 4 个 safetensors 分片 (~17.2GB 总计)
- config.json, tokenizer.json, tokenizer.model 均存在

### 数据目录 ✅
- `data/gemma2/` 已创建（空，准备接收输出）
- `logs/` 已创建

### ConflictQA 原始数据 ✅
- `data/raw_sampled_train.jsonl` ✅
- `data/raw_sampled_test.jsonl` ✅
- `data/en_conflict_train.jsonl` ✅
- `data/en_conflict_test.jsonl` ✅

### 翻译模型
- translate_to_zh.py 和 validate_translation.py 默认使用 Qwen3-8B-Instruct
- 模型路径: `/root/autodl-tmp/models/Qwen3-8B-Instruct/` ✅

---

## 环境前缀

所有命令前加：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/clkc_mech_interp
```

---

## Step 1: Verify EN Parametric Knowledge

用 Gemma 逐条回答问题，与 ChatGPT 的参数答案对比，翻转不一致的 conflict/no_conflict 标签。

```bash
CUDA_VISIBLE_DEVICES=1 python src/verify_parametric_knowledge.py \
    --model /root/autodl-tmp/models/gemma-2-9b-it \
    --data_dir data/ \
    --raw_dir data/ \
    --output_dir data/gemma2/ \
    --batch_size 8
```

**输入**: `data/raw_sampled_{train,test}.jsonl` + `data/en_conflict_{train,test}.jsonl`
**输出**: `data/gemma2/en_conflict_{train,test}_verified.jsonl`
**预估时间**: ~15-25 min (逐条生成，约 500+ 条)

---

## Step 2a: 复制 verified 文件为 translate 所需的输入格式

translate_to_zh.py 硬编码读取 `en_conflict_{train,test}.jsonl`（无 _verified 后缀），需要将 verified 文件复制为基础文件名，确保翻译后的 ZH 文件继承 Gemma-verified 标签。

```bash
cp data/gemma2/en_conflict_train_verified.jsonl data/gemma2/en_conflict_train.jsonl
cp data/gemma2/en_conflict_test_verified.jsonl data/gemma2/en_conflict_test.jsonl
```

## Step 2b: Translate to ZH

使用 Qwen3-8B-Instruct 将 EN 数据翻译为 ZH。

```bash
CUDA_VISIBLE_DEVICES=1 python src/translate_to_zh.py \
    --model /root/autodl-tmp/models/Qwen3-8B-Instruct \
    --input_dir data/gemma2/ \
    --output_dir data/gemma2/ \
    --batch_size 4
```

**输入**: `data/gemma2/en_conflict_{train,test}.jsonl` (已包含 Gemma-verified 标签)
**输出**: `data/gemma2/zh_conflict_{train,test}.jsonl`
**预估时间**: ~30-45 min (逐条翻译 4 个字段 × 500+ 条)

**注意**: 翻译模型是 Qwen3（不是 Gemma），无需额外加载 Gemma。

---

## Step 3: Validate Translation Quality (= Verify ZH)

Back-translate + COMET 评分，过滤低质量翻译。

```bash
CUDA_VISIBLE_DEVICES=1 python src/validate_translation.py \
    --model /root/autodl-tmp/models/Qwen3-8B-Instruct \
    --zh_dir data/gemma2/ \
    --en_dir data/gemma2/ \
    --output_dir data/gemma2/ \
    --threshold 0.80
```

**输入**: `data/gemma2/zh_conflict_{train,test}.jsonl` + `data/gemma2/en_conflict_{train,test}.jsonl`
**输出**: `data/gemma2/zh_conflict_{train,test}_validated.jsonl` + `data/gemma2/translation_quality_report.json`
**预估时间**: ~40-60 min (back-translate + COMET scoring)

**依赖**: `unbabel-comet` (检查是否已安装: `pip list | grep comet`)

---

## Step 4: Collect EN Activations

```bash
CUDA_VISIBLE_DEVICES=1 python src/collect_activations.py \
    --model /root/autodl-tmp/models/gemma-2-9b-it \
    --data_dir data/gemma2/ \
    --output_dir data/gemma2/ \
    --lang en \
    --batch_size 4
```

**输入**: `data/gemma2/en_conflict_{train,test}_verified.jsonl`
**输出**: `data/gemma2/en_activations.pt`
**预估时间**: ~10-15 min

---

## Step 5: Collect ZH Activations

```bash
CUDA_VISIBLE_DEVICES=1 python src/collect_activations.py \
    --model /root/autodl-tmp/models/gemma-2-9b-it \
    --data_dir data/gemma2/ \
    --output_dir data/gemma2/ \
    --lang zh \
    --batch_size 4
```

**输入**: `data/gemma2/zh_conflict_{train,test}_validated.jsonl`
**输出**: `data/gemma2/zh_activations.pt`
**预估时间**: ~10-15 min

---

## Step 6: Train Probes with Bootstrap (n=2000)

```bash
python src/train_probe.py \
    --activation_dir data/gemma2/ \
    --output_dir data/gemma2/ \
    --bootstrap_seeds 2000 \
    --output_file probe_results_bootstrap_n2000.json
```

**输入**: `data/gemma2/{en,zh}_activations.pt`
**输出**: `data/gemma2/probe_results_bootstrap_n2000.json` + `data/gemma2/probe_accuracy_by_layer.png`
**预估时间**: ~60-90 min (2000 seeds × 4 directions × 42 layers)

不需要 GPU（纯 LogisticRegression on CPU）。

---

## 时间/资源预估

| Step | 预估时间 | GPU 需求 | VRAM |
|------|---------|---------|------|
| 1. Verify EN | 15-25 min | cuda:1 | ~20GB (Gemma bf16) |
| 2. Translate ZH | 30-45 min | cuda:1 | ~18GB (Qwen3 bf16) |
| 3. Validate ZH | 40-60 min | cuda:1 | ~18GB (Qwen3) + COMET |
| 4. Collect EN acts | 10-15 min | cuda:1 | ~20GB (Gemma bf16) |
| 5. Collect ZH acts | 10-15 min | cuda:1 | ~20GB (Gemma bf16) |
| 6. Train probe | 60-90 min | 无 (CPU) | N/A |

**总计**: ~3-4 小时
**GPU**: RTX PRO 6000 96GB (cuda:1) 绰绰有余，Gemma bf16 约 18GB + 推理开销 ~25GB

---

## 潜在风险

1. **Gemma chat template**: verify 和 collect 脚本中用 `model.generate()` + `apply_chat_template`，需确认 Gemma-2-9B-IT 的 tokenizer 支持 chat template（通常内置于 tokenizer_config.json 中，已确认存在）。

2. **`model.model.layers` 路径**: collect_activations.py 用 `model.model.layers` 访问 transformer 层。Gemma-2 架构使用同名属性 ✅。

3. **`enable_thinking` 参数**: translate_to_zh.py 中 `apply_chat_template(enable_thinking=False)` 是 Qwen3 特有的。翻译和验证步骤使用 Qwen3 模型，不受影响。

4. **`strip_think_tags`**: verify 脚本中剥离 `<think>` 标签是 Qwen3 特有的。Gemma 不会生成此标签，该函数对 Gemma 输出无副作用 ✅。

5. **COMET 模型**: validate_translation.py 需要 `unbabel-comet` 包和 COMET 模型权重。如果首次运行，会自动下载 ~1.5GB 模型到默认缓存。

6. **label 传递**: 必须执行 Step 2a（复制 verified → base 文件名），否则 translate 会从 data/ 读取 ChatGPT 标签而非 Gemma-verified 标签，导致 ZH 数据标签错误。
