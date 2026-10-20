# diagnose gpu registry alignment

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-registry-alignment_20260528T085439_result.json`
- **Structured JSON:** [`22d4026bb05ba04a6065.json`](../../sessions/22/22d4026bb05ba04a6065.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Got all the data. Here's the report:

## Part 1: 未知进程

- **westd-10894:cuda:1**: PID 822480 — `finetune.py` 训练 **detach_ln_v2_s4**（parent PID 822402，CUDA_VISIBLE_DEVICES=1）→ 本项目实验，非未知进程，registry 需补注册 GPU 信息
- **westd-34685:cuda:0**: PID 47238 — `finetune.py` 训练 **detach_ln_v2_s2**（parent PID 47162，--resume True --resume_step 25000）→ 本项目实验，非未知进程，registry 需补注册 GPU 信息

## Part 2: 空闲确认

- **westd-10894:cuda:0**: 空闲（0 MiB used）
- **westd-34685:cuda:2**: 空闲（3 MiB used）
- **westd-34685:cuda:3**: 空闲（3 MiB used）

## Part 3: 训练进度

服务器当前时间: 2026-05-28 08:56 UTC（北京时间 16:56）
截止时间: 2026-05-28 12:00 UTC（北京时间 20:00）

| exp_id | server:gpu | step/total | speed (it/s) | 剩余时间 | ETA (UTC) | 能否按时 |
|--------|-----------|------------|-------------|---------|-----------|---------|
| detach_ln_v2_s4 | 10894:cuda:1 | 37086/50005 | ~1.06 | ~3h23m | ~12:19 | 略超时 |
| detach_ln_v2_s2 | 34685:cuda:0 | 24195/50005 | ~1.09 | ~6h35m | ~15:31 | 超时 |
| vanilla_object_s2 | 10894:cuda:3 | 13256/50005 | ~1.08 | ~9h27m | ~18:23 | 超时 |
| full_occ_bn_v2_s2 | 34685:cuda:1 | 15671/50005 | ~1.09 | ~8h45m | ~17:41 | 超时 |
| full_occ_bn_v2_s3 | 10894:cuda:2 | 13203/50005 | ~1.08 | ~9h28m | ~18:24 | 超时 |

**注意**: detach_ln_v2_s2 使用了 `--resume True --resume_step 25000`，但 tqdm 显示 24195/50005（batch_idx 从 0 重计数，与 C002/M052 描述的问题一致）。实际已训练 25000+24195=49195 步的数据，但训练循环仍会跑到 50005，总计将训练 75005 步。

**总结**: 5 个实验全部无法在 12:00 UTC 截止前完成。detach_ln_v2_s4 最接近（约超时 19 分钟）。其余 4 个超时 3.5~6.5 小时。3 个空闲 GPU 已确认可用。

---
