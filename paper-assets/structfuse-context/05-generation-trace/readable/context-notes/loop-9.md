# director / loop_9.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`757817dbec01d7bac4a7.json`](../../sessions/75/757817dbec01d7bac4a7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-15T10:01:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 bjb1-42106 的 cuda:0 和 cuda:1，严禁在其他设备启动实验
- paper_framing.md 的 Claim 1 数字已标注过时（"+1.6-2.0pp" 是 pilot 值），任何写作引用必须用 provisional 格式（D049）
- Claim 1 不能用 "challenges the assumption"/"significantly outperforms"——已软化为 "reliable improvement at zero additional cost"（D049）
- Claim 2 必须用 exploratory 措辞（"our analysis suggests"/"we observe"），不能用因果断言（D035）
- dataflow-aware 策略的论文描述必须匹配代码实现（BM25 排序 + 结构过滤，不是 pretrained embedding similarity）（D041）
- s42 用了旧 regime（3 epochs 无 early stop，D026），与 s43/s44（2 epochs + patience=2）不一致——混入 CI 计算会被审稿人攻击（D047）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com)，用户 root
- 工作目录：/root/structfuse
- 训练数据：/root/autodl-tmp/structfuse/full_m2_training_data/
- M2 输出：/root/structfuse/outputs/m2_full_qwen/ 和 m2_full_starcoder/
- 活跃进程：PID 337267（Qwen chain，cuda:0，已运行 ~20h）、PID 519791（StarCoder chain，cuda:1）
- plan_005 脚本：/root/structfuse/scripts/run_plan005_s43.sh（dry-run 通过，等 GPU 空闲执行）
- API key：openrouter_api_key 在 secrets vault（plan_003 SWE-bench E2E 评估用）
- 无 conda env，无 W&B 配置

### 3. 📊 当前状态
**刚做完**：本轮完成 D047-D049 三个重大决策；论文 Introduction v1 / Method v1 / Related Work v1 全部写完并经 Reviewer 审查修正；paper_framing.md D049 叙事软化 + 状态刷新；checkpoint criterion table + fixed-checkpoint table 数值全部修正；val_loss divergence 讨论段落完成。

**RUNNING 实验**：
- m2_full_qwen_continued：Qwen chain，embed_s44 在 step 850（⚠️ @500 R@1=0.5942 vs random best=0.6009，delta 可能为负）
- m2_full_starcoder_resumed：StarCoder chain，random_s44 在 step 300
- m1_reextract_v2：M1 重提取，进度 ~90.5%

**Agent 队列**：有 2 条排队指令（Related Work v1 修正 4 项 + Method v1 修正超参确认），Agent 正在处理。

### 4. 📋 待办（条件触发式）
- embed_s44 完成 → 对比 random_s44 best=0.6009：如果 delta 为负，Claim 1 进入 Scenario B/C（Reviewer 已准备好 4 档措辞），需要立即与 Reviewer 评估 3-seed 均值
- M2 Qwen 全 9 runs 完成 → 第一优先级：plan_005 分层分析（脚本已就绪 run_plan005_s43.sh）+ pool=50 重新评估所有 best checkpoint（D042/D048，这是支撑 Claim 1 的最关键数据）
- GPU 释放后 → s42 重跑（2-epoch+early-stop regime，D047）+ plan_018 Phase 2（BM25 训练）+ plan_015（dynamic mining）
- 三 seed 数据到齐 → paper_framing.md 填入最终数字替换 placeholder + Intro/Method/RW 数字 TODO 填充
- StarCoder 全部完成 → 跨 encoder 对比分析，更新 Claim 1 "across encoders" 表述

### 5. 🎯 战略上下文
**核心焦虑**：Claim 1 delta 从 pilot +2.0pp 缩水到 M2 s43 +0.52pp，且 s44 @500 已显示 -0.67pp。如果 3-seed 均值接近零，Claim 1 需要大幅重构。Reviewer 已准备 Scenario A-D 四档措辞（D045 审查），D049 已做预防性软化。

**最易判断错的事**：
1. 不要因 delta 小就 panic 降级会议目标——pool=50 评估是翻盘点（pool=8 噪声 ±0.5pp 与 delta 同阶，pool=50 可能给出更清晰信号）
2. 不要只看 best_by_R@1——fixed-checkpoint 对比是更稳定的证据（s43 三个 checkpoint 均 embedding > random）
3. 不要做 goalpost-moving（Reviewer 明确警告：仅在 delta 缩水后转向 training dynamics 叙事会被审稿人察觉）——双轨并报是正确策略（D049）
4. StarCoder seed 间方差极大（s42=0.4604, s43=0.4912, 差 3pp），multi-seed 统计必不可少

**决策链**：D026(s42 regime) → D035(Claim2 exploratory) → D036(R@1 checkpoint) → D041(dataflow=BM25) → D042(pool=50) → D044→D045(best_by_R@1) → D047(s42 regime 不一致+两层统计) → D048(s43 delta +0.52pp) → D049(软化 framing+双轨并报)


---
