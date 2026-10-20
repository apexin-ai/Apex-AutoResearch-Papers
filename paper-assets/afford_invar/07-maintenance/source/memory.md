# afford_invar — Memory

## [失败模式] v2 Heatmap 空间信号是训练 overfitting (2026-05-20)

phase1_transfer_v2 训练中 hm_ent 8.7→6.5 看似"积极信号"，但 held-out eval 证明是幻觉：
- **训练轨迹**: 8.74(init) → 5.33(step200 瞬态) → 6.51(step1000) → 7.8-8.0(step7500+) — 不可持续
- **Eval (checkpoint-9000)**: hm_ent=11.54, peak_dist=82.9px, mass_ratio=0.97x — 全部 FAIL，接近 uniform
- **Train/eval gap**: 训练 7.8 vs eval 11.5 — decoder 记住了训练样本模式但完全无法泛化
- **教训**: 训练 hm_ent 下降不能作为空间结构学习的证据。未来实验必须在 1000-step 硬判断时同时跑 held-out eval，不仅看训练指标。checkpoint cleanup 也不能删掉用于 eval 的 checkpoint。

## [失败模式] LIBERO-Goal 指令间正对稀缺 (2026-05-20)

v2 的 pos=0.27/step (v1 的 1.55/step) 不是 bug——LIBERO-Goal 10 条指令中仅 1/45 对 SigLIP sim > 0.80。
- v1 可能用了 LIBERO-Spatial（"pick up black bowl from X" 结构相似→大量正对）
- **修复**: paraphrase augmentation（task identity 决定正负对，不依赖 SigLIP sim）或降 threshold
- **教训**: pair mining 依赖指令间语义相似度，但 LIBERO-Goal 指令多样性高。Contrastive learning 的正对来源必须在实验前验证充足

## Phase 1 关键教训：L_consist 单独不能驱动空间选择性 (2026-05-19)

**实验 phase1_lconsist_v1 negative 结果的根因分析：**

1. L_consist 只约束 paraphrase 一致性，不约束空间选择性。Decoder 的 trivial solution（均匀 heatmap）完美满足一致性约束（KL=0），但无空间结构。
2. L_action 不流经 decoder——decoder 唯一的训练信号是 L_consist。没有下游任务梯度驱动 decoder 学习有意义的空间分布。
3. 增大 alpha 无法解决：L_consist 梯度仍指向均匀解。需要额外信号源。
4. lambda_H（entropy 正则）可防 delta 坍缩但无法防均匀坍缩——entropy 正则和 trivial solution 方向一致。

**设计启示**：Decoder 必须有 spatial selectivity 的监督信号。候选：L_action gating（heatmap 参与 action prediction）、L_transfer（跨物体 InfoNCE）、或两者组合。

## [失败模式] spatial_normalize global avg pool 毁掉 contrastive learning (2026-05-20)

phase1_transfer_v1 L_xfr 锁死 4.1744（= ln(65) chance level）2000 步无改善。根因：`features * heatmap → global_avg_pool → L2_norm → (B,C)` 完全丢失空间信息，InfoNCE 无法区分不同空间模式。
- **修复（D011）**: 方案 A — decoder pre-softmax 4×4 spatial grid + projection head (Flatten→Linear→ReLU→Linear, 18688 params)
- **教训**: contrastive loss 的特征表示必须保留空间维度；global avg pool 是 spatial contrastive learning 的 anti-pattern

## [失败模式] 磁盘管理 (2026-05-20)

1. **根分区爆满**: checkpoint 默认写 `/root/afford_invar/runs/`（根分区 30G），多实验累积导致 100% 满
   - **修复**: symlink `/root/afford_invar/runs/ → /root/autodl-tmp/afford_invar/runs/`
   - **预防**: 所有 --run_root_dir 指向 `/root/autodl-tmp/afford_invar/runs/`

