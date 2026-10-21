# fix westd m128 conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_m128_conflict_20260519T044830_result.json`
- **Structured JSON:** [`79d1a47c9d74b082ad3b.json`](../../sessions/79/79d1a47c9d74b082ad3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. Kill 结果** — 成功。进程 463767 及其 wandb 子进程 464073 均已终止，不再存在。

**2. tmux 训练状态** — 正常运行中。PID 459645 在 GPU 1 上运行，当前 step 18550/100000（18.6% 进度），loss ~0.06-0.32，lr 9.26e-05，速度 5.3 sps，一切正常。

**3. Checkpoint 完整性** — 存在两份 checkpoint，大小相同但 **md5 不同**，说明两个进程各自写了一份：
   - `/root/autodl-tmp/.../checkpoints/smart_compress_m128_seed44/checkpoint.pt` — 1.878 GB, 12:47 写入, md5 `a6584f53...`
   - `/root/checkpoints/smart_compress_m128_seed44/checkpoint.pt` — 1.878 GB, 12:48 写入, md5 `6b679fe2...`
   
   两份来自不同进程、不同训练步数，内容不同。tmux 进程（459645）启动更早，其 checkpoint 应该是第一个路径（12:47 时间更接近其运行时长）。第二个路径是被杀进程写的，可安全忽略或删除。

**4. GPU 状态** — GPU 1 现在只有 PID 459645 一个进程（3366 MiB）。GPU 0 上有另一个 python 进程 462076。冲突已解除。

---
