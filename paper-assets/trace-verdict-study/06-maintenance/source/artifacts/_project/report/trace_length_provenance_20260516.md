# Trace Length Data Provenance + Paper Compile + Training Status
Date: 2026-05-16

## 1. Trace Length 256/512 数据溯源

**结论：两个数据点均可溯源，有完整的 checkpoint 和 eval_results.json。**

### 256tok → 78.82%
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/`
  - 训练步数：444 steps (checkpoint-3, 148, 296, 444 + final)
  - 框架：TRL 1.1.0 SFT, PyTorch 2.10.0+cu128
- **Eval 结果**: `full_trace_256tok/final/eval_results.json`
  - accuracy = 0.78824 → **78.82%** ✓
  - 95% CI: [76.4%, 81.0%]
  - n=1190, pass_f1=84.19%, fail_f1=67.94%
- **训练脚本**: `train/train_sft.py --max_trace_tokens 256`
  - `truncate_traces()` 函数截断 trace 到前 256 tokens

### 512tok → 80.42%
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_512tok/`
  - 训练步数：444 steps (checkpoint-148, 296, 444 + final)
  - 框架：TRL 1.1.0 SFT, PyTorch 2.10.0+cu128
- **Eval 结果**: `full_trace_512tok/final/eval_results.json`
  - accuracy = 0.80420 → **80.42%** ✓
  - 95% CI: [78.1%, 82.6%]
  - n=1190, pass_f1=86.17%, fail_f1=66.47%
- **训练脚本**: `train/train_sft.py --max_trace_tokens 512`

### 数字出现位置
| 文件 | 用途 |
|------|------|
| `figures/gen_fig_trace_length.py` | 图表生成（硬编码数值） |
| `analysis/fig_trace_ablation.py` | 分析脚本（从 eval_results.json 加载，硬编码作 fallback） |
| `analysis/figures/token_length_ablation_table.tex` | 生成的 LaTeX 表格 |
| `docs/paper/experiments.tex` | 论文正文 |
| `analysis/token_length_analysis.py` | 汇总分析脚本 |

### 缺失项
- **无 registry 记录**：256tok 和 512tok 没有像 1024tok 那样在 registry 中注册（1024tok 有 exp_id: full_trace_1024tok_seed42）
- **无 wandb run name 确认**：README.md 是 TRL 自动生成的模板，未记录具体 wandb run

---

## 2. 论文编译状态

**编译成功。** 
- 输出：`main.pdf`，18 页，322KB
- 警告：仅 Underfull hbox（断词排版微调），无错误
- tex 文件列表：main.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex, appendix.tex

---

## 3. ae_only 训练进度

| 实验 | 进度 | 速度 | 预计剩余 |
|------|------|------|----------|
| ae_only_seed123 | 241/444 (54%) | ~19s/it | ~64min |
| ae_only_seed456 | 211/444 (48%) | ~19s/it | ~74min |

### GPU 状态
| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| GPU 0 | 100% | 90,385 / 97,887 MiB (92%) |
| GPU 1 | 100% | 41,325 / 97,887 MiB (42%) |

两个 seed 实验均正常运行中，预计约 1~1.5 小时后完成。
