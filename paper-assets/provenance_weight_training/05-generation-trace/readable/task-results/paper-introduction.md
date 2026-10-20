# paper introduction

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_introduction_20260515T233432_result.json`
- **Structured JSON:** [`2cb3531f103ebed622fe.json`](../../sessions/2c/2cb3531f103ebed622fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

720 words (including LaTeX markup), within the ~600-700 target range. `register_artifact` is not available as a tool or command — the file is written to the artifacts directory.

**产出**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction_draft.md`

**结构**:
- **P1**: 问题动机 — web 语料合成污染 + model collapse（Shumailov, Dohmatob）
- **P2**: 现有方法不足 — Drayson 的 b 需 grid search，He 的 Golden Ratio 需已知比例，hard filtering 丢弃边界样本
- **P3**: 方法核心 — dual-constrained adaptive b*，α_eff 质量下界 + ESS 稳定上界 + 最小干预原则（Wang 2026 理论动机）
- **P4**: 最小干预 vs 最大干预的实证区分（40% α_eff binding, b*=1.67 vs ESS-only 4.15）
- **P5**: 实验结果 — adaptive 17.651 匹配 grid-best 17.646，ESS-only 17.722 劣于 uniform 17.694，轻量检测器即可
- **P6**: 三点 contributions

所有必需引用（Drayson, Shumailov, Dohmatob, Wang, He）均已包含，使用 `\citet{}`/`\citep{}` 格式。数据与任务指定完全一致。

---
