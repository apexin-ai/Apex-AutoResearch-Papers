# code batch eval script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch-eval-script_20260526T165454_result.json`
- **Structured JSON:** [`76bb587e5a364179b05a.json`](../../sessions/76/76bb587e5a364179b05a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器均已部署成功。exit code 1 是因为无参数运行触发了 usage 输出（符合预期）。

部署结果：
- **westd-10894**: `/root/occsafe_vla/scripts/batch_eval.sh` ✓
- **westd-34685**: `/root/occsafe_vla/scripts/batch_eval.sh` ✓

使用方式：
```bash
# 34685 上跑 4 个 eval
bash /root/occsafe_vla/scripts/batch_eval.sh \
  vanilla_v2_s1:0 vanilla_v2_s2:1 detach_ln_s3:2 cutoff_25k_s1_v2:3

# 10894 上跑 3 个 eval
bash /root/occsafe_vla/scripts/batch_eval.sh \
  full_occ_ln_v2_s0:1 full_occ_ln_v2_s1:2 detach_ln_v2_s0:3
```

脚本会先检查所有 checkpoint 目录是否存在，全部 OK 才启动 eval；每个 eval 在独立 tmux session 中运行（`{exp_id}_eval`），日志写到 `/root/occsafe_vla/logs/{exp_id}_eval.log`。

---
