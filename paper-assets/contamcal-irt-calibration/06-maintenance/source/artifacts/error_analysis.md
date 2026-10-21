# 系统性失败案例分析

**分析日期**: 2026-05-20  
**数据源**: Registry (conclusion=failed: 68 条, conclusion=killed: 37 条, 总计 105 条)

---

## 1. 按失败原因分类统计

| 类别 | 数量 | 占比 | GPU-hours 浪费估算 |
|------|------|------|-------------------|
| 实验废弃/设计变更 | 20 | 19.0% | ~15h (含 73% 被杀的 d100 SFT) |
| GPU 进程冲突/重复提交 | 18 | 17.1% | ~12h (GPU 2 六连撞最严重) |
| Cron/监控误报 | 16 | 15.2% | ~0h (多数实际已完成) |
| 配置/命令/代码错误 | 13 | 12.4% | ~5h |
| 外部 kill / Worker 误杀 | 11 | 10.5% | ~10h (d100_a32_v2 在 73% 被杀最痛) |
| 磁盘满 | 4 | 3.8% | ~4h |
| 数据/模型/算法设计问题 | 4 | 3.8% | ~3h |
| CUDA_VISIBLE_DEVICES 绑定失败 | 3 | 2.9% | ~1h |
| OOM (纯显存不足) | 2 | 1.9% | ~2h |
| 平台基础设施 (SeetaCloud) | 2 | 1.9% | ~3h |
| 其他 (网络/版本/挂起/未分类) | 12 | 11.4% | ~5h |
| **合计** | **105** | **100%** | **~60h** |

---

## 2. 分类详情

### 2.1 GPU 进程冲突 / 重复提交 (18 条)

**核心模式**: 多个 Worker 或 on_failed hook 同时向同一 GPU 提交任务，无查重机制。GPU 2 在 05-14 连续 6 次 v3→v4→v6 撞车最为典型。

| exp_id | 原因摘要 | 已重跑 | 数据可恢复 |
|--------|----------|--------|-----------|
| exp_001_eval_05B_d000_s42_v2 | GPU 2 多进程链 SIGKILL | ✅ v7+ | ❌ |
| exp_001_eval_05B_d000_s42_v3 | GPU 2 多进程链 | ✅ | ❌ |
| exp_001_eval_05B_d000_s42_v4 | GPU 2 多进程链 | ✅ | ❌ |
| exp_001_eval_05B_d000_s42_v6 | GPU 2 多进程链 | ✅ | ❌ |
| exp_001_eval_05B_d100_v3 | GPU 2 多进程链 | ✅ v6+ | ❌ |
| exp_001_eval_05B_d100_v4 | GPU 2 多进程链 | ✅ | ❌ |
| exp_001_eval_05B_d100_v6 | GPU 2 多进程链 | ✅ | ❌ |
| exp_001_eval_3B_d000_s42_v2 | d005 worker 抢 GPU 5 (SIGKILL) | ✅ v3 | ❌ |
| exp_001_eval_3B_d005_s42_aligned_v2 | 重复提交，与 PID 551290 冲突 | ✅ 已有 | ❌ |
| exp_001_eval_llama32_3B_d000_s42_v2 | 双 PID 冲突 (cuda:4 + cuda:1) | ✅ 后续版本 | 部分 (MMLU) |
| exp_001_sft_d005_05B | zombie eval PID 234755 占 GPU 5 | ✅ v2→r3 | ❌ |
| exp_001_sft_d005_05B_r3 | 与 v3 间隔 48s 重复提交 | ✅ v3 完成 | ❌ |
| exp_001_sft_05B_d025_s123 | cuda:4 三进程竞争 | ✅ | ❌ |
| exp_001_sft_3B_d000_v3 | cuda:4 SFT+signals 双进程 OOM 55% | ✅ 后续版本 | ❌ |
| exp_001_sft_3B_d100_s42_a32 | cuda:4 OOM (signals 冲突) | ✅ cuda:1 重跑 | ❌ |
| exp_001_eval_3B_d100_s123_para_aligned | signals_v3 抢 cuda:3 | ✅ v2 cuda:2 | ❌ |
| exp_002_signals_3B_v2 | signals vs SFT 共享 cuda:4 | ✅ v3+ | ❌ |
| exp_002_signals_3B_v3 | 静默死亡，疑似 OOM 共享 GPU | ✅ v4+ | 部分 (d000 完成) |

