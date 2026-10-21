# director / loop_15.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_15.md`
- **Structured JSON:** [`560cfbc4c8a3ec4df4f8.json`](../../sessions/56/560cfbc4c8a3ec4df4f8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-21T11:15:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-17606 cuda:0,1 + westd-47453 cuda:0,1,2,3，共 6 张，不可用其他服务器/卡
- westd 多实验并行时必须 Ray 集群隔离：Seed 5 用默认 port 6379，Seed 6 用 `RAY_ADDRESS=local`（M041 教训：CUDA_VISIBLE_DEVICES 不隔离 Ray）
- `qwen3_exp021_ragen_sft_v4` (3.3GB) 禁删——三个 seed 的 base model + SFT baseline OOD eval 需要
- 修改 YAML config 对已运行的 verl 进程无效（启动时加载到内存，不重读）
- Checkpoint 自动清理 watchdog 已部署（westd PID 118779, bjb1 PID 313318），接手后先验证是否存活
- >10GB 删除操作需 Director 批准

### 2. 🖥️ 基础设施快照
- **bjb1-17606**: root@bjb1-17606, `/root/cost-verify-agent-rl`, 2× RTX PRO 6000 96GB, 磁盘 ~55GB free
- **westd-47453**: root@westd-47453, `/root/cost-verify-agent-rl`, 4× RTX PRO 6000 96GB, 磁盘 ~81GB free
- Python/conda: aml-train 镜像, `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- SFT checkpoint: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/` (两台都有)
- FSDP→HF 转换脚本: `convert_fsdp_to_hf.py`（两台都有）
- W&B project: cost-verify-agent-rl
- Cron 监控已全部删除（误判太多），手动检查训练状态
- Watchdog: westd PID 118779, bjb1 PID 313318（step 10 后删 step 5，step 15 后删 step 10）

### 3. 📊 当前状态
三个 seed 并行训练中，全部正常无 collapse：
- **Seed 4 v2** (bjb1 cuda:0,1): W&B `fb1o765g`, ~4/15 step, train success 19.5%, seed=123
- **Seed 5 v2** (westd cuda:0,1): W&B `yyoghk1f`, ~9/15 step, train success 43.8%, seed=456, 最快完成（~2h）
- **Seed 6 v3** (westd cuda:2,3): W&B `2bbyvsdr`, ~7/15 step, train success 42.2%, seed=789

Registry 待处理：
- `sft_baseline_ood_eval`: PREPARING 已 8h+ 未推进，配置文件已就绪（westd），需要执行

刚发的 Director 指令（Agent 可能还没处理）：验证 watchdog 存活 + 删 bjb1 旧 HF ckpt + 推进 SFT baseline OOD eval

### 4. 📋 待办
- Watchdog PID 死了 → 重新部署（westd 两 seed + bjb1 一 seed）
- Seed 5 训练完成（最快） → FSDP→HF 转换 (`convert_fsdp_to_hf.py`) → 134-task OOD eval (τ=0.4)
- Seed 6 训练完成 → 同上
- Seed 4 训练完成 → 同上
- 三个 seed OOD eval 全部完成 → 更新论文 Table 1 为 5-seed mean±std（Seed 1: 23.88%, Seed 3: 10.45%, Seeds 4/5/6: TBD）
- SFT baseline OOD eval 完成 → 填入 Table 1 的 SFT baseline OOD 列（当前标"---"）
- 所有数据到位 → 通知 Paper Agent 更新 Table 1 + Abstract 数字 → submit_paper_to_review

### 5. 🎯 战略上下文
- 论文核心：step-independent agent RL 的双机制病理（M1 信息丢失 + M2 符号错误归因）+ episode-level 修复
- 目标 EMNLP 2026，8 页限制，当前 v16 已编译 8 页
- Cell C 不存在的原因：full trajectory + step-level advantage 是退化情况（只有一个 window，step=episode），论文 method.tex L53 有解释
- 已有 2 seed OOD：23.88% (Seed 1) 和 10.45% (Seed 3)，差距 13.4pp。如果新 3 seeds 聚集在低端，mean 会偏低但 episode-level > step-independent 的 claim 不受影响
- 48 个 failure 几乎全是早期环境调试（exp001-028），10 个 negative 是设计内的 negative controls（γ-sweep collapse、REINFORCE++ 平 baseline 等），支撑论文 claim
- M040: Seed 6 checkpoint 被误删导致全重训；M041: Ray 集群共享导致 GPU 越界；M042: Seed 4 batch size 不一致。这三个已解决但代价大——新 seed 启动前务必交叉校验 config
- Seed 5 train success 从 73.4% 回调到 43.8%，Reviewer 判断是正常波动（entropy>0, pass@8=1.0），如 step 10 继续降到 <30% 需重新评估


---
