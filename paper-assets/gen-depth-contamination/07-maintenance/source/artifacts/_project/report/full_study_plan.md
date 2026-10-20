# Full Study 实验矩阵预案

> 基于 MVP (Qwen2.5-1.5B-Instruct, C4 5K, depth 0→5, nucleus p=0.95 T=1.0) 的经验推算
> 目标: EMNLP ARR 2026-05-25 提交（剩余 13 天）
> 硬件: 1×RTX 4090D 24GB @ autodl-4090d

---

## 1. 实验矩阵

### 维度 1：模型族

| 模型 | 参数量 | 类型 | HuggingFace 路径 | ModelScope 路径 | VRAM (bf16) | 4090D 可行性 | 推荐 batch_size | 目的 |
|------|--------|------|-------------------|-----------------|-------------|-------------|----------------|------|
| Qwen2.5-1.5B-Instruct | 1.5B | Instruct | `Qwen/Qwen2.5-1.5B-Instruct` | `Qwen/Qwen2.5-1.5B-Instruct` | ~3GB | ✅ 余量 21GB | gen=64, feat=24 | MVP baseline，Instruct 代表真实污染源 |
| Pythia-1.4B | 1.4B | Base | `EleutherAI/pythia-1.4b` | N/A（用 HF_ENDPOINT mirror） | ~2.8GB | ✅ 余量 21GB | gen=64, feat=24 | Base vs Instruct 对比；Drayson et al. 用同系列 |
| OLMo-1B | 1B | Base | `allenai/OLMo-1B-0724-hf` | N/A（用 HF_ENDPOINT mirror） | ~2GB | ✅ 余量 22GB | gen=64, feat=32 | 不同训练方法/数据的 base model family |
| Qwen2.5-7B-Instruct | 7B | Instruct | `Qwen/Qwen2.5-7B-Instruct` | `Qwen/Qwen2.5-7B-Instruct` | ~14GB | ✅ 余量 10GB | gen=8, feat=4 | Cross-scale: K* 是否随模型规模变化 |

**注**: Pythia/OLMo 在 ModelScope 无官方仓库，AutoDL 下载需设 `HF_ENDPOINT=https://hf-mirror.com`。Qwen 系列优先走 ModelScope CDN。

### 维度 2：解码策略消融

| ID | 策略 | 参数 | 目的 | 与 MVP 关系 |
|----|------|------|------|-------------|
| D-greedy | Greedy | T→0 (do_sample=False) | 确定性下界：最大 mode collapse，预测 K* 最小 | 新增 |
| D-p90 | Nucleus p=0.9 | top_p=0.9, T=1.0 | p 值敏感性 | 新增 |
| D-p95 | Nucleus p=0.95 | top_p=0.95, T=1.0 | MVP 默认 | 已有 |
| D-lowT | Low temperature | top_p=0.95, T=0.7 | 温度降低 → 多样性下降速度加快? | 新增 |
| D-highT | High temperature | top_p=0.95, T=1.2 | 温度升高 → 延缓饱和? 支撑 MI 衰减假设检验 | 新增 |

**核心假设检验**: greedy → 近指数 MI 衰减（快速饱和），high-T → 较慢多项式衰减（随机性延缓同质化）。用 AIC/BIC 对比拟合优度。

### 维度 3：生成方式

| 方式 | 配置 | 预估耗时 | 目的 |
|------|------|----------|------|
| Prompt-chain | 直接喂上一代输出给 LLM，用 rewrite prompt | ~2-2.5h/config (1.5B) | Upper bound，MVP 已验证 |
| Retrain-chain | 在上一代输出上 LoRA 微调后再生成 | ~6-8h/config (1.4B) | Ecological validity：模拟真实递归训练污染路径 |

### 维度 4：下游评估

| 评估任务 | 工具 | 说明 | 优先级 |
|----------|------|------|--------|
| MMLU (5-shot) | lm-eval-harness | 知识密集型，对数据质量敏感 (FineWeb-Edu 验证) | P0 |
| HellaSwag (10-shot) | lm-eval-harness | 常识推理，DataComp-LM 标准 benchmark | P0 |
| XSum 摘要 | ROUGE-L | 生成质量评估 | P1 |

**评估方法**: 构造不同深度污染比例的训练集 → LoRA continued pretraining Pythia-1.4B → lm-eval-harness 评估

