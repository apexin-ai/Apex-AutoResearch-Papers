# Memory — collapse_aware_reward_rebalancing

## 环境经验

### ArmoRM transformers 兼容性 (2026-05-16)
- **问题**: ArmoRM-Llama3-8B-v0.1 的 `modeling_custom.py` 导入 `LLAMA_INPUTS_DOCSTRING`，该符号在 transformers ≥4.42 中已移除
- **修复**: 将 import 替换为 `LLAMA_INPUTS_DOCSTRING = None`（只用于 docstring 装饰器，不影响推理）
- **注意**: transformers 加载 `trust_remote_code=True` 时从多个位置读取自定义代码，需要 patch 所有副本（模型目录 + .hf_cache/modules/ + .cache/huggingface/modules/）
- **教训**: 用 `trust_remote_code=True` 的模型，先测试 import 兼容性再启动长时间实验

### ArmoRM gating token 容错 (2026-05-16)
- **问题**: ArmoRM `find_token_for_gating` 期望 LLaMA-3 chat template 的 `<|eot_id|>` token，Qwen3 生成的部分空/异常 response 缺少此 token
- **修复**: score_quality 中 batch forward 加 try/except，fallback 逐样本打分，异常样本赋 0.0
- **影响**: 仅 2/8000 batch fallback，0 样本丢失

### AutoDL 目录名转义 (2026-05-16)
- HuggingFace `snapshot_download(local_dir=...)` 创建目录时，模型名中的 `.` 和 `-` 会被转义为 `___` 和 `_hyphen_`
- config.py 路径必须用实际目录名（如 `Qwen3-0___6B`），不是逻辑名

### K 值变更时的关键约束 (2026-05-16)
- **GEN_BATCH_SIZE 必须同步调整**: `GEN_BATCH_SIZE = max(1, 64 // K_CANDIDATES)`，否则 OOM
  - K=4 → batch=16 (16×4=64 seq)
  - K=8 → batch=8 (8×8=64 seq)
  - K=16 → batch=4 (4×16=64 seq)
- **输出目录必须独立**: 每个 K 配置用独立 output dir（outputs_k8/, outputs_k16/ 等），避免 checkpoint 交叉污染
- **HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1**: 所有实验启动命令必须包含（网络不通）

### Full-FT 训练显存约束 (2026-05-16)
- **RTX 5090 32GB 上 Qwen3-0.6B (596M params) full-FT**:
  - fp16 不可用（GradScaler 冲突），必须 bf16
  - batch_size=2 OOM，需要 gradient_checkpointing=True + per_device_train_batch_size=1 + gradient_accumulation_steps=8
  - Generation 阶段 gen_batch_size=16 × K=4 = 64 seq 在独占 GPU 时约占 ~25GB（可行）
- **generate.py:10 仍用 torch.float16**：目前不阻塞（generation 用 fp16 推理比 bf16 快且显存够），但若 generation OOM 则需改为 bf16
- **重要**: cuda:1 上启动新实验前必须确认无残留进程（之前出现过双进程占满显存导致 OOM）

## 决策上下文

### P1 诊断阶梯全面 FAIL (2026-05-16)

**核心发现：3代迭代训练不产生绝对 diversity collapse，只产生 relative suppression。**

| 条件 | Vendi 变化 | 结论 |
|------|-----------|------|
| K=4 LoRA | -0.27% | FAIL |
| K=8 LoRA | -0.03% | FAIL |
| K=4 Full-FT LR=5e-6 | +0.91% | FAIL |
| No-curation baseline (LoRA) | +3.13% | 对照 |
| No-curation baseline (Full-FT) | +1.38% | 对照 |

**关键洞察：**
1. LoRA 不是 collapse 的约束因素（Full-FT 同样不 collapse）
2. 选择压力大小 (K=4 vs K=8) 在 LoRA 下不影响 diversity 轨迹
3. 迭代训练本身使 diversity 上升；curation 抑制这种上升，但不导致下降
4. Relative gap ~3pp/3代 存在，但 narrative 需从 "collapse reversal" 转向 "suppression prevention"

### Full-FT No-Curation Baseline 结果 (carr_fullft_nocuration_01, 2026-05-16)

实验 carr_fullft_nocuration_01 结果:
gen0: {mean_quality: 0.1126, vendi_score: 107.17, self_bleu: 0.0045, perplexity: 8.77, mean_nn_distance: 0.7061, complexity_mean: 2.847}
gen1: {mean_quality: 0.1111, vendi_score: 107.87, self_bleu: 0.0047, perplexity: 8.70, mean_nn_distance: 0.7094, complexity_mean: 2.793}
gen2: {mean_quality: 0.1117, vendi_score: 108.64, self_bleu: 0.0065, perplexity: 8.82, mean_nn_distance: 0.7114, complexity_mean: 2.820}
vendi_decline_pct: +1.38% (diversity 略微上升，无 collapse)
checkpoint_path: /root/autodl-tmp/carr/outputs_fullft_nocuration/gen_2/condition_0/merged
elapsed: 12695s (~3.5h)

