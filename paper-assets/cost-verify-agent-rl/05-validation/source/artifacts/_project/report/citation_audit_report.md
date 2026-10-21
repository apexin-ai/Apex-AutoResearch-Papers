# Citation Audit Report

> Audit date: 2026-05-15
> Scope: literature_map.yaml (28 papers) + related_work_survey.md
> Method: WebSearch verification of arXiv ID → title → authors

---

## 1. Priority Papers (7 papers)

| 论文 | 声称 arXiv ID | 声称作者 | 验证结果 | 正确信息/备注 |
|------|-------------|---------|---------|--------------|
| ARES | 2603.07915 | Yang et al. | ✅ | ID、标题、作者均正确。Jingbo Yang et al. |
| AgentPRM (Choudhury) | 2502.10325 | Choudhury et al. | ❌ 标题/作者 | 实际标题: "Process Reward Models for LLM Agents: Practical Framework and Directions"（无 "AgentPRM" 前缀）。单一作者 Sanjiban Choudhury，非 "et al."。Survey 中错写为 "Chatterjee et al." |
| CorrectBench | 2510.16062 | Tie et al. (map) / He et al. (survey) | ⚠️ Survey 作者错 | ID 正确。literature_map "Tie et al." 正确（首作 Guiyao Tie）。Survey 错写为 "He et al." |
| AutoThink | 2505.10832 | Tu et al. | ✅ | ID、标题、作者均正确。Songjun Tu et al. |
| Self-Guide | 2604.03098 | Wang et al. | ✅ | ID、标题、作者均正确。Xinyu Wang et al. |
| Thinkless | 2505.13379 | Du et al. | ❌ 作者 | ID 和标题正确。但首作是 Gongfan Fang，应为 **"Fang et al."**，非 "Du et al." |
| ReflAct | 2505.15182 | Kim et al. | ✅ | ID、标题、作者均正确。Jeonghye Kim et al. |

---

## 2. Sampled Papers (11 papers)

| 论文 | 声称 arXiv ID | 声称作者 | 验证结果 | 正确信息/备注 |
|------|-------------|---------|---------|--------------|
| Self-Correction Survey | 2406.01297 | Kamoi et al. (map) / Huang et al. (survey) | ⚠️ Survey 作者错 | ID 正确。literature_map "Kamoi et al." 正确（Ryo Kamoi）。Survey 错写为 "Huang et al." |
| GiGPO | 2505.10978 | Feng et al. | ✅ | ID、标题、作者均正确。Lang Feng et al. |
| SPEAR | 2509.22601 | Qin et al. | ⚠️ 标题不精确 | ID 和作者正确（Yulei Qin）。实际标题: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"，非 "SPEAR: Self-Imitation with..." |
| Self-Verification Dilemma | 2602.03485 | Long et al. | ✅ | ID、标题、作者均正确。Quanyu Long et al. |
| Derailer-Rerailer | 2408.13940 | Wan et al. | ✅ | ID 正确，ACL 2025 Findings 确认。Guangya Wan et al. |
| Sherlock | 2511.00330 | Microsoft | ✅ | ID、标题正确。Microsoft Research 确认。 |
| ReSpAct | 2411.00927 | Dongre et al. | ✅ | ID、标题、作者均正确。Vardhan Dongre et al. |
| WebAgent-R1 | 2505.16421 | Wei et al. (map) / Pei et al. (survey) | ⚠️ Survey 作者错 | ID 正确。literature_map "Wei et al." 正确（Zhepei Wei）。Survey 错写为 "Pei et al." |
| Retrospex | 2505.11807 | Xiang et al. | ✅ | ID 正确。Yufei Xiang et al. EMNLP 2024 确认。 |
| CFGM | 2508.15305 | Yang et al. | ✅ | ID 正确。EMNLP 2025 确认。 |
| AgentPRM (Xi) | 2511.08325 | Xi et al. | ✅ | ID、标题、作者均正确。Zhiheng Xi et al. |

---

## 3. 错误汇总

### literature_map.yaml 中的错误

| # | 错误类型 | 条目 | 错误内容 | 应改为 |
|---|---------|------|---------|-------|
| 1 | ❌ 作者 | `du2025thinkless` | `authors: "Du et al."` | `authors: "Fang et al."` (Gongfan Fang, Xinyin Ma, Xinchao Wang) |
| 2 | ❌ 标题 | `choudhury2025agentprm` | `title: "AgentPRM: Process Reward Models for LLM Agents"` | `title: "Process Reward Models for LLM Agents: Practical Framework and Directions"` |
| 3 | ⚠️ 作者 | `choudhury2025agentprm` | `authors: "Choudhury et al."` | `authors: "Choudhury"` (单一作者 Sanjiban Choudhury) |
| 4 | ⚠️ 标题 | `spear2025` | `title: "SPEAR: Self-Imitation with Progressive Exploration for Agentic RL"` | `title: "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"` |

### related_work_survey.md 中的错误

| # | 错误类型 | 位置 | 错误内容 | 应改为 |
|---|---------|------|---------|-------|
| 5 | ❌ 作者 | CorrectBench 条目 | "He et al., 2025" | "Tie et al., 2025" (Guiyao Tie) |
| 6 | ❌ 作者 | Self-Correction Survey 条目 | "Huang et al., 2024" | "Kamoi et al., 2024" (Ryo Kamoi) |
| 7 | ❌ 作者 | WebAgent-R1 条目 | "Pei et al., 2025" | "Wei et al., 2025" (Zhepei Wei) |
| 8 | ❌ 作者 | AgentPRM 条目 | "Chatterjee et al., 2025" | "Choudhury, 2025" (Sanjiban Choudhury) |

---

## 4. 未验证论文（剩余 10 篇）

以下论文未做抽样验证（arXiv ID 未逐一 WebSearch 确认），建议后续补验：

- Incentivize Self-Verify (2506.01369, Zhang et al.)
- MAR (2512.20845, Ozer et al.)
- SSR (2511.10621, Shi et al.)
- DAPO (2503.14476, Yu et al.)
- DigiRL (2406.11896, Bai et al.)
- SORL (2511.20718, Li et al.)
- Agentic RL Survey (2509.02547, Zhang et al.)
- When To Solve, When To Verify (2504.01005, Singhi et al.)
- Efficient Agents (2508.02694, Wang et al.)
- Trust but Verify (2508.16665, Venktesh et al.)

---

## 5. 总结

- **已验证**: 18/28 篇（7 重点 + 11 抽样）
- **arXiv ID 全部真实**: 所有已验证论文的 arXiv ID 均指向真实论文，无编造 ID
- **发现 8 处错误**: 4 处在 literature_map.yaml，4 处在 related_work_survey.md
- **主要问题类型**: 作者姓名错误（6 处）、标题不准确（2 处）
- **无 arXiv ID 错误**: 所有 ID 均正确映射到对应论文
