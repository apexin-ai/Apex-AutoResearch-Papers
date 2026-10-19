# paper restructure 3claims

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_restructure_3claims_20260526T053244_result.json`
- **Structured JSON:** [`a643cb2e96e4d7ebee2c.json`](../../sessions/a6/a643cb2e96e4d7ebee2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Only `analysis_claim4.tex` still contains old references, but it's no longer `\input`-ed from `main.tex` so it's a dead file. All active tex files are clean.

Restructuring complete. Summary:

### 改动摘要

| 文件 | 改动 |
|------|------|
| `analysis_claim1.tex` | 末尾追加 capability-safety observation 段落（从旧 claim2 合并），更新 sec:a1_pi05 → sec:avoidance_source |
| `analysis_claim2.tex` | 完全替换为旧 claim3 内容（EE-only SDF limitation），更新两处交叉引用 |
| `analysis_claim3.tex` | 完全替换为新 Claim 3 骨架（avoidance source diagnosis），含确认的 low-λ 数据表、TSR collapse 机制分析、λ=0.1 placeholder |
| `analysis_claim4.tex` | 保留但不再被 main.tex 引用（dead file） |
| `main.tex` | TSR-CAR scatter 图移到 displacement 图之后（都属于 Claim 1）；删除 `\input{analysis_claim4}`；\input 顺序: claim1 → claim2 → claim3 |
| `introduction.tex` | 贡献列表从 4 条重组为 3 条：C1 合并 capability-safety 观察，C2 EE-only，C3 avoidance source diagnosis |
| `discussion.tex` | 更新 3 处交叉引用（sec:tsr_car → sec:fake_safety, sec:a1_pi05 → sec:avoidance_source 和 sec:ee_only） |
| `experimental_framework.tex` | sec:a1_pi05 → sec:avoidance_source |

### 新结构对应关系

| 文件 | Claim | 内容 |
|------|-------|------|
| `analysis_claim1.tex` | Claim 1: CAR Metric Contaminated | Fake safety 主证据 (A1 800ep) + dfCAR metric + capability-safety observation (Pi0 vs Pi0.5 TSR-CAR) |
| `analysis_claim2.tex` | Claim 2: EE-only Structural Limitation | 3 GT SDF oracle 均劣于 baseline + arm-body collision 分析 |
| `analysis_claim3.tex` | Claim 3: Avoidance Source Diagnosis | LoRA-only CAR=55.3% ≈ SDF CAR=50.5-52.8% + TSR collapse 复合机制 + λ=0.1 placeholder |

---
