# ssh comprehensive check kill deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_comprehensive-check-kill-deploy_20260517T120011_result.json`
- **Structured JSON:** [`d3c254712fd74f978f19.json`](../../sessions/d3/d3c254712fd74f978f19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 占用确认完成。两个实验都在正常运行。

```
=== 任务 1：结果检查 ===
1A) obs_only norm03 seed47 @ bjb1-18228: 无结果（进程被 kill 时仅完成加载，未开始 rollout）
1B) perdof norm03 seed44-r2 @ bjb1-32546: 无结果（进程被 kill 时仅完成 task1 的 4/10 rollouts，未生成 JSON）

=== 任务 2：Kill 结果 ===
PID 401104 @ bjb2-28827: DEAD (force killed)
PID 388460 @ bjb2-40593: DEAD (SIGTERM)
PID 429284 @ bjb1-32546: DEAD (force killed)
PID 617632 @ bjb1-18228: DEAD (force killed)

=== 任务 3：GPU 空闲扫描 ===
bjb1-18228: 空闲 [cuda:1], GPU进程数: 3, LIBERO ps count: 9
bjb1-32546: 空闲 [cuda:0], GPU进程数: 5, LIBERO ps count: 14
bjb2-28827: 空闲 [cuda:2], GPU进程数: 5, LIBERO ps count: 13
bjb2-40593: 空闲 [cuda:0], GPU进程数: 0, LIBERO ps count: 0（不部署）

=== 任务 4：部署结果 ===
4a) random-selection: 需要代码修改（evaluate.py 无 random mode，仅支持 crm_perdof/crm_scalar/crm_obs_only/vla_only/reconvla）
4b) perdof norm02 seed47: 部署到 bjb2-28827 cuda:2 PID=404982, GPU占用 5664 MiB ✓
4c) obs_only norm003 seed43: 部署到 bjb1-18228 cuda:1 PID=621126, GPU占用 5664 MiB ✓
```

注意：所有服务器的 LIBERO ps count 远超 4（bjb1-32546=14, bjb2-28827=13），这是因为每个 evaluate.py 进程会 fork 多个子进程（环境 worker）。实际 GPU 占用的独立 eval job 数分别为 3/5/5，与 GPU 卡数匹配。

---
