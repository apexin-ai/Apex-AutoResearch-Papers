# Plan 013: Downstream Curation PoC — 实验方案

> Claim 3 (Discussion): RF depth predictor 做数据 curation，filtered data finetune 的下游 perplexity 优于 unfiltered。

## 1. 数据来源

### 已有数据复用

使用 Pythia-1.4B nucleus (p=0.95) cell 的 d0–d3 数据（项目最成熟的 pipeline，78.2% 4-class acc）。

数据路径（服务器）:
```
/root/autodl-tmp/recursive_gen_depth_est/data/pythia_nucleus/
  depth_0.jsonl  # human seed (WikiText-103 train subset)
  depth_1.jsonl  # 1st generation
  depth_2.jsonl  # 2nd generation
  depth_3.jsonl  # 3rd generation
```

### 混合比例

**均匀混合**（worst-case 污染）: 每 depth 取 2500 samples，共 10,000 samples。

理由: 均匀比例最大化 curation 难度，且与 3×3 矩阵训练 RF 时的分布一致，避免 distribution shift。真实污染比例（如 70% d0 + 20% d1 + 8% d2 + 2% d3）可作为追加消融，但不是 PoC 的 primary setting。

### Token 预算

每 sample ≈ 512 tokens → 10k samples ≈ 5.1M tokens。Pythia-410M LoRA finetune 在 5–10M tokens 已足够观察 perplexity 差异（参考 Pythia 论文 training dynamics）。

## 2. 过滤策略

### RF 预测方式

使用已训练的 RF 模型（Pythia nucleus cell, 5-fold best）的 `predict_proba()`，获取 4-class 概率分布 `[P(d0), P(d1), P(d2), P(d3)]`。

### 三档过滤策略

| 策略 | 过滤规则 | 预期保留率 | 说明 |
|------|----------|-----------|------|
| **Strict** | `predicted_class == 0` | ~25% (~2500) | 仅保留 RF 判定为 human 的样本 |
| **Moderate** | `predicted_class ∈ {0, 1}` | ~50% (~5000) | 保留 d0+d1（低 depth 数据质量仍可接受） |
| **Soft** | `P(d0) + P(d1) > 0.6` | ~55–65% (~5500–6500) | 概率软过滤，允许高置信边界 case |

### 控制组

| 控制 | 描述 | 作用 |
|------|------|------|
| **Unfiltered** | 全部 10k samples | 基线：无 curation |
| **Oracle-strict** | Ground truth `depth == 0` | 上界：完美过滤器 |
| **Oracle-moderate** | Ground truth `depth ∈ {0, 1}` | 上界：完美低 depth 过滤 |
| **Random-strict** | 随机删至与 Strict 同量 | 排除 data volume 效应 |
| **Random-moderate** | 随机删至与 Moderate 同量 | 排除 data volume 效应 |

共 **8 个条件** (3 RF + 3 oracle/random + 2 基线去重 = 实际 8 个独立 finetune 配置)。

## 3. Finetune 设置

### 模型选择

**Pythia-410M** (`EleutherAI/pythia-410m`)

- 与数据生成器 (Pythia-1.4B) 不同规模，避免 self-evaluation circularity
- 410M 参数，LoRA finetune VRAM ≈ 3–4 GB，单卡可并行多 run
- Pythia 家族内保持架构一致性，减少混淆变量

### LoRA 配置

```python
LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["query_key_value"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
```

### 训练超参数

| 参数 | 值 | 理由 |
|------|-----|------|
| epochs | 3 | PoC 不需过长；3 epoch 足够收敛 |
| learning_rate | 2e-4 | LoRA 标准 LR |
| batch_size | 8 | 每 GPU |
| gradient_accumulation | 4 | effective batch = 32 |
| max_seq_len | 512 | 与生成时一致 |
| warmup_ratio | 0.05 | |
| weight_decay | 0.01 | |
| bf16 | True | RTX 6000 Pro 支持 |
| lr_scheduler | cosine | |

### 训练数据格式

复用现有 `scripts/lora_finetune.py` 的 `TextDataset`，输入为 JSONL（`{"text": "...", "depth": N, ...}`）。过滤后的数据仍为 JSONL 格式，仅行数减少。

## 4. 评估指标

### Primary: Validation Perplexity

- **评估集**: WikiText-103 test set（~245k tokens）
- 计算方式: sliding-window PPL（stride=512, max_length=1024）
- 使用 HuggingFace `evaluate` 库或手动实现

