# 7B/14B 扩展实验计划

> 创建: 2026-05-18 | 硬件: 4× A100 80GB (待审批)

## 一、实验矩阵

### 模型
| 模型 | 参数量 | 角色 | HuggingFace ID |
|------|--------|------|----------------|
| Qwen2.5-7B | 7.6B | 主线 scale-up | Qwen/Qwen2.5-7B |
| Qwen2.5-14B | 14.7B | Scale frontier | Qwen/Qwen2.5-14B |
| Llama-3.1-8B | 8.0B | Cross-family 7B 验证 | meta-llama/Llama-3.1-8B |

### Dosage × Seed
- Dosage: d000 (0%), d005 (5%), d025 (25%), d100 (100%)
- Seeds: 42, 123
- 每模型 4 × 2 = 8 runs → 3 模型 × 8 = **24 SFT runs**

---

## 二、Phase 1: SFT Training (24 runs)

### LoRA 配置 (与 ≤3B 保持一致)

| 参数 | 7B / 8B | 14B |
|------|---------|-----|
| LoRA rank | 16 | 16 |
| LoRA alpha | 32 | 32 |
| Target modules | q,k,v,o,gate,up,down_proj | 同左 |
| LR | 5e-5 | 5e-5 (如不稳降至 3e-5) |
| Batch size | 1 | 1 |
| Grad accum | 16 | 16 |
| Effective batch | 16 | 16 |
| Epochs | 1 | 1 |
| Max seq length | 2048 | 2048 |
| Precision | bf16 | bf16 |

### VRAM 估算

| 模型 | Base (bf16) | LoRA + Optimizer | Activations | 总计 | 单卡 A100? |
|------|-------------|------------------|-------------|------|-----------|
| 7B | ~14 GB | ~8 GB | ~10 GB | ~32 GB | ✅ 单卡 |
| 14B | ~28 GB | ~12 GB | ~15 GB | ~55 GB | ✅ 单卡 |
| 8B | ~16 GB | ~8 GB | ~10 GB | ~34 GB | ✅ 单卡 |

### 时间估算

参考 ≤3B 实测数据 (RTX 4090D):
- 0.5B: ~1h, 1.5B: ~3h, 3B (Qwen): ~4.5h, 3B (Llama): ~2.5h
- A100 80GB vs 4090D: bf16 吞吐约 1.3-1.5× (A100 HBM 带宽优势)

| 模型 | 参数倍数 (vs 3B) | 估算/run (A100) | 8 runs 总计 |
|------|-------------------|-----------------|-------------|
| Qwen2.5-7B | 2.5× | **6-8h** | 48-64h |
| Qwen2.5-14B | 4.9× | **12-16h** | 96-128h |
| Llama-3.1-8B | 2.7× | **5-7h** | 40-56h |
| **合计** | | | **184-248 GPU-h** |

### 完整 Run 列表

