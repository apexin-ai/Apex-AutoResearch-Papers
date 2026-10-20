# LLM Local Inference Alternatives Assessment

**Date:** 2026-05-21  
**Context:** exp-003 Phase B requires LLM annotation on ~5,000 TweetEval sentiment tweets (3-class: positive/neutral/negative). API key unavailable after 3 requests.

---

## 1. Candidate Model Comparison Table

| Model | Total Params | FP16 VRAM | INT4 VRAM | Min GPUs (FP16) | Min GPUs (INT4) | Est. Speed (tok/s, INT4) | Sentiment Acc (zero-shot) |
|-------|-------------|-----------|-----------|-----------------|-----------------|--------------------------|---------------------------|
| Qwen3-235B-A22B | 235B (22B active) | ~470 GB | ~117 GB | 8x A100 80GB | 4x H100 80GB | ~15-25 | ~85-88% |
| Qwen2.5-72B-Instruct | 72B | ~144 GB | ~40 GB | 2x A100 80GB | **1x A100 80GB** | ~30-50 | ~82-85% |
| Llama-3.1-70B-Instruct | 70B | ~140 GB | ~38 GB | 2x A100 80GB | **1x A100 80GB** | ~30-50 | ~80-84% |
| Qwen2.5-7B-Instruct | 7B | ~14 GB | ~5 GB | **1x A100 80GB** | **1x A100 80GB** | ~100-200 | ~72-78% |
| Llama-3.1-8B-Instruct | 8B | ~16 GB | ~6 GB | **1x A100 80GB** | **1x A100 80GB** | ~100-200 | ~70-76% |

---

## 2. Detailed Assessment

### 2.1 Qwen3-235B-A22B (MoE)

**GPU Requirements:**
- FP16: ~470 GB VRAM → 8x A100 80GB (或 6x H100 80GB)
- INT4: ~117 GB → 最少 2x A100 80GB (紧凑), 推荐 4x A100 80GB
- 注意：虽然激活参数仅 22B，但全部 235B 权重必须加载到显存

**推理速度估算:**
- INT4 + vLLM, 4x A100: ~15-25 tokens/s (单请求), batch 处理可提升 5-10x
- 5000 条 tweets × ~300 tokens/条 ÷ 150 tok/s (batched) ≈ **~2.8 小时**

**标注质量:**
- 预期 zero-shot 3-class sentiment accuracy: 85-88%
- GPT-4 级表现，跨子群异质误分类特征明显

**结论:** 资源需求远超预算 (4+ GPU)，排除。

---

### 2.2 Qwen2.5-72B-Instruct ★ 推荐

**GPU Requirements:**
- FP16: ~144 GB → 2x A100 80GB (tensor parallel)
- INT4 (AWQ/GPTQ): ~40 GB → **1x A100 80GB 可运行** (剩余 ~35GB 给 KV cache)
- vLLM 部署: 单卡 A100 80GB 可用 AWQ-Int4 版本

**推理速度估算:**
- INT4 + vLLM, 1x A100 80GB: ~30-50 tokens/s (单请求)
- Batch inference (batch=32): ~200-400 tokens/s 总吞吐
- 5000 条 × 300 tokens ÷ 300 tok/s ≈ **~1.4 小时**

**标注质量:**
- Zero-shot 3-class sentiment: ~82-85% accuracy (F1 ~0.80-0.83)
- 达到 GPT-4 性能的 90%+ (研究表明 LLaMA3.1_70B/Qwen2.5-72B 达到 ChatGPT-4 的 >90%)
- Qwen2.5 系列在多语言 sentiment 任务上表现优异
- **会产生跨子群异质误分类** — 对特定话题/表达风格的推文系统性偏差

**可行性:** 1x A100 80GB + AWQ-Int4 即可运行，完全在预算内。

---

### 2.3 Llama-3.1-70B-Instruct

