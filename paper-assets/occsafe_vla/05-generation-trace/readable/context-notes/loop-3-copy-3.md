# reviewer / loop_3.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`bf92f2c5bf639139174c.json`](../../sessions/bf/bf92f2c5bf639139174c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-22T18:20:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-10894 和 westd-34685 各 4 GPU（cuda:0-3），项目白名单 gpu_ids=[0,1,2,3]，两台都可全用
- Checkpoint 路径统一在 `/root/autodl-tmp/checkpoints/{exp_name}/`，不是 `/root/occsafe_vla/checkpoints/`
- 训练日志在 `/root/runs/occsafe_vla/{exp_id}.log`（不是 `/root/occsafe_vla/logs/`，那个路径不存在）
- ssh_read_only 不支持 `&&`、`|`、`;` 等 shell metacharacter，必须分开调用
- Rotation 脚本 KEEP=1（`/root/checkpoint_rotation.sh`），每台服务器一个，覆盖当前所有 4 个实验。不要创建新的或修改 KEEP 值
- OCC 条件的 mvp_occ_s1 registry 有旧数据（conclusion=negative），后来重跑为 occ_s1_fresh（conclusion=success），引用数据时用 occ_s1_fresh

### 2. 🖥️ 基础设施快照
- **westd-10894**: 4× RTX PRO 6000 (97887 MiB)，`/root/occsafe_vla`，conda env `occsafe`（`/root/miniconda3/envs/occsafe/bin/python3.10`）
  - 实验: ablation_random_occ_s2(cuda:0), ablation_occ_detach_s2(cuda:1), depth_s2(cuda:2), depth_s3(cuda:3)
  - Rotation: `/root/checkpoint_rotation.sh`（nohup 后台），日志 `/root/rotation_new.log`
  - 磁盘: `/root/autodl-tmp` 154GB free (39% used)
- **westd-34685**: 同配置
  - 实验: cutoff_s0(cuda:0), depth_s0(cuda:1), depth_s1(cuda:2), cutoff_s1(cuda:3)
  - Rotation: `/root/checkpoint_rotation.sh`（nohup 后台），日志 `/root/rotation_new.log`
  - 磁盘: `/root/autodl-tmp` 270GB free (24% used)
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/`
  - registry: `registry.yaml`，paper 文件: `docs/paper/`，framing: `paper_framing.md`

### 3. 📊 当前状态
最后一次全面检查时的进度（约 UTC 18:00, May 22）：

| 实验 | 服务器 | 步数 | 进度 | 速度 | 剩余~h |
|------|--------|------|------|------|--------|
| random_occ_s2 | 10894 | 38595 | 77% | 1.07 it/s | ~3.0 |
| detach_s2 | 10894 | 38705 | 77% | 1.09 it/s | ~2.9 |
| depth_s2 | 10894 | 35480 | 71% | 1.08 it/s | ~3.7 |
| depth_s3 | 10894 | 35430 | 71% | 1.08 it/s | ~3.8 |
| cutoff_s1 | 34685 | 30729 | 61% | 1.04 it/s | ~5.2 |
| depth_s0 | 34685 | 30707 | 61% | 1.05 it/s | ~5.1 |
| depth_s1 | 34685 | 30634 | 61% | 1.06 it/s | ~5.1 |
| cutoff_s0 | 34685 | 28724 | 57% | 1.04 it/s | ~5.7 |

**刚完成的工作**：
- 审查了 Option 4 分析论文 story arc 定稿，已 post 给 Director（WARNING 级）
- 核心审查意见：Finding 1+2 应合并为一个 contribution，加 study design methodology 作为独立贡献，per-task + temporal dynamics 独立成 section
- 指出 OCC s2 可能是异常 seed（T4 TSR=0.36 严重偏低），Random vs OCC 排序建立在 2v3 不对等比较上

**等待中**：
- 无 Worker 回调或 Cron 待处理
- Director 可能回复 story arc 审查意见

### 4. 📋 待办（条件触发式）
- **cutoff_s1 到达 step 35000**（约 UTC ~19:00-19:30 May 22）→ 检查 AUX 输出验证 occ_loss 是否归零。这是 OCC-Cutoff 条件的关键验证点
- **cutoff_s0 到达 step 35000**（约 UTC ~19:40-20:00）→ 同上验证
- **random_occ_s2 / detach_s2 完成**（约 UTC ~21:00）→ 触发 eval audit。detach_s2 是 Detach 3rd seed，直接决定 Finding 1 显著性。如果 detach_s2 CAR > 0.770，Detach vs Vanilla 差异可能不显著，需走补救方案（per-task hard-task analysis + bootstrap CI）
- **depth_s2/s3 完成**（约 UTC ~22:00）→ depth 4-seed 齐全后触发 50r eval + Depth MVP Gate 判定
- **所有 8 实验完成** → 验证 rotation 脚本正常清理最终 checkpoint 外的残留，检查磁盘
- **Director 回复 story arc 审查** → 可能要求补充审查或修改 paper_framing.md

### 5. 🎯 战略上下文
- **D017 核心决策**：梯度流正则化是主导机制（Random≈OCC > Vanilla > Detach），空间内容次要
- **论文路径**：Option 4 分析论文（AAAI 2027，Abstract Jul 21，Paper Jul 28）
- **Depth 是最大不确定性**：决定 Path A/B/C/D。Path B（Depth≈Random≈OCC，概率 40-50%）最可能，此时论文本质上只有一个核心 finding（梯度流正则化）
- **Depth MVP Gate 已预注册**（2026-05-22 09:30 UTC 锁定）：4-seed mean CAR bootstrap 95% CI 下界 > 0.780 + TSR ≥ 0.870
- **易错点**：
  1. OCC 数据引用时注意用 occ_s1_fresh 而非 mvp_occ_s1（后者 s1 是旧的有问题的 run）
  2. Random vs OCC 的 0.9pp 差异极其脆弱（2 vs 3 seeds），不要在 random_s2 到达前下定论
  3. cutoff_s0 曾出过 cron false positive（报 failed 但实际在跑），如果再收到 failure 通知先 tail log 验证
  4. nvidia-smi 瞬态 0% 利用率是正常的（checkpoint save 期间），需要二次采样确认
  5. 两台服务器的旧 rotation 脚本（`/root/occsafe_vla/checkpoint_rotation.sh`）只覆盖旧实验，当前有效的是 `/root/checkpoint_rotation.sh`


---
