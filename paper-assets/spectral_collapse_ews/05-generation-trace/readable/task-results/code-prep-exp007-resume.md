# code prep exp007 resume

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp007-resume_20260519T131258_result.json`
- **Structured JSON:** [`3b1acf8b54a57a65a0a5.json`](../../sessions/3b/3b1acf8b54a57a65a0a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**结果：**
- `run_phase1.py` 已有 `--start_gen` resume 支持，无需修改代码
- Resume 逻辑：加载 `gen_5` checkpoint + 已有 results JSON（含 gen 0-5 共 6 条），从 gen 6 续跑到 gen 10
- Checkpoint 目录 `fixed_mix_r02_seed42/` 中 gen_0 ~ gen_5 完整
- Results JSON 存在且格式正常

**Launch 脚本：** `/root/spectral_collapse_ews/launch_exp007_resume.sh`

**Dry-run：** `--help` 确认 `--start_gen` 参数正常识别

等 cuda:0 上的 exp_009 跑完后，执行 `bash /root/spectral_collapse_ews/launch_exp007_resume.sh` 即可。

---
