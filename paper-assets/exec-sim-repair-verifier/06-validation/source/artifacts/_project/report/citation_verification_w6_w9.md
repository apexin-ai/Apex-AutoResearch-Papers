# Citation Verification & Supplementary Citations (W6/W9)

Generated: 2026-05-15

---

## Part A: Bib 条目核查结果 (W9)

### 核查总结

- 总条目数: 24
- 正确: 15
- **错误 (first author 不一致): 8**
- 需注意: 1

### 错误条目明细

| bib key | 论文标题 | bib 中 first author | 实际 first author | arXiv ID |
|---------|---------|---------------------|-------------------|----------|
| `ding2025selfexecution` | Self-Execution Simulation Improves Coding Models | Ding, Yangruibo | **Maimon, Gallil** | 2604.03253 |
| `ye2025demystifying` | Demystifying Errors in LLM Reasoning Traces | Ye, Yanzhuo | **Abdollahi, Mohammad** | 2512.00215 |
| `chen2025solidcoder` | SolidCoder: Bridging the Mental-Reality Gap | Chen, Xinyun | **Lee, Woojin** | 2604.19825 |
| `zhang2025swerm` | SWE-RM: Execution-free Feedback | Zhang, Jiayi | **Shum, KaShun** | 2512.21919 |
| `wu2025patchreasoner` | Scalable Supervising Software Agents with Patch Reasoner | Wu, Zuxin | **Xu, Junjielong** | 2510.22775 |
| `wang2025vgsearch` | Rethinking Optimal Verification Granularity | Wang, Jinghan | **Chen, Hao Mark** | 2505.11730 |
| `zhang2025sstar` | S*: Test Time Scaling for Code Generation | Zhang, Dacheng | **Li, Dacheng** | 2502.14382 |
| `aleithan2025survey` | A Survey of LLM-based Automated Program Repair | Aleithan, Reem | **Yang, Boyang** | 2506.23749 |

### 需注意条目

| bib key | 说明 |
|---------|------|
| `meta2025cwm` | bib 中 author 为 `{Meta AI}`。实际论文作者为 FAIR CodeGen team + 50+ 个人作者（首位个人作者 Jade Copet）。团队署名可接受但不精确。 |

### 正确条目 (15/24)

| bib key | first author | 状态 |
|---------|-------------|------|
| `liu2024codemind` | Liu, Changshu | ✅ |
| `snell2024scaling` | Snell, Charlie | ✅ |
| `jimenez2024swebench` | Jimenez, Carlos E | ✅ |
| `chowdhury2024swebenchverified` | Chowdhury, Neil | ✅ |
| `yang2024sweagent` | Yang, John | ✅ |
| `xia2024agentless` | Xia, Chunqiu Steven | ✅ |
| `yang2024qwen25` | Yang, An | ✅ |
| `chen2021humaneval` | Chen, Mark | ✅ |
| `austin2021mbpp` | Austin, Jacob | ✅ |
| `hu2022lora` | Hu, Edward J | ✅ |
| `dettmers2024qlora` | Dettmers, Tim | ✅ |
| `rajpurkar2016squad` | Rajpurkar, Pranav | ✅ |
| `lewis2020bart` | Lewis, Mike | ✅ |
| `raffel2020t5` | Raffel, Colin | ✅ |
| `schuirmann1987tost` | Schuirmann, Donald J | ✅ |
| `davison1997bootstrap` | Davison, Anthony C | ✅ |
| `shrout1979icc` | Shrout, Patrick E | ✅ |

---

## Part A-fix: 修正后的 BibTeX 条目

