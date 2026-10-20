# audit citation verify w3

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation-verify-w3_20260526T101541_result.json`
- **Structured JSON:** [`7bb87042c09047963fdf.json`](../../sessions/7b/7bb87042c09047963fdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。现在编写完整报告。

---

# 引用逐项正确性验证报告（Worker 3/3）

## 逐条验证结果（按 bib key 字母序）

```
[abreu2007accuracy] Abreu(2007) "On the Accuracy of Spectrum-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL suspiciousness ranking
  问题: 无
```

```
[appt2024] Zhang(2024) "APPT: Boosting Automated Patch Correctness..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — patch correctness prediction (79.7%)
  问题: 无
```

```
[austin2021program] Austin(2021) "Program Synthesis with Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ — MBPP-sanitized
  引用位置: [method.tex:13] ✓ — MBPP-sanitized
  问题: 无
```

```
[barr2015oracle] Barr(2015) "The Oracle Problem in Software..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:15] ✓ — test oracle problem
  问题: 无
```

```
[bengio2009curriculum] Bengio(2009) "Curriculum Learning"
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓ — curriculum learning
  问题: 无
```

```
[bouzenia2025repairagent] Bouzenia(2025) "RepairAgent: An Autonomous, LLM-Based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓ — agent-based repair
  问题: 无
```

```
[chen2021evaluating] Chen(2021) "Evaluating Large Language Models Trained..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ — HumanEval
  引用位置: [method.tex:13] ✓ — HumanEval
  问题: 无
```

```
[chen2024selfdebug] Chen(2024) "Teaching Large Language Models to..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓ — SelfDebug iteratively refine code
  问题: 无
```

```
[chen2025tracepile] Chen(2025) "Chain of Execution Supervision Promotes..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ — traces for code LLMs
  引用位置: [related_work.tex:5] ✓ — TracePile pre-trained on 2.6M samples（确认 TracePile 是该论文数据集名）
  引用位置: [method.tex:7] ✓ — code generation
  问题: 无
```

```
[deepseek2024coder] Guo(2024) "DeepSeek-Coder: When the Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ — architecture family
  引用位置: [method.tex:32] ✓ — model reference
  问题: 无
```

```
[ding2024traced] Ding(2024) "TRACED: Execution-aware Pre-training for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ — traces for code LLMs
  引用位置: [related_work.tex:16] ✓ — execution-aware pretraining for vulnerability detection
  问题: 无
```

```
[eguchi2025etcot] Eguchi(2025) "Making LLMs Program Interpreters via..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:7] ✓ — ET-CoT trace chain-of-thought
  问题: 无
```

```
[ferrando2025execute] Armengol-Estapé(2025) "What I Cannot Execute, I..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:7] ✓ — compact traces comparable to full traces
  问题: ⚠ bib key "ferrando2025" 与第一作者 Armengol-Estapé 不匹配（cosmetic，不影响编译）
```

```
[foster2025mutation] Foster(2025) "Mutation-Guided LLM-based Test Generation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:18] ⚠ — 文中称其 demonstrated "structured fault signals...improve localization"，但该论文是关于 test generation，不是 fault localization
  问题: ⚠ MISATTRIBUTION — Foster et al. 的工作是 mutation-guided test generation，不是 fault localization
```

```
[geng2024calibration] Geng(2024) "A Survey of Confidence Estimation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:48] ✓ — LLM calibration survey
  问题: 无
```

```
[gu2024cruxeval] Gu(2024) "CRUXEval: A Benchmark for Code..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:8] ✓ — execution reasoning benchmark
  引用位置: [method.tex:7] ✓ — output prediction
  问题: 无
```

```
[guo2017calibration] Guo(2017) "On Calibration of Modern Neural..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:48] ✓ — neural network calibration
  问题: 无
```

```
[haque2025traces] Haque(2025) "Towards Effectively Leveraging Execution..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✗  arXiv: ✓
  引用位置: [related_work.tex:10] ✓ — raw traces limited repair benefit
  问题: ✗ Venue 错误 — bib 写 "KnowledgeNLP Workshop at ACL 2025"，实际是 NAACL 2025 的 workshop
```

```
[hoang2019deepjit] Hoang(2019) "DeepJIT: An End-to-End Deep Learning..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓ — JIT defect prediction
  问题: 无
```

```
[hoang2020cc2vec] Hoang(2020) "CC2Vec: Distributed Representations of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — code change representation
  问题: 无
```

```
[hu2022lora] Hu(2022) "LoRA: Low-Rank Adaptation of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [method.tex:33] ✓ — LoRA
  引用位置: [appendix.tex:38] ✓ — LoRA
  问题: 无
```

```
[huang2026tracecoder] Huang(2026) "TraceCoder: A Trace-Driven Multi-Agent..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓ — selective trace extraction for debugging
  问题: 无
```

```
[jiang2023llmlingua] Jiang(2023) "LLMLingua: Compressing Prompts for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:10] ✓ — prompt compression
  引用位置: [discussion.tex:66] ✓ — prompt compression
  问题: 无
