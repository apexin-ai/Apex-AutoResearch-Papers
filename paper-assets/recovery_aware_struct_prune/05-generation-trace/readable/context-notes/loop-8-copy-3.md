# reviewer / loop_8.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`997cafe8e5b9e6fb6ee0.json`](../../sessions/99/997cafe8e5b9e6fb6ee0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T19:24:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 仅 cuda:0/cuda:1，westd-11672 仅 cuda:0/cuda:1（C001/C003）
- 所有大文件写 `/root/autodl-tmp/recovery_aware_struct_prune/`，禁止写根分区（根分区仅 30GB，C002）
- westb 磁盘 78%（56GB free），westd 需检查——checkpoint save 可能因磁盘满失败
- Reviewer 只读：不执行实验、不修改文件，唯一输出渠道 `reviewer_post_to_director`
- W&B entity/project 未配置，`fetch_wandb_metrics` 不可用——只能从服务器日志直接提取 metrics

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× RTX PRO 6000 Blackwell (~98GB each)
  - cuda:0: PID 547366 — grpo_unpruned_baseline（未剪枝 DeepSeek-R1-7B GRPO，82.7GB，刚启动）
  - cuda:1: PID 534667 — grpo_stage2_standard_20_v8（step ~32/100，71.7GB）
  - 日志：`/tmp/grpo_standard_v8.log`, `/tmp/grpo_unpruned_baseline.log`
  - 模型路径：`/root/autodl-tmp/recovery_aware_struct_prune/` 下各子目录
  - Base model：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`
- **westd-11672**: 2× RTX PRO 6000 (~98GB each)
  - **双卡完全空闲**（0% util, 0 MiB）
  - SFT 模型已保存：`sft_rasp_20_westd/`, `sft_standard_20_westd/`
  - eval 脚本反复失败（EXIT_CODE=2, shell syntax），Agent 在修但尚未修好
- Python: `/root/miniconda3/bin/python`，conda base 环境
- 代码根目录：`/root/recovery_aware_struct_prune`（两台服务器相同）
- HF cache: `/root/autodl-tmp/.hf_cache`

### 3. 📊 当前状态
**我刚完成的审查**：
- GRPO v8 双组 step 20 + step 30 独立核实（日志直接提取 metrics）
- RASP v8 collapse 确认 → kill 执行核实（进程消失确认）
- Standard v8 step 30 正面意外：frac_zero_std 逆转 0.675→0.525，模型在学习
- GPU 资源合规检查全部通过

**RUNNING 实验**：
- `grpo_stage2_standard_20_v8` — westb cuda:1, step ~32/100, 健康且改善中。Step 50 做 eval。
- `grpo_unpruned_baseline` — westb cuda:0, 刚启动，未剪枝模型 GRPO（验证 GRPO 本身是否正常工作）

**阻塞/待修**：
- `eval_sft_rasp_20_westd_n100` + `eval_sft_standard_20_westd_n100` — EXIT_CODE=2 反复失败（≥3次），westd 双卡空闲浪费中
- N=1319 full eval 被 N=100 eval 阻塞

### 4. 📋 待办（条件触发式）
- Standard v8 step 40 metrics 出现（~19:30 UTC）→ 核实 frac_zero_std 趋势是否持续改善
- Standard v8 step 50 checkpoint → Agent 应做 N=100 eval，核实 accuracy 变化（64% baseline）
- Standard v8 step 100 完成 → 最终 eval + 与 RASP collapse 对比 → 决定论文 story
- unpruned GRPO step 10 metrics → 核实未剪枝模型 GRPO 正常（排除 GRPO 实现 bug）
- westd eval 修复成功 → 核实 RASP westd ~57% / Standard westd ~64% 跨服务器复现性
- westd eval 持续失败 → 提醒 Director 空闲 GPU 浪费，建议改用 westb eval 或手动修 shell syntax

### 5. 🎯 战略上下文
**核心决策链**：D027 post-prune claim 崩塌（RASP 31% vs Standard 27%, p=0.54）→ D029 SFT 也 Standard > RASP → D033 所有 claim 系于 GRPO v8 → **RASP v8 collapse 确认（v2/v5/v8 三次），Standard v8 在改善中**

**当前论文 story 候选**（待 Standard v8 + unpruned baseline 完成后定）：
1. Standard GRPO 成功 + RASP collapse → "Pruning strategy determines RL recoverability"（方向与原假设相反但可发表）
2. 双方都 collapse → "GRPO 对结构化剪枝模型系统性失效"（需 unpruned baseline 证明 GRPO 本身正常）
3. GraSP 41% vs Standard 64% vs RASP 57% (post-SFT) 是唯一 p<0.001 数据点（D034 已确认为核心 finding）

**最容易判断错的事**：
- **不要套人类时间直觉**——"v1-v8 连续 8 版失败说明项目不行" 是错的，v1-v7 是工程问题（截断/OOM/磁盘满），v8 是首个工程稳定版本，算法结论才刚开始有效
- **Standard v8 frac_zero_std 的 step 10→20 上升不代表 collapse**——我在 step 20 时预测 step 30 会到 0.85，实际降到 0.525，GRPO 早期波动是正常的
- **SFT accuracy 差异（57% vs 64%）在 N=100 下统计不显著**（D033: p=0.31），不要当作确定结论
- **westd eval EXIT_CODE=2 是 shell syntax 问题不是模型问题**——SFT 训练本身成功（checkpoint 已保存）


---
