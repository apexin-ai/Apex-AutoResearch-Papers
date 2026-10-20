# agent / loop_8.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`2ce925ee825325a47f18.json`](../../sessions/2c/2ce925ee825325a47f18.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T01:29:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只分配 westc-26893:cuda:0，禁止用其他 GPU
- 服务器别名已从 autodl-4090d 改为 westc-26893，所有 SSH/cron 必须用新名
- exp-006 已 timeout 失败 2 次（EXIT_CODE=124），第三次重跑必须去掉所有 timeout wrapper，且确认 tmux session 不会被系统清理
- AutoDL 实例需 `source /etc/network_turbo` 才能访问外网；HF 下载必须设 `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量
- 环境用 conda（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不要创建 venv

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893（AutoDL 4090D 24GB），工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct`
- 其他模型：Pythia-1.4B `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b`，OLMo-1B `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf`
- 数据：`/root/autodl-tmp/gen-depth-contamination/data_exp0*` 各实验数据目录，depth_corpus_30k 在 `data/depth_corpus_30k`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：无（全部 DONE）。有一个刚派出的诊断 Worker `worker_diagnose_exp_006_graduated_filtering_v2_20260514T213308` 正在 SSH 诊断 exp-006 失败原因，尚未回调

### 3. 📊 当前状态
**刚做完**：收到 exp-006 第二次失败的 cron 回调，完成 session 初始化（read_registry + reconcile_crons），派出诊断 Worker 去 westc-26893 查日志。

**Registry 全景**：12 实验全部 DONE（10 success + 2 failed）
- exp_006_graduated_filtering: **DONE/failed** — 第二次 EXIT_CODE=124 timeout。第一次跑完 32/50 runs，恢复后 18 runs 状态未知。诊断 Worker 正在查
- exp_015_neural_probe: **DONE/failed** — GPU OOM（与 exp-006 争显存）。K*(neural)=3 仅 Qwen-cont 单数据集，需独占 GPU 重跑
- 其他 10 个实验全部 success

**等待中**：
- Worker `worker_diagnose_exp_006_graduated_filtering_v2_20260514T213308` 回调 → 拿到失败原因 + 已完成 runs 数 + 未完成列表
- 诊断完成后需向 Director 汇报并决策 exp-006 第三次重跑方案

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 根据结果更新 registry notes/failure_reason → 向 Director 汇报（带 [资源] 行）→ 制定 exp-006 第三次重跑方案（建议拆分小批次避免 timeout）
- exp-006 最终完成 → **C3 叙事决策点**：graduated > binary-ours 则写 positive C3；否则切 D013 fallback story（负向 implication）。中间结果预警：前 22 runs graduated(α=0.1,0.3) 均不如 binary-ours（MMLU -0.53~-0.68pp），α≥0.5 + surprisal + dsir 是翻盘希望
- exp-006 完成且 GPU 空闲 → 立即启动 exp-015 neural probe 重跑（独占 GPU，~1h，3 数据集 + bootstrap CI + permutation test）
- exp-015 完成 → 立即启动 exp-004 7B cross-scale（~3h）
- 全部实验完成 → Discussion + Conclusion 定稿 → re-dream → Reviewer 审查 → 05-25 ARR 提交

### 5. 🎯 战略上下文
- **核心结论**：K*=2 跨 8 条件（4 模型 × 2 generation modes × 4 decoding configs）稳定不变（D016 universality）。Neural probe K*(neural)=3 说明 K*=2 是 15D features 的操作下界而非信息论极限（D019/D020）
- **论文结构**：2+1 claim（D012）。C1' = K* characterization（4 子组件 a-d 全 ✅）。C3 = graduated filtering（**悬而未决**）。Supporting: LLM zero-shot + decoding ablation
- **C3 是当前最大风险**：中间结果 graduated < binary-ours，如果 α≥0.5/surprisal/dsir 也不行，必须走 D013 fallback（负向 implication story："K*=2 意味着 graduated filtering 无法超越 binary"）。此时需按 red-section skill 产 Framing 调整提案，禁止默默跑下一个实验
- **易错点**：
  - exp-006 脚本有 skip logic（检查 eval_results.json），重跑时不需要从头开始，但要确认之前的结果文件没有损坏
  - exp-015 重跑必须等 exp-006 完成/GPU 空闲，两者同时跑会 OOM（15.5GB + 9GB > 24GB）
  - 论文中 K*(neural)=3 被引用 4+ 次但数据仅来自 Qwen-cont 单模型，在 exp-015 重跑确认前要标注 "pending"
- **DDL**：05-25 ARR，剩 10 天。exp-006 + exp-015 + exp-004 约 25h GPU 时间，时间紧但可行


---
