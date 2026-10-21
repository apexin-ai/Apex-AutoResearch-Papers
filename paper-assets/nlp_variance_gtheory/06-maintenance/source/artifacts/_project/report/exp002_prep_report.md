exp-002 Multi-Benchmark Infrastructure Prep Report

## 数据
- GSM8K: 1,319 items, downloaded
- ARC-Challenge: 1,172 items, downloaded  
- HellaSwag: 10,042 items, downloaded
Location: /root/autodl-tmp/.hf_cache/hub/

## 200-item Samples (data/ directory)
- GSM8K: easy/medium/hard/very_hard 各50
- ARC: 按选项数分层 (4-choice:193, 3-choice:4, 5-choice:3)
- HellaSwag: 按activity_label分层 (192类别)

## 代码适配清单 (~8.5天)
- prompt_templates.py: GSM8K生成式模板 + 变长选项 (~2天)
- run_experiment.py: benchmark路由 + GSM8K数值答案提取 + 评分逻辑 (~3天)
- vllm_runner.py: max_tokens可配置 (~0.5天)
- generate_design.py: benchmark因子 + 精度/温度级数 (~0.5天)
- few_shot.py: 各benchmark独立few-shot (~1.5天)

## 设计
- 4 models × 4 benchmarks × 2 precisions × 2 temps × 6 prompts × 6 seeds × 4 orderings = 9,216 conditions
- × 200 items = 1,843,200 total inferences
- GPU time: MC ~7h + GSM8K ~16-32h = ~23-39h (4 GPU parallel)

Server file: results/analysis/exp002_prep_report.md