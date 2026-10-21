# director / loop_12.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`d30a0415bc6f6fc331a9.json`](../../sessions/d3/d30a0415bc6f6fc331a9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-27T00:52:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-10894 (4×A100) + westd-34685 (4×A100)，共 8 卡
- 10894 有系统性 stall 历史（驱动层 stuck utilization counter），每次启动后 30min 必须监控确认
- 34685:cuda:0 有未注册孤儿进程 PID 681204（detach_ln_v2_s1, seed=43, step 4608+）——与 10894:cuda:3 的 detach_ln_v2_s1c 重复，**下一步必须处理这个冲突**
- Cell 2 的 full_occ_ln_v2 seed=42 (s0) 多次失败未成功启动，是 CRITICAL 数据缺口

### 2. 🖥️ 基础设施快照
- westd-10894：4×A100 80GB，项目路径 /root/occsafe_vla/
- westd-34685：4×A100 80GB，项目路径 /root/occsafe_vla/，磁盘 ~58% free
- 产出路径：/root/occsafe_vla/artifacts/（eval JSON 存这里）
- 10894 磁盘 ~51%，34685 磁盘 ~42%

### 3. 📊 当前状态
**8/8 GPU 应在运行（但有冲突需处理）：**

34685:
- cuda:0: detach_ln_v2_s1 (Cell 4, seed 43) — 未注册孤儿，step ~4608+
- cuda:1: detach_ln_s4 (Cell 4, seed 46, n=5 expansion)
- cuda:2: ablation_occ_detach_s4 (Cell 3, seed 46, n=5)
- cuda:3: mvp_occ_s4 (Cell 1, seed 46, n=5)

10894:
- cuda:0: full_occ_ln_v2_s1c (Cell 2, seed 43)
- cuda:1: full_occ_ln_v2_s2 (Cell 2, seed 44)
- cuda:2: detach_ln_v2_s0c (Cell 4, seed 42)
- cuda:3: detach_ln_v2_s1c (Cell 4, seed 43) — **重复**，远落后于 34685 版本

**等待中**：Reviewer 建议 kill 10894:cuda:3 重复实验，用释放的 GPU 启动 full_occ_ln_v2_s0（Cell 2 seed 42）。Director 已发指令但 Agent 未执行即被 reset。

### 4. 📋 待办
- Agent 就绪 → 立即执行：kill 10894:cuda:3 detach_ln_v2_s1c + 注册 34685 PID 681204 + 在 10894:cuda:3 启动 full_occ_ln_v2 seed 42 (Cell 2)
- 34685 训练完成（~12:30-13:15 UTC）→ eval + 轮替启动 Cell 2/4 补种子
- 10894 训练完成（~14:30 UTC）→ eval + 数据录入
- 全部 eval 完成 → factorial ANOVA（每 cell n≥3）→ 更新论文数据 → Paper Agent patch

### 5. 🎯 战略上下文
**Factorial 2×2 设计**（gradient_flow × norm_type）核心发现：Detach+LN (0.802) > Detach+BN (0.767) > Vanilla (0.745) > Full+LN (0.740) ≈ Full+BN (0.725)。Ordinal interaction 确认梯度方向是主效应。

**数据现状**：Cell 1 n=3, Cell 2 n=1(⚠️), Cell 3 n=4, Cell 4 n=1(⚠️), Vanilla n=3。Cell 2/4 急需补到 n≥3。

**易错点**：
- M074 教训：Agent reset 后旧队列指令会被新 session 当最新执行。reset 前务必更新队列到最新状态
- 10894 反复出问题但每次都能恢复（不是真硬件故障），不要轻易永久放弃
- 多个 CRON "需要判断" 通知堆积时大部分是已 kill 实验的残留，用 replace_agent_queue 统一清理而不是逐条处理
- Deadline: May 29 提交，May 28 需要论文数据更新完成


---
