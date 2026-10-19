# check m2 status 20260514 v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_m2_status_20260514_v2_20260514T190621_result.json`
- **Structured JSON:** [`c8ed6c4566eee97acd9d.json`](../../sessions/c8/c8ed6c4566eee97acd9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 检查 1: M2 训练进程存活
```
337267    07:42:43 bash run_m2_full_qwen.sh
519791    01:03:46 bash -c rm -f /tmp/agent-ml-exit/m2_full_starcoder.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo "EXIT_CODE=$_EC" >> ~/runs/structfuse-context/m2_full_starcoder.log; printf "%s|%s\n" "$_EC" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > /tmp/agent-ml-exit/m2_full_starcoder.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/structfuse && export CUDA_VISIBLE_DEVICES=1 && timeout 518400 env bash -c 'bash -c "cd /root/structfuse && bash run_m2_full_starcoder_resume.sh"'; } > ~/runs/structfuse-context/m2_full_starcoder.log 2>&1
```

### 检查 2: 各 chain 产出 runs 数

**/root/autodl-tmp/structfuse/full_m2_outputs/**:
```
total 4
drwxr-xr-x  3 root root   32 May 14 00:59 .
drwxr-xr-x 17 root root 4096 May 14 18:26 ..
drwxr-xr-x  2 root root   31 May 14 00:59 random_s42
```

**/root/structfuse/outputs/m2_full_runs/qwen/**:
```
ls: cannot access '/root/structfuse/outputs/m2_full_runs/qwen/': No such file or directory
```

**/root/structfuse/outputs/m2_full_runs/starcoder/**:
```
ls: cannot access '/root/structfuse/outputs/m2_full_runs/starcoder/': No such file or directory
```

### 检查 3: 当前正在训练哪个 run

**/root/autodl-tmp/structfuse/full_m2_outputs/*/wandb/**:
```
total 0
drwxr-xr-x 2 root root 31 May 14 00:59 random_s42
```

**日志文件列表** (`/root/runs/structfuse-context/`):
```
total 8768
-rw-r--r-- 1 root root 3534927 May 15 03:06 m1_reextract_v2.log
-rw-r--r-- 1 root root 3880321 May 15 03:06 m1_rerun.log
-rw-r--r-- 1 root root     994 May 15 02:57 m2_full_starcoder.log
-rw-r--r-- 1 root root     157 May 14 19:17 m2_full_qwen.log
-rw-r--r-- 1 root root   50951 May 14 01:31 sc_data_build.log
```

**m2_full_qwen.log 尾部**:
```
==========================================
[1/9] Starting: random_s42 at Thu May 14 01:39:30 CST 2026
==========================================
EXIT_CODE=0
```

**m2_full_starcoder.log 尾部**:
```
`use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`.
  step 50  loss=0.6781  lr=3.42e-06
  step 100  loss=1.1000  lr=6.98e-06
  step 150  loss=0.3684  lr=1.05e-05
  step 200  loss=0.4080  lr=1.41e-05
```

### 检查 4: m1_reextract_v2 进度

两个预期路径均无 jsonl 文件：
```
/root/autodl-tmp/structfuse/extraction_v2/all.jsonl — No such file or directory
/root/structfuse/outputs/m1_reextract_v2/recovered.jsonl — No such file or directory
find /root/autodl-tmp/structfuse/ -name "*.jsonl" -path "*reextract*" — (无结果)
find /root/structfuse/outputs/ — No such file or directory
```

**m1_reextract_v2.log 尾部**（进程仍在运行）:
```
2026-05-15 03:06:28,487 [INFO] batch_extract: [facebookresearch/hydra] processed 200/402 instances
2026-05-15 03:06:33,281 [INFO] batch_extract: [facebookresearch__hydra.0f03eb60.func_pm_remove_assign__cprdx2mm] CodeQL call_graph: 120 entries, 36 reachable files (threshold=1)
2026-05-15 03:06:44,288 [INFO] batch_extract: [facebookresearch__hydra.0f03eb60.func_pm_remove_assign__eis10fmy] CodeQL call_graph: 336 entries, 44 reachable files (threshold=1)
2026-05-15 03:06:55,432 [INFO] batch_extract: [facebookresearch__hydra.0f03eb60.func_pm_remove_assign__em226h0t] CodeQL call_graph: 1 entries, 1 reachable files (threshold=1)
2026-05-15 03:07:05,157 [INFO] batch_extract: [facebookresearch__hydra.0f03eb60.func_pm_remove_assign__g9z2lch9] CodeQL call_graph: 142 entries, 19 reachable files (threshold=1)
```

### 检查 5: BM25 watcher tmux 状态
```
Command blocked: 'tmux' is not allowed in read-only mode.
```
（`tmux` 不在 ssh_read_only 白名单中，无法执行）

### 检查 6: GPU 使用
```
0, 100 %, 50641 MiB, 97887 MiB
1, 100 %, 53927 MiB, 97887 MiB
```

---
