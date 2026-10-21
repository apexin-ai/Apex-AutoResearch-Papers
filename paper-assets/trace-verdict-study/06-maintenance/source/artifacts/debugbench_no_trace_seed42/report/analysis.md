# DebugBench no_trace (seed42) 实验分析

## 实验概要

| 项目 | 值 |
|------|-----|
| 条件 | debugbench_no_trace（纯代码输入，无 trace） |
| 模型 | Qwen2.5-Coder-7B-Instruct + LoRA |
| 训练 | 3 epochs, train_loss=0.249, eval_loss=0.532 |
| 测试集 | n=426 |
| Checkpoint | `/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final` |

## 核心指标

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **96.71%** | [94.8%, 98.4%] |
| Majority baseline | 51.4% | [50.0%, 56.3%] |
| Lift over majority | +45.3pp | [+39.9pp, +47.4pp] |

### Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 1.000 | 0.936 | 0.967 |
| fail | 0.937 | 1.000 | 0.967 |

模型倾向于预测 fail（fail_recall=1.0, pass_recall=0.936），即宁可误判 pass 为 fail，也不遗漏真正的 bug。

## 条件对比

| Condition | Accuracy | Pass F1 | Fail F1 | Δ vs no_trace |
|-----------|----------|---------|---------|---------------|
| **no_trace** | 96.71% | 0.967 | 0.967 | — |
| **vota** | 99.77% | 0.998 | 0.998 | +3.06pp |

VOTA 条件（含 trace）相比 no_trace 提升 +3.06pp accuracy，差异在统计上显著（CI 不重叠：no_trace 上界 98.4% < vota 下界 99.3%）。

## 结论

**Status: SUCCESS** — baseline 建立成功。

- 实验正常完成，指标合理
- no_trace accuracy 96.7% 高于原始参考值 75.1%，但该参考值来自 zero-shot 设定；fine-tuned 7B 模型在代码判断任务上达到此水平符合预期
- 关键发现：即使 fine-tuned 模型仅凭代码已能达到 96.7%，trace 信息（VOTA 条件）仍能额外提升 +3.06pp 至近乎完美（99.8%）
- trace 的增益主要体现在 pass_recall 提升（0.936 → 0.995），即 trace 帮助模型正确识别"代码无 bug"的情况
