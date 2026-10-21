# Project coordination (archived snapshot) — Part 2 of 2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../coordination-coordination-20260517-205756.md) · [Structured JSON](../../../sessions/73/73d9a3e436522fb3a89c.json)

## Round 89

### Tool result

_source line 601 · 2026-05-17T20:24:54.152082+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_monitor_all-server-status-loop25_20260517T202300\", \"status\": \"done\", \"task_type\": \"monitor:all-server-status-loop25\", \"project\": \"exec-sim-repair-verifier\", \"started_at\": \"2026-05-17T20:23:00.379904+00:00\", \"ended_at\": \"2026-05-17T20:24:45.020355+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"```\\n=== SEETACLOUD STATUS ===\\nGPU 0 (CLS v4 ckpt-4422):  [running] 3960/9784 (40.5%), running_acc=70.9%\\nGPU 1 (CWM s42 best):      [running] 1199/9784 (12.3%), running_acc=58.1%\\nGPU 2 (CLS s123 best):     [running] 3480/9784 (35.6%), running_acc=74.6%\\nGPU 3 (CWM s123 ckpt-8844):[running]  856/9784 ( 8.7%), running_acc=62.9%\\n\\nSpeed estimates:\\n  GPU 0/2 (CLS, batch=4): ~40 samples/min → ~2.4h remaining each\\n  GPU 1/3 (CWM, batch=1): ~5 samples/min → ~28h / ~30h remaining\\n\\n=== CLS S123 TRAINING METRICS ===\\nfinal_train_loss: 0.0039\\ntotal_steps: 6633/6633 (completed, 3 epochs)\\ncheckpoints: [checkpoint-4422, checkpoint-6633, best]\\nnote: eval_loss=NaN at final checkpoint (likely label mismatch in eval, not a real issue)\\n\\n=== EVAL RESULTS (completed, func-level) ===\\nfew_shot_results.json (func-level, already done):\\n  DeepSeek-6.7B: acc=59.95%, pass_f1=44.13, fail_f1=68.78, unparseable=0%\\n  Qwen3-8B:      acc=68.78%, pass_f1=64.46, fail_f1=72.17, unparseable=0%\\n\\n=== HOME GPU STATUS ===\\nQwen3 repo-level few-shot: [running] 5202/9784 (53.2%), ETA ~82min\\n  Process: run_qwen_repo_level.py (PID 3890761), GPU util 99%\\n\\n=== DISK ===\\n/root/autodl-tmp: 74% used (185G/250G), 66G available\\n```\\n\\nKey observations:\\n- CLS s123 (74.6%) is outperforming CLS v4 (70.9%) significantly\\n- CWM s123 (62.9%) is outperforming CWM s42 (58.1%) by ~5 points\\n- CWM evals are very slow (batch_size=1, generation mode) — ~28-30h remaining\\n- Home server Qwen3 repo-level baseline should finish in ~1.5h\"}}, \"error\": null, \"me
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 101
}
```

</details>

---


## Round 90

## Round 90

8 recorded events


### User

_source line 602 · 2026-05-17T20:24:58.205671+00:00_

[Director 指令] CLS s123 eval (GPU 2, PID 665019) 目前没有 cron 监控。请给它加一个 10min 间隔 cron，完成后立即启动 CWM s42 epoch 2 eval。

同样给 CWM s42 (GPU 1, PID 662946) 和 CWM s123 (GPU 3, PID 668680) 各加一个 30min 间隔 cron（这两个还要跑 ~28h，不急）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "source": "director"
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-17T20:25:06.903468+00:00_

called mcp__agent-ml-research__register_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_cron</summary>

```json
{
  "exp_id": "deepseek-cls-repo-s123",
  "server": "seetacloud-westd-4x5090",
  "pid": "665019",
  "project": "exec-sim-repair-verifier",
  "interval_seconds": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__register_cron",
  "tool_args": {
    "exp_id": "deepseek-cls-repo-s123",
    "server": "seetacloud-westd-4x5090",
    "pid": "665019",
    "project": "exec-sim-repair-verifier",
    "interval_seconds": "600"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-17T20:25:07.405638+00:00_

{"result":"{\"success\": true, \"data\": {\"registered\": {\"exp_id\": \"deepseek-cls-repo-s123\", \"server\": \"seetacloud-westd-4x5090\", \"pid\": \"665019\", \"wandb_run_id\": null, \"log_path\": null, \"interval_seconds\": 600, \"project\": \"exec-sim-repair-verifier\", \"tracked_metrics\": null, \"chat_id\": null, \"hooks\": null, \"last_checked\": null, \"created_at\": \"2026-05-17T20:25:06.915Z\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__register_cron",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-17T20:25:08.309188+00:00_

called mcp__agent-ml-research__register_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_cron</summary>

```json
{
  "exp_id": "deepseek-cwm-repo-s42-epoch2-eval",
  "server": "seetacloud-westd-4x5090",
  "pid": "662946",
  "project": "exec-sim-repair-verifier",
  "interval_seconds": "1800"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__register_cron",
  "tool_args": {
    "exp_id": "deepseek-cwm-repo-s42-epoch2-eval",
    "server": "seetacloud-westd-4x5090",
    "pid": "662946",
    "project": "exec-sim-repair-verifier",
    "interval_seconds": "1800"
  }
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-17T20:25:08.761972+00:00_

{"result":"{\"success\": true, \"data\": {\"registered\": {\"exp_id\": \"deepseek-cwm-repo-s42-epoch2-eval\", \"server\": \"seetacloud-westd-4x5090\", \"pid\": \"662946\", \"wandb_run_id\": null, \"log_path\": null, \"interval_seconds\": 1800, \"project\": \"exec-sim-repair-verifier\", \"tracked_metrics\": null, \"chat_id\": null, \"hooks\": null, \"last_checked\": null, \"created_at\": \"2026-05-17T20:25:08.369Z\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__register_cron",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-17T20:25:09.063617+00:00_

called mcp__agent-ml-research__register_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_cron</summary>

```json
{
  "exp_id": "deepseek-cwm-repo-s123",
  "server": "seetacloud-westd-4x5090",
  "pid": "668680",
  "project": "exec-sim-repair-verifier",
  "interval_seconds": "1800"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__register_cron",
  "tool_args": {
    "exp_id": "deepseek-cwm-repo-s123",
    "server": "seetacloud-westd-4x5090",
    "pid": "668680",
    "project": "exec-sim-repair-verifier",
    "interval_seconds": "1800"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-17T20:25:09.215023+00:00_

{"result":"{\"success\": true, \"data\": {\"registered\": {\"exp_id\": \"deepseek-cwm-repo-s123\", \"server\": \"seetacloud-westd-4x5090\", \"pid\": \"668680\", \"wandb_run_id\": null, \"log_path\": null, \"interval_seconds\": 1800, \"project\": \"exec-sim-repair-verifier\", \"tracked_metrics\": null, \"chat_id\": null, \"hooks\": null, \"last_checked\": null, \"created_at\": \"2026-05-17T20:25:09.103Z\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__register_cron",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 609 · 2026-05-17T20:25:15.660159+00:00_

已注册 3 个 cron：
- `deepseek-cls-repo-s123` (PID 665019, 10min) — 完成后立即启动 CWM s42 epoch 2 eval
- `deepseek-cwm-repo-s42-epoch2-eval` (PID 662946, 30min) — 监控 CWM s42 epoch 3 eval
- `deepseek-cwm-repo-s123` (PID 668680, 30min) — 监控 CWM s123 eval

加上已有的 `deepseek-cls-repo-v4` (PID 664774, 10min)，4 个进程全部有监控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8"
}
```

</details>

---


## Round 91

## Round 91

3 recorded events


### User

_source line 610 · 2026-05-17T20:56:08.289053+00:00_

[Director 指令] Home 5090 状态确认：当前跑的 3-shot repo baseline 是我之前安排的任务还是残留进程？请 nvidia-smi 确认 PID 和进程内容。如果是我安排的 baseline，预计多久完成？完成后这张卡下一个任务是什么？

请简要汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "source": "director"
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-17T20:56:19.151107+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "check:home-gpu-quick",
  "project": "exec-sim-repair-verifier",
  "task_prompt": "SSH 到 home-1x5090，快速确认当前 GPU 进程：\n\n```bash\nnvidia-smi\nps -p $(nvidia-smi --query-compute-apps=pid --format=csv,noheader) -o pid,etime,args --no-headers 2>/dev/null\n```\n\n汇报：PID、进程命令、运行时长、GPU 利用率。一句话总结即可。",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "check:home-gpu-quick",
    "project": "exec-sim-repair-verifier",
    "task_prompt": "SSH 到 home-1x5090，快速确认当前 GPU 进程：\n\n```bash\nnvidia-smi\nps -p $(nvidia-smi --query-compute-apps=pid --format=csv,noheader) -o pid,etime,args --no-headers 2>/dev/null\n```\n\n汇报：PID、进程命令、运行时长、GPU 利用率。一句话总结即可。",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---


### Tool result

_source line 612 · 2026-05-17T20:56:25.233399+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_check_home-gpu-quick_20260517T205619\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/logs/workers/worker_check_home-gpu-quick_20260517T205619.log\", \"setup_data\": {}, \"message\": \"Worker worker_check_home-gpu-quick_20260517T205619 started. Use get_worker_status('worker_check_home-gpu-quick_20260517T205619') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 6082
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 613 · 2026-05-17T20:56:57.724659+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 614 · 2026-05-17T20:57:56.554199+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- seetacloud GPU 分配：cuda:0/1/2/3 全部在本项目白名单内
- CWM eval 必须 max_new_tokens=512（M003 硬约束），CLS eval 必须 max_seq_length=8192（与 Qwen3 一致）
- DeepSeek CWM repo-level 必须用 last-epoch checkpoint（eval_loss=NaN 无法 val-select）
- --no_wandb 训练的 cron 会产生 false positive（sentinel 检测依赖 W&B heartbeat）——**不要信 cron 的"进程退出"通知**，必须 SSH 确认 PID 存活
- cwm-repo-s123 registry 状态被错误标记 DONE/failed（无法回退），实际训练已死（epoch 2 止步），eval 用 checkpoint-8844
- CLS v5 retrain 命名避免与被 kill 的 v4 混淆，output_dir=checkpoints_deepseek_cls_repo_v5/

### 2. 🖥️ 基础设施快照
**seetacloud-westd-4x5090**（4×RTX 5090 32GB）：
- 工作目录：`/home/sonny/exec-sim-repair-verifier/`
- 数据：`data/swebench_full/swebench_{train,val,test}.jsonl`
- 模型：`/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- Checkpoints: `/root/autodl-tmp/checkpoints_deepseek_{cls,cwm}_repo_{v4,v5,s123}/`
- Eval 脚本：`eval_repo_cls.py`（CLS）、`eval_repo_cwm.py`（CWM）
- Conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 磁盘：66G 可用（需关注，4 个 eval 同时写）

活跃进程（seetacloud）：
- GPU 0: PID 664774, tmux=cls-v4-eval-8192, CLS v4 eval (ckpt-4422, seq8192), ~40% done
- GPU 1: PID 662946, 无 tmux（stdout→log）, CWM s42 eval (best=ckpt-13266, tokens512), ~12% done
- GPU 2: PID 665019, tmux=cls-s123-eval-8192, CLS s123 eval (best, seq8192), ~35% done
- GPU 3: PID 668680, tmux=cwm-s123-eval, CWM s123 eval (ckpt-8844, tokens512), ~9% done

Crons：
- deepseek-cls-repo-v4 (PID 664774, 10min)
- deepseek-cls-repo-s123 (PID 665019, 10min)
- deepseek-cwm-repo-s42-epoch2-eval (PID 662946, 30min)
- deepseek-cwm-repo-s123 (PID 668680, 30min)

**home-1x5090**（1×RTX 5090 32GB）：
- Qwen3-8B 模型在本地
- 正在跑 repo-level 3-shot baseline（PID 3890761, ~53% done, ETA ~80min）
- Worker worker_check_home-gpu-quick_20260517T205619 待回调

### 3. 📊 当前状态
刚完成：注册 4 个 cron 监控所有 overnight eval 进程。向 Director 确认了 cron 不会干扰进程。

等待中：
- worker_check_home-gpu-quick（确认 home GPU 进程）— 即将回调
- CLS v4 eval cron 通知（~6h 后完成）→ 触发 v5 retrain
- CLS s123 eval cron 通知（~7h 后完成）→ 触发 CWM s42 epoch 2 eval
- Home 3-shot repo baseline 完成（~80min）→ 汇报结果
- CWM eval 两个都要 ~28-30h（后天）

Registry 关键实验：
- deepseek-cls-repo-v5: PREPARING（已注册 hypothesis，命令已准备，等 GPU 0 释放）
- deepseek-cwm-repo-s42-epoch2-eval: PREPARING（命令已准备，等 GPU 2 释放）

### 4. 📋 待办（条件触发式）
- CLS v4 eval (GPU 0) 完成 cron 通知 → 记录 accuracy/unparseable → submit_training_job deepseek-cls-repo-v5 on cuda:0（命令见下方）
- CLS s123 eval (GPU 2) 完成 cron 通知 → 记录 accuracy/unparseable → 启动 CWM s42 epoch 2 eval on cuda:2
- Home 3-shot repo baseline 完成 → 注册 artifact + 汇报 Director
- CWM s42 eval (GPU 1) 完成 → 记录 accuracy/unparseable/parseable-only → 汇报 Director
- CWM s123 eval (GPU 3) 完成 → 同上
- CWM s42 epoch 2 eval 完成 → 对比 epoch 3 (58.2%) 判断过拟合

**CLS v5 retrain 命令**：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --train_file swebench_full/swebench_train.jsonl --val_file swebench_full/swebench_val.jsonl --task cls --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 8 --lr 2e-4 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/ --run_name deepseek-cls-repo-v5
```

**CWM s42 epoch 2 eval 命令**：
```bash
CUDA_VISIBLE_DEVICES=2 python3 /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-8844/ --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir /home/sonny/exec-sim-repair-verifier/data/swebench_full --device cuda:0 --batch_size 1 --max_seq_length 4096 --max_new_tokens 512 --output eval_deepseek_cwm_repo_s42_ep2.json --pred_output eval_deepseek_cwm_repo_s42_ep2_predictions.jsonl --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_ep2_test --split test
```

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 ARR May 25 投稿（剩 8 天），Table 4 DeepSeek repo-level 数字是最后缺失块
- D116: Design space characterization framing — CLS vs CWM vs TRAJ 三种 formulation 比较
- C2 narrative: CWM repo-level unparseable rate + accuracy 决定 Path A（CWM works at repo）vs Path B（CWM fails at repo）
- 当前证据倾向 Path B: CWM s42 running_acc 58.2% 远低于 CLS s123 的 74.5%
- CWM epoch 2 vs epoch 3 对比（D124）：s123(ep2)=62.6% vs s42(ep3)=58.2%，gap 4.4pp 暗示过拟合
- CLS v4 (ckpt-4422, epoch 2) running_acc 70.9% < s123 (best) 74.5%，因为 v4 只有 epoch 2 checkpoint（训练被 kill）→ 所以 Director 要求 v5 从零完整训练

易错点：
- 不要信 cron "进程退出" 通知——必须 SSH 确认（--no_wandb 导致 false positive，本 session 已踩坑 3 次）
- CWM eval 脚本用 `--device cuda:0` 但实际 GPU 由 CUDA_VISIBLE_DEVICES 控制映射
- Registry deepseek-cwm-repo-s123 状态 DONE/failed 是错误的（无法修复），实际 eval 在跑
- Home GPU 空闲时找活干（Director L1：GPU 空着=失职）
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b2cf3b1eba4db851529b6a1a7a34c4e8"
}
```

</details>

---
