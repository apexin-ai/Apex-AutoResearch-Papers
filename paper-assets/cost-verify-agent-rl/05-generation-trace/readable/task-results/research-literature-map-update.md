# research literature map update

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_map_update_20260515T190618_result.json`
- **Structured JSON:** [`6545d9d822d51cd54b8a.json`](../../sessions/65/6545d9d822d51cd54b8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已更新。修改项汇总：

### 1. ARES (yang2026ares) — 描述修正
- relevance_note 重写：明确 ARES 使用 SFT 初始化 + GRPO 精调（非纯 SFT router）
- 差异化描述改为：(1) reward signal — ARES 用 token efficiency reward，B-IAVR 用 action-change signal；(2) data requirement — ARES 需 difficulty-annotated training data

### 2. AgentPRM 两条目修正
- **xi2025agentprm**: title 更正为完整标题 "...via Step-Wise Promise and Progress"；relevance_note 改为独立工作描述（TD+GAE approach），移除 "extending" 措辞
- **choudhury2025agentprm**: 保持不变，已正确
- ACM Web Conference 2026 venue 经搜索确认正确

### 3. 引用错误修正
- **huang2024self-correction-survey → kamoi2024self-correction-survey**: id 前缀从 "huang" 改为 "kamoi"（实际第一作者是 Ryo Kamoi）
- **dapo2025**: authors 从 "ByteDance/Tsinghua" 改为 "Yu et al."（第一作者 Qiying Yu），标题确认正确
- **cfgm2025**: venue EMNLP 2025 确认正确
- **wei2025webagent-r1**: 第一作者确认为 Zhepei Wei，"wei" key 正确

### 4. 补充 arXiv ID（原 null）
| 条目 | arXiv ID |
|------|----------|
| tie2025correctbench | 2510.16062 |
| spear2025 | 2509.22601 |
| wei2025webagent-r1 | 2505.16421 |
| digiRL2024 | 2406.11896 |
| wan2025derailer-rerailer | 2408.13940 |
| tu2025autothink | 2505.10832 |
| xiang2024retrospex | 2505.11807 |
| cfgm2025 | 2508.15305 |

### 5. 补充 authors（原 null）
| 条目 | authors |
|------|---------|
| self-verification-dilemma-2026 | Long et al. |
| mar2025 | Ozer et al. |
| ssr2025 | Shi et al. |
| selfguide2026 | Wang et al. |
| digiRL2024 | Bai et al. |
| agentic-rl-survey-2025 | Zhang et al. |
| cfgm2025 | Yang et al. |
| respact2024 | Dongre et al. |

### 6. 附带修正
- **he2025correctbench → tie2025correctbench**: id/authors/title 全部更正（实际第一作者 Guiyao Tie，非 He）
- **tu2025autothink**: title 更正为论文实际标题 "Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL"
- **mar2025/ssr2025**: title 补全为 arXiv 完整标题
- **spear2025**: authors 从 "Tencent"（机构）改为 "Qin et al."（第一作者 Yulei Qin）

---
