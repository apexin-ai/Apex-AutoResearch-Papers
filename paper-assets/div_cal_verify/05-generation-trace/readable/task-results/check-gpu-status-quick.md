# check gpu status quick

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_quick_20260514T030846_result.json`
- **Structured JSON:** [`40f7aeb6781d8b6d28a1.json`](../../sessions/40/40f7aeb6781d8b6d28a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**1. nvidia-smi**
```
0, 100 %, 71641 MiB, 97887 MiB
1, 0 %, 0 MiB, 97887 MiB
```

**2. ps aux | grep train/python**
```
root        912  0.0  0.0 191560 105628 ?       S    May12   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py
root        917  0.0  0.0 3574328 81144 ?       Sl   May12   1:03 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs
root       1009  0.0  0.0 28341192 12248 ?      Sl   May12   2:00 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_t_ochydy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_t_ochydy/startup_error
root     391599  399  0.7 66842276 7795812 pts/0 Rl+ 09:58 282:55 python3 /root/div_cal_verify/run_mvp.py --method uncurated --student_model gpt2-medium --self_iterate --no_quality_filter --data_dir /root/div_cal_verify/data_gpt2 --output_dir /root/autodl-tmp/div_cal_verify/results_medium_uncurated_seed123 --num_generations 8 --gen_tokens 500000 --train_epochs 3 --train_lr 5e-5 --train_batch_size 4 --train_grad_accum 8 --seq_len 512 --gpu_ids 0 --seed 123
```

**3. ps aux | grep chain_cuda0**
```
root     391587  0.0  0.0   4364  3140 pts/0    Ss+  09:58   0:00 bash -c bash chain_cuda0_seed123.sh 2>&1 | tee /root/autodl-tmp/div_cal_verify/chain_cuda0_seed123.log
root     391589  0.0  0.0   4364  3132 pts/0    S+   09:58   0:00 bash chain_cuda0_seed123.sh
root     391590  0.0  0.0   2796  1036 pts/0    S+   09:58   0:00 tee /root/autodl-tmp/div_cal_verify/chain_cuda0_seed123.log
```

**4. ps aux | grep medium_external**
```
(无匹配进程)
```

**5. tmux ls**
```
chain_cuda0_s123: 1 windows (created Thu May 14 09:58:34 2026)
medium_random50: 1 windows (created Thu May 14 10:05:05 2026)
```

---
