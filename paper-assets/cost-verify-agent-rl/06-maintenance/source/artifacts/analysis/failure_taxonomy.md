# Experiment Failure Taxonomy — cost-verify-agent-rl

> 基于 51 个实验的系统分析 | 生成日期: 2026-05-15 | 数据来源: project registry + decisions.yaml + memory.md

## 概览

| 结论 | 数量 | 占比 |
|------|------|------|
| success | 3 | 5.9% |
| negative | 5 | 9.8% |
| failed | 28 | 54.9% |
| killed | 11 | 21.6% |
| N/A (preparing/pending) | 4 | 7.8% |
| **总计** | **51** | **100%** |

排除 4 个未执行实验和 1 个运行中 (exp027)，46 个已结论实验中：
- 3 成功 (6.5%)
- 5 负向结果 (10.9%)
- 38 失败/终止 (82.6%)

失败模式分布（38 个失败/终止实验，部分实验涉及多个类别）：

| 失败类别 | 实验数 | 占失败总数 |
|----------|--------|-----------|
| 工程类 | 24 | 63.2% |
| GRPO 训练不稳定类 | 9 | 23.7% |
| SFT 格式/数据类 | 4 | 10.5% |
| 奖励设计类 | 3 | 7.9% |

---

## 1. 工程类失败 (24 个)

### 1.1 早期环境/框架搭建失败 (7 个)

| Exp ID | 失败描述 | 根因 | 修复 | 决策 |
|--------|---------|------|------|------|
| exp_001 | 训练启动失败 | 未知（早期搭建） | — | — |
| exp_001b | 训练启动失败 | 未知（早期搭建） | — | — |
| exp_002 | 训练启动失败 | 未知（早期搭建） | — | — |
| exp_003 | 95.3% invalid actions, pg_loss≈0 | Qwen3-1.7B 原生输出 `<think>` 后不生成 `<answer>` 标签，RAGEN 解析器正则要求 `<answer>` | 修改解析器适配 Qwen3 格式 (D004) | D003, D004 |
| exp_003 (underscore) | 启动失败 | 早期配置错误 | — | — |
| exp_003_dryrun* (3个) | dry run 失败 | 早期配置调试 | — | — |

**模式总结**: 项目启动期的框架适配问题。exp003 的 Qwen3 格式不兼容是最关键发现——95% invalid action 完全阻断了学习信号。修复后所有后续实验不再出现此问题。

### 1.2 磁盘空间耗尽 (3 个)

| Exp ID | 触发位置 | 磁盘路径 | 根因 | 修复 |
|--------|---------|---------|------|------|
| exp007 | step 10 | `/tmp` (30GB root) | Ray session 文件填满根分区 | `RAY_TMPDIR=/root/autodl-tmp/tmp` |
| exp010 | step 11 | `/tmp` (30GB root) | fast_downward 同样路径，修复未完全 | `TMPDIR=/root/autodl-tmp/tmp` |
| exp023c | step 9 | `/root/autodl-tmp` (94%, 233G/250G) | checkpoint + 模型文件累积 | 清理旧 checkpoint |

**模式总结**: AutoDL 实例根分区仅 30GB，数据盘 250GB。两种磁盘满路径：(1) `/tmp` 被 Ray/PDDL planner 填满 (exp007/010)；(2) 数据盘被 checkpoint 累积填满 (exp023c)。D009 pre-flight checklist 中加入了 `df -h` 检查。

### 1.3 依赖/版本不兼容 (2 个)

| Exp ID | 错误 | 根因 | 修复 |
|--------|------|------|------|
| exp012 | `TypeError: EngineArgs.__init__() got unexpected keyword argument 'disable_mm_preprocessor_cache'` | vLLM 版本与 RAGEN 代码不兼容 | 固定 vLLM 版本 |
| exp023_grpo_parallel | `tatsu FailedToken: expecting 'action', got template "take {o} from {r}"` | val env_groups=16 加载了更多 ALFWorld game files，触发 PDDL parser 不兼容 | 降回 env_groups=4，使用 serial 模式 (exp023c) |

### 1.4 错误入口点/配置参数 (4 个)