```bibtex
@article{maimon2025selfexecution,
  title={Self-Execution Simulation Improves Coding Models},
  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
  journal={arXiv preprint arXiv:2604.03253},
  year={2025}
}

@article{abdollahi2025demystifying,
  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
  journal={arXiv preprint arXiv:2512.00215},
  year={2025}
}

@article{lee2025solidcoder,
  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
  author={Lee, Woojin and Huang, Jin-Xia},
  journal={arXiv preprint arXiv:2604.19825},
  year={2025}
}

@article{shum2025swerm,
  title={{SWE-RM}: Execution-free Feedback for Software Engineering Agents},
  author={Shum, KaShun and Hui, Binyuan and Chen, Jiawei and Zhang, Lei and Yang, Jiaxi and Huang, Yuzhen and Lin, Junyang and He, Junxian},
  journal={arXiv preprint arXiv:2512.21919},
  year={2025}
}

@article{xu2025patchreasoner,
  title={Scalable Supervising Software Agents with Patch Reasoner},
  author={Xu, Junjielong and Tan, Boyin and Liu, Xiaoyuan and Peng, Chao and Gao, Pengfei and He, Pinjia},
  journal={arXiv preprint arXiv:2510.22775},
  year={2025}
}

@article{chen2025vgsearch,
  title={Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling},
  author={Chen, Hao Mark and Lu, Guanxi and Okoshi, Yasuyuki and Mo, Zhiwen and Motomura, Masato and Fan, Hongxiang},
  journal={arXiv preprint arXiv:2505.11730},
  year={2025}
}

@inproceedings{li2025sstar,
  title={S*: Test Time Scaling for Code Generation},
  author={Li, Dacheng and Cao, Shiyi and Cao, Chengkun and Li, Xiuyu and Tan, Shangyin and Keutzer, Kurt and Xing, Jiarong and Gonzalez, Joseph E. and Stoica, Ion},
  booktitle={Findings of EMNLP},
  year={2025}
}

@article{yang2025aprsurvey,
  title={A Survey of {LLM}-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications},
  author={Yang, Boyang and Cai, Zijian and Liu, Fengling and Le, Bach and Zhang, Lingming and Bissyand{\'e}, Tegawend{\'e} F. and Liu, Yang and Tian, Haoye},
  journal={arXiv preprint arXiv:2506.23749},
  year={2025}
}
```

**注意**: 修正后 bib key 也需更新（如 `ding2025selfexecution` → `maimon2025selfexecution`），论文 .tex 中的 `\cite{}` 引用需同步修改。

---

## Part B: 补充引用 BibTeX 条目 (W6)

### 1. LEVER (Ni et al., ICML 2023)

```bibtex
@inproceedings{ni2023lever,
  title={{LEVER}: Learning to Verify Language-to-Code Generation with Execution},
  author={Ni, Ansong and Iyer, Srini and Radev, Dragomir and Stoyanov, Veselin and Yih, Wen-tau and Wang, Sida I. and Lin, Xi Victoria},
  booktitle={ICML},
  year={2023}
}
```

### 2. CodeT (Chen et al., ICLR 2023)

```bibtex
@inproceedings{chen2023codet,
  title={{CodeT}: Code Generation with Generated Tests},
  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},
  booktitle={ICLR},
  year={2023}
}
```

### 3. Andrews et al. (2005, ICSE)

```bibtex
@inproceedings{andrews2005mutation,
  title={Is Mutation an Appropriate Tool for Testing Experiments?},
  author={Andrews, James H. and Briand, Lionel C. and Labiche, Yvan},
  booktitle={ICSE},
  pages={402--411},
  year={2005}
}
```

### 4. Just et al. (2014, FSE)

```bibtex
@inproceedings{just2014mutants,
  title={Are Mutants a Valid Substitute for Real Faults in Software Testing?},
  author={Just, Ren{\'e} and Jalali, Darioush and Inozemtseva, Laura and Ernst, Michael D. and Holmes, Reid and Fraser, Gordon},
  booktitle={FSE},
  year={2014}
}
```

### 5. VG-Search (Chen et al., 2025) — 已在 bib 中但需修正

见 Part A-fix 中的 `chen2025vgsearch` 条目。原 `wang2025vgsearch` first author 错误。

---

## Qwen3 技术报告状态

**Qwen3 有独立技术报告。** arXiv:2505.09388，发布于 2025-05-14。

当前 bib 中引用 Qwen2.5 报告 (`yang2024qwen25`, arXiv:2412.15115) 来支持 Qwen 模型，如果论文使用的是 Qwen3 模型，应改用或增加 Qwen3 报告引用：

```bibtex
@article{qwen2025qwen3,
  title={{Qwen3} Technical Report},
  author={Yang, An and Li, Anfeng and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and others},
  journal={arXiv preprint arXiv:2505.09388},
  year={2025}
}
```

---

## 行动清单

1. **紧急**: 修正 8 个错误 first author 的 bib 条目（见 Part A-fix）
2. **紧急**: 同步更新 .tex 文件中对应的 `\cite{}` key
3. **W6 响应**: 将 Part B 的 5 个 BibTeX 条目添加到 references.bib
4. **Qwen3**: 如论文用了 Qwen3 模型，增加 Qwen3 报告引用
5. **CWM**: 考虑将 `{Meta AI}` 改为完整作者列表或 `{{FAIR CodeGen Team} and Copet, Jade and others}`
