# research storycloze investigation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_storycloze_investigation_20260519T143651_result.json`
- **Structured JSON:** [`0378768a381c1452e491.json`](../../sessions/03/0378768a381c1452e491.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已足够。以下是完整调查结果：

```
=== StoryCloze Investigation ===

1. lm-eval support: Available but BROKEN (data access issue)
   - Task name(s): storycloze_2016, storycloze_2018
   - Dataset: LSDSem/story_cloze (HuggingFace)
   - Problem: 该数据集使用旧式 loading script (story_cloze.py)，
     当前 datasets 库 (lm-eval 0.4.12 环境) 已不支持脚本加载，
     报错 "Dataset scripts are no longer supported"
   - 原始数据源: storycloze.cs.rochester.edu（需注册申请）
   - 本地缓存: /root/.cache/huggingface/hub/datasets--LSDSem--story_cloze/
     仅有 repo 元数据，无实际数据文件
   
   ★ 替代方案: xstorycloze_en
     - Dataset: juletxara/xstory_cloze (en)
     - 同类任务（4句故事 + 2选1结尾），公开免费
     - 格式: multiple_choice, metric: acc

2. LAMBADA variants found:
   - lambada_openai        (EleutherAI/lambada_openai, loglikelihood, 已本地缓存 ✓)
   - lambada_standard      (cimec/lambada, loglikelihood)
   - lambada_openai_cloze_yaml   (同 openai 数据, cloze prompt 格式)
   - lambada_standard_cloze_yaml (同 standard 数据, cloze prompt 格式)
   - lambada_mt_*          (多语言变体: de/en/es/fr/it)
   - lambada_uyghur        (维吾尔语)

3. Other context-completion benchmarks in lm-eval:
   - swag                  (allenai/swag, 4选1续写, HellaSwag 前身, 免费 ✓)
   - hellaswag             (已在 exp-011 使用)
   - squad_completion      (SQuAD-based, 自定义 task class)
   - xstorycloze_en        (见上, 免费 ✓)

4. Recommendation — 向 exp-011 补充以下 benchmark:

   (a) lambada_openai [首选，必加]
       - 最经典的上下文预测 benchmark，预测段落最后一个词
       - loglikelihood 任务，直接测 entrainment 对长程上下文建模的影响
       - 数据已本地缓存，零额外下载
       - 指标: perplexity + acc
       - ★ 这是最接近 Reviewer 要求的"第二锚点"

   (b) xstorycloze_en [推荐]
       - StoryCloze 的可用替代品，任务结构相同
       - 4句故事上下文 → 2选1正确结尾
       - multiple_choice 任务，测叙事连贯性理解
       - 公开数据，无需注册

   (c) swag [可选]
       - HellaSwag 的前身，4选1续写
       - 与 HellaSwag 有高度相关性，加了信息增量有限
       - 如果 benchmark 数量不是瓶颈可以加

   优先级: lambada_openai > xstorycloze_en >> swag
```

---
