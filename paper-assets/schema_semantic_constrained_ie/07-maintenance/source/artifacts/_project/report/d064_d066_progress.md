# d064 / d066 / d067 进度报告 (2026-05-20)

## d064 greedy 进度（westd-16980）

两张 RTX PRO 6000 Blackwell (98GB)，GPU利用率 88%/84%，各占 ~19GB 显存。

| 文件 | 行数 | 目标 | 状态 |
|------|------|------|------|
| d064_llama_docred_greedy_unconstrained_w5.jsonl | 998 | 998 | ✅ 完成 |
| d064_llama_docred_greedy_constrained_w5.jsonl | 998 | 998 | ✅ 完成 |
| d064_qwen_docred_greedy_unconstrained.jsonl | 171 | 998 | 🔄 运行中 (17.1%) |
| d064_qwen_docred_greedy_constrained.jsonl | 34 | 998 | 🔄 Cascade 已启动 (3.4%) |

- Qwen greedy unc: log 显示 [167/998]，平均 ~10-12s/sample（波动大，个别超30s），预计 ETA **2-3h**
- Qwen greedy con: cascade 已自动启动（模型加载完成），34 行已输出，两个任务分别跑在两张 GPU 上
- Llama greedy 两组全部完成

## d066 SciERC beam sweep（westd-21461）

两张 RTX PRO 6000 Blackwell (98GB)，GPU利用率 78%/82%，各占 ~19GB 显存。

| 文件 | 行数 | 目标 | 状态 |
|------|------|------|------|
| qwen_scierc_beam1_unconstrained.jsonl | 551 | 551 | ✅ 完成 |
| qwen_scierc_beam1_full_s1.jsonl (con) | 551 | 551 | ✅ 完成 |
| qwen_scierc_beam2_unconstrained.jsonl | 506 | 551 | ⏳ 接近完成 (91.8%) |
| qwen_scierc_beam2_constrained | — | 551 | 未开始 |
| qwen_scierc_beam4_unconstrained | — | 551 | 未开始 |
| qwen_scierc_beam4_constrained | — | 551 | 未开始 |
| qwen_scierc_beam8_unconstrained | — | 551 | 未开始 |
| qwen_scierc_beam8_constrained | — | 551 | 未开始 |

- GPU1 log (d066_beam_sweep_scierc_gpu1.log) 显示 [356/551]，平均 ~2-3s/sample
- 已完成 2/8 configs，第3个接近完成；剩余 5 configs 待跑
- 预估每个 config ~20-30min，总 ETA **~2-3h**

## d067 seed variance（westd-21461）

| 指标 | 值 |
|------|------|
| 进度 | 529/551 (96.0%) |
| 输出文件 | 尚无 jsonl 输出 |
| 预估完成 | **~5min** |

- d067_seed_variance.log 显示 [529/551]，即将完成当前 seed
- 无 jsonl 输出文件可能意味着结果写入其他位置或在全部 seed 完成后统一输出
