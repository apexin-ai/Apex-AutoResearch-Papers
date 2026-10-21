# exp_018 系列溯源调查 + 3-seed NER 5-signal 指标报告

**日期**: 2026-05-15  
**服务器**: autodl-5090  
**项目路径**: /root/autodl-tmp/struct_self_consist_ie

---

## 1. 目录概况

| 目录 | 文件 | 时间戳 | run.log |
|------|------|--------|---------|
| exp_018_qwen_scierc_seed123 | report.json, samples.jsonl | May 15 13:13 | **缺失** |
| exp_018_qwen_scierc_seed456 | report.json, run.log, samples.jsonl | May 15 13:13 | **有** |
| exp_018_llama_scierc_seed123 | report.json, samples.jsonl | May 15 13:12–13:13 | **缺失** |
| exp_018_llama_scierc_seed456 | report.json, run.log, samples.jsonl | May 15 13:08 | **有（但来自 exp_007）** |

---

## 2. 溯源结论

### exp_018_qwen_scierc_seed456 — **新推理**
- **证据**: run.log 时间戳 2026-05-15 13:08–13:13，vLLM 初始化使用 `checkpoints/qwen3-8b-scierc-merged-v2`
- run.log 末尾: `Sampling complete. Saved to output/exp_018_qwen_scierc_seed456/samples.jsonl`
- 这是今天新执行的推理，输出路径直接指向 exp_018 目录

### exp_018_qwen_scierc_seed123 — **新推理（缺日志）**
- **证据**: 服务器上无任何先前的 Qwen seed123 目录（仅 exp_012_rerun_1024 为 seed42）
- samples.jsonl 大小 3,823,802 字节，与 exp_012_rerun_1024 (3,820,412) 不同
- report.json 指标 (NER SJ ρ=0.3878) 与 exp_012_rerun_1024 (SJ ρ=0.3599) 不同
- **结论**: 首次推理的 Qwen seed123 实验，run.log 未被保留

### exp_018_llama_scierc_seed456 — **复制自 exp_007_llama_seed456**
- **证据**: 
  - MD5 完全一致: `2034b5e4989c387b84e2b7225c7e5367`（两个 samples.jsonl 相同）
  - run.log 时间戳为 2026-05-14 23:08–23:12（昨天），非今天
  - run.log 末尾: `Sampling complete. Saved to output/exp_007_llama_seed456/samples.jsonl` — **输出路径指向 exp_007，非 exp_018**
  - report.json 指标与 exp_007_llama_seed456 完全一致 (NER SJ ρ=0.3663, FK ρ=0.3115)
- **结论**: 文件整体复制到 exp_018 目录，非新推理

### exp_018_llama_scierc_seed123 — **新推理（缺日志）**
- **证据**:
  - MD5 不同: `072eeca68236d46b4c5c84b945209abc` vs exp_007_llama_seed123 的 `765712e5b842f12fd4f19494598ab341`
  - 文件大小不同: 3,762,518 vs 3,759,488 字节
  - report.json 指标不同: NER SJ ρ=0.3552, FK ρ=0.2897 vs exp_007 的 SJ ρ=0.3371, FK ρ=0.2143
  - 第一条 samples.jsonl 的 logprobs 值不同
- **结论**: 新的推理运行（可能使用不同参数，如 max_tokens=1024），run.log 未被保留

---

## 3. 关于 exp_018_llama_scierc_seed456/run.log 引用 exp_007 的解释

该 run.log 是 exp_007_llama_seed456 原始推理运行的日志**原文复制**。关键证据：
- 日志中所有时间戳为 May 14 23:08–23:12（一天前）
- 日志末尾明确写 `Saved to output/exp_007_llama_seed456/samples.jsonl`
- samples.jsonl 的 MD5 与 exp_007_llama_seed456 完全一致

**原因推测**: 创建 exp_018 目录时，直接将 exp_007_llama_seed456 的全部内容（samples.jsonl + run.log）复制过来，然后重新生成了 report.json（report.json 时间戳为 May 15 13:08）。这是数据复用，不是重新推理。

---

## 4. 缺 run.log 的实验来源判断

| 实验 | samples.jsonl 来源 | 依据 |
|------|-------------------|------|
| exp_018_qwen_scierc_seed123 | **首次推理** | 无先前 Qwen seed123 目录存在 |
| exp_018_llama_scierc_seed123 | **新推理**（非 exp_007 复制）| MD5 不同、指标不同、logprobs 不同 |

---

## 5. Spec 信息

### 共通参数
- **dataset**: scierc / joint
- **n_instances**: 551
- **n_samples (N)**: 8
- **temperature (T)**: 1.0
- **use_train_format**: True
- **tensor_parallel_size**: 1 (单 GPU)
- **vLLM**: v0.18.1
- **dtype**: bfloat16

### 各实验 Spec

| 实验 | seed | model_path | max_tokens | 推理类型 | 原始 output_dir |
|------|------|------------|------------|---------|----------------|
| exp_018_qwen_scierc_seed123 | 123 | checkpoints/qwen3-8b-scierc-merged-v2 | 1024(推测) | 新推理 | exp_018_qwen_scierc_seed123 |
| exp_018_qwen_scierc_seed456 | 456 | checkpoints/qwen3-8b-scierc-merged-v2 | 1024(推测) | 新推理 | exp_018_qwen_scierc_seed456 |
| exp_018_llama_scierc_seed123 | 123 | checkpoints/llama3.1-8b-scierc-merged | 1024(推测) | 新推理 | exp_018_llama_scierc_seed123 |
| exp_018_llama_scierc_seed456 | 456 | checkpoints/llama3.1-8b-scierc-merged | 1024(确认) | 复制 exp_007 | exp_007_llama_seed456 |