| Exp ID | 错误 | 根因 | 修复 | 决策 |
|--------|------|------|------|------|
| exp012 | 使用 agent_proxy 而非 train.py | Worker 使用错误入口点 | 引入 pre-flight checklist | D009 |
| exp020 | `AssertionError: model_path doesn't contain "qwen"` | checkpoint 软链接路径不含 "qwen" 字符串 | 修改软链接命名 | — |
| exp020c | Hydra key path 错误 | 配置参数路径写错 | — | 放弃，转 exp020d |
| exp020d | 放弃 | exp020b 已证明 RAGEN 格式不兼容 | — | D021 |

### 1.5 Ray/AutoDL 容器限制 (7 个)

| Exp ID | 错误 | 根因 | 修复 |
|--------|------|------|------|
| exp013b | Raylet killed by cgroup OOM | Ray object_store 70GB + memory 164GB = 234GB > cgroup 220GB 限制 | env_groups 8→4 |
| exp013c | 预防性终止 | 确认同 exp013b 的 cgroup 根因 | 降 env_groups + 降 object_store |
| exp013d | RAY_object_store_memory 环境变量无效 | Ray 忽略环境变量，需通过 Hydra 配置 | 改用 Hydra config override |
| exp013e | `ActorUnavailableError: RPC Socket closed` | vLLM worker 在 val→train 切换时 memory peak 超限 | 禁用 Ray MemoryMonitor, 清理旧 session |
| exp025 | `ModuleNotFoundError` | 激活错误 conda 环境 (base vs verl-agent) | `which python` 验证 |
| exp025b | `EAGAIN: Resource temporarily unavailable` (36+ 次) | AutoDL cgroup pids.max=20480，verl-agent Ray 多进程超限 | 无法修复，放弃 verl-agent |
| exp025c | 同上 | pids.max 硬限制确认 | pivot 到 Track B cherry-pick |

**模式总结**: AutoDL 容器两个硬限制阻碍了训练：(1) cgroup 内存 220GB，Ray 默认 object_store 分配可超限；(2) pids.max=20480，verl-agent 架构在此限制下不可行。最终导致 verl-agent 方案被放弃 (D028)，转向 cherry-pick step-independent rollout 到 RAGEN。6 次失败、10+ GPU-h 空转。

### 1.6 监控/Cron 误判 (2 个)

| Exp ID | 问题 | 根因 | 修复 | 决策 |
|--------|------|------|------|------|
| exp019_expert_sft_v2 | cron 报告 process dead | 监控了 shell wrapper PID 而非训练进程 PID | 监控正确 PID | — |
| exp026 | cron 5 次误判 failed，registry 标记 DONE(failed) | `WANDB_MODE=disabled` + 监控错误 PID | 启用 W&B + 监控正确 PID | D029, D033 |

**模式总结**: 监控 PID 必须是实际训练进程（非 shell wrapper）。`WANDB_MODE=disabled` 与 cron 监控不兼容——已建立硬规则禁止同时使用 (memory.md)。

### 1.7 资源冲突 (2 个)

| Exp ID | 问题 | 根因 |
|--------|------|------|
| exp009 | response_mask assertion + GPU 冲突 | 与 exp010 同时占用 cuda:0+1，写同一 checkpoint 目录 |
| exp019c | GPU 被占用 | exp019b 的 nohup 进程仍在运行 |

---

## 2. GRPO 训练不稳定类 (9 个)

### 2.1 稀疏奖励冷启动 / 零梯度死锁 (3 个)

| Exp ID | 假设 | 关键配置 | 失败描述 | 根因 | 决策 |
|--------|------|---------|---------|------|------|
| exp012b | format_penalty=0 isolate impact | format_penalty=0, group_size=16, LR=1e-6 | step 6 success=8.59%, step 7 pg_loss=0, grad_norm 1.48→0.09 | format_penalty=0 消除了组内 reward 方差，GRPO 无梯度信号 | D010 |
| exp015 | 极低 LR 防 collapse | LR=1e-7, KL=0.1, grad_clip=1.0 | step 3-5 连续零梯度 | LR=1e-7 参数更新量 ~5e-12，模型行为无可观测变化 | D014 |
| exp016 | LR 折中方案 | LR=5e-7, KL=0.1, 从 exp015 恢复 | 12 步中 11 步 pg_loss=0, 仅 step 7 有 4.7% success | base success ~4.7% 太稀疏，GRPO 在此 sparsity 下无法产生有效学习 | D015, D016 |