### 2.2 Cron/监控误报 (16 条)

**核心模式**: `reconcile_crons` 通过 tmux session 检测进程存活，tmux 死亡但 python 进程存活时误报。"process dead 5×" 是最常见的假阳性信号。

| exp_id | 原因摘要 | 实际状态 |
|--------|----------|---------|
| sft_gemma2_s123_sweep | process dead 5× auto-resolve | 可能已完成 |
| sft_qwen14b_s123_sweep | process dead 5× auto-resolve | 可能已完成 |
| eval_qwen7b_s42_cqa1_v2 | process dead 5× auto-resolve | 可能已完成 |
| phase2_eval_gpu0_phi4 | process dead 5× auto-resolve | 未验证 |
| phase2_eval_gpu1_qwen14b | process dead 5× auto-resolve | 未验证 |
| phase2_eval_gpu2_qwen7b_gemma | process dead 5× auto-resolve | 未验证 |
| phase2_eval_gpu3_gemma_olmo | process dead 5× auto-resolve | 未验证 |
| eval_phi4_mmlu_arc_westd | process dead 5× auto-resolve | 未验证 |
| eval_14b_mmlu_arc_westd | process dead 5× auto-resolve | 未验证 |
| exp_002_signals_3B_d000_s123_cuda2 | process dead 5× auto-resolve | 未验证 |
| exp_002_signals_15B_instruct_gsm8k | process dead 5× auto-resolve | 未验证 |
| exp_006_mmlu_domain_gamma_n24_v2 | reconcile_crons auto-resolve | 未验证 |
| exp_001_eval_05B_d100_aligned | tmux 死亡但 python PID 存活 | 实际完成 |
| exp_004_sim_sweep_v2 | 误标 failed，PID 仍在运行 | 实际运行中 |
| exp_004_sim_sweep_v4 | Worker 误在远程查找本地 PID | 实际运行中 |
| exp_001_eval_3B_d000_v2_para_aligned_v3 | tmux 名称查询误判 | 实际运行中 |

### 2.3 实验废弃/设计变更 (20 条)

**核心模式**: alpha=16→32 标准化 (D055)、lr 混淆 (D076)、IRT 设计迭代导致大量中间版本被废弃。

| exp_id | 废弃原因 |
|--------|----------|
| exp_001_sft_3B_d000_s42 | D076: lr=2e-4 confound |
| exp_001_sft_3B_d000_v4 | alpha=16→32 修正 |
| exp_001_sft_3B_d025_s42_a32 | 与 d025_v3 重复 (同 config) |
| exp_001_sft_3B_d025_s42_a32_v3 | D086: 已有有效 checkpoint |
| retrain_gemma2_d100_s123 | 重复 registry 条目 |
| retrain_qwen14b_d100_s123 | 重复 registry 条目 |
| eval_7b_batch_cqa1 | 替换为 eval_7b_mmlu_arc_cqa1 |
| exp_006_irt_05B_v2 | 被后续版本替代 |
| signals_05B_s123_batch | 被后续版本替代 |
| exp_002_signals_15B_instruct_gsm8k_v2 | 被后续版本替代 |
| exp_001_eval_3B_d025_s123 | 被后续版本替代 |
| exp_001_eval_3B_d005_s123 | 被后续版本替代 |
| exp006-gsm8k-d024-delta | 被 pooled cross-family 替代 |
| exp_001_eval_3B_d025_v3_s42_batch | 被后续版本替代 |
| exp_004_sim_sweep_v6 | 被后续版本替代 |
| exp_004_sim_sweep | v1 被 v2 替代 |
| exp_005_noise_prop_v3 | 崩溃后重启为 v4 |
| exp_001_eval_3B_d100_v2_aligned | 数据完整性问题 (D036) |
| exp_001_sft_d025_3B | 注册但从未启动 |
| exp_001_sft_100pct_05B | 重复 registry 条目 |