**注**: max_tokens=1024 基于实验命名惯例推测（exp_012_rerun_**1024** 为同系列 seed42 实验）。run.log 中未显示 max_tokens 参数。有 run.log 的实验可从 vLLM 配置确认 `max_seq_len=4096`（模型上下文长度，非生成 max_tokens）。

**CUDA_VISIBLE_DEVICES**: run.log 中未显示该环境变量。vLLM 配置显示 `data_parallel_size=1, pipeline_parallel_size=1, tensor_parallel_size=1`，使用单 GPU。

---

## 6. 3-seed NER 5-signal 指标

### 数据来源映射

| Model | seed42 目录 | seed123 目录 | seed456 目录 |
|-------|------------|-------------|-------------|
| Qwen3-8B-SciERC | exp_012_rerun_1024 | exp_018_qwen_scierc_seed123 | exp_018_qwen_scierc_seed456 |
| LLaMA3.1-8B-SciERC | exp007_llama_inference | exp_018_llama_scierc_seed123 | exp_018_llama_scierc_seed456 |

### 6.1 NER Full ρ (Spearman rank correlation)

| Signal | Qwen s42 | Qwen s123 | Qwen s456 | **Qwen mean±σ** | LLaMA s42 | LLaMA s123 | LLaMA s456 | **LLaMA mean±σ** |
|--------|----------|-----------|-----------|-----------------|-----------|------------|------------|------------------|
| SJ | 0.3599 | 0.3878 | 0.3445 | **0.3641±0.0220** | 0.3630 | 0.3552 | 0.3663 | **0.3615±0.0057** |
| FK | 0.2665 | 0.2628 | 0.2314 | **0.2536±0.0193** | 0.3266 | 0.2897 | 0.3115 | **0.3093±0.0186** |
| logprob | 0.2052 | 0.2341 | 0.2107 | **0.2167±0.0154** | 0.1827 | 0.1970 | 0.1911 | **0.1903±0.0072** |
| EM | 0.2945 | 0.3135 | 0.3205 | **0.3095±0.0134** | 0.3152 | 0.2844 | 0.3088 | **0.3028±0.0163** |
| voting_conf | 0.3792 | 0.4133 | 0.3909 | **0.3945±0.0173** | 0.4331 | 0.4193 | 0.4135 | **0.4220±0.0101** |

### 6.2 NER Full AUROC

| Signal | Qwen s42 | Qwen s123 | Qwen s456 | **Qwen mean±σ** | LLaMA s42 | LLaMA s123 | LLaMA s456 | **LLaMA mean±σ** |
|--------|----------|-----------|-----------|-----------------|-----------|------------|------------|------------------|
| SJ | 0.6917 | 0.7236 | 0.6996 | **0.7050±0.0166** | 0.7099 | 0.7092 | 0.7061 | **0.7084±0.0020** |
| FK | 0.6290 | 0.6308 | 0.6213 | **0.6270±0.0051** | 0.6648 | 0.6678 | 0.6723 | **0.6683±0.0038** |
| logprob | 0.5783 | 0.6124 | 0.6030 | **0.5979±0.0176** | 0.5569 | 0.5839 | 0.5636 | **0.5681±0.0141** |
| EM | 0.7493 | 0.7605 | 0.7668 | **0.7589±0.0088** | 0.7658 | 0.7468 | 0.7538 | **0.7555±0.0096** |
| voting_conf | 0.6841 | 0.7182 | 0.6971 | **0.6998±0.0172** | 0.7283 | 0.7159 | 0.7113 | **0.7185±0.0088** |

### 6.3 信号排序一致性

**ρ 排序** (3-seed mean):
- Qwen: voting_conf (0.394) > SJ (0.364) > EM (0.310) > FK (0.254) > logprob (0.217)
- LLaMA: voting_conf (0.422) > SJ (0.362) > FK (0.309) > EM (0.303) > logprob (0.190)

**AUROC 排序** (3-seed mean):
- Qwen: EM (0.759) > SJ (0.705) > voting_conf (0.700) > FK (0.627) > logprob (0.598)
- LLaMA: EM (0.756) > voting_conf (0.719) > SJ (0.708) > FK (0.668) > logprob (0.568)

**稳定性** (σ 最小 → 最稳定):
- LLaMA 各信号跨 seed 方差普遍小于 Qwen（LLaMA SJ σ=0.006 vs Qwen σ=0.022）
- EM 的 AUROC 在两个模型上都非常稳定 (σ < 0.01)
- logprob 的 AUROC 方差相对较大

---

## 7. 时间线重建

| 时间 | 事件 |
|------|------|
| May 14 ~21:58 | exp007_llama_inference (LLaMA seed42) 推理完成 |
| May 14 ~23:08–23:12 | exp_007_llama_seed123 + exp_007_llama_seed456 批量推理 |
| May 15 ~06:17 | exp_012_rerun_1024 (Qwen seed42) 推理完成 |
| May 15 ~07:09–07:38 | exp_012_rerun_1024 5-signal/AUROC 分析完成 |
| May 15 ~13:08 | exp_018_llama_scierc_seed456 目录创建（复制自 exp_007） |
| May 15 ~13:08–13:13 | exp_018_qwen_scierc_seed456 新推理 |
| May 15 ~13:12–13:13 | exp_018_llama_scierc_seed123 新推理 + exp_018_qwen_scierc_seed123 新推理 |
| May 15 ~13:13 | 所有 exp_018 的 report.json 生成 |

---

## 附录：原始数据文件

- 5-signal 分析结果: `/root/autodl-tmp/struct_self_consist_ie/output/exp018_3seed_5signal_results.json`
- 分析脚本: `/root/autodl-tmp/struct_self_consist_ie/code/exp018_5signal_analysis.py`
