# director / loop_4.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`0f295fce4def99572fab.json`](../../sessions/0f/0f295fce4def99572fab.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T12:54:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0 和 cuda:1（westd-11235 双卡）。禁止使用其他 GPU
- bash -c 提交的训练命令必须在脚本体内显式 `export CUDA_VISIBLE_DEVICES={N}`，不能依赖外层环境变量——conda activate 会静默重置 CVD
- seed 实验启动前必须确认目标 GPU 无其他进程占用（上一轮 vota_seed123 因 CVD 被 conda 重置撞卡 OOM）

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/trace-verdict-study
- Python 环境：conda base（/root/miniconda3/bin/python），aml-train 镜像
- 活跃进程（截至 handoff 时）：
  - deepseek_vota_seed42：cuda:0，RUNNING（DeepSeek-Coder-6.7B VOTA 验证）
  - vota_seed123_v2：cuda:1，PID 103781，RUNNING（seed robustness 重试，已修复 CVD）
- vota_seed456：PREPARING，尚未填充命令

### 3. 📊 当前状态
本轮主要处理了 Reviewer critical：vota_seed123 因命令硬编码 --gpu 0 与 deepseek_vota 撞卡 OOM。根因是 conda activate 重置了 launcher 设置的 CVD 环境变量。Agent 已修复（命令内部显式 export CVD）并重新提交为 vota_seed123_v2。

已更新 ml-experiment-guide.skill.md，新增"bash -c 子 shell 中 conda activate 会重置 CVD"条目。

等待中：
- deepseek_vota_seed42 完成回调（预计很快，已跑较久）
- vota_seed123_v2 完成回调
- vota_seed456 待启动

### 4. 📋 待办
- deepseek_vota_seed42 完成 → 分析结果，判断 VOTA 是否跨模型泛化（plan_004 核心验证）
- vota_seed123_v2 完成 → 与 seed42 对比，确认 seed robustness（plan_008）
- deepseek_vota 完成释放 cuda:0 → 启动 vota_seed456（用 cuda:0 或 cuda:1，看哪个空闲）
- 两个 seed 实验都完成 → 汇总 seed robustness 结论，更新 ROADMAP

### 5. 🎯 战略上下文
- 项目处于 Research + 审稿并行阶段。核心验证：VOTA 方法的 verdict accuracy 优势是否跨模型泛化、是否 seed-robust
- deepseek_vota_seed42 是跨模型泛化的关键数据点（从 Qwen2.5-Coder 扩展到 DeepSeek-Coder-6.7B）
- 26 个实验中 11 个 success，1 个 RUNNING，9 个待处理
- 易错点：提交新实验时务必检查命令字符串中有无显式 `export CUDA_VISIBLE_DEVICES=N`，不要信任外层注入
- 审稿由 Group C 独立进行（review_chat_id 已配置），Research Director 不参与论文格式/投稿材料准备


---
