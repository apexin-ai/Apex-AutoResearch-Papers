# analysis eval postprune cka only 30 failure

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849.jsonl`
- **Structured JSON:** [`ea75cfbe4c3adc585d00.json`](../../sessions/ea/ea75cfbe4c3adc585d00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-17T23:19:57.639663+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,TaskOutput",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,TaskOutput",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T23:19:57.640110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T23:19:57.640482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -100 ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T23:19:57.640836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-18 06:00:36,064 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\\n2026-05-18 06:00:36,442 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-18 06:02:00,507 [INFO] Loading GSM8K test set...\\n'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-18 06:03:20,704 [WARNING] '[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\nRetrying in 1s [Retry 1/5].\\n2026-05-18 06:03:20,704 [WARNING] Retrying in 1s [Retry 1/5].\\nUsing the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\n2026-05-18 06:03:21,706 [WARNING] Using the latest cached version of the dataset since openai/gsm8k couldn't be found on the Hugging Face Hub\\nFound the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Sun May 17 13:00:54 2026).\\n2026-05-18 06:03:21,707 [WARNING] Found the latest cached dataset configuration 'main' at /root/.cache/huggingface/datasets/openai___gsm8k/main/0.0.0/740312add88f781978c0658806c59bc2815b9866 (last modified on Sun May 17 13:00:54 2026).\\n2026-05-18 06:03:21,720 [INFO] Evaluating on 200 test samples\\n2026-05-18 06:03:21,721 [INFO] Generation config: do_sample=False, temperature=0.0\\n\\rEvaluating:   0%|          | 0/200 [00:00<?, ?it/s]\\rEvaluating:   0%|          | 1/200 [01:35<5:18:04, 95.90s/it]\\rEvaluating:   1%|          | 2/200 [03:11<5:15:23, 95.57s/it]\\rEvaluating:   2%|▏         | 3/200 [04:46<5:13:41, 95.54s/it]\\rEvaluating:   2%|▏         | 4/200 [06:22<5:12:08, 95.55s/it]\\rEvaluating:   2%|▎         | 5/200 [07:57<5:
…[truncated 3556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T23:19:57.641088+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-11672",
  "command": "ps aux | grep eval_math500; echo \"---TMUX---\"; tmux ls 2>&1; echo \"---RESULTS---\"; ls -la /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_unpruned.json 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-11672",
    "command": "ps aux | grep eval_math500; echo \"---TMUX---\"; tmux ls 2>&1; echo \"---RESULTS---\"; ls -la /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_unpruned.json 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T23:19:57.641403+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"root       2506  0.0  0.0   6328  4044 ?        Ss   May17   0:01 tmux new-session -d -s eval_math500_unpruned bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_unpruned.json --seed 42 --max_new_tokens 4096 2>&1 | tee /root/runs/recovery_aware_struct_prune/eval_math500_unpruned.log; echo EXIT_CODE=$? >> /root/runs/recovery_aware_struct_prune/eval_math500_unpruned.log'\\nroot      14551  0.0  0.0   4364  3260 ?        S    May17   0:00 bash -c source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20.json --seed 42 --max_new_tokens 4096 2>&1 | tee /root/autodl-tmp/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log\\nroot      14556  101  0.1 76175776 2039836 ?    Rl   May17 842:40 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20.json --seed 42 --max_new_tokens 4096\\nroot      14557  0.0  0.0   2796  1024 ?        S    May17   0:00 tee /root/autodl-tmp/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log\\nroot      31701  0.0  0.0   4496  3564 pts/2    Ss+  May17   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_math500_grpo_rasp_20_v3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/recovery_aware_struct_prune/eval
…[truncated 3910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T23:19:57.641751+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-11672",
  "command": "ps aux | grep cka_only_30 | grep -v grep; echo \"---END_OF_LOG---\"; tail -30 ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log; echo \"---LOG_SIZE---\"; wc -l ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-11672",
    "command": "ps aux | grep cka_only_30 | grep -v grep; echo \"---END_OF_LOG---\"; tail -30 ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log; echo \"---LOG_SIZE---\"; wc -l ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T23:19:57.641980+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "tail -20 ~/runs/recovery_aware_struct_prune/eval_math500_grpo_unpruned.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "tail -20 ~/runs/recovery_aware_struct_prune/eval_math500_grpo_unpruned.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T23:19:57.642407+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root      59403  0.0  0.0   4496  3492 ?        Ss   05:59   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_postprune_cka_only_30.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_postprune_cka_only_30.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/recovery_aware_struct_prune && export CUDA_VISIBLE_DEVICES=2 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_cka_only_30.json\\\"'; } > ~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log 2>&1\\nroot      59407  0.0  0.0   2800  1040 ?        S    05:59   0:00 timeout 86400 env bash -c bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_cka_only_30.json\\\"\\nroot      59408  105  0.1 49599576 1860632 ?    Rl   05:59  84:56 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_cka_only_30.json\\n---END_OF_LOG---\\n2026-05-18 06:00:36,064 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\\n2026-05-18 06:00:36,442 [INFO] Non-uniform MLP detected: intermediate_size range [8128, 18944]\\n2026-05-18 06:02:00,507 [INFO] Loading GSM8K 
…[truncated 5334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T23:19:57.642865+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-18 07:09:16,619 [INFO] Loading model from /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/339 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/339 [00:01<10:51,  1.93s/it]\\rLoading weights:   1%|          | 4/339 [00:02<02:13,  2.51it/s]\\rLoading weights:   2%|▏         | 6/339 [00:02<01:34,  3.53it/s]\\rLoading weights:   4%|▍         | 15/339 [00:02<00:35,  9.21it/s]\\rLoading weights:   7%|▋         | 24/339 [00:03<00:21, 14.37it/s]\\rLoading weights:   9%|▉         | 30/339 [00:03<00:16, 18.70it/s]\\rLoading weights:  12%|█▏        | 39/339 [00:03<00:12, 24.93it/s]\\rLoading weights:  13%|█▎        | 43/339 [00:03<00:13, 22.63it/s]\\rLoading weights:  15%|█▍        | 50/339 [00:03<00:11, 25.12it/s]\\rLoading weights:  16%|█▌        | 54/339 [00:04<00:13, 21.68it/s]\\rLoading weights:  19%|█▉        | 64/339 [00:04<00:09, 28.21it/s]\\rLoading weights:  20%|██        | 68/339 [00:04<00:11, 23.49it/s]\\rLoading weights:  21%|██        | 72/339 [00:04<00:11, 23.52it/s]\\rLoading weights:  23%|██▎       | 77/339 [00:04<00:09, 27.10it/s]\\rLoading weights:  24%|██▍       | 81/339 [00:04<00:09, 27.86it/s]\\rLoading weights:  26%|██▌       | 88/339 [00:05<00:08, 30.20it/s]\\rLoading weights:  27%|██▋       | 92/339 [00:05<00:10, 23.22it/s]\\rLoading weights:  29%|██▉       | 100/339 [00:05<00:08, 28.91it/s]\\rLoading weights:  31%|███       | 104/339 [00:05<00:09, 24.57it/s]\\rLoading weights:  32%|███▏      | 110/339 [00:06<00:08, 27.64it/s]\\rLoading weights:  34%|███▎      | 114/339 [00:06<00:09, 24.55it/s]\\rLoading weights:  37%|███▋      | 124/339 [00:06<00:06, 31.88it/s]\\rLoading weights:  38%|███▊      | 128/339 [00:06<00:08, 25.40it/s]\\rLoading weights:  40%|███▉      | 135/339 [00:06<00:07, 28.72it/s]\\rLoading weights:  41%|████      | 139/339 [00:07<00:08, 24.90it/
…[truncated 4714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T23:19:57.643230+00:00_

结果：

### 1. eval_postprune_cka_only_30 — 未失败，仍在运行

进程仍活跃 (PID 59408, 105% CPU, cuda:2)，当前进度 **56/200**。

日志中 sample 35 处出现 `Terminated` 字样，但进程并未退出，eval 继续运行到了 56。可能是同 GPU 上之前的某个进程被 kill。

关键指标（50/200 中间报告）：
- **acc = 0.0000**（零准确率）
- eos_rate = 4.00%
- avg_len = 4024（几乎全部 max out）

CKA-only 30% 剪枝后模型在 GSM8K 上完全丧失数学能力。

### 2. eval_math500_grpo_unpruned — 运行中

- 在 westd-11672 cuda:2 上运行（PID 64472, 07:09 启动）
- 当前进度 **11/500**
- 模型 `grpo_unpruned_v2/` 加载成功
- 结果文件尚未生成

### ⚠️ GPU 冲突

eval_postprune_cka_only_30 和 eval_math500_grpo_unpruned **都在 cuda:2 上**。这解释了 cka_only_30 在 sample 35 后速度从 ~95s/it 骤降到 ~48-90s/it。两个 eval 互相争抢显存和算力，都会变慢。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_postprune_cka_only_30_failure_20260517T231849"
}
```

</details>

---