```python
# PPL 计算伪码
def eval_ppl(model, tokenizer, text, stride=512, max_len=1024):
    encodings = tokenizer(text, return_tensors="pt")
    nlls = []
    for i in range(0, encodings.input_ids.size(1), stride):
        begin = max(i + stride - max_len, 0)
        end = min(i + stride, encodings.input_ids.size(1))
        target_len = end - i
        input_ids = encodings.input_ids[:, begin:end].to(device)
        with torch.no_grad():
            outputs = model(input_ids, labels=input_ids)
        neg_log_likelihood = outputs.loss * target_len
        nlls.append(neg_log_likelihood)
    ppl = torch.exp(torch.stack(nlls).sum() / end)
    return ppl.item()
```

### Secondary (Optional)

- **LAMBADA** last-word accuracy（`lm-eval-harness --tasks lambada_openai`）
- 仅在 PPL 结果有意义时追加，不作为 PoC 必须项

### 统计要求

- **5 seeds** per condition: seeds = [42, 123, 456, 789, 1024]
- 报告: mean ± std
- 显著性: paired t-test（filtered vs unfiltered），报告 p-value
- Cohen's d effect size

## 5. GPU 预算

### 单 Run 估算

| 阶段 | GPU·h |
|------|-------|
| 数据加载 + tokenize | ~0.02 |
| Pythia-410M LoRA finetune (10k samples × 3 epochs) | ~0.3 |
| PPL 评估 (WikiText-103 test) | ~0.05 |
| **单 run 合计** | **~0.4** |

### 总预算

| 项目 | 计算 | GPU·h |
|------|------|-------|
| 8 conditions × 5 seeds | 40 runs × 0.4h | **16** |
| 数据准备 (RF predict + filter) | CPU only | 0 |
| Buffer (重跑/调试) | 20% | 3.2 |
| **总计** | | **~19 GPU·h** |

在 experiment_plan.yaml 预估的 15 GPU·h 附近，可控。

### 硬件分配

- **cuda:1** on gpu-6000pro-2（RTX 6000 Pro, 48GB VRAM）
- Pythia-410M LoRA ≈ 3–4 GB VRAM，可在单卡上串行跑（或两卡并行加速 2×）
- 建议: 40 runs 用 `nohup` 脚本串行执行，每 run 约 20 min

## 6. 预期时长

| 阶段 | 时长 | 说明 |
|------|------|------|
| **数据准备** | 1–2h | 提取特征 → RF predict → 按策略 filter → 写 JSONL |
| **模型下载** | 0.5h | Pythia-410M (~800MB) → `/root/autodl-tmp/models/` |
| **Finetune 全部 runs** | ~14h (单卡) / ~7h (双卡) | 40 runs × ~20min/run |
| **PPL 评估** | ~2h | 40 evals × ~3min/eval |
| **分析 + 出图** | 2h | 统计检验 + bar chart |
| **总计** | **~20h (单卡) / ~12h (双卡)** | |

### Deadline 可行性

EMNLP ARR May 25，剩余 10 天。实验 1 天可完成。但此实验为 Discussion future work (D012)，不阻塞提交。如果 May 16 启动，May 17 即可获得结果，有以下用途:

1. **最优**: 结果显著 → 写入 Discussion 作为 preliminary evidence，附 1 张 bar chart
2. **可接**: 结果不显著 → Discussion 保持原文（conceptual argument），数据留做 camera-ready 补充
3. **最差**: 实验出 bug → 不影响提交

## 7. 代码框架

### Step 1: 数据准备脚本 `scripts/curation_data_prep.py`

