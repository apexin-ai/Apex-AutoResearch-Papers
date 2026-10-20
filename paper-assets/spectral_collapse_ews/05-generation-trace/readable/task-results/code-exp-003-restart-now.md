# code exp 003 restart now

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_003_restart_now_20260517T131148_result.json`
- **Structured JSON:** [`0647746b615c510ffe23.json`](../../sessions/06/0647746b615c510ffe23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行。Log 中只有 tokenizer warnings（正常，Pythia padding 相关），print 输出因 Python 缓冲暂未刷出。进程 alive，GPU 已占用。

---

**产出：**

```
D011 bugfix: 已就位（set_baseline @ pipeline.py:148, report_actual @ pipeline.py:178-181, total_per_gen @ pipeline.py:153）
D012 params: k=20.0, tau=0.002（controller.py + run_phase1.py argparse 均已更新）
exp_003 PID: 116006
GPU 0: 65909 MiB (phase0 run, PID 59365)
GPU 1: 18980 MiB, 97% util (exp_003 adaptive, PID 116006) ✓
启动确认: 进程活跃，tokenizer warnings 正常，stdout 缓冲中
```

---
