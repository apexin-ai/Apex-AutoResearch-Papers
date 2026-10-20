# diagnose westb full status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westb_full_status_20260522T121352_result.json`
- **Structured JSON:** [`ed63d8ec4dc4f06b8d48.json`](../../sessions/ed/ed63d8ec4dc4f06b8d48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU STATUS ===
0, 0 MiB, 97887 MiB, 0 %
1, 27395 MiB, 97887 MiB, 100 %

=== MF3 N=500 eval (GPU 1, PID 202364) ===
202364       07:08  261
RUNNING
tail -5 eval_gsm8k_grpo_qwen_math_cka_only_20_n500.log:
2026-05-22 20:08:52,193 [INFO] Loading GSM8K test set...
2026-05-22 20:08:53,206 [INFO] HTTP Request: HEAD https://s3.amazonaws.com/datasets.huggingface.co/datasets/datasets/parquet/parquet.py "HTTP/1.1 404 Not Found"
2026-05-22 20:08:53,270 [INFO] Evaluating on 500 test samples
2026-05-22 20:08:53,273 [INFO] Generation config: do_sample=False, temperature=0.0
Evaluating:   0%|          | 0/500 [00:00<?, ?it/s]

=== SFT random_20 transfer status ===
-rw-r--r-- 1 root root 6042042368 May 22 20:14 model.safetensors
8.0G	/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/

=== GPU 0 processes ===
202364, 27824 MiB, python
(no other eval/train processes besides PID 202364)

=== DISK ===
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        250G  230G   21G  92% /root/autodl-tmp
```

**摘要：**
- **GPU 0**: 空闲（0 MiB）
- **GPU 1**: PID 202364 占用 27.8GB / 95.6GB，运行 7h08m，利用率 100%。eval 刚开始（0/500），正在生成中
- **SFT random_20**: model.safetensors 5.6GB 已就位，目录总计 8.0GB
- **数据盘**: 230G/250G 已用（92%），剩余 21GB

---
