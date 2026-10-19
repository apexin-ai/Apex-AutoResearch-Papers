# Citation Verification Report

Date: 2026-05-17

## hcapo2026
- Status: **REAL**
- Title found: "Hindsight Credit Assignment for Long-Horizon LLM Agents"
- Authors found: Hui-Ze Tan, Xiao-Wen Yang, Hao Chen, Jie-Jing Shao, Yi Wen, Yuteng Shen, Weihong Luo, Xiku Du, Lan-Zhe Guo, Yu-Feng Li
- Venue: arXiv preprint (March 2026)
- arXiv ID: 2603.08754 (confirmed)
- Evidence: https://arxiv.org/abs/2603.08754
- Notes: Title on arXiv omits "HCAPO:" prefix (HCAPO is the framework name within the paper). "Tan et al." is correct (first author: Hui-Ze Tan).

## skillmaster2026
- Status: **REAL**
- Title found: "SkillMaster: Toward Autonomous Skill Mastery in LLM Agents"
- Authors found: Min Yang, Jinghua Piao, et al. (Shandong University, Zhongguancun Academy, Tsinghua University, Southeast University, USTC)
- Venue: arXiv preprint (May 2026)
- arXiv ID: 2605.08693 (confirmed)
- Evidence: https://arxiv.org/abs/2605.08693
- Notes: Exact title match. "Yang et al." is correct (first author: Min Yang). Code at https://github.com/sduyangmin/Skill-Master

## selfbudgeter2026
- Status: **REAL**
- Title found: "SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning"
- Authors found: Zheng Li, Qingxiu Dong, Jingyuan Ma, Di Zhang, Kai Jia, Zhifang Sui
- Venue: arXiv preprint (May 2025), under review at ICLR 2026
- arXiv ID: 2505.11274 (confirmed)
- Evidence: https://arxiv.org/abs/2505.11274 ; https://openreview.net/forum?id=e7EBzbi8Qd
- Notes: Citation key says "2026" but arXiv submission date is May 2025. The paper is under review at ICLR 2026 per OpenReview. Recommend using year 2025 for the citation key or noting venue as "ICLR 2026 (under review)". "Li et al." is correct (first author: Zheng Li).

## yang2026ares
- Status: **REAL**
- Title found: "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
- Authors found: Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, Shiyu Chang
- Venue: arXiv preprint (March 2026)
- arXiv ID: 2603.07915 (confirmed)
- Evidence: https://arxiv.org/abs/2603.07915 ; https://github.com/UCSB-NLP-Chang/Ares
- Notes: Exact title match (arXiv capitalizes as "Ares" not "ARES"). "Yang et al." is correct (first author: Jingbo Yang). From UCSB NLP Chang group.

## agent-omit2026
- Status: **REAL**
- Title found: "Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic Reinforcement Learning"
- Authors found: Yansong Ning, Jun Fang, Naiqiang Tan, Hao Liu
- Venue: arXiv preprint (February 2026)
- arXiv ID: 2602.04284 (confirmed)
- Evidence: https://arxiv.org/abs/2602.04284 ; https://github.com/usail-hkust/Agent-Omit
- Notes: Exact title match. "Ning et al." is correct (first author: Yansong Ning). From HKUST.

## yao2023react
- Status: **REAL**
- Title found: "ReAct: Synergizing Reasoning and Acting in Language Models"
- Authors found: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- Venue: ICLR 2023 (Notable Top 5% paper)
- arXiv ID: 2210.03629
- Evidence: https://arxiv.org/abs/2210.03629 ; https://openreview.net/forum?id=WE_vluYUL-X ; https://react-lm.github.io/
- Notes: Seminal paper in LLM agent research. "Yao et al." correct. From Princeton / Google.

### BibTeX entry:

```bibtex
@inproceedings{yao2023react,
  title     = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2023},
  url       = {https://arxiv.org/abs/2210.03629}
}
```

---

## Summary

| Citation Key | Status | arXiv ID | Notes |
|---|---|---|---|
| hcapo2026 | REAL | 2603.08754 | Title prefix "HCAPO:" not in arXiv title |
| skillmaster2026 | REAL | 2605.08693 | Exact match |
| selfbudgeter2026 | REAL | 2505.11274 | Year should be 2025 (submitted May 2025, under review ICLR 2026) |
| yang2026ares | REAL | 2603.07915 | Exact match |
| agent-omit2026 | REAL | 2602.04284 | Exact match |
| yao2023react | REAL | 2210.03629 | ICLR 2023, Notable Top 5% |

**Result: All 6 citations are REAL. No hallucinated papers found.**

Minor issues to fix:
1. `selfbudgeter2026` — consider changing citation year to 2025 (arXiv date) or adding "under review" note
2. `hcapo2026` — if citing with "HCAPO:" prefix in title, use braces in BibTeX to preserve capitalization
