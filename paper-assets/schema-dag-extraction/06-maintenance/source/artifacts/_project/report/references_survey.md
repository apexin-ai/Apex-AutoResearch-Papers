# References Survey for Schema-DAG-Extraction

> Generated: 2026-05-15 | Purpose: Related work expansion (Dream review feedback)

## Required References (14)

### 1. LLM-PEE
- **Full title**: Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction
- **Authors**: Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
- **Venue**: EMNLP 2025 (Main)
- **arXiv/DOI**: arXiv:2503.02628 | https://aclanthology.org/2025.emnlp-main.1743/
- **Key contribution**: Proposes similarity-based type recall (ColBERT) + type-partitioning prompting to handle massive event types (3,465 types). Creates EEMT dataset (200K+ samples). Achieves 12.9% F1 improvement over mainstream LLMs in zero-shot setting.
- **Relation to our work**: [support] — Directly validates our core claim that schema partitioning improves LLM IE; their embedding-similarity partitioning is a key baseline for our DAG-based approach.

### 2. GoLLIE
- **Full title**: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction
- **Authors**: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre
- **Venue**: ICLR 2024
- **arXiv/DOI**: arXiv:2310.03668 | https://openreview.net/forum?id=Y3wpuxd7u9
- **Key contribution**: Fine-tunes Code-LLaMA to follow annotation guidelines encoded as Python class definitions with docstrings. Demonstrates that code-style schema representation enables zero-shot generalization to unseen IE tasks.
- **Relation to our work**: [complement] — Demonstrates code-style schema formatting for IE; our work addresses schema complexity/confusability orthogonally to schema representation format.

### 3. GLiNER
- **Full title**: GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer
- **Authors**: Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois
- **Venue**: NAACL 2024
- **arXiv/DOI**: arXiv:2311.08526 | https://aclanthology.org/2024.naacl-long.300/
- **Key contribution**: Compact bidirectional NER model that matches entity type embeddings to span representations in latent space. GLiNER-L (F1=60.9) outperforms ChatGPT and fine-tuned LLMs in zero-shot NER while being 140x smaller than UniNER-13B.
- **Relation to our work**: [contrast] — Encoder-based approach that avoids type confusability via parallel span-type matching; contrasts with our generative decomposition strategy.

### 4. IEPile
- **Full title**: IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus
- **Authors**: Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, Huajun Chen
- **Venue**: ACL 2024 (Short)
- **arXiv/DOI**: arXiv:2402.14710 | https://aclanthology.org/2024.acl-short.13/
- **Key contribution**: Constructs 0.32B-token bilingual IE instruction corpus with hard-negative schema construction — explicitly building confusable schema pairs to train models to discriminate semantically proximate types. Covers NER, RE, EE across 33 datasets.
- **Relation to our work**: [support] — Hard-negative schema construction directly validates our type confusability hypothesis; their training-based mitigation complements our training-free decomposition approach.

### 5. CrossAgentIE
- **Full title**: CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction
- **Authors**: Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang
- **Venue**: ACL 2025 Findings
- **arXiv/DOI**: https://aclanthology.org/2025.findings-acl.718/ | https://openreview.net/forum?id=OaSBRV0xMG
- **Key contribution**: Multi-agent framework with intra-group cross-type debate (resolves entity-label conflicts via confidence aggregation) and inter-group cross-task debate (NER↔RE mutual refinement). Template fine-tuning distills multi-agent outputs into single model.
- **Relation to our work**: [support] — Explicitly addresses type confusion via multi-agent debate; validates that type confusability is a real bottleneck in zero-shot IE.

### 6. InstructUIE
- **Full title**: InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction
- **Authors**: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du
- **Venue**: arXiv 2023 (preprint)
- **arXiv/DOI**: arXiv:2304.08085
- **Key contribution**: Unified IE framework via instruction tuning on IE INSTRUCTIONS benchmark (32 datasets). Outperforms GPT-3.5 in zero-shot settings and BERT-base in supervised NER/RE/EE.
- **Relation to our work**: [complement] — Representative of instruction-tuning UIE paradigm; our training-free approach targets the same tasks but without fine-tuning.

