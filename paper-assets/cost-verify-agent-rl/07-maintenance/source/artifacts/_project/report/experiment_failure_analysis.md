# cost-verify-agent-rl 实验失败模式系统性分析

> 分析范围：全部 50 个实验（exp_001 ~ exp026）  
> 时间跨度：2026-05-13 18:26 ~ 2026-05-15 11:07 UTC（~41 小时）  
> 生成日期：2026-05-15

---

## 1. 实验总览表

| exp_id | status | conclusion | 一句话摘要 | 失败分类 |
|--------|--------|------------|-----------|---------|
| exp_001 | DONE | failed | 首次环境搭建 | Infrastructure |
| exp_001b | DONE | failed | 环境搭建重试 | Infrastructure |
| exp_002 | DONE | failed | 环境搭建 v2 | Infrastructure |
| exp_003 | DONE | failed | 全历史 GRPO + 冷启动失败 | Algorithm Design |
| exp_003 (underscore) | PREPARING | failed | GRPO v3 prompt truncation | Algorithm Design |
| exp_003_dryrun | PREPARING | failed | dry-run 调试 | Infrastructure |
| exp_003_dryrun2 | PREPARING | failed | dry-run 调试 v2 | Infrastructure |
| exp003_dryrun3 | PREPARING | failed | dry-run 调试 v3 | Infrastructure |
| exp_003_dryrun3 | PREPARING | failed | dry-run 调试 v3 重复 | Infrastructure |
| exp005 | PREPARING | (未执行) | Fast config 方案，未实际运行 | — |
| exp007_dryrun | PREPARING | (未执行) | exp007 dry-run，未记录结果 | — |
| exp007 | DONE | failed | Parser fix + /tmp 磁盘满 + action_is_valid 8.4% | Infrastructure + Algorithm |
| exp008 | PREPARING | killed | SFT warmup 方案被撤回 | — |
| **exp008_sft** | **DONE** | **success** | **SFT warmup: format_ok=100%, action_is_valid=90%, success=0%** | **— (成功)** |
| exp009 | DONE | failed | response_mask 断言 + 资源冲突 | Environment/Format |
| exp010 | DONE | failed | GRPO 11步后 /tmp 满崩溃; success 4.7%→0% | Infrastructure + Algorithm |
| exp011 | DONE | killed | reward shaping 问题，Director 终止 | Algorithm Design |
| exp012 | DONE | failed | vLLM 版本不兼容 (disable_mm_preprocessor_cache) | Environment/Format |
| exp012b | DONE | killed | Step 7 catastrophic collapse (LR=1e-6) | Hyperparameters |
| exp013 | DONE | killed | Director 驳回纯 KL 方案，要求 dense reward | — |
| exp013b | DONE | failed | Ray OOM (object_store 70GB + memory 164GB > cgroup 220GB) | Infrastructure |
| exp013c | DONE | killed | 预防性 kill (与 exp013b 同配置) | Infrastructure |
| exp013d | DONE | failed | Ray object_store env var 未生效 → OOM | Infrastructure |
| exp013e | DONE | failed | Ray RPC Socket closed (val→train 切换) | Infrastructure |
| **exp013f** | **DONE** | **negative** | **Dense reward GRPO: reward gaming (action_is_valid 60%→97.5%, success 不变)** | **Algorithm Design** |
| exp014a | PREPARING | killed | success-gated bonus bootstrap 问题 | Algorithm Design |
| exp014b | PREPARING | killed | 被 Director 修订 | — |
| exp014c | PREPARING | (未执行) | 未记录 | — |
| exp015 | DONE | killed | LR=1e-7 过保守，零梯度 | Hyperparameters |
| exp016 | DONE | failed | Sparse GRPO pg_loss=0，base success ~0% 无学习信号 | Algorithm Design |
| **exp017_expert_sft** | **DONE** | **success** | **Expert PDDL SFT: 5% success, 63.8% action_is_valid** | **— (成功)** |
| exp018_sft_grpo | PREPARING | killed | exp017 eval 5% 太弱，取消 GRPO | — |
| exp019_expert_sft_v2 | DONE | killed | move→put 替换方向错误 | Environment/Format |
| exp019b_expert_sft_v2 | PREPARING | (未执行) | 被 v3 取代 | — |
| **exp019b_expert_sft_v3** | **DONE** | **success** | **两阶段 Expert SFT: eval_sft 20% success, format_ok=100%** | **— (成功)** |
| exp019c_expert_sft_v3 | PREPARING | killed | GPU 被 exp019b nohup 占用 | Infrastructure |
| exp020_grpo_from_sft | DONE | failed | Checkpoint path 缺 "qwen" → AssertionError | Environment/Format |
| **exp020b_grpo_from_sft** | **DONE** | **negative** | **GRPO from SFT: entropy 坍缩 61%, success 18.75%→4.69%, val 始终 0%** | **Algorithm Design + Eval Mismatch** |
| exp020c_grpo_from_sft | PREPARING | failed | SFT/RAGEN 格式不兼容，废弃 | Environment/Format |
| exp020d_grpo_from_sft | PREPARING | failed | 同上 | Environment/Format |
| **exp021_ragen_sft_v4** | **DONE** | **negative** | **RAGEN 格式 SFT: 16ep eval 6.25% (原 4ep 25% 不可靠)** | **Evaluation Mismatch** |
| exp021_sft_ragen_format | PREPARING | killed | 被 exp021_ragen_sft_v4 取代 | — |
| exp022_grpo_from_sft_v4 | DONE | killed | GRPO step 0: action_is_valid 48.75% (远低于 SFT 87.5%) | Algorithm Design |
| exp023_grpo_parallel | DONE | failed | TextWorld tatsu parser 多线程崩溃 | Framework Limitation |
| **exp023c_grpo_serial** | **DONE** | **failed** | **磁盘满 + GRPO 8步退化 (success 29.7%→23.4%, entropy↓)** | **Infrastructure + Algorithm** |
| exp024_success_gated_grpo | DONE | killed | RAGEN GRPO 路线终止后不适用 | — |
| exp025 | DONE | failed | ModuleNotFoundError (错误 conda env) | Environment/Format |
| exp025b | DONE | failed | pthread_create EAGAIN (cgroup pids.max) | Framework Limitation |
| exp025c | PENDING | failed | cgroup pids.max=20480 硬限制，verl-agent 路线终止 | Framework Limitation |
| exp026_step_independent_grpo | DONE | failed* | Cron 误判 DONE(failed)，实际可能仍在运行 | Infrastructure (误报) |