**过滤策略对比**:
| 策略 | 说明 |
|------|------|
| No filter | 全部混入（baseline） |
| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |
| Depth-graduated | weight = quality(k)/quality(0)，按深度衰减曲线经验推导权重 |
| Surplexity filter | 按 surprisal 高低过滤 |

**污染比例**: 10% / 30% / 50% 合成文本注入

---

## 2. 实验优先级排序

### P0：核心论文支撑（必须完成）

| # | 实验 | 配置 | 预估 GPU 时间 | 依赖 | 论文贡献 |
|---|------|------|-------------|------|----------|
| P0-1 | MVP depth chain | Qwen2.5-1.5B, D-p95, 5K docs, depth 0-5 | ~2.5h | 无 | Pilot K* 判定 (已运行中) |
| P0-2 | 跨模型 depth chain: Pythia | Pythia-1.4B, D-p95, 5K docs, depth 0-5 | ~2.5h | 无 | Cross-model generalization |
| P0-3 | 跨模型 depth chain: OLMo | OLMo-1B, D-p95, 5K docs, depth 0-5 | ~2h | 无 | Cross-model generalization |
| P0-4 | 解码消融: Greedy | Qwen2.5-1.5B, D-greedy, 5K docs, depth 0-5 | ~1.5h | 无 | MI 衰减假设检验 (lower bound) |
| P0-5 | 解码消融: p=0.9 | Qwen2.5-1.5B, D-p90, 5K docs, depth 0-5 | ~2.5h | 无 | p 值敏感性 |
| P0-6 | 解码消融: Low T | Qwen2.5-1.5B, D-lowT, 5K docs, depth 0-5 | ~2.5h | 无 | 温度敏感性 |
| P0-7 | 解码消融: High T | Qwen2.5-1.5B, D-highT, 5K docs, depth 0-5 | ~2.5h | 无 | MI 衰减假设检验 (upper bound) |
| P0-8 | Cross-scale probe | Qwen2.5-7B, D-p95, 5K docs, depth 0-5 | ~10h | 无 | Scale transfer: 1B → 7B |
| P0-9 | 全配置特征提取 | P0-1~8 的所有 depth 数据 | ~3h | P0-1~8 | 特征矩阵构建 |
| P0-10 | Ordinal classifier | CORAL + LightGBM + MLP + baselines | ~3h | P0-9 | C1: depth estimation |
| P0-11 | K* + 饱和边界分析 | per-feature saturation curves, cross-model comparison | ~2h | P0-9 | C2: saturation boundary K* |
| P0-12 | 下游过滤评估 (30%) | 4 策略 × 30% 污染, Pythia-1.4B LoRA, MMLU+HellaSwag | ~16h | P0-10 | C3: graduated filtering > binary |

**P0 总计: ~50h GPU**

### P1：重要消融（强烈期望完成）

| # | 实验 | 配置 | 预估 GPU 时间 | 依赖 | 论文贡献 |
|---|------|------|-------------|------|----------|
| P1-1 | Retrain-chain | Pythia-1.4B, D-p95, LoRA × 5 depths | ~8h | 无 | Ecological validity |
| P1-2 | 下游过滤评估 (10%+50%) | 4 策略 × 2 污染比例, MMLU+HellaSwag | ~24h | P0-10 | 污染剂量效应 |
| P1-3 | Ordinal vs Multinomial vs Regression | 3 种分类范式对比 | ~2h | P0-9 | Ordinal structure 必要性证明 |
| P1-4 | LLM zero/few-shot depth estimation | Qwen2.5-7B 直接判断 depth | ~4h | P0-8 | "为什么不直接用 LLM" baseline |
| P1-5 | Binary detector confidence as depth proxy | DetectGPT/Binoculars score vs true depth | ~3h | P0-9 | "为什么不用 detection confidence" baseline |
| P1-6 | Prompt-chain vs Retrain-chain 特征对比 | 对比两种方式的特征分布差异 + cross-setting transfer | ~2h | P1-1 | Feature 鲁棒性 |
| P1-7 | XSum 下游评估 | 4 策略 × 30%, ROUGE-L | ~8h | P0-10 | 生成质量评估 |

**P1 总计: ~51h GPU**

### P2：锦上添花（有时间就做，否则进 appendix/future work）

