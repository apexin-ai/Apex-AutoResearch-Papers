# prep g0 analysis compat

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_g0_analysis_compat_20260512T180752_result.json`
- **Structured JSON:** [`32ca3a7718ad72d7d735.json`](../../sessions/32/32ca3a7718ad72d7d735.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，以下是分析结果。

---

## 任务 1：analyze_g0.py 兼容性验证

### ✅ 兼容
| 项目 | analyze_g0.py 期望 | v5 实际 | 状态 |
|------|-------------------|---------|------|
| Checkpoint 命名 | `checkpoint-{step}` 子目录 | `checkpoint-152`, ..., `checkpoint-1373` | ✅ |
| tokens_per_step | 默认 65536 | 2048 × 8 × 4 = 65536 | ✅ |
| 模型名 | `EleutherAI/pythia-1b` | 同 | ✅ |
| 指标模块 | `metrics.compute_spectral_effective_rank`, `compute_perplexity` | 共用同一 metrics.py | ✅ |

### ⚠️ 不兼容项

**1. Holdout 路径不可用（需修复）**

analyze_g0.py 默认 `--holdout-path /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-103-raw-v1`，该路径是 HF datasets cache 目录（内含 `0.0.0/` 版本子目录），`load_dataset(path, split="test")` 传入本地路径时不会识别 cache 格式，会报错。

修复方式：运行时传 `--holdout-path wikitext`（让 HF 自动从缓存加载），或改代码为 `load_dataset("wikitext", "wikitext-103-raw-v1", split="test")`。

**2. final_model 不被发现（影响轻微）**

`discover_checkpoints()` 只扫描 `--checkpoint-dir` 下匹配 `checkpoint-*` 的目录。`final_model/` 位于 `G0/final_model/`（不在 `G0/training/` 下），不会被扫到。但 `checkpoint-1373` 就是 final step（max_steps=1373），权重等价，影响可忽略。

---

## 任务 2：G1 合成数据生成参数预检

### ✅ 正确

- **模型链接**：G1 从 `prev_model_dir = G0/final_model/` 初始化 — `/root/autodl-tmp/output/G0/final_model/` 已存在（2GB model.safetensors + tokenizer）✓
- **采样参数**：temperature=1.0, top_p=0.95, gen_max_new_tokens=2048 — 合理 ✓
- **生成函数**：`generate_synthetic_data()` 从 G0 final model 采样，输出到 `config.synthetic_data_path(0)` = `/root/autodl-tmp/output/G0/synthetic_data/` ✓
- **G1 训练数据**：`prepare_synthetic_data(config.synthetic_data_path(0))` 从 G0 合成数据加载 ✓

### ⚠️ 问题

**tokens_per_generation = 90M vs ROADMAP 100M**

- ROADMAP 写明 "3 代 × 100M tokens"
- `PilotConfig` 默认 `100_000_000`
- 但 `parse_args()` 默认 `90_000_000`，`launch_pilot_v5.sh` 也传 `90000000`
- 每代少 ~10M tokens、少 1 个 checkpoint（9 个 interval + 1 final，而非预期的 10+1）
- 不影响实验有效性，但与 ROADMAP 规格不一致

---

## 需修复项汇总

| 优先级 | 问题 | 修复 |
|--------|------|------|
| **高** | analyze_g0.py holdout 路径指向 HF cache 目录，load_dataset 会失败 | 运行时加 `--holdout-path wikitext`，或修改代码用 dataset name 加载 |
| **低** | tokens_per_generation 90M vs ROADMAP 100M 不一致 | 确认是否有意调整；如是，更新 ROADMAP；如否，下次运行改回 100M |

---