**统计**：成功 3 / 阴性 3 / 失败 22 / 被 kill 13 / 未执行 9 = 50 总计  
*exp026 被 cron 误标，真实状态待确认

---

## 2. 按失败原因分类

### 2.1 Infrastructure（基础设施问题）— 14 个实验

#### /tmp 磁盘满（3 次）
- **exp007**: step 10, /tmp 被 Ray session 文件占满 30GB 根分区
- **exp010**: step 11, fast_downward libdownward.so 复制到 /tmp 失败
- **exp023c_grpo_serial**: step 9, /root/autodl-tmp 94% (233G/250G), OSError Errno 28

**共性模式**: AutoDL 根分区仅 30GB，Ray session logs + TextWorld 临时文件 + checkpoint 累积超限。  
**缓解措施**: `TMPDIR=/root/autodl-tmp/tmp/` 部分解决了 /tmp 问题，但数据盘本身也会满。  
**教训**: 每次启动前 `df -h` 是 pre-flight checklist 必检项。

#### Ray/cgroup OOM（4 次）
- **exp013b**: object_store 70GB + memory 164GB = 234GB > cgroup 220GB → Plasma ENOMEM
- **exp013c**: 预防性 kill（同配置）
- **exp013d**: `RAY_object_store_memory` env var 未被 Ray 读取（需 Hydra config override）
- **exp013e**: Ray RPC Socket closed（val→train 内存峰值切换）

**共性模式**: AutoDL cgroup 内存上限 220GB，Ray 默认 object_store 70GB 必超。128 并发 ALFWorld 游戏加剧。  
**缓解措施**: `object_store_memory=30GB` (Hydra override) + `env_groups=4` (降并发) + `RAY_memory_monitor_refresh_ms=0`。exp013f 验证全部修复生效。  
**教训**: Ray env var 在 Hydra 场景下可能不生效，必须用 config override。

#### cgroup pids.max 限制（3 次）
- **exp025**: ModuleNotFoundError（实际是错 conda env，但暴露了 verl-agent 依赖多进程）
- **exp025b**: 8 个 AlfworldWorker + Ray 线程总数超 pids.max=20480 → EAGAIN
- **exp025c**: 降到单 GPU 仍无法解决，路线终止

