# director / loop_4.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`4ad61a2c2e801c6b2afa.json`](../../sessions/4a/4ad61a2c2e801c6b2afa.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T04:26:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westc-26893 上的 cuda:0（1×RTX 4090D），不可占用其他 GPU
- exp-006 第 3 次超时崩溃后已去掉 timeout wrapper，**严禁再加 timeout 参数**——直接 tmux 裸跑
- binary-ours 的 filtering boundary 是 K*=2（保留 depth-0+1，丢弃 depth-≥2），需核对 exp006_filtering_strategies.py 确认实现与论文描述一致
- C3 graduated filtering 已确认不如 binary-ours（D024/D025），论文中**禁止再出现 "graduated may outperform binary" 类断言**——discussion.tex L193-194 修复已派给 Agent 但尚未确认完成

### 2. 🖥️ 基础设施快照
- 服务器：westc-26893 (connect.westc.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/gen-depth-contamination
- Python/环境：待 Agent 确认（AutoDL 实例，可能是 conda base 或 venv）
- 活跃进程：exp-006 在 tmux session 中运行（session 名需确认，之前叫 exp006_final），42/51 runs 完成
- Cron：应用级 cron 监控 exp-006 tmux session
- 模型/数据/HF cache：均在 /root/autodl-tmp/ 下

### 3. 📊 当前状态
**刚做完**：
- D025 论文落地：C3 两版骨架（Version A/B）、intro/abstract C3 降级措辞、Discussion degradation 防御段落——3 个 Worker 全部完成
- 派 Agent 修复 Reviewer 发现的 2 个 critical：TODO_ai_prevalence 引用占位符（intro + discussion 共 3 处）+ discussion.tex L193-194 graduated>binary 错误断言。**Agent 尚未回复确认完成**
- Reviewer 审了 intro/abstract 修改，发现同样的 TODO 引用 + 跨章节矛盾（与已派任务重叠，不需重复派单）

**RUNNING**：
- exp_006_graduated_filtering：42/51 runs，剩余 surprisal ×4 + dsir ×5，ETA ~10:15 UTC（约 05-15）

**等待中**：
- Agent 回调：TODO 引用修复 + L193-194 修复完成确认
- exp-006 完成回调（cron 触发）

### 4. 📋 待办
- Agent 回复 TODO 引用修复完成 → 派 Reviewer 验证全文无残留 TODO 引用
- exp-006 51/51 完成 → Agent 运行 exp006_analyze.py → 汇报完整 6 策略结果（特别关注 surprisal/dsir vs binary-ours）→ 更新 registry DONE
- exp-006 分析完成 → **C3 叙事最终决策**：surprisal/dsir 也不如 binary-ours → Version B 定稿（大概率）；有惊喜 → 混合叙事
- exp-006 GPU 释放 → 立即启动 exp-015 neural probe 重跑（3 模型 Pythia/OLMo/Qwen，~1h）——**这是论文 Main vs Findings 的 single point of failure**
- exp-015 完成 → 立即启动 exp-004 7B cross-scale（~3h）
- 全部实验完成 → C3 章节填数 + neural probe 章节定稿 + Discussion/Conclusion 集成 → re-dream → 提交审稿

### 5. 🎯 战略上下文
- **核心决策链**：D012(2+1 结构) → D016(K*=2 universality) → D024(α 趋势不显著，binary-ours 显著优于 drayson) → D025(论文从 2+1 降为 "K* characterization + practical implications")
- **C3 是 informative negative**：graduated filtering 全 α 值不如 binary-ours，α 趋势统计不显著（Reviewer D024 确认）。论文不能 claim α 单调递增。C3 reframing 为 "binary K*-aware filtering is optimal, validating K*=2 as natural decision boundary"
- **exp-015 比 C3 更重要**：Reviewer 压力测试结论——C3 降级后论文只剩 C1'，是否够 EMNLP Main 取决于 exp-015（K* hierarchy 跨模型验证）和 exp-004（7B scale）。两者都成功 → Solid Main（70%概率）；都没做 → Findings
- **最容易判断错的事**：
  1. 不要以为 exp-006 ETA 已过就完成了——42/51 上次确认，每 run ~45min 不是 25min
  2. C3 abstract/intro 中 "matching or exceeding" 措辞要等全部 51 runs 确认后才能锁定
  3. discussion.tex L193-194 修复可能还没完成——Agent 派了但未收到确认回复
  4. base_model degradation 防御已写好但需要真实引用替换 TODO——这是 blocking issue
- **DDL**：05-25 ARR，余 10 天，时间充裕但 exp-015 + exp-004 是关键路径


---
