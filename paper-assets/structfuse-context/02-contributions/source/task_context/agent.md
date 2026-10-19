---
loop: 13
reason: max_wall_time
updated: '2026-05-16T16:24:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（bjb1-42106）。即使 Director 指令用其他 GPU 也必须 push back
- StarCoder chain 脚本禁用 `set -euo pipefail`——已因 exit 143 级联杀掉 wrapper 两次。改用 `set -eo pipefail` + 每 run 后检查 checkpoint 产出
- evaluate_pool50.py 正在被修复以支持 LoRA adapter-only checkpoint（<100MB）。修复完成前不要用旧版跑 embedding/dataflow checkpoint 的 D062 eval
- UniXcoder 环境必须 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不能假设 python 在 PATH 里（已踩坑一次）
- 训练必须用 `submit_training_job`，禁止 nohup（orphan 进程无监控无回调）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (root@)，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/structfuse，数据盘：/root/autodl-tmp/structfuse/
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：Qwen `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B`，StarCoder `/root/autodl-tmp/structfuse/models/bigcode/starcoder2-3b`，UniXcoder `microsoft/unixcoder-base`（HF cache）
- Qwen outputs: /root/autodl-tmp/structfuse/full_m2_qwen_outputs/
- StarCoder outputs: /root/autodl-tmp/structfuse/full_m2_starcoder_outputs/
- UniXcoder outputs: /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/
- D062 results: /root/autodl-tmp/structfuse/d062_results/
- 活跃进程（session 结束时）：
  - Qwen chain PID 337267 (cuda:0, cron 监控中) — dataflow_s44 running, 剩 bm25_s43/s44 + watcher PID 966920 等触发 supplement
  - UniXcoder s43/s44 chain PID 167371→187348 (cuda:0) — embedding_distance_s44 刚 early stop，下一个 dataflow_s44
  - StarCoder wrapper PID 519791 **已死**，旧 cron 反复触发（已忽略 3 次）
  - D062 eval PID 183027 在跑 test set random_s43 (cuda:0)

### 3. 📊 当前状态
**两个关键 Worker 正在运行**（session 结束时未完成，需要处理回调）：
1. `worker_code_d062_eval_adapter_fix_20260516T162002` — **最高优先级**。正在修复 evaluate_pool50.py 的 LoRA adapter 加载兼容。最后状态：dry-run 验证阶段（turn 8）。完成后需重跑 D062 items 7-14（embed×6 + dataflow×2）
2. `worker_ops_starcoder_chain_restart_20260516T162141` — 正在从 embed_s44 重启 StarCoder chain。最后状态：检查配置阶段（turn 11）。完成后 cuda:1 恢复训练

**Registry RUNNING**：
- `m2_full_qwen_continued`：cuda:0，dataflow_s44 (7/9)，剩 3 runs + supplement watcher
- `m2_full_starcoder_resumed`：**wrapper 已死**，等 restart Worker 重新提交。旧 cron 不要 poll（会误标 failed）
- `unixcoder-3strat-s43`：s43 全部完成（null confirmed, span=0.92pp），s44 进行中（embed_s44 刚 early stop）

**Registry PREPARING**：
- `unixcoder-3strat-s44`：s44 串行在 s43 chain 里，自动推进
- `qwen_random_s42_retrain`：脚本就绪 /root/structfuse/scripts/run_random_s42_retrain.sh，等 GPU 空闲
- `plan_005_stratified`：blocked on D062 eval 完成

### 4. 📋 待办
- D062 adapter fix Worker 完成 → 确认 8 个 checkpoint eval 已提交/运行 → 汇报 Director
- StarCoder restart Worker 完成 → 确认新 PID + 新 cron 注册 → 更新 registry metrics
- StarCoder 旧 cron 再次触发 → 忽略，不 poll（等新 cron 替换）
- UniXcoder s44 chain 完成（3 strategies done）→ 收集 metrics → 更新 registry → 3-seed null result 统计汇报 Director
- Qwen chain 完成 → watcher PID 966920 自动触发 supplement (embed_s42+dataflow_s42+bm25_s42) → 确认启动
- D062 eval 14/14 全部完成 → 跑 d062_analysis.py → stratified + bootstrap CI → 汇报 Director
- GPU 空闲 → 优先 qwen_random_s42_retrain（已审批免审批），然后 RepoBench-R eval
- Qwen+StarCoder 全部完成 → BM25 Phase 2 训练自动触发

### 5. 🎯 战略上下文
- **D062 是当前最大阻塞**：checkpoint selection (query split) 阻塞 Claim 1 最终结论 + Claim 2 stratified analysis + bootstrap CI。Director 刚发 CRITICAL 指令修复 adapter 加载 bug
- **Dual-track narrative (D059)**：A=stratified heterogeneity reveals when mining helps，B=explain why aggregate deltas are small。Claim 2 覆盖率仍为 0%，全依赖 D062 完成
- **UniXcoder null result 已跨 2 seed 确认**（s42 span 0.37pp, s43 span 0.92pp, 排序一致 random≥embed>dataflow）。这支撑 Track B（小模型/encoder-only 无法利用 hard negatives）
- **Checkpoint selection criterion effect 巨大**：+16.3pp for s43 (by_R@1=0.504 vs by_val_loss=0.341)，远超策略差异。D062 query split 是唯一可靠解法
- **易错点**：(1) in-training eval pool=8 有 ±0.5pp noise，不可作为最终比较依据，必须用 pool=50 (2) s42 regime (3ep/p0) 与 s43/s44 (2ep/p2) 不同，跨 seed 比较需标注 regime (3) StarCoder checkpoint 可能也有 adapter vs full model 不一致问题，D062 fix 需兼顾 (4) bm25_s42 在 StarCoder chain 中是否真的跑了存疑（之前有过虚假记录修正）
- **ARR May 25 deadline**：9 天完成所有补充实验 + 论文定稿，时间紧张但 GPU·h 余量充足（~250h 可用）
