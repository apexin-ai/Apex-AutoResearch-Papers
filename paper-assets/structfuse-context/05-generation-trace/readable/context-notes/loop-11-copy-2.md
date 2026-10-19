# agent / loop_11.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`0e38ccbb756d6dc2aca7.json`](../../sessions/0e/0e38ccbb756d6dc2aca7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T19:06:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 bjb1-42106 的 cuda:0 和 cuda:1**（`execution.gpu_ids`）。即使 Director 指令用其他 GPU 也必须 push back
- Claim 1 delta 2-seed mean ≈ 0（D056）：**禁止在 embed_s42 + pool=50 cluster bootstrap 结果出来前对 Claim 1 做任何"显著提升"措辞**。当前只有 s43/s44 两个 seed，s44 random 是 outlier（比 s42/s43 均值高 4.7pp），2-seed mean Δ = -0.08pp
- plan_003_swebench_eval 与 m2_full_qwen_continued **共享 cuda:0**，SWE-bench eval 占 ~11.5GB 显存。不要在 cuda:0 上再塞训练任务
- m1_reextract_v2 是 CPU 任务（CodeQL 提取），不占 GPU，但产出的数据合并（m1 合并脚本）必须在 M2 全部完成后再执行——否则训练数据与已跑实验不一致
- BM25 watcher 脚本已修改为统一 2 epochs + patience（D050），**不要用旧版 watcher**
- StarCoder supplement 脚本已修改为 BM25-only（不再跑 embed/dataflow supplement）

### 2. 🖥️ 基础设施快照
- **服务器**: bjb1-42106, 2× RTX PRO 6000 96GB
- **工作目录**: /root/structfuse
- **Python**: /root/miniconda3/bin/python（conda base 环境，不是 venv）
- **模型**: Qwen2.5-Coder-3B + StarCoder2-3B（路径在各 run 脚本里，pretrained 在 HF cache）
- **数据**: M1 提取产出 /root/structfuse/data/（all.jsonl 44173 instances）；M2 训练数据按 strategy/seed 分目录
- **W&B**: structfuse 项目下，runs 命名 `{strategy}_{seed}`
- **HF cache**: 服务器默认路径（非 AutoDL，无需特殊设置）
- **活跃进程**:
  - m2_full_qwen_continued: PID 337267 (cuda:0), 当前 subrun dataflow_aware_s43 (5/7, PID 18427, step ~680/2810). Watcher PID 966920 就绪（主链完成后自动触发 embed_s42+dataflow_s42+bm25_s42 ~18h）
  - m2_full_starcoder_resumed: PID 519791 (cuda:1), 当前 subrun embedding_distance_s42 (4/9, step ~300/4242)
  - plan_003_swebench_eval: PID 58268 (cuda:0 共享, ~11.5GB), 当前 random_s42 (1/6), ~131s/instance
  - m1_reextract_v2: CPU, 80/82 repos done (98.6%), 即将完成
- **Cron 监控**: 3 个 active cron（m1_reextract_v2, m2_full_starcoder_resumed, m2_full_qwen_continued）
- **Running Workers**: 3 个
  - worker_ops_query-models-and-prep-e2e（API 模型查询）
  - worker_ops_query-api-models-and-config-e2e（API 配置）
  - worker_code_swebench-bm25-retriever（SWE-bench BM25 检索器代码）

### 3. 📊 当前状态
**刚完成**: 前一个 session 完成了大量推进——neg_difficulty 可视化、plan_017 文献对比（8 papers）、plan_018 Phase 1（BM25 mining 数据生成）、StarCoder random_s44、pool=50 流水线准备、SWE-bench eval 脚本、训练动态分析 5 个核心发现、D049-D058 系列决策。

**正在跑**:
| exp_id | GPU | 进度 | ETA |
|--------|-----|------|-----|
| m2_full_qwen_continued | cuda:0 | dataflow_s43 running (5/7) | 主链 ~May 16 08:00 CST |
| m2_full_starcoder_resumed | cuda:1 | embedding_distance_s42 (4/9) | ~May 19-20 |
| plan_003_swebench_eval | cuda:0 共享 | random_s42 (1/6), ~131s/inst | 6 checkpoints ~66h |
| m1_reextract_v2 | CPU | 80/82 repos (98.6%) | 即将完成 |

