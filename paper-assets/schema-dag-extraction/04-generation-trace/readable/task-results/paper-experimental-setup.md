# paper experimental setup

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experimental-setup_20260515T164246_result.json`
- **Structured JSON:** [`e36c199d713d36853d61.json`](../../sessions/e3/e36c199d713d36853d61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§3 Experimental Setup 完成。两个文件已写入并注册：

**`experimental_setup.tex`** (~850 words, 5 subsections):
- §3.1 三数据集描述 + Table 1 引用
- §3.2 SCS/BCS 形式化定义（Eq.1-2），Qwen3-32B + MiniLM 双 embedding
- §3.3 Exp1 count curve（5 batches/count, 固定 1000 samples）+ Exp2 BCS-controlled factorial（Few-NERD n=54, FewRel 80-rel count {8,16}）
- §3.4 NER text-match F1, RE accuracy, ED relaxed F1（formal definition: token overlap + exact type match, 解释 exact F1 < 0.04），bootstrap 95% CI (1000 resamples)
- §3.5 Qwen3-32B-FP8 via vLLM, greedy decoding, thinking mode disabled, max 4096 tokens

**`dataset_stats.tex`** (Table 1): Few-NERD 66 types / 1000 / cross, FewRel 80 / 1000 / cross, MAVEN 168 / 18904† / same

**待处理 citation keys**: 5 个 `TODO-` 标记（ding-fewnerd-2021, han-fewrel-2018, wang-maven-2020, reimers-gurevych-2019, kwon-vllm-2023），需在 bib 文件中补齐后替换。

---
