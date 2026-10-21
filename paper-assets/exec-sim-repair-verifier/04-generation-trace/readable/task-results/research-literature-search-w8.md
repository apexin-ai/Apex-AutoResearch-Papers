# research literature search w8

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-search-w8_20260519T090952_result.json`
- **Structured JSON:** [`0d1f794bff91f106e86f.json`](../../sessions/0d/0d1f794bff91f106e86f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部找到。以下是完整结果。

---

## 1. CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation

**BibTeX:**
```bibtex
@inproceedings{li2025codeprm,
    title     = {{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation},
    author    = {Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong},
    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
    year      = {2025},
    address   = {Vienna, Austria},
    pages     = {8169--8182},
    doi       = {10.18653/v1/2025.findings-acl.428},
}
```

**与本文关系：** CodePRM 用 execution feedback 构建 process reward model 来验证 code generation 的中间步骤，与本文的 per-test classification formulation 共享 process supervision 视角，但 CodePRM 依赖 execution feedback 而本文是 execution-free。

**建议引用：** Yes. 直接相关的 process-level verification baseline，且凸显本文 execution-free 的差异化贡献。

---

## 2. FunPRM: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation

**BibTeX:**
```bibtex
@misc{zhang2026funprm,
    title         = {{FunPRM}: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation},
    author        = {Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xue, Eric and Xie, Pengtao},
    year          = {2026},
    eprint        = {2601.22249},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}
```

**与本文关系：** FunPRM 将函数作为 PRM 的推理步骤粒度，与本文的 function-level verification 思路相近；其 meta-learning reward correction 机制也涉及用 test outcome 去校准 process reward，可作为 function-level granularity 的对照讨论。

**建议引用：** Yes. 同期工作，function-level verification granularity 的直接对照。

---

## 3. Efficient Guided Generation for Large Language Models

**BibTeX:**
```bibtex
@misc{willard2023efficient,
    title         = {Efficient Guided Generation for Large Language Models},
    author        = {Willard, Brandon T. and Louf, R\'{e}mi},
    year          = {2023},
    eprint        = {2307.09702},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}
```

**与本文关系：** 本文 CWM formulation 使用 constrained decoding 强制输出符合 per-test JSON schema；Willard & Louf 提出的 FSM-guided generation（Outlines 库的理论基础）正是此类 format compliance 的方法论支撑。

**建议引用：** Yes. CWM constrained decoding 的方法论引用，说明 format compliance 有理论保障。

---

## 4. CodeScaler: Scaling Code LLM Training and Test-Time Inference via Execution-Free Reward Models

**BibTeX:**
```bibtex
@misc{zhu2026codescaler,
    title         = {{CodeScaler}: Scaling Code {LLM} Training and Test-Time Inference via Execution-Free Reward Models},
    author        = {Zhu, Xiao and Zhou, Xinyu and Zhu, Boyu and Hu, Hanxu and Du, Mingzhe and Zhang, Haotian and Wang, Huiming and Guo, Zhijiang},
    year          = {2026},
    eprint        = {2602.17684},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}
```

**与本文关系：** CodeScaler 训练 execution-free reward model 用于 RL 训练和 test-time inference，与本文核心主题（execution-free verification）高度重合。其 syntax-aware code extraction 和 validity-preserving reward shaping 可作为 execution-free 方向的同期工作讨论。关键差异：CodeScaler 侧重 RL 训练 scaling，本文侧重 repair verification formulation 比较。

**建议引用：** Yes. 同期 execution-free verification 工作，强化本文研究方向的时效性和重要性。

---

## 5. CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment

**BibTeX:**
```bibtex
@misc{jiang2025coderlplus,
    title         = {{CodeRL}+: Improving Code Generation via Reinforcement with Execution Semantics Alignment},
    author        = {Jiang, Xue and Dong, Yihong and Liu, Mengyang and Deng, Hongyi and Wang, Tian and Tao, Yongding and Cao, Rongyu and Li, Binhua and Jin, Zhi and Jiao, Wenpin and Huang, Fei and Li, Yongbin and Li, Ge},
    year          = {2025},
    eprint        = {2510.18471},
    archivePrefix = {arXiv},
    primaryClass  = {cs.SE},
}
```

**与本文关系：** CodeRL+ 将 execution semantics（variable-level execution trajectories）融入 RL 训练，解决 binary pass/fail signal 过于稀疏的问题。与本文的 TRAJ formulation（trajectory-level verification）概念上相关：都试图利用比 binary outcome 更细粒度的 execution 信息。差异在于 CodeRL+ 用于 RL 训练，本文用于 verification。

**建议引用：** Yes. execution semantics alignment 视角支撑本文 TRAJ formulation 的动机。

---

## 6. Mutation-Real Fault Coupling

### 6a. Just et al. (FSE 2014) — 最直接的实证验证

**BibTeX:**
```bibtex
@inproceedings{just2014mutants,
    title     = {Are Mutants a Valid Substitute for Real Faults in Software Testing?},
    author    = {Just, Ren\'{e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D. and Holmes, Reid and Fraser, Gordon},
    booktitle = {Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering},
    series    = {FSE 2014},
    year      = {2014},
    address   = {Hong Kong, China},
    pages     = {654--665},
    doi       = {10.1145/2635868.2635929},
}
```

**与本文关系：** 本文用 synthetic mutations 训练和评测 verifier，coupling hypothesis（mutation detection 与 real fault detection 显著相关）是这一设计选择的理论基础。Just et al. 在 357 个真实缺陷上实证验证了这一假设，是最直接的支撑文献。

**建议引用：** Yes. 支撑本文 synthetic mutation 实验设计的核心理论依据。

### 6b. Andrews et al. (TSE 2006) — 奠基性实证研究

**BibTeX:**
```bibtex
@article{andrews2006mutation,
    title   = {Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria},
    author  = {Andrews, James H. and Briand, Lionel C. and Labiche, Yvan and Namin, Akbar Siami},
    journal = {IEEE Transactions on Software Engineering},
    volume  = {32},
    number  = {8},
    pages   = {608--624},
    year    = {2006},
    doi     = {10.1109/TSE.2006.83},
}
```

**与本文关系：** 奠基性工作，证明 generated mutants 可有效替代真实缺陷进行测试评估。Just et al. 2014 在此基础上做了更大规模验证。

**建议引用：** Yes（可选）。如果篇幅允许，与 Just et al. 一起引用提供更完整的理论链条；篇幅紧张时只引 Just et al. 即可。

---

## 汇总 BibTeX（可直接复制）

```bibtex
% === 1. CodePRM (ACL 2025 Findings) ===
@inproceedings{li2025codeprm,
    title     = {{CodePRM}: Execution Feedback-enhanced Process Reward Model for Code Generation},
    author    = {Li, Qingyao and Dai, Xinyi and Li, Xiangyang and Zhang, Weinan and Wang, Yasheng and Tang, Ruiming and Yu, Yong},
    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
    year      = {2025},
    address   = {Vienna, Austria},
    pages     = {8169--8182},
    doi       = {10.18653/v1/2025.findings-acl.428},
}

% === 2. FunPRM (arXiv 2026) ===
@misc{zhang2026funprm,
    title         = {{FunPRM}: Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation},
    author        = {Zhang, Ruiyi and Qin, Peijia and Cao, Qi and Xue, Eric and Xie, Pengtao},
    year          = {2026},
    eprint        = {2601.22249},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}

% === 3. Willard & Louf (arXiv 2023) ===
@misc{willard2023efficient,
    title         = {Efficient Guided Generation for Large Language Models},
    author        = {Willard, Brandon T. and Louf, R\'{e}mi},
    year          = {2023},
    eprint        = {2307.09702},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}

% === 4. CodeScaler (arXiv 2026) ===
@misc{zhu2026codescaler,
    title         = {{CodeScaler}: Scaling Code {LLM} Training and Test-Time Inference via Execution-Free Reward Models},
    author        = {Zhu, Xiao and Zhou, Xinyu and Zhu, Boyu and Hu, Hanxu and Du, Mingzhe and Zhang, Haotian and Wang, Huiming and Guo, Zhijiang},
    year          = {2026},
    eprint        = {2602.17684},
    archivePrefix = {arXiv},
    primaryClass  = {cs.CL},
}

% === 5. CodeRL+ (arXiv 2025) ===
@misc{jiang2025coderlplus,
    title         = {{CodeRL}+: Improving Code Generation via Reinforcement with Execution Semantics Alignment},
    author        = {Jiang, Xue and Dong, Yihong and Liu, Mengyang and Deng, Hongyi and Wang, Tian and Tao, Yongding and Cao, Rongyu and Li, Binhua and Jin, Zhi and Jiao, Wenpin and Huang, Fei and Li, Yongbin and Li, Ge},
    year          = {2025},
    eprint        = {2510.18471},
    archivePrefix = {arXiv},
    primaryClass  = {cs.SE},
}

% === 6a. Just et al. (FSE 2014) — mutation-real fault coupling ===
@inproceedings{just2014mutants,
    title     = {Are Mutants a Valid Substitute for Real Faults in Software Testing?},
    author    = {Just, Ren\'{e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D. and Holmes, Reid and Fraser, Gordon},
    booktitle = {Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering},
    series    = {FSE 2014},
    year      = {2014},
    address   = {Hong Kong, China},
    pages     = {654--665},
    doi       = {10.1145/2635868.2635929},
}

% === 6b. Andrews et al. (TSE 2006) — mutation analysis foundations ===
@article{andrews2006mutation,
    title   = {Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria},
    author  = {Andrews, James H. and Briand, Lionel C. and Labiche, Yvan and Namin, Akbar Siami},
    journal = {IEEE Transactions on Software Engineering},
    volume  = {32},
    number  = {8},
    pages   = {608--624},
    year    = {2006},
    doi     = {10.1109/TSE.2006.83},
}
```

7 篇 BibTeX 全部基于 WebSearch 验证，非幻觉。建议全部引用（Andrews et al. 视篇幅可选）。

---
