# deploy pi05 fix redeploy bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-fix-redeploy-bjb1-32546_20260521T101313_result.json`
- **Structured JSON:** [`77a4c8d1f091109b548a.json`](../../sessions/77/77a4c8d1f091109b548a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**执行摘要**：
1. **Kill**：bjb1-32546 上 12 个进程（6 个 bash 包装 + 6 个 python evaluate.py）全部 SIGKILL，无残留 tmux session
2. **同步代码**：bjb2-40593 打包 99KB tar.gz → scp 到本地 → scp 到 bjb1-32546（绕过 32KB ssh 输出截断限制）
3. **验证一致**：`src/evaluate.py` = 802 行，`predict_action`=3 处，`reset_action_queue`=2 处；`src/pi05_wrapper.py` = 413 行，`action_queue`=6 处，`torch.flip`=1 处
4. **重新部署**：6 个实验全部提交成功，PID 982849–984515，tmux session 列表显示 6 个 session 运行中，模型正在加载（日志显示已进入 PI05 from /root/autodl-tmp/models/pi05_libero_finetuned/ 阶段）

**注意**：日志里 args 字典显示 `'K': 1`（而命令传的是 `--K 10`）。可能是 evaluate.py 中 `vla_only` 模式硬覆盖 K 值或 argparse 配置问题，但与本次部署无关，是代码行为问题。

---