### 7. KGGen
- **Full title**: KGGen: Extracting Knowledge Graphs from Plain Text with Language Models
- **Authors**: Belinda Mo, Kyssen Yu, Joshua Kazdan, Joan Cabezas, Proud Mpala, Lisa Yu, Chris Cundy, Charilaos Kanatsoulis, Sanmi Koyejo
- **Venue**: NeurIPS 2025
- **arXiv/DOI**: arXiv:2502.09956 | https://openreview.net/forum?id=YyhRJXxbpi
- **Key contribution**: Two-stage KG extraction: LM-based triple extraction → iterative entity clustering for deduplication. Introduces MINE benchmark. Addresses entity sparsity via node consolidation and edge merging.
- **Relation to our work**: [complement] — Post-extraction deduplication addresses related but distinct problem; their entity resolution stage handles type/entity confusion at output level vs. our input-level schema decomposition.

### 8. Ethayarajh (2019) — Contextual Anisotropy
- **Full title**: How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings
- **Authors**: Kawin Ethayarajh
- **Venue**: EMNLP-IJCNLP 2019
- **arXiv/DOI**: arXiv:1909.00512 | https://aclanthology.org/D19-1006/
- **Key contribution**: Shows all layers of BERT/ELMo/GPT-2 exhibit anisotropy — representations occupy a narrow cone in embedding space. Upper layers produce more context-specific representations. Less than 5% variance explained by static embeddings.
- **Relation to our work**: [support] — Anisotropy of contextual representations provides theoretical grounding for why embedding-based type similarity measures can be unreliable, motivating our confusability-aware decomposition.

### 9. Gao et al. (2019) — Representation Degeneration
- **Full title**: Representation Degeneration Problem in Training Natural Language Generation Models
- **Authors**: Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu
- **Venue**: ICLR 2019
- **arXiv/DOI**: arXiv:1907.12009 | https://openreview.net/forum?id=SkEYojRqtm
- **Key contribution**: Proves weight-tying in NLG causes word embeddings to degenerate into a narrow cone (especially low-frequency tokens). Proposes cosine regularization (MLE-CosReg) to mitigate.
- **Relation to our work**: [support] — Theoretical foundation for embedding degeneration that underlies type confusability in LLM embedding space; explains why semantically distinct types can have high cosine similarity.

### 10. LLM4IE Survey
- **Full title**: Large Language Models for Generative Information Extraction: A Survey
- **Authors**: Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xian Wu, Yefeng Zheng, Yang Wang, Enhong Chen
- **Venue**: Frontiers of Computer Science, vol. 18, no. 6, December 2024
- **arXiv/DOI**: arXiv:2312.17617 | DOI:10.1007/s11704-024-40555-y
- **Key contribution**: Comprehensive survey categorizing LLM-based IE by subtask taxonomy (NER/RE/EE/KG) and technique taxonomy (ICL, instruction tuning, tool augmentation). Covers low-resource scenarios and emerging trends.
- **Relation to our work**: [complement] — Positions our work within the broader LLM4IE landscape; our type confusability analysis fills a gap not covered by existing surveys.

### 11. UniNER
- **Full title**: UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition
- **Authors**: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon
- **Venue**: ICLR 2024
- **arXiv/DOI**: arXiv:2308.03279 | https://openreview.net/forum?id=r65xfUb76p
- **Key contribution**: Distills ChatGPT into smaller models (7B) for open NER via mission-focused instruction tuning. Per-type querying strategy. Largest NER benchmark (43 datasets, 9 domains). Outperforms ChatGPT by 7-9 F1 points. UniNER-type variant struggles with semantically similar types.
- **Relation to our work**: [support] — Per-type splitting is an extreme schema decomposition; their finding that UniNER-type fails on semantically similar types directly supports our confusability analysis.

