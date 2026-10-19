# code anonymous repo prep

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_anonymous-repo-prep_20260525T083831_result.json`
- **Structured JSON:** [`833d263128abc672e6c9.json`](../../sessions/83/833d263128abc672e6c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完成报告

### 1. 完整文件列表

```
anonymous_repo/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── scripts/
│   ├── run_pipeline.sh
│   └── run_probes.sh
└── src/
    ├── bootstrap_asymmetry.py
    ├── bootstrap_mlp_delta.py
    ├── bootstrap_probe.py
    ├── collect_activations.py
    ├── comet_tertile_ablation.py
    ├── compute_auroc.py
    ├── compute_cka.py
    ├── cross_task_transfer.py
    ├── cross_task_transfer_bootstrap.py
    ├── prepare_xnli.py
    ├── probe_cosine_similarity.py
    ├── random_labels_control.py
    ├── steering_experiment.py
    ├── supplement_sampling.py
    ├── token_overlap_analysis.py
    ├── tost_equivalence.py
    ├── tost_power_analysis.py
    ├── train_mlp_probe.py
    ├── train_probe.py
    ├── translate.py
    ├── validate_translation.py
    └── verify_parametric_knowledge.py
```

**28 files** total (22 Python scripts + 2 shell scripts + 4 infrastructure files)

### 2. README.md 概要

覆盖：项目描述（cross-lingual knowledge conflict mechanistic interpretability）、repo 结构表、环境配置、数据获取（ConflictQA + XNLI + 3 models）、完整复现流程（step-by-step + one-command pipeline）、关键实验对照表、匿名 BibTeX。

### 3. requirements.txt

```
torch>=2.0, transformers>=4.40, datasets>=2.0, accelerate>=0.20,
scikit-learn>=1.3, scipy>=1.10, numpy>=1.24, pandas>=2.0,
matplotlib>=3.7, unbabel-comet>=2.2
```

### 4. 匿名化检查结果

| 检查项 | 结果 |
|--------|------|
| `/root/` 绝对路径 | **0 处** |
| `hf-mirror.com` URL | **0 处** |
| `autodl` 引用 | **0 处** |
| 个人邮箱/姓名 | **0 处** |
| 硬编码模型路径字典 | **0 处**（全部改为 `--models` JSON argparse） |

全部通过。

### 5. 代码总行数

- **Python 源文件**: 3,605 行
- **全部文件（含 README/scripts/config）**: 3,922 行

### 6. Git 状态

- 仓库已初始化：`user.name="Anonymous"`, `user.email="anonymous@anonymous.invalid"`
- 分支：`main`
- 初始 commit：`53821b9 Initial commit: anonymous code for EMNLP 2026 submission`

### 7. 排除的死代码文件（10 个）

`comet_tertile_ablation_fix.py`, `prepare_gemma_data.py`, `bootstrap_mlp_delta_llama_fix.py`, `bootstrap_xnli_gemma_parallel.py`, `token_overlap.py`, `token_overlap_en_de.py`, `aggregate_layerwise.py`, `extract_layerwise.py`, `integrate_de_results.py`, `train_probe_fast.py`

### 8. 合并的文件

`translate_to_zh.py` + `translate_to_de.py` → `translate.py`（`--target_lang` 参数）

---
