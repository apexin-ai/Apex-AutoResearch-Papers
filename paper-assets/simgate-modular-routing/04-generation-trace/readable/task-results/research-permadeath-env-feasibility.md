# research permadeath env feasibility

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_permadeath-env-feasibility_20260518T034021_result.json`
- **Structured JSON:** [`f00dcdeb3d0b02edeb58.json`](../../sessions/f0/f00dcdeb3d0b02edeb58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/permadeath_env_feasibility.md`。

**结论**：

**推荐 Crafter**，理由：
1. LLM agent 实际能跑（BALROG ~33% 里程碑完成率），episode 有信息量
2. 死亡率在合理区间（LLM ~60-80%，启发式 agent ~20-40%），能产生 DAF 信号
3. 语义地图 (64x64) + 完整 inventory dict = 可直接构建 heuristic "oracle"
4. Episode ~500-1000 步，pilot 成本可控（~$10 API）
5. 安装一行 pip，纯 Python

**不推荐 NetHack**：虽然 AutoAscend 是完美的 deterministic modality，但 LLM agent 表现太差（~1.5%），episode 太短/无信息量，且单 episode 代价极高（10^4+ LLM calls）。

**Pilot 方案**：50 episodes（25 LLM + 25 heuristic），5-7 天工作量。最大风险是 heuristic agent 与 LLM 的死亡率对比不够显著，可通过调节 heuristic 强度缓解。

---