```python
"""构建 curation 实验数据：混合 d0-d3 + RF 过滤 + 控制组。"""
import json, os, random, pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]
DATA_DIR = "/root/autodl-tmp/recursive_gen_depth_est/data/pythia_nucleus"
FEATURES_DIR = "/root/autodl-tmp/recursive_gen_depth_est/results/pythia_nucleus"
OUTPUT_DIR = "/root/autodl-tmp/recursive_gen_depth_est/data/curation_poc"
SAMPLES_PER_DEPTH = 2500
SEEDS = [42, 123, 456, 789, 1024]

def load_features_and_texts():
    """加载特征矩阵和原始文本。"""
    features, labels, texts = [], [], []
    for depth in range(4):
        feat_path = f"{FEATURES_DIR}/depth_{depth}_features.jsonl"
        text_path = f"{DATA_DIR}/depth_{depth}.jsonl"
        # ... load and pair features with texts
    return np.array(features), np.array(labels), texts

def train_rf(X, y):
    """训练 RF 并返回 predict_proba。"""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_scaled, y)
    proba = rf.predict_proba(X_scaled)  # 注意: 这里用 train set predict 是故意的
    # 实际应用: RF 在 held-out 数据上 predict
    return rf, scaler, proba

def apply_filters(proba, labels, texts):
    """生成各策略的 filtered 数据。"""
    pred_class = proba.argmax(axis=1)
    conditions = {
        "unfiltered": np.ones(len(labels), dtype=bool),
        "rf_strict": pred_class == 0,
        "rf_moderate": np.isin(pred_class, [0, 1]),
        "rf_soft": (proba[:, 0] + proba[:, 1]) > 0.6,
        "oracle_strict": labels == 0,
        "oracle_moderate": np.isin(labels, [0, 1]),
    }
    # Random controls: match RF retention count
    n_strict = conditions["rf_strict"].sum()
    n_moderate = conditions["rf_moderate"].sum()
    idx_all = np.arange(len(labels))
    rng = np.random.RandomState(42)
    rand_strict_idx = rng.choice(idx_all, size=n_strict, replace=False)
    rand_moderate_idx = rng.choice(idx_all, size=n_moderate, replace=False)
    conditions["random_strict"] = np.isin(idx_all, rand_strict_idx)
    conditions["random_moderate"] = np.isin(idx_all, rand_moderate_idx)
    return conditions

def write_filtered_data(conditions, texts, labels):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name, mask in conditions.items():
        path = f"{OUTPUT_DIR}/{name}.jsonl"
        with open(path, "w") as f:
            for i in np.where(mask)[0]:
                json.dump({"text": texts[i], "depth": int(labels[i])}, f,
                          ensure_ascii=False)
                f.write("\n")
        print(f"{name}: {mask.sum()} samples -> {path}")
```

**关键设计决策**: RF 的 `predict_proba` 应在 **held-out fold** 上计算（cross-validated prediction），而非 train set 上直接 predict，否则过滤质量被高估。使用 `sklearn.model_selection.cross_val_predict(method='predict_proba')`。

### Step 2: Finetune + Eval 批量脚本 `scripts/run_curation_poc.sh`

```bash
#!/bin/bash
# Downstream curation PoC: finetune Pythia-410M on filtered data, eval PPL
set -e

BASE_MODEL="EleutherAI/pythia-410m"
MODEL_CACHE="/root/autodl-tmp/models/pythia-410m"
DATA_DIR="/root/autodl-tmp/recursive_gen_depth_est/data/curation_poc"
RESULT_DIR="/root/autodl-tmp/recursive_gen_depth_est/results/curation_poc"
GPU=1  # cuda:1

CONDITIONS="unfiltered rf_strict rf_moderate rf_soft oracle_strict oracle_moderate random_strict random_moderate"
SEEDS="42 123 456 789 1024"

for cond in $CONDITIONS; do
    for seed in $SEEDS; do
        OUT="${RESULT_DIR}/${cond}/seed_${seed}"
        echo "=== ${cond} seed=${seed} ==="
        
        # Finetune
        python scripts/lora_finetune.py \
            --input_data "${DATA_DIR}/${cond}.jsonl" \
            --output_dir "${OUT}/adapter" \
            --model_name "$BASE_MODEL" \
            --model_cache "$MODEL_CACHE" \
            --epochs 3 \
            --lr 2e-4 \
            --batch_size 8 \
            --gradient_accumulation 4 \
            --max_seq_len 512 \
            --seed $seed \
            --gpu $GPU
        
        # Eval PPL
        python scripts/eval_ppl.py \
            --adapter_dir "${OUT}/adapter" \
            --model_name "$BASE_MODEL" \
            --model_cache "$MODEL_CACHE" \
            --eval_data "wikitext-103-test" \
            --output "${OUT}/ppl_result.json" \
            --gpu $GPU
    done
done
```

### Step 3: 分析脚本 `scripts/analyze_curation.py`