### 12. CMAS-NER
- **Full title**: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition
- **Authors**: Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, Zhaochun Ren
- **Venue**: TheWebConf (WWW) 2025
- **arXiv/DOI**: arXiv:2502.18702 | DOI:10.1145/3696410.3714923
- **Key contribution**: Four-agent cooperative framework (self-annotator, TRF extractor, demonstration discriminator, overall predictor). Decomposes NER into entity recognition + type-related feature extraction. Self-reflection mechanism for demonstration selection.
- **Relation to our work**: [support] — Schema decomposition via multi-agent collaboration; their type-related feature extraction validates the importance of isolating type-specific signals.

### 13. KnowCoder
- **Full title**: KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction
- **Authors**: Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
- **Venue**: ACL 2024 (Long)
- **arXiv/DOI**: arXiv:2403.07969 | https://aclanthology.org/2024.acl-long.475/
- **Key contribution**: Code-style schema library covering 30,000+ types (29,177 entity, 876 relation, 519 event). Two-phase learning: code pretraining (1.5B data) + instruction tuning. 49.8% F1 improvement over LLaMA2 in few-shot; up to 21.9% improvement in low-resource.
- **Relation to our work**: [complement] — Largest schema library for UIE; demonstrates that scaling schema types requires structured representation. Our work addresses the confusability problem that arises when scaling to many types.

### 14. Lost in the Middle
- **Full title**: Lost in the Middle: How Language Models Use Long Contexts
- **Authors**: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
- **Venue**: TACL 2024, vol. 12, pp. 157-173
- **arXiv/DOI**: arXiv:2307.03172 | DOI:10.1162/tacl_a_00638
- **Key contribution**: Demonstrates position bias in long-context LLMs: performance degrades when relevant information is in the middle of input. Affects multi-document QA and key-value retrieval. Even explicitly long-context models exhibit this U-shaped performance curve.
- **Relation to our work**: [support] — Provides theoretical motivation for schema decomposition: stuffing all types into one prompt causes middle-position types to be overlooked, directly supporting our partitioning approach.

---

## Additional References (7)

### 15. CodeIE
- **Full title**: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors
- **Authors**: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu
- **Venue**: ACL 2023 (Long)
- **arXiv/DOI**: arXiv:2305.05711 | https://aclanthology.org/2023.acl-long.855/
- **Key contribution**: Recasts IE structured output as code generation; Code-LLMs (Codex) outperform both fine-tuned IE models (UIE) and NL-LLMs in few-shot NER and RE. Lower perplexity for code-format output explains Code-LLM advantage.
- **Relation to our work**: [complement] — Pioneering work on code-style IE that inspired GoLLIE/KnowCoder; our schema decomposition is orthogonal to output format.

### 16. ADELIE
- **Full title**: ADELIE: Aligning Large Language Models on Information Extraction
- **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li
- **Venue**: EMNLP 2024 (Main)
- **arXiv/DOI**: arXiv:2405.05008 | https://aclanthology.org/2024.emnlp-main.419/
- **Key contribution**: Aligns LLMs for IE via IEInstruct dataset (83K+ instances) + SFT + DPO training. Handles closed/open/on-demand IE. 5% F1 improvement over standard LLMs in closed IE.
- **Relation to our work**: [contrast] — Training-based alignment approach to IE; our training-free method avoids alignment cost while addressing schema complexity directly.

### 17. Decompose, Enrich, and Extract! (DEE)
- **Full title**: Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs
- **Authors**: Fatemeh Shiri, Van Nguyen, Farhad Moghimifar, John Yoo, Gholamreza Haffari, Yuan-Fang Li
- **Venue**: IEEE ICTAI 2024
- **arXiv/DOI**: arXiv:2406.01045 | https://ieeexplore.ieee.org/document/10706385/
- **Key contribution**: Decomposes event extraction into detection + argument extraction; enriches prompts with dynamic schema-aware retrieval examples. Addresses LLM hallucination in EE via task decomposition.
- **Relation to our work**: [support] — Schema-aware decomposition for event extraction directly validates our decomposition strategy; their retrieval-augmented approach complements our confusability-based partitioning.

