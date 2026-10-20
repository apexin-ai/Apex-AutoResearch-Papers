# verify server state

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_server-state_20260513T014230_result.json`
- **Structured JSON:** [`ebc2d2549b01061d8149.json`](../../sessions/eb/ebc2d2549b01061d8149.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux 被 read_only 模式阻止，其他全部完成。以下是原样输出：

---

### CHECK 1: Merged model
```
/root/autodl-tmp/models/Qwen2.5-7B-DPO003-merged/
total 14889884
-rw-r--r-- 1 root root        605 May 13 09:16 added_tokens.json
-rw-r--r-- 1 root root       2507 May 13 09:16 chat_template.jinja
-rw-r--r-- 1 root root       1318 May 13 09:15 config.json
-rw-r--r-- 1 root root        243 May 13 09:15 generation_config.json
-rw-r--r-- 1 root root    1671853 May 13 09:16 merges.txt
-rw-r--r-- 1 root root 4877660776 May 13 09:15 model-00001-of-00004.safetensors
-rw-r--r-- 1 root root 4932751008 May 13 09:16 model-00002-of-00004.safetensors
-rw-r--r-- 1 root root 4330865200 May 13 09:16 model-00003-of-00004.safetensors
-rw-r--r-- 1 root root 1089994880 May 13 09:16 model-00004-of-00004.safetensors
-rw-r--r-- 1 root root      27788 May 13 09:16 model.safetensors.index.json
-rw-r--r-- 1 root root        613 May 13 09:16 special_tokens_map.json
-rw-r--r-- 1 root root   11421896 May 13 09:16 tokenizer.json
-rw-r--r-- 1 root root       4686 May 13 09:16 tokenizer_config.json
-rw-r--r-- 1 root root    2776833 May 13 09:16 vocab.json
```

`/root/autodl-tmp/models/` 下的 Qwen 相关目录：
```
Qwen/
Qwen2.5-7B-DPO003-merged/
Qwen2.5-7B-Instruct/
Qwen2.5-7B-Instruct-DPO-merged/
```

---

### CHECK 2: cuda:2 processes
```
GPU 2: NVIDIA GeForce RTX 4090 D, 0% util, 0MiB / 24564MiB
No running processes found
```

---

### CHECK 3: PID 55024
```
PID_55024_NOT_FOUND
```

pgrep -f vllm 也无结果（ps aux 输出中无 vllm 进程）。

---

### CHECK 4: cuda:3 processes
```
GPU 3: NVIDIA GeForce RTX 4090 D, 0% util, 0MiB / 24564MiB
No running processes found
```

---

### CHECK 5: Diagnostic trace files
```
/root/democalib/results/diag_merged/  (创建于 May 13 09:18)
  └─ tool-calling-democalib-diag-0.0_range_0-5_user-democalib-diag-llm_0513091751.json

/root/democalib/results/diag_base/    (创建于 May 13 09:33)
  └─ tool-calling-democalib-diag-0.0_range_0-5_user-democalib-diag-llm_0513092625.json
  └─ tool-calling-democalib-diag-0.0_range_0-5_user-democalib-diag-llm_0513093332.json
```

其他 diag/merged 相关文件：
```
/root/democalib/results/baseline_merged.json
/root/democalib/test_mismatch_diagnosis.py
/root/democalib/eval_dpo003_merged.sh
```

---

### CHECK 6: Full GPU status
```
0, NVIDIA GeForce RTX 4090 D, 0 %, 0 MiB, 24564 MiB
1, NVIDIA GeForce RTX 4090 D, 0 %, 0 MiB, 24564 MiB
2, NVIDIA GeForce RTX 4090 D, 0 %, 0 MiB, 24564 MiB
3, NVIDIA GeForce RTX 4090 D, 0 %, 0 MiB, 24564 MiB
4, NVIDIA GeForce RTX 4090 D, 0 %, 0 MiB, 24564 MiB
5, NVIDIA GeForce RTX 4090 D, 0 %, 3 MiB, 24564 MiB
```

6x RTX 4090 D，全部空闲（0% util），仅 GPU 5 有 3MiB 占用。

---

### CHECK 7: All relevant processes (python/vllm/run_mvp)

**无 vLLM 进程。** 在跑的 python 进程：

| PID | 描述 |
|-----|------|
| 821 | tensorboard --port 6007 |
| 822 | jupyter-lab |
| 444913 | `huggingface_hub.snapshot_download('bigcode/starcoder2-3b')` |
| 494664 | `wget` 下载 starcoder2-3b model.safetensors |
| 570727 | `modelscope.snapshot_download('bigcode/starcoder2-3b')` |
| 577872 | `python extraction/batch_extract.py` (structfuse m1_extraction, 8 workers) |
| 577874 | 同上（子进程） |
| 多个 | codeql java 进程（structfuse 的 CodeQL 查询） |

---

### CHECK 8: tmux sessions
`tmux list-sessions` 被 read_only 模式阻止，无法执行。

---
