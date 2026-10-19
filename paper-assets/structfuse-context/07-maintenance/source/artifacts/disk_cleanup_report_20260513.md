# 磁盘清理报告 — cqa1-21977

**日期**: 2026-05-13

## 清理前后对比

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 154G (91%) | 109G (64%) |
| 可用 | 16G | 61G |
| **释放** | — | **45G** |

## 清理明细

| 删除项 | 大小 | 说明 |
|--------|------|------|
| P2B checkpoints (4个: embedding_distance_s42, random_s42/s123/s456) | 24G | 已分析完毕，metrics 在 registry |
| .hf_cache/datasets/ (SWE-bench/swe-smith) | 4.9G | 无关数据集 |
| alfworld_data/ | 2.2G | 无关 RL 项目 |
| mvp_results/ | 1.7G | 旧 MVP 结果 |
| structfuse/dryrun_repos/ + dryrun_output* + 50repo_results/ + mvp_data/ | ~1G | 旧测试/dry-run 数据 |
| gpt2-small/ | 526M | 未使用 |
| mvp_data/ (root) | 295M | 旧数据 |
| repos/ | 170M | 旧数据 |
| rl-active-probe-fl/ | 160M | 无关项目 |
| __pycache__ | ~60K | 缓存 |

## 保留项

- StarCoder2-3B cache (12G) — 指令要求保留
- Qwen 模型 (.hf_cache/Qwen 984M + structfuse/models/Qwen 5.8G) — 指令要求保留
- Qwen3-14B-AWQ (9.4G) — 未明确可删，保守保留
- models/Mistral-7B-Instruct-v0.3 (14G) + Qwen2.5-7B-DPO*-merged (30G) — 可能仍有用，未删
- M1 全部数据（m1_extraction/ 2.2G, m1_repos/ 11G, m1_training_data/ 311M）

## M1 完成预估

| 指标 | 数值 |
|------|------|
| 已处理 repos | 23/131 |
| 已产出 JSON | 5,426 个, 2.2G |
| 平均每 repo 提取量 | ~96MB |
| 131 repos 总提取预估 | ~12.5G |
| 剩余需增长 | ~10.3G |
| codeql_db 峰值占用 | ~10-15G（当前 8 个 DB 共 10.6G，进程滚动创建/复用） |
| M1 总计还需 | ~20-25G |
| 当前可用 | **61G** |

**结论：空间充足，M1 可以顺利完成全部 131 repos。**

## 如果未来仍需更多空间

可进一步清理的候选项（需确认后操作）：
1. models/Mistral-7B-Instruct-v0.3 — 14G
2. models/Qwen2.5-7B-DPO003-merged — 15G
3. models/Qwen2.5-7B-Instruct-DPO-merged — 15G
4. .hf_cache/Qwen3-14B-AWQ — 9.4G
5. 已完成提取的 codeql_db（当前有 5 个非活跃 DB，共 ~6.6G）

以上合计可再释放 ~60G。
