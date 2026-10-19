# collect multiscale eval all seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_multiscale-eval-all-seeds_20260517T205921_result.json`
- **Structured JSON:** [`080551e865b34cf910e0.json`](../../sessions/08/080551e865b34cf910e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验已完成。汇总如下：

---

## Multi-Scale K=1 CRM Eval 结果

### seed=42 (bjb2-28827, status=完成):
```
overall SR = 12/100 (12%)
alphabet_soup:      0/10
cream_cheese:       0/10
salad_dressing:     1/10
bbq_sauce:          2/10
ketchup:            0/10
tomato_sauce:       3/10  ★
butter:             1/10
milk:               0/10
chocolate_pudding:  3/10  ★
orange_juice:       2/10
```

### seed=43 (bjb1-32546, status=完成):
```
overall SR = 9/100 (9%)
alphabet_soup:      0/10
cream_cheese:       0/10
salad_dressing:     1/10
bbq_sauce:          2/10
ketchup:            0/10
tomato_sauce:       2/10  ★
butter:             0/10
milk:               0/10
chocolate_pudding:  2/10  ★
orange_juice:       2/10
```

### seed=44 (bjb1-32546, status=完成):
```
overall SR = 10/100 (10%)
alphabet_soup:      0/10
cream_cheese:       0/10
salad_dressing:     2/10
bbq_sauce:          1/10
ketchup:            0/10
tomato_sauce:       1/10  ★
butter:             0/10
milk:               0/10
chocolate_pudding:  4/10  ★
orange_juice:       2/10
```

### seed=43-r2 (bjb1-18228, status=完成):
```
overall SR = 9/100 (9%)
alphabet_soup:      0/10
cream_cheese:       0/10
salad_dressing:     1/10
bbq_sauce:          2/10
ketchup:            0/10
tomato_sauce:       2/10  ★
butter:             0/10
milk:               0/10
chocolate_pudding:  2/10  ★
orange_juice:       2/10
```

### seed=44-r2 (bjb1-18228, status=完成):
```
overall SR = 10/100 (10%)
alphabet_soup:      0/10
cream_cheese:       0/10
salad_dressing:     2/10
bbq_sauce:          1/10
ketchup:            0/10
tomato_sauce:       1/10  ★
butter:             0/10
milk:               0/10
chocolate_pudding:  4/10  ★
orange_juice:       2/10
```

---

## 重点关注 (chocolate_pudding & tomato_sauce)

| seed | chocolate_pudding | tomato_sauce |
|------|:-:|:-:|
| 42 | 3/10 | 3/10 |
| 43 | 2/10 | 2/10 |
| 44 | 4/10 | 1/10 |
| 43-r2 | 2/10 | 2/10 |
| 44-r2 | 4/10 | 1/10 |

chocolate_pudding 是 K=1 CRM 表现最好的 task (avg 3.0/10)。tomato_sauce 次之 (avg 1.8/10)。

**注意：** seed43-r2 与 seed43 结果完全一致，seed44-r2 与 seed44 也完全一致（per-task 数字相同）。这两对是同一次 eval 的结果拷贝或完全确定性的重跑。

---

## 附加检查

**OpenVLA eval (bjb1-18228):** 正在运行。`eval-openvla-object-vla-only-seed42-v2` 启动于 04:57，cuda:1 占用 15.8GB。同时 flash-attn 正在编译中。

**GPU 空闲状态：**
| Server | GPU0 | GPU1 | GPU2 | GPU3 | GPU4 | GPU5 |
|--------|------|------|------|------|------|------|
| bjb2-28827 | **空闲**(1MB) | 5.2GB | 3.3GB | 5.2GB | 2.9GB | 5.2GB |
| bjb1-32546 | 2.9GB | 1.9GB | 2.4GB | 2.4GB | **空闲**(2MB) | 2.9GB |
| bjb1-18228 | 4.7GB | 15.8GB(OpenVLA) | 5.7GB | **空闲**(4MB) | — | — |

---
