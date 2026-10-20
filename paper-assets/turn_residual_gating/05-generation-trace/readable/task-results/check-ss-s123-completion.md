# check ss s123 completion

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ss_s123_completion_20260523T172618_result.json`
- **Structured JSON:** [`557b878cc798110afaa5.json`](../../sessions/55/557b878cc798110afaa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。汇报如下：

---

## 训练结果：SS s123 — 成功 ✓

**最终 metrics (Epoch 2 完成)：**
- Avg Loss: **0.9316** (NTP: 0.9307, GAR: 0.0009, DIV: 0.0000)
- Gate mean: **0.9505**, std=0.0508, min=0.7383, max=1.0000
- SS 使用率: 8899/24000 (**37.1%**)，fallback=0
- 训练时长: **38773s** (~10.8h)
- 3 个 epoch checkpoint 齐全 (epoch_0/1/2 + gate_params.pt + lora)
- 保存路径: `checkpoints/tg_v8b_ss_s123/` → 已链接到 `runs/d048_ss_s123/`

**Gate profile (step 3000):** L5 最低 (0.738)，L27 最高 (1.000)，与其他 seed 一致。

---

## GPU 链状态：已自动启动 ✓

- **等待脚本 PID 94251**: 已退出
- **PID 84793 退出时间**: 01:24:19 CST
- **gpu_chain_next.sh**: 01:24:29 自动启动，PID 108997
- **当前运行**: Step 1/7 — SS s123 eval (TF + AR N=50)
  - PID **109385**: `eval_phase2_gar.py --gate-type threadgate --checkpoint-dir runs/d048_ss_s123/epoch_2 --gar-variant ours --gate-profile`
  - 进度: Conv ~116/200（AR eval 阶段，PPL ~2.55）
  - GPU: 37.7GB / 97.9GB, 60% util

---

## 总结

训练成功完成，GPU 链已自动接续运行 eval，无需手动干预。链共 7 步，当前在第 1 步。

---
