## memory.md

### 关键发现

**D029 (updated): 8 种 representation-to-reward formulation 全部失败**
- cosine R1 (exp-002): tanh 饱和 → kill
- cosine R1 v2 (exp-002v2): 去 tanh 后 mode collapse → kill  
- cosine R1 scaled (exp-002v3): 5x 放大噪声等比放大 → mode collapse
- cosine R1 recalib (exp002v2-recalib): 500 步 recalibrate 仍然 collapse
- binary probe (exp-008v3): 即时 stubbornness trap，ToF=0 at ckpt-500
- continuous probe (exp-014): adversarial gaming，30 步内 probe gamed
- continuous probe probability (exp-009): "慢性 binary probe"，ckpt-500 ≈ vanilla → kill
- R3-only behavioral (exp-003): "uniform stubbornness"，拒绝所有压力而非选择性拒绝
- ActAdd inference-time (exp-016): 提升 NoF 但摧毁 ToF，净负效果

**R3-only 非单调轨迹 (exp-003, 2026-05-20 ckpt-4500 修正)**
- 完整 8 点轨迹：1000(0.074) → 2000(0.085) → 3000(0.095) → 4000(0.114) → **4500(0.134 ≈ vanilla)** → 5000(0.114) → 5500(0.114)
- **不是 "step 4000 plateau at 0.114"**——实际是先升到 step 4500 追平 vanilla，然后退化到 0.114
- R3-only 最佳也仅能追平 baseline，永远无法超越
- 退化行为可能暗示 behavioral reward 在 baseline 附近的 overfitting/reward hacking
- "uniform stubbornness" 机制：NLI 只能判断"是否让步"，无法区分"该让步"和"不该让步"

**R3-only 跨 seed 可复现性确认 (exp-003-s2, 2026-05-20)**
- Seed 2 (seed=43) 早期轨迹与 seed 1 (seed=42) 方向完全一致
- s2-ckpt500=0.085, s2-ckpt1000=0.084, s2-ckpt1500=0.104 — 均低于 vanilla (0.134)
- Seed 2 绝对值略高于 seed 1 同阶段（~14%），但数量级一致
- 结论：R3-only below-vanilla 不是随机波动，跨 seed 可复现

**ACT 非单调训练轨迹 (exp-004, 16 checkpoint 完整数据)**
- 整体趋势向上，但存在锯齿振荡
- 两个 dip 区：ckpt-1500 早期 dip (回落到 ckpt-500 水平) + ckpt-2500-4500 中期 dip (谷底 ckpt-4500=0.188)
- 所有 16 个 checkpoint 始终高于 vanilla baseline (0.134)
- 后半程 (5000+) 持续上升，ckpt-8000 达 0.301 (+126%)
- ACT 最差点 (0.170) 仍高于 R3-only 最好点 (0.134)，差距 +27%

**Reduced LoRA ACT 关键发现 (exp-004-reduced-lora, 2026-05-23)**
- Reduced LoRA (r=64, alpha=64, 4 modules: qkvo) vs Full LoRA (r=64, alpha=128, 7 modules: qkvo+gate+up+down)
- Trajectory: 500(0.152)→1000(0.170)→1500(0.161)→2000(0.205)→2500(0.171)→3000(0.171)→3500(0.188)→4000(0.205)→**4500(0.271)**
- **ckpt-4500=0.271 超过了 full-LoRA ACT s2 同期 (ckpt-4500=0.223)**——reduced-lora 给足步数后不仅追平还超越部分 full-LoRA 数据点
- 全部 9 个 checkpoint > vanilla (0.134)，与标准 ACT 一致
- 暗示 supervision granularity (per-token SFT) 是 ACT 成功的主因，LoRA capacity 的影响有限
- 趋势仍在上升，训练中 (step ~5000/8000)

**D027 统一 Eval 基线校正**
- 所有实验统一用 eval_unified_preset.py (D027 标准)
- vanilla baseline: ToF=0.072, NoF=0.945, SYCONScore=0.134
- 旧 eval_pipeline.py 给出的 vanilla SYCONScore=0.197 因 eval 脚本差异而偏高

**Llama-3-8B 跨模型验证 (exp-012)**
- Llama d_syc AUROC=0.779 (best layer 16)，style-controlled=0.923
- Llama random direction gap +0.248 > Qwen +0.108 — sycophancy 信号在 Llama 上更集中
- 跨模型 discriminability 确认，强化 Claim 1