| # | 实验 | 配置 | 预估 GPU 时间 | 论文贡献 |
|---|------|------|-------------|----------|
| P2-1 | Pythia × 其他 decoding 策略 | Pythia-1.4B × D-greedy/D-highT | ~4h | 跨模型 × 跨策略交叉 |
| P2-2 | OLMo × 其他 decoding 策略 | OLMo-1B × D-greedy/D-highT | ~3.5h | 同上 |
| P2-3 | Common Crawl 自然验证 | CC 样本 depth prediction + AlignScore proxy | ~5h | Naturalistic validation |
| P2-4 | Learned representation baseline | Frozen LM embeddings + MLP vs handcrafted | ~3h | Baseline completeness |
| P2-5 | Heterogeneous model chain | 交替 Pythia→Qwen→OLMo 生成 | ~4h | 鲁棒性 (appendix) |
| P2-6 | Human editing robustness | Simulated span replacement/paraphrasing | ~3h | 鲁棒性 (appendix) |

**P2 总计: ~22.5h GPU**

---

## 3. 资源规划

### GPU 时间汇总

| 优先级 | GPU 时间 | 累计 |
|--------|---------|------|
| P0 | ~50h | 50h |
| P1 | ~51h | 101h |
| P2 | ~22.5h | 123.5h |
| Buffer (调试/重跑 20%) | ~25h | 148.5h |

### 可用资源

- 1×RTX 4090D, 13 天 = **312h 理论上限**
- 实际可用（考虑文件传输、调试、服务器维护）: **~260h**
- **P0+P1 可完成，P2 部分可完成**

### 1×4090D 是否够用？

**结论: 勉强够，但没有余量应对意外。**

| 情况 | 能否完成 |
|------|---------|
| 只做 P0 | ✅ 充裕（50h / 260h = 19%） |
| P0 + P1 | ✅ 可行（101h / 260h = 39%） |
| P0 + P1 + P2 全部 | ✅ 可行（123.5h / 260h = 48%） |
| P0 + P1 + P2 + buffer | ⚠️ 紧张但可行（148.5h / 260h = 57%） |

**瓶颈不是 GPU 总时间，而是 wall-clock 串行依赖：**

### 关键路径分析

```
Day 1-2:  MVP 完成 (P0-1, 已运行中)
Day 2-3:  P0-2,3 (Pythia + OLMo chains, 各~2.5h, 串行 = 5h)
Day 3-4:  P0-4,5,6,7 (Qwen 1.5B × 4 decoding strategies, 串行 = 9h)
Day 4-5:  P0-8 (7B chain, ~10h)
Day 5-6:  P0-9,10,11 (特征提取 + 分类器 + K* 分析, ~8h)
Day 6-8:  P0-12 (下游过滤评估, ~16h)
--- P0 完成线: Day 8 ---
Day 8-9:  P1-1 (retrain-chain, ~8h)
Day 9-11: P1-2 (更多下游评估, ~24h)
Day 11-12: P1-3,4,5,6 (各种 baselines, ~11h)
Day 12-13: P1-7 或 P2 精选
--- Deadline: Day 13 (May 25) ---
```

**写作并行**: 全程同步进行，不占 GPU。Day 1-3 写 Intro+Related Work，Day 4-6 写 Method，Day 7-10 写 Results，Day 11-13 整合。

### 如果需要加速

| 方案 | 效果 | 建议 |
|------|------|------|
| +1×4090D | P0 和 P1 可完全并行，总 wall-clock 减半 | 强烈建议：可同时跑 7B + 1.5B 实验 |
| +1×A100 40GB | 7B 实验更快(bs 更大)，且可并行 | 最优方案 |
| 减少 P1 scope | 砍 P1-2 (只做 30%不做 10%/50%) + 砍 P1-7 | 节省 ~32h，但论文说服力降 |

**建议向 Director 申请**: 1 块额外 4090D（或同级 GPU），专门跑 P0-8 (7B chain, 10h) 和 P1-2 (下游评估, 24h)，主卡跑其余实验。两卡并行可在 Day 9 完成所有 P0+P1。

### 并行策略（单卡）

所有 depth chain 内部必须串行（depth k 依赖 depth k-1），但不同 config 之间完全独立，可按任意顺序串行执行。建议按优先级排队：

```
Queue: P0-1 → P0-2 → P0-3 → P0-4 → P0-5 → P0-6 → P0-7 → P0-8 → P0-9 → P0-10 → ...
```