```

```
[jimenez2024swebench] Jimenez(2024) "SWE-bench: Can Language Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓ — SWE-bench ecosystem
  问题: ⚠ 标题大小写细微差异 "Real-World GitHub" vs ICLR 官方 "Real-world Github"（minor）
```

```
[jones2002visualization] Jones(2002) "Visualization of Test Information to..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL
  问题: 无
```

```
[kadavath2022language] Kadavath(2022) "Language Models (Mostly) Know What..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:48] ✓ — LLM calibration
  问题: 无
```

```
[kamei2013large] Kamei(2013) "A Large-Scale Empirical Study of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓ — JIT quality assurance
  问题: 无
```

```
[kang2024autofl] Kang(2024) "A Quantitative and Qualitative Evaluation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:19] ✓ — AutoFL LLM-based fault localization
  问题: ⚠ Venue 严格来说是 PACMSE (FSE issue)，但学界普遍简写 FSE 2024，可接受
```

```
[li2023selectivecontext] Li(2023) "Compressing Context to Enhance Inference..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:10] ✓ — Selective Context prompt compression
  引用位置: [discussion.tex:66] ✓ — prompt compression
  问题: 无
```

```
[liu2023codeexecution] Liu(2023) "Code Execution with Pre-trained Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:5] ✓ — pre-trained models predict execution outputs
  问题: 无
```

```
[ni2024next] Ni(2024) "NExT: Teaching Large Language Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ — traces for code LLMs
  引用位置: [related_work.tex:7] ✓ — NExT trace chain-of-thought
  问题: 无
```

```
[papadakis2019mutation] Papadakis(2019) "Mutation Testing Advances: An Analysis..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:18] ✓ — equivalent-mutant problem
  问题: 无
```

```
[pornprasit2021jitline] Pornprasit(2021) "JITLine: A Simpler, Better, Faster..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓ — JIT defect prediction
  问题: 无
```

```
[qin2024agentfl] Qin(2024) "AgentFL: Scaling LLM-based Fault..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ⚠  arXiv: ✓
  引用位置: [related_work.tex:19] ✓ — AgentFL LLM-based fault localization
  问题: ⚠ Venue 标注 "ASE 2024" 未通过搜索确认正式收录，可能仅为 arXiv preprint，需核实
```

```
[qwen2025coder] Qwen Team(2024) "Qwen2.5-Coder Technical Report..."
  存在: ✓  作者: ⚠  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ — Qwen model family
  引用位置: [method.tex:32] ✓ — Qwen-2.5-Coder
  问题: ⚠ (1) bib key 写 "2025" 但 year=2024；(2) 作者 "Qwen Team" 应列出具名作者（arXiv 有 24 位）
```

```
[roziere2024code] Rozière(2023) "Code Llama: Open Foundation Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [introduction.tex:14] ✓ — CodeLlama architecture family
  引用位置: [method.tex:32] ✓ — CodeLlama-13B
  问题: ⚠ bib key 写 "2024" 但 year=2023（cosmetic）
```

```
[sachdeva2024dataefficient] Sachdeva(2024) "How to Train Data-Efficient LLMs..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:51] ✓ — data selection methods
  问题: 无
```

```
[shi2023distracted] Shi(2023) "Large Language Models Can Be Easily..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:9] ✓ — LLMs distracted by irrelevant context
  问题: 无
```

```
[shinn2023reflexion] Shinn(2023) "Reflexion: Language Agents with Verbal..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓ — iteratively refine code using execution outcomes
  问题: 无
```

```
[spiess2025calibration] Spiess(2025) "Calibration and Correctness of Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓ — calibration for code models
  引用位置: [appendix.tex:547] ✓ — calibration for code models
  问题: 无
```

```
[steenhoek2024deepdfa] Steenhoek(2024) "Dataflow Analysis-Inspired Deep Learning..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:16] ✓ — DeepDFA for defect detection
  问题: 无
```

```
[swayamdipta2020cartography] Swayamdipta(2020) "Dataset Cartography: Mapping and Diagnosing..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓ — dataset cartography via training dynamics
  问题: 无
```

```
[tian2020patchcorrectness] Tian(2020) "Evaluating Representation Learning of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — change representations for repair correctness
  问题: 无
```

```
[tian2024debugbench] Tian(2024) "DebugBench: Evaluating Debugging Capability..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [experiments.tex:126] ✓ — DebugBench cross-dataset generalization
  引用位置: [appendix.tex:617] ✓ — DebugBench
  问题: 无
```

```
[wang2025dcsh] Wang(2025) "Do Code Semantics Help? A Comprehensive..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ — traces for code LLMs
  引用位置: [introduction.tex:12] ✓ — no single trace representation consistently outperforms
  引用位置: [related_work.tex:6] ✓ — trace utility task/format-dependent
  问题: 无
```

```
[wang2025inspectcoder] Wang(2025) "InspectCoder: Dynamic Analysis-Enabled Self..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓ — selective trace extraction for debugging
  问题: 无
