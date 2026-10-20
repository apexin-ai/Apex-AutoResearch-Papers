# analysis ood cross dataset feasibility

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ood_cross_dataset_feasibility_20260515T113259_result.json`
- **Structured JSON:** [`8a68fdf2d82ad7bbd52f.json`](../../sessions/8a/8a68fdf2d82ad7bbd52f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## Cross-dataset OOD 可行性评估

### 1. 资源现状

**模型（均存在）：**
- SciERC Qwen: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2` (也有 v2-ckpt400)
- CoNLL Qwen: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged`
- 另有 LLaMA 版本可做补充

**数据（均存在）：**
- SciERC: `data/scierc/`
- CoNLL: `data/conll2003/`

**已有 cross-dataset 结果：** `loo_sj_cross_dataset/results.json` 是 LOO-SJ 稳定性分析，不是 cross-dataset 推理。无已有 OOD 推理结果。

### 2. 代码兼容性分析

**核心发现：代码零修改即可运行 cross-dataset。**

`run_mvp_pilot.py` 的 `--model_path` 和 `--dataset` 是完全独立的参数：
- `--dataset` 决定加载哪个数据集 + 自动选择对应的 schema hint
- `--model_path` 只是指定 vLLM 加载的模型权重
- Schema hint 嵌入到 prompt 中告诉模型要抽什么类型

所以 SciERC 模型 + `--dataset conll2003` 会在 prompt 里注入 `"Entity types: PER, ORG, LOC, MISC"`，模型虽然训练时只见过 SciERC 类型，但由于 Qwen3-8B 的指令跟随能力，它可能仍能按 prompt 指示抽取 CoNLL 类型——这正是 OOD 测试的有趣之处。

### 3. 两个方案评估

| | 方案 1: SciERC → CoNLL | 方案 2: CoNLL → SciERC |
|---|---|---|
| **可行性** | ✅ 可直接运行 | ✅ 可直接运行 |
| **修改量** | 0 行 | 0 行 |
| **预计运行时间** | ~15-20 min（CoNLL test 3.5k 句，N=16） | ~5-8 min（SciERC test 529 句，N=16） |
| **预期 F1** | 低但非零（4 个粗粒度 NER 类型，模型可能靠指令跟随完成） | 更低（6 个细粒度科学类型，CoNLL 模型不熟悉学术文本） |
| **SCS 信号** | 更有说服力：大 test set (2756 inst) 统计功效高 | 小 test set (529 inst) 统计功效较弱 |
| **学术意义** | science→news: 大 domain shift + schema shift | news→science: 同样大 shift，但样本少 |

### 4. 推荐

**两个都做**，优先方案 1。理由：
1. 代码零修改，两次推理总共 ~25 min
2. 双向 cross-dataset 形成对称对比，论文更有说服力
3. 关键论点不是 F1 绝对值，而是 **SCS 信号（ρ）在 OOD 下是否仍显著为正**——即使 F1=0.2，只要 ρ(SJ, F1) > 0.2 且 p < 0.05，就能说明 SCS 的泛化能力

### 5. 运行命令草案

```bash
cd /root/autodl-tmp/struct_self_consist_ie/code

# 方案 1: SciERC model → CoNLL test (优先)
python run_mvp_pilot.py \
  --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2 \
  --dataset conll2003 \
  --data_dir /root/autodl-tmp/struct_self_consist_ie/data/conll2003 \
  --subtask ner \
  --n_samples 16 \
  --temperature 1.0 \
  --max_tokens 1024 \
  --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_ood_scierc2conll \
  --seed 42

# 方案 2: CoNLL model → SciERC test
python run_mvp_pilot.py \
  --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged \
  --dataset scierc \
  --data_dir /root/autodl-tmp/struct_self_consist_ie/data/scierc \
  --subtask ner \
  --n_samples 16 \
  --temperature 1.0 \
  --max_tokens 1024 \
  --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_ood_conll2scierc \
  --seed 42
```

可以串行跑（方案 1 完了接方案 2），也可以分两个 nohup 但注意 GPU 显存——Qwen3-8B 单模型占 ~16GB，5090 如果只有一张卡就必须串行。

---