```python
"""汇总 curation PoC 结果，生成统计和图表。"""
import json, os, glob
import numpy as np
from scipy import stats

RESULT_DIR = "/root/autodl-tmp/recursive_gen_depth_est/results/curation_poc"
CONDITIONS = ["unfiltered", "rf_strict", "rf_moderate", "rf_soft",
              "oracle_strict", "oracle_moderate", "random_strict", "random_moderate"]

def collect_results():
    results = {}
    for cond in CONDITIONS:
        ppls = []
        for seed_dir in sorted(glob.glob(f"{RESULT_DIR}/{cond}/seed_*")):
            with open(f"{seed_dir}/ppl_result.json") as f:
                ppls.append(json.load(f)["perplexity"])
        results[cond] = np.array(ppls)
    return results

def statistical_tests(results):
    baseline = results["unfiltered"]
    for cond in CONDITIONS:
        if cond == "unfiltered":
            continue
        t_stat, p_val = stats.ttest_rel(baseline, results[cond])
        d = (baseline.mean() - results[cond].mean()) / baseline.std()
        print(f"{cond}: PPL={results[cond].mean():.2f}±{results[cond].std():.2f} "
              f"| Δ={baseline.mean()-results[cond].mean():.2f} "
              f"| p={p_val:.4f} | d={d:.2f}")
```

### Step 4: 出图（bar chart for Discussion）

```python
"""PPL bar chart: conditions on x-axis, PPL on y-axis, error bars = std."""
import matplotlib.pyplot as plt

def plot_curation_results(results):
    fig, ax = plt.subplots(figsize=(10, 5))
    names = ["Unfiltered", "RF-Strict", "RF-Moderate", "RF-Soft",
             "Oracle-Strict", "Oracle-Moderate", "Rand-Strict", "Rand-Moderate"]
    means = [results[c].mean() for c in CONDITIONS]
    stds = [results[c].std() for c in CONDITIONS]
    colors = ["#888"] + ["#2196F3"]*3 + ["#4CAF50"]*2 + ["#FF9800"]*2
    
    bars = ax.bar(names, means, yerr=stds, capsize=4, color=colors, edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Perplexity (WikiText-103 test)")
    ax.set_title("Downstream Impact of RF-based Depth Curation")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig("figures/curation_poc_ppl.pdf", dpi=300)
```

## 8. 预期结果与假设

### Primary Hypothesis

RF-filtered data (especially `rf_strict` 和 `rf_moderate`) finetune 的 PPL **低于** unfiltered baseline，且差异与 oracle 控制组方向一致。

### 预期效果量

| 条件 | 预期 PPL 排名 | 理由 |
|------|-------------|------|
| Oracle-strict | 最低 (最好) | 仅用 human 数据训练 |
| RF-strict | 第 2–3 | RF 78% acc → ~78% precision on d0 |
| Oracle-moderate | 第 3–4 | d1 数据质量接近 d0 |
| RF-moderate | 第 4–5 | 加入 d1 增加数据量但引入少量噪声 |
| RF-soft | 第 5–6 | 软阈值，介于 strict 和 unfiltered 之间 |
| Random-* | 接近 unfiltered | 无信息过滤 |
| Unfiltered | 最高 (最差) | 含 d2/d3 低质量数据 |

### 若 Hypothesis 不成立

可能原因:
1. **d0–d3 质量差异太小** → depth degradation 在 finetune 级别不可观测（正常，depth 信号主要在 distributional 层面）
2. **数据量效应抵消质量效应** → Strict 过滤删太多数据，PPL 反升
3. **Pythia-410M 太小** → 无法区分 training data quality

任何结果都有论文价值:
- 正向结果 → Discussion 升级为 preliminary evidence
- 无差异 → honest reporting，"depth signal is distributional, not downstream-performative"
- 数据量 vs 质量 tradeoff → 本身是 finding

## 9. 需补充的代码

| 文件 | 状态 | 说明 |
|------|------|------|
| `scripts/curation_data_prep.py` | 新建 | 数据混合 + RF predict + filter |
| `scripts/eval_ppl.py` | 新建 | WikiText-103 PPL 评估 |
| `scripts/run_curation_poc.sh` | 新建 | 批量 finetune + eval 驱动脚本 |
| `scripts/analyze_curation.py` | 新建 | 结果汇总 + 统计 + 出图 |
| `scripts/lora_finetune.py` | 已有 | 需添加 `--warmup_ratio` 和 `--weight_decay` 参数 |

## 10. Checklist

- [ ] 确认服务器 d0–d3 数据路径和 features 文件路径
- [ ] 确认 RF 模型是否有保存的 pickle（或需重新训练）
- [ ] 下载 Pythia-410M 到服务器
- [ ] 下载 WikiText-103 test set
- [ ] 编写并测试 `curation_data_prep.py`
- [ ] 编写并测试 `eval_ppl.py`
- [ ] 用 1 个 condition × 1 seed 做 dry run 验证 pipeline
- [ ] 启动全量 40 runs
- [ ] 汇总结果 + 统计检验
- [ ] 生成图表

[APPROVAL NEEDED]
