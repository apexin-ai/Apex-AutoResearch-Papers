# C4 Patch Locations — Tier Hierarchy / loop_only 引用清单

## 核心修改点（三模型数据齐后必须 patch）

| # | 文件:行 | 当前内容 | 需改为 |
|---|---------|---------|--------|
| 1 | introduction.tex:30 | "cross-model verification in progress", loop_only=86.1% | 去掉 in progress，改为三模型范围 77–86% |
| 2 | experiments.tex:25-27 | cross_model 表无 loop_only/ae_only | 添加 loop_only 行 |
| 3 | experiments.tex:37 | 脚注仅 Qwen seed 数据 | 追加 CL/DS loop_only seed |
| 4 | experiments.tex:66 | "restrict ae_only/loop_only to Qwen-7B" | **删除**，改为三模型已验证 |
| 5 | experiments.tex:67 | "direct Tier~2 verification...remains future work" | **删除**，报告三模型结果 |
| 6 | experiments.tex:83 | ablation 表仅 Qwen | 扩展为三模型或加列 |
| 7 | experiments.tex:95-97 | Tier~2 段 loop_only=86.05%, +10.92pp | 改为三模型范围 + 各 delta |
| 8 | discussion.tex:25-27 | "Tier~2 = 86.1%", "+10.50pp" | 改为三模型范围 |

## 可能需改（取决于 framing 决策）

| # | 文件:行 | 内容 | 备注 |
|---|---------|------|------|
| 9 | experiments.tex:4 | RQ2 措辞 | 可扩展为 "across models" |
| 10 | experiments.tex:71 | tab:ablation caption "on Qwen-2.5-7B" | 改为 "across three models" |
| 11 | conclusion.tex:3-5 | 无 C4 具体数据 | 可选加入三模型 Tier~2 |
| 12 | main.tex:43 | "other conditions use single seed" | 若 CL/DS loop_only 多 seed 则更新 |

## 无需修改

| # | 文件:行 | 内容 | 原因 |
|---|---------|------|------|
| 13 | method.tex:26 | loop_only 定义 | 纯定义无数据 |
| 14 | experiments.tex:170 | calibration mirrors tier | 仅引用概念 |
| 15 | appendix.tex:219 | Qwen seed 表 | 保留，另加 CL/DS 表 |
| 16 | appendix.tex:533-535 | calibration tier | 独立于 loop_only 跨模型 |
| 17 | appendix.tex:576-577 | error overlap | Qwen-only 分析可保留 |

## 当前三模型 loop_only 数据

| Model | Accuracy | vs no_trace | Delta |
|-------|----------|-------------|-------|
| Qwen-7B | 86.05% (3-seed mean) | 75.13% | +10.92pp |
| CodeLlama-13B | 77.06% | 76.47% | +0.59pp (not significant) |
| DeepSeek-6.7B | 81.26% | 73.36% | +7.90pp |
