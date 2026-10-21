# Llama-3.1-8B-Instruct 跨模型验证实验设计

> 目标：在 Llama-3.1-8B-Instruct 上复现 Qwen2.5-7B 的三个 negative findings（NF1/NF2/NF3），证明 ThreadGate 的失败是结构性问题而非 Qwen 特有。这是 Route B negative result paper 从 Findings 升级 main track 的关键加分项。

---

## Phase 1: GAR 衰减诊断

**目标**: 确认 Llama-3.1-8B-Instruct 存在与 Qwen 类似的 GAR 衰减现象。

**方法**: 复用 Phase 1 GAR 诊断脚本，切换 `--model` 参数。

```bash
python eval_phase1_gar.py \
  --model /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ \
  --dataset ultrachat \
  --turns 1,3,5,7 \
  --metric gar
```

**参考基线**: Dongre et al. 在 Llama-3.1-8B 上报告 27-48% GAR 衰减（随 turn 数增加）。

**GPU 时间**: ~30min（inference only，无训练）

**预期结果**: 观察到类似 Qwen 的 70%+ raw GAR drop（随 turn 深度递增）。若衰减幅度与 Qwen 在同一数量级，即可确认跨模型一致性。

---

## Phase 2: ThreadGate v7 训练

**目标**: 在 Llama 上训练 ThreadGate，复现三个 negative findings。

**训练配置**（与 Qwen v7 完全一致，保证可比性）:

| 参数 | 值 |
|---|---|
| Loss | MSE + gate_div |
| λ_gar | 1.0 |
| λ_div | 1.0 |
| Epochs | 3 |
| 数据集 | ultrachat_8k |
| LoRA rank | 16 |
| Learning rate | 2e-4 |
| Batch size | 4 (grad_accum=8) |

**模型适配**（threadgate.py 自动检测）:

| 参数 | Qwen2.5-7B | Llama-3.1-8B |
|---|---|---|
| hidden_dim | 3584 | 4096 |
| num_layers | 28 | 32 |
| vocab_size | 152064 | 128256 |

**训练命令**:

```bash
python train_phase2.py \
  --model /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ \
  --dataset ultrachat_8k \
  --loss mse_gate_div \
  --lambda_gar 1.0 --lambda_div 1.0 \
  --epochs 3 \
  --lora_rank 16 \
  --lr 2e-4 \
  --batch_size 4 --grad_accum 8 \
  --seed 42 \
  --output_dir artifacts/phase2_tg_llama_v7
```

**GPU 时间**: ~6-7h（Llama 参数量略大于 Qwen：8B vs 7B，且 hidden_dim 更大）

**预期 negative findings**:

- **NF1' (turn conditioning 反向)**: gate 在 later turns 反而更开放（与设计意图相反），与 Qwen 上观察到的行为一致
- **NF2' (training-inference GAR gap)**: training loss 正常下降但 inference GAR 无改善或恶化，gap 量级预期 ~30x（与 Qwen 一致）
- **NF3' (gate attenuation 不足)**: gate 值集中在 0.4-0.6 区间，未形成有效的 0/1 二值化，turn-aware 调节能力不足

---

## Phase 3: Eval

### 最小方案（推荐，时间约束下优先）

仅做 Base vs ThreadGate 对比：

```bash
# Base model eval
python eval_phase2_gar.py \
  --model /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ \
  --mode base \
  --output artifacts/eval_llama_base.json

# ThreadGate eval
python eval_phase2_gar.py \
  --model /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ \
  --mode threadgate \
  --checkpoint artifacts/phase2_tg_llama_v7/best.pt \
  --output artifacts/eval_llama_tg.json
```

- 2 个 eval，~30min 总计
- 足够证明 NF2'（GAR gap）和论文核心 claim

### 扩展方案（可选）

四路消融：Base + TG + UG + LoRA-only

| 条件 | 额外训练时间 | Eval 时间 |
|---|---|---|
| Base | 0 | ~15min |
| ThreadGate (TG) | 0（Phase 2 已训练） | ~15min |
| Uniform Gate (UG) | ~6h | ~15min |
| LoRA-only | ~6h | ~15min |

扩展方案额外需要 ~12h 训练时间。仅在时间充裕时考虑。

---

## Phase 4: 磁盘规划

**当前状态**:

| 项目 | 大小 |
|---|---|
| 磁盘总量 | 30GB |
| 已用（含 Qwen cache） | ~15GB |
| 可用 | ~15GB |
| Llama 权重需求 | ~16GB |

Llama 权重 (16GB) 无法与 Qwen cache (15GB) 共存。

**串行方案**:

1. 完成所有 Qwen 实验（四路 eval 全部跑完）
2. 确认所有 Qwen 结果已保存（checkpoint + eval json + wandb logs）
3. 删除 Qwen 模型 cache（**需 Director 确认**）：
   ```bash
   rm -rf /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct/  # ~15GB
   ```
4. 下载 Llama 权重：
   ```bash
   # ModelScope 已验证可用，无需 HF token
   # tokenizer 已存在于 /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/
   # 需下载完整权重（model*.safetensors）
   python -c "from modelscope import snapshot_download; snapshot_download('LLM-Research/Meta-Llama-3.1-8B-Instruct')"
   ```
5. 下载后可用空间：~14GB（足够训练 checkpoint 和 eval 输出）

**不删除的文件**（必须保留）:

- `artifacts/phase2_tg_s42_v7/` — Qwen ThreadGate 训练 checkpoint
- `artifacts/eval_*.json` — 所有 eval 结果
- `artifacts/src/` — 源代码
- 训练日志和 wandb 数据

---

## 时间表

| 时间 | 任务 | 耗时 | 依赖 |
|---|---|---|---|
| D+0 | Qwen 四路 eval 完成（LoRA-only 训练后） | ~1.5h | 当前进行中 |
| D+1 | 确认 Qwen 结果完整，清理 Qwen cache | ~10min | Director 确认 |
| D+1 | 下载 Llama 完整权重 | ~30-60min | 网络带宽 |
| D+1 | Phase 1: GAR 衰减诊断 | ~30min | 权重就绪 |
| D+1 ~ D+2 | Phase 2: ThreadGate v7 训练 | ~6-7h | Phase 1 完成 |
| D+2 | Phase 3: Eval（最小方案） | ~30min | Phase 2 完成 |
| **总计** | | **~9-10h GPU 时间** | |

---

## 风险评估

| 风险 | 概率 | 影响 | 应对 |
|---|---|---|---|
| Llama 上 GAR 不衰减 | 极低（Dongre et al. 已验证） | 高：跨模型 claim 不成立 | 调整 story 为 model-specific analysis |
| Llama 上 TG 意外 work | 极低 | 高：negative finding 不成立 | 转为正向叙事，分析为何 Llama 有效 |
| 磁盘不够 | 中等 | 中：阻塞训练 | 激进清理旧 checkpoint，只保留 best.pt |
| Llama 下载失败 | 低 | 低：延迟 | 切换 HF mirror 或手动分片下载 |
| 训练 OOM | 低（Qwen 已跑通，Llama 略大） | 低 | 减小 batch_size 或启用 gradient checkpointing |

---

## 论文价值

跨模型验证成功后，论文可新增：

- **Table**: Llama vs Qwen negative findings 对比（NF1/NF2/NF3 在两个模型上的具体数值）
- **Claim 升级**: "ThreadGate's failure is structural, not model-specific" — 从单模型观察升级为跨架构结论
- **审稿人预期回应**: 预先封堵 "maybe it only fails on Qwen" 的质疑
- 预估可将 Overall Assessment 从 3.0 (Findings) 提升 0.3-0.5 分