**对比 LoRA no-curation baseline (carr_baseline_no_curation_01):**
- LoRA baseline Vendi +3.13%, Full-FT baseline Vendi +1.38%
- Full-FT 的 diversity 增长更温和，但同样无 collapse
- Quality 稳定在 ~0.111-0.113，Self-BLEU 略增（0.0045→0.0065）但绝对值极低

### LR=2e-5 假设 (2026-05-16)
- **动机**: Full-FT K=4 LR=5e-6 的 Vendi 反而上升（+0.91%），与 baseline 趋势一致。怀疑 LR=5e-6 太低导致模型几乎没学到 curated 分布的偏好
- **实验**: carr_fullft_lr2e5_probe_01, LR 提高 4x 到 2e-5，其余配置不变
- **预期**: 如果 underfitting 是问题，更高 LR 应让模型充分学习 top-1 筛选偏好，从而在后续代看到 diversity 下降
- **如果仍然 FAIL**: 说明 0.6B 模型 + 2200 prompts + 3 代在此 task 上根本无法触发 collapse，需要 pivot narrative

### CARR Dry-Run 可行性 FAIL (2026-05-17)

**结论：CARR 自适应权重（MWU）在当前 proxy score 设置下无增量。Direction C 实质性失败。**

- 根因：quality/diversity/complexity 三维 proxy scores 高度相关（Pearson r=0.63-0.77）
- 99.3% selection overlap between adaptive weights and fixed (1/3,1/3,1/3)
- 即使 eta=10，overlap >87%；极端单维权重 (1,0,0)，overlap >61%
- 候选内 score 方差逐代下降（Gen0: 0.0055 → Gen2: 0.0028），进一步压缩 rebalancing 空间
- **CARR 有价值的前提条件（当前均不满足）**：
  1. 维度间弱相关/反相关（需真实独立 RM，非 text heuristic）
  2. 某维度主动退化（collapse scenario，P1 已证伪）
  3. 候选间 score 方差足够大

**教训**：基于文本 heuristic 的 proxy scores（长度→complexity, n-gram→diversity, RM→quality）天然正相关——"好的回答"在各维度都高。要让 multi-objective rebalancing 有意义，必须用本质不同的评估信号（如 embedding diversity vs reward quality 是真正正交的轴）。

### 竞品论文验证结果 (2026-05-17)

5/5 论文全部真实，无幻觉：
- DIVE (2501.00747) ✅ — iterative self-improvement diversity
- DARLING (2509.02534, Facebook) ✅ — **最直接竞品**，online RL quality+diversity
- CD-RLHF (2501.11463, Baidu, ACL 2025) ✅ — curiosity reward for diversity
- GEM (2408.16673, ICLR 2025) ✅ — game-theoretic SFT diversity（GEM 是算法名非论文标题）
- Kirk et al. (2310.06452, ICLR 2024) ✅ — foundational: RLHF reduces diversity

**竞争格局**：DARLING 是最强竞品（Facebook Research，方法更 general），但在 training objective 层面操作。CARR 原本的 differentiator（curation-time lightweight）因 dry-run FAIL 已不成立。

### Pivot 候选方向 (2026-05-16，待 Director 决策)
- A) 换更大模型/更多数据 → 更多参数空间去 overfit（风险：GPU 时间不够）
- B) 换度量 → embedding cluster concentration 或 response mode collapse（风险：ad-hoc）
- C) Reframe 为 "diversity stagnation prevention" → CARR 的价值是促进增长而非逆转下降（最有前景，已有 baseline 数据支撑 relative gap 存在）→ **2026-05-17 dry-run FAIL，C 路径实质死亡**
- D) 增加代数 T=3→T=10 → 让 compounding 效应累积（风险：GPU 时间 3x）

**C→D fallback pipeline: C 已 FAIL，建议切 Direction D（negative result paper）。等待 Director 决策。**

## Pivot Framing Research (2026-05-16)

### 调研结论：Stagnation Framing 可行性评估 = B-（可行但有显著风险）

### 1. 最相关论文（5篇）

