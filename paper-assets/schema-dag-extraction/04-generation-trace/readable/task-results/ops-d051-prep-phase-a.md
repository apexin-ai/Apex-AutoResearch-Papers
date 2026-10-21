# ops d051 prep phase a

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d051-prep-phase-a_20260516T222613_result.json`
- **Structured JSON:** [`371a0a1e091c17a07e36.json`](../../sessions/37/371a0a1e091c17a07e36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。汇总如下：

---

## 汇报

### 1. Few-NERD seed=42 count_66 状态：**已完成**

文件存在：`/root/schema-dag-extraction/artifacts/d051_fewnerd_n25_s42/results_count_66.jsonl`

tmux session `d051_batch2` 当前为空（所有内容已跑完或任务已退出）。

实际上 **Few-NERD seed=42 全部 6 个 count level 都已完成**：count_2, 6, 12, 22, 44, 66。

---

### 2. 脚本精确调用方式

```bash
python3 scripts/run_d051_count_curves_25.py --dataset fewnerd --n_batches 25 --seed 123
python3 scripts/run_d051_count_curves_25.py --dataset fewnerd --n_batches 25 --seed 456
```

可用参数：
- `--dataset`: `fewnerd` / `fewrel`
- `--n_batches`: 默认 25
- `--seed`: 默认 42
- `--counts`: 覆盖 count levels（逗号分隔，如 `6,12,22`）
- `--gpu_mem`: 默认 0.90
- `--output_dir`: 可选，不指定则自动生成
- GPU 通过脚本内 `os.environ["CUDA_VISIBLE_DEVICES"] = "0"` 硬编码

---

### 3. 输出文件自动区分 seed

输出目录格式：`artifacts/d051_{dataset}_n{n_batches}_s{seed}/`

例如：
- `d051_fewnerd_n25_s42/`
- `d051_fewrel_n25_s42/`
- `d051_fewrel_n25_s123/`（已存在，只跑了 count_16）

文件名中 **通过目录名区分 seed**，jsonl 文件本身命名为 `results_count_{N}.jsonl`。

---

### 4. FewRel seed=42 数据概要

| Count | Mean Accuracy | Std | Min | Max |
|-------|--------------|-----|-----|-----|
| 4 | 0.870 | 0.068 | 0.688 | 1.000 |
| 8 | 0.805 | 0.082 | 0.667 | 0.927 |
| 16 | 0.719 | 0.063 | 0.609 | 0.828 |
| 32 | 0.652 | 0.049 | 0.570 | 0.745 |
| 40 | 0.606 | 0.042 | 0.517 | 0.688 |
| 64 | 0.539 | 0.026 | 0.493 | 0.596 |
| 80 | 0.504 | 0.0002 | 0.503 | 0.504 |

### Few-NERD seed=42 数据概要（metric = recall）

| Count | Mean Recall | Std | Min | Max |
|-------|------------|-----|-----|-----|
| 2 | 0.527 | 0.190 | 0.094 | 0.826 |
| 6 | 0.390 | 0.115 | 0.178 | 0.604 |
| 12 | 0.306 | 0.102 | 0.059 | 0.443 |
| 22 | 0.268 | 0.103 | 0.113 | 0.444 |
| 44 | 0.301 | 0.112 | 0.108 | 0.546 |
| 66 | 0.407 | 0.002 | 0.402 | 0.410 |

---

### 5. 当前 batch2 进度

根据 `run_d051_batch2.sh` 脚本顺序：
- **Part A FewRel seed=42**: 完成（7/7 count levels）
- **Part A Few-NERD seed=42**: 完成（6/6 count levels）
- **Part B FewRel seed=123**: 进行中（仅 count_16 完成，后续中断/未继续）
- **Part B FewRel seed=456**: 未开始
- **Part B Few-NERD seed=123/456（key levels 6,12,22）**: 未开始

---

### 6. Figure 1a 位置

- `/root/schema-dag-extraction/figures/paper/fig_count_curves.pdf`
- `/root/schema-dag-extraction/figures/paper/fig_count_curves.png`
- 绘图脚本：`/root/schema-dag-extraction/figures/paper/fig_count_curves.py`

---
