# research llm baseline numbers

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_llm-baseline-numbers_20260523T050340_result.json`
- **Structured JSON:** [`32dd4985e9c732b76aba.json`](../../sessions/32/32dd4985e9c732b76aba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是汇总结果：

---

## LLM-based DocRE Baselines on Re-DocRED

### AutoRE

AutoRE 原论文（[arXiv 2403.14888](https://arxiv.org/abs/2403.14888)，ACL 2024 Demo，非 AAAI）**只报告 F1，不报告 ign_f1**：

| Variant | Re-DocRED dev F1 | Re-DocRED test F1 | Source |
|---------|------------------|--------------------|--------|
| AutoRE-Vicuna-7B | 54.29 | 53.84 | 原论文 Table 4 |
| AutoRE-Mistral-7B | 53.01 | 51.91 | 原论文 Table 4 |
| AutoRE-ChatGLM3-6B | 49.86 | 51.11 | 原论文 Table 4 |

AutoRE-LLaMA3-8B 的 **ign_f1** 来自 RelPrior 论文（[arXiv 2511.08143](https://arxiv.org/html/2511.08143)，Table 2）复现：

| Variant | dev Ign F1 | dev F1 | test Ign F1 | test F1 |
|---------|-----------|--------|------------|---------|
| AutoRE-LLaMA3-8B | **52.14** | 52.28 | **51.55** | 51.97 |

### GLiDRE

**注意：GLiDRE 是 dual-encoder 模型（几百M参数），不是 LLM generative 方法。**（[arXiv 2508.00757](https://arxiv.org/abs/2508.00757)）

| Setting | dev Ign F1 | dev F1 | test Ign F1 | test F1 | Source |
|---------|-----------|--------|------------|---------|--------|
| Fully supervised | 76.70±0.35 | 77.76±0.35 | 76.80±0.22 | 77.83±0.23 | Table 1 |
| Zero-shot | 16.37 | 16.72 | 16.41 | 17.32 | Table 3 |

GLiDRE 与 LLM generative 方法不直接可比（架构完全不同）。

### 其他 LLM-based Baselines（从 GLiDRE 和 RelPrior 论文中提取）

**RelPrior**（[arXiv 2511.08143](https://arxiv.org/html/2511.08143)，Table 2）：

| Method | dev Ign F1 | dev F1 | test Ign F1 | test F1 |
|--------|-----------|--------|------------|---------|
| RelPrior-LLaMA3-8B | **55.50** | 55.94 | **54.53** | 54.80 |
| RelPrior-LLaMA3.1-8B | 54.31 | 54.88 | 53.48 | 53.56 |
| RelPrior-Qwen2.5-7B | 51.02 | 51.43 | 50.64 | 50.72 |
| D-R-F-LLaMA3-8B | 50.56 | 51.04 | 50.02 | 50.49 |

**LMRC**（[arXiv 2408.13889](https://arxiv.org/html/2408.13889v1)，Table 7b）— 注意 LMRC 用 LLM+关系分类器，非纯 generative：

| Method | test Ign F1 | test F1 | Source |
|--------|------------|---------|--------|
| LMRC-LLaMA2-13B-Chat | **74.08** | 74.63 | LMRC 原论文 |
| LMRC-LLaMA2-7B-Chat | 72.33 | 72.92 | LMRC 原论文 |
| LMRC-LLaMA3-8B-Instruct | 72.21 | 72.80 | GLiDRE Table 1 |
| LMRC-LLaMA3.1-8B-Instruct | 72.35 | 72.93 | GLiDRE Table 1 |

---

### 关键发现

1. **AutoRE 原论文不报 ign_f1**，只有 F1。ign_f1 数据来自 RelPrior 用 LLaMA3-8B 复现（dev 52.14 / test 51.55）。Mistral/Vicuna 版本的 ign_f1 无公开数据。

2. **GLiDRE 不是 LLM-based 方法**，是 encoder-based dual-encoder。其 supervised 结果（ign_f1=76.80）不适合与 LLM generative 方法对比。

3. **最相关的纯 LLM generative baselines**（与我们方法可比）：
   - AutoRE-LLaMA3-8B: Re-DocRED dev ign_f1 = **52.14**
   - RelPrior-LLaMA3-8B: Re-DocRED dev ign_f1 = **55.50**（当前 LLM-based SOTA）
   - D-R-F-LLaMA3-8B: Re-DocRED dev ign_f1 = **50.56**

4. **LMRC** 成绩很高（72+）但使用 LLM+分类器混合架构，是否归类为 "LLM-based" 取决于你的定义。

---
