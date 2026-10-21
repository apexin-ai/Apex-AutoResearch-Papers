# code control b preparation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_control-b-preparation_20260515T132206_result.json`
- **Structured JSON:** [`2c0d6c8160d77697fcad.json`](../../sessions/2c/2c0d6c8160d77697fcad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是分析结果。

---

## Control B（Label Permutation）验证报告

### 脚本状态：就绪

`train_probes.py` 内置 `--shuffle_labels` 参数（L63），实现正确：

```python
# L467-468
if shuffle_labels:
    y_tr = y_tr[torch.randperm(len(y_tr))]
    y_val = y_val[torch.randperm(len(y_val))]
```

逻辑：特征对 `(X_tr, X_val)` 不变，仅对距离标签做随机排列。符合标准 permutation test null control。

### 命名歧义（需注意）

代码中有**两个**不同的 control flag：

| Flag | 代码注释 | 实际行为 |
|------|---------|---------|
| `--shuffle_cross_trajectory` | "Control B" | 跨轨迹配对（改变特征对结构） |
| `--shuffle_labels` | "Negative control" | 标签置换（保留特征对，shuffle 标签） |

任务定义的 Control B 是 **label permutation**，应使用 `--shuffle_labels`。现有 `dinov2_shuffle/` 目录（ρ=0.650, `cross_trajectory: true`）是跨轨迹 control，不是 label permutation。

### 输出路径

`save_results` 写入 `output_dir/temporal_distance/`。**必须用不同的 `--output_dir`**，否则会覆盖正常 probe 结果。

### 完整运行命令

```bash
cd /root/vla-ssd
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained_label_perm/ \
  --probe_type temporal_distance \
  --shuffle_labels
```

### analyze_results.py 兼容性

`analyze_results.py` 不专门处理 Control B。它通过 `--results_dirs name:path` 接受任意数量的结果目录进行对比。Control B 结果只需作为额外条目传入：

```bash
python scripts/analyze_results.py \
  --results_dirs trained:results/trained/,label_perm:results/trained_label_perm/,... \
  --output_dir results/analysis/
```

verdict 逻辑（`compute_judgment`）不依赖 Control B——它只用 trained/untrained/dinov2 做判断。Control B 结果会在对比表和图中展示，但不影响 PASS/FAIL 判定。

### Features 确认

Trained features 存在（10 个 task .h5 文件），33 层 × 4096 维。

### 预估运行时间

33 层全跑，每层约 30 秒（基于 dinov2 单层 ~11 epoch 的训练时间推算），总计约 **15-20 分钟**。

### 无需修复的问题

脚本可直接运行，无需代码修改。

---
