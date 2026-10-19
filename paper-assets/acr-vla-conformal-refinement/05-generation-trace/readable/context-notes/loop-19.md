# director / loop_19.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`dcd2d9dceb139a4bced7.json`](../../sessions/dc/dcd2d9dceb139a4bced7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-23T19:47:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228(4×4090), bjb1-32546(6×4090), bjb2-28827(6×4090), bjb2-40593(1×4090D), cqa1-32758(6×4090D)。不得使用其他项目的卡。
- CRM checkpoint 分两个版本：3-suite (Spatial/Object/Goal) 用于主实验，4-suite (含Long) 仅用于 Long 实验。不要混用。
- Object 实验输出文件名必须包含 exp_id，禁止通用名（M070 教训：VLA-only 和 K2mean 同名覆盖丢数据）。
- τ=0.25 是论文锁定参数，Object Adaptive 的正确 trigger rate 是 3-5%。若看到 >50% trigger → 用了错误 τ 值，结果作废。
- p<0.05 已从论文移除（n=3 vs n=3 不够）。不要在任何汇报中声称统计显著性。

### 2. 🖥️ 基础设施快照
- 5 台服务器，工作目录均为 `/root/acr-vla-conformal-refinement/`
- Python: conda base (`/root/miniconda3/bin/python`)
- CRM 3-suite checkpoint: `/root/acr-vla-conformal-refinement/crm_checkpoints/crm_3suite_obs_only.pt`（各服务器）
- CRM 4-suite checkpoint: 同目录 `crm_4suite_obs_only.pt`（Long 实验用）
- π0.5 precompute 正在 bjb1-18228 上跑（ETA 5/24-25），不要打断
- eval 脚本: `scripts/wrapper_eval.py`，n_rollouts=20
- 当前只有 eval-supp-reconvla-obj-s46 在跑（大量 GPU 空闲）

### 3. 📊 当前状态
刚从 RESET_BOTH 恢复。发现 Agent 空闲 63 分钟（M072），23 GPU 全部闲置。

已发送紧急指令要求 Agent：
1. 扫描所有服务器收割已完成实验（Object s45/s46 全套、Long s43/s44 全套）
2. 在空闲 GPU 上部署缺失实验

Registry: 仅 eval-supp-reconvla-obj-s46 RUNNING，其余全 DONE/killed。
等待 Agent 回复实验结果汇报。

### 4. 📋 待办
- Agent 汇报 Object Adaptive s45/s46 SR → 更新 5-seed 均值，判断 s44=75.0% 是否 outlier → 若 5-seed 均值 > VLA-only 则 D133 narrative 加强，否则维持"gating correctly abstains"
- Long s43/s44 结果到位 → 更新 Table 1 Long 行为 3-seed 均值±std
- Object/Long 全部 5-method 3-seed 完成 → Paper Agent Patch 更新 Table 1 最终数据
- π0.5 precompute 完成 (ETA 5/24-25) → 训练 π0.5 CRM → eval → 验证跨模型泛化性
- 所有数据稳定后 → submit_paper_to_review 做最终审稿

### 5. 🎯 战略上下文
- **D133 叙事**（核心）: "Gating prevents harmful correction + improves where VLA uncertain"。不是"所有 suite 都正"，而是"Adaptive ≥ CRM everywhere + gating 选择性介入"。
- Object Adaptive = VLA-only (77.8%) 不是问题，是 feature — gating 正确 abstain（trigger 仅 3.5%），CRM always-on 反而 -1.3pp。
- 论文 Paper Agent 已完成 Full Draft + 4 轮 Reviewer 迭代，当前 0 CRITICAL / 0 WARNING。Table 1 完整无 placeholder。
- **CoRL DDL 2026-05-29**，剩 ~5 天。核心表数据已足够投稿，补 seed 是加固 variance estimate。
- **易错点**：(1) 不要把旧 pipeline (lerobot eval) 数据和新 pipeline (wrapper eval) 混淆；(2) bjb2-40593 只有 1 张卡且之前缺 CRM checkpoint 反复崩溃，优先用其他服务器；(3) Agent 容易在 session reset 后静默空转，必须主动 push。


---