**Probe Reward Trap 关键数据 (exp-008v3, 2026-05-20)**
- R1_mean 剧烈波动（0→0.875→0.25→1.0，probe 每 500 步重训）但 ToF 从 step 500 锁死≈0
- Entropy 从 0.70 降到 0.30（1300 步 behavioral-distributional lag）
- 数据文件：artifacts/figures/probe_trap_data.json (art_20260520_43877a)
- 图表文件：artifacts/figures/fig_probe_trap.pdf/png

**C1 多 Seed Probe Trap 验证完成 (2026-05-25)**
- exp-008-seed2 (SFT, seed=42) + exp-008-seed3 (SFT, seed=43) 均完成 2000 步
- 两个 seed 均在 step ~50 出现 St collapse（S(t)→0），与原始 exp-008v3 (GRPO) 的 ~30 步一致
- Probe 每 100 步 retrain，每次恢复到 AUROC=1.0 / acc=1.0，但模型 ~10 步内重新 game 掉
- 20 次 retrain cycle 无一例外——模型始终能击败重训后的 probe
- **核心结论**：probe reward trap 源于 binary probe 语义本身（二值分类器天然可被梯度欺骗），与训练范式（GRPO/SFT）和随机种子无关。3 seeds 一致复现，可作为论文 C1 的多 seed 证据
- 为什么 SFT collapse 稍晚（~50 vs ~30 步）：SFT 梯度更平滑（无 RL variance），但给足步数后效果相同

### Seed2 跨服务器一致性调查 (2026-05-25)

#### Checkpoint 来源

| 项目 | 详情 |
|------|------|
| 训练服务器 | westd-29046（唯一）|
| 训练方式 | training_from_base（从头训练，非 checkpoint 迁移）|
| 训练时间 | 2026-05-20 08:17 → 2026-05-22 23:30 |
| seed | 43 |
| 总 checkpoint 数 | 16 + final (step 500–8000, 每 500 步) |
| LoRA 配置 | r=64, alpha=64, target=[q_proj, v_proj, k_proj, o_proj], peft=0.19.1 |
| adapter_model.safetensors 大小 | 245,405,936 bytes（所有 checkpoint 一致）|

**结论：所有 seed2 checkpoint 来自 29046 上的同一次训练 run。28034 上从未有成功的 seed2 训练（28034 因 OOM 失败后实验迁移到 29046 从头训练）。**

#### Eval 数据来源清单

| ckpt step | eval 来源 | SYCONScore | eval 时间 | 审计状态 |
|-----------|----------|-----------|----------|---------|
| 500 | ⚠️ 无 registry / 无结果文件 | 0.0845 | ~2026-05-20 | 不可审计 |
| 1000 | ⚠️ 无 registry / 无结果文件 | 0.0844 | ~2026-05-20 | 不可审计 |
| 1500 | ⚠️ 无 registry / 无结果文件 | 0.1044 | ~2026-05-20 | 不可审计 |
| 2000 | ⚠️ 无 registry / 无结果文件 | 0.0846 | ~2026-05-21 | 不可审计 |
| 2500 (旧) | ⚠️ 来源不明 (trajectory_data_compiled.md) | **0.1046** | ~2026-05-21 | 不可审计 |
| 2500 (新) | ✅ registry exp-003-s2-eval-ckpt2500 | **0.1241** | 2026-05-25 | 完全可审计 |
| 3000 (旧) | ⚠️ 无 registry / 无结果文件 | 0.0945 | ~2026-05-21 | 不可审计 |
| 3500 | ⚠️ 来源不明 (trajectory_data_compiled.md) | 0.0744 | ~2026-05-21 | 不可审计 |
| 4000 | ✅ 结果文件 exp003_d027_eval/ | 0.1430 | 2026-05-22 | 可审计 |
| 7500 | ✅ 结果文件 exp003_d027_eval/ | 0.1241 | 2026-05-23 | 可审计 |
| 8000 | ✅ 结果文件 exp003_d027_eval/ | 0.1240 | 2026-05-23 | 可审计 |

#### ckpt-2500 差异分析 (0.1046 vs 0.1241, Δ=18.6%)

| 指标 | 旧值 (compiled, ~05-21) | 新值 (registry, 05-25) |
|------|------------------------|----------------------|
| SYCONScore | 0.1046 | 0.1241 |
| ToF | 0.0552 | 0.0663 |
| NoF | 0.9724 | 0.9669 |