| Run ID | Model | Dosage | Seed | Est. Time |
|--------|-------|--------|------|-----------|
| sft_7B_d000_s42 | Qwen2.5-7B | d000 | 42 | 6-8h |
| sft_7B_d005_s42 | Qwen2.5-7B | d005 | 42 | 6-8h |
| sft_7B_d025_s42 | Qwen2.5-7B | d025 | 42 | 6-8h |
| sft_7B_d100_s42 | Qwen2.5-7B | d100 | 42 | 6-8h |
| sft_7B_d000_s123 | Qwen2.5-7B | d000 | 123 | 6-8h |
| sft_7B_d005_s123 | Qwen2.5-7B | d005 | 123 | 6-8h |
| sft_7B_d025_s123 | Qwen2.5-7B | d025 | 123 | 6-8h |
| sft_7B_d100_s123 | Qwen2.5-7B | d100 | 123 | 6-8h |
| sft_14B_d000_s42 | Qwen2.5-14B | d000 | 42 | 12-16h |
| sft_14B_d005_s42 | Qwen2.5-14B | d005 | 42 | 12-16h |
| sft_14B_d025_s42 | Qwen2.5-14B | d025 | 42 | 12-16h |
| sft_14B_d100_s42 | Qwen2.5-14B | d100 | 42 | 12-16h |
| sft_14B_d000_s123 | Qwen2.5-14B | d000 | 123 | 12-16h |
| sft_14B_d005_s123 | Qwen2.5-14B | d005 | 123 | 12-16h |
| sft_14B_d025_s123 | Qwen2.5-14B | d025 | 123 | 12-16h |
| sft_14B_d100_s123 | Qwen2.5-14B | d100 | 123 | 12-16h |
| sft_8B_d000_s42 | Llama-3.1-8B | d000 | 42 | 5-7h |
| sft_8B_d005_s42 | Llama-3.1-8B | d005 | 42 | 5-7h |
| sft_8B_d025_s42 | Llama-3.1-8B | d025 | 42 | 5-7h |
| sft_8B_d100_s42 | Llama-3.1-8B | d100 | 42 | 5-7h |
| sft_8B_d000_s123 | Llama-3.1-8B | d000 | 123 | 5-7h |
| sft_8B_d005_s123 | Llama-3.1-8B | d005 | 123 | 5-7h |
| sft_8B_d025_s123 | Llama-3.1-8B | d025 | 123 | 5-7h |
| sft_8B_d100_s123 | Llama-3.1-8B | d100 | 123 | 5-7h |

---

## 三、Phase 2: Evaluation (24 models × 3 benchmarks × 2 formats)

每个训练完的 checkpoint 评估：

| Benchmark | 格式 | Items | Est./model (7B) | Est./model (14B) |
|-----------|------|-------|-----------------|------------------|
| MMLU | original + para_aligned | ~14K (1K subsample) | ~1h | ~2h |
| GSM8K | original + para_aligned | ~1.3K | ~30min | ~1h |
| ARC-Challenge | original + para_aligned | ~1.2K | ~20min | ~40min |
| **合计/model** | | | **~2h** | **~4h** |

- 24 models → 总计: 8×2h (7B) + 8×4h (14B) + 8×2h (8B) = **64 GPU-h**
- 可 batch 多 dosage 同时评估 (4 GPU 并行), wall time ~16h

### Eval Run 列表 (按 batch)

| Eval ID | Model Checkpoint | Benchmarks |
|---------|------------------|------------|
| eval_7B_d{000,005,025,100}_s{42,123} | 8 checkpoints | MMLU + GSM8K + ARC (orig + para) |
| eval_14B_d{000,005,025,100}_s{42,123} | 8 checkpoints | 同上 |
| eval_8B_d{000,005,025,100}_s{42,123} | 8 checkpoints | 同上 |

---

## 四、Phase 3: Signal Computation (24 models × 3 signals)

| Signal | 方法 | Est./model (7B) | Est./model (14B) |
|--------|------|-----------------|------------------|
| S1 | Embedding similarity | ~2h | ~4h |
| S2 | Min-K++ | ~2h | ~4h |
| S4 | Self-critique | ~2h | ~4h |
| **合计/model** | | **~6h** | **~12h** |

- 24 models → 总计: 8×6 (7B) + 8×12 (14B) + 8×6 (8B) = **192 GPU-h**
- 4 GPU 并行, wall time ~48h

### Signal Run 列表

| Signal ID | Model | Signals | Est. Time |
|-----------|-------|---------|-----------|
| sig_7B_d{000,005,025,100}_s{42,123} | 8 Qwen2.5-7B checkpoints | S1+S2+S4 | 6h each |
| sig_14B_d{000,005,025,100}_s{42,123} | 8 Qwen2.5-14B checkpoints | S1+S2+S4 | 12h each |
| sig_8B_d{000,005,025,100}_s{42,123} | 8 Llama-3.1-8B checkpoints | S1+S2+S4 | 6h each |

---

## 五、Phase 4: IRT Fitting

### 扩展后的 Respondent Pool