### 2.4 配置/命令/代码错误 (13 条)

| exp_id | 错误类型 | 具体原因 |
|--------|----------|---------|
| exp_001_eval_05B_d100_aligned_v2 | EXIT_CODE=127 | 缺少 `conda activate` |
| exp_001_sft_15B_d025_s123 | EXIT_CODE=2 | shell 语法错误 |
| exp_001_sft_15B_d005_s123 | EXIT_CODE=2 | shell 语法错误 |
| exp_001_eval_15B_d000_s42 | 挂死 11h | 使用相对路径而非绝对路径 |
| exp_001_eval_05B_d000_s42 | FileNotFoundError | output_dir 未预创建 |
| exp_002_signals_05B_s123_batch | EXIT_CODE=127 | 脚本文件不存在 |
| exp_002_signals_3B | ValueError | argparse `%` 转义 bug |
| exp_002_signals_3B_v4 | rc=2 (11/12 失败) | `--signal` 参数 bug |
| exp_001_eval_3B_instruct_aligned_para | 结果无效 | Instruct 模型未加 chat template |
| exp_006_mmlu_domain_gamma_n24_v3 | 错用脚本 | run_mmlu_domain_gamma.py vs \_n24.py |
| exp_002_signals_3B_v6 | s3_constat 崩溃 | Item count mismatch (代码 bug) |
| exp_002_signals_3B_v9 | wrapper 退出 | 1/4 tasks 完成，wrapper PID 异常退出 |
| exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k | 部分完成 | 进程中途死亡，s4 部分/缺失 |

### 2.5 外部 kill / Worker 误杀 (11 条)

**核心模式**: Worker agent 检测到 GPU 冲突后主动 SIGTERM（D083），tmux wrapper 死亡传播 SIGHUP，或 Director 手动 kill 卡死进程。

| exp_id | kill 来源 | 进度 | GPU-hours 浪费 |
|--------|----------|------|---------------|
| exp_001_sft_3B_d100_s42_a32_v2 | Worker SIGTERM (D083) | 73% (3030/4159) | ~3.6h |
| exp_001_sft_3B_d025_s42_a32_v2 | Worker SIGTERM | 0.6% (22/3384) | ~0.03h |
| exp_001_sft_olmo2_7b_d005_s42 | 外部 kill | 完成 1.96h 训练 | ~2h |
| exp_001_eval_05B_d100_aligned_v3 | SIGHUP (tmux 死亡) | GSM8K 13% | ~0.5h |
| exp_002_signals_3B_v5 | SIGHUP (orphan 清理) | 3/4 完成 | ~1h |
| exp_001_eval_llama32_3B_d000_s42 | Director kill (GSM8K 挂起) | MMLU 完成 | ~1.5h |
| exp_001_eval_05B_aligned_batch | timeout 超限 | 4/6 完成 | ~2h |
| exp_001_eval_05B_d100 | SIGTERM | 未知 | ~0.5h |
| exp_001_eval_05B_d100_v2 | SIGKILL | 未知 | ~0.5h |
| exp_008_base_pretrained_eval | Director kill (挂起 2.5h+) | 0% 输出 | ~2.5h |
| exp_001_eval_05B_d000_s42_v7 | 静默死亡 2h+ | 无输出 | ~2h |

### 2.6 磁盘满 (4 条)