**GPU Requirements:**
- FP16: ~140 GB → 2x A100 80GB
- INT4 (AWQ): ~38 GB → **1x A100 80GB 可运行**
- 与 Qwen2.5-72B 资源需求几乎相同

**推理速度估算:**
- INT4 + vLLM, 1x A100 80GB: ~30-50 tokens/s
- Batch: ~200-400 tokens/s
- 总推理时间: **~1.5 小时**

**标注质量:**
- Zero-shot 3-class sentiment: ~80-84% accuracy
- Meta 训练数据含大量社交媒体文本，对 tweet 风格适应性好
- 略逊于 Qwen2.5-72B（Qwen 在 NLP benchmarks 上整体领先 1-3 分）

**可行性:** 同样 1x A100 80GB 可行，作为 Qwen2.5-72B 的备选。

---

### 2.4 小模型 (Backup Plan)

#### Qwen2.5-7B-Instruct
- FP16: ~14 GB → 单卡 A100 轻松运行（甚至 RTX 4090 24GB 可跑）
- 推理极快: ~100-200 tokens/s 单请求, batch 可达 1000+ tok/s
- 总推理时间: **~25 分钟**
- Zero-shot sentiment: ~72-78% accuracy
- **足以产生异质误分类**：准确率不高反而更易观察到跨子群差异

#### Llama-3.1-8B-Instruct
- 资源需求与 Qwen2.5-7B 相当
- Zero-shot sentiment: ~70-76%
- Fine-tuned 可达 90%+，但 zero-shot 较弱

**关键判断:** 7B/8B 模型的 ~25% 误分类率实际上**有利于实验设计** — 更大的误分类异质性使 HTE 效应更容易检测。但需确保误分类不是纯随机的（需要系统性偏差才有意义）。

---

## 3. 推理时间估算汇总

| Model | Quantization | GPUs | 5000 tweets 总时间 |
|-------|-------------|------|-------------------|
| Qwen2.5-72B-AWQ | INT4 | 1x A100 80GB | ~1.4 小时 |
| Llama-3.1-70B-AWQ | INT4 | 1x A100 80GB | ~1.5 小时 |
| Qwen2.5-7B (FP16) | None | 1x A100 80GB | ~25 分钟 |
| Llama-3.1-8B (FP16) | None | 1x A100 80GB | ~25 分钟 |

---

## 4. 费用估算 (AutoDL 云 GPU)

| 配置 | AutoDL 单价 | 推理用时 | 总费用 |
|------|------------|---------|--------|
| 1x A100 80GB | ~¥5/小时 | 2 小时 (含部署) | ~¥10 |
| 1x A100 80GB (72B 模型) | ~¥5/小时 | 3 小时 (含下载+部署+推理) | ~¥15 |
| 1x A100 80GB (7B 模型) | ~¥5/小时 | 1.5 小时 (含下载+部署+推理) | ~¥8 |

注：模型下载 (Qwen2.5-72B-AWQ ~40GB) 在 AutoDL 内网从 HuggingFace 镜像通常 10-20 分钟。

---

## 5. 推荐方案

### 首选: Qwen2.5-72B-Instruct-AWQ (INT4)

**理由:**
1. 1x A100 80GB 即可运行，费用 <¥20
2. Zero-shot sentiment accuracy ~82-85%，接近 GPT-4 水平
3. 会产生有意义的跨子群异质误分类（实验所需）
4. HuggingFace 已有官方 AWQ 量化版本，无需自行量化
5. vLLM 原生支持，部署简单

### 备选: Qwen2.5-7B-Instruct (FP16)

**理由:**
1. 资源需求极低，任何单卡即可
2. 推理极快（25 分钟完成全部标注）
3. 较低准确率 (~75%) 产生更大误分类异质性
4. 可作为"高噪声标注者"与 72B 形成对比实验

### 建议策略: 两模型并行标注

