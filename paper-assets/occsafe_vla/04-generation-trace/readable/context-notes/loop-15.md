# director / loop_15.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_15.md`
- **Structured JSON:** [`b5007ea414a3872bb774.json`](../../sessions/b5/b5007ea414a3872bb774.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-28T05:42:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34685 cuda:0/1/2/3 + westd-10894 cuda:0/1/2/3，共 8 张，不可越界
- v2 数据纯净性：Cell 1-4 factorial 数据只用 v2 实验，v1 数据（如 detach_ln_s4 CAR=0.738）不纳入 v2 统计，Director 已决策（D067/D071）
- DDL: **2026-05-28 12:00 UTC**，SafeRL Workshop @ RSS 2025
- LIBERO-Object 无 OCC labels → 只能跑 vanilla baseline，不要尝试 OCC 条件
- Paper Agent 和 Main Agent 不直接通信，所有协调经过 Director

### 2. 🖥️ 基础设施快照
- 服务器 1: westd-34685 (connect.westd.seetacloud.com), root, /root/occsafe_vla
- 服务器 2: westd-10894 (connect.westd.seetacloud.com), root, /root/occsafe_vla
- 磁盘: 34685 ~148G free, 10894 ~74G free
- 轮询脚本: PID 61243/61244/61245 on 34685，监控 50000_chkpt → auto kill → eval
- 审稿 chat_id: oc_faa96524df7d6444f5c8cbc48d5a616b（Review 阶段已启动）

### 3. 📊 当前状态
**刚完成：** 8/8 GPU 排满 + registry 全部对齐 + Paper Agent 空窗期 5 项非数据工作完成（appendix/related work/notation/figure/per-task heatmap Cell 1/3/Vanilla 已填真实数据）+ Reviewer claim 强度评估完成（结论：不升级 framing，"≈5pp"改"4-5pp"）

**运行中（8 实验）：**

| 服务器:GPU | exp_id | 类型 | ETA (UTC) |
|-----------|--------|------|-----------|
| 34685:0 | detach_ln_v2_s2 | DDL Cell 4 seed 44 | ~08:36 eval触发 |
| 34685:1 | full_occ_bn_v2_s2 | Cell 1 扩展 seed 44 | ~18:00 |
| 34685:2 | full_occ_ln_v2_s3 | DDL Cell 2 seed 47 | ~06:27 eval触发 |
| 34685:3 | detach_ln_v2_s3 | DDL Cell 4 seed 45 | ~06:27 eval触发 |
| 10894:0 | vanilla_object_s1 | LIBERO-Object seed 43 | ~06:42 eval触发 |
| 10894:1 | detach_ln_v2_s4 | Cell 4 seed 46 (DDL后) | ~11:48 |
| 10894:2 | full_occ_bn_v2_s3 | Cell 1 扩展 seed 45 | ~18:00 |
| 10894:3 | vanilla_object_s2 | LIBERO-Object seed 44 | ~18:00 |

**Paper Agent 待命中，等 Wave 1 数据。**

### 4. 📋 待办
- ~06:27 full_occ_ln_v2_s3 + detach_ln_v2_s3 eval 完成 → 转发 CAR 给 Paper Agent → Wave 1 启动（Cell 2 n=5 + Cell 4 n=3，批量更新 6 个 .tex + 3 个脚本 + 1 个 config + 重算 ANOVA/Cohen's d）
- ~06:42 vanilla_object_s1 eval 完成 → 数据填入 appendix "safety gap universality" 一句
- ~08:36 detach_ln_v2_s2 eval 完成 → Cell 4 n=4 → Paper Agent Wave 2（仅 Cell 4 行更新，30min）
- Wave 1+2 完成后 → 编译验证 → Reviewer 建议的 3 个微调确认（"≈5pp"→"4-5pp"、Limitations 解释 why no Object OCC、vanilla_object appendix）→ 最终提交
- 所有 eval 由轮询脚本自动触发，Agent 承诺 eval 完第一时间汇报 CAR

### 5. 🎯 战略上下文
- 核心 claim: gradient flow 是 BN 下安全损害源，detach 后 aux head 无害（≈Vanilla）。Framing: "normalization-dependent gradient flow effect"，不要升级到更通用的 "gradient flow mechanism"（Reviewer 已评估，LN 行方向一致但未跨 Vanilla 阈值）
- ANOVA interaction ≈ 0 支持 additive model，这是论文结构基础
- Cell 2 (Full OCC LN) 已有 4 eval: [0.740, 0.754, 0.792, 0.798]，第 5 个 ~06:27 到
- Cell 4 (Detach LN) 已有 2 eval: [0.802, 0.826]，第 3 个 ~06:27，第 4 个 ~08:36
- 易错点：Paper Agent 更新清单非常详细（6 .tex + 3 脚本 + 1 config），数据到后不要只改 results.tex 忘了 abstract/intro/discussion/conclusion/appendix 的硬编码数字
- detach_ln_v2_s4 (seed 46) 赶不上 DDL，不影响——Cell 4 n=4 已超目标
- 用户明确要求充分利用显卡，idle GPU 立即派实验，不要空着


---