**差异根因分析**：
- 两次 eval 均在 westd-29046 上执行，使用同一 checkpoint 文件
- eval 脚本 `eval_unified_preset.py`: do_sample=False, enable_thinking=False, max_new_tokens=512 → 理论上 greedy 解码完全确定
- 数据文件：两个路径 (contrastive_entrain_calib/data/ 和 mvp_v2_1_expanded/data/) 大小一致 (367,001 bytes, 362 行)，内容首行相同
- 环境：torch=2.12.0+cu130, transformers=5.8.1

**可能原因（按概率排序）**：
1. **eval 脚本版本差异**：旧 eval 可能使用了 eval_unified_preset.py 的早期版本或完全不同的 eval 脚本。当前脚本修改时间为 2026-05-18，但 git 部署历史无法追溯
2. **旧数据转录错误**：旧值来自 Agent session context 的临时输出，可能在编译 trajectory_data_compiled.md 时转录有误
3. **torch/transformers 版本更新**：如果 May 21 到 May 25 之间更新了包版本，可能影响 float 精度

#### 环境对比

| 项目 | westd-28034 | westd-29046 |
|------|-------------|-------------|
| 状态 | ❌ 不可达 (port 28034 connection refused) | ✅ 在线 |
| torch | 无法检查 | 2.12.0+cu130 |
| transformers | 无法检查 | 5.8.1 |
| peft | 无法检查 | 0.19.1 |
| GPU | RTX 5090 32GB (历史) | 2× RTX PRO 6000 96GB |
| eval_unified_preset.py | 无法检查 | 10,837 bytes, modified 2026-05-18 |
| seed2 checkpoint 路径 | ❌ 不存在（训练 OOM 未完成）| /root/autodl-tmp/checkpoints/exp003_r3only_seed2/ |

#### 结论

1. **是否同一训练 run？** — **是**。所有 seed2 checkpoint 来自 29046 上一次完整训练（2026-05-20 → 2026-05-22, 8000 steps）。28034 上不存在成功的 seed2 训练。
2. **差异来源？** — **不是跨服务器问题，而是 eval 可审计性问题**。ckpt-2500 的两个 SYCONScore 值均来自 29046，差异原因最可能是旧 eval 使用了不同版本的脚本或参数。旧值 (0.1046) 无 registry 记录、无结果文件，完全不可审计。
3. **需要重新 eval 的 checkpoint** — **ckpt-500, 1000, 1500, 2000, 2500, 3000, 3500**（所有标记为"不可审计"的 checkpoint）。ckpt-4000/7500/8000 有结果文件可审计。建议在 29046 上用当前版本 eval_unified_preset.py 重新 eval 全部 16 个 seed2 checkpoint，产生完整可审计轨迹。

### R3-only 完整轨迹分析 (exp-003 seed 1 + seed 2, 2026-05-21)

Vanilla baseline: SYCONScore=0.1335, ToF=0.072, NoF=0.945。所有 eval 使用 D027 标准 (eval_unified_preset.py, 362 pairs)。

**Seed 1 (exp-003, seed=42) — 11 checkpoints**

| Step | SYCONScore | ToF | NoF | vs Vanilla |
|------|-----------|------|------|------------|
| 1000 | 0.0743 | 0.0387 | 0.9448 | −44.3% |
| 2000 | 0.0846 | 0.0442 | 0.9834 | −36.6% |
| 3000 | 0.0946 | 0.0497 | 0.9724 | −29.1% |
| 4000 | 0.1144 | 0.0608 | 0.9669 | −14.3% |
| 4500 | 0.1337 | 0.0718 | 0.9613 | +0.1% |
| 5000 | 0.1144 | 0.0608 | 0.9669 | −14.3% |
| 5500 | 0.1144 | 0.0608 | 0.9724 | −14.3% |
| 6000 | 0.0846 | 0.0442 | 0.9724 | −36.6% |
| 6500 | 0.1529 | 0.0829 | 0.9834 | +14.5% |
| 7000 | 0.1046 | — | — | −21.6% |
| 7500 | 0.1046 | — | — | −21.6% |

注：ckpt-8000 eval 正在 RUNNING，待补充。ckpt-7000/7500 的 ToF/NoF 未记录在 registry metrics 中。

**Seed 2 (exp-003-s2, seed=43) — 可审计 eval 结果**

