# harvest bjb1 32546 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 0
- **Tool calls:** 55
- **Original source:** `logs/chats/worker_harvest_bjb1-32546-check_20260526T195918.jsonl`
- **Structured JSON:** [`0e2aa7bca869c3baae10.json`](../../sessions/0e/0e2aa7bca869c3baae10.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

111 recorded events

### Tool call

_source line 1 · 2026-05-26T20:10:39.085536+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T20:10:39.086018+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T20:10:39.086319+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 903949,904304,908783,909918,911462,912825 -o pid,etime,args --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps -p 903949,904304,908783,909918,911462,912825 -o pid,etime,args --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T20:10:39.086551+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -w -w",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux --no-headers -w -w",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T20:10:39.086945+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"903949    04:13:54 bash -c cd /root/acr-vla-conformal-refinement && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 43 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed43_bjb1.json' > logs/eval-pi05-adaptive-long-s43-bjb1.log 2>&1 & echo \\\"PID=$!\\\"\\n904304    04:13:23 bash -c cd /root/acr-vla-conformal-refinement && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 44 --n_rollouts 20 --output_file logs/eval_long_adaptive_pi05_seed44_bjb1.json' > logs/eval-pi05-adaptive-long-s44-bjb1.log 2>&1 & echo \\\"PID=$!\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T20:10:39.087240+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root          1  0.0  0.0   4476  3364 ?        Ss   May15   0:02 bash /init/boot/boot.sh\\nroot        940  1.4  0.0 723360 21136 ?        Sl   May15 249:30 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        955  0.0  0.0 191548 105800 ?       S    May15   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        961  0.0  0.0 4147608 81420 ?       Sl   May15   7:13 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        962  0.0  0.0  15444  9424 ?        S    May15   1:11 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        964  0.1  0.0 3978752 18352 ?       Sl   May15  24:21 proxy -c /init/proxy/proxy.ini\\nroot        965  0.2  0.0 5342848 101276 ?      Sl   May15  43:52 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        966  0.0  0.0 3756340 17948 ?       Sl   May15   7:26 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1079  0.0  0.0 17524960 9964 ?       Sl   May15   6:14 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_q6bmzxvy/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_q6bmzxvy/startup_error\\nroot     831215  0.0  0.0  16768 10632 ?        Ss   May25   0:17 sshd: root@notty\\nroot     903949  0.0  0.0   4364  1940 ?        S    May26   0:00 bash -c cd /root/acr-vla-conformal-refinement && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unifie
…[truncated 1964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T20:10:39.087585+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T20:10:39.087948+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 32296\\ndrwxr-xr-x 3 root root   28672 May 27 02:10 .\\ndrwxr-xr-x 8 root root    4096 May 21 18:18 ..\\n-rw-r--r-- 1 root root    4247 May 23 12:08 adapt_tau015_spatial_s42.log\\n-rw-r--r-- 1 root root    4246 May 23 12:06 adapt_tau025_spatial_s42.log\\n-rw-r--r-- 1 root root    4245 May 23 12:09 adapt_tau035_spatial_s42.log\\n-rw-r--r-- 1 root root    4218 May 23 12:09 crm_norm02_spatial_s42.log\\n-rw-r--r-- 1 root root    7417 May 23 11:10 dirA_norm005_spatial_s42.log\\n-rw-r--r-- 1 root root    7411 May 23 11:14 dirA_norm01_spatial_s42.log\\n-rw-r--r-- 1 root root    6750 May 23 11:19 dirA_norm03_spatial_s42.log\\n-rw-r--r-- 1 root root    7538 May 23 11:18 dirB_adaptive_spatial_s42.log\\n-rw-r--r-- 1 root root    7174 May 23 11:17 dirC_reconvla_spatial_s42.log\\n-rw-r--r-- 1 root root    7531 May 25 01:09 eval-adaptive-k1-spatial-s42.log\\n-rw-r--r-- 1 root root    4076 May 20 20:37 eval-argmin-object-seed48.log\\n-rw-r--r-- 1 root root    4076 May 20 20:35 eval-argmin-object-seed49.log\\n-rw-r--r-- 1 root root    4017 May 20 23:00 eval-argmin-object-seed50.log\\n-rw-r--r-- 1 root root    5857 May 25 10:49 eval-canonical-adaptive-k10-spatial-s48.log\\n-rw-r--r-- 1 root root    5855 May 25 10:47 eval-canonical-adaptive-k10-spatial-s49.log\\n-rw-r--r-- 1 root root    5561 May 27 01:49 eval-crm-goal-s43-d149-bjb1.log\\n-rw-r--r-- 1 root root    6377 May 25 01:24 eval-crm-obj-s47-reeval.log\\n-rw-r--r-- 1 root root    6427 May 27 02:10 eval-crm-object-s42-d149-bjb1.log\\n-rw-r--r-- 1 root root    6426 May 27 02:10 eval-crm-object-s43-d149-bjb1.log\\n-rw-r--r-- 1 root root    1316 May 21 12:32 eval-crm-spatial-k10-seed50.log\\n-rw-r--r-- 1 root root    7460 May 27 01:48 eval-crm-spatial-s48-d149-bjb1.log\\n-rw-r--r-- 1 root root    7538 May 25 10:04 eval-k10-tau025-spatial-s46.log\\n-rw-r--r-- 1 root root    7533 May 25 12:49 eval-k2-adaptive-spatial-s46.log\\n-rw-r--r-- 1 root root    7539 May 25 12:50 e
…[truncated 6408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T20:10:39.088192+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -30 /root/acr-vla-conformal-refinement/logs/eval-pi05-adaptive-long-s43-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -30 /root/acr-vla-conformal-refinement/logs/eval-pi05-adaptive-long-s43-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T20:10:39.088524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 5/20, success so far: 5/5\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 10/20, success so far: 10/10\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 15/20, success so far: 13/15\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 20/20, success so far: 17/20\\n[LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket] success rate: 85.0% (17/20)\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 5/20, success so far: 5/5\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 10/20, success so far: 10/10\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 15/20, success so far: 15/15\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 20/20, success so far: 20/20\\n[LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket] success rate: 100.0% (20/20)\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 10/20, success so far: 10/10\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 15/20, success so far: 15/15\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 20/20, success so far: 20/20\\n[KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it] success rate: 100.0% (20/20)\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_
…[truncated 1637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T20:10:39.088763+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -30 /root/acr-vla-conformal-refinement/logs/eval-pi05-adaptive-long-s44-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -30 /root/acr-vla-conformal-refinement/logs/eval-pi05-adaptive-long-s44-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T20:10:39.089016+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading LIBERO long environments...\\n[info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\\n[eval] 10 tasks loaded.\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 5/20, success so far: 4/5\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 10/20, success so far: 9/10\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 15/20, success so far: 13/15\\n  LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket: rollout 20/20, success so far: 18/20\\n[LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket] success rate: 90.0% (18/20)\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 5/20, success so far: 5/5\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 10/20, success so far: 10/10\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 15/20, success so far: 15/15\\n  LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket: rollout 20/20, success so far: 19/20\\n[LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket] success rate: 95.0% (19/20)\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 5/20, success so far: 5/5\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 10/20, success so far: 10/10\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 15/20, success so far: 15/15\\n  KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it: rollout 20/20, success so far: 20/20\\n[KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it] success rate: 100.0% (20/20)\\n  KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it: rollout 5/20, success so far: 4/5\\n  KITCH
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T20:10:39.089331+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T20:10:39.089558+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (crm_obs_only): 80.5% (161/200)\\n============================================================\\n[eval] Results saved to logs/eval_spatial_crm_norm005_s48_d149.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T20:10:39.089767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T20:10:39.089981+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (crm_obs_only): 77.0% (154/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_crm_norm005_s42_d149.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T20:10:39.090186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T20:10:39.090419+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (crm_obs_only): 78.5% (157/200)\\n============================================================\\n[eval] Results saved to logs/eval_object_crm_norm005_s43_d149.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T20:10:39.090633+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T20:10:39.090847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nOverall success rate (crm_obs_only): 82.0% (164/200)\\n============================================================\\n[eval] Results saved to logs/eval_goal_crm_norm005_s43_d149.json\\nsys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T20:10:39.091048+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T20:10:39.091257+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_crm_norm005_s42_d149.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_norm005_s43_d149.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T20:10:39.091655+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_norm005_s48_d149.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_norm005_s48_d149.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T20:10:39.091943+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.805,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_th
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T20:10:39.092196+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_norm005_s42_d149.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_norm005_s42_d149.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T20:10:39.092521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.77,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T20:10:39.092773+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_norm005_s43_d149.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_crm_norm005_s43_d149.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T20:10:39.093046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.785,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.65,\\n      \\\"successes\\\": 13,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T20:10:39.093299+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_s43_d149.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cat /root/acr-vla-conformal-refinement/logs/eval_goal_crm_norm005_s43_d149.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T20:10:39.093576+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"goal\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.82,\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.75,\\n      \\\"successes\\\": 15,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"success_rate\\\": 0.6,\\n      \\\"successes\\\": 12,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_top_of_the_cabinet\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_cream_cheese_in_the_bowl\\\": {\\n      \\\"success_rate\\\": 0.5,\\n      \\\"successes\\\": 10,\\n      \\\"total\\\": 20\\n    },\\n    \\\"turn_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.9,\\n      \\\"successes\\\": 18,\\n      \\\"total\\\": 20\\n    },\\n    \\\"put_the_wine_bottle_on_the_rack\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T20:10:39.093806+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_norm005_s42_d149*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_crm_norm005_s42_d149*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T20:10:39.094094+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_crm_norm005_s42_d149*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T20:10:39.094363+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "fields": "['exp_id', 'status', 'hypothesis', 'spec']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "fields": "['exp_id', 'status', 'hypothesis', 'spec']",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T20:10:39.095144+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"pi05-object-tau035-s42-bjb2\": {\"status\": \"RUNNING\", \"hypothesis\": \"PI05 + ACR-VLA on Libero-Object with adaptive_conformal_crm at conformal_threshold=0.35 (higher than central tau=0.25) will decrease correction-trigger frequency and explore the high-tau regime of the tau-sweep curve. Combined with tau=0.15 (low) and existing tau=0.25 (central), this completes the Object-suite tau-sweep and reveals whether SR varies monotonically or peaks near 0.25.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.35 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_adaptive_pi05_tau035_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"pid\": \"549421\", \"data_path\": \"libero_object\", \"data_count\": 20, \"model_name\": \"pi05\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/pi05_libero_finetuned/\", \"eval_data\": \"libero_object 20 rollouts\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_tau035_seed42.log\", \"output_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_pi05_tau035_seed42.json\", \"tau\": 0.35, \"K\": 2, \"max_correction_norm\": 0.2}}, \"pi05-object-tau015-s42-bjb2\": {\"status\": \"RUNNING\", \"hypothesis\": \"PI05 + ACR-VLA on Libero-Object with adaptive_conformal_crm at conformal_threshold=0.15 (lower than central tau=0.25) will increase correction-trigger frequency and thereby explore the low-tau regime of the tau-sweep curve, allowing us to determine whether SR-vs-tau is monotonic or shows a sweet spot near 0.25 for the Object suite. Pairs with tau=0.35 (high regime) and existing tau=0.25 (central) point.\", \"spec\": {\"command\": \"
…[truncated 19002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T20:10:39.095506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T20:10:39.095842+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T20:10:39.096055+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T20:10:39.096297+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T20:10:39.096517+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T20:10:39.096733+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T20:10:39.096931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|CUDA error|out of memory|RuntimeError\" /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T20:10:39.097129+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T20:10:39.097338+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -c \"success rate: 0.0%\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -c \"success rate: 0.0%\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T20:10:39.097548+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T20:10:39.097741+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep \"success rate: 0.0%\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep \"success rate: 0.0%\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T20:10:39.097943+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T20:10:39.098168+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T20:10:39.098397+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T20:10:39.098607+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T20:10:39.098805+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T20:10:39.099001+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T20:10:39.099196+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T20:10:39.099416+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -iE \"OOM|out.of.memory|RuntimeError|CUDA.error\" /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T20:10:39.099616+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T20:10:39.099838+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T20:10:39.100041+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T20:10:39.100245+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T20:10:39.100476+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T20:10:39.100663+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T20:10:39.100865+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T20:10:39.101056+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -i -e OOM -e \"out of memory\" -e RuntimeError -e \"CUDA error\" /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T20:10:39.101256+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T20:10:39.101551+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-s48-d149-bjb1",
  "field": "metrics",
  "value": "{'overall_sr': 0.805, 'per_task': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.95, 'table_center': 1, 'on_cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.9, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.8}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-s48-d149-bjb1",
    "field": "metrics",
    "value": "{'overall_sr': 0.805, 'per_task': {'between_plate_ramekin': 1, 'next_to_ramekin': 0.95, 'table_center': 1, 'on_cookie_box': 0.95, 'top_drawer': 0.75, 'on_ramekin': 0, 'next_to_cookie_box': 0.95, 'on_stove': 0.9, 'next_to_plate': 0.75, 'on_wooden_cabinet': 0.8}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T20:10:39.101797+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s42-d149-bjb1",
  "field": "metrics",
  "value": "{'overall_sr': 0.77, 'per_task': {'alphabet_soup': 0.7, 'cream_cheese': 0.7, 'salad_dressing': 0.75, 'bbq_sauce': 0.9, 'ketchup': 0.8, 'tomato_sauce': 0.7, 'butter': 0.7, 'milk': 0.75, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s42-d149-bjb1",
    "field": "metrics",
    "value": "{'overall_sr': 0.77, 'per_task': {'alphabet_soup': 0.7, 'cream_cheese': 0.7, 'salad_dressing': 0.75, 'bbq_sauce': 0.9, 'ketchup': 0.8, 'tomato_sauce': 0.7, 'butter': 0.7, 'milk': 0.75, 'chocolate_pudding': 0.85, 'orange_juice': 0.85}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T20:10:39.102023+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s43-d149-bjb1",
  "field": "metrics",
  "value": "{'overall_sr': 0.785, 'per_task': {'alphabet_soup': 0.65, 'cream_cheese': 0.8, 'salad_dressing': 0.85, 'bbq_sauce': 0.8, 'ketchup': 0.8, 'tomato_sauce': 0.75, 'butter': 0.7, 'milk': 0.7, 'chocolate_pudding': 0.9, 'orange_juice': 0.9}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s43-d149-bjb1",
    "field": "metrics",
    "value": "{'overall_sr': 0.785, 'per_task': {'alphabet_soup': 0.65, 'cream_cheese': 0.8, 'salad_dressing': 0.85, 'bbq_sauce': 0.8, 'ketchup': 0.8, 'tomato_sauce': 0.75, 'butter': 0.7, 'milk': 0.7, 'chocolate_pudding': 0.9, 'orange_juice': 0.9}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T20:10:39.102258+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-s43-d149-bjb1",
  "field": "metrics",
  "value": "{'overall_sr': 0.82, 'per_task': {'open_middle_drawer': 0.75, 'bowl_on_stove': 1, 'wine_on_cabinet': 0.9, 'open_top_drawer_bowl': 0.6, 'bowl_on_cabinet': 0.95, 'plate_to_front': 0.95, 'cream_cheese_in_bowl': 0.5, 'turn_on_stove': 0.95, 'bowl_on_plate': 0.9, 'wine_on_rack': 0.7}}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-s43-d149-bjb1",
    "field": "metrics",
    "value": "{'overall_sr': 0.82, 'per_task': {'open_middle_drawer': 0.75, 'bowl_on_stove': 1, 'wine_on_cabinet': 0.9, 'open_top_drawer_bowl': 0.6, 'bowl_on_cabinet': 0.95, 'plate_to_front': 0.95, 'cream_cheese_in_bowl': 0.5, 'turn_on_stove': 0.95, 'bowl_on_plate': 0.9, 'wine_on_rack': 0.7}}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T20:10:39.102533+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-s48-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:51:58.942Z\", \"updated_at\": \"2026-05-26T20:01:20.235Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on spatial s48 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 48 --n_rollouts 20 --output_file logs/eval_spatial_crm_norm005_s48_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-spatial 10 tasks x 20 rollouts\", \"pid\": 908783, \"log_path\": \"logs/eval-crm-spatial-s48-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.805, \"per_task\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.1641}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T20:10:39.102774+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s42-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:03.258Z\", \"updated_at\": \"2026-05-26T20:01:29.122Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s42 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s42_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 909918, \"log_path\": \"logs/eval-crm-object-s42-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.77, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.3348}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T20:10:39.103029+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:07.581Z\", \"updated_at\": \"2026-05-26T20:01:38.589Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 911462, \"log_path\": \"logs/eval-crm-object-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.785, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.8, \"ketchup\": 0.8, \"tomato_sauce\": 0.75, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4254}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-26T20:10:39.103297+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:11.867Z\", \"updated_at\": \"2026-05-26T20:01:48.054Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on goal s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"pid\": 912825, \"log_path\": \"logs/eval-crm-goal-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"open_middle_drawer\": 0.75, \"bowl_on_stove\": 1, \"wine_on_cabinet\": 0.9, \"open_top_drawer_bowl\": 0.6, \"bowl_on_cabinet\": 0.95, \"plate_to_front\": 0.95, \"cream_cheese_in_bowl\": 0.5, \"turn_on_stove\": 0.95, \"bowl_on_plate\": 0.9, \"wine_on_rack\": 0.7}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1148}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T20:10:39.103578+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-s48-d149-bjb1",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-s48-d149-bjb1",
    "field": "checkpoint_path",
    "value": "N/A - eval only",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T20:10:39.103794+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s42-d149-bjb1",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s42-d149-bjb1",
    "field": "checkpoint_path",
    "value": "N/A - eval only",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T20:10:39.103994+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s43-d149-bjb1",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s43-d149-bjb1",
    "field": "checkpoint_path",
    "value": "N/A - eval only",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T20:10:39.104180+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-s43-d149-bjb1",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-s43-d149-bjb1",
    "field": "checkpoint_path",
    "value": "N/A - eval only",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T20:10:39.104445+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-s48-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:51:58.942Z\", \"updated_at\": \"2026-05-26T20:02:03.859Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on spatial s48 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 48 --n_rollouts 20 --output_file logs/eval_spatial_crm_norm005_s48_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-spatial 10 tasks x 20 rollouts\", \"pid\": 908783, \"log_path\": \"logs/eval-crm-spatial-s48-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.805, \"per_task\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}, \"checkpoint_path\": \"N/A - eval only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.5629}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T20:10:39.104699+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s42-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:03.258Z\", \"updated_at\": \"2026-05-26T20:02:25.275Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s42 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s42_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 909918, \"log_path\": \"logs/eval-crm-object-s42-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.77, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"checkpoint_path\": \"N/A - eval only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.0714}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T20:10:39.104951+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:07.581Z\", \"updated_at\": \"2026-05-26T20:02:59.177Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 911462, \"log_path\": \"logs/eval-crm-object-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.785, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.8, \"ketchup\": 0.8, \"tomato_sauce\": 0.75, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}, \"checkpoint_path\": \"N/A - eval only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.6047}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T20:10:39.105203+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:11.867Z\", \"updated_at\": \"2026-05-26T20:03:26.223Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on goal s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"pid\": 912825, \"log_path\": \"logs/eval-crm-goal-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"open_middle_drawer\": 0.75, \"bowl_on_stove\": 1, \"wine_on_cabinet\": 0.9, \"open_top_drawer_bowl\": 0.6, \"bowl_on_cabinet\": 0.95, \"plate_to_front\": 0.95, \"cream_cheese_in_bowl\": 0.5, \"turn_on_stove\": 0.95, \"bowl_on_plate\": 0.9, \"wine_on_rack\": 0.7}}, \"checkpoint_path\": \"N/A - eval only\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 27.4865}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T20:10:39.105489+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-s48-d149-bjb1",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-s48-d149-bjb1",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T20:10:39.105699+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s42-d149-bjb1",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s42-d149-bjb1",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T20:10:39.105902+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s43-d149-bjb1",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s43-d149-bjb1",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-26T20:10:39.106098+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-s43-d149-bjb1",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-s43-d149-bjb1",
    "field": "log_path",
    "value": "/root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T20:10:39.106351+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-s48-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:51:58.942Z\", \"updated_at\": \"2026-05-26T20:03:51.804Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on spatial s48 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 48 --n_rollouts 20 --output_file logs/eval_spatial_crm_norm005_s48_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-spatial 10 tasks x 20 rollouts\", \"pid\": 908783, \"log_path\": \"logs/eval-crm-spatial-s48-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.805, \"per_task\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.4966}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T20:10:39.106623+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s42-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:03.258Z\", \"updated_at\": \"2026-05-26T20:04:21.508Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s42 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s42_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 909918, \"log_path\": \"logs/eval-crm-object-s42-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.77, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.9282}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T20:10:39.106879+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:07.581Z\", \"updated_at\": \"2026-05-26T20:04:53.708Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 911462, \"log_path\": \"logs/eval-crm-object-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.785, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.8, \"ketchup\": 0.8, \"tomato_sauce\": 0.75, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 30.9571}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T20:10:39.107129+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:11.867Z\", \"updated_at\": \"2026-05-26T20:05:35.596Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on goal s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"pid\": 912825, \"log_path\": \"logs/eval-crm-goal-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"open_middle_drawer\": 0.75, \"bowl_on_stove\": 1, \"wine_on_cabinet\": 0.9, \"open_top_drawer_bowl\": 0.6, \"bowl_on_cabinet\": 0.95, \"plate_to_front\": 0.95, \"cream_cheese_in_bowl\": 0.5, \"turn_on_stove\": 0.95, \"bowl_on_plate\": 0.9, \"wine_on_rack\": 0.7}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 43.8767}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T20:10:39.107377+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-s48-d149-bjb1",
  "field": "conclusion",
  "value": "SR=80.5% (161/200). CRM obs_only K=10 norm=0.05 on spatial s48. on_ramekin task 0% (known hard). No OOM/errors.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-s48-d149-bjb1",
    "field": "conclusion",
    "value": "SR=80.5% (161/200). CRM obs_only K=10 norm=0.05 on spatial s48. on_ramekin task 0% (known hard). No OOM/errors.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T20:10:39.107581+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s42-d149-bjb1",
  "field": "conclusion",
  "value": "SR=77.0% (154/200). CRM obs_only K=10 norm=0.05 on object s42. All tasks 70-90%. No OOM/errors.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s42-d149-bjb1",
    "field": "conclusion",
    "value": "SR=77.0% (154/200). CRM obs_only K=10 norm=0.05 on object s42. All tasks 70-90%. No OOM/errors.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T20:10:39.107782+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s43-d149-bjb1",
  "field": "conclusion",
  "value": "SR=78.5% (157/200). CRM obs_only K=10 norm=0.05 on object s43. All tasks 65-90%. No OOM/errors.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s43-d149-bjb1",
    "field": "conclusion",
    "value": "SR=78.5% (157/200). CRM obs_only K=10 norm=0.05 on object s43. All tasks 65-90%. No OOM/errors.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T20:10:39.107977+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-s43-d149-bjb1",
  "field": "conclusion",
  "value": "SR=82.0% (164/200). CRM obs_only K=10 norm=0.05 on goal s43. Range 50-100%. No OOM/errors.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-s43-d149-bjb1",
    "field": "conclusion",
    "value": "SR=82.0% (164/200). CRM obs_only K=10 norm=0.05 on goal s43. Range 50-100%. No OOM/errors.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T20:10:39.108174+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'SR=80.5% (161/200). CRM obs_only K=10 norm=0.05 on spatial s48. on_ramekin task 0% (known hard). No OOM/errors.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 38.105}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T20:10:39.108424+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'SR=77.0% (154/200). CRM obs_only K=10 norm=0.05 on object s42. All tasks 70-90%. No OOM/errors.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 29.1376}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-26T20:10:39.108629+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'SR=78.5% (157/200). CRM obs_only K=10 norm=0.05 on object s43. All tasks 65-90%. No OOM/errors.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 29.5219}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T20:10:39.108820+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'SR=82.0% (164/200). CRM obs_only K=10 norm=0.05 on goal s43. Range 50-100%. No OOM/errors.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 15.7729}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T20:10:39.109018+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-s48-d149-bjb1",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-s48-d149-bjb1",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T20:10:39.109213+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s42-d149-bjb1",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s42-d149-bjb1",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T20:10:39.109432+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s43-d149-bjb1",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s43-d149-bjb1",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-26T20:10:39.109632+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-s43-d149-bjb1",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-s43-d149-bjb1",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T20:10:39.109869+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-s48-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:51:58.942Z\", \"updated_at\": \"2026-05-26T20:07:55.659Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on spatial s48 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 48 --n_rollouts 20 --output_file logs/eval_spatial_crm_norm005_s48_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-spatial 10 tasks x 20 rollouts\", \"pid\": 908783, \"log_path\": \"logs/eval-crm-spatial-s48-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.805, \"per_task\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 15.4689}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T20:10:39.110122+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s42-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:03.258Z\", \"updated_at\": \"2026-05-26T20:08:12.344Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s42 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s42_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 909918, \"log_path\": \"logs/eval-crm-object-s42-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.77, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 19.3346}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-26T20:10:39.110395+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:07.581Z\", \"updated_at\": \"2026-05-26T20:08:30.480Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 911462, \"log_path\": \"logs/eval-crm-object-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.785, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.8, \"ketchup\": 0.8, \"tomato_sauce\": 0.75, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.0861}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T20:10:39.110658+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-s43-d149-bjb1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:11.867Z\", \"updated_at\": \"2026-05-26T20:08:45.716Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on goal s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"pid\": 912825, \"log_path\": \"logs/eval-crm-goal-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"open_middle_drawer\": 0.75, \"bowl_on_stove\": 1, \"wine_on_cabinet\": 0.9, \"open_top_drawer_bowl\": 0.6, \"bowl_on_cabinet\": 0.95, \"plate_to_front\": 0.95, \"cream_cheese_in_bowl\": 0.5, \"turn_on_stove\": 0.95, \"bowl_on_plate\": 0.9, \"wine_on_rack\": 0.7}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.5002}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T20:10:39.110874+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-spatial-s48-d149-bjb1",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-spatial-s48-d149-bjb1",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-26T20:10:39.111067+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s42-d149-bjb1",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s42-d149-bjb1",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T20:10:39.111259+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-object-s43-d149-bjb1",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-object-s43-d149-bjb1",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T20:10:39.111485+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-crm-goal-s43-d149-bjb1",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-crm-goal-s43-d149-bjb1",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-26T20:10:39.111878+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-spatial-s48-d149-bjb1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:51:58.942Z\", \"updated_at\": \"2026-05-26T20:09:01.485Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on spatial s48 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 48 --n_rollouts 20 --output_file logs/eval_spatial_crm_norm005_s48_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-spatial 10 tasks x 20 rollouts\", \"pid\": 908783, \"log_path\": \"logs/eval-crm-spatial-s48-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.805, \"per_task\": {\"between_plate_ramekin\": 1, \"next_to_ramekin\": 0.95, \"table_center\": 1, \"on_cookie_box\": 0.95, \"top_drawer\": 0.75, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.9, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.8}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T20:09:01.485Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 21.6427}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T20:10:39.112214+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s42-d149-bjb1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:03.258Z\", \"updated_at\": \"2026-05-26T20:09:15.800Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s42 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s42_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 909918, \"log_path\": \"logs/eval-crm-object-s42-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.77, \"per_task\": {\"alphabet_soup\": 0.7, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.9, \"ketchup\": 0.8, \"tomato_sauce\": 0.7, \"butter\": 0.7, \"milk\": 0.75, \"chocolate_pudding\": 0.85, \"orange_juice\": 0.85}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T20:09:15.800Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 14.8342}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-26T20:10:39.112564+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-object-s43-d149-bjb1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:07.581Z\", \"updated_at\": \"2026-05-26T20:09:31.590Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on object s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-object\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-object 10 tasks x 20 rollouts\", \"pid\": 911462, \"log_path\": \"logs/eval-crm-object-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.785, \"per_task\": {\"alphabet_soup\": 0.65, \"cream_cheese\": 0.8, \"salad_dressing\": 0.85, \"bbq_sauce\": 0.8, \"ketchup\": 0.8, \"tomato_sauce\": 0.75, \"butter\": 0.7, \"milk\": 0.7, \"chocolate_pudding\": 0.9, \"orange_juice\": 0.9}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T20:09:31.590Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.3738}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T20:10:39.112875+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-crm-goal-s43-d149-bjb1\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T15:52:11.867Z\", \"updated_at\": \"2026-05-26T20:10:00.430Z\", \"hypothesis\": \"SmolVLA CRM (K=10, norm=0.05) on goal s43 provides action correction (Table 1 D149 seed, bjb1-32546 rerun)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --output_file logs/eval_goal_crm_norm005_s43_d149.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-goal 10 tasks x 20 rollouts\", \"pid\": 912825, \"log_path\": \"logs/eval-crm-goal-s43-d149-bjb1.log\"}, \"metrics\": {\"overall_sr\": 0.82, \"per_task\": {\"open_middle_drawer\": 0.75, \"bowl_on_stove\": 1, \"wine_on_cabinet\": 0.9, \"open_top_drawer_bowl\": 0.6, \"bowl_on_cabinet\": 0.95, \"plate_to_front\": 0.95, \"cream_cheese_in_bowl\": 0.5, \"turn_on_stove\": 0.95, \"bowl_on_plate\": 0.9, \"wine_on_rack\": 0.7}}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-26T20:10:00.430Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 27.6943}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-26T20:10:39.113188+00:00_

4 个 CRM D149 实验已全部 DONE。Registry 已更新。

## bjb1-32546 实验状态

| exp_id | PID | 状态 | SR | 备注 |
|--------|-----|------|-----|------|
| pi05-adaptive-long-s43-bjb1 | 903949 | **alive** | — | task 7/10 (STUDY_SCENE1 rollout 15/20)，已跑 4h14m，预计还 ~1.5h |
| pi05-adaptive-long-s44-bjb1 | 904304 | **alive** | — | task 6/10 (STUDY_SCENE1 rollout 10/20)，已跑 4h13m，预计还 ~2h |
| eval-crm-spatial-s48-d149-bjb1 | 908783 | **done** → DONE | **80.5%** | on_ramekin 0%（known hard），其余 75-100% |
| eval-crm-object-s42-d149-bjb1 | 909918 | **done** → DONE | **77.0%** | all tasks 70-90% |
| eval-crm-object-s43-d149-bjb1 | 911462 | **done** → DONE | **78.5%** | all tasks 65-90% |
| eval-crm-goal-s43-d149-bjb1 | 912825 | **done** → DONE | **82.0%** | cream_cheese_in_bowl 50%（最低） |
| E_smolvla_crm_norm005_spatial_s42_d149 | — | **不在此服务器** | — | 注册在 bjb1-18228 |
| E_smolvla_adaptive_tau045_spatial_s42 | — | **不在此服务器** | — | 注册在 bjb1-18228 |
| E_smolvla_adaptive_tau015_spatial_s42 | — | **不在此服务器** | — | 注册在 bjb1-18228 |
| E_smolvla_adaptive_tau035_spatial_s42 | — | **不在此服务器** | — | 注册在 bjb1-18228 |

**关键发现：**
- 4 个 CRM D149 补跑全部完成，日志干净（无 OOM/CUDA error），registry 已更新为 DONE
- π0.5 Long s43/s44 hedge run 仍在跑，s43 略领先 s44 约 1 个 task
- τ-sweep 4 个实验不在 bjb1-32546 上（注册服务器是 bjb1-18228），bjb1-32546 上目前只有 GPU 0/1 被 π0.5 占用，GPU 2-5 已空闲

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_harvest_bjb1-32546-check_20260526T195918"
}
```

</details>

---
