# Reference Audit Report

审计日期：2026-05-14

## 审计结果

| # | Key | 状态 | 说明 |
|---|-----|------|------|
| 1 | scienceworld-2022 | ✅ | Wang et al., EMNLP 2022。标题、作者、venue 均正确 |
| 2 | react-2023 | ✅ | Yao et al., ICLR 2023。标题、作者、venue 均正确 |
| 3 | art-2023 | ✅ | Paranjape et al., arXiv:2303.09014, 2023。标题、作者均正确 |
| 4 | toolformer-2024 | ⚠️ | 年份错误：实际为 NeurIPS **2023**，bib 写了 2024 |
| 5 | chameleon-2024 | ⚠️ | 年份错误：实际为 NeurIPS **2023**，bib 写了 2024 |
| 6 | retool-2026 | ⚠️ | 年份错误：arXiv:2504.11536 提交于 2025 年 4 月，bib 写了 2026 |
| 7 | cogrouter-2026 | ⚠️ | 第一作者错误：实际为 Yang, Ruihan（杨瑞涵），bib 写了 Yang, Jiahao |
| 8 | ares-2026 | ⚠️ | 第一作者错误：实际为 Yang, Jingbo，bib 写了 Yang, Zhuoqun |
| 9 | mixture-of-recursions-2025 | ⚠️ | 第一作者错误：实际为 Bae, Sangmin，bib 写了 Bae, Jongho |
| 10 | mtrouter-2026 | ⚠️ | 第一作者错误：实际为 Zhang, Yiqun，bib 写了 Zhang, Yifan |
| 11 | itp-2026 | ⚠️ | 第一作者错误：实际为 Liu, Youwei，bib 写了 Liu, Haoyu |
| 12 | dynathink-2025 | ⚠️ | 作者已解匿名：实际为 Yu, Xiao et al.（Microsoft Research），bib 仍写 Anonymous |
| 13 | envsimbench-2026 | ❌ | 未找到任何可验证来源（无 arXiv、无 OpenReview、无 GitHub），高度疑似幻觉引用 |

## 需要修正的条目

### 4. toolformer — 年份 2024 → 2023

```bibtex
@inproceedings{toolformer-2024,
  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2023}
}
```

### 5. chameleon — 年份 2024 → 2023

```bibtex
@inproceedings{chameleon-2024,
  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2023}
}
```

### 6. retool — 年份 2026 → 2025

```bibtex
@article{retool-2026,
  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
  author={Feng, Jiazhan and others},
  journal={arXiv preprint arXiv:2504.11536},
  year={2025}
}
```

### 7. cogrouter — 第一作者 Yang, Jiahao → Yang, Ruihan

```bibtex
@article{cogrouter-2026,
  title={Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents},
  author={Yang, Ruihan and others},
  journal={arXiv preprint arXiv:2602.12662},
  year={2026}
}
```

### 8. ares — 第一作者 Yang, Zhuoqun → Yang, Jingbo

```bibtex
@article{ares-2026,
  title={ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents},
  author={Yang, Jingbo and others},
  journal={arXiv preprint arXiv:2603.07915},
  year={2026}
}
```

### 9. mixture-of-recursions — 第一作者 Bae, Jongho → Bae, Sangmin

```bibtex
@inproceedings{mixture-of-recursions-2025,
  title={Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation},
  author={Bae, Sangmin and others},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2025}
}
```

### 10. mtrouter — 第一作者 Zhang, Yifan → Zhang, Yiqun

```bibtex
@inproceedings{mtrouter-2026,
  title={MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings},
  author={Zhang, Yiqun and others},
  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2026}
}
```

### 11. itp — 第一作者 Liu, Haoyu → Liu, Youwei

```bibtex
@article{itp-2026,
  title={Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models},
  author={Liu, Youwei and others},
  journal={arXiv preprint arXiv:2601.08955},
  year={2026}
}
```

### 12. dynathink — Anonymous → 实际作者

```bibtex
@article{dynathink-2025,
  title={Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents},
  author={Yu, Xiao and others},
  journal={arXiv preprint arXiv:2506.00320},
  year={2025}
}
```

## 可能幻觉的条目

### 13. envsimbench-2026 ❌

**问题**：搜索 "EnvSimBench: State Prediction for LLM Environment Simulation" 未找到任何匹配结果。无 arXiv 页面、无 OpenReview 提交、无 GitHub 仓库、无 Semantic Scholar 条目。

**建议**：
- 如果论文中引用 EnvSimBench 作为评测基准，需要找到真实替代或删除该引用
- 相关的真实 benchmark 替代选项：
  - **EnvBench** (ICLR 2025 Workshop) — 自动化环境搭建 benchmark
  - **SimBench** (OpenReview) — LLM 行为模拟 benchmark
  - **ScienceWorld** (已在 references 中) — 交互式环境中的 agent 评测
