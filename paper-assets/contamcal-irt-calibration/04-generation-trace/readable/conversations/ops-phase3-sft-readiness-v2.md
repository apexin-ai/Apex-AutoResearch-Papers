# ops phase3 sft readiness v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_ops_phase3-sft-readiness-v2_20260514T025400.jsonl`
- **Structured JSON:** [`94c522f32ebb728ae1c7.json`](../../sessions/94/94c522f32ebb728ae1c7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-14T02:58:13.158976+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T02:58:13.161533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "ToolSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T02:58:13.161910+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T02:58:13.162247+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## Phase 3 GPU 调度优先级 (Director 2026-05-14)\\n**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025/d050。**\\n优先级从高到低：\\n1. 1.5B d005 + d100 — GPU 0/5 完成 0.5B SFT 后立即接上\\n2. 3B d005 + d100 — 等有 GPU 空出\\n3. 0.5B d025 + d050 — eval GPU (1/2/4) 完成后可用\\n4. 1.5B d025 + d050 — 填充 dose-response 曲线\\n5. 3B d025 + d050 — 最后填充\\n\\n**免审批：** GPU 空出时直接按优先级启动，事后汇报。\\n\\n**Why:** 即使时间不够，至少有 3 sizes × 2 dosages 的 dose-response 数据足以支撑 paper core claim。\\n\\n## SFT 训练参数经验 (2026-05-14)\\n- 6 个 0% baseline 全部成功（0.5B/1.5B/3B × s42/s123）\\n- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)\\n- LoRA r=16 alpha=32, 1 epoch\\n- **0.5B**: batch_size=4, grad_accum=4 可用\\n- **1.5B**: 必须 batch_size=1, grad_accum=16（batch_size=2 在 24GB 4090D 上 OOM，exp_001_sft_d100_15B 事故教训）\\n- **3B**: 必须 batch_size=1, grad_accum=16\\n- --gpu 参数必须匹配物理 GPU 编号（v1/v2 OOM 教训：--gpu 0 导致 CUDA_VISIBLE_DEVICES 覆盖）\\n\\n## Dosage 数据版本 (2026-05-14)\\n- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）\\n- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases\\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\\n- 当前跑的 d005/d100 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition（D010 决策）\\n- D012 ablation: d100_qc_only 仅用 QC pass (7,547/16,697 = 45.2%)，脚本就绪未执行\\n\\n## Eval Pipeline 能力 (2026-05-14)\\n- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅\\n- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅ — IRT 分析可直接用\\n- 批量链式触发: `run_exp001.sh --phase all` ✅\\n- 单 job 链式触发: `train_and_eval.sh` (新建) ✅\\n- Dry-run: `--max-samples N` 参数已补 ✅\\n- ⚠️ Bug: `load_paraphrased_benchmark` 中 `'list' object has no attribute 'get'`，paraphrased eval 受影响，需后续修复\\n- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`\\n\\n## exp_005 γ bias 诊断结论 (2026-05-14)\\n- **
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T02:58:13.162549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T02:58:13.162801+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    50826 /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\\n    54133 /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\\n    58266 /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl\\n    66533 /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\\n   229758 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T02:58:13.163013+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -d /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/ /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B/ /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -d /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/ /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B/ /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T02:58:13.163219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/\\n/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B/\\n/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T02:58:13.165482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -d /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/ /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -d /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/ /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T02:58:13.165703+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/\\n/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T02:58:13.165903+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T02:58:13.166106+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090 D, 10055 MiB, 24564 MiB, 41 %\\n1, NVIDIA GeForce RTX 4090 D, 12620 MiB, 24564 MiB, 100 %\\n2, NVIDIA GeForce RTX 4090 D, 7330 MiB, 24564 MiB, 99 %\\n3, NVIDIA GeForce RTX 4090 D, 8957 MiB, 24564 MiB, 55 %\\n4, NVIDIA GeForce RTX 4090 D, 10365 MiB, 24564 MiB, 47 %\\n5, NVIDIA GeForce RTX 4090 D, 5829 MiB, 24564 MiB, 43 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T02:58:13.166302+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps aux --cols 300 --no-headers -ww"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps aux --cols 300 --no-headers -ww"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T02:58:13.168659+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  2628 ?        Ss   May12   0:00 bash /init/boot/boot.sh\\nroot        801  3.1  0.0 724896 21592 ?        Sl   May12  76:01 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        820  0.0  0.0  15444  8436 ?        S    May12   0:02 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        821  0.0  0.0 4147752 79024 ?       Sl   May12   1:51 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        822  0.0  0.0 191548 103764 ?       S    May12   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        823  0.0  0.0 2795776 18828 ?       Sl   May12   0:37 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        824  0.1  0.0 3016972 20536 ?       Sl   May12   4:31 proxy -c /init/proxy/proxy.ini\\nroot        826  0.3  0.0 6526400 104308 ?      Sl   May12   7:35 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        932  0.0  0.0 26177944 9896 ?       Sl   May12   2:08 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_jfe2b4s0/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_jfe2b4s0/startup_error\\nroot     171779  0.0  0.0  16692 10836 ?        Ss   May13   0:03 sshd: root@notty\\nroot     179620  0.0  0.0  16692 10712 ?        Ss   01:08   0:03 sshd: root@notty\\nroot     179657  0.0  0.0  16692 10756 ?        Ss   01:08   0:03 sshd: root@notty\\nroot     180149  0.0  0.0  16692 10568 ?        Ss   01:17   0:03 sshd: root@notty\\nroot     180471  0.0  0.0  16808 10868 ?        Ss   01:23   0:07 sshd: root@notty\\nroot     208932  0.0  0.0   6364  4060 ?        Ss   03:37   0:01 tmux new-session -d -s exp_001_sft_0pct_05B rm -f /tm
…[truncated 6385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T02:58:13.169053+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -d /root/autodl-tmp/exp001/checkpoints/Qwen2.5-*_d*_s42/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -d /root/autodl-tmp/exp001/checkpoints/Qwen2.5-*_d*_s42/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T02:58:13.169273+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T02:58:13.169494+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps aux --cols 300 --no-headers -ww"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps aux --cols 300 --no-headers -ww"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T02:58:13.169821+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  2628 ?        Ss   May12   0:00 bash /init/boot/boot.sh\\nroot        801  3.1  0.0 724896 21592 ?        Sl   May12  76:02 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        820  0.0  0.0  15444  8436 ?        S    May12   0:02 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        821  0.0  0.0 4147752 79024 ?       Sl   May12   1:51 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        822  0.0  0.0 191548 103764 ?       S    May12   0:03 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        823  0.0  0.0 2795776 18828 ?       Sl   May12   0:37 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        824  0.1  0.0 3016972 20536 ?       Sl   May12   4:31 proxy -c /init/proxy/proxy.ini\\nroot        826  0.3  0.0 6526400 104308 ?      Sl   May12   7:35 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        932  0.0  0.0 26177944 9896 ?       Sl   May12   2:08 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_jfe2b4s0/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_jfe2b4s0/startup_error\\nroot     171779  0.0  0.0  16692 10836 ?        Ss   May13   0:03 sshd: root@notty\\nroot     179620  0.0  0.0  16692 10712 ?        Ss   01:08   0:03 sshd: root@notty\\nroot     179657  0.0  0.0  16692 10756 ?        Ss   01:08   0:03 sshd: root@notty\\nroot     180149  0.0  0.0  16692 10568 ?        Ss   01:17   0:03 sshd: root@notty\\nroot     180471  0.0  0.0  16808 10868 ?        Ss   01:23   0:07 sshd: root@notty\\nroot     208932  0.0  0.0   6364  4060 ?        Ss   03:37   0:01 tmux new-session -d -s exp_001_sft_0pct_05B rm -f /tm
…[truncated 6385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T02:58:13.170126+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/checkpoints/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/checkpoints/"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T02:58:13.172369+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/contamcal-irt-calibration/exp001/train_sft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/contamcal-irt-calibration/exp001/train_sft.py"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T02:58:13.172603+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"add_argument\" /root/contamcal-irt-calibration/exp001/train_sft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"add_argument\" /root/contamcal-irt-calibration/exp001/train_sft.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T02:58:13.172810+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen2.5-0.5B_d000_s123\\nQwen2.5-0.5B_d000_s42\\nQwen2.5-0.5B_d005_s42\\nQwen2.5-0.5B_d100_s42\\nQwen2.5-1.5B_d000_s123\\nQwen2.5-1.5B_d000_s42\\nQwen2.5-1.5B_d100_s42\\nQwen2.5-3B_d000_s123\\nQwen2.5-3B_d000_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T02:58:13.173034+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLoRA SFT training for controlled contamination experiments.\\n\\nTrains Qwen2.5-{0.5B,1.5B,3B} with LoRA on mixed SFT data at different\\ncontamination dosage levels. Saves LoRA adapter then merges to full model.\\n\\nInput:  JSONL training data from prepare_sft_data.py\\nOutput: LoRA adapter + merged full model checkpoints\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nfrom pathlib import Path\\n\\nimport torch\\nfrom datasets import load_dataset\\nfrom peft import LoraConfig, get_peft_model, TaskType\\nfrom transformers import (\\n    AutoModelForCausalLM,\\n    AutoTokenizer,\\n    TrainingArguments,\\n)\\nfrom trl import SFTTrainer, SFTConfig\\n\\nlogger = logging.getLogger(__name__)\\n\\nHF_HOME = os.environ.get(\\\"HF_HOME\\\", \\\"/root/autodl-tmp/.hf_cache\\\")\\nos.environ[\\\"HF_HOME\\\"] = HF_HOME\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T02:58:13.173288+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"85:    parser.add_argument(\\\"--model-name\\\", type=str, required=True,\\n87:    parser.add_argument(\\\"--data-path\\\", type=str, required=True,\\n89:    parser.add_argument(\\\"--output-dir\\\", type=str, required=True,\\n91:    parser.add_argument(\\\"--seed\\\", type=int, default=42,\\n93:    parser.add_argument(\\\"--gpu\\\", type=str, default=None,\\n95:    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048,\\n97:    parser.add_argument(\\\"--lora-r\\\", type=int, default=DEFAULT_LORA_CONFIG[\\\"r\\\"],\\n99:    parser.add_argument(\\\"--lora-alpha\\\", type=int, default=DEFAULT_LORA_CONFIG[\\\"lora_alpha\\\"],\\n101:    parser.add_argument(\\\"--epochs\\\", type=int, default=1, help=\\\"Number of training epochs\\\")\\n102:    parser.add_argument(\\\"--batch-size\\\", type=int, default=4, help=\\\"Per-device batch size\\\")\\n103:    parser.add_argument(\\\"--grad-accum\\\", type=int, default=4, help=\\\"Gradient accumulation steps\\\")\\n104:    parser.add_argument(\\\"--lr\\\", type=float, default=2e-4, help=\\\"Learning rate\\\")\\n105:    parser.add_argument(\\\"--merge\\\", action=\\\"store_true\\\",\\n107:    parser.add_argument(\\\"--cache-dir\\\", type=str, default=\\\"/root/autodl-tmp/.hf_cache\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T02:58:13.173622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"DEFAULT_LORA\" /root/contamcal-irt-calibration/exp001/train_sft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"DEFAULT_LORA\" /root/contamcal-irt-calibration/exp001/train_sft.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T02:58:13.173849+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"32:DEFAULT_LORA_CONFIG = {\\n97:    parser.add_argument(\\\"--lora-r\\\", type=int, default=DEFAULT_LORA_CONFIG[\\\"r\\\"],\\n99:    parser.add_argument(\\\"--lora-alpha\\\", type=int, default=DEFAULT_LORA_CONFIG[\\\"lora_alpha\\\"],\\n139:        lora_dropout=DEFAULT_LORA_CONFIG[\\\"lora_dropout\\\"],\\n140:        target_modules=DEFAULT_LORA_CONFIG[\\\"target_modules\\\"],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T02:58:13.174051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T02:58:13.174256+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T02:58:13.176550+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"251924, GPU-52bfebf5-3ba8-8f6e-ae36-56511cce901f, 10046 MiB, python\\n249294, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 8948 MiB, python\\n255322, GPU-466bc8fe-796f-8068-9660-0fb52de3681b, 3658 MiB, python\\n266521, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 3658 MiB, python\\n266790, GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54, 3658 MiB, python\\n242591, GPU-c30258a6-4c47-f7a8-7b0c-4c5cbdc3c1c3, 8948 MiB, python\\n243300, GPU-ec1378f2-6e00-01ce-6bf6-c5e8081f887b, 10356 MiB, python\\n250610, GPU-f1a0b9ee-87a0-41a4-a300-b3cb3c870263, 5820 MiB, python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T02:58:13.176762+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"lora_adapter\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T02:58:13.176978+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp001/train_sft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp001/train_sft.py"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T02:58:13.177161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /proc/251924/cmdline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /proc/251924/cmdline"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T02:58:13.177585+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLoRA SFT training for controlled contamination experiments.\\n\\nTrains Qwen2.5-{0.5B,1.5B,3B} with LoRA on mixed SFT data at different\\ncontamination dosage levels. Saves LoRA adapter then merges to full model.\\n\\nInput:  JSONL training data from prepare_sft_data.py\\nOutput: LoRA adapter + merged full model checkpoints\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nfrom pathlib import Path\\n\\nimport torch\\nfrom datasets import load_dataset\\nfrom peft import LoraConfig, get_peft_model, TaskType\\nfrom transformers import (\\n    AutoModelForCausalLM,\\n    AutoTokenizer,\\n    TrainingArguments,\\n)\\nfrom trl import SFTTrainer, SFTConfig\\n\\nlogger = logging.getLogger(__name__)\\n\\nHF_HOME = os.environ.get(\\\"HF_HOME\\\", \\\"/root/autodl-tmp/.hf_cache\\\")\\nos.environ[\\\"HF_HOME\\\"] = HF_HOME\\n\\nDEFAULT_LORA_CONFIG = {\\n    \\\"r\\\": 16,\\n    \\\"lora_alpha\\\": 32,\\n    \\\"lora_dropout\\\": 0.05,\\n    \\\"target_modules\\\": [\\n        \\\"q_proj\\\", \\\"k_proj\\\", \\\"v_proj\\\", \\\"o_proj\\\",\\n        \\\"gate_proj\\\", \\\"up_proj\\\", \\\"down_proj\\\",\\n    ],\\n    \\\"task_type\\\": \\\"CAUSAL_LM\\\",\\n    \\\"bias\\\": \\\"none\\\",\\n}\\n\\nDEFAULT_TRAINING_ARGS = {\\n    \\\"num_train_epochs\\\": 1,\\n    \\\"per_device_train_batch_size\\\": 4,\\n    \\\"gradient_accumulation_steps\\\": 4,\\n    \\\"learning_rate\\\": 2e-4,\\n    \\\"warmup_ratio\\\": 0.05,\\n    \\\"bf16\\\": True,\\n    \\\"logging_steps\\\": 10,\\n    \\\"save_strategy\\\": \\\"epoch\\\",\\n    \\\"save_total_limit\\\": 1,\\n    \\\"report_to\\\": \\\"none\\\",\\n    \\\"optim\\\": \\\"adamw_torch\\\",\\n    \\\"lr_scheduler_type\\\": \\\"cosine\\\",\\n    \\\"max_grad_norm\\\": 1.0,\\n    \\\"dataloader_num_workers\\\": 4,\\n    \\\"remove_unused_columns\\\": False,\\n}\\n\\n\\ndef formatting_func(example):\\n    \\\"\\\"\\\"Format chat messages into
…[truncated 7442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T02:58:13.177864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"python\\u0000/root/contamcal-irt-calibration/exp001/train_sft.py\\u0000--model-name\\u0000/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B\\u0000--data-path\\u0000/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\\u0000--output-dir\\u0000/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42\\u0000--seed\\u000042\\u0000--gpu\\u00000\\u0000--batch-size\\u00001\\u0000--grad-accum\\u000016\\u0000--cache-dir\\u0000/root/autodl-tmp/.hf_cache\\u0000\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T02:58:13.178106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter/"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T02:58:13.178294+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T02:58:13.180661+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "content": "# Memory — contamcal-irt-calibration\n\n## Phase 3 GPU 调度优先级 (Director 2026-05-14)\n**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025/d050。**\n优先级从高到低：\n1. 1.5B d005 + d100 — GPU 0/5 完成 0.5B SFT 后立即接上\n2. 3B d005 + d100 — 等有 GPU 空出\n3. 0.5B d025 + d050 — eval GPU (1/2/4) 完成后可用\n4. 1.5B d025 + d050 — 填充 dose-response 曲线\n5. 3B d025 + d050 — 最后填充\n\n**免审批：** GPU 空出时直接按优先级启动，事后汇报。\n\n**Why:** 即使时间不够，至少有 3 sizes × 2 dosages 的 dose-response 数据足以支撑 paper core claim。\n\n## SFT 训练参数经验 (2026-05-14)\n- 6 个 0% baseline 全部成功（0.5B/1.5B/3B × s42/s123）\n- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)\n- LoRA r=16 alpha=32, 1 epoch\n- **0.5B**: batch_size=4, grad_accum=4 可用\n- **1.5B**: 必须 batch_size=1, grad_accum=16（batch_size=2 在 24GB 4090D 上 OOM，exp_001_sft_d100_15B 事故教训）\n- **3B**: 必须 batch_size=1, grad_accum=16\n- --gpu 参数必须匹配物理 GPU 编号（v1/v2 OOM 教训：--gpu 0 导致 CUDA_VISIBLE_DEVICES 覆盖）\n\n## Dosage 数据版本 (2026-05-14)\n- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）\n- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\n- 当前跑的 d005/d100 使用 ALL paraphrases（含 QC fail），属于 \"noisy contamination\" condition（D010 决策）\n- D012 ablation: d100_qc_only 仅用 QC pass (7,547/16,697 = 45.2%)，脚本就绪未执行\n\n## Eval Pipeline 能力 (2026-05-14)\n- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅\n- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅ — IRT 分析可直接用\n- 批量链式触发: `run_exp001.sh --phase all` ✅\n- 单 job 链式触发: `train_and_eval.sh` (新建) ✅\n- Dry-run: `--max-samples N` 参数已补 ✅\n- ⚠️ Bug: `load_paraphrased_benchmark` 中 `'list' object has no attribute 'get'`，paraphrased eval 受影响，需后续修复\n- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`\n\n## exp_005 γ bias 诊断结论 (2026-05-14)\n- **两个诊断实验均确认 γ bias 严重**：\n  - simple model: γ_mean=0.7877, rel_bias=+57.5%, CI 不覆盖真值 0.5\n  - analytic ME model: γ_mean=0.7959, rel_bias=+59.2%, CI [0.556, 1.060] 不覆盖真值 0.5\n  - 两者 R-hat=1.006, 0 divergences — 收敛良好但结果有偏\n- **结论：bias 根因不在 measurement error 处理方式**，可能是模型 identifiability / 参数化问题（σ_e=0.1 场景下）\n- exp_004 sim sweep 结果可能揭示 bias 与 N_models / signal quality 的关系\n- 不阻塞 Phase 3 主实验链\n\n## IRT Pipeline 方法论决策 (Director 2026-05-14)\n- **论文结果必须用 CmdStanPy (Bayesian MCMC)**，不能用 PyTorch MLE\n- CmdStanPy 1.3.0 + CmdStan 2.38.0 已装，`run_irt_stan.py` 就绪 ✅\n- Synthetic validation: 0 divergences, R-hat=1.006, ESS=1402, gamma posterior SD=0.137\n- PyTorch MLE 版本 `run_irt_calibration.py` 保留作 debug（θ recovery 0.93, γ recovery 0.63）\n- 原因：MLE Hessian SE 失效 (49/50 items b_se=10000.0)，gamma_corr 退化 (0.629 vs Stan 0.94)\n- 复用 mvp_sim 已验证的 Stan model 文件 (contam_irt_4pl_simple.stan)\n\n## Phase 3 SFT 提交计划 (2026-05-14 检查)\n\n### 就绪检查结果\n\n**Dosage 数据文件** ✅ 全部存在：\n| 文件 | 行数 |\n|------|------|\n| sft_dosage_005.jsonl | 50,826 |\n| sft_dosage_025.jsonl | 54,133 |\n| sft_dosage_050.jsonl | 58,266 |\n| sft_dosage_100.jsonl | 66,533 |\n\n**基础模型** ✅ 全部存在：Qwen2.5-0.5B, 1.5B, 3B at `/root/autodl-tmp/.hf_cache/Qwen/`\n\n**已完成 checkpoint**：\n| Checkpoint | 状态 |\n|-----------|------|\n| Qwen2.5-0.5B_d000_s42 | ✅ |\n| Qwen2.5-0.5B_d000_s123 | ✅ |\n| Qwen2.5-0.5B_d005_s42 | ✅ |\n| Qwen2.5-0.5B_d100_s42 | ✅ |\n| Qwen2.5-1.5B_d000_s42 | ✅ |\n| Qwen2.5-1.5B_d000_s123 | ✅ |\n| Qwen2.5-1.5B_d100_s42 | 🏃 GPU 0 (PID 251924, lora_adapter 为空 = 尚未保存) |\n| Qwen2.5-3B_d000_s42 | ✅ |\n| Qwen2.5-3B_d000_s123 | ✅ |\n\n**GPU 状态** (2026-05-14 ~11:00 UTC):\n| GPU | 显存占用 | 利用率 | 任务 |\n|-----|---------|--------|------|\n| 0 | 10055/24564 MiB | 41% | 1.5B d100 SFT (PID 251924) |\n| 1 | 12620/24564 MiB | 100% | eval jobs |\n| 2 | 7330/24564 MiB | 99% | eval jobs |\n| 3 | 8957/24564 MiB | 55% | eval jobs |\n| 4 | 10365/24564 MiB | 47% | eval jobs |\n| 5 | 5829/24564 MiB | 43% | eval jobs |\n\n### 待做 SFT 列表 (8 jobs)\n\n脚本参数格式：`--model-name`/`--data-path`/`--batch-size`/`--grad-accum`/`--lr`/`--epochs`（hyphen 格式）。\n\n#### 1. 1.5B d005 — 最高优先 (~101min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 2. 3B d100 — 次高 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 3. 3B d005 — 次高 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 4. 0.5B d025 — 中 (~53min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 5. 0.5B d050 — 中 (~53min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d050_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 6. 1.5B d025 — 低 (~101min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 7. 1.5B d050 — 低 (~101min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d050_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 8. 3B d025 — 最低 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 9. 3B d050 — 最低 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d050_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n### 总预计时长\n- 全部 9 jobs 串行: ~53×2 + 101×3 + 214×4 = 1265 min ≈ 21h\n- 若并行 2 GPU: ~11h; 3 GPU: ~7h\n- 注意：提交前必须 `nvidia-smi` 检查目标 GPU 无同类进程 (C001 约束)\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "memory.md",
    "content": "# Memory — contamcal-irt-calibration\n\n## Phase 3 GPU 调度优先级 (Director 2026-05-14)\n**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025/d050。**\n优先级从高到低：\n1. 1.5B d005 + d100 — GPU 0/5 完成 0.5B SFT 后立即接上\n2. 3B d005 + d100 — 等有 GPU 空出\n3. 0.5B d025 + d050 — eval GPU (1/2/4) 完成后可用\n4. 1.5B d025 + d050 — 填充 dose-response 曲线\n5. 3B d025 + d050 — 最后填充\n\n**免审批：** GPU 空出时直接按优先级启动，事后汇报。\n\n**Why:** 即使时间不够，至少有 3 sizes × 2 dosages 的 dose-response 数据足以支撑 paper core claim。\n\n## SFT 训练参数经验 (2026-05-14)\n- 6 个 0% baseline 全部成功（0.5B/1.5B/3B × s42/s123）\n- 训练时长：0.5B ~53min, 1.5B ~101min, 3B ~214min (单 4090D)\n- LoRA r=16 alpha=32, 1 epoch\n- **0.5B**: batch_size=4, grad_accum=4 可用\n- **1.5B**: 必须 batch_size=1, grad_accum=16（batch_size=2 在 24GB 4090D 上 OOM，exp_001_sft_d100_15B 事故教训）\n- **3B**: 必须 batch_size=1, grad_accum=16\n- --gpu 参数必须匹配物理 GPU 编号（v1/v2 OOM 教训：--gpu 0 导致 CUDA_VISIBLE_DEVICES 覆盖）\n\n## Dosage 数据版本 (2026-05-14)\n- 所有 dosage 文件于 May 14 07:16 重新生成 v3（含 MMLU+ARC+GSM8K）\n- 0% dosage = 纯 SlimOrca 50000 条，不含 paraphrases\n- data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533\n- 当前跑的 d005/d100 使用 ALL paraphrases（含 QC fail），属于 \"noisy contamination\" condition（D010 决策）\n- D012 ablation: d100_qc_only 仅用 QC pass (7,547/16,697 = 45.2%)，脚本就绪未执行\n\n## Eval Pipeline 能力 (2026-05-14)\n- 4 benchmarks: MMLU, GSM8K, ARC, HumanEval ✅\n- Item-level 输出: `per_item` in `eval_results.json` + `correctness_matrix.json` ✅ — IRT 分析可直接用\n- 批量链式触发: `run_exp001.sh --phase all` ✅\n- 单 job 链式触发: `train_and_eval.sh` (新建) ✅\n- Dry-run: `--max-samples N` 参数已补 ✅\n- ⚠️ Bug: `load_paraphrased_benchmark` 中 `'list' object has no attribute 'get'`，paraphrased eval 受影响，需后续修复\n- 输出路径: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/`\n\n## exp_005 γ bias 诊断结论 (2026-05-14)\n- **两个诊断实验均确认 γ bias 严重**：\n  - simple model: γ_mean=0.7877, rel_bias=+57.5%, CI 不覆盖真值 0.5\n  - analytic ME model: γ_mean=0.7959, rel_bias=+59.2%, CI [0.556, 1.060] 不覆盖真值 0.5\n  - 两者 R-hat=1.006, 0 divergences — 收敛良好但结果有偏\n- **结论：bias 根因不在 measurement error 处理方式**，可能是模型 identifiability / 参数化问题（σ_e=0.1 场景下）\n- exp_004 sim sweep 结果可能揭示 bias 与 N_models / signal quality 的关系\n- 不阻塞 Phase 3 主实验链\n\n## IRT Pipeline 方法论决策 (Director 2026-05-14)\n- **论文结果必须用 CmdStanPy (Bayesian MCMC)**，不能用 PyTorch MLE\n- CmdStanPy 1.3.0 + CmdStan 2.38.0 已装，`run_irt_stan.py` 就绪 ✅\n- Synthetic validation: 0 divergences, R-hat=1.006, ESS=1402, gamma posterior SD=0.137\n- PyTorch MLE 版本 `run_irt_calibration.py` 保留作 debug（θ recovery 0.93, γ recovery 0.63）\n- 原因：MLE Hessian SE 失效 (49/50 items b_se=10000.0)，gamma_corr 退化 (0.629 vs Stan 0.94)\n- 复用 mvp_sim 已验证的 Stan model 文件 (contam_irt_4pl_simple.stan)\n\n## Phase 3 SFT 提交计划 (2026-05-14 检查)\n\n### 就绪检查结果\n\n**Dosage 数据文件** ✅ 全部存在：\n| 文件 | 行数 |\n|------|------|\n| sft_dosage_005.jsonl | 50,826 |\n| sft_dosage_025.jsonl | 54,133 |\n| sft_dosage_050.jsonl | 58,266 |\n| sft_dosage_100.jsonl | 66,533 |\n\n**基础模型** ✅ 全部存在：Qwen2.5-0.5B, 1.5B, 3B at `/root/autodl-tmp/.hf_cache/Qwen/`\n\n**已完成 checkpoint**：\n| Checkpoint | 状态 |\n|-----------|------|\n| Qwen2.5-0.5B_d000_s42 | ✅ |\n| Qwen2.5-0.5B_d000_s123 | ✅ |\n| Qwen2.5-0.5B_d005_s42 | ✅ |\n| Qwen2.5-0.5B_d100_s42 | ✅ |\n| Qwen2.5-1.5B_d000_s42 | ✅ |\n| Qwen2.5-1.5B_d000_s123 | ✅ |\n| Qwen2.5-1.5B_d100_s42 | 🏃 GPU 0 (PID 251924, lora_adapter 为空 = 尚未保存) |\n| Qwen2.5-3B_d000_s42 | ✅ |\n| Qwen2.5-3B_d000_s123 | ✅ |\n\n**GPU 状态** (2026-05-14 ~11:00 UTC):\n| GPU | 显存占用 | 利用率 | 任务 |\n|-----|---------|--------|------|\n| 0 | 10055/24564 MiB | 41% | 1.5B d100 SFT (PID 251924) |\n| 1 | 12620/24564 MiB | 100% | eval jobs |\n| 2 | 7330/24564 MiB | 99% | eval jobs |\n| 3 | 8957/24564 MiB | 55% | eval jobs |\n| 4 | 10365/24564 MiB | 47% | eval jobs |\n| 5 | 5829/24564 MiB | 43% | eval jobs |\n\n### 待做 SFT 列表 (8 jobs)\n\n脚本参数格式：`--model-name`/`--data-path`/`--batch-size`/`--grad-accum`/`--lr`/`--epochs`（hyphen 格式）。\n\n#### 1. 1.5B d005 — 最高优先 (~101min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 2. 3B d100 — 次高 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 3. 3B d005 — 次高 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 4. 0.5B d025 — 中 (~53min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 5. 0.5B d050 — 中 (~53min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d050_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 6. 1.5B d025 — 低 (~101min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 7. 1.5B d050 — 低 (~101min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d050_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 8. 3B d025 — 最低 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n#### 9. 3B d050 — 最低 (~214min)\n```\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d050_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\"\n```\n\n### 总预计时长\n- 全部 9 jobs 串行: ~53×2 + 101×3 + 214×4 = 1265 min ≈ 21h\n- 若并行 2 GPU: ~11h; 3 GPU: ~7h\n- 注意：提交前必须 `nvidia-smi` 检查目标 GPU 无同类进程 (C001 约束)\n"
  }
}
````

</details>

---

### Tool result

_source line 38 · 2026-05-14T02:58:13.181058+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T02:58:13.181307+00:00_

检查完成，结果汇总：

### 就绪状态

| 检查项 | 结果 |
|--------|------|
| Dosage 数据 (d005/025/050/100) | ✅ 全部存在 (50826/54133/58266/66533 行) |
| 基础模型 (0.5B/1.5B/3B) | ✅ 全部存在 |
| 0.5B d005 checkpoint | ✅ |
| 0.5B d100 checkpoint | ✅ |
| 1.5B d100 | 🏃 GPU 0 仍在训练 (PID 251924, lora_adapter 为空) |

### GPU 现状
所有 6 GPU 均在使用中：GPU 0 跑 1.5B d100 SFT，GPU 1-5 跑各种 eval jobs。

### 修正
- 脚本实际参数用 **hyphen 格式**：`--model-name`、`--data-path`、`--batch-size`、`--grad-accum`、`--lr`、`--epochs`（非 underscore）
- 待做 SFT 实际是 **9 jobs**（用户列表里 1.5B d100 虽有 checkpoint 目录但尚未完成，仍在训练）

完整的 9 条 submit command 已保存到 `memory.md` 的 "Phase 3 SFT 提交计划" section。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_phase3-sft-readiness-v2_20260514T025400"
}
```

</details>

---
