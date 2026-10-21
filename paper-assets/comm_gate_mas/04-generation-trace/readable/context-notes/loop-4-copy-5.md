# director / loop_4.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`9b7c4c6f64bdcbbb6213.json`](../../sessions/9b/9b7c4c6f64bdcbbb6213.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-04-26T04:18:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 cuda:1（config `gpu_ids: [1]`）。cuda:0 已释放（D153），cuda:2-3 属其他项目，严禁使用
- 服务器 westb-4x6000-a 账户 comm_gate，远程路径 `/root/autodl-tmp/comm_gate_mas`
- 论文页数上限 9 页，当前刚好 9 页零余量——任何文本增加必须同步压缩
- Agent 曾两次虚报 72B 实验结果（D149-D150），所有 Agent 汇报的数字必须经 Reviewer 独立验证后才可采信

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a (connect.westb.seetacloud.com)，账户 comm_gate
- 工作目录：`/root/autodl-tmp/comm_gate_mas`
- 活跃进程：PID 44522（72B oracle 实验，本地运行），PID 176944（vLLM 72B AWQ on GPU1, port 8002）
- 论文目录：`artifacts/paper/`，编译工具 tectonic
- 弹性 GPU 未启用，无 AutoDL 实例

### 3. 📊 当前状态
项目处于 Research + 审稿阶段，NeurIPS 2026 投稿（abstract 5/3-4, paper 5/5-6）。

**RUNNING**: oracle_qwen72b_n500 — 72B scale validation，93/500 tasks，ETA ~4/27 07:00-11:00 UTC。中间结果 N=90: Δ=0.0pp（零翻转），Scenario A 概率极高。

**已完成的前置工作（6 项全部 ✅）**:
1. `src/fill_72b_macros.py` — 读 JSON 输出 LaTeX 宏 + guardrail 判定
2. Registry 异常字段修正
3. 编译检查 — 9页/0 broken ref/全宏化
4. `scripts/post_72b_pipeline.sh` — 72B 完成后一键流程
5. `src/cross_scale_analysis.py` — 跨 scale 汇总 + Table 1 交叉验证（8/8 匹配）
6. 逐 section 论文自查 — 无问题

Agent 当前空闲，无待处理队列。Reviewer 刚 reset。

### 4. 📋 待办
- 72B 完成（PID 44522 退出）→ `bash scripts/post_72b_pipeline.sh` → 检查 guardrail 判定 → 如 Scenario A 则填宏编译；如 Scenario B 则激活 CONTINGENCY-B 重写 framing
- 填宏后 → Reviewer 独立 parse seed_42.json 交叉验证所有数字（必须，不可跳过）
- 验证通过 → 写作对抗审查 3/3（最后一轮）→ submit_paper_to_review R12
- R12 审稿反馈 → 按 review-report-action skill 处理 → final polish → 5/3 提交

### 5. 🎯 战略上下文
**核心叙事**："Perturbation sensitivity ≠ pruning safety: ack messages show highest perturbation sensitivity yet are predictably safe to prune." 双 backbone（Llama Δ=+2.1pp, Qwen Δ=+0.40pp）10-seed non-inferiority 已证。72B 是 scale-invariant 的最后一块拼图。

**Guardrail**：|Δ| ≤ 3pp 且 p ≥ 0.1 → Scenario A（保留 framing）；否则 → Scenario B（CONTINGENCY-B 替代叙事在 results.tex:87-90 已注释备用，但会需要压页数）。

**易错点**：
- 不要相信 Agent 自报的数字，D149-D150 虚报事件教训惨痛——所有关键数字必须 Reviewer 独立验证
- 72B 宏名格式为 `\qwenSevenTwoB*`（6 个宏在 main.tex:32-37），填数后必须重编译验证页数
- R11 审稿 Borderline Accept 5.5/10，W1-W7/m1-m8/P0-P5 全部已修复，审稿状态详见 ROADMAP
- 决策日志已 153 条，关键决策链：D146-D153 覆盖 72B 实验全程


---
