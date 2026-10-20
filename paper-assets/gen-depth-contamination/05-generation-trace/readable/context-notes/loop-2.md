# director / loop_2.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`263fc213054b252d8c92.json`](../../sessions/26/263fc213054b252d8c92.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T21:03:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westc-26893:cuda:0（项目 gpu_constraint 白名单，服务器仅 1 块 RTX 4090 D）
- 服务器别名已从 `autodl-4090d` 改为 `westc-26893`，所有 SSH/cron/registry 必须用新名
- Dream report 数据禁止以 "our experiments" 形式出现在论文中（已发生过 CRITICAL）
- 模型名必须是 Qwen2.5-**1.5B**-Instruct（"7B" 错误已出现 3 次被拦截）
- OBD 方向：代码用 P(depth > k)，论文已统一为 P(depth > k)，预测用 argmax 不是 median

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893 (connect.westc.seetacloud.com)，root 账号
- 工作目录：/root/autodl-tmp/gen-depth-contamination
- Python：conda base 环境（/root/miniconda3/bin/python）
- 模型：Qwen2.5-1.5B-Instruct 本地路径（run_exp006.sh 已修为绝对路径）
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃进程：exp-006 graduated filtering **刚崩溃**（bc 缺失，exit 127），Agent 正在修复中（安装 bc 或改脚本第 68 行为纯 bash），修复后立即重跑
- Cron：exp-006 监控 300s 间隔已注册
- API key：openrouter_api_key 已存储（exp-011 用，base_url http://47.94.22.126/v1）

### 3. 📊 当前状态
**刚做完**：exp-003 decoding ablation 4/4 complete（全部 K*=2），D016 universality 确认。论文 introduction 已升级为 final。Paper Agent 完成 4 章（Intro/Related Work/Method/Experiments C1'），全部 0 critical 0 warning。

**RUNNING/PREPARING**：
- exp-006 graduated filtering — **崩溃修复中**，bc 缺失导致脚本退出。base model 评估已完成可复用，50 个 training runs 一个没跑。修复是 1 行改动，Agent 已在处理
- exp-015 neural probe — PREPARING，代码就绪+dry-run 通过，等 exp-006 释放 GPU

**等待中**：
- Agent worker 修复 exp-006 bc 问题的回调
- Reviewer 指出 config4_t12 registry metrics 仍有 null（0v1/2v3/3v4/4v5/top3_features），Agent 需补全
- paper_framing.md D016 universality 更新（Agent 已在处理）

### 4. 📋 待办
- Agent 修复 bc 完成 → 确认 exp-006 重启成功（PID + GPU util）→ 等 ~21h
- exp-006 完成 → 立即启动 exp-015 neural probe（3h）→ K*_learned=2 则升级 claim 为 "data-intrinsic boundary"，K*_learned>2 则 reframe 为 "feature-dependent K*"
- exp-015 完成 → 更新 paper_framing.md → re-dream（验证 median 是否过 weak accept 线）
- exp-006 结果出来 → Paper Agent 写 Experiments C3 + Discussion + Conclusion + Abstract（4 章）
- Registry config4_t12 null metrics → 让 Agent 从 results_exp003_t12/pairwise_auc.json 补全
- 论文完整初稿 target ~05-17，ARR DDL 05-25

### 5. 🎯 战略上下文
- **核心结论**：K*=2 across 8 configs（4 main + 4 decoding ablation），universality narrative（D016）
- **决策链**：D012（2+1 claim 结构）→ D013（C3 单点依赖风险+fallback）→ D014（exp-015 升 P0）→ D015（Dream 行动项）→ D016（universality 替代 controllability）
- **论文命运取决于两个实验**：exp-006（C3 graduated filtering，如果 null result 则 fallback 到 "informative negative"，仍可投 Main）和 exp-015（K*_learned=2 → 强 claim，K*_learned>2 → 需 reframe 但仍 viable，Reviewer 评估 7/10）
- **易错点**：(1) 不要引用 Dream report 数据作为实验结果 (2) transfer retention 80-92% 不能量化为 "70-85% text-intrinsic"（不等价） (3) DPI 是 motivation 不是 contribution (4) θ=0.60 是 load-bearing threshold，Qwen-cont CI_lower 仅超 0.0015，论文已承认 marginal (5) exp-003 用 rewrite mode 不是 continuation，特征排名不与 continuation-mode 横向比较
- **Dream 评估**：Best=Weak Accept, Median/Worst=Weak Reject。升级条件：θ sensitivity ✅ + greedy ablation ✅ + K* under learned features（exp-015 待做）+ graduated filtering（exp-006 待做）


---