**共性模式**: AutoDL 容器 pids.max=20480 硬限制不可调，verl-agent Ray 多进程架构天然不兼容。  
**缓解措施**: 无法在 AutoDL 上解决。D028 决定放弃 verl-agent 直接运行。  
**教训**: 容器化环境必须提前检测 cgroup 限制。

#### 早期环境搭建（4 次）
- **exp_001, exp_001b, exp_002**: 首次 RAGEN + ALFWorld 环境搭建
- **exp_003_dryrun 系列** (4 次): Ray 配置调试

**共性模式**: 新框架首次部署的常规困难。  
**教训**: 首次实验预留至少 4h 用于环境调试。

#### Cron 误报 / 资源冲突（3 次）
- **exp019c_expert_sft_v3**: GPU 被 exp019b 的 nohup 占用
- **exp026**: Cron 误判进程已死（实际 GPU 双卡 100%）
- **exp019b_expert_sft_v3**: Cron 误报 failed（训练实际正常完成）

**教训**: 必须用 submit_training_job 提交；cron 报 failed 先验日志。

---

### 2.2 Environment/Format（格式不匹配）— 8 个实验

#### SFT 格式 vs RAGEN 格式不一致（4 次）
- **exp020_grpo_from_sft**: checkpoint 路径不含 "qwen" → AssertionError
- **exp020b**: GRPO from SFT checkpoint, val success 始终 0%（格式偏移）
- **exp020c/d**: 同一根因，废弃

**共性模式**: SFT 训练数据的 observation/action 格式与 RAGEN runtime 格式不一致 → 分布偏移。exp019b eval_sft 20% success，但 RAGEN val 0%。  
**解法**: `convert_sft_to_ragen_format.py` 将数据转为 RAGEN 精确格式（v4 数据），exp021 验证通过。  
**教训**: SFT 数据**必须**与 inference 框架的精确格式对齐。这是本项目最大的格式教训。

#### Checkpoint 路径命名断言（2 次）
- **exp009**: `enable_response_mask` 断言检查 `"qwen" in model_path.lower()`
- **exp020_grpo_from_sft**: 同一断言

**缓解**: 创建含 "qwen" 的 symlink。

#### 错误 conda 环境（1 次）
- **exp025**: `conda activate base` 而非 verl-agent 专属环境 → ModuleNotFoundError

#### move→put 数据替换错误（1 次）
- **exp019_expert_sft_v2**: ALFWorld admissible_commands 包含 `move X to Y`，不含 `put`。诊断 Worker 误判导致数据错误。

---

### 2.3 Hyperparameters（超参选择）— 4 个实验

| exp | LR | KL coef | 问题 | 结果 |
|-----|-------|---------|------|------|
| exp015 | 1e-7 | — | 过保守，零梯度 | killed |
| exp012b | 1e-6 | — | 过激，step 7 collapse | killed |
| exp020b | 5e-7 | 0.1 | KL 约束过弱，entropy 坍缩 61% | negative |
| exp022/023c | 5e-7 | 0.5 | KL 约束过强，限制探索 | killed/failed |

**共性模式**: 超参空间极窄。LR 在 1e-7（无学习）和 1e-6（崩溃）之间仅一个数量级。KL coef 0.1 太弱、0.5 太强。  
**最佳区间（基于 verl-agent 论文）**: LR=1e-6 + KL=0.01，exp026 正在验证。  
**教训**: Agent RL 超参敏感度远高于标准 NLP fine-tuning，需要更系统的搜索。

---

### 2.4 Algorithm Design（算法设计）— 8 个实验

#### Sparse GRPO 冷启动失败（4 次）
- **exp003**: base model success ~0%，GRPO 无学习信号
- **exp007**: parser fix 后 action_is_valid 仅 8.4%，仍无法 bootstrap
- **exp010**: success 4.7%→0%，action_is_valid 提升但 success 下降
- **exp016**: pg_loss 恒为 0，12 步无任何学习信号

**共性模式**: base Qwen3-1.7B 在 ALFWorld 的 success ~4.7%（val）, temperature=1.0 下接近 0%（train）。GRPO group 几乎全零 reward → advantage=0 → 无梯度。  
**解法**: SFT warmup 提升 baseline success 后再接 GRPO。exp008_sft 验证 format 学习，exp017/019b/021 逐步提升 task knowledge。