2. **OFT finetune.py 保存 15GB merged checkpoint**: 每 500 步存完整模型（base+LoRA merge），20000 步需 600GB
   - **修复**: `--merge_lora_during_training False` + `--save_freq 2000`，checkpoint 降至 756MB
   - **教训**: OFT 原始脚本 save 逻辑是 merge 后存，不像 afford 脚本只存 LoRA adapter。提交 OFT baseline 前必须估算 checkpoint 总量

3. **phase1_lconsist_v1_cont 崩溃**: 实际是 `--resume` 参数解析错误（exitcode 2），非磁盘满

## Phase 0.5 多层扫描结果 (2026-05-19)

| Layer | Attn KL (real) | Real/Dummy Ratio | Image Cos Dist |
|------:|---------------:|-----------------:|---------------:|
| 4     | 2.46e-05       | 5.70x            | 1.45e-06       |
| 8     | 8.02e-05       | 3.44x            | 8.95e-06       |
| 12    | 1.58e-04       | 2.41x            | 2.11e-05       |
| 18    | 1.91e-04       | 2.74x            | 3.54e-05       |
| 24    | 2.02e-04       | 2.85x            | 6.29e-05       |
| 30    | 1.17e-04       | 1.39x            | 1.17e-04       |

Layer 24 text-image coupling 最强，但 Director 决定用 Layer 18（差异噪声级）。

## L_transfer 正对密度 (2026-05-19)

| Threshold | Positive Pairs | Avg Pos/Anchor |
|-----------|----------------|----------------|
| 0.80      | 5,986          | 15.3           |
| 0.85      | 1,867          | 4.8            |
| 0.90      | 485            | 1.2            |

MARGINAL at 0.85, SUFFICIENT at 0.80。跨 suite 正对为零——L_transfer 只在同 suite 内起作用。815/1867 正对来自 libero_90 内部（相同指令不同 task）。12 个任务在 0.85 完全孤立。

## Phase 0 完整结果 (2026-05-19)

### Tier 分布 (SigLIP embedding, 650 paraphrases from Qwen3-4B)
- Tier-1 (trivial, >0.95): 170 (26.2%)
- Tier-2 (moderate, 0.80-0.95): 185 (28.5%)
- Tier-3 (deep, <0.80): 295 (45.4%)
- **Tier-2+: 480 (73.8%)** → 远超 40% PASS 阈值

### KL + Hidden State Divergence (Layer 18, 真实 LIBERO 图片)

| 指标 | 真实图片 | Dummy | 倍率 |
|------|----------|-------|------|
| Attention KL | 1.91e-4 nats | 7.0e-5 | 2.7x |
| Cosine dist (all tokens) | 0.0277 (sim 0.972) | 0.0284 | ~1x |
| Cosine dist (image tokens) | 3.5e-5 (sim 0.99997) | 2.3e-5 | 1.5x |
| Normalized L2 (all tokens) | 2.03 | 1.89 | ~1x |

**核心发现**: text tokens 有 divergence (sim 0.972)，但 image tokens 几乎完全不变 (sim 0.99997)。

### 结果文件
- Paraphrases: `/root/afford_invar/data/paraphrases.json` (130 tasks × 5, 61KB)
- Phase 0 results: `/root/afford_invar/results/phase0/`
- Layer scan: `/root/afford_invar/results/phase0/layer_scan/`
- L_transfer density: `/root/afford_invar/results/ltransfer_pair_density.json`

## Phase 1 代码实现 (2026-05-19)

### 完成的模块
1. **AffordanceDecoder** (`prismatic/models/affordance_decoder.py`): 1.72M params (含 transfer_proj 18688), Layer-18 features → 3 transposed conv + GroupNorm + FiLM → 128×128 heatmap
2. **ConsistencyLoss** (`prismatic/training/consistency_loss.py`): pairwise symmetric KL + entropy regularization
3. **TransferLoss** (`prismatic/training/transfer_loss.py`): InfoNCE + TransferPairMiner + feature queue
4. **finetune_afford.py** (`vla-scripts/finetune_afford.py`): L_consist 训练循环 + GRAD MONITOR
5. **finetune_afford_transfer.py** (`vla-scripts/finetune_afford_transfer.py`): L_transfer 训练入口（v2: transfer_proj 替代 spatial_normalize）
6. **Heatmap 评估** (`scripts/evaluation/`): extract_ground_truth.py + heatmap_metrics.py + run_heatmap_eval.py + eval_pride.py

