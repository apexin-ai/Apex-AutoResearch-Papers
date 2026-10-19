# reviewer / loop_1.md

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`d36c58015aec4b367a04.json`](../../sessions/d3/d36c58015aec4b367a04.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-22T18:30:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0,1,2,3（westd-41302）。之前无越界事件，但必须每次核对
- Gemma probe 新数据（76.2%, +6.6pp p=0.006）写入论文前**必须** registry 注册 + 独立验证。ROADMAP 已列但 registry 无对应实验记录
- 论文 EMNLP 2026 ARR DDL = **2026-05-25**（距今 ~3 天）。主正文 ≤8 页硬约束（当前 7 页）
- `yang2024qwen25` 引用的是 Qwen2.5 Technical Report，但论文用的模型是 Qwen3-8B。未找到 Qwen3 独立论文，暂可接受但审稿人可能追问

### 2. 🖥️ 基础设施快照
- 服务器：westd-41302(root)，工作目录 `/root/clkc_mech_interp`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/`
- 论文目录：`docs/paper/`（根目录 .tex 是编译版，`sections/` 子目录是旧草稿——**只审根目录版本**）
- Steering 数据：`data/llama31/steering_results/`、`data/qwen3/steering_results/`、`data/gemma2/steering_results/`
- Probe 数据：`data/{llama31,qwen3,gemma2}/probe_results.json`
- 活跃进程：截至 handoff 时 registry 无 RUNNING 实验。Gemma XNLI 激活采集刚启动（GPU），DE probe n=2000 CPU 约 43%

### 3. 📊 当前状态
**刚完成**：论文 Step 5 迭代审查 Round 1→4，Overall 从 4 升至 6 并收敛。已发送 12+ 条审查报告给 Director。所有历史 critical/warning 已关闭（C1 引用归属、W1 Qwen power、W2 Bonferroni k、W3 "neither" 描述）。

**Registry 关键实验**：
- steering_107_L13: DONE/success — **唯一成功的 steering**（p=0.002, p<0.001）
- steering_107_gemma_L17/L21: DONE/negative — informative negative
- steering_107_qwen_L14/L23: DONE/negative — underpowered (p→c) + adequate (c→p)
- de_activations_112: DONE/success — DE 激活已采集，等 probe 训练完

**等待中**：Gemma XNLI 激活→probe→Table 1 扩展；DE probe n=2000→可能加入论文

### 4. 📋 待办
- Gemma XNLI probe 完成 → 验证 Table 1 XNLI 列 Gemma 数字 + Fig 3 三模型 forest plot 数据一致性
- Gemma conflict probe bootstrap 结果可用 → 验证 C1 "76.2%" 和 C2 "+6.6pp p=0.006" 是否与源 JSON 一致，确认 registry 已注册
- DE probe n=2000 完成 → 审查 EN↔DE 迁移不对称性是否与 EN↔ZH pattern 一致（预期：+Δ 更小因印欧语系更近）
- 任何新数据写入论文 → 触发新一轮写作审查（当前 Round 4 收敛基于 Llama+Qwen 两模型版本）
- Paper Agent 提交最终版 → 做 pre-submission checklist（占位符扫描、编译零 error、匿名化、引用完整性）

### 5. 🎯 战略上下文
**核心结论链**：D008（C2 reframe: 不对称性非冲突特异性）→ D012（C3 降为 observation）→ D014（L13 steering SUCCESS）→ D015（steering 是 Llama-specific）。论文 story = "冲突信号跨语言可检测 + 不对称性继承通用结构 + detection≠decision dissociation"。

**易错点**：
1. `docs/paper/` 根目录 vs `sections/` 子目录有同名文件但内容不同。**编译用根目录**，sections/ 是旧版。Rule #5 双边核对源
2. Qwen steering "uninformative" 只限 p→c 方向（n=8）；c→p 方向（n=76）零翻转是 informative negative。这个区分花了 3 轮才修好
3. Bonferroni k=10 = L13 的 10 个 alpha 值（{±20,±10,±5,±2,±1}），per-layer correction。审稿人可能要求 k=30（跨全部 3 层），此时 p=0.002 不通过但 p<0.001 仍通过。rebuttal 准备中需预备此论证
4. n_test < probe test set 是因为 steering 用了 ~50% 子集（Llama 136/272, Gemma 158/316），不是因为排除了 "neither"。Round 4 已删除错误描述但未补充正确解释


---
