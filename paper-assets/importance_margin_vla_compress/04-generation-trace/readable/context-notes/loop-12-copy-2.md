# agent / loop_12.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`6215c3006f3dd20703c3.json`](../../sessions/62/6215c3006f3dd20703c3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-24T00:13:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 14 张：westd-27271:cuda:0/1, cqa1-33015:cuda:0-3, westd-41074:cuda:0-3, westd-38929:cuda:0-3。白名单外的 GPU 即使 Director 指示也必须 push back
- eval_pi05_l2norm_k095_object_seed42_v3 是重复的 CRON 回调（本 session 收到两次），v2 已成功 (SR=98.2%)，不要重跑
- submit_training_job 的 command 必须用 `bash -c "..."` 包装，tmux 用 sh 不是 bash，不包会 EXIT_CODE=127
- X-VLA 实验工作目录在 `/root/autodl-tmp/X-VLA`，π0.5 实验工作目录需要确认（不同服务器可能不同）
- CoRL 2026 Abstract **May 26**（2天后），Paper **May 29**（5天后）——时间极紧

### 2. 🖥️ 基础设施快照
- **westd-38929**：X-VLA eval 主力。模型 `/root/autodl-tmp/X-VLA-Libero`，代码 `/root/autodl-tmp/X-VLA`。HF_HOME=/root/autodl-tmp/.hf_cache。4×GPU 分配
- **westd-41074**：π0.5 eval 主力。4×GPU 分配。日志目录可能缺失（v3 失败疑似 logs/ 不存在导致）
- **cqa1-33015**：π0.5 eval。4×GPU 分配。4 个实验在跑 (pid 304615/304879/305122/305386)
- **westd-27271**：2×GPU 分配。Worker ops:deploy_e3_xvla_openvla_westd27271 正在部署 E3 实验
- 活跃进程：westd-38929 pid 250272 (xvla_random_k05_goal), pid 251117 (xvla_random_k09_long)；cqa1 4 个 pi05 实验
- GPU 健康缓存对 westd-38929 无数据（"no data yet"），需要下轮 SSH 刷新

### 3. 📊 当前状态
**刚完成**：
- eval_pi05_l2norm_k095_object_seed42_v3 标记 DONE/failed（v2 已有数据，不影响）
- eval_xvla_l2norm_k05_long_seed42 确认成功并标记 DONE/success (SR=45%)——cron 误报 miss
- eval_xvla_l2norm_k07_long_seed42 标记 DONE/failed（westd-38929:gpu0 进程死亡无日志）
- 已向 Director 汇报上述三个实验状态
- 飞书结果卡片已发

**正在等待**：
- Worker `worker_ops_resubmit_xvla_l2norm_k07_long_20260523T080300`：诊断 k07 失败根因 + 以 v2 重新提交到 westd-38929
- Worker `worker_ops_deploy_e3_xvla_openvla_westd27271_20260523T073129`：部署 E3 到 westd-27271
- Worker `worker_ops_fill_4_gpus_e3_seed43_20260523T075512`：铺 westd-41074 的 seed43 实验
- Worker `worker_ops_harvest_xvla_random_k09_long_20260523T080003`：收割 xvla_random_k09_long 结果
- 6 个 GPU 实验在跑（2 westd-38929 + 4 cqa1），预计各 1-2h 完成

**Registry PREPARING 实验（37 个待铺）**：包括 pi05 seed43 验证系列、smolvla spatial 系列、xvla object 系列等

### 4. 📋 待办（条件触发式）
- Worker resubmit_xvla_l2norm_k07_long 完成 → 确认 v2 已提交并有 cron 监控，更新 registry spec
- Worker harvest_xvla_random_k09_long 完成 → 读取结果，更新 registry，填 Table 2 对应格子
- Worker fill_4_gpus_e3_seed43 完成 → 确认 westd-41074 4 卡全在跑，更新 registry
- Worker deploy_e3 完成 → 确认 westd-27271 实验已启动
- cqa1 4 个 pi05 实验完成 → 收割结果，更新 Table，空出 GPU 铺下一批（smolvla spatial 等 PREPARING 实验）
- eval_xvla_l2norm_k07_long_seed42_v2 完成 → 与 k=0.5(45%), k=0.9(27.5%), k=0.95(47.0%) 对比，确认非单调曲线形状
- 所有 Table 2 缺口填完 → 向 Director 汇报 E1 完成，推进 E2(OpenVLA multi-suite) + Writing fixes

### 5. 🎯 战略上下文
- **D181 行动矩阵**：正式审稿 5/10 weak reject，6 Must-Fix + 8 Should-Fix。当前执行 E1(Table 2 fill 9 gaps)、E3(cosine similarity)、E4(inference latency)
- **核心发现**：L2norm 在 Long suite 上非单调——k=0.5(45%) > k=0.9(27.5%) < k=0.95(47.0%)。这支持 D173/D174 的"小N危险区"观察
- **2-axis 框架**：connector architecture × task complexity。6 模型 × 4 LIBERO 套件
- **易错**：
  - 不要把 eval_pi05_l2norm_k095_object_seed42_v3 的重复 CRON 当新失败处理——它会再来一次
  - westd-38929 的 GPU 健康数据缓存为空，首次查需要 SSH 触发
  - xvla 实验 registry 之前 summary view 不含 spec/server 字段，必须 update_registry 才能看到完整数据（read_registry 的 summary 字段过滤导致）
  - report.md 的 AUTO-FACTS 区自动生成，不要手动改


---
