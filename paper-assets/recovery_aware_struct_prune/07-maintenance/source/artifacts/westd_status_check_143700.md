# westd-11672 GPU Status Check — 2026-05-17 22:38 UTC

## GPU 占用总览

| GPU | Temp | Power | VRAM | Util | PID | Task | Status |
|-----|------|-------|------|------|-----|------|--------|
| cuda:0 | 71°C | 515W/600W | 16.8/97.9 GB | 97% | 28136 | eval_humaneval_grpo_rasp_20_2048 | Running 45min |
| cuda:1 | 78°C | 598W/600W | 31.5/97.9 GB | 99% | 14556 | eval_math500_grpo_standard_20 | Running 5h12m |
| cuda:2 | 75°C | 581W/600W | 17.3/97.9 GB | 97% | 27199 | eval_humaneval_grpo_standard_20_2048 | Running 57min |
| **cuda:3** | **29°C** | **34W/600W** | **0/97.9 GB** | **0%** | — | — | **IDLE** |

## 各任务进度

### cuda:0 — eval_humaneval_grpo_rasp_20_2048 (PID 28131/28136)
- 进度: 52/164 (32%)
- Pass@1 @ 40: 0.2000
- 估计剩余: ~2-3h (平均 ~48s/problem, 波动大)

### cuda:1 — eval_math500_grpo_standard_20 (PID 14556)
- 运行 5h12m, max_new_tokens=4096, VRAM 31.5GB
- stdout 输出到 pipe, 无可读日志文件
- **风险**: 与 RASP 版相同的 max_new_tokens=4096 设置, 已运行超 5h, 可能同样面临超时

### cuda:2 — eval_humaneval_grpo_standard_20_2048 (PID 27194/27199)
- 进度: 39/164 (24%)
- Pass@1 @ 20: 0.1500
- 平均 ~83s/problem, 估计剩余: ~2.5-3h

### cuda:3 — eval_math500_grpo_rasp_20_v2 (PID 11896) — 已退出

## eval_math500_grpo_rasp_20_v2 超时诊断

- **EXIT_CODE=124** (timeout kill)
- 启动: 16:34:18, 评估开始: 16:35:45
- 超时设置: 21600s (6h)
- **超时时进度: 193/500 (38.6%)**
- 最后 accuracy checkpoint (150/500): **Acc = 0.3067**
- 平均 ~112s/problem, 但方差极大 (2.5s ~ 247s)
- 根因: max_new_tokens 过大导致部分问题生成时间极长, 6h 仅完成 38.6%
- **无部分结果**: `math500_grpo_rasp_20.json` 不存在, 进程被 kill 前未写出 JSON

## 结论

- **cuda:3 空闲可用**, 0 显存占用, 可立即启动新任务
- MATH-500 RASP 评估需要重跑, 建议降低 max_new_tokens (如 2048) 或增加 timeout
- cuda:1 的 math500 standard 评估同样使用 max_new_tokens=4096, 高概率也会超时