| # | 论文 | Venue | 核心发现 | 与 CARR 关系 |
|---|------|-------|---------|-------------|
| 1 | **DIVE: Diversified Iterative Self-Improvement** (arXiv 2501.00747, Jan 2025) | 未确认venue | 首个研究 iterative self-improvement 中 diversity loss 的工作；提出 Sample Pool Expansion + Diversity-aware Data Selection，在 MATH/GSM8k 上 diversity +10-45% | **最直接竞争者**。同样关注 iterative 训练中 diversity 下降，但 focus 在 reasoning tasks 的 self-play 而非 reward curation。CARR 需明确区分：我们是 reward-model-guided curation（外部信号），DIVE 是 self-play（内部信号）|
| 2 | **DARLING: Jointly Reinforcing Diversity and Quality** (Facebook, arXiv 2509.02534, Sep 2025) | 未确认venue | 在 online RL 中引入 learned diversity partition function，同时优化 quality 和 diversity。创意写作+数学上均优于 quality-only RL | **强竞争者**。方法更通用（任何 RL 训练），CARR 更 lightweight（只调 reward rebalancing 权重）。区分点：CARR 是 curation-time 干预，DARLING 是 training-time objective 修改 |
| 3 | **CD-RLHF: Curiosity-Driven RLHF** (ACL 2025, arXiv 2501.11463) | ACL 2025 | 在 RLHF 中加 curiosity intrinsic reward，缓解 diversity-alignment tradeoff | 中等相关。方法层面不同（intrinsic reward vs reward rebalancing），但 motivation 完全重叠。需在 related work 中仔细 position |
| 4 | **GEM: Preserving Diversity in Supervised Fine-Tuning** (ICLR 2025, arXiv 2408.16673) | ICLR 2025 | Game-theoretic SFT，替代 CE loss 以保持 diversity。Llama-3.1-8B 上 +5pt chat / +8pt code | 间接相关。GEM 解决 SFT 阶段问题，我们解决 iterative curation 阶段。可作为 related work 中的 complementary approach |
| 5 | **Understanding the Effects of RLHF on LLM Generalisation and Diversity** (Kirk et al., ICLR 2024, arXiv 2310.06452) | ICLR 2024 | 首次系统证明 RLHF 显著降低 output diversity（vs SFT），建立 diversity-alignment tradeoff | **foundational reference**。为整个领域奠基。注意：他们观测到的是 *absolute* diversity reduction，我们观测到的是 relative stagnation——这是区分点 |

### 2. 核心问题回答

**Q1: 有没有论文已经指出 "iterative curation 抑制 diversity 增长"？**
- **没有精确匹配。** DIVE 最接近，但它研究的是 iterative self-improvement（模型在自己生成的数据上训练），观测到 absolute diversity decline。我们的 observation 更微妙：diversity 不下降，只是增长被抑制。这个 "stagnation vs decline" 的区分目前无人明确提出。
- **Novelty 空间存在但狭窄。** 如果只讲 "curation 导致 stagnation"，novelty 薄弱（Kirk 2024 已经建立了 alignment 降低 diversity 的大方向）。需要 CARR 方法本身足够有差异化。

**Q2: "防止 stagnation" 作为 contribution 是否比 "防止 collapse" 弱？**
- **是的，显著更弱。** "Collapse" 暗示系统失败，urgency 强；"stagnation" 暗示 suboptimal，urgency 弱。
- **但有先例可循：** DARLING 和 GEM 都没有 claim "preventing collapse"，而是 "jointly improving quality AND diversity" 或 "preserving diversity"。这种 positive framing（"我们让它更好"而非"我们修复了问题"）在顶会是可以接受的。
- **关键转换**：不要说 "prevents stagnation"（消极），而说 **"maintains diversity growth under reward-guided curation"**（积极）或更强的 **"unlocks diversity-quality co-improvement in iterative reward curation"**（对标 DARLING 的 framing）。

**Q3: "maintains diversity growth under curation pressure" 是否被现有数据支撑？**
- **目前数据不足。** 现有数据只证明了 *问题存在*（curation stagnates, baseline grows）。CARR 方法尚未实际运行，无法证明它 *恢复了增长*。
- **需要的数据**：Curation + CARR 条件下 Vendi Score 上升（理想 ≥ baseline 的 +3%）。
- **风险**：如果 CARR 只恢复到 +1-1.5%，effect size 太小（3pp gap 中只补回一半），reviewer 会质疑 practical significance。

### 3. Framing 可行性评估

**总体评级：B-（可行但需额外实验 + 精确定位）**

**支撑因素（+）：**
- "Diversity preservation under iterative optimization" 是 2024-2025 热点话题（5+ 顶会论文）
- 我们的 specific setting（reward-guided curation with selection pressure K）尚无直接研究
- "Stagnation" 观察本身是 novel empirical finding
- CARR 作为 lightweight reward rebalancing（vs DARLING 的 learned partition / CD-RLHF 的 curiosity module）有 simplicity 优势

**风险因素（-）：**
- 竞争激烈：DARLING (Facebook)、CD-RLHF (ACL 2025)、DIVE、GEM 都在相邻空间
- Effect size concern：3pp relative gap / 3 rounds → 如果 CARR 补回 1-2pp，practical significance 存疑
- 缺失关键实验：CARR 实际效果数据为零
- "Stagnation" narrative 的 reviewer appeal 弱于 "collapse"
- EMNLP DDL 2026-05-25 仅剩 9 天，时间极紧

**如果走这条路，必须满足的条件：**
1. CARR 实验显示 curation + CARR ≥ baseline diversity growth（+3% 或更多）
2. 同时 quality 不下降（否则 trivial solution 是不做 curation）
3. Framing 必须是 positive（"unlocks co-improvement"）而非 defensive（"prevents stagnation"）
4. Related work 必须精确 position vs DARLING/CD-RLHF/DIVE，强调 setting 和 method 差异