### 18. OneKE
- **Full title**: OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System
- **Authors**: Yujie Luo, Lingyong Yan, Zhenghao Liu, Yixin Ji, Weiqi Wang, Shi Yu, Yukun Yan, Shuo Wang, Yue Zhang, Shulin Cao, Weicheng Ren, Honghao Gui, Zhen Bi, Yongfei Huang, Yuan Yao, Ningyu Zhang, Huajun Chen
- **Venue**: WWW 2025 (Companion)
- **arXiv/DOI**: arXiv:2412.20005 | DOI:10.1145/3701716.3715189
- **Key contribution**: Multi-agent system (Schema Agent + Extraction Agent + Reflection Agent) for schema-guided knowledge extraction from web/PDF. Supports various LLM backends and integrates case repository for error correction.
- **Relation to our work**: [complement] — System-level multi-agent IE framework; our confusability analysis could inform their Schema Agent's type decomposition strategy.

### 19. Schema as Parameterized Tools (SPT)
- **Full title**: Schema as Parameterized Tools for Universal Information Extraction
- **Authors**: (arXiv 2025)
- **Venue**: arXiv preprint, June 2025
- **arXiv/DOI**: arXiv:2506.01276 | https://openreview.net/forum?id=r1QGqAOBxa
- **Key contribution**: Reframes IE as tool-calling: schemas become parameterized tools for selection and parameter filling. Unifies closed/open/on-demand IE via schema retrieval, filling, and generation. Comparable to LoRA baselines with fewer trainable parameters.
- **Relation to our work**: [complement] — Novel schema-as-tools paradigm for UIE; when numerous schemas exist, their schema retrieval faces similar confusability challenges that our DAG decomposition addresses.

### 20. PARSE
- **Full title**: PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction
- **Authors**: (Amazon Science, 2025)
- **Venue**: arXiv preprint, October 2025
- **arXiv/DOI**: arXiv:2510.08623
- **Key contribution**: Treats JSON schemas as optimization targets; iteratively refines schema definitions to reduce LLM extraction errors. Addresses that ambiguous/incomplete schema specifications cause hallucinations and unreliable agent behavior.
- **Relation to our work**: [complement] — Schema optimization approach to reduce extraction errors; our work addresses confusability at the schema presentation level while PARSE addresses it at the schema definition level.

### 21. Familiarity: Zero-Shot NER Label Shift
- **Full title**: Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data
- **Authors**: (arXiv, December 2024)
- **arXiv/DOI**: arXiv:2412.10121
- **Key contribution**: Introduces metrics to quantify label shifts in synthetic NER training data. Shows that models trained on LLM-generated datasets with thousands of entity types suffer from varying label shift effects, impacting zero-shot generalization.
- **Relation to our work**: [support] — Quantifies how large label spaces create distribution shifts that degrade NER performance, directly supporting our claim that label space size matters for IE quality.

---

## Summary Statistics
- Total references found: **14/14 required + 7 additional = 21 total**
- Not found: None — all 14 required papers verified via web search
- Coverage by relation type:
  - **Support** (validates our claims): #1 LLM-PEE, #4 IEPile, #5 CrossAgentIE, #8 Ethayarajh, #9 Gao, #11 UniNER, #12 CMAS-NER, #14 Lost in the Middle, #17 DEE, #21 Familiarity (10 papers)
  - **Complement** (orthogonal methods): #2 GoLLIE, #6 InstructUIE, #7 KGGen, #10 LLM4IE Survey, #13 KnowCoder, #15 CodeIE, #18 OneKE, #19 SPT, #20 PARSE (9 papers)
  - **Contrast** (alternative approaches): #3 GLiNER, #16 ADELIE (2 papers)