**模式总结**: LR 搜索区间穷尽 — 1e-6 (collapse) / 5e-7 (无效学习) / 1e-7 (零梯度)。根因不是超参选择，而是 base success rate (~1-5%) 过低，sparse binary reward 下 GRPO 无法产生有效梯度。最终 pivot 到 Expert SFT warmup (D016)。

### 2.2 灾难性 collapse / 死亡螺旋 (3 个)

| Exp ID | 假设 | 关键配置 | 峰值 → 崩塌 | 根因 | 决策 |
|--------|------|---------|------------|------|------|
| exp010 | 首次 GRPO after SFT | format_penalty=-0.1, LR=1e-6 | step 1 success=4.7% → step 10 success=0% | format_penalty 劫持梯度 + /tmp 磁盘满 | D007 |
| exp011 | exp010 从 step 10 恢复 | 同 exp010 reward config | — (preemptive kill) | 同 exp010 reward 问题会重复 | D007 |
| exp026 | step-independent GRPO | LR=1e-6, KL=0.01, env_groups=4 (64 rollouts), save_freq=25 | step 2 success=**32.81%** → step 4 success=**0%** | sparse reward + 小 env_groups → 全零 batch 概率高 → 负 advantage → 策略被推回 reference | D035, D036 |

**模式总结**: 两种 collapse 机制：(1) format_penalty 梯度劫持（exp010/011）——模型优化格式而非任务；(2) 稀疏奖励死亡螺旋（exp026）——偶然的全零 batch 产生纯负 advantage，策略保守化 → success 进一步降低 → 恶性循环。exp026 的 save_freq=25 导致峰值 checkpoint 丢失，是最大教训。

### 2.3 RAGEN full-history 导致的 entropy collapse (3 个)

| Exp ID | 假设 | 关键配置 | 指标退化 | 根因 | 决策 |
|--------|------|---------|---------|------|------|
| exp020b | GRPO from SFT (20% baseline) | LR=5e-7, KL=0.1, sparse reward | entropy 0.107→0.042 (-61%), train success 18.75%→4.69%, val=0% 始终 | RAGEN full-history concatenation → context 随步数爆炸 → 1.7B 模型推理退化 | D022 |
| exp022 | GRPO from RAGEN SFT (25% baseline) | LR=5e-7, KL=0.5, sparse reward | action_is_valid 48.75% (远低于 SFT 87.5%) | 同上，KL=0.5 仅减缓退化未改变方向 | D025 |
| exp023c | Serial GRPO, 同 exp022 config | LR=5e-7, KL=0.5, serial mode | train success 29.7%→23.4%, entropy 下降, step 9 磁盘满 | 同上，8 步已显示退化趋势 | D025, D026 |

**模式总结**: RAGEN 框架的 full-history concatenation 是 3/3 GRPO 退化的共因 (D025, D026)。KL 从 0.1 到 0.5 仅减缓退化速度，未改变方向。KL 仅 0.0005 时 success 已退化，说明是算法-任务结构性不匹配。Self-Guide 论文在 verl-agent (step-independent context) 上达到 72.7%，确认问题在 RAGEN 而非 GRPO 本身。这是 pivot 到 step-independent rollout cherry-pick 的核心依据。

---

## 3. SFT 数据/格式类 (4 个)

### 3.1 训练数据格式与推理框架不匹配

| Exp ID | 假设 | 问题 | 影响 | 修复 | 决策 |
|--------|------|------|------|------|------|
| exp017 | Expert trajectory SFT | expert 数据无 RAGEN `<think>`/`<answer>` 结构 | format_ok 100%→75%, valid 90%→63.8%, success 仅 5% | 两阶段 SFT：先 format SFT 再 expert SFT | D018 |
| exp019 | 修复 expert 数据 (v2) | move→put 替换方向错误，admissible_commands 中是 "move" 不是 "put" | 训练数据 2157 条错误替换，会恶化 valid | 保留 "move" 原样 + admissible actions augmentation | D019 |
| exp020b-d | SFT ckpt → RAGEN GRPO | SFT 数据无 Turn/State/Reward 包装，RAGEN eval 0% vs eval_sft_fast 20% | GRPO 从错误 baseline 启动，全程 val=0% | 将 SFT 数据转换为 RAGEN 格式重训 (exp021) | D021, D022 |
| exp021 | RAGEN 格式 SFT (v4) | 4-episode eval 报 25% success（高方差幸运值），16-episode eval 仅 6.25% | exp022 基于不可靠 baseline 启动 | 强制 ≥16 episodes eval (C003) | D024 |

