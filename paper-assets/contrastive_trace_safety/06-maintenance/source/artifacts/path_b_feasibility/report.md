# Path B 数据扩展可行性

## 当前数据概况

**数据来源**: HuggingFace `ishitakakkar-10/HarmThoughts` dataset

| 模型 | 数据集总traces | Jailbreak | Jailbreak+CP | Safe | 已提取HS |
|------|--------------|-----------|-------------|------|---------|
| R1-32B | 221 | 150 | **100** | 71 | 100 (全部) |
| QwQ-32B | 140 | 100 | **95** | 40 | 95 (全部) |
| R1-8B | 324 | 209 | 209 | 115 | 209 |

**结论**: HarmThoughts 数据集中的 jailbreak+CP traces 已全部用尽。扩展到 n≥200 必须自行生成新 traces。

**数据格式**: 每条 trace 对应一个 `.pt` 文件:
- `hidden_states`: tensor `[num_sentences, 64, 5120]` (fp16)
- `trace_id`, `num_sentences`, `commitment_point`, `step_labels`, `query`

**Trace 统计**:
- R1-32B: 平均 38.6 sentences/trace, ~857 tokens/trace
- QwQ-32B: 平均 50.0 sentences/trace, ~1012 tokens/trace

## 生成方案

### 现有脚本
- 隐层提取 (R1-32B): `src/experiments/exp_001a_extract_r1_32b.py`
- 隐层提取 (QwQ): `src/experiments/exp_001b_extract_qwq.py`
- 数据加载: `src/data_loader.py` (从 HarmThoughts 读取)
- Pilot 生成参考: `pilot_7b.py` (R1-7B trace 生成, 可复用结构)

### Prompt 来源
- 数据集中存在大量未被 32B 模型使用过的 jailbreak prompts:
  - 可用于 R1-32B: **695 个未用 queries** (来自 r1-8b / QwQ / ot-7b)
  - 可用于 QwQ: **776 个未用 queries**
- Prompts 充足，不构成瓶颈

### 推理配置
- R1-32B 模型路径: `/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B` (62GB, 已缓存)
- QwQ-32B 模型路径: `/root/autodl-tmp/.hf_cache/Qwen/QwQ-32B` (62GB, 已缓存)
- 采样参数 (参考 pilot_7b): `temperature=0.6, top_p=0.95, max_new_tokens=4096`
- Chat format: `tokenizer.apply_chat_template`

### 扩展 Pipeline (4 步)

1. **Trace 生成**: 用 32B 模型推理 jailbreak prompts → 获取 CoT reasoning + response
2. **Sentence Splitting**: 拆分为句子 (nltk / regex)
3. **Annotation**: 标注每个句子的类别 (16 类: DKE, TD, IA, FL, RA, CE, OB, HV, AL, IR, ED, PS, CR, CC, PA, RS)
   - SAFETY_LABELS = {RA, AL, CC, ED, IA} → 这些定义 commitment point
4. **Hidden State 提取**: 复用现有 `exp_001a/001b` 脚本逻辑

## 资源预估

### GPU 配置
- **2× NVIDIA RTX PRO 6000 Blackwell** (98GB VRAM each, currently 97GB free)
- 32B fp16 模型 = ~64GB → 单卡可容纳，有充裕余量

### 需要生成的 traces 数量
考虑 jailbreak yield rate (不是所有 prompt 都会产生 jailbreak+CP):
- R1-32B: 需 100 more CP traces, yield=45% → 需运行 ~**225 queries**
- QwQ-32B: 需 105 more CP traces, yield=68% → 需运行 ~**155 queries**
- 总计: ~380 queries

### 时间预估

| Step | R1-32B | QwQ-32B | 备注 |
|------|--------|---------|------|
| 模型加载 | ~2 min | ~2 min | 一次性 |
| Trace 生成 | ~75 min (225q × 20s) | ~52 min (155q × 20s) | **可并行** (2 GPUs) |
| Sentence split | ~1 min | ~1 min | CPU |
| Annotation | **2-4 hours** | **2-4 hours** | 见下文 |
| Hidden state 提取 | ~8 min (100t × 5s) | ~9 min (105t × 5s) | 重载模型 |

**Annotation 是关键瓶颈**. 三种方案:
1. **LLM API (推荐)**: 用 Claude/GPT-4 标注 ~15000 sentences. 成本 ~$15-30, 耗时 2-4 小时 (含 rate limit)
2. **本地分类器**: 用现有 8525 条 r1-32b 标注数据训练 BERT/小模型分类器. 耗时 ~1 小时训练, 精度可能略低
3. **规则匹配**: 基于关键词 (参考 pilot_7b.py), 最快但精度最差

### 磁盘预估
- Raw traces (JSON): ~10MB (可忽略)
- Hidden states (100 new R1-32B): ~2.2GB
- Hidden states (105 new QwQ): ~3.4GB
- **总额外磁盘**: ~5.6GB
- **可用空间**: 90GB → 完全充裕

## 可行性结论

### 是否可在 deadline (May 25) 前完成?
**可以.** 保守估计 1.5 天即可完成全部 pipeline.

### 瓶颈
1. **Annotation** (最大瓶颈): 需要对 ~15000 新 sentences 标注 16 类安全标签
   - 推荐方案: LLM API annotation (Claude) + 人工抽检
   - 备选方案: 训练本地 classifier (用 HarmThoughts 中已有的 8525 条标注数据)
2. **Jailbreak yield**: 不是所有 prompt 都能产生 jailbreak+CP trace, 需要多跑 queries
3. **模型加载**: 32B 模型加载需 ~2 min, 但只需一次

### 不构成瓶颈的
- GPU 显存: 98GB 远超 64GB 需求
- Prompts: 700+ 可用, 远超需要
- 磁盘: 90GB 可用, 仅需 5.6GB
- 模型缓存: 两个 32B 模型都已在本地
- Hidden state 提取: 现有脚本可直接复用, 总时间 <20 min

### 建议方案 (Day 1-2)

**Day 1**:
1. 编写 trace 生成脚本 (基于 pilot_7b.py 改造)
2. 两个 GPU 并行生成 traces (R1-32B on GPU0, QwQ on GPU1)
3. Sentence splitting
4. 启动 LLM annotation (或训练本地 classifier)

**Day 2**:
5. Annotation 完成 + 抽检
6. 筛选 jailbreak+CP traces (目标: 各 ≥100 new)
7. 运行 hidden state extraction
8. 验证: 重跑 bootstrap test 确认统计显著性

**最终目标**: R1-32B ≥ 200 traces (40 test), QwQ-32B ≥ 200 traces (40 test)
