# agent / loop_3.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`4b8d9a4a1d6ba82f028e.json`](../../sessions/4b/4b8d9a4a1d6ba82f028e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T03:41:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 cuda:0 和 cuda:1，不可用其他 GPU
- 论文 scaling section（results.tex §5.7, experiments.tex §4.5）**不要修改**——Director 明确要求等 355M 全部 3-seed 完成后再定论
- tmux chain 必须用单个 bash 脚本串行执行（`script1 && script2`），**禁止 tmux send-keys 追加命令**（已导致 cuda:1 空闲 1h 事故）
- 355M 上 RGDS vs Uncurated 排序与 125M **相反**（RGDS 优于 Uncurated），写论文时不能简单说"RGDS 是最差的"——核心 claim 锚定在"同 budget RGDS 劣于 Random"(C3)

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 `/root/div_cal_verify`，数据 `/root/div_cal_verify/data_gpt2/`
- Python：`/root/miniconda3/bin/python`，conda base 环境，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 结果目录：`/root/autodl-tmp/div_cal_verify/results_medium_*`
- 日志目录：`/root/autodl-tmp/div_cal_verify/medium_*.log`
- 活跃 tmux sessions：
  - `chain_cuda0_s123` — cuda:0 串行 uncurated→rgds→random50 seed=123
  - `medium_external_seed123` — cuda:1 external seed=123 (PID 405067)
  - `auto_cuda1` — 等 external_seed123 完成后自动在 cuda:1 启动 random50_seed123（flag `/tmp/random50_seed123_on_cuda1`）
- Cron 监控：medium_uncurated_seed123 (chain_cuda0_s123), medium_external_seed123

### 3. 📊 当前状态
刚完成 seed=456 全部 6 个脚本创建（4 方法 + 2 chain），registry 已注册 4 个 PREPARING。

**RUNNING**：
- `medium_uncurated_seed123` — cuda:0, chain 第 1/3，Gen 6/8
- `medium_external_seed123` — cuda:1, Gen 1/8
- `medium_rgds_seed123` — PREPARING（等 uncurated 完成后 chain 自动接）
- `medium_random50_seed123` — PREPARING（cuda:1 auto_cuda1 会抢跑，或 cuda:0 chain 兜底）

**DONE（355M seed=42 四方法完整）**：
- Uncurated: PPL=91.66 | RGDS: 82.84 | External: 77.74 | Random: 70.25

**等待**：seed=123 全部完成 → 两卡同时启动 seed=456 chain

### 4. 📋 待办
- seed=123 任一实验 cron 回调 → spawn Worker 提取 metrics，update_registry DONE
- cuda:1 external_seed123 完成 → auto_cuda1 自动启动 random50_seed123（已部署），确认 nvidia-smi
- cuda:0 chain_cuda0_s123 跑到 random50 → 检查 `/tmp/random50_seed123_on_cuda1` flag，有则跳过
- seed=123 全部 4 方法完成 → 两卡同时启动 seed=456：`tmux new -d -s chain_cuda0_s456 "bash chain_cuda0_s456.sh"` + `tmux new -d -s chain_cuda1_s456 "bash chain_cuda1_s456.sh"`，注册 cron，汇报 Director
- seed=456 全部完成 → 355M 3-seed 统计检验 → 更新论文 scaling section → 汇报 Director

### 5. 🎯 战略上下文
- **EMNLP 2026 ARR DDL: 2026-05-25**（剩 11 天）
- **D019**：355M 升级为 3-seed。seed=456 脚本已就绪，等 seed=123 完成后启动。预计 seed=456 全部完成 ~21:00-22:00 CST 今天。
- **355M 关键发现**：排序 Random(70.25) < External(77.74) < RGDS(82.84) < Uncurated(91.66)。C3 成立（RGDS 劣于 Random +18%），但 RGDS < Uncurated（与 125M 相反）。原因：355M baseline collapse 极严重（+245%），50% 裁剪的正则化效应抵消了 alignment gap。
- **125M 论文主体已完成**：Table 1 + Table 2（统计检验）+ Figure 1（PPL trends）+ Figure 2（ratio trajectory）全部就绪，3-seed 数据已写入全部 .tex 文件。
- **易错点**：(1) chain 完成不等于所有子实验都成功——chain 内第一个实验的 cron 会在 chain 中间触发"进程退出"，实际是子实验完成，需要检查日志判断是哪个子实验完成了 (2) run_medium_random50_seed123.sh 开头有 flag 检查，run_medium_random50_seed456.sh 没有（已清理）(3) medium_external_seed42 的 registry 之前 Worker 更新失败过一次，需确认 metrics 已写入


---
