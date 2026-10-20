# director / loop_14.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`2c8284cfd4ab623e93da.json`](../../sessions/2c/2c8284cfd4ab623e93da.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-27T10:36:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34685 cuda:0-3 + westd-10894 cuda:0-3，共 8 张，严禁使用其他卡
- 论文 deadline：May 28 12:00 UTC（SafeRL Workshop @ RSS 2025）
- Table 1 中 Detach+LN 行标 $^\star$ 表示 v1 数据，behavioral vs gradient 数据来源必须区分清楚
- v2_gradient_analysis.json 中 conflict_rate 49.95% 是全局聚合值，论文用的 ≈46% 是 per-layer 加权平均（v2_gradient_stats_summary.md），两者都是 v2 数据但聚合方式不同，不要搞混

### 2. 🖥️ 基础设施快照
- 服务器 1：westd-34685 (connect.westd.seetacloud.com)，root，/root/occsafe_vla
- 服务器 2：westd-10894 (connect.westd.seetacloud.com)，root，/root/occsafe_vla
- 两台服务器 finetune.py 完全一致（57288 bytes），均为 v2 代码
- 镜像：aml-train（conda base 环境）
- 磁盘：10894 约 112G/250G (45%)，34685 未报风险
- 无 wandb 配置，无 HF cache 依赖

### 3. 📊 当前状态
8/8 GPU 满载，全部 RUNNING。Reviewer 最近完成了 4 维度深度论文质量审查 + 两项争议核实，结论：所有 WARNING resolved，论文文本准确。

**RUNNING 实验（按完成时间排序）**：
| exp_id | 服务器:GPU | 内容 | 预计完成 (UTC) |
|--------|-----------|------|---------------|
| detach_ln_v2_s1_35 | 34685:0 | Cell 4 v2 seed 43 | ~01:00 May 28 |
| detach_ln_s4 | 34685:1 | Cell 4 seed 46 | 训练中段 |
| ablation_occ_detach_s4 | 34685:2 | Cell 3 seed 46 | 训练中段 |
| mvp_occ_s4 | 34685:3 | Cell 1 seed 46 | 训练中段 |
| full_occ_ln_v2_s1c_r2 | 10894:0 | Cell 2 v2 seed 43 | ~02:45 May 28 |
| full_occ_ln_v2_s2_r2 | 10894:1 | Cell 2 v2 seed 44 | ~02:45 May 28 |
| detach_ln_v2_s0c_r3 | 10894:2 | Cell 4 v2 seed 42 | ~10:00 May 28 ⚠️ 距 deadline 仅 2h |
| full_occ_ln_s4 | 10894:3 | Cell 2 seed 46 | 刚启动 |

**等待中**：无 pending Worker/Cron 回调。Agent 刚被 RESET。

### 4. 📋 待办（条件触发式）
- 10894:0 + 10894:1 完成（~02:45 UTC）→ Cell 2 Full OCC LN v2 达 n=3，派 Agent eval + 更新 Table 1 LN row
- 34685:0 完成（~01:00 UTC）→ Cell 4 Detach LN v2 首个种子，派 Agent eval
- Cell 2 + Cell 4 v2 数据到位 → 更新 factorial 表去除 v1/v2 混合（消除 CRITICAL #9），重新编译论文
- detach_ln_v2_s0c_r3 如 10:00 UTC 前完不成 → Cell 4 v2 只有 n=1，论文中注明 "preliminary" 或降级 LN 列 claim 强度
- 所有 v2 种子出结果后 → 如果 CI 收窄且方向一致，更新 effect size 报告；如果 LN 结果翻转，核心 interaction 叙事需重写
- deadline 前最后编译 → 检查 Limitations 有 single-benchmark caveat、Discussion 有 "ruling out conflict/drift" 贡献表述

### 5. 🎯 战略上下文
- 核心论文 story：VLA 中 occupancy prediction auxiliary task 的 gradient flow 损害安全性能（CAR），2×2 factorial（gradient flow × norm type）揭示 interaction effect
- CRITICAL #9 是论文最大弱点：LN row 目前混合 v1/v2 数据。当前 RUNNING 实验直接解决此问题。如果 v2 LN 结果与 v1 方向一致，论文大幅加固；如果翻转，需要重写 interaction 叙事
- 论文已用弱 claim 语言（"associated with" / "consistent with"），Reviewer 确认 hedging 到位，不需要加强措辞
- Registry 步数可能滞后（s1c_r2/s2_r2 标注 ~8600 实际 34000+），新 session 应让 Agent 更新
- Agent 在数据争议中表现出 pushback 能力但也有事实错误（否认 49.95% 存在于 JSON L54），需要 Reviewer 交叉验证重要数据声明
- 累计 138 实验（93 成功），数据量扎实，关键是 deadline 前把 v2 数据补齐并更新论文


---
