# code d37b mech interp analysis

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d37b_mech_interp_analysis_20260521T065824_result.json`
- **Structured JSON:** [`fa5e05eee172859f9476.json`](../../sessions/fa/fa5e05eee172859f9476.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D37-B 完成。

## 结果

### Step 1: 模型架构
- **GPT-NeoX** (Pythia-410M), 24 layers, 16 heads, hidden=1024, vocab=50304

### Step 2: 可用 checkpoints
大多数实验只保留最后 2 代 checkpoint (gen_9/gen_10)。α=0.00 和 α=1.00 的 alpha_sweep 实验无 checkpoint（只有 metrics JSON）。

alpha_sweep 中 s42_fp32 有 checkpoint 的实验：a005, a010, a025, a030, a035, a040, a045, a046, a048, a050, a052, a055, a060, a065, a070, a075（均 gen_9/gen_10）。

### Step 3: 脚本
`/root/autodl-tmp/distrib_canary_collapse/mech_interp_analysis.py`

5 个指标：
1. **Attention entropy per layer** — 每层每 head 的 attention 分布熵
2. **Head diversity** — head 间 cosine similarity（趋同度）
3. **Effective rank** — 最后一层 hidden states 的有效秩
4. **Logit confidence** — top-1 概率均值
5. **Activation norm** — 每层 hidden state L2 norm

### Step 4: Dry-run 结果 (a050_s42_fp32, CPU, 5 samples)

| 指标 | Gen 9 | Gen 10 | 趋势 |
|------|-------|--------|------|
| Logit confidence | 0.4573 | 0.4704 | ↑ 更自信 |
| Effective rank | 355.1 | 351.7 | ↓ 表征塌缩 |
| Mean attn entropy | 1.0230 | 1.0051 | ↓ attention 更集中 |
| Head diversity (cos sim) | 0.7040 | 0.7057 | → 基本不变 |
| Activation norm | 48.56 | 49.52 | ↑ 激活增长 |

即使只有 2 代 + 5 samples，趋势已与 collapse 预期一致：confidence↑, effective rank↓, entropy↓。

### Step 5: GPU 预估 & 建议

**时间/显存**：
- ~15-20s/checkpoint（GPU, 50 samples）→ 每实验 ~40s
- 峰值显存 ~3GB（model 1.6GB + attention weights ~400MB + buffer）

**建议运行的实验**（cross-alpha 对比，均 s42_fp32, gen_9/gen_10）：

| 实验 | α值 | 角色 |
|------|-----|------|
| a005_s42_fp32_v3_d080 | 0.05 | 近 baseline（最低可用 α） |
| a025_s42_fp32 | 0.25 | 低 collapse |
| a050_s42_fp32 | 0.50 | boundary |
| a075_s42_fp32 | 0.75 | 强 collapse |
| padding_robustness/a100_s42_fp32 | 1.00 | full collapse（alpha_sweep 无 ckpt，此处有） |

GPU 运行命令示例：
```bash
python mech_interp_analysis.py \
    --experiment_dir results/alpha_sweep/a050_s42_fp32 \
    --eval_data data/wikitext103_5k/eval \
    --num_samples 50 --device cuda:0
```

5 个实验总计 ~4 分钟 GPU 时间。

---
