# recon 340m eval prep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_340m-eval-prep_20260521T222040_result.json`
- **Structured JSON:** [`704891a28685204c645a.json`](../../sessions/70/704891a28685204c645a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 340M 模型列表

`/root/autodl-tmp/models/` 下共 **16 个**模型目录（15 hybrid/pure + 1 Transformer baseline）：

**GatedDeltaNet (5):**
- `340M-20B-GatedDeltaNet-pure-baseline`
- `340M-20B-GatedDeltaNet-hybrid-3-1`
- `340M-20B-GatedDeltaNet-hybrid-6-1`
- `340M-20B-GatedDeltaNet-hybrid-12-1`
- `340M-20B-GatedDeltaNet-New-hybrid-24-1` （注意 "New" 前缀）

**RetNet (5):**
- `340M-20B-RetNet-pure`
- `340M-20B-RetNet-hybrid-3-1`
- `340M-20B-RetNet-hybrid-6-1`
- `340M-20B-RetNet-hybrid-12-1`
- `340M-20B-RetNet-hybrid-24-1`

**HGRN2 (5):**
- `340M-20B-HGRN2-pure-baseline`
- `340M-20B-HGRN2-hybrid-3-1`
- `340M-20B-HGRN2-hybrid-6-1`
- `340M-20B-HGRN2-hybrid-12-1`
- `340M-20B-HGRN2-hybrid-24-1`

**Transformer baseline (1):**
- `transformer_340M_baseline`

## Eval 脚本参数

根目录的 `/root/entrainment_gated_ft/run_lmeval_clean.py`（exp007 实际使用的版本）：

| 参数 | 说明 |
|------|------|
| `--model_path` | 必填，模型路径 |
| `--tasks` | 逗号分隔任务名，默认 `lambada_openai,hellaswag,winogrande,piqa,arc_easy,arc_challenge,mmlu` |
| `--output_dir` | 输出目录，默认 `/root/entrainment_gated_ft/lm_eval_clean` |
| `--batch_size` | 默认 `auto` |
| `--device` | 默认 `cuda:0` |
| `--log_samples` | **支持**，`store_true` 标志。启用后将每个 task 的 samples 写入 `{output_dir}/samples/{task_name}.jsonl` |

注意：`scripts/run_lmeval_clean.py` 是旧版本，**没有** `--log_samples`、`--device` 参数，也没注册 HGRN2。批处理脚本使用的是根目录版本。

## 已有 log_samples 输出

`/root/entrainment_gated_ft/lm_eval_clean/exp007/` 结构：
```
exp007/
├── 340m/
│   ├── GDN-pure/          (含 .json + samples/lambada_openai.jsonl)
│   ├── GDN-h3-1/
│   ├── GDN-h6-1/
│   ├── GDN-h12-1/
│   ├── GDN-h24-1/
│   ├── RetNet-pure/
│   ├── RetNet-h3-1/ ~ h24-1/
│   ├── HGRN2-pure/
│   ├── HGRN2-h3-1/ ~ h24-1/
│   └── Transformer/
└── 1.3b/
```

每个子目录包含 `{model_name}.json`（汇总结果）和 `samples/lambada_openai.jsonl`（逐样本 logprob）。**16 个 340M 模型全部已有 log_samples 产出。**

旧的 `lm_eval_clean/340m/` 目录包含之前非 log_samples 的 eval 结果（GDN 为 .json，其余为子目录）。

## 参考脚本

**`run_exp007_logsamples.sh`**（exp007 批处理，实际使用的格式）：
- 调用 `run_lmeval_clean.py`（根目录版本）
- 参数：`--model_path ... --tasks lambada_openai --log_samples --output_dir ...`
- 包含跳过已完成模型的逻辑（检查 samples 目录是否已有 .jsonl）
- 覆盖 340M (16) + 1.3B (11) 模型

**`run_all_340m_eval.sh`**（旧版多 task eval，无 log_samples）：
- 调用 `scripts/run_lmeval_clean.py`（旧版本）
- tasks: `lambada_openai,hellaswag,winogrande,arc_easy,arc_challenge,mmlu`
- 只有 10 个模型（RetNet + HGRN2），无 GDN

## 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| `/root/autodl-tmp` | 250G | 120G | **131G** | 48% |
| `/autodl-pub/data` | 20T | 1.6T | 18T | 9% |

磁盘空间充裕。

---
