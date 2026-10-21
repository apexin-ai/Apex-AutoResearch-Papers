# director / loop_3.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`ff8af6475c301b9ef91d.json`](../../sessions/ff/ff8af6475c301b9ef91d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-15T09:51:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- **用户在等最终裁决数据**：吴俊豪明确说"有结果请艾特我 并让我裁决"。obs-only-r3 完成后必须立即 `director_reply_to_user` 通知，附完整数据表和推荐。
- **D029 kill criterion 已触发**：perdof CRM spatial = 35% vs argmin 34% = +1pp，per-DOF claim 正式死亡。不要再在 perdof 上浪费 GPU。
- **GPU 部署前必须 `nvidia-smi -i &lt;gpu_id>`**：bjb1-18228 cuda:0 连续 3 次双进程冲突（ghost、cron auto-retry、naming 混淆），已写入 feedback memory。
- **kill 进程时必须 kill python 子进程 PID，不能只 kill tmux**：tmux kill 后 python 子进程存活，已有 2 次事故。
- **submit_training_job 的命令必须用 `bash -c "source conda ... && ..."`**：直接写 python 会 EXIT_CODE=127（sh 找不到 conda python）。

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4×RTX 4090): `connect.bjb1.seetacloud.com`, `/root/acr-vla-conformal-refinement`, conda base (`/root/miniconda3/bin/python`)
- **bjb1-32546** (6×RTX 4090): 同上 host 不同端口, 同路径同环境
- **bjb2-28827** (6×RTX 4090): `connect.bjb2.seetacloud.com`, 同路径同环境
- **bjb2-40593** (1×RTX 4090 D): `connect.bjb2.seetacloud.com`, 同路径同环境
- 模型: SmolVLA checkpoint 在各服务器本地 `/root/acr-vla-conformal-refinement/` 下
- W&B/HF: 未配置（不用）
- 总计 17 张 4090，全部 RUNNING

### 3. 📊 当前状态
**刚做完**: D029 logged（perdof kill），Reviewer 和我自己都 RESET_BOTH。上一个 session 最后一步是 post_to_reviewer 请求全卡状态快照，但 Reviewer 在处理前就 hit limit 了，**那个请求已丢失，新 Reviewer 需要重新发**。

**最关键等待项**: bjb1-18228 cuda:3 `eval-acr-spatial-v4-obs-only-r3`，上次查看时正在跑 T9 (0/5 rollouts)，应该已完成或即将完成。这是项目生死数据点。

**RUNNING 实验**:
- bjb1-18228 cuda:0: `eval-mag-obsonly-norm-0p3-r2` (obs_only norm=0.3)
- bjb1-18228 cuda:1: `eval-acr-spatial-v4-scalar-r2` (scalar, 从 T3 开始)
- bjb1-18228 cuda:2: `eval-obs-only-spatial-seed43` (seed43 复现, PID 341873, 部署状态待验证)
- bjb1-18228 cuda:3: `eval-acr-spatial-v4-obs-only-r3` (obs-only restart, T9 应已完成)
- bjb1-32546 cuda:0-5: 6 路 object eval (reconvla/perdof/obs-only/scalar/obs-only-norm02/vla-mean)，各 2-3/10 tasks
- bjb2-28827 cuda:0-5: 6 路 magnitude sweep (perdof+obs_only × norm 0.03/0.05/0.2/0.3)，各 3-4/10 tasks
- bjb2-40593 cuda:0: `eval-mag-obsonly-norm003-b2` (obs_only norm=0.03, T0=90% 已恢复)

### 4. 📋 待办
- **obs-only-r3 完成（可能已完成）→** 合并 parent T0-T5 + restart T6-T9 计算 10-task SR；对比 argmin 34%；≥37% (+3pp) borderline，≥39% (+5pp) Scenario C viable，≤36% 全 fail。**立即 `director_reply_to_user` 通知吴俊豪并附推荐。**
- **cuda:2 seed43 状态不明 →** post_to_reviewer 验证 PID 341873 是否在跑
- **magnitude sweep 完成 →** 画 norm sensitivity curve，判断 obs_only 是否在某个 norm 显著优于 argmin
- **object eval 完成 →** cross-benchmark validation，判断 spatial 是 anomaly 还是 pattern
- **全部数据到齐 →** 综合裁决 Scenario C 是否成立，@ 用户最终决策
- **若 Scenario C 成立 →** 启动 Paper Agent 写 CoRL 初稿（"learned correction" framing）
- **若全 fail →** @ 用户确认项目关闭

### 5. 🎯 战略上下文
**项目存活条件 (D027)**:
1. ~~perdof >> argmin at some norm~~ → FAILING（magnitude sweep 初步 obs_only >= perdof at every norm）
2. ~~perdof > argmin on object~~ → FAILING（前 2 tasks perdof = 0%）
3. **obs_only CRM +5pp stable** → 唯一存活路径，但 Reviewer 预测 spatial 只有 +1-2pp
4. 全 fail → dead

**已知 spatial 数据**: obs_only parent (T0-T5): 90/100/0/40/10/0 = 40%。restart r3 T6=90%。T7-T9 待确认。argmin = 34%。

**易错点**:
- Reviewer 上轮预测 obs_only 最终 ~35-36%（仅 +1-2pp），如果确认则 Scenario C 也 fail on spatial，项目只剩 object + magnitude 两条线
- `output_file` bug：bjb1-18228 restart 实验的 `--output_file` 指向 log 文件路径，JSON 结果会覆盖 log。数据仍可提取（JSON 在文件头部），但读取时注意
- 命名：norm03 = norm=0.3，norm003 = norm=0.03，之前出过混淆事故
- Fisher exact test: 40/100 vs 34/100 → p≈0.37 不显著，这是部署 seed43 复现的原因


---