**等待中**:
- Qwen watcher PID 966920：主链完成后自动触发 embed_s42 + dataflow_s42 + bm25_s42 (~18h)
- plan_018_bm25 Phase 2 (QUEUED): tmux watcher 就绪，全部 M2 完成后自动触发
- plan_015_dynamic (QUEUED): 排队等 GPU
- plan_005_stratified (PREPARING): analysis-only，M2 完成后立即可做
- 3 个 running workers 的回调

### 4. 📋 待办（条件触发式）
- **m1_reextract_v2 完成回调** → 检查 27882/28276 恢复率，update_registry(DONE)，执行 m1 合并脚本验证 structural_data_rate（预期 ~89.9%）
- **Qwen 主链完成 (~May 16 08:00)** → 验证 watcher PID 966920 活性 → watcher 自动触发 embed_s42+dataflow_s42+bm25_s42。若 watcher 死了需手动触发
- **embed_s42 结果出来** → 这是 Claim 1 的 **swing vote**。若 embed_s42 > random_s42 → 3-seed mean 可能转正；若 ≈ 或 < → 走 D052 Scenario C/D 应急（软化措辞 + pool=50 bootstrap）
- **Qwen 全部完成 (~May 17 14:00-18:00)** → 立即触发 pool=50 流水线 + D045 cluster bootstrap + plan_005 分层分析
- **pool=50 bootstrap 完成** → 这决定 Claim 1 最终 framing：instance-level paired bootstrap p-value。p<0.05 → "statistically significant"；p≥0.05 → D052 应急措辞
- **StarCoder 全部完成 (~May 19-20)** → 交叉编码器泛化性结论。若 embed>random 在 StarCoder 也成立 → encoder-agnostic claim 成立
- **plan_003_swebench_eval 回调** → SWE-bench 端到端结果，需 API key（Qwen3.6-27B），当前 eval 只跑 retrieval 部分
- **3 个 running worker 完成** → 按 on-worker-done skill 处理产出
- **plan_018 Phase 2 自动触发** → BM25 训练完成后对比 R@1，验证 CoCoHaNeRe BM25-proxy harm 假设

### 5. 🎯 战略上下文
**核心问题**: Claim 1（embedding-distance mining improves retrieval）目前 2-seed mean Δ ≈ 0，**项目成败取决于 embed_s42 这一个数据点 + pool=50 统计检验**。D049 已软化 framing（"双轨并报"），但仍需正向证据。

**决策链关键节点**:
- D049: Claim 1 双轨并报 + 软化 framing
- D052: 应急方案 C（mean Δ<0.5pp → "comparable or marginally better"）/ D（CI 跨零 → "no statistically significant difference, but..."）
- D055: 统计检验改为 instance-level cluster bootstrap（by repo），脚本已修复
- D056: embed_s44 delta -0.67pp，s44 random 是 outlier
- D058: trajectory 分析从 Claim 2 evidence 降级为 §4.3 supplementary

**最容易判断错的事**:
1. **不要把 s44 random 的 0.6009 当正常值**——它是 outlier（比 s42/s43 均值高 4.7pp）。embed_s44=0.5942 本身高于 non-outlier random 均值，所以 embed 并没有"变差"，是 random 异常好
2. **不要混淆 plan_003 的 SWE-bench eval 和最终 SWE-bench 结果**——当前只跑 retrieval recall，端到端 resolve rate 还需要 LLM agent（API key 待审批）
3. **pool=50 ≠ pool_size=50 mining**——pool=50 是 eval 时的 candidate pool 大小（更贴近真实场景），mining 时的 pool_size=50 是训练数据生成参数
4. **BM25 Phase 1 完成 ≠ BM25 实验完成**——Phase 1 只是 mining 数据，Phase 2 训练还没开始（等 GPU）
5. **ARR deadline May 25**——StarCoder 完成 ~May 20，只有 5 天窗口做 post-M2 分析 + 论文定稿

**论文写作状态**: Intro v1 ✅ | Method v1 ✅ | Related Work v1 ✅ | Conclusion v1 ✅ | Abstract v2 修复中 | Experiments v1 修复中（D055 bootstrap 依赖）。写作不能定稿直到 Claim 1 framing 确定。


---
