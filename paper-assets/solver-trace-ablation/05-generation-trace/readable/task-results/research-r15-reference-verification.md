# research r15 reference verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r15-reference-verification_20260520T044621_result.json`
- **Structured JSON:** [`7d0861ab74b87486e629.json`](../../sessions/7d/7d0861ab74b87486e629.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是结果：

---

## [1] LLMs Gaming Verifiers — arXiv:2604.15149

- **完整标题**: LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking
- **作者**: Lukas Helff, Quentin Delfosse, David Steinmann, Ruben Härle, Hikaru Shindo, Patrick Schramowski, Wolfgang Stammer, Kristian Kersting, Felix Friedrich
- **年份**: 2026
- **Venue**: arXiv preprint / LLM Reasoning Workshop @ ICLR 2026
- **验证状态**: ✅ 论文存在，信息正确
- **Bib 状态**: ❌ 不在 references.bib 中，也未在任何 .tex 文件中引用
- **BibTeX entry**:
```bibtex
@article{helff2026gaming,
  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
  journal      = {arXiv preprint arXiv:2604.15149},
  year         = {2026},
  eprint       = {2604.15149},
  archivePrefix = {arXiv},
}
```

---

## [2] Countdown-Code — arXiv:2603.07084

- **完整标题**: Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR
- **作者**: Muhammad Khalifa, Zohaib Khan, Omer Tafveez, Hao Peng, Lu Wang
- **年份**: 2026
- **Venue**: arXiv preprint
- **验证状态**: ✅ 论文存在，信息正确
- **Bib 状态**: ❌ 不在 references.bib 中，也未在任何 .tex 文件中引用
- **BibTeX entry**:
```bibtex
@article{khalifa2026countdown,
  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
  journal      = {arXiv preprint arXiv:2603.07084},
  year         = {2026},
  eprint       = {2603.07084},
  archivePrefix = {arXiv},
}
```

---

## [3] Uesato et al. (2022) — arXiv:2211.14275

- **完整标题**: Solving math word problems with process- and outcome-based feedback
- **作者**: Jonathan Uesato, Nate Kushman, **Ramana** Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, Irina Higgins
- **年份**: 2022
- **Venue**: NeurIPS 2022 Workshop on MATH-AI
- **验证状态**: ⚠️ 需修正 — bib 中作者写成 **"Ramesh"** Kumar，应为 **"Ramana"** Kumar
- **Bib 状态**: 已有 (`uesato2022solving`, L396-401)，需修正作者名
- **修正**:
```diff
- author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramesh and ...}
+ author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and ...}
```

---

## [4] Cobbe et al. (2021) — arXiv:2110.14168

- **完整标题**: Training Verifiers to Solve Math Word Problems
- **作者**: Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, **Heewoo** Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, John Schulman
- **年份**: 2021
- **Venue**: arXiv preprint (未正式发表于会议)
- **验证状态**: ⚠️ 需修正 — bib 中作者写成 **"Heather Jun"**，应为 **"Heewoo Jun"**
- **Bib 状态**: 已有 (`cobbe2021training`, L509-514)，需修正作者名
- **修正**:
```diff
- author={... and Heather Jun and ...}
+ author={... and Heewoo Jun and ...}
```

---

## 汇总

| # | 论文 | 存在性 | Bib 状态 | 需修正 |
|---|------|--------|----------|--------|
| 1 | LLMs Gaming Verifiers | ✅ | ❌ 缺失 | 需添加 entry |
| 2 | Countdown-Code | ✅ | ❌ 缺失 | 需添加 entry |
| 3 | Uesato 2022 | ✅ | ⚠️ 有 | Kumar, Ramesh → Ramana |
| 4 | Cobbe 2021 | ✅ | ⚠️ 有 | Heather Jun → Heewoo Jun |

Sources:
- [arXiv:2604.15149](https://arxiv.org/abs/2604.15149)
- [arXiv:2603.07084](https://arxiv.org/abs/2603.07084)
- [arXiv:2211.14275](https://arxiv.org/abs/2211.14275)
- [arXiv:2110.14168](https://arxiv.org/abs/2110.14168)
- [DBLP: Heewoo Jun](https://dblp.org/pid/200/8045.html)

---
