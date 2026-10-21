# paper writing claim3

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_claim3_20260526T161705_result.json`
- **Structured JSON:** [`a47361b3eadb6dcef95d.json`](../../sessions/a4/a47361b3eadb6dcef95d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。主要变更：

1. **标题和结构**：`\section{Avoidance Source Diagnosis}` + 两个 subsection (TSR Collapse Mechanism, Dose-Response at Higher Loss Weights)
2. **Block 1**: 更新 CAR 数据 (54.5/54.5/56.3)，新增 null distribution 分析 (mean=55.3%, std=2.13%, λ=0.01 在 0.5σ 内)，新增 Phase 2 λ=0 ablation (CAR=57.5%)，归因至 collision-free demo data (+28pp)
3. **Block 2**: TSR 崩塌 74.7%→6.3-6.8%，三条证据诊断 catastrophic forgetting (EE motion retained, obstacle disp 0.143→0.059m, safe failure rate 100× 增加)，SDF TSR 仅高 0.2-0.5pp (within noise，未 claim improvement)
4. **Block 3**: `\placeholder` 标记 λ=0.1 pending，三种 scenario (a/b/c)，Lambda-CAR figure fbox placeholder
5. **措辞约束**: 全文用 "does not improve beyond LoRA-only (p>0.1)"，无 em-dash，无 -ing phrase 结尾，SDF01 seeds 更新为 3

---