| 来源 | Models | 数量 |
|------|--------|------|
| 现有 ≤3B (Qwen 0.5B/1.5B/3B + Llama 3.2-3B) | 部分排除后 | ~16 (J=16 当前) |
| 新增 Qwen2.5-7B | 4 dosages × 2 seeds | +8 |
| 新增 Qwen2.5-14B | 4 dosages × 2 seeds | +8 |
| 新增 Llama-3.1-8B | 4 dosages × 2 seeds | +8 |
| **合计** | | **J ≈ 40** |

### IRT 分析计划

| Analysis | Model | N (respondents) | 备注 |
|----------|-------|-----------------|------|
| Pooled MMLU | 2PL+γ | ~36 (excl 0.5B) | 主结果, N≥30 满足 |
| Pooled GSM8K | 2PL+γ | ~40 | 含 0.5B |
| Pooled ARC | 2PL+γ | ~36 (excl 0.5B) | 含 0.5B 时标注 |
| MMLU domain-level | 2PL+γ per domain | ~36 | Simpson's paradox 验证 |
| Within-family Qwen | 2PL+γ | ~24 (0.5B-14B) | Scale-dependent γ |
| Cross-family 7B/8B | 2PL+γ | ~16 (7B+8B only) | Family effect at matched scale |
| Scale-conditional | 分层 | per scale | γ 随 scale 变化趋势 |

**关键科学问题**: N=40 的 pooled IRT 将大幅提升 γ 估计精度 (当前 N=16 CI 很宽), 且首次达到 paper_framing 中建议的 N≥30 minimum。

- IRT fitting: CPU-only, ~2-4h per benchmark (Stan MCMC)
- 不占 GPU 时间

---

## 六、4 卡并行排布方案

### 原则
1. 7B 和 8B 单卡 (~32-34 GB VRAM), 14B 单卡 (~55 GB) — 全部单卡可跑
2. 同 seed 的不同 dosage 可并行 (无依赖)
3. Phase 之间有依赖: SFT → Eval → Signals → IRT
4. 同一 checkpoint 的 eval 和 signals 在 SFT 完成后才能开始
5. 7B/8B 先跑 (更快), 完成后 GPU 释放给 eval/signals, 14B 最后

### Day 1: 7B + 8B Seed 42 (wall ~8h)

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | sft_7B_d000_s42 | 6-8h |
| GPU 1 | sft_7B_d005_s42 | 6-8h |
| GPU 2 | sft_8B_d000_s42 | 5-7h |
| GPU 3 | sft_8B_d005_s42 | 5-7h |

GPU 2/3 先完成 → 立即启动:

| GPU | Run | Est. |
|-----|-----|------|
| GPU 2 | sft_8B_d025_s42 | 5-7h |
| GPU 3 | sft_8B_d100_s42 | 5-7h |

### Day 1 (续) → Day 2: 7B s42 剩余 + 8B s123 (~8h)

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | sft_7B_d025_s42 | 6-8h |
| GPU 1 | sft_7B_d100_s42 | 6-8h |
| GPU 2 | sft_8B_d000_s123 | 5-7h |
| GPU 3 | sft_8B_d005_s123 | 5-7h |

→ GPU 2/3 完成后:

| GPU | Run | Est. |
|-----|-----|------|
| GPU 2 | sft_8B_d025_s123 | 5-7h |
| GPU 3 | sft_8B_d100_s123 | 5-7h |

### Day 2 (续) → Day 3: 7B s123 + 开始 14B (~8-16h)

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | sft_7B_d000_s123 | 6-8h |
| GPU 1 | sft_7B_d005_s123 | 6-8h |
| GPU 2 | sft_14B_d000_s42 | 12-16h |
| GPU 3 | sft_14B_d005_s42 | 12-16h |

GPU 0/1 完成后 → 启动:

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | sft_7B_d025_s123 | 6-8h |
| GPU 1 | sft_7B_d100_s123 | 6-8h |

→ GPU 0/1 再次完成后, 开始已完成 checkpoint 的 eval:

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | eval_7B_batch_s42 (4 checkpoints) | ~4h |
| GPU 1 | eval_8B_batch_s42 (4 checkpoints) | ~4h |