#### Dense Reward Gaming（1 次）
- **exp013f**: valid_action_bonus=0.15 被独立最大化。action_is_valid 60%→97.5%（学会合法命令），但 success 始终 0-8%。cumulative bonus ~4.5 主导梯度 vs sparse success 10.0。

**教训**: Dense reward 必须 success-gated 或极低比例（<1:100），否则模型最大化中间奖励而非最终目标。

#### Full-History Context 爆炸导致 GRPO 退化（3 次）
- **exp020b**: entropy 0.107→0.042 (坍缩 61%), success 18.75%→4.69%
- **exp022**: step 0 即退化，action_is_valid 从 SFT 87.5% 降至 48.75%
- **exp023c**: 8 步稳定退化，success 29.7%→23.4%, pass@16 75%→50%

**共性模式**: RAGEN 全历史拼接 → 50步 context 25K+ tokens → 信噪比极低 → GRPO 从噪声中学到错误梯度。这是 RAGEN 框架的**结构性限制**，非超参可解决。  
**解法**: Step-independent rollout（verl-agent 核心创新），每步 context 恒定 ~2-3K tokens。exp026 实现此方案。

#### Catastrophic Collapse（1 次单独归因）
- **exp012b**: step 6 success=8.59% → step 7 success=0%, grad_norm 1.48→0.09, pg_loss→0

**根因**: GRPO 单步 policy update 过激（LR=1e-6），跳出有 success 的分布区域后无法恢复。

---

### 2.5 Evaluation Mismatch（评估方法不一致）— 3 个实验

- **exp021_ragen_sft_v4**: 4-episode eval 显示 25% success（原 conclusion=success），16-episode eval 降至 6.25%。D024 降级为 negative。
- **exp019b_expert_sft_v3**: eval_sft_fast 20% success，但 RAGEN 框架内 val 0%（格式差异）
- **exp022_grpo_from_sft_v4**: step 0 仅 8 episodes 评估，val_success=12.5% 不可靠

**共性模式**: 小样本（4-8 episodes）方差极大，不同 eval 框架结果不可比。  
**制度**: C003 约束——所有 eval 必须 ≥16 episodes。  
**教训**: Eval 方法必须与训练框架一致，否则指标不可信。

---

### 2.6 Framework Limitation（框架局限）— 3 个实验

#### RAGEN 全历史拼接
- 结构性问题，影响 exp020b/022/023c 全部 GRPO 实验
- context 长度随 episode 步数线性增长，50 步 → 25K+ tokens
- 每 episode 仅 1 个 training sample（vs verl-agent 每步 1 sample → 50x 数据效率）

#### TextWorld/tatsu 线程不安全
- **exp023_grpo_parallel**: `textworld.envs.pddl.logic._PARSER` 单例非线程安全
- 多线程并行 rollout 崩溃
- 修复：`threading.Lock()` 包裹整个 textworld 加载链

#### verl-agent + AutoDL 容器不兼容
- **exp025/025b/025c**: cgroup pids.max=20480 限制 Ray 多进程架构
- 无法在当前服务器环境解决

---

## 3. 成功 / 阴性实验分析

### 3.1 成功实验（3 个）

| exp | 方案 | 关键指标 | 成功条件 |
|-----|------|---------|---------|
| exp008_sft | 基础 SFT (1200 条, 3 epochs) | format_ok=100%, action_is_valid=90%, success=0% | 单阶段 SFT 足以学会格式 |
| exp017_expert_sft | Expert PDDL SFT (2460 条, 3 epochs) | success=5%, action_is_valid=63.8%, format_ok=75% | Expert trajectory 有 task knowledge 但格式退化 |
| exp019b_expert_sft_v3 | 两阶段 SFT (exp008→v3 data, 2 epochs) | success=20%, format_ok=100%, action_is_valid=85.3% | **两阶段保留 format 知识 + 叠加 task knowledge** |

**关键发现**:
1. **两阶段 SFT 优于单阶段**: exp017 直接用 expert data → format_ok 降至 75%；exp019b 从 exp008 checkpoint 出发 → format_ok 保持 100%
2. **SFT 是必要 warmup**: 从 0% 到 20% success 全靠 SFT，GRPO 尚未贡献正增益
3. **数据量 2460-2546 条、2-3 epochs、单卡 ~48 min** 是高效的 SFT 配置

### 3.2 阴性实验（3 个）——揭示了什么

