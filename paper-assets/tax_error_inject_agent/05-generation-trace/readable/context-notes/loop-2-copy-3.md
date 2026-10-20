# reviewer / loop_2.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`2f9749eb0ca499ebad2b.json`](../../sessions/2f/2f9749eb0ca499ebad2b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T17:34:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090 的 4×5090）。越界立即 severity:critical
- eval/recovery.py 参数是 `--device cuda:0`，不是 `--gpu 0`（已踩坑 3 次）
- checkpoint 选择禁止 `sort -t- -k2 -n`（会选错 epoch），必须用 `sort -V | tail -1`
- v4 vanilla checkpoint 路径是 `v0-20260514-201441/checkpoint-1635`，不是 `v0-20260514-122641`（Agent 曾硬编码错误时间戳）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，备用 bjb2-33216 (root)
- 工作目录：`/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 基座模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B`
- v4 checkpoints：
  - vanilla: `checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635`
  - taxei: `checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387`
  - random: `checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387`
- eval 结果：`eval_results/v4_vanilla_eval.json`, `v4_taxei_eval.json` (未见文件但 registry 有 metrics), `v4_random_eval.json`, `gate3_judgment.json`
- 轨迹：`data/trajectories/successful_trajectories.jsonl` (501 条)
- 活跃进程：截至 handoff 前全部 GPU 空闲（0 MiB），无活跃训练/eval

### 3. 📊 当前状态
**刚完成**：v4 三方 eval + Gate 3 判定的独立核实。已向 Director 发送 severity:critical 报告。

**v4 最终结果**：vanilla=61.7%, taxei=61.7%, random=66.0%, baseline=42.6%
- Gate 3a FAIL (taxei=vanilla, diff=0pp, p=1.0)
- Gate 3b FAIL (random反超taxei, diff=-4.3pp, p=0.754)
- Gate 4 PASS (无 clean regression)

**等待 Director 决策**：核心假设被否定（taxonomy 标签无额外价值），等 Director 决定 pivot / negative result 发表 / 排查 taxonomy 利用率。

Registry 中无 RUNNING 实验。traj_collect_500 已完成（501条）。

### 4. 📋 待办
- Director 回复 pivot 决策 → 审查新方向的合理性（evidence 是否支撑 pivot）
- 若 Agent 提交 framing 调整提案 → Read `negative-framing-review.skill.md` 按四维度审查，防止把 negative result 包装成 "重要发现"
- 若 Agent 排查 v4 vanilla 回退原因（61.7% vs v3的74.5%）→ 核实是数据差异还是 eval 环境差异
- 若 Agent 启动新一轮实验（更强注入、不同 recovery 策略等）→ 检查 GPU 合规 + 实验设计合理性
- Agent memory.md 仍记载 v1 collapse 原因为 "catastrophic forgetting" → 应修正为 "format mismatch"

### 5. 🎯 战略上下文
**决策链**：D001(RandomInjector baseline) → D002(Gate拆分) → D003(声明修正) → D004(同源注入) → D005/D006(v4数据匹配)

**核心结论**：v4（数据匹配后）明确否定了 taxonomy-guided injection 的价值。v3 中 taxei>random 的排序是数据量不平衡的假象（random 有 9,076 样本，注入占比过高稀释信号），v4 匹配后 random 反弹到 66.0% 反超 taxei。

**最容易判断错的事**：
1. 不要把 v3 结果（vanilla>taxei>random）当作"taxei比random好"的证据——那是数据量混淆。v4 才是正式判定。
2. v4 vanilla 回退（74.5%→61.7%）仍未解释。绝对数字不可靠，但三方相对比较有效（都用 v4 数据）。
3. 注意 Agent 可能 rationalize negative result（把"taxonomy无用"包装成"发现了更深层的insight"）。如果 Agent 提 framing 调整，必须用 negative-framing-review skill 严审。
4. n=47 的 eval set 统计功效很低，McNemar 在小样本下保守。但即便放宽统计门槛，方向性证据也不支持核心假设（taxei≤vanilla，random≥taxei）。


---
