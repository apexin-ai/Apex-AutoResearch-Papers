# analysis hsweep config check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_hsweep_config_check_20260523T180554_result.json`
- **Structured JSON:** [`778cbbb51af8c09e58c6.json`](../../sessions/77/778cbbb51af8c09e58c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，结果已写入 `artifacts/hsweep_config_analysis.md`。

**核心发现：**

1. **配置一致性问题**：h=20 的 `optimizer_offload=False` 是异常值（其余全为 True），导致 step 1 的 update_actor 花了 4.2h。多 seed 重跑应统一为 True。

2. **实测训练时间**：h=2 约 10-12h/run，h=20 约 20-25h/run（offload=True 估算），15 步。

3. **GPU 问题**：bjb1 nvidia-smi 只显示 **1 张 GPU**，但所有 h-sweep 配置需要 2 张 (`n_gpus_per_node: 2`)。需确认 cuda:1 状态。

4. **30h 不够跑完 8 组**：4 个 h 值 × 2 seeds 串行需要 ~114-138h。推荐方案：
   - **最小可行**：只加跑 h=2 seed3 + h=5 seed2（~22-26h），结合已有 h=2 seed1,2
   - **双机方案**：bjb1 跑 h=2,5，westd-47453 跑 h=10,20，~55h 墙钟可覆盖 4 个 h 值各 2-3 seeds

5. **评测**：训练中 inline eval 用 32-task ID set（满足 C003 的 ≥16 episodes 要求），OOD eval 需单独跑。

---
