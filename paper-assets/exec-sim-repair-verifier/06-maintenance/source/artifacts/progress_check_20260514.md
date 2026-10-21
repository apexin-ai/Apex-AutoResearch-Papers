# Progress Check — 2026-05-14 ~23:45 (server time)

## GPU Status (nvidia-smi)

| GPU | Model | Util | VRAM Used | VRAM Total | Temp |
|-----|-------|------|-----------|------------|------|
| 0 | RTX 5090 | 85% | 12,999 MiB | 32,607 MiB | 60°C |
| 1 | RTX 5090 | 88% | 12,999 MiB | 32,607 MiB | 61°C |
| 2 | RTX 5090 | 94% | 21,205 MiB | 32,607 MiB | 68°C |
| 3 | RTX 5090 | 97% | 26,751 MiB | 32,607 MiB | 73°C |

---

## 1. CWM v12 Eval (PID 195668, cuda:1)

| 指标 | 值 |
|------|-----|
| **状态** | ALIVE (uptime 14h38m) |
| **进度** | 8352 / 9784 (**85.4%**) |
| **Running Accuracy** | **57.8%** (从 58.3% 微降，正常波动) |
| **速度** | ~8 samples / 51 sec |
| **剩余** | 1432 samples ≈ **2.5 小时** |
| **预计完成** | ~02:15 server time (May 15) |

---

## 2. CWM seed123 Eval (PID 195531, cuda:0)

| 指标 | 值 |
|------|-----|
| **状态** | ALIVE (uptime 14h38m) |
| **进度** | 8248 / 9784 (**84.3%**) |
| **Running Accuracy** | **59.1%** (从 57.3% 上升) |
| **速度** | ~8 samples / 52 sec |
| **剩余** | 1536 samples ≈ **2.8 小时** |
| **预计完成** | ~02:30 server time (May 15) |

---

## 3. CWM 8B Training (PID 245775, cuda:2)

| 指标 | 值 |
|------|-----|
| **状态** | ALIVE (重启后 1h13m) — **之前崩溃过** |
| **崩溃原因** | `DataLoader worker killed by signal: Terminated` — eval 阶段 OOM |
| **重启时间** | 22:28 server time |
| **当前 step** | ~1500 / 6633 (**22.6%**，从 ckpt-1200 resume) |
| **当前状态** | 正在做 eval（eval 进度 46%，4327/9335） |
| **Training Loss** | 0.5103 → 0.5436 → 0.5294 → **0.4453** |
| **Eval Loss** | step 1400: **0.3637** |
| **训练速度** | ~12s/step（不含 eval） |
| **预计完成** | ~May 15 17:00 server time（粗估） |

---

## 4. CLS 8B seed123 Training (PID 248041, cuda:3)

| 指标 | 值 |
|------|-----|
| **状态** | ALIVE (重启后 55m) — **之前崩溃过** |
| **崩溃原因** | `DataLoader worker killed by signal: Terminated` — eval 阶段 OOM |
| **重启时间** | ~22:48 server time |
| **当前 step** | 2677 / 6633 (**40.4%**，从 ckpt-2400 resume) |
| **Training Loss** | step 2650: **0.3559** |
| **Eval Loss** | step 2600: **0.2779** |
| **训练速度** | ~8.3s/step |
| **预计完成** | ~May 15 11:00 server time（粗估） |
| **日志位置** | `/tmp/cls_8b_s123_ckpt2400_resume.log` |

---

## 总结

| 进程 | 状态 | 进度 | 关键指标 | 预计完成 |
|------|------|------|----------|----------|
| CWM v12 eval | 正常 | 85.4% | acc=57.8% | ~02:15 |
| CWM seed123 eval | 正常 | 84.3% | acc=59.1% | ~02:30 |
| CWM 8B train | 崩溃后重启 | 22.6% | loss=0.45, eval_loss=0.36 | ~May 15 17:00 |
| CLS 8B s123 train | 崩溃后重启 | 40.4% | loss=0.36, eval_loss=0.28 | ~May 15 11:00 |

### 风险提示
两个 8B training 都在 eval 阶段因 DataLoader worker 被 kill 而崩溃（疑似内存不足）。
重启时已设 `dataloader_num_workers=0`（主进程加载），应能避免再次崩溃。需持续关注。
