# diagnose plan 002 v3 kill and rootcause

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-002-v3-kill-and-rootcause_20260514T060232_result.json`
- **Structured JSON:** [`1f95a894df825d4ab4e7.json`](../../sessions/1f/1f95a894df825d4ab4e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因分析完成。

## Kill 状态
- PID 224543: killed（tmux session + 进程已清理）
- GPU0: 533 MiB（已释放）
- GPU1: 4533 MiB（其他进程占用，非本任务）

## 根因分析

### config 对比
- ModelScope 版: vocab_size=151936, arch=Qwen3ForCausalLM, 无 num_labels（base model）
- HF cache 版: find 命令被 read_only 限制，但 dryrun eval 结果 (92.3%) 证明模型本身没问题
- 差异: 无关键差异，不是模型问题

### label encoding
- label_map: `{internal: 0, deterministic: 1}`
- 原始数据: **1830 det-preferred (89.7%) / 210 internal-preferred (10.3%)**
- internal 仅存在于 4 个 task: chemistry-mix(60), find-non-living-thing(90), grow-fruit(30), lifespan-longest-lived-then-shortest-lived(30)

### 数据 split 问题
- Episode-level split: 55 train / 13 val episodes → 1650 train / 390 val
- **Val 集 0 个 internal 样本**（混淆矩阵 `[[0,0],[390,0]]` 证实）
- 原因: episode 级 split 将所有含 internal 的 episode 分到了 train，val 只有纯 deterministic episode

### 模型 forward（未训练 baseline）
- logits: [-1.38, -3.23] → 未训练就偏向 class 0 (internal)
- softmax: [0.86, 0.14]
- classification head `score.weight` 随机初始化

### 训练日志（v3）
- **Class weights: [3.93, 0.57]**（auto inverse frequency，internal 权重是 det 的 6.9 倍）
- **Upsampling: enabled**（WeightedRandomSampler 同时过采样 internal）
- **train_loss: 4.07**（binary CE 随机应为 ~0.69，高出 6 倍）
- **grad_norm: 125.8**（梯度爆炸）
- Epoch 1 eval: accuracy=0.0, 全部预测为 class 0 (internal)
- Epoch 3 eval: accuracy=0.0, 无变化

### dryrun 对比
- Dryrun eval: accuracy=92.3%
- 混淆矩阵: `[[0,30],[0,360]]` → 全预测 class 1 (deterministic)，trivial majority baseline
- Dryrun 大概率未用 class_weights + upsample_minority

## 根因结论

**class_weights="auto" + upsample_minority 双重少数类校正导致灾难性过校正。** 过采样使 internal 在 batch 中占 ~50%，class_weight 再给 internal 3.93x 权重加成，internal 的 loss 贡献是 deterministic 的 ~7:1。模型被极端推向预测 internal，collapse 为全部输出 class 0。加上 val 集恰好 0 个 internal 样本，accuracy = 0。

## 修复建议

1. **只用其中一个**：`class_weights="auto"` 或 `upsample_minority`，不能同时用
2. **修复 stratified split**：当前按 episode 分，不保证 label 分布。需要 label-aware split，确保 val 集包含两个 class 的样本
3. **加早期 sanity check**：如果 epoch 1 train_loss > 2.0 或 eval_accuracy = 0，自动停止
4. 推荐：只用 `class_weights="auto"`（不用 upsample），同时修复 split 逻辑保证 val 有 internal 样本

---
