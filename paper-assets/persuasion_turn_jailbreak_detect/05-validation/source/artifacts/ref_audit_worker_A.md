# 引用验证报告 — Worker A

## 统计
- 总 .bib 条目数: 91
- 验证通过: 63
- 发现问题: 10 (cited entries with errors) + 5 (uncited entries with errors)
- 未被正文引用: 18
- 疑似重复: 2 对

---

## 一、被引用条目中的错误（需修复）

### ren2024actorattack ✗✗✗ [CRITICAL — 正文高频引用]
- **问题 1 — 标题伪造**: Bib 写 "ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory"，但论文实际标题是 **"Derail Yourself: Multi-turn LLM Jailbreak Attack through Self-discovered Clues"**（arXiv v1）或 **"LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts"**（arXiv v2 / ACL 2025 版本）。"ActorAttack" 只是方法名，不是论文标题。
- **问题 2 — Venue 错误**: Bib 写 ICLR 2025，但论文已从 ICLR 2025 撤稿，修改后被 **ACL 2025** 接收。
- **问题 3 — 缺少 arXiv ID**: 应为 2410.10700。
- **引用位置**: introduction.tex (line 5, 16), related_work.tex (line 6), experiments.tex (line 42, 155), conclusion.tex (line 11)
- **来源**: [arXiv 2410.10700](https://arxiv.org/abs/2410.10700), [GitHub](https://github.com/renqibing/ActorAttack)

### robey2024smoothllm ✗✗ [CRITICAL — Venue 错误]
- **问题 — Venue 错误**: Bib 写 "Proceedings of the 41st International Conference on Machine Learning" (ICML 2024)，但 SmoothLLM **不在 ICML 2024 proceedings 中**。该论文是 arXiv preprint (2310.03684)，后发表于 **TMLR 2025**。
- **引用位置**: related_work.tex (line 9)
- **来源**: [arXiv 2310.03684](https://arxiv.org/abs/2310.03684), [Semantic Scholar](https://www.semanticscholar.org/paper/SmoothLLM-Robey-Wong/8cf9b49698fdb1b754df2556576412a7b44929f6)

### mehrotra2024tap ✗✗ [CRITICAL — 标题错误]
- **问题 — 副标题伪造**: Bib 写 "Tree of Attacks: Jailbreaking Black-Box LLMs **with the Pruning of Candidate Outputs**"，但 NeurIPS 2024 正式标题是 **"Tree of Attacks: Jailbreaking Black-Box LLMs Automatically"**。副标题 "with the Pruning of Candidate Outputs" 是伪造的。
- **引用位置**: related_work.tex (line 6)
- **来源**: [NeurIPS 2024 Poster](https://neurips.cc/virtual/2024/poster/95078), [arXiv 2312.02119](https://arxiv.org/abs/2312.02119)

### jiang2024redqueen ✗✗ [CRITICAL — 标题/年份/Venue 全错]
- **问题 1 — 标题错误**: Bib 用 arXiv v1 标题 "RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking"，但已发表的版本标题改为 **"Red Queen: Exposing Latent Multi-Turn Risks in Large Language Models"**。
- **问题 2 — 年份错误**: Bib 写 2024，应为 **2025**（ACL 2025 Findings, pp 25554-25591）。
- **问题 3 — Venue 缺失**: Bib 只写 arXiv preprint，但已发表于 **Findings of ACL 2025**。
- **引用位置**: related_work.tex (line 6)
- **来源**: [ACL Anthology 2025.findings-acl.1311](https://aclanthology.org/2025.findings-acl.1311/), [arXiv 2409.17458](https://arxiv.org/abs/2409.17458)

### metallamaguard3_2024 ✗ [MODERATE — 无独立论文]
- **问题**: 不存在标题为 "Llama Guard 3" 的独立论文。Llama Guard 3 是在 "The Llama 3 Herd of Models"（arXiv 2407.21783, Grattafiori et al.）中介绍的，或以 model card 形式存在于 HuggingFace。
- **建议**: 改为引用 Llama 3 Herd 论文，或添加 HuggingFace model card URL。
- **引用位置**: related_work.tex (line 9), experiments.tex (line 50)
- **来源**: [HuggingFace Model Card](https://huggingface.co/meta-llama/Llama-Guard-3-8B), [arXiv 2407.21783](https://arxiv.org/abs/2407.21783)

### gguard2025 ✗ [MODERATE — 标题已更新]
- **问题**: Bib 标题 "An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs" 是 arXiv v1 版本，当前 v2 标题已改为 **"Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak"**。
- **引用位置**: introduction.tex (line 7), related_work.tex (line 9)
- **来源**: [arXiv 2507.07146](https://arxiv.org/abs/2507.07146)

### lu2025xboundary ✗ [MODERATE — 标题已更新]
- **问题**: Bib 标题写 "...Shield LLMs from **Multi-Turn Jailbreaks** without Compromising Usability"，但 ACL Anthology 发表版标题改为 "...Shield LLMs from **Jailbreak Attacks** without Compromising Usability"。
- **引用位置**: related_work.tex (line 9)
- **来源**: [ACL Anthology 2025.findings-emnlp.282](https://aclanthology.org/2025.findings-emnlp.282/)

### song2026multibreak ✗ [MODERATE — 标题/Venue 待确认]
- **问题 1**: Bib 副标题写 "for Evaluating LLM Safety"，但 OpenReview 提交版标题为 "for **Stress-testing** LLM Safety"。
- **问题 2**: Bib 声称 ICML 2026，但截至 2026 年 5 月，该论文仍在 review 中，**接收尚未公开确认**。
- **引用位置**: related_work.tex (line 6)
- **来源**: [arXiv 2605.01687](https://arxiv.org/abs/2605.01687), [OpenReview](https://openreview.net/forum?id=uJgfj5EJ2W)

### chao2024jailbreakbench ✗ [MODERATE — Venue 不完整]
- **问题**: Bib 只列为 arXiv preprint，但该论文已被 **NeurIPS 2024 Datasets and Benchmarks Track** 接收。应更新 venue。
- **引用位置**: related_work.tex (line 6)
- **来源**: [NeurIPS 2024 Proceedings](https://papers.nips.cc/paper_files/paper/2024/hash/63092d79154adebd7305dfd498cbff70-Abstract-Datasets_and_Benchmarks_Track.html)

### conneau2018probing ✗ [MINOR — 标题细节]
- **问题**: Bib 标题写 `What you can cram into a single \$\&!\#* vector`，完整准确标题应保留 grawlix 符号。实际 ACL Anthology 标题为 "What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties"。Bib 中的 LaTeX 转义是合理的近似。
- **引用位置**: related_work.tex (line 15)
- **来源**: [ACL Anthology P18-1198](https://aclanthology.org/P18-1198/)

---

## 二、未被引用条目中的错误

### marchiori2025jdapt ✗✗✗ [UNCITED — 作者和标题错误]
- **作者错误**: Bib 写 "Marchiori, Andrea"，实际第一作者是 **Francesco Marchiori**。
- **标题错误**: Bib 写 "J-DAPT: CORAL-Based Domain Adaptation with Cross-Modal Fusion for Multimodal Robotic Jailbreak Detection"，实际标题是 **"Preventing Robotic Jailbreaking via Multimodal Domain Adaptation"**。J-DAPT 是方法名，不是论文标题。
- **来源**: [arXiv 2509.23281](https://arxiv.org/abs/2509.23281)

### wang2026trajguard ✗✗✗ [UNCITED — 作者和标题完全错误]
- **作者错误**: Bib 写 "Wang, Yifan and others"，实际作者是 **Cheng Liu, Xiaolei Liu, Xingyu Li, Bangzhou Xin, Kangyi Ding**，无 "Wang Yifan"。
- **标题错误**: Bib 写 "TrajGuard: Trajectory-Based Hidden-State Detection of Multi-Turn Jailbreak Attacks"，实际标题是 **"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense"**。
- **来源**: [arXiv 2604.07727](https://arxiv.org/abs/2604.07727)

### li2025m2s ✗✗✗ [UNCITED — 作者和标题完全错误]
- **作者错误**: Bib 写 "Li, Minxuan et al."，实际作者是 **Junwoo Ha, Hyunjun Kim, Sangyoon Yu, Haon Park, Ashkan Yousefpour, Yuna Park, Suhyun Kim**，无 "Li Minxuan"。
- **标题错误**: Bib 写 "M2S: Multi-Turn to Single-Turn -- Converting Multi-Turn Jailbreak Attacks to Single-Turn for Enhanced Safety Guardrails"，实际标题是 **"M2S: Multi-turn to Single-turn jailbreak in Red Teaming for LLMs"**。
- **来源**: [arXiv 2503.04856](https://arxiv.org/abs/2503.04856), [ACL Anthology](https://aclanthology.org/2025.acl-long.805/)

### hsu2024improved ✗✗✗ [UNCITED — 作者伪造，重复条目]
- **作者伪造**: Bib 写 "Hsu, Erick and Hsu, Ikuya and Chung, Paul"，实际作者是 **Erick Galinkin and Martin Sablotny** (NVIDIA)。完全不同的人。
- **标题略错**: "Improved LLM Jailbreak Detection" vs 实际 "Improved **Large Language Model** Jailbreak Detection"。
- **与 galinkin2024improved 重复**: 同一 arXiv ID 2412.01547。
- **来源**: [arXiv 2412.01547](https://arxiv.org/abs/2412.01547)

### phute2023selfdefense ✗✗ [UNCITED — 5/7 作者名错误]
- **作者错误**: Bib 写 "Helber, Alec"，实际为 **Helbling, Alec**；Bib 写 "Peng, ShiNung"，实际为 **Peng, ShengYun**；Bib 写 "Szyber, Sebastian"，实际为 **Szyller, Sebastian**；Bib 写 "Caliskan, Aylin"，实际为 **Cornelius, Cory**；Bib 写 "Khashabi, Daniel"，实际为 **Chau, Duen Horng**。
- **来源**: [arXiv 2308.07308](https://arxiv.org/abs/2308.07308)

---

## 三、疑似重复

### shen2025antidote vs shen2024jailbreakantidote — 确认重复
- 同一论文：arXiv 2410.02298，同一标题 "Jailbreak Antidote"，同一作者 (Shen, Zhao, Dong, He, Zeng)，发表于 ICLR 2025。
- **shen2024jailbreakantidote** 被正文引用（related_work.tex），**shen2025antidote** 未被引用。
- **建议**: 删除 shen2025antidote，保留 shen2024jailbreakantidote（并考虑更新 year 为 2025 以匹配 ICLR 2025 发表年份）。

### hsu2024improved vs galinkin2024improved — 确认重复（且 hsu 版作者伪造）
- 同一论文：arXiv 2412.01547。
- **galinkin2024improved** 作者正确 (Galinkin, Sablotny)，**hsu2024improved** 作者完全错误 (Hsu, Hsu, Chung)。
- 两者均未被正文引用。
- **建议**: 删除 hsu2024improved。如需引用该论文，使用 galinkin2024improved。

---

## 四、未被正文引用的 .bib 条目（18 条）

以下条目存在于 references.bib 中但未在任何 .tex 文件中被 `\cite`/`\citep`/`\citet` 引用：

| # | cite_key | 论文存在性 | 备注 |
|---|----------|-----------|------|
| 1 | he2021deberta | ✓ 存在 | DeBERTa v1; v3 (he2023debertav3) 已被引用 |
| 2 | zou2023gcg | ✓ 存在 | GCG attack paper |
| 3 | devlin2019bert | ✓ 存在 | BERT 原始论文 |
| 4 | chen2020simclr | ✓ 存在 | SimCLR |
| 5 | grill2020byol | ✓ 存在 | BYOL |
| 6 | marchiori2025jdapt | ✗ 作者/标题错误 | 见上方错误分析 |
| 7 | wang2026trajguard | ✗ 作者/标题错误 | 见上方错误分析 |
| 8 | templeton2024saemitigators | ✓ 存在 | Scaling Monosemanticity |
| 9 | alon2023perplexity | ✓ 存在 | Perplexity-based detection |
| 10 | phute2023selfdefense | ✗ 作者名错误 | 见上方错误分析 |
| 11 | nian2025jaildam | ✓ 存在 | JailDAM, COLM 2025 |
| 12 | anil2024manyshot | ✓ 存在 | Many-shot Jailbreaking, NeurIPS 2024 |
| 13 | jain2023baseline | ✓ 存在 | Baseline Defenses |
| 14 | shen2025antidote | ✓ 存在但重复 | 与 shen2024jailbreakantidote 重复 |
| 15 | hsu2024improved | ✗ 作者伪造+重复 | 与 galinkin2024improved 重复 |
| 16 | li2025m2s | ✗ 作者/标题错误 | 见上方错误分析 |
| 17 | li2025repejailbreak | ✓ 存在 | COLING 2025 |
| 18 | galinkin2024improved | ✓ 存在 | 与 hsu2024improved 重复 |

---

## 五、验证通过的条目（逐条）

以下 73 条经 WebSearch 验证，元数据无误（或仅有不影响正确性的细节说明）：

### inan2023llamaguard ✓
- 作者: ✓ (Inan et al.)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv: ✓ (2312.06674)
- 来源: [arXiv](https://arxiv.org/abs/2312.06674)

### zeng2024shieldgemma ✓
- 作者: ✓ (Zeng, Wenjun et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (arXiv preprint)
- arXiv: ✓ (2407.21772)
- 来源: [arXiv](https://arxiv.org/abs/2407.21772)

### han2024wildguard ✓
- 作者: ✓ (Han, Seungju et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (NeurIPS 2024)
- 来源: [NeurIPS 2024](https://neurips.cc/virtual/2024/poster/97764)

### anthropic2025constitutional ✓
- 作者: ✓ (Sharma, Mrinank et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2501.18837)
- 来源: [arXiv](https://arxiv.org/abs/2501.18837)

### deepcontext2026 ✓
- 作者: ✓ (Albrethsen et al.)
- 年份: ✓ (2026)
- 标题: ✓
- arXiv: ✓ (2602.16935)
- 来源: [arXiv](https://arxiv.org/abs/2602.16935)

### tong2025biid ✓
- 作者: ✓ (Tong, Haibo et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2509.22732)
- 来源: [arXiv](https://arxiv.org/abs/2509.22732)

### safedream2026 ✓
- 作者: ✓ (Yan, Bo et al.)
- 年份: ✓ (2026)
- 标题: ✓
- arXiv: ✓ (2604.16824)
- 来源: [arXiv](https://arxiv.org/abs/2604.16824)

### bullwinkel2025repeng ✓
- 作者: ✓ (Bullwinkel, Blake et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2507.02956)
- 来源: [arXiv](https://arxiv.org/abs/2507.02956)

### mann1988rst ✓
- 作者: ✓ (Mann & Thompson)
- 年份: ✓ (1988)
- 标题: ✓
- Venue: ✓ (Text & Talk, vol 8(3), pp 243-281)
- 来源: [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/text.1.1988.8.3.243/html)

### prasad2008pdtb ✓
- 作者: ✓ (Prasad, Rashmi et al.)
- 年份: ✓ (2008)
- 标题: ✓
- Venue: ✓ (LREC 2008)
- 来源: [ACL Anthology](https://aclanthology.org/L08-1093/)

### stolcke2000dialogueact ✓
- 作者: ✓ (Stolcke, Andreas et al.)
- 年份: ✓ (2000)
- 标题: ✓
- Venue: ✓ (Computational Linguistics, vol 26(3), pp 339-374)
- 来源: [ACL Anthology](https://aclanthology.org/J00-3003/)

### austin1962speechacts ✓
- 作者: ✓ (Austin, J. L.)
- 年份: ✓ (1962)
- 标题: ✓
- Venue: ✓ (Harvard University Press)
- 来源: [Harvard University Press](https://www.hup.harvard.edu/books/9780674411524)

### searle1969speechacts ✓
- 作者: ✓ (Searle, J. R.)
- 年份: ✓ (1969)
- 标题: ✓
- Venue: ✓ (Cambridge University Press)
- 来源: [Cambridge University Press](https://www.cambridge.org/core/books/speech-acts/D2D7B03E472C8A390ED60B86E08640E7)

### cialdini2001influence ✓
- 作者: ✓ (Cialdini, Robert B.)
- 年份: ✓ (2001, 4th ed.)
- 标题: ✓
- Venue: ✓ (Allyn & Bacon)
- 来源: [Biblio](https://www.biblio.com/book/influence-science-practice-cialdini-robert-b/d/484235249)

### zeng2024pap ✓
- 作者: ✓ (Zeng, Yi et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ACL 2024)
- 来源: [ACL Anthology](https://aclanthology.org/2024.acl-long.773/)

### russinovich2024crescendo ✓
- 作者: ✓ (Russinovich, Salem, Eldan)
- 年份: ✓ (2025, USENIX Security)
- 标题: ✓
- arXiv: ✓ (2404.01833)
- 备注: cite key 写 2024（preprint 年份），year field 写 2025（发表年份），均合理
- 来源: [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/russinovich)

### chao2023pair ✓
- 作者: ✓ (Chao, Patrick et al.)
- 年份: ✓ (2025, IEEE SaTML)
- 标题: ✓
- arXiv: ✓ (2310.08419)
- 备注: cite key 写 2023（preprint），year 写 2025（发表），均合理
- 来源: [SaTML 2025](https://satml.org/2025/accepted-papers/)

### wei2023jailbroken ✓
- 作者: ✓ (Wei, Haghtalab, Steinhardt)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (NeurIPS 2023)
- 来源: [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html)

### hagendorff2026reasoning ✓
- 作者: ✓ (Hagendorff, Derner, Oliver)
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (Nature Communications, vol 17, 1435)
- DOI: ✓ (10.1038/s41467-026-69010-1)
- 来源: [Nature Communications](https://www.nature.com/articles/s41467-026-69010-1)

### fitd2024 ✓
- 作者: ✓ (Wang, Zhenhua et al.)
- 年份: ✓ (2024)
- 标题: ✓
- arXiv: ✓ (2402.15690)
- 来源: [arXiv](https://arxiv.org/abs/2402.15690)

### deceptivedelight2024 ✓
- 作者: ✓ (Palo Alto Networks Unit 42; 个人作者为 Jay Chen 和 Royce Lu)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (blog/tech report)
- 来源: [Unit 42 Blog](https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/)

### zou2023gcg ✓ [UNCITED]
- 作者: ✓ (Zou, Andy et al.)
- 年份: ✓ (2023)
- 标题: ✓
- arXiv: ✓ (2307.15043)
- 来源: [arXiv](https://arxiv.org/abs/2307.15043)

### lin2023toxicchat ✓
- 作者: ✓ (Lin, Zi et al.)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (EMNLP 2023 Findings, pp 4694-4702)
- 来源: [ACL Anthology](https://aclanthology.org/2023.findings-emnlp.311/)

### li2024mhj ✓
- 作者: ✓ (Li, Nathaniel et al.)
- 年份: ✓ (2024)
- 标题: ✓
- arXiv: ✓ (2408.15221)
- 来源: [arXiv](https://arxiv.org/abs/2408.15221)

### gururangan2018artifacts ✓
- 作者: ✓ (Gururangan, Suchin et al.)
- 年份: ✓ (2018)
- 标题: ✓
- Venue: ✓ (NAACL 2018)
- 来源: [ACL Anthology](https://aclanthology.org/N18-2017/)

### niven2019probing ✓
- 作者: ✓ (Niven, Timothy and Kao, Hung-Yu)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (ACL 2019)
- 来源: [ACL Anthology](https://aclanthology.org/P19-1459/)

### nasr2025attackermovessecond ✓
- 作者: ✓ (Nasr, Milad et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2510.09023)
- 来源: [arXiv](https://arxiv.org/abs/2510.09023)

### andriushchenko2024adaptive ✓
- 作者: ✓ (Andriushchenko, Croce, Flammarion)
- 年份: ✓ (2025, ICLR)
- 标题: ✓
- Venue: ✓ (ICLR 2025)
- 来源: [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/63fa7efdd3bcf944a4bd6e0ff6a50041-Abstract-Conference.html)

### he2021deberta ✓ [UNCITED]
- 作者: ✓ (He, Pengcheng et al.)
- 年份: ✓ (2021)
- 标题: ✓
- Venue: ✓ (ICLR 2021)
- 来源: [OpenReview](https://openreview.net/forum?id=XPZIaotutsD)

### he2023debertav3 ✓
- 作者: ✓ (He, Gao, Chen)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (ICLR 2023)
- 来源: [ICLR 2023](https://iclr.cc/virtual/2023/poster/11295)

### kopf2023openassistant ✓
- 作者: ✓ (Köpf, Andreas et al.)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (NeurIPS 36)
- 来源: [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/949f0f8f32267d297c2d4e3ee10a2e7e-Abstract-Datasets_and_Benchmarks.html)

### kornblith2019cka ✓
- 作者: ✓ (Kornblith et al.)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (ICML 2019, pp 3519-3529)
- 来源: [PMLR](https://proceedings.mlr.press/v97/kornblith19a.html)

### qwen3_2025 ✓
- 作者: ✓ (Yang, An et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2505.09388)
- 来源: [arXiv](https://arxiv.org/abs/2505.09388)

### gururangan2020dontstop ✓
- 作者: ✓ (Gururangan, Suchin et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (ACL 2020, pp 8342-8360)
- 来源: [ACL Anthology](https://aclanthology.org/2020.acl-main.740/)

### caruana1997multitask ✓
- 作者: ✓ (Caruana, Rich)
- 年份: ✓ (1997)
- 标题: ✓
- Venue: ✓ (Machine Learning, vol 28(1), pp 41-75)
- 来源: [Springer](https://link.springer.com/article/10.1023/A:1007379606734)

### phang2018stilts ✓
- 作者: ✓ (Phang, Jason et al.)
- 年份: ✓ (2018)
- 标题: ✓
- arXiv: ✓ (1811.01088)
- 来源: [arXiv](https://arxiv.org/abs/1811.01088)

### liu2019mtdnn ✓
- 作者: ✓ (Liu, Xiaodong et al.)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (ACL 2019, pp 4487-4496)
- 来源: [ACL Anthology](https://aclanthology.org/P19-1441/)

### howard2018ulmfit ✓
- 作者: ✓ (Howard & Ruder)
- 年份: ✓ (2018)
- 标题: ✓
- Venue: ✓ (ACL 2018, pp 328-339)
- 来源: [ACL Anthology](https://aclanthology.org/P18-1031/)

### dasanmartino2020semeval ✓
- 作者: ✓ (Da San Martino et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (SemEval 2020, pp 1377-1414)
- 来源: [ACL Anthology](https://aclanthology.org/2020.semeval-1.186/)

### dasanmartino2019fine ✓
- 作者: ✓ (Da San Martino et al.)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (EMNLP 2019, pp 5636-5646)
- 来源: [ACL Anthology](https://aclanthology.org/D19-1565/)

### jin2020textfooler ✓
- 作者: ✓ (Jin, Di et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (AAAI 2020, vol 34, pp 8018-8025)
- 来源: [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/6311)

### li2020bertattack ✓
- 作者: ✓ (Li, Linyang et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (EMNLP 2020, pp 6193-6202)
- 来源: [ACL Anthology](https://aclanthology.org/2020.emnlp-main.500/)

### devlin2019bert ✓ [UNCITED]
- 作者: ✓ (Devlin et al.)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (NAACL 2019, pp 4171-4186)
- 来源: [ACL Anthology](https://aclanthology.org/N19-1423/)

### hewitt2019structural ✓
- 作者: ✓ (Hewitt & Manning)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (NAACL 2019, pp 4129-4138)
- 来源: [ACL Anthology](https://aclanthology.org/N19-1419/)

### liu2019roberta ✓
- 作者: ✓ (Liu, Yinhan et al.)
- 年份: ✓ (2019)
- 标题: ✓
- arXiv: ✓ (1907.11692)
- 来源: [arXiv](https://arxiv.org/abs/1907.11692)

### wang2019persuasion ✓
- 作者: ✓ (Wang, Xuewei et al.)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (ACL 2019, pp 5635-5649)
- 来源: [ACL Anthology](https://aclanthology.org/P19-1566/)

### mazeika2024harmbench ✓
- 作者: ✓ (Mazeika et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ICML 2024)
- 来源: [PMLR](https://proceedings.mlr.press/v235/mazeika24a.html)

### kadali2026trace ✓
- 作者: ✓ (Kadali & Papalexakis)
- 年份: ✓ (2026)
- 标题: ✓
- arXiv: ✓ (2602.11495)
- 来源: [arXiv](https://arxiv.org/abs/2602.11495)

### hua2026rcs ✓
- 作者: ✓ (Hua, Peichun et al.)
- 年份: ✓ (2026)
- 标题: ✓
- Venue: ✓ (ACL 2026)
- arXiv: ✓ (2512.12069)
- 来源: [arXiv](https://arxiv.org/abs/2512.12069)

### xie2024gradsafe ✓
- 作者: ✓ (Xie et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ACL 2024, pp 507-518)
- 来源: [ACL Anthology](https://aclanthology.org/2024.acl-long.30/)

### xu2024safedecoding ✓
- 作者: ✓ (Xu, Zhangchen et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (ACL 2024)
- 来源: [ACL Anthology](https://aclanthology.org/2024.acl-long.303/)

### zou2024circuitbreakers ✓
- 作者: ✓ (Zou, Andy et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (NeurIPS 2024)
- 来源: [NeurIPS 2024](https://neurips.cc/virtual/2024/poster/95761)

### zhang2025jbshield ✓
- 作者: ✓ (Zhang, Shenyi et al.)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (USENIX Security 2025)
- arXiv: ✓ (2502.07557)
- 来源: [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-shenyi)

### perez2022redteaming ✓
- 作者: ✓ (Perez, Ethan et al.)
- 年份: ✓ (2022)
- 标题: ✓
- Venue: ✓ (EMNLP 2022, pp 3419-3448)
- 来源: [ACL Anthology](https://aclanthology.org/2022.emnlp-main.225/)

### kulkarni2026latentadversarial ✓
- 作者: ✓ (Kulkarni, Prashant)
- 年份: ✓ (2026)
- 标题: ✓
- arXiv: ✓ (2604.28129)
- 来源: [arXiv](https://arxiv.org/abs/2604.28129)

### derya2026revisitingjbshield ✓
- 作者: ✓ (Derya & Sunar)
- 年份: ✓ (2026)
- 标题: ✓
- arXiv: ✓ (2605.03095)
- 来源: [arXiv](https://arxiv.org/abs/2605.03095)

### lee2020biobert ✓
- 作者: ✓ (Lee, Jinhyuk et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (Bioinformatics, vol 36(4), pp 1234-1240)
- 来源: [Oxford Academic](https://academic.oup.com/bioinformatics/article/36/4/1234/5566506)

### beltagy2019scibert ✓
- 作者: ✓ (Beltagy, Lo, Cohan)
- 年份: ✓ (2019)
- 标题: ✓
- Venue: ✓ (EMNLP 2019, pp 3615-3620)
- 来源: [ACL Anthology](https://aclanthology.org/D19-1371/)

### chen2020simclr ✓ [UNCITED]
- 作者: ✓ (Chen, Ting et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (ICML 2020, pp 1597-1607)
- 来源: [PMLR](https://proceedings.mlr.press/v119/chen20j.html)

### grill2020byol ✓ [UNCITED]
- 作者: ✓ (Grill, Jean-Bastien et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (NeurIPS 2020)
- 来源: [NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/f3ada80d5c4ee70142b17b8192b2958e-Abstract.html)

### zhang2021understanding ✓
- 作者: ✓ (Zhang, Chiyuan et al.)
- 年份: ✓ (2021)
- 标题: ✓
- Venue: ✓ (CACM, vol 64(3), pp 107-115)
- DOI: ✓ (10.1145/3446776)
- 来源: [ACM DL](https://dl.acm.org/doi/10.1145/3446776)

### maennel2020random ✓
- 作者: ✓ (Maennel et al.)
- 年份: ✓ (2020)
- 标题: ✓
- Venue: ✓ (NeurIPS 2020)
- 来源: [NeurIPS 2020](https://papers.nips.cc/paper/2020/hash/e4191d610537305de1d294adb121b513-Abstract.html)

### templeton2024saemitigators ✓ [UNCITED]
- 作者: ✓ (Templeton, Adly et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (Transformer Circuits Thread)
- 来源: [Transformer Circuits](https://transformer-circuits.pub/2024/scaling-monosemanticity/)

### alon2023perplexity ✓ [UNCITED]
- 作者: ✓ (Alon & Kamfonas)
- 年份: ✓ (2023)
- 标题: ✓
- arXiv: ✓ (2308.14132)
- 来源: [arXiv](https://arxiv.org/abs/2308.14132)

### nian2025jaildam ✓ [UNCITED]
- 作者: ✓ (Nian, Yi et al.)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (COLM 2025)
- arXiv: ✓ (2504.03770)
- 来源: [arXiv](https://arxiv.org/abs/2504.03770)

### anil2024manyshot ✓ [UNCITED]
- 作者: ✓ (Anil, Cem et al.)
- 年份: ✓ (2024)
- 标题: ✓
- Venue: ✓ (NeurIPS 2024)
- 来源: [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ea456e232efb72d261715e33ce25f208-Abstract-Conference.html)

### jain2023baseline ✓ [UNCITED]
- 作者: ✓ (Jain, Neel et al.)
- 年份: ✓ (2023)
- 标题: ✓
- arXiv: ✓ (2309.00614)
- 来源: [arXiv](https://arxiv.org/abs/2309.00614)

### shen2024jailbreakantidote ✓ [保留此条目]
- 作者: ✓ (Shen, Guobin et al.)
- 年份: ✓ (2024/2025 ICLR)
- 标题: ✓
- arXiv: ✓ (2410.02298)
- 来源: [arXiv](https://arxiv.org/abs/2410.02298), [ICLR 2025](https://iclr.cc/virtual/2025/poster/28150)

### kadali2025internallayers ✓
- 作者: ✓ (Kadali & Papalexakis)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2510.06594)
- 来源: [arXiv](https://arxiv.org/abs/2510.06594)

### markov2023holistic ✓
- 作者: ✓ (Markov, Todor et al.)
- 年份: ✓ (2023)
- 标题: ✓
- Venue: ✓ (AAAI 2023, vol 37, pp 15009-15018)
- 来源: [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/26752)

### wu2025safeint ✓
- 作者: ✓ (Wu, Jiaqi et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2502.15594)
- 来源: [arXiv](https://arxiv.org/abs/2502.15594)

### alobaid2026echochamber ✓
- 作者: ✓ (Alobaid, Ahmad et al.)
- 年份: ✓ (2026)
- 标题: ✓
- arXiv: ✓ (2601.05742)
- 来源: [arXiv](https://arxiv.org/abs/2601.05742)

### yousefpour2025repbend ✓
- 作者: ✓ (Yousefpour, Ashkan et al.)
- 年份: ✓ (2025)
- 标题: ✓
- arXiv: ✓ (2504.01550)
- 来源: [arXiv](https://arxiv.org/abs/2504.01550), [ACL 2025](https://aclanthology.org/2025.acl-long.1173/)

### li2025repejailbreak ✓ [UNCITED]
- 作者: ✓ (Li, Tianlong et al.)
- 年份: ✓ (2025)
- 标题: ✓
- Venue: ✓ (COLING 2025)
- arXiv: ✓ (2401.06824)
- 来源: [arXiv](https://arxiv.org/abs/2401.06824), [ACL Anthology](https://aclanthology.org/2025.coling-main.212/)

### galinkin2024improved ✓ [UNCITED]
- 作者: ✓ (Galinkin, Erick and Sablotny, Martin)
- 年份: ✓ (2024)
- 标题: ✓
- arXiv: ✓ (2412.01547)
- 来源: [arXiv](https://arxiv.org/abs/2412.01547)

---

## 六、引用上下文检查

以下检查正文中的引用是否恰当（cite 了 A 但说的是 B 的结论）：

1. **正文引用均与论文内容匹配**。`\citet{zeng2024pap}` 引用 PAP 的 40 个说服技术 — 正确；`\citet{hagendorff2026reasoning}` 引用大推理模型的越狱能力 — 正确；`\citep{bullwinkel2025repeng}` 引用攻击 turn 占据良性 embedding 区域 — 正确。
2. **ren2024actorattack** 在正文中作为 ActorAttack 数据集/方法引用（experiments.tex line 42: OOD evaluation），引用上下文合理，但 bib 元数据需要修正。
3. **robey2024smoothllm** 在 related_work.tex 作为 perturbation-based defense 引用 — 上下文正确。
4. **所有其他引用上下文检查通过**，无发现 cite A 说 B 的情况。

---

## 七、总结：需要修复的问题优先级

### P0 — 必须修复（正文引用条目，信息严重错误）
1. **ren2024actorattack**: 标题改为实际论文标题，venue 改为 ACL 2025，添加 arXiv ID 2410.10700
2. **robey2024smoothllm**: venue 从 ICML 2024 改为 arXiv preprint (或 TMLR 2025)
3. **mehrotra2024tap**: 标题副标题从 "with the Pruning of Candidate Outputs" 改为 "Automatically"
4. **jiang2024redqueen**: 标题更新为发表版，year 改为 2025，venue 改为 Findings of ACL 2025

### P1 — 建议修复
5. **metallamaguard3_2024**: 改为引用 Llama 3 Herd 论文
6. **gguard2025**: 标题更新为 arXiv v2 版
7. **lu2025xboundary**: 标题更新为发表版
8. **chao2024jailbreakbench**: 补充 NeurIPS 2024 venue
9. **song2026multibreak**: 确认 ICML 2026 接收状态或改为 arXiv preprint

### P2 — 清理
10. 删除 18 条未引用条目（或移入注释）
11. 删除重复条目 shen2025antidote 和 hsu2024improved
