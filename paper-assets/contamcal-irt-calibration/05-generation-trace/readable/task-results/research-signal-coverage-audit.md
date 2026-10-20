# research signal coverage audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_signal_coverage_audit_20260516T005503_result.json`
- **Structured JSON:** [`1d10a9a454655ce7e325.json`](../../sessions/1d/1d10a9a454655ce7e325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**当前 N 值远未达到 IRT pooling 所需的 N >= 16：**
- mmlu: 14（仅 s1+s2）/ 8（s1+s2+s4）
- gsm8k: 12 / 10
- arc: 12 / 10

**三大瓶颈：**

1. **0.5B + 1.5B 的 s123 信号完全空白**（16 个 checkpoint × 3 benchmark，零产出）— SFT checkpoint 都已就绪，只是从未跑 signal。这是最大的 quick win：补上后每个 benchmark 直接 +8 respondents。

2. **s3_constat 系统性缺失** — 全项目仅 3B_d000_v2_s42 有 constat 信号，0.5B/1.5B 从未计算过。需决策：s3 是否为 IRT 必须？

3. **3B s4_selfcritique 不完整** — d000_v2 完全缺 s4，d025_v3 s4_mmlu 在跑（26%，约 1.5h），d100 缺 s4_mmlu，d005 等 SFT 完成。

**运行中实验**：d025_v3_s42 s4_selfcritique 在跑，d005_s42 和 d100_s42 SFT 在跑。

产出已注册：`art_20260516_b3d6af`

---
