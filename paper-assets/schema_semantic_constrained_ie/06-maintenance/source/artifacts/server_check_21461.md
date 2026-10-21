# Server Check: westd-21461
**Time**: 2026-05-20 11:51 CST

## (a) Python 进程

| PID | State | GPU | VRAM | 命令 |
|-----|-------|-----|------|------|
| 167691 | R (running) | cuda:0 | 18910 MiB | `python run_constrained_extraction.py --mode unconstrained --dataset docred --model_path qwen_lora_docred_merged --output_path d065_qwen_docred_greedy_unc_4096.jsonl --device cuda:0 --max_new_tokens 4096 --decoding_strategy greedy --skip_on_error` |

**GPU1 无进程** — d066 beam sweep 已完成，进程正常退出。

## (b) nvidia-smi

| GPU | 型号 | Util | 显存占用 | 进程 |
|-----|------|------|----------|------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | 87% | 18919/97887 MiB | PID 167691 (python) |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 0% | 0/97887 MiB | — |

Driver: 580.119.02, CUDA: 13.0

## (c) tmux sessions

无法通过 ssh_read_only 检查（tmux 不在白名单中）。

## (d) d066 SciERC beam8 constrained 进度

**已完成** — 完成时间 2026-05-20 11:47:46 CST

所有 beam sweep 配置均已跑完（beam{1,2,4,8} x {unc, constrained}）：

| 文件 | 行数 |
|------|------|
| qwen_scierc_beam8_full_s1.jsonl (constrained) | **551/551** |
| qwen_scierc_beam8_unconstrained.jsonl | **551/551** |

### beam8 评估结果对比

| 指标 | Unconstrained | Constrained (full_s1) |
|------|--------------|----------------------|
| Entity P/R/F1 | 63.75 / 69.28 / **66.40** | 63.73 / 69.22 / **66.36** |
| Relation P/R/F1 | 37.81 / 50.31 / **43.17** | 38.25 / 50.82 / **43.65** |
| DR violation rate | 1.77% (23/1297) | **0.00%** (0/1295) |
| Entity type violations | 0 | 0 |
| Relation vocab violations | 0 | 0 |
| Cross-field violations | 1 | 0 |

**注意**: `eval_beam8_con.json` 文件缺失（仅有 `eval_beam8_unc.json`），但 violation report 中有完整 F1 数据。

### d066_docred_beam_sweep 目录
- qwen_docred_beam1_unc.jsonl
- qwen_docred_beam4_unc_200.jsonl / beam4_s1_200.jsonl (200-sample subset)
- eval_beam4_unc.json / eval_beam4_s1.json

## (e) d065 Qwen greedy 4096 进度

**运行中** — PID 167691, GPU0

| 指标 | 值 |
|------|-----|
| 已处理 | **104 / 998** docs (10.4%) |
| 模式 | unconstrained |
| 数据集 | DocRED dev (998 docs) |
| 模型 | qwen_lora_docred_merged |
| 解码 | greedy, max_new_tokens=4096 |
| 启动时间 | 2026-05-20 11:14:29 CST |
| 已运行 | ~37 min |
| 预估速度 | ~2.8 docs/min |
| 预估剩余 | ~5.3 hours |

## (f) 日志摘要

**d066 log** (最后输出): beam sweep 全部完成，beam8 constrained violation rate = 0.0%, Relation F1 = 43.65。

**d065 log**: 模型加载完成，开始推理。无报错。

## 总结

1. **d066 SciERC beam sweep**: 全部完成，GPU1 空闲可用
2. **d065 Qwen DocRED unc**: 104/998 (10.4%), 预计还需 ~5h
3. **GPU1 空闲** — 可安排新任务
4. **待处理**: d065 constrained 还未启动（需等 unconstrained 完成后，或用 GPU1 并行跑）
