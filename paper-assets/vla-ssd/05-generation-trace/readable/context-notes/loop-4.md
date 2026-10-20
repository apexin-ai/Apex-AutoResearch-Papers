# director / loop_4.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`c9111099a1c249e4d93d.json`](../../sessions/c9/c9111099a1c249e4d93d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-17T21:57:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- GPU 预算 ~26 GPU·h，当前已用 ~27-29 GPU·h（Reviewer 已发 warning，超预算 1-3h）。不要再批准大实验，除非用户明确同意扩预算
- 论文 8 页限制（CoRL 格式），当前恰好 8 页正文，任何新增内容必须同步压缩
- C3 (vision encoder geometry) 定位为 "qualified observation"，不得升级回 "finding"（Reviewer 明确反对，CKA 反转未解决）
- Head count 不一致待修复：Abstract "21-25"，Table 2 "25/32"，ablation code 用 24 个。已派 Agent 确认 ground truth，**结果还没回来，必须先拿到再统一全文**

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，工作目录 /root/vla-ssd/
- 论文本地路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/
- 分析脚本：/root/vla-ssd/scripts/analyze_ablation_50demos.py（已验证可用）
- 50-demo 结果 JSON：/root/vla-ssd/results/ablation_50demos_combined.json
- 图表 artifacts：projects/vla-ssd/artifacts/（fig_rsa_perlayer_curve.pdf, fig_ablation_*.pdf）
- 活跃进程：llama2base_action_probe (cuda:1, PID 913317, 特征提取完成，Phase 2 CPU probe 训练中)
- cuda:0 空闲

### 3. 📊 当前状态
**刚完成**：50-demo ablation critical path 全部完成并已 patch 进论文。Paper Agent 完成了所有文本更新：
- D060 reframe（C1→框架, C2→锚, C3→观察）
- L115 RSA "stable...then declines" 叙事修正
- FDR 校正结果加入 §4.4
- 50-demo ablation 数字替换 5-demo（experiments.tex + discussion.tex）
- Control8 gradient 叙事（3.5×）
- Demo sensitivity 提及（appendix）
- Mechanistic interpretation 段落（Discussion）
- RSA per-layer curve（appendix figure）
- Citation 格式修复

**Registry RUNNING**：llama2base_action_probe (cuda:1) — Llama-2 base 模型 per-layer action R² probe，补充 C2 三条件梯度。ETA 已过估计时间，应该快完成或已完成。

**等待中**：
- Agent 回复 head count ground truth（24 vs 25）
- llama2base_action_probe 完成回调
- Round 5 review 审批卡已发（apr_20260517T215433_4mly, pending 用户批准）
- check_paper_consistency 结果：2 critical（corl_example.tex 中的 Gauss1857/Lagrange1788 引用缺失——这是模板示例文件，非论文正文，可忽略）

### 4. 📋 待办
- **Agent 回复 head count** → 确认 24 or 25 → 派 Paper Agent 统一 Abstract/Table 2/正文中所有 head count 数字
- **llama2base_action_probe 完成** → 检查 R² 是否呈 untrained < llama2base < trained 梯度 → 若是，派 Paper Agent 加入 §4.2 或 appendix 作为 C2 补充证据
- **Round 5 review 用户批准** → review 自动启动，等审稿报告
- **审稿报告回来** → 按 review-report-action skill 处理（Holistic Pass → Action Matrix）
- **corl_example.tex 引用** → 确认 main.tex 不 \input corl_example.tex（模板残留），如果 input 了就移除

### 5. 🎯 战略上下文
- **项目处于 Round 5 提交前最后阶段**。CoRL DDL：Abstract 5/26, Paper 5/29，还有 12 天
- **D060 决策链**：Round 4 weak reject → D060 reframe（C1 降为框架, C2 升为唯一核心, C3 降为观察）→ 50-demo ablation 确认因果证据 → Round 5
- **核心数字**：all24 vs baseline L1 Δ=+0.059 (p<0.0001), specificity all24 vs control8 Δ=+0.042 (p<0.0001)
- **易错点 1**：Head count 24 vs 25 不一致是 Reviewer 明确标的 warning，必须在 Round 5 review 前修复。不要假设哪个对，等 Agent 确认
- **易错点 2**：GPU 已超预算，不要再批大实验。llama2base 是最后一个
- **易错点 3**：Paper Agent 已多次压缩 Discussion/Limitations 来保持 8 页，再加内容必须同步压缩。"Code will be released" 和 RT-2/π₀ 引用已被移除
- **Reviewer 已确认的定位**：C3 不升级（CKA 反转），control8 用 gradient 叙事（非零效应是特性不是 bug），RSA curve 放 appendix 不放 main


---
