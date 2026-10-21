# Reviewer coordination (archived snapshot) — Part 5 of 5

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../reviewer-coordination-20260522-183404.md) · [Structured JSON](../../../sessions/e3/e347a2407583df85188d.json)

## Round 158

### User

_source line 2325 · 2026-05-22T18:33:12.348020+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_09b04b56f2fb04931812c4a55f159dee:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2326 · 2026-05-22T18:34:04.634400+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目是 measurement/analysis 论文，无 GPU 训练实验。westb-29275 的 4×RTX PRO 6000 Blackwell 96GB 空闲，Reviewer #108 书面确认无值得跑的 GPU 实验。不要建议跑新 GPU 实验。
- 所有实验使用 API-based judges（GPT-4o、Qwen3-32B、Llama-70B、Gemini-2.5-Flash、Claude Sonnet 4），不涉及本地模型推理。
- 论文 DDL: **May 25, 2026 AoE**（EMNLP 2026 ARR）。8 页正文限制 + unlimited references。
- Reviewer 是只读角色：不修改文件、不执行实验，唯一输出渠道 `reviewer_post_to_director`。

### 2. 🖥️ 基础设施快照
- 服务器：westb-29275 (root)，远程代码目录 `/root/causal_style_decomp_judge`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/`
- 论文源文件：`docs/paper/sections/*.tex` + `docs/paper/main.tex`
- Registry：`registry.yaml`（54 experiments, 53 done, 1 blocked）
- 活跃进程：无（所有实验已完成）
- 标注数据：两位标注者均已完成 50 pairs，数据已集成论文

### 3. 📊 当前状态
**我的 Report 序列：#83-#115（Loop #3）。**

刚完成 **Report #115**：R12 Action Matrix 独立审查。R12 fresh review 评分 3.0（从 R11 的 3.5 下降）。核心判断：
- 下降原因：D069 hedging 过度（正文 hedge 但标题没改→内部矛盾加剧）+ reviewer 噪声
- **改了我 #114 的立场**：现在支持改副标题（"Detecting Hidden Style Bias" → 中性描述）
- MF2（formality confound）是关键杠杆：正确处理 = MF3（novelty）的解药
- 给出 P0-P4 优先级排序（~7.5h Paper Agent 工作量）
- WARNING: hedging 过度风险——区分 "agnostic about mechanism" vs "uncertain about findings"

Registry: 全部 DONE/blocked，无 RUNNING 实验。
等待：Director 对 R12 action matrix 的决策（标题是否改、MF2+MF3 联合处理方案）。

### 4. 📋 待办
- Director 确认标题改动 → 审查新标题是否 neutral（不要又预设方向）
- Paper Agent 完成 R12 修复 → Mode B 对抗审查（重点检查：hedging 是否重新平衡、formality claim 是否正确降级、GEE novelty 是否升格）
- R13 审稿返回 → 独立评估是否突破 3.5
- 标注者 2 如果有 issue → 已到手，κ=0.44/AC1=0.65 已集成
- 提交前最终 check → 数字一致性 grep（上次 42→50 更新时做过，如果又改数字需要再做一轮）

### 5. 🎯 战略上下文
**Score trajectory**: R1 2.5 → R2-R4 3.0 → R5-R10 3.5 → R11 3.5 → R12 3.0 → Target 4.0

**核心瓶颈**：pairwise > Likert 的 novelty 天花板（Thurstone 1927 domain transfer）。这是结构性问题，不可通过写作 reframe 完全解决。真正 novel 的是 C2b（per-axis GEE confound structure）但一直没被充分 marketing。

**最容易判断错的事**：
1. **不要继续加 hedge**。D069 加了大量 hedge 后分反而下降了。论文对 phenomenon（divergence exists）应该 confident，对 mechanism（attenuation vs amplification）应该 agnostic。
2. **Formality ≠ verbosity**。Verbosity 是 clean style bias（GEE Style OR 8-13, Orig NS），formality 是 quality-confounded conditional effect。不能把两轴放在同一个 "bias" 框架下——这正是 R12 MF2 的攻击点，也是 C2b novelty 的来源。
3. **合成实验不值得做**（Report #114 论证过）。设计需要 ground-truth bias oracle → 循环论证。24h 内执行风险太高。
4. **κ=0.44 不是弱点**。pass precision 100%（majority vote）/ 84-100%（per annotator）才是 precision-oriented gate 的正确指标。Appendix S 已有 Feinstein + AC1 preemptive framing。
5. **Cross-axis d=-0.23**：Appendix R caption 说 "d<0.20 negligible" 但自己数据 0.23。改 caption 阈值为 Cohen's "small"（0.20-0.50）即可，不需要新分析。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_09b04b56f2fb04931812c4a55f159dee:reviewer"
}
```

</details>

---