如果有 2 卡：
```
GPU-0: P0-1 → P0-2 → P0-3 → P0-4~7 → P0-9 → P0-10 → P0-12
GPU-1: P0-8 (7B) → P1-1 (retrain) → P1-2 (下游评估)
```

---

## 4. Retrain-chain 配置细节

### 目标
模拟真实递归训练污染：不是用 prompt 让模型改写，而是在每一代输出上微调模型后再生成下一代。

### LoRA 配置

| 参数 | 值 | 说明 |
|------|-----|------|
| 模型 | Pythia-1.4B | 选 base model 更合理（retrain 场景通常是 base model） |
| LoRA rank | 16 | 1.4B 模型不需要高 rank |
| LoRA alpha | 32 | 2× rank，标准实践 |
| Target modules | `query_key_value` | Pythia 用 fused QKV；如用 Qwen 则为 `q_proj, k_proj, v_proj, o_proj` |
| Dropout | 0.05 | 防过拟合（小数据集） |
| 训练数据 | 上一代 depth 输出 (5K docs) | depth 0 = C4 human seed |
| Max seq length | 512 | 与 prompt-chain 一致 |
| Epochs | 3 | 5K docs × 3 epochs，不至于过拟合 |
| Learning rate | 2e-4 | LoRA 标准 lr |
| LR scheduler | cosine | 标准 |
| Batch size | 8 | gradient accumulation = 4 → effective batch = 32 |
| Optimizer | AdamW (8-bit) | 用 bitsandbytes 8-bit Adam 省显存 |
| bf16 | True | 4090D 支持 |

### 每轮流程

```
depth k-1 output (5K docs)
    ↓
LoRA fine-tune Pythia-1.4B on depth k-1 output (3 epochs)
    ↓
Merge LoRA weights → new model checkpoint
    ↓
Generate depth k output from depth k-1 prompts using new model
    ↓
重复直到 depth 5
```

### 时间估算

| 步骤 | 每轮耗时 | 说明 |
|------|---------|------|
| LoRA fine-tune | ~40 min | 5K docs × 3 epochs × 512 tokens, bs=8, 4090D |
| LoRA merge | ~2 min | 合并权重到 base model |
| Generation (5K docs, 5 depths worth) | ~25 min | bs=64, 256 new tokens |
| 小计 | ~67 min/轮 | |

| 项目 | 时间 |
|------|------|
| 5 轮 retrain-chain | ~5.6h |
| 特征提取 (6 depths) | ~0.5h |
| 分析 | ~0.5h |
| **总计** | **~6.5h** |

### 与 Prompt-chain 对比分析
- 比较两种方式下的 15 维特征分布差异 (MMD distance)
- 用 prompt-chain 训练的 classifier 在 retrain-chain 数据上的 transfer accuracy
- 报告 K* 是否一致

---

## 5. 已知约束和注意事项

### 必须修复项

| 问题 | 影响 | 修复方案 | 何时修复 |
|------|------|----------|----------|
| **right-padding** | batch generation 质量受影响，padding tokens 干扰 attention | `tokenizer.padding_side = "left"` | Full study 第一行代码 |
| **batch_size 未优化** | GPU 利用率仅 45%，VRAM 空闲 20GB | gen: bs=64, feat: bs=24（1.5B 模型）| Full study pipeline |
| **empty_cache 开销** | 每 batch 调用不必要 | 移除或改为每 N batch 调用 | Full study pipeline |

### AutoDL 环境约束