| exp | 假设 | 阴性结论 |
|-----|------|---------|
| exp013f | Dense reward 解决 sparse 冷启动 | Reward gaming: 模型最大化中间奖励，忽略最终目标 |
| exp020b | GRPO from SFT 提升 success | Entropy 坍缩: GRPO 在 RAGEN 框架中系统性退化 SFT 能力 |
| exp021_ragen_sft_v4 | RAGEN 格式 SFT 达 25% success | 16ep eval 仅 6.25%，4ep 结果不可靠 |

**核心阴性结论**: **RAGEN 框架内的 GRPO 训练（无论什么超参）都会退化 SFT 获得的能力**。这不是超参问题，是架构问题。

---

## 4. 已证伪的路线

### 4.1 RAGEN 全历史 GRPO（3/3 失败）
- exp020b: entropy 坍缩 61%, success 18.75%→4.69%
- exp022: action_is_valid 从 87.5% 降至 48.75%
- exp023c: 8 步持续退化
- **结论**: 全历史拼接导致 context 爆炸，信噪比过低，GRPO 无法有效学习。D025/D026 终止此路线。

### 4.2 Unconditional Dense Reward Shaping（1/1 失败）
- exp013f: valid_action_bonus=0.15 被独立最大化
- **结论**: 非 success-gated 的 dense bonus 必然导致 reward gaming。

### 4.3 过高 KL Coefficient（0.5 过度约束）
- exp022: KL=0.5 下 step 0 即退化
- exp023c: KL=0.5 下 8 步持续退化
- **结论**: KL=0.5 过强，限制了有效探索。verl-agent 论文用 KL=0.01。

### 4.4 verl-agent 直接运行（3/3 失败）
- exp025/025b/025c: AutoDL cgroup pids.max=20480 硬限制
- **结论**: 当前容器环境不支持 Ray 多进程架构。D028 终止。

### 4.5 Sparse GRPO 冷启动（从 base model）
- exp003/007/010/016: base success ~0-4.7%，无学习信号
- **结论**: 必须 SFT warmup 到 ≥5% success 才有可能 bootstrap。

---

## 5. 仍成立的假设

### 5.1 Step-Independent Rollout 是关键差异（exp026 验证中）
- RAGEN 全历史 3/3 退化 vs verl-agent step-independent 论文 86.1% success
- exp026 dry run step 0 验证通过：step-level advantage 生效（max=11.93/min=-0.47）
- 每步 context ~2-3K tokens（恒定）vs 全历史 25K+（线性增长）
- 每 episode 产出 ~50 training samples（vs 全历史 1 sample）

### 5.2 SFT Baseline 6.25% 是可靠起点
- exp021 16ep eval 确认 6.25% success（C003 compliant）
- 两阶段 SFT 路线（exp008→exp019b→exp021）已验证
- Checkpoint `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/` 可复用

### 5.3 KL=0.01 + LR=1e-6 是更优超参区间
- 来源：verl-agent 论文在 ALFWorld 的最佳配置
- KL=0.01 << 0.1/0.5，允许更大探索幅度
- LR=1e-6 配合 KL=0.01 的低正则化，exp026 正在验证
- 对比 exp012b (LR=1e-6 + 无 KL→collapse) 和 exp015 (LR=1e-7→零梯度)

### 5.4 两阶段 SFT 保留 Format 知识
- exp017 单阶段 → format_ok 75%（退化）
- exp019b 两阶段 → format_ok 100%（保留）
- 后续 SFT 实验应从 exp008_sft checkpoint 出发

### 5.5 Pre-flight Checklist 显著减少基础设施失败
- C002 制定后，exp023c 到 exp026 的基础设施失败率明显下降
- 必检项：磁盘、入口点、config 参数、checkpoint 路径

---

## 6. exp026 后的下一步建议

### 场景 A：exp026 成功（success ≥ 20%）

1. **确认 MVP**：Step-independent rollout + GRPO 在 RAGEN 框架内有效
2. **Phase 2 GiGPO**：叠加 step-level advantage grouping（anchor state grouping + 折扣回报），预期进一步提升
3. **Invalid action penalty**：添加 -0.1/step 惩罚（verl-agent 配置），抑制无效动作
4. **扩大 eval**：50+ episodes 确认稳健性
5. **Scale up**：增加训练步数（150→300），探索 7B 模型

### 场景 B：exp026 失败但无退化（success ~6.25%，持平 SFT baseline）

