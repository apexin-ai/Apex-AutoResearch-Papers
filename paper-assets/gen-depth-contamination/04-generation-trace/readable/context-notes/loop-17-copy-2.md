# reviewer / loop_17.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`998b2a8868ff23986025.json`](../../sessions/99/998b2a8868ff23986025.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-19T09:15:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-22115 全名必须带端口号，ssh_read_only 用 "cqa1" 会失败
- ssh_read_only 不支持 shell metacharacters（`&&`, `|`, `>`, `$()`）和 `git` 命令
- exp_code_llama8b registry 仍为 conclusion=failed，metrics 缺失——已连续 3 次审查报告要求 Agent 修正，下一轮若仍未改应升级为 critical
- code_crossmodel_table.tex（两个副本）LLaMA-8B 列仍为 TBD，同样连续未修
- pp 单位换算：1pp = 0.01，历史上两次犯 10× 错误（见 memory feedback_pp_unit_conversion.md），报告前必须二次核验

### 2. 🖥️ 基础设施快照
- **cqa1-22115** (root): `/root/autodl-tmp/gen-depth-contamination`
  - 4× 4090D (24GB each)
  - cuda:0 空闲, cuda:1 exp_code_qwen7b, cuda:2 空闲, cuda:3 exp_code_mistral7b
  - 模型缓存: `/root/autodl-tmp/.hf_cache/` (Qwen2.5-1.5B, LLaMA-3.1-8B, Mistral-7B, Pythia-1.4B, Qwen2.5-7B; 无 base Qwen2.5-14B)
  - 磁盘剩余 ~150GB
- **westd-42896** (root): 同项目路径, cuda:1 跑 exp_32b_c4
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- registry / ROADMAP / paper_framing.md / decisions.yaml 均在本地 workspace
- 论文: `docs/paper/` (28 页, 正文 ≤8 页, 编译通过)

### 3. 📊 当前状态
**刚完成**：
- exp_code_qwen1b5_pythia_scorer 审查 PASS (K*=2 cross-scorer confirmed, D079)
- exp_code_llama8b 失败审查 + diagnostic worker 审查 (K*=2 confirmed, D080)
- ROADMAP 审查：Pythia AUC 0.5765→0.5983 修正已确认

**RUNNING 实验**：
| exp_id | server | gpu | ETA |
|--------|--------|-----|-----|
| exp_code_mistral7b | cqa1 | cuda:3 | ~May 19 11:00 UTC |
| exp_code_qwen7b | cqa1 | cuda:1 | ~May 19 18:00 UTC |
| exp_32b_c4 | westd | cuda:1 | ~May 20-21 |

**Dream simulation** dream_20260519T090934 正在 imagining 阶段（full review mode）

**等待中**: Mistral/Qwen-7B Code 完成的 cron 回调

### 4. 📋 待办
- exp_code_mistral7b cron 回调 → 审查结果，核对 registry metrics vs remote summary.txt，验证 K* 值
- exp_code_qwen7b cron 回调 → 同上；5/5 Code 模型完成后审查最终 code_crossmodel_table.tex 是否完整
- dream_20260519T090934 完成 → 审查 dream review 结论，检查 claim-evidence 匹配度
- exp_32b_c4 完成 → 审查 32B scale C4 K*（预期 K*=2），验证 GPU 合规 westd cuda:1
- 若 Agent 仍未修正 exp_code_llama8b registry（conclusion=failed→success + metrics）→ 升级为 critical
- 若 code_crossmodel_table.tex 仍为 TBD → 在 Round 11 内审前升级为 critical

### 5. 🎯 战略上下文
- **核心框架**: Plan C "domain ceiling + model competence" (D076)。Domain hierarchy: Wiki=1, C4=Code=2, arXiv=3。K* 由域复杂度设上界，模型能力决定能否触及上界
- **决策链**: D072(Code域启动) → D073(OLMo放弃) → D074(4域矩阵) → D075(Pythia K*=1暂不改framing) → D076(Plan C) → D077/D078(Retrain K*=7双家族) → D079(Cross-scorer Code K*=2) → D080(LLaMA Code K*=2)
- **DDL**: EMNLP 2026 May 25，6 天
- **易错点**:
  1. Pythia Code 1v2 AUC=0.5983 极其 borderline（仅 -0.17pp below θ=0.60，3/5 折 > 0.60）。论文中 "competence-limited" 叙事要谨慎，不能说 "clearly below"
  2. arXiv cross-scorer: Qwen-7B scorer 下 K* 从 3 降到 2（exp_arXiv_qwen7b_crossscorer, 2v3 AUC=0.5989），同家族 bias ~0.027。其他 arXiv cross-scorer K*=3 稳定。论文需小心措辞
  3. read_registry 的 exp_id filter 经常返回空（可能是 API 的 key vs field 问题），用 status filter + limit 更可靠
  4. Worker 声称 "已更新" 但实际未执行的情况已发生 2 次（registry + LaTeX），务必独立验证


---
