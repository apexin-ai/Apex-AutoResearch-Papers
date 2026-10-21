# ops westd38929 env readiness

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-env-readiness_20260520T181750_result.json`
- **Structured JSON:** [`2872d29f2f4af049afd1.json`](../../sessions/28/2872d29f2f4af049afd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕，**westd-38929 可以立即启动 seed43 sweep**。

### GPU 状态
4 GPU 全部空闲，0% 利用率，0 MiB 显存占用。

### --seed 参数支持
脚本 `eval_openvla_l2norm_libero.py` **已原生支持 `--seed` 参数**：
- 第 48 行：`p.add_argument("--seed", type=int, default=7)`
- 第 55-60 行：`set_seed()` 函数设置 `torch.manual_seed`、`torch.cuda.manual_seed_all`、`np.random.seed`、`random.seed`
- 第 181 行：主流程调用 `set_seed(args.seed)`
- 第 286 行：seed 值写入结果 JSON

用法：`--seed 43` 即可。

### 已有结果（seed42 sweep）
`eval_results/` 下已有 seed42 的 l2norm 结果：`k0_3`、`k0_5`、`k0_9`、`k0_95`（object suite）。

### 注意
第 219 行 `env.seed(0)` 环境 seed 硬编码为 0，不受 `--seed` 控制。如果希望环境初始化也用不同 seed，需改这行为 `env.seed(args.seed)`。不过如果 seed42 sweep 也是这样跑的，保持一致即可。

---
