# urgent full status check all experiments

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_full_status_check_all_experiments_20260521T203550_result.json`
- **Structured JSON:** [`21bf7023ca3373828701.json`](../../sessions/21/21bf7023ca3373828701.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full summary:

```
=== 实验状态 ===

1. len_penalty (westd 0,1): ✅ 完成
   - 进程: PID 495138 已退出, EXIT_CODE=0, 总耗时 ~2h40m
   - 进度: 7/7 步完成 + final validation
   
   val success 趋势:    step0=6.25%  → step7=28.13%  (↑)
   val resp_len 趋势:   step0=8600   → step7=7598    (↓ 仅减 12%)
   train success:       step1=31.25% (之后中间步被截断)
   train/resp_len:      step1=1992   (penalty 在 train 上生效)
   rollout resp_len:    step1=10319  → step7=14284   (↑ 持续膨胀)
   
   判断: ❌ 未通过
   - val resp_len = 7598 >> 2000 阈值 (FAIL)
   - val success = 28.13% < 30% 阈值 (FAIL, 差 1.87%)
   - 结论: length penalty 效果不足，只把 val 从 8600 压到 7598，远未达标

2. high_kl (bjb1 0,1): 🔄 进行中
   - 进程: GPU 活跃 (77.8 GB used, 71% util), 无 EXIT_CODE
   - 进度: 已完成 step 5/7 (含 val), 正在跑 step 6 或 7
   - kl_coef = 0.1 (len_penalty 的 10 倍)
   
   val success 趋势:    step0=15.63% → step5=28.13%  (↑ 持续改善)
   val resp_len 趋势:   step0=5575   → step5=5353    (→ 基本稳定)
   train success:       step1=15.63% → step5=13.28%  (→ 稳定偏低)
   rollout resp_len:    step1=... → step5=13169       (↑ 膨胀)
   
   预计完成: ~35-70 min 后 (每步 ~35min)

3. seed8 (westd 2,3): 🔄 进行中
   - 进程: GPU 活跃 (45.2/46.3 GB, 100% util), 已运行 4h25m
   - 进度: step 9/15 (60%)
   
   val success 趋势:    step0=31.25% → step5=28.13%  (↓ 略降)
   val resp_len 趋势:   step0=2469   → step5=3162    (↑ 缓慢增长)
   train success:       step1=35.9%  → step9=10.9%   (↓↓ 急剧下降!)
   train resp_len:      step1=1784   → step9=11569   (↑↑ 6.5 倍膨胀!)
   rollout resp_len:    step1=9879   → step9=14869   (↑ 逼近 16K 上限)
   
   ⚠️ 严重信号: train success 从 36% 暴跌到 11%, 同时 resp_len 
   从 1784 → 11569, 经典的 response length 膨胀 / reward hacking
   
   预计完成: ~3h26m 后 (ETA ~07:30 UTC)

=== GPU 状态 ===
westd: GPU 0=[0 MiB, 0%]  GPU 1=[0 MiB, 0%]  GPU 2=[45169 MiB, 100%]  GPU 3=[46285 MiB, 100%]
bjb1:  GPU 0=[77809 MiB, 71%]  GPU 1=[77811 MiB, 68%]

=== 空闲 GPU ===
westd cuda:0, cuda:1  ← len_penalty 完成后已释放
```

**关键发现:**
- len_penalty 未达标 — penalty 强度不够，resp_len 只从 8600 降到 7598
- high_kl 趋势最健康 — val success 持续上升，resp_len 保持稳定在 5300-5500
- seed8 正在 reward hack — train success 崩塌 + resp_len 爆炸，后 6 步可能继续恶化

---