```

```
[wang2025openhands] Wang(2025) "OpenHands: An Open Platform for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓ — agent-based repair with execution feedback
  问题: 无
```

```
[widyasari2024fusefl] Widyasari(2024) "Demystifying Faulty Code: Step-by-Step..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:18] ✓ — FuseFL structured fault signals（确认 FuseFL 是该论文方法名）
  问题: 无
```

```
[wong2014dstar] Wong(2014) "Software Fault Localization Using DStar..."
  存在: ✗  作者: ✓  年份: ✓  标题: ✗  Venue: ✗  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL DStar（引用上下文正确）
  问题: ✗✗✗ 严重错误 — bib 条目混合了两个不同版本：
    - 标题 "Software Fault Localization Using DStar (D*)" 是 SERE 2012 会议版
    - Venue "Journal of Systems and Software, vol 91, pages 44-58" 错误，实际该论文的期刊版是：
      Title: "The DStar Method for Effective Software Fault Localization"
      Venue: IEEE Transactions on Reliability, vol 63, no 1, pages 290-308, 2014
      DOI: 10.1109/TR.2013.2285319
    - bib 中 DOI 10.1016/j.jss.2013.12.020 不对应此论文
```

```
[xia2024agentless] Xia(2024) "Agentless: Demystifying LLM-based..."
  存在: ✓  作者: ✓  年份: ⚠  标题: ⚠  Venue: ⚠  arXiv: ✓
  引用位置: [related_work.tex:20] ✓ — Agentless repair
  问题: ⚠ 已正式发表于 FSE 2025 (PACMSE 2(FSE):801-824)，bib 仍标注为 arXiv preprint 2024。
    建议更新 venue、year、title（正式版标题去掉了 "Agentless:" 前缀）
```

```
[xie2023doremi] Xie(2023) "DoReMi: Optimizing Data Mixtures..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:51] ✓ — data selection methods
  问题: 无
```

```
[xu2025cruxevalx] Xu(2025) "CRUXEval-X: A Benchmark for Multilingual..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:8] ✓ — CRUXEval extended to 19 languages
  问题: 无
```

```
[yadavally2024slicing] Yadavally(2024) "A Learning-Based Approach to Static..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:16] ✓ — learned program slicing
  问题: 无
```

```
[yang2024generalization] Yang(2024) "Unveiling the Generalization Power of..."
  存在: ✓  作者: ⚠  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:52] ✓ — fine-tuned LLMs generalize on concise inputs
  引用位置: [appendix.tex:655] ✓ — generalization
  问题: ⚠ 作者 "Pheng Ann Heng" 应为 "Pheng-Ann Heng"（带连字符，ACL Anthology 官方写法）
```

```
[yang2024sweagent] Yang(2024) "SWE-agent: Agent-Computer Interfaces Enable..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓ — SWE-agent repair with execution feedback
  问题: 无
```

```
[zhong2024ldb] Zhong(2024) "LDB: A Large Language Model Debugger..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓ — LDB segment-level trace verification
  问题: ✗ 标题错误 — ACL Anthology 官方标题为 "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"，不是 "LDB: ..."
```

```
[zhou2024llm4patch] Zhou(2024) "Leveraging Large Language Model for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — LLM4PatchCorrect (84.4%)
  问题: 无
```

---

## 汇总

**总计：57 条**

**需修正问题：9 条**

| # | Key | 问题类型 | 严重程度 | 说明 |
|---|-----|---------|---------|------|
| 1 | `wong2014dstar` | 标题/Venue/DOI 全错 | **严重** | 标题、venue、pages、DOI 全部混淆。应改为：Title "The DStar Method for Effective Software Fault Localization", Venue "IEEE Transactions on Reliability", vol 63, no 1, pp 290-308, DOI 10.1109/TR.2013.2285319 |
| 2 | `zhong2024ldb` | 标题错误 | **中** | 正式标题是 "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"，非 "LDB: ..." |
| 3 | `haque2025traces` | Venue 错误 | **中** | "KnowledgeNLP Workshop at ACL 2025" → 应为 "NAACL 2025" |
| 4 | `foster2025mutation` | MISATTRIBUTION | **中** | related_work.tex:18 称其 demonstrated "improve localization"，实际是 test generation |
| 5 | `xia2024agentless` | Venue 过时 | **低-中** | 已发表于 FSE 2025，仍标注 arXiv 2024 |
| 6 | `qin2024agentfl` | Venue 未确认 | **低-中** | "ASE 2024" 未通过检索确认正式收录 |
| 7 | `yang2024generalization` | 作者拼写 | **低** | "Pheng Ann Heng" → "Pheng-Ann Heng" |
| 8 | `qwen2025coder` | Key/作者不规范 | **低** | bib key "2025" vs year=2024；作者应列具名 |
| 9 | `ferrando2025execute` | Key 不匹配 | **低** | bib key "ferrando" 不是第一作者 |

**无问题：48 条**（全部通过 6 项检查且引用上下文正确）

---
