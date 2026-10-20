# Embedding & LLM-Judge 状态报告
> 检查时间: 2026-05-14 ~21:20 UTC

## 1. Encoder Ablation Embedding

| Encoder | 状态 | 文件大小 | Windows 数 | Embedding 维度 | 耗时 |
|---------|------|----------|-----------|---------------|------|
| **e5-large** | ✅ 完成 | 2.07 GB | 54,809 | [10, 1024] per window | ~36 min |
| **bge-m3** | ✅ 完成 | 1.05 GB | 54,809 | [10, 1024] per window | ~23 min |
| **gte-large** | ⚠️ 仅 10 条 | 0.4 MB | 10 | [10, 1024] per window | (pilot/测试) |

- 文件路径: `/root/autodl-tmp/agent_progress_probe/ablation_embeddings/{name}_embeddings.pt`
- 数据结构: dict, keys = `[embeddings, labels, trajectory_ids, instance_ids, step_indices_list, confidences, embed_dim, encoder, model_id]`
- e5-large 和 bge-m3 均完成全部 54,809 windows（5,000 trajectories）
- gte-large 仅 10 条，应为 pilot 测试产物
- 两个进程均已退出（e5-large EXIT_CODE=129/SIGHUP, bge-m3 EXIT_CODE=0）

## 2. Baseline LLM-Judge

| 指标 | 值 |
|------|-----|
| 状态 | 🔄 运行中 (pid=27419 存活) |
| 进度 | **1,400 / 1,824** (76.8%) |
| 模型 | anthropic/claude-sonnet-4.6 |
| 模式 | zero-shot |
| 当前 macro_f1 | **0.6659** |
| 总 tokens | input=2,182,949 / output=158,595 |
| 已花费 | ~$8.93 |
| 解析失败 | 0 |
| 预计总花费 | ~$11.6 (线性外推) |

- 结果文件: `/root/autodl-tmp/agent_progress_probe/results/llm_judge_full_zeroshot.json` (1.7 MB, 1400 条记录)
- 日志: `/root/autodl-tmp/agent_progress_probe/logs/llm_judge_full.log`
- macro_f1 在 0.65-0.67 区间波动，趋于稳定
- 0 parse failures，运行健康
- 剩余 424 条，预计还需 ~1-2 小时完成
