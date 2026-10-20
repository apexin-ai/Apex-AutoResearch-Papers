# agent / loop_13.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`a96eb279027b33a549c3.json`](../../sessions/a9/a96eb279027b33a549c3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-15T22:47:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**westd-22162 cuda:0/1/2/3**，仅此 4 卡，无其他服务器
- DS accuracy 数据已降级为**定性观察**（D086），不作为 paper 主证据；QW 是 accuracy dose-response 主线
- GSM8K 聚合**必须用 nanmedian + Wilcoxon + bootstrap(median)**（D083），不能用 mean
- G× 论文数值已修正为 **21-64×**（D082），禁止引用旧值 58-241×
- batch1 accuracy 数据（pre-v2）需 v2 rescore 修正，**未修正的 batch1 数字不能写入论文**
- EMNLP 2026 ARR 截稿 **2026-05-25**（距今 10 天）

### 2. 🖥️ 基础设施快照
- 服务器：**westd-22162**，工作目录 `/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型路径：`checkpoints/Qwen2.5-7B-Instruct`、`checkpoints/DeepSeek-R1-Distill-Qwen-7B`（均在 `/root/autodl-tmp/pacs/` 下）
- 活跃进程：
  - PID 280638 — acc_ds_s020_8k_v2，cuda:2，已跑 51min
  - PID 282534 — acc_ds_s025_8k_v2，cuda:3，已跑 24min
  - PID 283843 — acc_ds_dense_8k_v2，cuda:0，已跑 17min
  - acc_qw_s025_n100_b2_fix — cuda:1（推测），刚提交，cron 已注册
- Cron 监控：4 个 active（上述 3 个 DS + acc_qw_s025_n100_b2_fix）
- 活跃 Worker：
  - `worker_code_qw_s020_s025_extend_n100`（21:08 启动，处理 QW n=100 扩展）
  - `worker_code_prepare_gsm8k_rand_s030_v2`（22:39 启动，准备 C10 GSM8K rand v2 代码）

### 3. 📊 当前状态
**刚做完：** acc_qw_s020_n100_b2_fix 进入 ANALYZING（QW s020 batch2 with 8k tokens 刚跑完），等待 Worker 回调提取结果。

**正在跑（4 RUNNING）：**
- acc_ds_s020_8k_v2（cuda:2）、acc_ds_s025_8k_v2（cuda:3）、acc_ds_dense_8k_v2（cuda:0）— DS 8k 重跑三件套
- acc_qw_s025_n100_b2_fix（刚提交）— QW s025 batch2 8k 修复

**排队（3 QUEUED）：**
- gsm8k_qw_rand_s025_v2、gsm8k_qw_rand_s030_v2 — **C10 最后缺失实验组**，bootstrap bug 修复后重跑
- acc_ds_s030_8k_v2

**等待：**
- Worker `worker_code_prepare_gsm8k_rand_s030_v2` 回调 → 拿到准备好的代码后提交 C10 GSM8K
- Worker `worker_code_qw_s020_s025_extend_n100` 回调 → QW 扩展结果
- acc_qw_s020_n100_b2_fix ANALYZING → cron/worker 回调提取 metrics
- 3 个 DS 8k 实验 cron 回调

### 4. 📋 待办（条件触发式）
- acc_qw_s020_n100_b2_fix cron 回调到达 → 提取 accuracy metrics → update_registry(DONE) → 与 batch1 合并计算 n=100 accuracy
- acc_qw_s025_n100_b2_fix 完成 → 同上，然后编译完整 QW accuracy 4-point dose curve（s015/s020/s025/s030）
- 3 个 DS 8k 实验完成 → 提取 accuracy → 记为定性观察（D086），不作为主证据
- worker_code_prepare_gsm8k_rand_s030_v2 回调 → 代码就绪后在 cuda:0+cuda:1 提交 gsm8k_qw_rand_s025_v2 + gsm8k_qw_rand_s030_v2（需等 DS dense 8k 释放 cuda:0）
- C10 GSM8K 两组全部完成 → 汇报 Director → 进入 Round 10 consistency check → 最终提交决策
- acc_ds_s030_8k_v2、acc_ds_s015_8k_v2 → DS 剩余 8k 实验，GPU 空出后排队跑

### 5. 🎯 战略上下文
**核心结论：** importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed, 两个模型家族 DS+QW）。QW 是主证据线，DS 为辅助。

**关键决策链：**
- D080: GSM8K 聚合 bug 修复（NaN 过滤 + nanmean→nanmedian）
- D082: G× 数值下修 58-241× → 21-64×
- D083: 统计方法统一为 median + Wilcoxon
- D086: DS accuracy 降为定性观察（truncation-dominated），QW 作为主线
- D087: QW n=100 eval 完成，batch1 待 v2 修正

**易错点：**
- batch1 数据有 pre-v2 和 v2 两版，当前 registry 里部分 batch1 可能是旧值，合并时必须用 v2 rescored 数据
- DS 的 failure mode 是 truncation（CoT 太长），不是 reasoning error——论文需明确声明这一点
- QW s015 几乎无损（0pp degradation），这是"免费午餐"论点，但只对 QW 成立
- C10 GSM8K random masking 是**对照组**（vs importance masking），结果无论正负都有价值，但如果 random 也显示 compound interaction，需要在论文中解释为什么 importance 仍然更好
- `r9c2-spike` 系列（3 个 failed）待清理标记 abandoned，不要重跑


---
