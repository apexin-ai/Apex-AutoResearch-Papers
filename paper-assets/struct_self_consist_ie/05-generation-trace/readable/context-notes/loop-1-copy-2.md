# agent / loop_1.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`2414a6f84431a6872d7f.json`](../../sessions/24/2414a6f84431a6872d7f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T11:35:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0/1/2/3 + gpu-5090-4x-2 cuda:0/1/2/3（共 8 张）。白名单外的 GPU 即使 Director 指令也必须 push back
- RE 已确认 FAIL（ρ_sj=0.234 < 0.30 硬截止线），不再做 RE 调参实验。RE 数据仅作论文 Section 5 诊断分析素材
- 项目已进入 research 阶段，新 GPU 实验需等 Director re-dream 审批后才能启动。代码/数据准备可继续
- exp-012 可能有 max_tokens=512 截断问题（Worker 正在检查），如果截断率 >5% 需要用 1024 重跑
- 后续所有推理必须同时输出 log-probabilities（正在改 run_mvp_pilot.py）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/struct_self_consist_ie/`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 环境初始化：`source /etc/network_turbo && source /root/autodl-tmp/struct_self_consist_ie/env.sh`
- 基座模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- ft_002_v2 merged：`checkpoints/qwen3-8b-scierc-merged-v2/`（当前唯一在用的 fine-tuned model）
- 数据集：`data/scierc/processed_data/`、`data/conll2003/`、`data/wnut17/`（后两个刚转换完成，含 UIE JSON + sharegpt 训练数据）
- vLLM 0.18.1、LLaMA Factory 0.9.4、tmux 3.2a
- 活跃进程：**无**（所有实验已完成，GPU 全空闲）
- 活跃 Worker：2 个正在跑（见下）

### 3. 📊 当前状态
**刚完成**：exp-012/013/014 三个 baseline 分析。关键结果——SJ 碾压 logprob（NER Δρ=+0.217），但 voting_confidence 略胜 SJ（NER ρ 0.392 vs 0.383）。

**正在跑的 Worker**（等回调）：
- `worker_code_logprob_script_and_truncation_check_20260514T113358`：检查 exp-012 截断比例 + 修改 run_mvp_pilot.py 支持 logprob 输出
- `worker_code_data_format_fix_20260514T113420`：WNUT-17 格式统一 JSONL + dataset_info.json 注册 + data_utils.py 新增 loader + sampling.py 新增 schema hints

**等待 Director 决策**：re-dream 完成后审批 P0 GPU 实验（exp-001~003 多数据集 fine-tune + pilot, exp-007 N=16）

**Registry 关键状态**：
- mvp_pilot_004 (T=1.0): DONE/negative
- mvp_pilot_005 (T=0.7): DONE/negative
- e1_component_wise_re_sj: DONE/negative（排除方案 B）
- exp_012_logprob_baseline: DONE/success（SJ >> logprob）
- exp_013_exact_match_voting: DONE/negative（EM 太粗）
- exp_014_entity_majority_voting: DONE/success（voting_conf 最强信号）

### 4. 📋 待办（条件触发式）
- Worker logprob_script 回调 → 检查截断比例：>5% 则标记需重跑 exp-012 with max_tokens=1024；合并 logprob 修改到 sampling.py
- Worker data_format_fix 回调 → 确认 JSONL 格式 + loader 可用 → 汇报 Director 准备就绪
- Director 发 `[re-dream 通过]` → 立即启动 P0 GPU 实验：CoNLL-2003 fine-tune (cuda:0) + WNUT-17 fine-tune (cuda:1) + SciERC N=16 (cuda:2) 并行
- 任何新 fine-tune 完成 → merge adapter → run pilot with logprob → 汇报 baseline 对比表
- E3 (N=16) 注意温度选择：Director 未明确，建议同时跑 T=1.0（与 pilot_004 对比）

### 5. 🎯 战略上下文
- **Narrative A 已确认**：NER-primary + RE diagnostic。方案 B（度量分解）被 E1 否定
- **核心结论链**：D001(MVP方案) → D004(Gate0 partial) → D005(pilot FAIL but signals) → D006(stay-the-course) → D007(Gate1 FAIL, RE<0.30) → E1(乘性假说否定) → exp-012(SJ>>logprob, contribution 成立)
- **Dream 暴露的关键缺陷**：只对比 FK 一个弱 baseline → 已补 logprob/EM/voting 四个 baseline
- **最易判断错的事**：voting_confidence 略胜 SJ（NER +0.009, RE +0.096），但论文不应把 voting 当竞争对手——应 frame 为"consistency-based family（SJ/voting/FK）远优于 model-internal signals（logprob）"，SJ 的独特价值在于 span-level 结构信息
- **CoNLL-2003 训练集 14K 条**：比 SciERC 1.8K 大很多，fine-tune 可能需要 subsample 到 ~5K 或减 epoch
- **DDL**：EMNLP via ARR May 2026-05-25（距今 11 天）


---
