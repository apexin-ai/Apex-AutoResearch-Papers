# agent / loop_25.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_25.md`
- **Structured JSON:** [`80c335cb1eb64b1a7f97.json`](../../sessions/80/80c335cb1eb64b1a7f97.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: idle_timeout
updated: '2026-05-23T03:10:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目分配的 GPU 白名单：cqa1-21977:cuda:0, westd-29999:cuda:0。westd 上 cuda:1/2/3 不在白名单，之前提交到这些卡上的实验是历史遗留
- westd-29999 网络默认不通（刚确认 `[Errno 101] Network is unreachable`），eval 脚本里 `load_dataset` 会联网。**必须设 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`** 或先 `source /etc/network_turbo`，否则 eval 必挂
- D215 决策：Falcon3 结果不管好坏直接提交 ARR，不再加内审轮次
- ARR deadline: May 25（D+4），时间极紧

### 2. 🖥️ 基础设施快照
- **westd-29999**: 工作目录 `/root/contamcal-irt-calibration/exp001/`，Python `/root/miniconda3/bin/python`，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **cqa1-21977**: 1× RTX 4090 D，同样 conda base 环境
- 模型缓存：`/root/autodl-tmp/.hf_cache/Falcon3-7B-Base`
- Checkpoint 路径模板：`/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d{dosage}_s42/lora_adapter`
- evaluate.py：`/root/contamcal-irt-calibration/exp001/evaluate.py`（line 167 调 `load_dataset("cais/mmlu", "all", split="test", cache_dir=cache_dir)`）
- 活跃进程：
  - `sft_falcon3_7b_d100_s42` — cqa1-21977 cuda:0, PID 666107（SFT 训练）
  - `sft_falcon3_7b_d050_s42_v2` — westd-29999 cuda:3, PID 600596（SFT 训练）
- 磁盘：westd 根分区 49% used (427GB free)，cqa1 根分区 95% used ⚠️

### 3. 📊 当前状态
**刚做完**：收到 eval_falcon3_d000_s42 失败 cron 回调，诊断出网络不通根因，更新了 registry failure_reason。

**RUNNING**:
- `sft_falcon3_7b_d100_s42` — cqa1-21977，Falcon3 100% dosage SFT
- `sft_falcon3_7b_d050_s42_v2` — westd-29999，Falcon3 50% dosage SFT（LR bug fix 重跑）

**DONE(failed) 待重试**:
- `eval_falcon3_d000_s42` — 网络不通，需重试
- `eval_falcon3_d005_s42` — 同上
- `eval_falcon3_d025_s42` — 大概率也已失败（同样命令同样服务器），需确认

**等待中**:
- Worker `worker_fix_eval_falcon3_network_20260522T110905` 正在 SSH 到 westd-29999 诊断网络+缓存状态，等其回调后决定修复方案并重试 eval
- d050_v2 和 d100 SFT 完成后需要提交对应 eval

### 4. 📋 待办
- Worker 网络诊断回调 → 根据结果修复 evaluate 命令（加 `HF_DATASETS_OFFLINE=1` 或 `source /etc/network_turbo`）→ 重新提交 d000/d005/d025 三个 eval
- sft_falcon3_7b_d050_s42_v2 完成回调 → 提交 eval_falcon3_d050_s42
- sft_falcon3_7b_d100_s42 完成回调 → 提交 eval_falcon3_d100_s42
- 全部 5 个 dosage (d000/d005/d025/d050/d100) eval 完成 → 汇总 Falcon3 dose-response profile → 判断 taxonomy 分类（Immune/Collapse/V-recovery/Benefit）→ 更新论文 → 按 D215 直接提交 ARR

### 5. 🎯 战略上下文
- 项目核心：SFT-route benchmark contamination 产生 family-dependent dose-response profiles，4-pattern taxonomy（Immune/Collapse/V-recovery/Benefit）
- 已有 6 families 完成：Phi-4(Immune), LLaMA-3(Immune), Qwen-14B(Collapse), Qwen-7B(V-recovery), Gemma-2(Benefit), OLMo-2(Benefit)
- **Falcon3-7B-Base 是第 7 个 family**，cross-family replication 的关键补充。d000/d005/d025 的 v2 SFT 已 success（LR bug fix 后），d050/d100 还在训练
- 终稿已经 ready（Round 10 action matrix 全部 resolved，8 页 main text 编译通过），Falcon3 数据是最后拼图
- **易错点**：westd 网络问题是 AutoDL 常见坑，eval 命令必须带离线环境变量。不要假设网络通。之前所有成功的 eval 要么在网络通的时候跑的，要么数据集已缓存+设了 offline mode
- **易错点**：cqa1 磁盘 95% 满，提交新实验前必须检查磁盘


---
