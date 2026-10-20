# research literature verify

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-verify_20260512T110045_result.json`
- **Structured JSON:** [`ae23a7b26401ff4224f6.json`](../../sessions/ae/ae23a7b26401ff4224f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入，ROADMAP 已更新。核心结论：

**文献真实性**:
| 论文 | 状态 |
|------|------|
| R2GRPO (2505.22068) | ✅ 存在，所有声称准确 |
| ProUIE (2604.10633) | ✅ 存在，SFR 纯结构奖励，无 evidence 维度 |
| EAPO (2601.10306) | ✅ 存在，但做长上下文推理非 IE |
| Ground-GRPO | ❌ 不存在 |
| MORE-R1 (2603.09478) | ✅ 存在，多模态 RE |
| LAT | ❌ 未找到 |

**关键发现**:
1. **ProvUIE 与 ProUIE 的差异化成立** — ProUIE 的 SFR 不含任何 evidence/faithfulness 维度，仅衡量结构正确性
2. **R2GRPO 真实存在** — 审稿人找不到可能因 2025.5 提交时索引延迟
3. **必须删除** Ground-GRPO 和 LAT 两个不存在的引用
4. **新威胁: MR-UIE (arXiv 2509.09082)** — UIE + RL 复合奖励中已有 faithfulness 维度 + "evidence-first" prompting，与 ProvUIE novelty 存在潜在重叠，**需优先阅读原文评估**

完整报告: `artifacts/literature_verification_report.md`

---