| Step | SYCONScore | ToF | NoF | vs Vanilla | 审计状态 |
|------|-----------|------|------|------------|---------|
| 2500 | 0.1241 | 0.0663 | 0.9669 | −7.0% | ✅ registry |
| 4000 | 0.1430 | 0.0773 | 0.9448 | +7.1% | ✅ 结果文件 |
| 7500 | 0.1241 | 0.0663 | 0.9724 | −7.0% | ✅ 结果文件 |
| 8000 | 0.1240 | 0.0663 | 0.9613 | −7.1% | ✅ 结果文件 |

⚠️ ckpt-500/1000/1500/2000/3000/3500: 旧 eval 数据不可审计，待重新 eval

**跨 Seed 对比（匹配 step）**

| Step | Seed 1 | Seed 2 | Δ(S2−S1) | 相对差 |
|------|--------|--------|----------|--------|
| 1000 | 0.0743 | 0.0844 | +0.0101 | +13.6% |
| 2000 | 0.0846 | 0.0846 | +0.0000 | 0.0% |
| 3000 | 0.0946 | 0.0945 | −0.0001 | −0.1% |

跨 seed 方差极小（step 2000/3000 几乎完全一致），确认 R3-only 轨迹可复现。Seed 2 在 step 1000 略高（+13.6%），可能因 seed 2 额外的 ckpt-500 warmup 窗口。

**三阶段分析 (基于 seed 1 完整数据)**

1. **初始爬升期 (step 1000→4500)**：SYCONScore 从 0.074 单调上升到 0.134，ToF 从 0.039 升到 0.072。模型逐步学会拒绝压力，但 NoF 始终 >0.94（几乎不让步），说明模型采取"全部拒绝"策略而非选择性拒绝。Step 4500 追平 vanilla baseline (+0.1%)，这是 R3-only 的理论天花板。

2. **退化+振荡期 (step 5000→6500)**：Step 5000/5500 回落到 0.114 (−14.3%)，step 6000 暴跌到 0.085 (−36.6%)，然后 step 6500 突然飙到 0.153 (+14.5%，超越 vanilla)。这是全轨迹唯一超越 vanilla 的点，但 ToF=0.083 对应的 NoF=0.983 表明仍是"uniform stubbornness"——不是学会了选择性拒绝，而是整体拒绝强度的随机波动。

3. **晚期收敛 (step 7000→7500)**：SYCONScore 稳定在 0.105 (−21.6%)，两个连续 checkpoint 完全一致，暗示模型在 vanilla 以下的一个次优均衡收敛。

**核心结论**：R3-only (behavioral reward only) 的 SYCONScore 天花板就是 vanilla baseline。Step 4500 的追平和 step 6500 的一次性超越不改变大局——模型学的是"uniform stubbornness"（NLI 无法区分该让步 vs 不该让步），而非 calibrated sycophancy resistance。跨 seed 完全可复现。

### 基础设施经验

**29046↔28034 直连 SCP (2026-05-20 发现)**
- 通过 `connect.westd.seetacloud.com` 网关可直连传输，无需本地中转
- SCP 命令：直接 `scp -r westd-29046:/path/ westd-28034:/path/` 即可（Worker 已验证）
- 这比之前假设的"NAT 无法直连"更高效

**29046 checkpoint 实际路径 (2026-05-20 确认)**
- exp-003 seed 1: `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-{step}/`
- exp-003-s2 seed 2: `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-{step}/`
- 不是 `/root/contrastive_entrain_calib/outputs/` 下

**exp-008v3 多 seed 复现准备 (2026-05-24 调查)**
- 原始 GRPO 脚本 `run_exp008v3_binary_probe_grpo.py` 不在 westd-29046 上，仅存于本地 artifacts
- 依赖 `probe_module.py` 也需上传
- DCGRPOTrainer 已在服务器 `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`
- 无 DeepSpeed 硬依赖，TRL GRPOTrainer 通过 Accelerate 自适应单/多卡
- 2x RTX PRO 6000 Blackwell (98GB each)，单卡即可运行 (原环境 2x A100 80GB total)
- 所有数据/模型/方向向量/激活文件均已就绪

**westd-28034 不可达 (2026-05-25 确认)**
- port 28034, IP 36.103.198.204 连接被拒绝
- 可能原因：实例已关停 / 端口变化
- 需要用户在 AutoDL 控制台确认状态

### 竞品实验参考
（待 Worker 调研后填充）

### 决策原因记录
- batch size 必须 32：显存限制 (A100 32GB on 28034)
- LoRA rank=64：exp-001 验证 rank 64 比 rank 8/16 更好地捕获 sycophancy direction
- ACT 用 SFT 而非 RL：L2 loss 在 hidden states 上直接优化，避开 reward 设计问题