### 已修复的 CRITICAL bug
- hidden_states off-by-one: `hidden_states[layer_idx]` → `hidden_states[layer_idx + 1]`
- token 布局: OpenVLA 实际是 `[image(256)][BOS+text...]`。image token: `[:, :NUM_PATCHES, :]`
- BatchNorm → GroupNorm
- spatial_normalize global avg pool → transfer_proj (4×4 grid + MLP)

### CLI 参数实际名称（踩过坑）
- `--paraphrases_path`（非 --paraphrase_file）
- `--save_freq`（非 --save_steps）
- 无 `--adapter_tmp_dir` 参数（第一次提交因此崩溃）
- 需要 `torchrun`（内部用 DDP dist.barrier）

### OFT 原始训练配置
- LoRA rank=32, alpha=16, target=all-linear, LR=5e-4, batch=8
- Total trainable: ~263M (LoRA 111M + action_head 151M + decoder 1.7M)

## PRIDE 指标验证 (2026-05-19, arXiv:2603.28301)

- **PD 公式**: PD = 1 - (α·SK + (1-α)·ST), α=0.5 ✅ 与我们实现一致
- **SK** (Keyword Similarity): Sentence-BERT (all-MiniLM-L6-v2) 编码 content words (NOUN/VERB/ADJ/ADV)，每个原始词与 paraphrase 词取 max cosine，再平均
- **ST** (Structural Similarity): Zhang-Shasha tree edit distance on dependency parse trees，节点标签=(dep, POS)
- **PRIDE 聚合（关键）**: `PRIDE(α) = Σ(success_i × PD_i) / Σ(PD_i) × 100` — 是 **PD 加权成功率**，不是简单均值。更难的 paraphrase（PD 大）权重更高
- **方向**: Higher = more robust
- **OFT baselines**: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)
- **实现注意**: 论文官方代码用 `libero_para_metadata.csv` 预计算 SK/ST，可直接复用
- **来源**: [arXiv HTML](https://arxiv.org/html/2603.28301v1), [GitHub](https://github.com/cau-hai-lab/LIBERO-Para)

## LIBERO-Para 调研结论 (2026-05-19)

- 原始 LIBERO-Goal SR: OFT_goal 97.9%, OFT_mixed 96.1% → paraphrase 退化 ~33pp
- 80-96% 失败来自 planning-level trajectory divergence

## 环境信息 (2026-05-20)

- 服务器: westd-19957, 4x RTX PRO 6000 Blackwell (94GB each)
- conda base: Python 3.12.3, PyTorch 2.8.0+cu128
- transformers: OFT fork 4.40.1 (moojink/transformers-openvla-oft)
- timm: 0.9.16
- RLDS 数据: /root/autodl-tmp/modified_libero_rlds/ (完整，4 suites)
- HDF5 数据: /root/autodl-tmp/LIBERO-datasets/（spatial/object/goal/10/90 全部有）
- 训练速度: ~4.3 it/s (transfer_v2), ~4.5 it/s (OFT baseline) on single RTX PRO 6000 (batch_size=2)
- symlink: /root/afford_invar/runs/ → /root/autodl-tmp/afford_invar/runs/
- 自动清理: nohup 后台守护进程每 5 分钟清理旧 checkpoint（保留最新 2 个），PID 127525

## 数据格式 (2026-05-19)

- OpenVLA-OFT 训练用 RLDS (tfrecord)
- 评估用 HDF5 demos
- HuggingFace 官方下载不可用（XET bridge），用 hf-mirror.com + ModelScope CDN
