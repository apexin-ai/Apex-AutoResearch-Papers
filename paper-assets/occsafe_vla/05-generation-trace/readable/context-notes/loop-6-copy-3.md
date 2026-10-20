# reviewer / loop_6.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`97bc87bbc7a788b505e3.json`](../../sessions/97/97bc87bbc7a788b505e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-25T19:25:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅 westd-10894 cuda:0-3 + westd-34685 cuda:0-3，越界立即 CRITICAL
- C002：cutoff/reverse_cutoff 实验禁止 --resume（batch_idx bug 未修复，resume 后 step 从 0 计数导致 cutoff 阈值不可达）
- D050：v1 BN 数据不得与 v2 数据混合做 ANOVA（代码版本共线）
- D052：v1≠v2 已确认（Full OCC BN v2 CAR=0.746 vs v1 CAR=0.832，差 8.6pp）
- Resume 实验 step 计数器从 0 开始（非 20000），eval 时需取 local step=30000 checkpoint（= 总 50K steps），不要取 step 50000

### 2. 🖥️ 基础设施快照
- 服务器：westd-10894 + westd-34685，均为 root 账号，4× NVIDIA RTX PRO 6000 Blackwell (98GB)
- 工作目录：/root/occsafe_vla（远程）；本地 workspace: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/
- Python：/root/miniconda3/envs/occsafe/bin/python3.10（conda env: occsafe）
- 模型：/root/autodl-tmp/models/openvla-7b；checkpoints: /root/autodl-tmp/checkpoints/
- 数据：/root/autodl-tmp/data/modified_libero_rlds/；occ_data: /root/occsafe_vla/occ_data
- 日志：/root/runs/occsafe_vla/*.log
- 8/8 GPU 全满（最后验证 ~19:22 UTC）：
  - 10894:0 cutoff_45k_s2_v2 (PID 4294)
  - 10894:1 mvp_occ_s3_v2 resume (PID 11723)
  - 10894:2 full_occ_ln_s3_v2 resume (PID 7027)
  - 10894:3 ablation_occ_detach_s3_v2 resume (PID 7243)
  - 34685:0 detach_bn_v2_s0 (PID 5166)
  - 34685:1 detach_bn_v2_s1 (PID 2867)
  - 34685:2 detach_bn_v2_s2 (PID 3084)
  - 34685:3 full_occ_bn_v2_s1 (PID 7427)

### 3. 📊 当前状态
本轮主要工作：集群重启后的崩溃恢复审查。发现并上报了 resume bug（FileNotFoundError: resume_step=None 拼入路径），Agent 修复后 7/8 恢复，又追踪到 full_occ_bn_v2_s1 遗漏和 mvp_occ_s3 缺失，最终 8/8 GPU 填满。ROADMAP 经 4 轮修正后与实际状态一致。

- 10894 s3 resume 实验 ~May 26 02:00 UTC 完成 → eval + CKA（叙事门控决策点）
- 34685 D051 实验 ~May 26 07:00 UTC 完成 → eval → v2 ANOVA
- 无等待中的 Worker 回调或 Director 决策

### 4. 📋 待办（条件触发式）
- s3 resume 完成通知到达 → 审查 eval 结果，核对 checkpoint 路径是 local step 30000（不是 50000）
- ablation_occ_detach_s3 eval CAR 出来 → 对照叙事门控：<0.750 Branch A / 0.770-0.780 Branch B / >0.780 Branch C
- D051 eval + v2 ANOVA 完成 → 审查交互效应 p 值，判断 Plan A（factorial story）vs Plan B（替代 framing）
- 论文章节提交审查 → 先查 Agent 是否加载了 red-section skill（合规 L1），再按模式 B 五维度审
- 任何新实验提交 → 核查 CUDA_VISIBLE_DEVICES 在 C001 白名单内

### 5. 🎯 战略上下文
- 核心问题链：D050 发现 BN 用 v1 代码 / LN 用 v2 代码（共线）→ D051 用 v2 重建 BN cells → D052 确认 v1≠v2（差 8.6pp）→ 交互效应存活概率仅 10-15%
- **最可能结局**：v2 ANOVA 交互效应消失，paper framing 需 pivot 到 Plan B（B1 机制分析 / B2 normalization 主效应 / B3 cautionary study）
- 易错点 1：resume 实验 step 计数器从 0 开始，千万不要让 Agent 取 step 50000 checkpoint 做 eval（那是多训了 20K 步的过拟合模型），正确 checkpoint 是 local step 30000
- 易错点 2：ROADMAP 更新频繁且多次与实际不符，不要信 ROADMAP 标注的 GPU 状态，每次都 SSH 独立验证
- 易错点 3：本地 workspace 文件和远程服务器文件可能不同步（L1 #5），断言"未修改"前两边都读
- CoRL 2026 deadline May 29，零余量


---