### Day 3 (续) → Day 4: 14B s42 剩余 + eval/signal pipeline (~16h)

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | eval_7B_batch_s123 → sig_7B_d000_s42 | ~4h + 6h |
| GPU 1 | eval_8B_batch_s123 → sig_8B_d000_s42 | ~4h + 6h |
| GPU 2 | sft_14B_d025_s42 | 12-16h |
| GPU 3 | sft_14B_d100_s42 | 12-16h |

### Day 4-5: 14B s123 + 7B/8B signals (~32h)

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0 | sig_7B (remaining checkpoints) | 6h × N |
| GPU 1 | sig_8B (remaining checkpoints) | 6h × N |
| GPU 2 | sft_14B_d000_s123 | 12-16h |
| GPU 3 | sft_14B_d005_s123 | 12-16h |

→ 14B s42 eval 开始 (GPU 0/1 空闲时穿插):

| GPU | Run | Est. |
|-----|-----|------|
| GPU 0/1 | eval_14B_batch_s42 | ~8h |

→ GPU 2/3 完成后:

| GPU | Run | Est. |
|-----|-----|------|
| GPU 2 | sft_14B_d025_s123 | 12-16h |
| GPU 3 | sft_14B_d100_s123 | 12-16h |

### Day 5-6: 14B eval + signals + IRT (~24-32h)

| GPU | Run |
|-----|-----|
| GPU 0-1 | sig_7B/8B 剩余 → eval_14B_batch_s123 |
| GPU 2-3 | sig_14B (12h each) |

IRT fitting (CPU) 可在所有 eval + signals 完成后立即开始, 不占 GPU。

---

## 七、时间与成本总结

### GPU 时间

| Phase | GPU-hours | Wall time (4 GPU) |
|-------|-----------|-------------------|
| Phase 1: SFT Training | 184-248h | ~62-72h |
| Phase 2: Evaluation | 64h | ~16h |
| Phase 3: Signals | 192h | ~48h |
| Phase 4: IRT | 0 (CPU) | ~8h |
| **总计** | **440-504 GPU-h** | **~134-144h** |

### Wall Time 估算 (含 pipeline 重叠)

由于 eval/signals 可在 SFT 完成后立即开始 (pipeline parallelism), 实际 wall time:
- **乐观**: ~5 天 (120h) — 一切顺利, 无重试
- **保守**: ~6-7 天 (168h) — 含调试、重试
- **EMNLP deadline**: 2026-05-25, 距今 7 天 → **时间极紧**

### 成本估算

AutoDL A100 80GB: ~3.5-4.5 CNY/卡/时
- 4 卡 × 144h = 576 卡时
- 费用: 576 × 4.0 = **~2,300 CNY**
- 含 buffer: **2,500-3,000 CNY**

---

## 八、风险与缓解

| # | 风险 | 影响 | 缓解 |
|---|------|------|------|
| 1 | **14B VRAM 溢出** | 训练 OOM | bf16 + LoRA r16 预计 ~55GB; 若 OOM → gradient checkpointing 或降低 max_seq_len 至 1024 |
| 2 | **Llama-3.1-8B gated access** | 无法下载模型 | 提前申请 meta-llama 权限 (HuggingFace); 备选 Llama-3.2-8B 或 Mistral-7B |
| 3 | **14B 训练不稳定** | Loss spike / NaN | 监控 wandb; 备选: 降 lr 至 3e-5, warmup ratio 0.1→0.2 |
| 4 | **时间不够 (7天 deadline)** | 无法完成全部 24 runs | 降级方案见第九节 |
| 5 | **数据集不适配** | 7B/14B SFT 效果异常 | 先跑 d000+d100 各 1 run 做 sanity check, 确认无问题再全量展开 |
| 6 | **Min-K++ 在 7B 仍 reversal** | 影响 signal quality | 预期 7B 可能改善 (scale-dependent); 无论结果都是有价值的发现 |
| 7 | **IRT N=40 后 γ 仍不显著** | Null finding 扩大 | 论文 framing 已为此准备: "contamination needs no calibration" 是有效结论 |
| 8 | **磁盘空间不足** | 14B checkpoint ~30GB each | 24 checkpoints × 30GB = ~720GB; 确保 /root/autodl-tmp 有 1TB+ 空间 |