**模式总结**: SFT 数据必须严格对齐推理框架格式。eval_sft_fast 和 RAGEN val 是两个不同框架，结果不可比（exp019b: 20% vs 0%）。4-episode eval 方差过大，不可作为 pass/fail 判定依据——C003 约束由此而来。

---

## 4. 奖励设计类 (3 个)

### 4.1 Format penalty 梯度劫持

| Exp ID | 奖励配置 | 现象 | 根因 | 决策 |
|--------|---------|------|------|------|
| exp010 | format_penalty=-0.1/turn, success=10.0 | valid 58.8%→68.3% 但 success 4.7%→0% | 零 success group 中 format_penalty 是唯一 reward 方差来源，GRPO 梯度指向格式优化 | D007, D008 |
| exp011 | 同 exp010 | 预防性终止 | 同 exp010 | D007 |

### 4.2 Dense reward gaming

| Exp ID | 奖励配置 | 现象 | 根因 | 决策 |
|--------|---------|------|------|------|
| exp013f | valid_action_bonus=0.15/action, success=10.0, format_penalty=0 | valid 60%→97.5%, success→0%, reward_mean=4.388 ≈ 29×0.15 | dense reward 可被独立最大化：模型学会产生合法但无效动作循环，回避高风险 success | D012 |

**模式总结**: 奖励设计面临两难——(1) format_penalty 在零 success 下劫持梯度；(2) unconditional dense bonus 被 gaming。Success-gated bonus 在 success≈0% 下退化为 sparse reward (D013)。最终方案：放弃 reward shaping，转向 step-independent rollout 从架构层面解决 credit assignment (D026)。

---

## 5. 跨实验关键发现

### Pattern 1: LR-stability 不可能三角 — sparse reward + GRPO 无安全 LR 区间
LR=1e-6 → collapse (exp012b step 7), LR=5e-7 → 无效学习 (exp016), LR=1e-7 → 零梯度 (exp015)。三个量级均失败，证明 sparse binary reward 下 GRPO 的 LR 搜索是无解的——根因是 reward signal 本身不足。(涉及: exp012b, exp015, exp016; 决策: D014, D016)

### Pattern 2: RAGEN full-history concatenation 是 GRPO 退化的结构性根因
3/3 RAGEN GRPO 实验 (exp020b/022/023c) 呈现一致退化模式：entropy 收缩 + success 退化 + KL 极低。KL 从 0.1 到 0.5 仅减缓退化。而 Self-Guide 论文使用 step-independent context 达到 72.7%。exp026 切换到 step-independent rollout 后，2 步内 train success 达 32.81%（前 3 次 RAGEN GRPO 从未超越 SFT baseline）。(涉及: exp020b, exp022, exp023c, exp026; 决策: D025, D026)

### Pattern 3: AutoDL 容器限制是不可绕过的硬约束
cgroup pids.max=20480 (verl-agent 不可用) + 内存 220GB (Ray object_store 需手动限制) + 根分区 30GB (/tmp 极易满) + 数据盘 250GB (checkpoint 需主动清理)。6 次 verl-agent 尝试、10+ GPU-h 空转后确认。(涉及: exp025, exp025b, exp025c, exp007, exp010, exp013b-e; 决策: D028)

### Pattern 4: 工程失败的可预防性
D009 pre-flight checklist 引入前：18 个实验仅 1 成功。多数失败为入口点错误 (exp012)、磁盘满 (exp007/010)、格式不兼容 (exp003) 等可在提交前拦截的问题。(涉及: exp003, exp007, exp010, exp012; 决策: D009)

### Pattern 5: 4-episode eval 的高方差陷阱
exp021 两次 eval 严重矛盾：4-ep 25% vs 16-ep 6.25%。基于 4-ep 结果启动的 exp022 浪费了计算资源。C003 约束（≥16 episodes）由此建立。(涉及: exp021, exp022; 决策: D024)

---

## 6. 正向结论（已验证有效的配置/方法）