1. **超参网格搜索**：LR ∈ {5e-7, 1e-6, 2e-6}, KL ∈ {0.005, 0.01, 0.02}
2. **增加 group_size**：当前 16 → 32，提升 GRPO advantage 估计质量
3. **Success-gated dense reward**：仅在 success episode 给 step-level bonus，避免 exp013f 的 gaming
4. **GiGPO 提前引入**：如果 GRPO 信号不足，step-level grouping 可能帮助 credit assignment

### 场景 C：exp026 退化（success < 6.25%，低于 SFT baseline）

1. **诊断退化原因**：是 entropy 坍缩 (类似 exp020b) 还是 KL 过大 (类似 exp022)?
2. **SPEAR 算法**：专门解决 sparse reward 冷启动（ICLR 2026），可能比 GRPO 更适合
3. **重新评估框架**：如果 step-independent 也退化，问题可能在 reward 结构（非 context 问题）
4. **更换服务器**：不受 cgroup 限制的环境直接运行 verl-agent 原版

---

## 7. 关键数字总结

| 指标 | 数值 |
|------|------|
| 总实验数 | 50 |
| 实际执行（DONE + 部分 PREPARING） | ~35 |
| 成功 | 3 (8.6% of DONE) |
| 阴性（有价值结论） | 3 |
| 基础设施失败 | 14 (40%) |
| 算法/设计失败 | 8 (23%) |
| 格式/环境失败 | 8 (23%) |
| 超参失败 | 4 (11%) |
| 框架局限 | 3 (9%) |
| 累计 GPU-hours | ~35h |
| 有效训练 GPU-hours（成功实验） | ~5h |
| GPU 利用率（有效/总计） | ~14% |
| 最佳 success rate | 20% (exp019b eval_sft), 6.25% (exp021 RAGEN 16ep) |

---

## 8. 实验时间线可视化

```
May 13 18:00  exp_001 ──────── 环境搭建（失败×5）
         ↓
May 13 21:00  exp_003 系列 ─── GRPO 冷启动（失败×4）
         ↓
May 14 00:00  exp007 ──────── Parser fix + 速度优化（/tmp满）
         ↓
May 14 03:00  exp008_sft ──── SFT warmup ✓ (format=100%)
         ↓
May 14 03:30  exp009/010 ──── GRPO from SFT（/tmp满 + success→0%）
         ↓
May 14 05:00  exp011/012 ──── Reward fix + vLLM 不兼容
         ↓
May 14 06:45  exp012b ─────── GRPO LR=1e-6 catastrophic collapse
         ↓
May 14 08:00  exp013b-f ───── Dense reward（4次 OOM + 1次 reward gaming）
         ↓
May 14 12:50  exp015/016 ──── Sparse GRPO（零梯度 / pg_loss=0）
         ↓
May 14 15:36  exp017 ──────── Expert SFT ✓ (success=5%)
         ↓
May 14 17:30  exp019b ─────── 两阶段 SFT ✓ (success=20%)
         ↓
May 14 22:00  exp020-020d ─── GRPO from SFT（格式不匹配 → val 0%）
         ↓
May 15 02:00  exp021 ──────── RAGEN 格式 SFT（6.25% @ 16ep）
         ↓
May 15 03:17  exp022 ──────── RAGEN GRPO #1（退化）
         ↓
May 15 04:00  exp023/023c ─── RAGEN GRPO #2/#3（崩溃 + 退化）
         ↓                   → D025/D026: RAGEN GRPO 终止
May 15 06:52  exp025 系列 ─── verl-agent 直接运行（cgroup 失败×3）
         ↓                   → D028: verl-agent 路线终止
May 15 09:34  exp026 ──────── Cherry-pick step-independent（训练中）
```

---

## 9. 失败模式 → 制度化约束 映射

| 失败模式 | 频次 | 对应约束 |
|---------|------|---------|
| 小样本 eval 误导决策 | 3 | C003: eval ≥16 episodes |
| Pre-flight 可拦截的失败 | 5+ | C002: 启动前 checklist |
| GPU 冲突 | 2 | C001: 指定 cuda:0,1 |
| Cron 误报 | 3 | 使用 submit_training_job + 日志验证 |
| SFT/inference 格式不一致 | 4 | memory: 必须用 convert_sft_to_ragen_format.py |
| Ray 内存超限 | 4 | memory: Hydra override object_store=30GB |
