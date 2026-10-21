# westd-41074 巡检报告

**时间**: 2026-05-22 09:52 UTC

## GPU 总览

| GPU | 显存占用 | PID | 实验 | 状态 | 进度/SR |
|-----|---------|-----|------|------|---------|
| 0 | 0/97887 MiB | 816297 | eval_pi05_l2norm_k085_object_seed42_v3 | **DEAD** | 结果已保存: SR=98.0% (490/500) |
| 1 | 0/97887 MiB | 816380 | eval_pi05_l2norm_k095_object_seed42 | **DEAD** | 结果已保存: SR=98.2% (491/500) |
| 2 | 28555/97887 MiB | 68539 | VTC M96 训练 | **ALIVE** | step 81150/100000 (81.2%) |
| 3 | 27535/97887 MiB | 59671 | VTC M64v6 训练 | **ALIVE** | step 33950/100000 (34.0%) |

## 详情

### GPU 0/1 — Eval 已完成，进程已退出

两个 eval 进程均已完成评测并写入结果 JSON，但随后在 post-eval 阶段因 `lerobot.policies.groot.groot_n1` 的 dataclass 错误崩溃（`TypeError: non-default argument 'backbone_cfg' follows default argument`）。这是 lerobot 包的已知兼容问题，不影响已保存的 eval 结果。

结果文件：
- `eval_results/pi05_l2norm_k0.85_libero_object_seed42.json` — SR=98.0%, 64min
- `eval_results/pi05_l2norm_k0.95_libero_object_seed42.json` — SR=98.2%, 63min

**GPU 0 和 GPU 1 空闲，可以接新实验。**

### GPU 2 — VTC M96 训练

- PID 68539, 启动于 May 20
- 当前 step 81150/100000 (81.2%)
- 速度 0.5 steps/sec, loss ~2.7
- 预计还需 ~10.5 小时完成

### GPU 3 — VTC M64v6 训练

- PID 59671, 启动于 May 21
- 当前 step 33950/100000 (34.0%)
- 速度 0.6 steps/sec, loss ~2.8
- 预计还需 ~30.6 小时完成

### 其他

- tmux session `eval_random_k09_s42` 存在但对应进程已结束（GPU 1 无显存占用）
- HTTP server (PID 584493) 在端口 18765 提供 pi05_libero_finetuned 模型

## Registry 状态建议

两个 PREPARING 状态的实验应更新为 DONE：
- `eval_pi05_l2norm_k085_object_seed42_v3` → DONE (SR=98.0%)
- `eval_pi05_l2norm_k095_object_seed42` → DONE (SR=98.2%)