### 发现 1: 两阶段 SFT 有效提升 ALFWorld baseline
- **方法**: 先 format SFT (exp008_sft) 教模型 RAGEN `<think>`/`<answer>` 格式，再 expert SFT (exp019b) 教 ALFWorld 任务知识
- **证据**: exp008_sft format_ok=100%, valid=90%; exp019b success=20%, format_ok=100%, valid=85.3%
- **关键因素**: admissible actions augmentation 是 success 从 5% (exp017, 无 augmentation) 到 20% (exp019b, 有 augmentation) 的关键差异

### 发现 2: Step-independent rollout 突破 RAGEN GRPO 天花板
- **方法**: Cherry-pick verl-agent 的 step-independent context + discounted returns 到 RAGEN
- **证据**: exp026 step 1-2 train success 21.88%→32.81%（前 3 次 RAGEN GRPO 从未超越 SFT baseline 6.25%）
- **对比**: RAGEN GRPO (exp020b/022/023c) 均退化，step-independent (exp026) 2 步内突破

### 发现 3: Qwen3 解析器适配方案有效且稳定
- **方法**: 修改 RAGEN 解析器适配 Qwen3 的 `<think>` + 自然语言输出（无 `<answer>` 标签）
- **证据**: exp003 invalid_action 95%→exp007 invalid_action 1.6%，修复后所有实验均不再出现此问题 (D004)

### 发现 4: 跨框架 baseline 一致性验证
- **发现**: Qwen3-1.7B raw baseline success≈6.25%，在 RAGEN (exp021 16-ep eval) 和 verl-agent (exp025b val_before_train=6.2%) 中一致
- **意义**: 模型基础能力跨框架稳定，训练算法/框架是关键差异因素 (D028)

---

## 7. 对 exp027 的启示

### 已规避的失败模式

| 失败模式 | exp027 中的规避措施 | 来源 |
|----------|-------------------|------|
| 全零 batch 死亡螺旋 | env_groups 4→8 (128 rollouts)，降低全零概率 | exp026 |
| LR 过激导致 collapse | LR 1e-6→5e-7 | exp012b, exp026 |
| save_freq 过大丢 checkpoint | save_freq 25→5 | exp026 |
| format_penalty 梯度劫持 | 使用 invalid_action_penalty=0.1（非 format_penalty） | exp010/011 |
| RAGEN full-history context 爆炸 | 使用 step-independent context | exp020b/022/023c |
| 4-ep eval 误判 | val env_groups=16 (≥16 episodes) | exp021, C003 |
| WANDB_MODE=disabled cron 误判 | W&B 已启用 (run id: y7jiibqk) | exp026, D033 |

### 仍需警惕的风险

| 风险 | 原因 | 监控指标 |
|------|------|---------|
| 稀疏奖励死亡螺旋仍可能发生 | env_groups=8 降低但未消除全零 batch 概率，LR=5e-7 仍可能过激 | 连续 2 步 success=0% 即触发 fail 条件 |
| entropy bonus 可能引入新 gaming | 0.01 entropy bonus 是未经验证的新参数 | entropy 持续上升但 success 不跟随 |
| train-val gap | 所有 GRPO 实验均存在显著 train-val gap (exp023c: 29.7% vs 6.25%) | step 5 val 是关键判定点 |
| 磁盘空间 | checkpoint 每 5 步保存，50 步 = 10 个 checkpoint × ~3.3GB = 33GB | df -h 定期检查 |
| KL=0.005 可能过低 | exp022 KL=0.5 仍 collapse，但 step-independent 框架下行为可能不同 | KL 持续接近 0 预示策略退化 |

---

## 附录: 实验时间线

```
Day 1 (05-13): exp_001 → exp003  [环境搭建 + Qwen3 格式发现]
Day 2 (05-14): exp007 → exp019b  [SFT pipeline + reward 设计迭代]
               - exp007-016: GRPO LR 搜索穷尽，pivot to SFT
               - exp010-013f: reward shaping 探索（penalty劫持 → gaming）
               - exp017-019b: Expert SFT 三版迭代
Day 3 (05-15): exp020 → exp027   [RAGEN GRPO 失败 → step-independent pivot]
               - exp020-023c: RAGEN GRPO 3/3 退化
               - exp025-025c: verl-agent 6次失败，放弃
               - exp026: step-independent 首次突破，但不稳定
               - exp027: 稳定化配置，运行中
```

**总 GPU 时间估算**: ~120 GPU-h（含 verl-agent 空转 10+ GPU-h、exp013f 30 步完整 reward gaming 实验 ~3h、exp023c 8 步 ~0.8h 等）