同一张 A100 80GB 上先跑 7B (25 min) 再跑 72B-AWQ (1.5 hr)，总计 ~2 小时：
- 72B 作为"高质量 LLM annotator"（模拟 GPT-4 级）
- 7B 作为"低质量 LLM annotator"（更大噪声）
- 两者对比可增强实验关于 annotator quality → HTE estimation 的发现

---

## 6. 决策建议: API Key vs 本地模型

| 维度 | 继续等 API Key | 本地模型路径 |
|------|--------------|-------------|
| 时间 | 不确定（已等 3 轮） | 1-2 天内完成 |
| 费用 | API 调用费 (GPT-4: ~$15-25 for 5K tweets) | AutoDL: ¥15-20 |
| 质量 | GPT-4 最优 | Qwen2.5-72B 达 GPT-4 的 90%+ |
| 可控性 | 依赖外部 | 完全自主 |
| 可复现 | 模型版本可能更新 | 本地固定版本，完全可复现 |

**建议: 立即走本地模型路径。** 不再等 API key。

理由：
1. API key 三次催促未果，继续等待机会成本过高
2. 开源模型质量已足够（>90% GPT-4 性能）
3. 费用极低（<¥20）
4. 本地推理可复现性更好（固定模型版本+固定 random seed）
5. 可同时获得多质量级别的标注（对实验有额外价值）

---

## 7. 向 Director 申请的资源

**最低需求:**
- 1x A100 80GB GPU（AutoDL 租用，约 ¥15-20 总费用，3 小时用时）
- 或：申请实验室/集群已有的任意 80GB+ GPU 2-3 小时使用权

**推荐需求:**
- 1x A100 80GB，预留半天（含调试和多模型运行）
- 预算：¥50 以内（含冗余）

**申请话术建议:**
> "exp-003 Phase B 需要 LLM 标注 5000 条 tweets。API key 多次申请未批准。拟用开源模型 (Qwen2.5-72B) 本地推理替代，仅需 1 张 A100 80GB 运行约 2 小时，AutoDL 租用费用约 ¥20。请批准。"

---

## Sources

- [Qwen3-235B-A22B Hardware Discussion](https://huggingface.co/Qwen/Qwen3-235B-A22B/discussions/43)
- [Qwen3-235B GPU Requirements Guide](https://willitrunai.com/blog/qwen-3-gpu-requirements)
- [Deploy Qwen 3 on GPU Cloud](https://www.spheron.network/blog/deploy-qwen3-gpu-cloud/)
- [Qwen2.5-72B-Instruct-AWQ (HuggingFace)](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-AWQ)
- [Qwen2.5-72B-Instruct-GPTQ-Int4 (HuggingFace)](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4)
- [Qwen2.5 Speed Benchmark](https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html)
- [4xA100 vs 4xA6000 vLLM Benchmark for 72B](https://www.databasemart.com/blog/vllm-gpu-benchmark-a100-40gb-4)
- [Self-Hosting LLaMA 3.1 70B Affordably](https://abhinand05.medium.com/self-hosting-llama-3-1-70b-or-any-70b-llm-affordably-2bd323d72f8d)
- [Llama-3.1-70B-Instruct-AWQ-INT4 (HuggingFace)](https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4)
- [vLLM v0.6.0 Performance Update](https://blog.vllm.ai/2024/09/05/perf-update.html)
- [LLM Inference Benchmark on AI Accelerators](https://arxiv.org/html/2411.00136v1)
- [Benchmarking Open-Source LLMs for Sentiment Classification](https://www.researchgate.net/publication/392176071)
- [Sentiment Analysis in the Age of Generative AI](https://link.springer.com/article/10.1007/s40547-024-00143-4)
- [AutoDL Pricing](https://www.autodl.com/docs/price/)
- [AWQ Quantization Guide for LLM Deployment](https://www.spheron.network/blog/awq-quantization-guide-llm-deployment/)