| exp_id | 磁盘位置 | 具体原因 |
|--------|----------|---------|
| exp_004_sim_sweep_v3 | /tmp (tmpfs 3.9GB) | CmdStanPy MCMC 临时文件 |
| exp_005_noise_prop_v2 | /tmp (tmpfs 3.9GB) | ME model ~1GB CSV × 4 chains |
| exp_005_noise_prop | /tmp (tmpfs) | Stan 临时文件 |
| exp_004_fisher_heatmap_w4 | /root/autodl-tmp | 数据盘写满 |

### 2.7 CUDA_VISIBLE_DEVICES 绑定失败 (3 条)

| exp_id | 声明 GPU | 实际 GPU | 根因 |
|--------|---------|---------|------|
| exp_001_sft_d025_05B | cuda:5 | GPU 0 | tmux 未传 CUDA_VISIBLE_DEVICES |
| exp_001_sft_d005_05B_v2 | cuda:5 | GPU 0 | `--gpu 0` 覆盖了设备映射 |
| exp_001_sft_d025_05B_v2 | cuda:5 | GPU 0 | 同上 |

### 2.8 数据/模型/算法问题 (4 条)

| exp_id | 问题 |
|--------|------|
| exp_002_signals_llama32_3B_d100_mmlu | Llama d100 模型退化 (all-A prediction) |
| exp_006_irt_05B | 混合 scale (0.5B+1.5B+3B) + legacy 格式 |
| exp_006_pooled_gsm8k_v1 | 混合 exposure scales + 3B GSM8K catastrophic forgetting 未排除 |
| exp_006_irt_05B_v1 | MMLU 14042 items → 56K params，NUTS 不可行 |

### 2.9 OOM (纯显存，非冲突) (2 条)

| exp_id | 原因 |
|--------|------|
| exp_001_sft_d100_15B | batch_size=2 OOM，改 1 后成功 |
| exp_002_signals_3B_v8 | selfcritique on 14042 items MMLU OOM |

### 2.10 平台基础设施 (2 条)

| exp_id | 原因 |
|--------|------|
| exp_006_j16_theta_extraction | SeetaCloud seccomp/cgroup 安全策略杀容器 (~88min) |
| exp_006_cross_family_irt_j16 | 同上，pooled fit 在 60% sampling 时被杀 |

### 2.11 其他 (12 条)

| exp_id | 原因 |
|--------|------|
| eval_qwen7b_s123_cqa1 | evaluate.py 版本不一致 (C009) |
| exp_002_signals_llama32_3B_d000_gsm8k | HF Hub 连接超时 |
| exp_006_theta_extraction_j13 | startup recovery (无 cron/server info) |
| exp_008_instruct_rl_proxy | startup recovery |
| exp006-oracle-arc-4pl-pooled | startup recovery |
| exp_002_signals_3B_v8_recovery | 状态不明 |
| eval_7b_batch1_westd | 原因不明 |
| j16-domain-gamma-rerun | 原因不明 |
| exp006-oracle-gsm8k-extended | 原因不明 |
| exp006-pooled-s1only-gsm8k | 原因不明 |
| exp006-pooled-05B-15B-mmlu-v2 | 原因不明 |
| exp_004_sim_sweep_v5 | 误标 (实为 v4 的延续) |

---

## 3. 系统性模式与根因分析

### 模式 A: GPU 调度无原子锁 (占 20%+ 失败)

GPU 进程冲突 (18) + CUDA_VISIBLE_DEVICES 绑定失败 (3) = **21 条**，是最大的系统性问题。

**根因链**:
1. `submit_training_job` 不检查目标 GPU 是否已有进程
2. `on_failed` hook 自动重试不做 GPU 查重
3. `--gpu N` 参数与 `CUDA_VISIBLE_DEVICES` 语义不一致
4. 多个 Worker session 并发操作同一 GPU

**已有约束**: C001/C002/C003/C004/C005 都是事后补丁，但 Worker prompt 遵从率不够。

