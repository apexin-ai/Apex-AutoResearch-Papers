# director / loop_1.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`1b4c262700b100c8e33d.json`](../../sessions/1b/1b4c262700b100c8e33d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T10:30:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0-3 only（constraint C001）
- "environment-grounded recovery" 声明禁止使用——代码实际是 "recovery conditioned on corrupted history + original observation"，不是重执行后的环境反馈 [D003]
- ms-swift 4.2.0 不支持 `--config yaml`，必须用命令行参数
- eval 必须用 `--task_list eval/eval_tasks_47.json`（47 task 固定列表），enable_thinking=False
- SFT 数据必须验证 taxei 和 vanilla 文件 md5 不同（之前踩过 byte-identical 的坑）
- formatter.py 会检查 `[DRY_RUN]`/`API_ERROR`/`Error code` 内容并 raise，确保不会把错误内容当训练数据

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com) + gpu-5090-4x-3 (connect.bjb2.seetacloud.com)，用户 root
- 工作目录：`/root/autodl-tmp/tax_error_inject_agent`
- 轨迹收集进程：PID 11050（CPU 任务，后台运行，~242/500 成功，成功率 74.2%）
- 数据：trajectories 在 `data/trajectories/`，SFT 数据在 `data/`
- 模型：Qwen3-8B（HF 下载，路径需确认）
- Teacher API：GPT-5.2（OpenAI 兼容端点）
- 无 W&B 配置，无 conda（pip 环境）

### 3. 📊 当前状态
刚做完：D001-D003 三个决策落盘、ROADMAP 更新至最新、Reviewer 论文规划建议已处理。
Agent 在 RESET 前正在处理 mini pipeline 指令（用已有 242 条数据跑 注入→GPT-5.2 recovery→SFT→eval），但可能未完成就被 RESET。
registry: traj_collect_500 RUNNING；vanilla-react-baseline DONE (42.6%)；sft-dryrun-73 DONE。
Related work 对比表 worker 已完成（远程 `docs/related_work_comparison.md`），但需修正 grounding 声明 [D003]。
4 张 5090 全部空闲。

### 4. 📋 待办
- Agent RESET 完成 → 重发 mini pipeline 指令（用已有 ~242+ 条轨迹跑注入+recovery+SFT+eval，占 GPU）
- mini pipeline 完成 → 看 TaxEI vs vanilla 早期信号方向
- 轨迹收集达 500 → 正式注入（taxonomy + random）+ recovery demo 生成 + 三组 SFT 训练 + eval + McNemar
- 修正 related work 对比表中 "environment-grounded" 为准确描述 [D003]
- 实现 RandomInjector（随机 perturbation baseline）[D001]——公平性约束：注入数量/位置分布/teacher 与 TaxEI 一致
- RandomInjector 加入 related work 对比表

### 5. 🎯 战略上下文
- MVP claim 已升级为 `TaxEI > random injection > vanilla SFT > zero-shot` [D001]，但 random vs vanilla 的排序关系是分析维度不是 gate [D002]
- Pass/Fail 5 个 gate：合法率≥80%、recovery质量≥75%、Gate3a TaxEI≥vanilla+5pp、Gate3b TaxEI>random、clean回归<2pp
- Paper framing：Method paper with empirical analysis（Reviewer 建议），不是纯 analysis paper
- 最易判断错的事：(1) 不要声称 environment-grounded，当前实现不是；(2) random injection 弱于 vanilla 不是 MVP 失败——反而强化 taxonomy 价值；(3) eval set 只有 47 tasks 不是 134，pick_and_place_with_movable_recep 完全缺失
- PALADIN 差异化要点：PALADIN=tool error only；TaxEI=planning+context error taxonomy + 跨 error type transfer analysis
- pick_cool 0% 是好素材——如果 TaxEI 在 cooling 任务上特别有效，可作强 case study


---