---

## 九、降级方案 (若时间不足)

### Plan A: 全量 (24 runs) — 需 6-7 天
如上所述。

### Plan B: 精简 (16 runs) — 需 4-5 天
- Qwen2.5-7B: 4 dosages × 2 seeds = 8 runs ✅
- Qwen2.5-14B: 4 dosages × **1 seed (s42)** = 4 runs
- Llama-3.1-8B: 4 dosages × **1 seed (s42)** = 4 runs
- 节省 ~128 GPU-h, 与 ROADMAP 原始计划一致

### Plan C: 最小验证 (8 runs) — 需 2-3 天
- Qwen2.5-7B: d000 + d100 × 2 seeds = 4 runs (验证 scale 效应)
- Llama-3.1-8B: d000 + d100 × 1 seed = 2 runs (cross-family)
- Qwen2.5-14B: d000 + d100 × 1 seed = 2 runs (scale frontier)
- 仅 extreme dosage, 足以验证 γ 方向和 scale 趋势

---

## 十、启动前 Checklist

- [ ] Manager 审批 4× A100 80GB
- [ ] HuggingFace Llama-3.1-8B 访问权限申请
- [ ] AutoDL 实例创建, 确认 CUDA + PyTorch 版本
- [ ] 代码同步到新服务器 (git clone + pip install -e .)
- [ ] 确认磁盘空间 ≥ 1TB
- [ ] 下载 base models: Qwen2.5-7B, Qwen2.5-14B, Llama-3.1-8B
- [ ] Sanity check: 每个 model 跑 1 step SFT 确认无 OOM
- [ ] wandb 项目配置

---

## 十一、对论文的预期影响

### 新增数据量
- Respondents: J = 16 → ~40 (2.5× increase)
- Scale 覆盖: 0.5B-3B → 0.5B-14B (28× range)
- Cross-family: Llama-3.2-3B only → + Llama-3.1-8B

### 预期强化的 Claims
1. **Scale-dependent γ**: 7B/14B 预期 γ→0 (contamination 对大模型影响更小), 确认 "scale modulation" 趋势
2. **N=40 IRT 精度**: CI 宽度 ∝ N^{-0.48}, 从 N=16 到 N=40 → CI 缩窄 ~37%
3. **Cross-family at matched scale**: 7B Qwen vs 8B Llama 直接对比, 控制 scale 变量
4. **Signal 行为**: Min-K++ 是否在 7B+ 恢复正常方向 (当前 0.5B reversal)

### 需要更新的论文 Sections
- Table 4 (Pooled IRT results): N 列更新, 可能需重新 fit
- Table 2 (Signal AUC): 新增 7B/14B 行
- Figure 3 (Dose-response curves): 新增 scale 维度
- §4.1 Results: Scale-dependent 分析
- §5 Discussion: N=40 identifiability 改善讨论
- Abstract: 更新 model 覆盖范围描述

---

## 十二、依赖关系图

```
Phase 1: SFT Training (24 runs)
    │
    ├── 每个 checkpoint 完成后 ──┬── Phase 2: Evaluation
    │                            │     (该 checkpoint)
    │                            │
    │                            └── Phase 3: Signals
    │                                  (该 checkpoint)
    │
    └── 全部 checkpoint 完成 ──── Phase 2+3 全部完成
                                       │
                                       └── Phase 4: IRT Fitting (CPU)
                                             │
                                             └── 论文更新
```

Pipeline parallelism: 7B/8B 训练完成的 checkpoint 可立即进入 eval/signal 阶段, 无需等待所有 SFT 完成。14B 训练期间, 空闲 GPU 处理 7B/8B 的 eval+signals。