**建议**: 在 `submit_training_job` 层面加 GPU 锁：提交前自动 `nvidia-smi --query-compute-apps=pid,gpu_uuid` 检查，已占用则拒绝提交并返回错误。

### 模式 B: 监控基于 tmux 不可靠 (占 15%)

**根因**: `reconcile_crons` / `check_job_status` 通过 tmux session 名称检测进程存活。tmux session 可能：
- 意外退出（但子进程通过 nohup 存活）
- 名称不匹配（手动 vs 自动提交）
- 跨服务器误查（本地 PID 在远程查）

**建议**: 改用 PID 文件 + `ps -p PID` 做进程检测，不依赖 tmux。完成标志改为 output_dir 下的 `DONE` sentinel 文件。

### 模式 C: /tmp tmpfs 是定时炸弹 (4 条)

CmdStanPy 默认写 /tmp，AutoDL /tmp 只有 3.9GB tmpfs。每次 MCMC 采样生成 ~200MB-1GB CSV。

**已修复**: exp_004 v4+ 设 `TMPDIR=/home/ubuntu/tmp_cmdstan`。但新 Stan 实验仍可能忘记。

**建议**: 在 `.bashrc` 或项目 env 脚本中永久设 `TMPDIR=/root/autodl-tmp/tmp_stan`。

### 模式 D: Worker 自杀悖论 (11 条)

Worker agent 检测到 GPU 冲突后主动 SIGTERM 进程（D083 确认），但有时杀错或杀早（d100_a32_v2 在 73% 被杀浪费 3.6 GPU-hours）。

**建议**: Worker 检测到冲突时应上报而非直接 kill。由 Director 决定哪个进程优先。

### 模式 E: 版本标识缺失 (13 条配置错误)

相同实验反复因 shell 语法、conda 激活、路径问题失败，说明命令模板没有标准化。

**建议**: 维护 per-server 的命令模板（含 conda activate、env exports、CUDA_VISIBLE_DEVICES），Worker 填参数即可，不手写完整 bash 命令。

---

## 4. 关键教训

1. **GPU 2 血案** (05-14): 6 个 eval 在 30 分钟内接连提交到 cuda:2，每个都因前一个未清理而 OOM。直接催生 C001 约束，但类似事件后续仍在 cuda:4 重演。
2. **D083 Worker 误杀**: Worker 检测 GPU 冲突后直接 `ssh_execute kill`，d100_a32_v2 在 step 3030/4159 (73%) 被杀，浪费 3.6 GPU-hours。这是自动化反噬的典型案例。
3. **alpha=16→32 迁移**: D055 决定标准化 alpha=32，导致 ~8 个旧 checkpoint 废弃。但 Worker 持续在废弃 checkpoint 上启动任务（催生 C006 黑名单），至少浪费 10+ GPU-hours。
4. **tmux 监控盲区**: 至少 3 个实验被误标 failed（实际进程存活），registry 不支持 DONE→RUNNING 回退，导致状态混乱。
5. **SeetaCloud 安全策略**: 88 分钟运行限制杀死 IRT pooled fit 两次，但 per-domain fit 8/8 成功。长时间 MCMC 任务需拆分为 <60min 的子任务。

---

## 5. 优先级建议

| 优先级 | 建议 | 预防失败数 | 实施难度 |
|--------|------|-----------|---------|
| P0 | submit_training_job 加 GPU 占用检查 | ~21 | 中 (改工具代码) |
| P0 | 进程检测改用 PID 文件 + sentinel | ~16 | 中 |
| P1 | 标准化命令模板 (per-server) | ~13 | 低 |
| P1 | Worker 检测冲突时上报而非 kill | ~11 | 低 (改 prompt) |
| P2 | TMPDIR 永久配置 | ~4 | 低 |
| P2 | SeetaCloud 长任务拆分策略 | ~2 | 中 |
