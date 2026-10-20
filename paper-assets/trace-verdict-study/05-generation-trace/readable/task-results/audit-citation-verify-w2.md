# audit citation verify w2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation-verify-w2_20260526T101532_result.json`
- **Structured JSON:** [`00a614868c5757fda5eb.json`](../../sessions/00/00a614868c5757fda5eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 组验证完成。汇总报告如下：

---

## 引用验证报告（Worker 2/3）

### 逐条验证结果

```
[abreu2007accuracy] Abreu(2007) "On the Accuracy of Spectrum-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓ — SBFL 基础工作
  问题: 格式小问题：应用 booktitle= 而非 journal=（这是会议论文）

[appt2024] Zhang(2024) "APPT: Boosting Automated Patch Correctness..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓ — 79.7% 准确率与论文报告一致
  问题: 无

[austin2021program] Austin(2021) "Program Synthesis with Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:13] ✓ — MBPP 来源正确
  问题: 无

[barr2015oracle] Barr(2015) "The Oracle Problem in Software Testing..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:15] ✓ — 正确引用 test oracle 综述
  问题: 无

[bengio2009curriculum] Bengio(2009) "Curriculum Learning"
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓
  问题: 无

[bouzenia2025repairagent] Bouzenia(2025) "RepairAgent: An Autonomous, LLM-Based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓
  问题: 无

[chen2021evaluating] Chen(2021) "Evaluating Large Language Models Trained..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:13] ✓ — HumanEval 来源正确
  问题: 无

[chen2024selfdebug] Chen(2024) "Teaching Large Language Models to Self-Debug"
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓
  问题: 无

[chen2025tracepile] Chen(2025) "Chain of Execution Supervision Promotes..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ [related_work.tex:5] ✓ [method.tex:7] ✓
  问题: 无

[deepseek2024coder] Guo(2024) "DeepSeek-Coder: When the Large Language..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:32] ✓
  问题: 无

[ding2024traced] Ding(2024) "TRACED: Execution-aware Pre-training..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ [related_work.tex:16] ✓
  问题: 作者 "Ben Steenhoek" 在 ACM 官方记录中为 "Benjamin Steenhoek"

[eguchi2025etcot] Eguchi(2025) "Making LLMs Program Interpreters via..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:7] ✓
  问题: 无

[ferrando2025execute] Armengol-Estapé(2025) "What I Cannot Execute, I..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:7] ✓
  问题: ⚠ bib key 含 "ferrando" 但无此姓作者（第一作者是 Armengol-Estapé）；
        作者名缺 accent："Estape" 应为 "Estap{\'e}"

[foster2025mutation] Foster(2025) "Mutation-Guided LLM-based Test Generation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:18] ✓
  问题: 无（venue 可补 "33rd" 但非错误）

[geng2024calibration] Geng(2024) "A Survey of Confidence Estimation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓
  问题: 无

[gu2024cruxeval] Gu(2024) "CRUXEval: A Benchmark for Code..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:8] ✓ [method.tex:7] ✓
  问题: 无

[guo2017calibration] Guo(2017) "On Calibration of Modern Neural..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:48] ✓
  问题: 无

[haque2025traces] Haque(2025) "Towards Effectively Leveraging Execution..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✗  arXiv: ✓
  引用位置: [related_work.tex:10] ✓
  问题: ⚠ Venue 错误：应为 "KnowledgeNLP Workshop at NAACL 2025"，非 "ACL 2025"

[hoang2019deepjit] Hoang(2019) "DeepJIT: An End-to-End Deep Learning..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓
  问题: 无

[hoang2020cc2vec] Hoang(2020) "CC2Vec: Distributed Representations of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓
  问题: 无

[hu2022lora] Hu(2022) "LoRA: Low-Rank Adaptation of Large..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [method.tex:33] ✓ [appendix.tex:38] ✓
  问题: 无

[huang2026tracecoder] Huang(2026) "TraceCoder: A Trace-Driven Multi-Agent..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓
  问题: 无

[jiang2023llmlingua] Jiang(2023) "LLMLingua: Compressing Prompts for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓ [discussion.tex:66] ✓
  问题: 无

[jimenez2024swebench] Jimenez(2024) "SWE-bench: Can Language Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:20] ✓
  问题: 标题大小写微小差异（"Real-World GitHub" vs proceedings 版 "Real-world Github"），非重大问题

[jones2002visualization] Jones(2002) "Visualization of Test Information..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:19] ✓
  问题: 无

[kadavath2022language] Kadavath(2022) "Language Models (Mostly) Know..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓
  问题: 无

[kamei2013large] Kamei(2013) "A Large-Scale Empirical Study..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓
  问题: 无

[kang2024autofl] Kang(2024) "A Quantitative and Qualitative Evaluation..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:19] ✓
  问题: 无

[li2023selectivecontext] Li(2023) "Compressing Context to Enhance..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:10] ✓ [discussion.tex:66] ✓
  问题: 无

[liu2023codeexecution] Liu(2023) "Code Execution with Pre-trained..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:5] ✓
  问题: 无

[ni2024next] Ni(2024) "NExT: Teaching Large Language Models..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4] ✓ [related_work.tex:7] ✓
  问题: 无

[papadakis2019mutation] Papadakis(2019) "Mutation Testing Advances: An..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:18] ✓
  问题: 无

[pornprasit2021jitline] Pornprasit(2021) "JITLine: A Simpler, Better..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:50] ✓
  问题: 无

[qin2024agentfl] Qin(2024) "AgentFL: Scaling LLM-based Fault..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✗  arXiv: ✓
  引用位置: [related_work.tex:19] ✓
  问题: ⚠ Venue 未确认为 ASE 2024——DBLP/ACM DL 搜不到该论文在 ASE 2024 的记录，可能仅为 arXiv 预印本

[qwen2025coder] Qwen Team(2024) "Qwen2.5-Coder Technical Report..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:32] ✓
  问题: bib key "qwen2025coder" 与 year={2024} 不一致（cosmetic）

[roziere2024code] Rozière(2023) "Code Llama: Open Foundation Models..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:14] ✓ [method.tex:32] ✓
  问题: ⚠ 作者列表中 "Rémi Lacroix" 可能不在该论文作者中（需二次确认，26 位作者的长列表）

[sachdeva2024dataefficient] Sachdeva(2024) "How to Train Data-Efficient..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:51] ✓
  问题: 无

[shi2023distracted] Shi(2023) "Large Language Models Can Be Easily..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:9] ✓
  问题: 无

[shinn2023reflexion] Shinn(2023) "Reflexion: Language Agents with..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓
  问题: 无

[spiess2025calibration] Spiess(2025) "Calibration and Correctness of..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:48] ✓ [appendix.tex:546] ✓
  问题: "and others" 不是标准 BibTeX 用法；应列出全部 9 位作者

[steenhoek2024deepdfa] Steenhoek(2024) "Dataflow Analysis-Inspired Deep..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:16] ✓
  问题: 无

[swayamdipta2020cartography] Swayamdipta(2020) "Dataset Cartography: Mapping and..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:51] ✓
  问题: 无

[tian2020patchcorrectness] Tian(2020) "Evaluating Representation Learning of..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓
  问题: 无

[tian2024debugbench] Tian(2024) "DebugBench: Evaluating Debugging..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [experiments.tex:126] ✓ [appendix.tex:616] ✓
  问题: 无

[wang2025dcsh] Wang(2025) "Do Code Semantics Help? A..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [introduction.tex:4,12] ✓ [related_work.tex:6] ✓
  问题: 无

[wang2025inspectcoder] Wang(2025) "InspectCoder: Dynamic Analysis-Enabled..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:10] ✓
  问题: 无

[wang2025openhands] Wang(2025) "OpenHands: An Open Platform for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓
  问题: 无

[widyasari2024fusefl] Widyasari(2024) "Demystifying Faulty Code: Step-by-Step..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:18] ✓
  问题: ⚠ 标题缺 "with LLM"——应为 "Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization"

[wong2014dstar] Wong(2014) "Software Fault Localization Using DStar..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✗  arXiv: N/A
  引用位置: [related_work.tex:19] ✓
  问题: ✗✗ 严重错误——
    (1) Venue 错：bib 写 "Journal of Systems and Software"，实际 2014 期刊版发表在 IEEE Transactions on Reliability (Vol.63, No.1, pp.290-308)
    (2) 标题错：2014 期刊版标题为 "The DStar Method for Effective Software Fault Localization"
    (3) Volume/pages 错：bib 写 vol.91 pp.44-58，应为 vol.63 pp.290-308
    (4) DOI 错：10.1016/j.jss.2013.12.020 指向无关论文，正确 DOI 为 10.1109/TR.2013.2285319

[xia2024agentless] Xia(2024) "Agentless: Demystifying LLM-based..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓
  问题: 已正式发表于 FSE 2025，建议更新 venue（当前 arXiv 标注不算错）

[xie2023doremi] Xie(2023) "DoReMi: Optimizing Data Mixtures..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:51] ✓
  问题: 无

[xu2025cruxevalx] Xu(2025) "CRUXEval-X: A Benchmark for Multilingual..."
  存在: ✓  作者: ✗  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:8] ✓
  问题: "and others" 应展开为完整作者列表（共 9 位作者）

[yadavally2024slicing] Yadavally(2024) "A Learning-Based Approach to Static..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:16] ✓
  问题: 无

[yang2024generalization] Yang(2024) "Unveiling the Generalization Power..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:52] ✓ [appendix.tex:655] ✓
  问题: 无

[yang2024sweagent] Yang(2024) "SWE-agent: Agent-Computer Interfaces..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: ✓
  引用位置: [related_work.tex:20] ✓
  问题: 无

[zhong2024ldb] Zhong(2024) "LDB: A Large Language Model Debugger..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✗  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:21] ✓
  问题: ⚠ 正式发表版标题为 "Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step by Step"，bib 中用了旧标题 "LDB: ..."

[zhou2024llm4patch] Zhou(2024) "Leveraging Large Language Model for..."
  存在: ✓  作者: ✓  年份: ✓  标题: ✓  Venue: ✓  arXiv: N/A
  引用位置: [related_work.tex:17] ✓
  问题: 无
```

---

### 汇总

**总计：57 条**
**幻觉引用（HALLUCINATED）：0 条** — 全部论文真实存在
**错误引用（MISATTRIBUTION）：0 条** — 所有引用上下文使用正确

**问题数：10 条**

| 严重程度 | Key | 问题类型 | 说明 |
|---------|-----|---------|------|
| **严重** | `wong2014dstar` | Venue/标题/DOI/页码全错 | venue 应为 IEEE Trans. Reliability，标题/vol/pages/DOI 均不对 |
| **中** | `haque2025traces` | Venue 错误 | "ACL 2025" 应为 "NAACL 2025" |
| **中** | `qin2024agentfl` | Venue 未确认 | 未在 ASE 2024 proceedings 中找到，可能仅为 arXiv 预印本 |
| **中** | `widyasari2024fusefl` | 标题不完整 | 缺 "with LLM" |
| **中** | `zhong2024ldb` | 标题过时 | 正式版标题以 "Debug like a Human:" 开头 |
| **低** | `ferrando2025execute` | bib key 不匹配 + 作者缺 accent | key 含 "ferrando" 但无此姓作者；"Estape" 缺 accent |
| **低** | `ding2024traced` | 作者名 | "Ben" 应为 "Benjamin" Steenhoek |
| **低** | `spiess2025calibration` | 作者不完整 | "and others" 非标准 BibTeX，应列全部 9 人 |
| **低** | `xu2025cruxevalx` | 作者不完整 | "and others" 应展开为全部 9 位作者 |
| **低** | `roziere2024code` | 作者存疑 | "Rémi Lacroix" 可能不在 Code Llama 作者列表中（需二次确认） |

---
