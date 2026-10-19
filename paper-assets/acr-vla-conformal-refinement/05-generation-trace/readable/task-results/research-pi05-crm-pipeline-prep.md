# research pi05 crm pipeline prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi05-crm-pipeline-prep_20260521T110149_result.json`
- **Structured JSON:** [`3de587ce050d102e84bc.json`](../../sessions/3d/3de587ce050d102e84bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已更新至 `artifacts/pi05_crm_pipeline_plan.md`。

关键发现和方案要点：

**当前阻塞**：π0.5 baseline 全线 0% SR，根因不是 vision tower（437 keys 已修），而是 **language_model + multi_modal_projector 的 376 个 key 仍然 missing**，导致 LM 在随机权重下运行。官方 lerobot-eval patched 版 3/3 = 100%，证明模型有效。

**Pipeline 5 步**：
1. **Step 0**：修复 376 key remap → 验证 missing_keys=0 + quick verify SR > 0%（阻塞性）
2. **Step 1**：重跑 baseline eval（3 seeds × 2 benchmarks，6 GPU 并行，~8h）
3. **Step 2**：Precompute π0.5 features（obs_dim=2048，K=1，~2h）
4. **Step 3**：训练 obs_dim=2048 的新 CRM（~30-40 min，~580K params）
5. **Step 4**：CRM + π0.5 eval（6 experiments，~8h）

**核心决策**：采用方案 A（obs_dim=2048 新 CRM），不复用 SmolVLA CRM；第一版只用 single obs feature，不做 multi-scale；总 wallclock 约 10-12h（并行优化后）。

---
