# diagnose westd bjb1 full status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-bjb1-full-status_20260519T044231_result.json`
- **Structured JSON:** [`fbf7e5ac7cfdeee827e1.json`](../../sessions/fb/fbf7e5ac7cfdeee827e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd-47453 (RTX PRO 6000 96GB × 4)
──────────────────────────────────────────────────────────
[cuda:0,1] 空闲 | 0 MiB, 0% util
[cuda:2,3] 7B zeroshot eval: 运行中 | 65/64 GB, 100% util
           W&B kbt8a170 state=running, 尚无 metrics（刚启动, 评估 134 OOD games）
           启动时间: 12:05 UTC

OOD reeval (l0zohzt5): ❌ crashed，无 metrics，无日志残留

额外进程: generate_scienceworld_sft.py (CPU, pid 755747)

SFT 数据: ✅ 已到位 /root/autodl-tmp/expert_sft/expert_sft_train.jsonl (2460 行, 12MB)

bjb1-17606 (RTX PRO 6000 96GB × 2)
──────────────────────────────────────────────────────────
[cuda:0,1] h=20 训练: step 3/15 | 97GB/98GB, 100% util
           W&B qi8g4f86 state=running
           train success: step1=20.3% → step3=40.6%, pass@8: 68.8% → 87.5%
           速度: init+step1 ≈6.9h, 之后 ≈22min/step
           预计完成: ~15:00-16:00 UTC 今日 (May 19)
```

要点：
- OOD reeval 已崩溃，需要排查或重跑
- 7B zeroshot eval 刚启动几分钟，等结果
- h20 训练正常推进，step 3 success 已到 40.6%

---