| 约束 | 应对方案 |
|------|----------|
| C4 加载触发全量 shard 解析 → ProxyError | 用单 shard URL + `HF_ENDPOINT=https://hf-mirror.com` (MVP 已验证) |
| 环境变量不跨 session 生效 | 所有 env vars 写入 `run_*.sh` 启动脚本 |
| `source /etc/network_turbo` | 每个脚本开头都加 |
| SSL 证书问题 | 设置 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE` |
| HF 大模型下载极慢 | Qwen 走 ModelScope；Pythia/OLMo 走 `HF_ENDPOINT` mirror |
| 根分区 30GB 限制 | 所有模型/数据/cache → `/root/autodl-tmp/` |
| `HF_HUB_DISABLE_XET=1` | xet_get 在 AutoDL 返回 401 |
| SSH 端口重启后可能变 | 连接失败时提醒检查端口 |

### MVP 经验迁移

| 经验 | Full Study 应用 |
|------|----------------|
| 5K docs 的 pipeline 约 5-7h (未优化) | 优化后 ~2.5h/config，可靠基准 |
| 15 维特征已实现且 pipeline 可跑 | 直接复用 `run_pipeline.py` 的特征提取代码 |
| LightGBM 5-fold CV 分析框架可用 | 复用，新增 CORAL/CORN ordinal regression |
| Rewrite prompt 格式已验证 | Full study 沿用，retrain-chain 不需要 prompt |

### 代码改造清单（MVP → Full Study）

| 改造项 | 工作量 | 优先级 |
|--------|--------|--------|
| 参数化 model_path / decoding 策略 | 小 (argparse 已有框架) | P0 |
| left-padding 修复 | 1 行 | P0 |
| batch_size 默认值调大 | 1 行 | P0 |
| 支持 greedy decoding (do_sample=False) | 5 行 | P0 |
| 支持 temperature/top_p 参数化 | 5 行 | P0 |
| 新增 CORAL/CORN ordinal regression | ~100 行新代码 | P0 |
| 新增 retrain-chain (LoRA pipeline) | ~200 行新代码 | P1 |
| 新增下游 continued pretraining + eval | ~150 行新代码 | P0 |
| 新增 flash-attn 支持 | 3 行 | P0 |
| 结果自动汇总 + 可视化 | ~100 行 | P0 |

### 风险预案

| 风险 | 概率 | 影响 | 预案 |
|------|------|------|------|
| K* ≤ 2 (大多数配置) | 中 | 论文 depth estimation 价值降低 | 转 saturation characterization 路线: 哪些特征先饱和、不同模型/策略的 K* 差异本身是贡献 |
| 7B 模型 OOM | 低 | 失去 cross-scale 数据 | 降 bs=4 或用 4-bit 量化 (bitsandbytes) |
| Retrain-chain 与 prompt-chain 特征差异过大 | 中 | Cross-setting transfer 不 work | 论文明确定位 prompt-chain 为 upper bound，retrain-chain 作为 ecological validity probe |
| 下游过滤效果不显著 | 中 | C3 (graduated > binary) 难以成立 | (1) 增大污染比例到 50%; (2) 用更敏感的 metric (held-out PPL); (3) 退路：depth signal 仍可作为数据审计工具 |
| 13 天跑不完 P0+P1 | 低 | 论文实验不够充分 | 砍 P1-2 (只保留 30% 污染) + 砍 P1-7 (XSum)，节省 ~32h |

---

## 附录：完整实验矩阵（供参考）

Full matrix = 4 models × 5 decoding × 2 generation methods = 40 种 corpus 配置。加上下游评估和 baselines，总实验数 > 60。

**实际执行的子集（P0+P1）：** 8 corpus configs + 1 retrain-chain + 12 downstream runs + 5 classifier variants = 26 个实验，约 101 GPU 小时。

| Config ID | 模型 | 解码策略 | 生成方式 | 优先级 | GPU 时间 |
|-----------|------|----------|----------|--------|---------|
| C01 | Qwen2.5-1.5B-Instruct | D-p95 | Prompt | P0 | 2.5h (MVP) |
| C02 | Pythia-1.4B | D-p95 | Prompt | P0 | 2.5h |
| C03 | OLMo-1B | D-p95 | Prompt | P0 | 2h |
| C04 | Qwen2.5-1.5B-Instruct | D-greedy | Prompt | P0 | 1.5h |
| C05 | Qwen2.5-1.5B-Instruct | D-p90 | Prompt | P0 | 2.5h |
| C06 | Qwen2.5-1.5B-Instruct | D-lowT | Prompt | P0 | 2.5h |
| C07 | Qwen2.5-1.5B-Instruct | D-highT | Prompt | P0 | 2.5h |
| C08 | Qwen2.5-7B-Instruct | D-p95 | Prompt | P0 | 10h |
| C09 | Pythia-1.4B | D-p95 | Retrain | P1 | 6.5h |
| C10 | Pythia-1.4B | D-greedy | Prompt | P2 | 2h |
| C11 | Pythia-1.4B | D-highT | Prompt | P2 | 2.5h |
| C12 | OLMo-1B | D-greedy | Prompt | P2 | 1.5h |
| C13 | OLMo-1B | D-highT | Prompt | P2 | 2h |
