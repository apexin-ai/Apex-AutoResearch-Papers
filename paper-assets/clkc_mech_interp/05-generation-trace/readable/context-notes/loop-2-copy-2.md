# reviewer / loop_2.md

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`faa77bdd3771779c4815.json`](../../sessions/fa/faa77bdd3771779c4815.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-23T20:01:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0,1,2,3 on westd-41302。越界进程立即 CRITICAL + kill。
- 匿名仓库 `anonymous-nlp-2026-2/clkc_mech_interp` 已 public，任何后续 push 不得包含真实姓名/邮箱/服务器地址。
- EMNLP 2026 ARR DDL 2026-05-25。Abstract ≤200 词（当前恰好 200）、主文 ≤8 页（当前 7 页 + limitations/refs 延伸至 p10）。
- Cross-task transfer 单种子结果（exp 116, lbfgs solver）已被 invalidated——Gemma "mid-layer collapse" 是 solver artifact。仅信任 bootstrap n=1000 结果（exp 119, liblinear）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-41302 (root)，工作目录 `/root/clkc_mech_interp`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/{gemma-2-9b-it, LLM-Research/Meta-Llama-3.1-8B-Instruct, Qwen3-8B}`
- 数据：`/root/clkc_mech_interp/data/{llama31,qwen3,gemma2,xnli/}`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/`
- 论文源：`docs/paper/` (本地) = `/root/clkc_mech_interp/docs/paper/` (远程)
- 活跃进程：无（全部实验完成，4 GPU 空闲）
- 匿名仓库：commit 44f46fb，36 files，含 requirements.txt

### 3. 📊 当前状态
全部审查完成，论文 submission-ready。我完成了：
- 12 个 steering 实验全部核实（1 success Llama L13, 11 negative）
- 全面数据审计（Table 1/2/3 + 60+ inline numbers 100% PASS）
- Discussion L27 factual error 修复确认
- Submission-readiness 6 项最终检查全 PASS
- 匿名仓库完整性确认（requirements.txt 已补）
- AI disclosure appendix 已添加

Registry: steering_gemma_L10_120 是 PREPARING（实际已完成，registry 状态未更新）。其余全 DONE。无 RUNNING 实验。
等待中：用户在 OpenReview 填写 ARR submission form。

### 4. 📋 待办
- 用户提交 ARR form 后 → 确认提交成功，无需 Reviewer 动作
- 若 Director 要求加入更多 steering 数据到论文（Qwen L18, Gemma L10/L24）→ 验证数据已就绪，源 JSON 路径见 ROADMAP
- 若收到论文写作修改审查请求 → 加载 `paper-quality-lessons.skill.md`，按模式 B 审查
- 若 Gemma L10 registry 未更新 → 提醒 Agent 将 status 从 PREPARING 改为 DONE

### 5. 🎯 战略上下文
**核心结论**：conflict 信号搭载在通用跨语言子空间上（C2 piggyback），因果影响仅在 Llama L13（C6 architecture-specific）。Detection ≠ Decision 是中心叙事。

**决策链关键节点**：
- D014: L13 steering SUCCESS → 整篇论文锚点
- D018: cross-task transfer 加入论文（推翻 D016）→ Discussion 新段落
- D019: 第二轮 steering 全 negative → 强化 architecture-specific

**易错点**：
1. 不要引用 exp 116 单种子数据（Gemma "mid-layer collapse" 是 lbfgs artifact）——只用 exp 119 bootstrap
2. Provenance 文件严重滞后（数字停留在 bootstrap 前），不要依赖它做数字核对——直接读源 JSON
3. Llama 目录有两个探针结果文件（`probe_results.json` vs `probe_results_perlayer.json`），论文用 perlayer 版本
4. `steering_results.json`（无后缀）在 gemma2 目录下已被 L10 覆盖，L17/L21 原始数据在 `steering_results/` 子目录


---
