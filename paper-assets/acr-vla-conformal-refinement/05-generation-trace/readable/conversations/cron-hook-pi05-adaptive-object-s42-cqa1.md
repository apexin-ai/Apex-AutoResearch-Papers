# cron hook pi05 adaptive object s42 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/cron_hook_pi05-adaptive-object-s42-cqa1.jsonl`
- **Structured JSON:** [`65fa57c6b940f9e11549.json`](../../sessions/65/65fa57c6b940f9e11549.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

1 recorded events

### User

_source line 1 · 2026-05-27T05:23:51.353727+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #29。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单 29 张，6 台服务器：bjb1-18228(0-3), bjb1-32546(0-5), bjb2-28827(0-5), cqa1-32758(0-5), westd-49937(0-5), bjb2-24035(0)。bjb2-40593 已掉线，禁用
- westd-49937 是 Blackwell RTX PRO 6000，与 4090 有 ~3pp 系统偏差（D158）。Table 数据必须同 GPU 型号配对对比
- SmolVLA CRM checkpoint 唯一正确路径：`/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`（`crm_smolvla_3suite_unified` 不存在）
- C001 硬约束：每个实验启动前必须 `nvidia-smi` 检查目标 GPU，显存 > 500MB 不启动
- CoRL 2026 DDL = **2026-05-28 20:00 北京时间**

### 2. 🖥️ 基础设施快照
- 所有服务器账号 root，项目路径 `/root/acr-vla-conformal-refinement`
- 服务器列表：bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758, westd-49937, bjb2-24035
- Python/conda：用 `detect_image` 先探测，aml-train 镜像用 `/root/miniconda3/bin/python`
- 活跃进程（5 个 RUNNING，cron 均在监控中）：
  - bjb1-18228: smolvla-tau015-long-s43 (cuda:0, PID 555572), smolvla-tau025-long-s43 (cuda:1, PID 556705), smolvla-tau035-long-s43 (cuda:2, PID 557567)
  - cqa1-32758: smolvla-vla-only-long-n20-s42 (cuda:0, PID 722840), smolvla-vla-only-long-n20-s43 (cuda:1, PID 724487)
- 磁盘警告：cqa1-32758 `/autodl-pub` 94% 已用；bjb2-24035 nvidia-smi 分区 90% 已用

### 3. 📊 当前状态
- **论文**：v54 14页，Table 1 + Table 2 锁定，Step 5 收敛，D169 Appendix τ-sweep patch 完成
- **审稿**：submit_paper_to_review 已发，⚠️ 等待用户审批 review mode（已多次提醒）
- **τ-sweep 数据**：scatter_data.csv 89 行，5 个补充实验仍在跑（3 个 SmolVLA τ-sweep long s43 + 2 个 SmolVLA vla-only long n20）
- **registry 总计**：1231 实验，RUNNING 5，DONE 1024（success 625 / negative 94 / failed 98 / killed 207），PREPARING 185，QUEUED 10，ANALYZING 1
- **待修正**：6 个 stale RUNNING（bjb1-18228 4个 + bjb2-28827 2个），需要确认是否已死并标记
- **Agent 稳定性问题**：连续 7 次 reset 后只处理 1-2 条消息就死，已向 Manager 升级

### 4. 📋 待办
- 5 个 RUNNING cron 回调到达 → 按 on-experiment-done 处理（更新 registry + scatter_data.csv + report.md + 汇报 Director）
- 用户审批 review mode → 收到审稿报告后按 P2 处理
- 6 个 stale RUNNING 确认死亡 → update_registry 标记 killed/failed + 释放 GPU 记录
- 所有 τ-sweep 完成 → 更新 scatter_data.csv 最终版 + Appendix 图表刷新
- DDL 前 paper_framing.md 需更新 D165-D169（P2，非阻塞）

### 5. 🎯 战略上下文
- **核心 claim**：MC1=Adaptive ≥ CRM on 3/4 suites + recovery 19-38%；MC2=cross-suite trigger rate ↔ Δ 单调正相关，within-suite τ-sweep 是 sensitivity analysis（SR 对 τ 稳健）；MC3=cross-VLA 模型能力依赖
- **D168**：Goal CRM harm 修正为 13.2pp（非 14.5pp），recovery 计算已纠正
- **D169**：τ-sweep 在 Appendix 定位为 sensitivity/robustness analysis，不是 MC2 within-suite 证据
- **易错点**：(1) pi05 376 missing_keys 是正常行为不是 bug（`_fix_vision_tower_keys` remap）(2) Goal VLA-only 基线选的是 May24=96.7±1.0%（Director 决策，非 May22）(3) EXIT_CODE=0 不等于实验成功，必须检查日志无 OOM + SR 无异常
- **DDL 紧迫**：~34h（截至 ROADMAP 更新时），主要实验已完成，剩余 5 个 τ-sweep 补充实验是锦上添花非阻塞

## 可查的历史
前 290 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:pi05-adaptive-object-s42-cqa1",
  "source": "system:ralph_loop"
}
```

</details>

---
