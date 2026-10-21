# diagnose scienceworld grpo cell c v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scienceworld_grpo_cell_c_v4_20260522T040906_result.json`
- **Structured JSON:** [`936c921674d6185f0318.json`](../../sessions/93/936c921674d6185f0318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diag_scienceworld_v4.md`。

**核心发现**：

1. **Validation 完成了**（174秒，32 episodes），但 success=0%，final_score=4.84/10
2. **训练步骤 0 的 rollout 阶段 silent crash**——进程在 `agent_proxy.rollout(batch, val=False)` 内部死亡，无 Python traceback
3. **WorkerDict 仍在 GPU 上运行**（pid=389842/389843，各占 37.6GB），证明是 TaskRunner 崩溃而非 GPU worker
4. **stderr 未被捕获**——主日志只记录 stdout，真正的错误丢失
5. **发现严重架构缺陷**：`env.py` 中 128 个 ScienceWorld 环境共享一个 JVM 对象（per-thread cache），`step()` 调用在错误的游戏状态上执行。这解释了 validation success=0%，也可能导致 JVM 崩溃

**最高优先级操作**：
- 清理 GPU 上残留的 Ray worker 进程
- 修复日志捕获（`2>&1`）以便下次崩溃能看到 traceback
- 修复 JVM 共享 bug（每个 env 实例需要独立 JVM，或在 step 前 reload 游戏状态）

---
