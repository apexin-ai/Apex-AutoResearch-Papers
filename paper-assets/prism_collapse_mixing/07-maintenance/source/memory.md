# Memory — prism_collapse_mixing

## 信号计算设计（Director 确认 2026-05-15）

### Per-example 信号（参与 Spearman ρ 计算，用于 pass/fail 判断）
1. **Per-example loss**: 每条 probe 序列的 cross-entropy loss → 5000 维向量
2. **Per-example output entropy**: 每条序列所有 token 位置的输出分布 Shannon entropy 均值 → 5000 维向量
3. **Per-example spectral effective rank**: 每条序列 [seq_len, hidden_dim] 最后层 hidden states → SVD → exp(Shannon entropy of normalized singular values) → 5000 维向量

### Corpus-level 辅助信号（不参与 ρ，每代 1 个值）
4. **Corpus-level spectral rank (SIGMA-style)**: 5000 条 mean-pooled embedding → [5000, hidden_dim] → Gram matrix → SVD → effective rank
5. **Distinct-1/2/3**: corpus-level generation diversity

### Spearman ρ 计算方式
- 在每代 checkpoint 上：ρ(loss_vec_5000, signal_vec_5000)
- 观察 ρ 从 Gen 0 → Gen 3 如何变化（脱钩 = ρ 下降）
- **不是**跨 4 个 generation 的时间序列 ρ

### Pass/Fail 阈值（预注册 D002）
- Pass（同时满足）：
  - ≥1 个 per-example 信号在 Gen 3 与 loss 的 |ρ| < 0.5，且 Gen 0-1 时 |ρ| > 0.7
  - 该信号从 Gen 0→Gen 3 单调退化，末代相对首代 ≥15% 下降
  - 2 个 seed (42, 137) 均观测到

### D003 决策：不改预注册标准（2026-05-15）
- **entropy 是 pass/fail 主信号**: Gen 0 ρ(loss,entropy)=0.93，满足 >0.7 前提
- **spectral_rank per-example ρ 基线低（|ρ|=0.21）是结构性的**，不是 bug
- **spectral_rank 继续作 corpus-level 辅助观测**（SIGMA-style, Gen 0=4.42）
- **不修改预注册阈值 = 不 rationalize**

## Gen 0→1 信号趋势（2026-05-15）

| 指标 | Gen 0 | Gen 1 (s42) | Gen 1 (s137) | Δ% |
|------|-------|------------|-------------|-----|
| ρ(loss,entropy) | 0.929 | 0.912 | 0.912 | **-1.8%** |
| ρ(loss,spectral) | -0.211 | -0.205 | -0.204 | ~持平 |
| loss_mean | 3.157 | 3.112 | 3.112 | -1.4% |
| entropy_mean | 3.156 | 3.044 | 3.047 | -3.5% |
| spectral_rank_mean | 163.7 | 165.0 | 164.8 | +0.8% |
| corpus_spectral_rank | 4.42 | 4.68 | 4.68 | +5.9% |
| distinct-1/2/3 | .039/.341/.687 | .038/.339/.679 | .038/.340/.682 | ~持平 |

### 关键观察
- **ρ(loss,entropy) 衰减极慢**：1 代仅下降 1.8%。若线性外推 Gen 3≈0.88，远不到 0.5 pass 线
- **但 collapse 通常非线性加速**，Gen 2-3 可能出现急剧下降——需要等数据
- **两 seed 高度一致**：值几乎相同，可重复性好
- **entropy_mean 下降了 3.5%**：信号绝对值在退化，但 ρ 未跟着大幅下降——说明 loss 和 entropy 同步下降
- **corpus_spectral_rank 反升**（4.42→4.68）：反直觉，可能因 1 代混合训练引入了更多多样性

### 风险判断
如果 Gen 2-3 ρ 衰减不加速，MVP 可能 fail。参见下方 Contingency Plan。

## Contingency Plan：如果 entropy ρ 衰减不显著（2026-05-15）

如果 Gen 3 的 |ρ(loss, entropy)| 仍 ≥ 0.5（pass 条件不满足），备选 story：

**(a) 代数不够**: 3 代可能不足以触发深度脱钩。Gen 1→3 如果 ρ 呈下降趋势但未跌破 0.5 → research 阶段扩到 5 代验证。这是最温和的 escalation，成本低（+2 代训练）。

**(b) 每代 tokens 不够**: 200M tokens/gen 可能不足以产生足够的 collapse 压力。如果信号值几乎不变 → 增加到 500M-1B tokens/gen。成本中等，但信号变化应更明显。

**(c) 模型规模太小**: Pythia-410M 可能 collapse 阈值高于大模型。如果 (a)(b) 都不行 → 需 Pythia-1B 或 1.4B 验证。成本最高，但模型越大 collapse 信号越敏感是已知规律。

**决策优先级**: (a) → (b) → (c)，逐步 escalate。不要跳级。

## OOM 修复记录（2026-05-15）

`compute_signals.py` 原先用 `output_hidden_states=True` 返回 Pythia 全 25 层 hidden states（每 batch ~200MB 浪费）。修复：
- forward hook 仅捕获最后一层
- 每 batch 后 `del` 中间变量 + `torch.cuda.empty_cache()`
- 修复已写入磁盘，Gen 2+ 自动生效（subprocess.Popen 调用）

## 论文 Figure/Table Layout 草案（2026-05-15）

### Core Figures
- **Fig 1: PRISM 框架概览图** — 展示 multi-resolution collapse signals → stage-aware mixing 的 pipeline。左侧: 迭代训练循环；中间: 3 类信号（entropy/spectral rank/diversity）的计算示意；右侧: 信号驱动的动态 mixing 比调整。
- **Fig 2: ρ 衰减曲线（MVP 核心结果）** — ρ(loss, entropy) 跨代变化。2 seed 分别画 + 均值线 + 阈值线（0.7/0.5）。这是论文的 **hero figure**，证明脱钩假设。
- **Fig 3: 信号趋势对比** — 2×2 或 1×4 子图：loss / entropy_mean / SIGMA spectral rank / distinct-n 跨代趋势。展示 loss 平稳但其他信号退化的"剪刀差"。

### Core Tables
- **Table 1: Gen 0-3 信号值汇总** — 每代的 loss, entropy, ρ, spectral rank, distinct-n。两 seed 分别列 + 均值。
- **Table 2: 方法对比（Research 阶段）** — AIOLI vs AIOLI+PRISM vs static mixing vs no-mixing baselines。多数据集 × 多指标。

### Supplementary
- **Fig S1: Per-example 信号分布变化** — KDE 曲线展示 loss/entropy/spectral_rank 分布随代际的形变
- **Fig S2: Loss vs Entropy 散点图** — Gen 0 vs Gen 3，直观展示相关性衰减
- **Table S1: 完整 provenance 信息** — 每个实验的超参数、数据量、种子、GPU 小时

## 环境信息（2026-05-15 探测）
- 服务器: rtx6000-diagprobe
- GPU: 2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 各 94GB
- Python 3.12.3 (conda base), PyTorch 2.10.0+cu128
- conda 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 不要用 venv，用 conda base
- **服务器无法直连 HuggingFace**，需 hf-mirror.com 或设 `HF_HUB_OFFLINE=1`（模型已缓存）
- 模型 `EleutherAI/pythia-410m-deduped` (405M params) 已缓存，推理验证通过

## 2-Seed 并行方案
- cuda:0 → seed=42, cuda:1 → seed=137
- Checkpoint 命名: gen{i}_seed{s}/
- 训练用单 GPU（每 seed 独占 1 卡），不用 DDP
