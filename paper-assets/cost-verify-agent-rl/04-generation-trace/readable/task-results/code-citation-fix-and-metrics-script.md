# code citation fix and metrics script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_citation_fix_and_metrics_script_20260515T182240_result.json`
- **Structured JSON:** [`7acf04f0f6a8c5e59fca.json`](../../sessions/7a/7acf04f0f6a8c5e59fca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

增量模式正常——第二次运行只输出 header，无重复数据。

现在处理 ROADMAP 的 AgentPRM 拆分。`save_project_file` 不支持写 ROADMAP.md（需要 `update_roadmap` 工具），所以报告需要修改的内容。

---

## 产出报告

### 1. literature_map.yaml 修改清单

| 条目 | 修改内容 |
|------|----------|
| `huang2024self-correction-survey` | authors `"Huang et al."` → `"Kamoi et al."` |
| `feng2025gigpo` (GiGPO) | arxiv_id `null` → `"2505.10978"` |
| `pei2025webagent-r1` | id → `wei2025webagent-r1`, authors `"Pei et al."` → `"Wei et al."` |
| `dapo2025` | title → `"DAPO: An Open-Source LLM Reinforcement Learning System at Scale"` |
| `chatterjee2025agentprm` | **拆分为两条**：(1) `choudhury2025agentprm` (arXiv 2502.10325, 91% ALFWorld) (2) `xi2025agentprm` (arXiv 2511.08325, ACM Web'26) |
| `cfgm2026` | id → `cfgm2025`, venue `"arXiv"` → `"EMNLP 2025"`, year 2026 → 2025 |
| `kim2025reflact` (ReflAct) | arxiv_id `null` → `"2505.15182"` |
| **新增** `du2025thinkless` | Thinkless, arXiv 2505.13379, NeurIPS 2025, direct-competitor |

**未补充 arXiv ID**（任务提及但无具体 ID 提供）：CorrectBench, SPEAR。如有 ID 请告知。

### 2. ROADMAP.md 需要修改

竞争格局表中 AgentPRM 行需拆分为：

```
| Choudhury et al. (2502.10325) | 3B trained PRM | 91% | 不同方向（process reward） |
| Xi et al. (2511.08325, ACM Web'26) | 3B trained PRM | 88-91% | AgentPRM 扩展版 |
```

`save_project_file` 不支持直接写 ROADMAP.md，需通过 `update_roadmap` 工具或手动修改。

### 3. 提取脚本

**路径**：`/root/runs/cost-verify-agent-rl/extract_step_metrics.sh`

**验证输出**：
```csv
step,success,kl_loss,entropy,grad_norm,timestamp
0,0.0625,,,,
1,0.359375,0.05756001640111208,0.2753342390060425,19.440051077315527,4343.20
2,0.1015625,0.4134434908628464,0.3602766990661621,19.310626896098256,10233.23
```

- Step 0 是 val 步（无 actor 指标）
- 支持增量运行（第二次调用无重复输出）
- 自动查找最新 worker log，也可手动指定路径

---
