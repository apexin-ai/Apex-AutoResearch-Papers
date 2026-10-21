# reviewer / loop_4.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`38645d365ed9f72ca606.json`](../../sessions/38/38645d365ed9f72ca606.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T23:39:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：cuda:0 和 cuda:1（项目配置 `config/projects/vla-ssd.yaml`）。当前服务器只有 2 张卡，所以不存在越界风险，但仍需核实进程绑定。
- **C001 约束（D018）**：任何 probe 实验必须 trained + untrained 对照齐全后才写 conclusion。Agent 曾两次在单臂数据下错误归因被 CRITICAL 打回。
- **服务器无外网**：AutoProcessor/HF 操作必须 `local_files_only=True`。
- **分析 Worker 不得覆盖 registry spec 字段**。
- **paper_provenance.yaml 尚未创建**——论文写作阶段前需要求 Director 让 Agent 建立溯源。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-19183（2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 98GB/卡）
- **工作目录**: `/root/vla-ssd`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **数据/模型/特征**: 全在 `/root/autodl-tmp/vla-ssd/`（checkpoints / data / features 均为 symlink）
- **已有特征目录**: `dinov2_libero_goal`, `siglip_only_libero_goal`, `trained_libero_goal`, `trained_libero_goal_no_inst`, `untrained_libero_goal`, `untrained_libero_goal_no_inst`
- **活跃进程**（截至 handoff）:
  - `action_probe_projector.py` — PID 672560 + 672990（两个实例，疑似被 kill+restart），**已完成**，结果输出到 `/root/autodl-tmp/vla-ssd/results/functional_validation/action_probe_projector.json`
  - `run_action_delta_all.py` — PID 673677，**仍在运行**，截至 handoff 跑到 untrained image_mean L23/32
- **Cron**: 无活跃 cron 任务
- **GPU 状态**: 两卡几乎空闲（1.4GB / 0.7GB 显存，0% GPU util）——probe 是 CPU 密集型（sklearn linear），不占 GPU

### 3. 📊 当前状态
**刚完成**：p0_functional_action_probe 已出结果（但 registry 还标 PREPARING，Agent 尚未更新）。

**关键结果（需审查的核心数据）**：
```
projector                  mean_R²=0.7063  (SigLIP+projector, no LLM)
image_mean_trained_L19     mean_R²=0.6832  (LLM image_mean 聚合)
llm_trained_L19            mean_R²=0.7309  (LLM last_preaction 聚合)
image_mean_untrained_best  mean_R²=0.7136  (untrained image_mean L0)
```
脚本判定 **GATE: PASS**（projector 0.7063 > image_mean LLM 0.6832, bootstrap p=0.0014）。

**⚠️ 审查要点**：llm_trained_L19 用 last_preaction 聚合时 R²=0.7309 **反超** projector 0.7063。gate 只比了 image_mean 聚合。这个 aggregation-dependent 的结论需要在审查中明确标注——Claim 2 的 functional validation 取决于聚合方式选择。paper_framing.md 已将 image_mean 定为主文公平对比口径，last_preaction 放 supplementary，但下一个"你"要核实 Agent 是否忠实执行这个约定，不 cherry-pick。

**⚠️ 另一个审查要点**：untrained image_mean best (L0) R²=0.7136 > trained image_mean (L19) R²=0.6832。Untrained 竟然略高——强化 Claim 3（training invariance）但可能引发 "training hurts?" 的过度解读。

**正在运行**: p0_functional_action_delta_probe（action-delta R² probe），跑到 untrained image_mean ~L23，预计 ~10-15 分钟完成。

**Registry PREPARING 但实际状态**:
- `p0_functional_action_probe`: 实际已完成，等 Agent 更新 registry
- `p0_functional_action_delta_probe`: 实际在跑

**QUEUED（已 killed，历史残留）**: lg_output_head_analysis, lg_instruction_ablation（这两个已被 D027 之前的 pivot 废弃，不用管）

### 4. 📋 待办（条件触发式）
- **p0_functional_action_delta_probe 完成 →** 审查 delta R² 结果：projector vs LLM vs DINO。关注 delta 维度是否与 raw action 结论一致。Delta 更能排除 autocorrelation，如果 projector 在 delta 上也 PASS 则 functional validation 更强。
- **Agent 更新 p0_functional_action_probe registry →** 核实 Agent 写的 conclusion 是否忠实反映 aggregation-dependent 的 nuance（image_mean PASS vs last_preaction FAIL），C001 约束检查（trained+untrained 对照是否齐全）。
- **plan_008 (random instruction control) 提交 →** 检查是否用了真正随机/无意义 token 而非简单空字符串（D024 教训）。
- **paper_provenance.yaml 仍未创建 →** 下次 Director 来沟通时提醒需要建立溯源。
- **Re-dream 触发前 →** 核实 plan_011 结论是否足够撑 functional validation claim。当前结果 aggregation-dependent 是 Dream reviewer 可能攻击的点。
- **Paper Agent 启动写作 →** 转入模式 B 章节审查，首先检查 Agent 是否读过 red-section skill（L1 硬约束 #1）。

### 5. 🎯 战略上下文
**项目核心结论**：frozen SigLIP+projector 是 VLA action-relevant 表征的主要来源（RSA=0.615），LLM 处理反而降低 alignment（→0.501 image_mean），训练和 instruction 均无显著影响（4 个条件收敛 0.48-0.50）。

**决策链关键节点**：
- D007: MVP Gate 2 FAIL（temporal distance vision-dominated）
- D013-D014: MVP-2 Action Probe 三轮均 FAIL（DINO 打平 trained VLA）
- D021-D022: 6 轮 probing 一致确认 trained ≈ untrained → Pivot 到 Option A2（vision encoder dominance）
- D027-D028: SigLIP-only RSA smoking gun PASS，MVP 通过
- D029: image_mean 聚合排除伪影
- D030: Dream 三档均低于 acceptance，#1 问题 = 缺功能验证 → plan_011

**下一个"你"最容易判断错的事**：
1. **Aggregation trap**：projector vs LLM 的 R² 比较结果取决于聚合方式。image_mean → projector 赢；last_preaction → LLM 赢。Agent 可能只报 PASS 的那个口径。你必须两个都看，且核实论文是否一致用 image_mean。
2. **untrained L0 反超 trained**：image_mean 下 untrained best R²=0.7136 > trained L19 R²=0.6832。这强化 Claim 3 但危险——Agent 可能解读为 "training degrades"，这已超出当前 evidence 可支撑的范围（L0 是 embedding 层，特殊性需讨论）。
3. **不要被 "GATE: PASS" 误导**：gate 是脚本里的自动判定逻辑，不等于论文 claim 站得住。你需要独立审查 gate 的前提条件是否合理。
4. **Dream re-dream 节点**：plan_011 结果 + framing 更新后必须 re-dream，不能跳过直接启动 Paper Agent。
5. **时间线**：距 CoRL abstract DDL（5/26）还有 11 天，paper DDL（5/29）14 天。plan_011 正在跑，如果结论站得住 → 5/17 re-dream → 5/19 初稿。GPU 预算 ~9 GPU·h 够用（probe 实验 CPU 密集不怎么吃 GPU·h）。


---
