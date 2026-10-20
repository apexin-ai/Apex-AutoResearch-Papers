# d064 DocRED Full Beam Status Check — Round 4

**时间**: 2026-05-19 22:39 CST

---

## westd-21461 (2x RTX PRO 6000 Blackwell, 98GB)

### GPU 0 — Llama-3.1-8B 级联脚本 (PID 99652)

级联脚本 `d064_gpu0_llama_all_with_greedy.sh` 正常工作（此前担心的 PID bug 未影响执行）。

| 阶段 | 任务 | 状态 | 进度 | 输出文件 | 大小 |
|------|------|------|------|----------|------|
| 1 | Greedy unconstrained | **完成** | 998/998 | `d064_llama_docred_greedy_unconstrained.jsonl` | 9.3 MB |
| 2 | Greedy constrained S1 | **运行中** (PID 112046) | 20/998 | `d064_llama_docred_greedy_constrained.jsonl` | 170 KB |
| 3 | Beam-4 unconstrained | 待启动 | — | — | — |
| 4 | Beam-4 constrained | 待启动 | — | — | — |

- Greedy constrained 于 22:35 启动，4 分钟处理 20 docs，~12s/doc
- **预计完成**: ~3.3h 后 (约 02:00 CST)
- GPU 利用率 86%, 显存 18.3/97.9 GB

### GPU 1 — Qwen-2.5-7B beam-4 unconstrained (PID 98185)

| 任务 | 状态 | 进度 | 输出文件 | 大小 |
|------|------|------|----------|------|
| Beam-4 unconstrained | **运行中** | 929/998 | `d064_qwen_docred_beam4_unconstrained.jsonl` | 8.3 MB |

- 日志最新进度: `[823/998] O'Shaughnessy Dam (Ohio): OK E=13 R=15 21.1s`（日志行数 835，但 JSONL 已有 929 行，日志 flush 滞后）
- 17:08 启动，5.5h 处理 929 docs，~21.3s/doc
- **预计完成**: ~25 min 后 (约 23:05 CST)
- GPU 利用率 66%, 显存 18.9/97.9 GB

**级联后续**: Qwen beam-4 unc 完成后，`d064_gpu1_qwen_con_fixed.sh` (PID 99686) 将自动启动 Qwen beam-4 constrained。

---

## westd-16980 (2x RTX PRO 6000 Blackwell, 98GB)

### GPU 0 — Llama beam-4 unconstrained (PID 647122)

| 任务 | 状态 | 进度 | 输出文件 | 大小 |
|------|------|------|----------|------|
| Beam-4 unconstrained | **运行中** | 48/998 | `d064_llama_docred_beam4_unconstrained_16980.jsonl` | 402 KB |

- 22:27 启动，12 分钟处理 48 docs，~15s/doc
- **预计完成**: ~4h 后 (约 02:40 CST)
- GPU 利用率 92%, 显存 18.3/97.9 GB

### GPU 1 — Llama beam-4 constrained (PID 647334)

| 任务 | 状态 | 进度 | 输出文件 | 大小 |
|------|------|------|----------|------|
| Beam-4 constrained S1 | **运行中** | 41/998 | `d064_llama_docred_beam4_constrained_16980.jsonl` | 339 KB |

- 22:28 启动，11 分钟处理 41 docs，~16s/doc
- **预计完成**: ~4.3h 后 (约 03:00 CST)
- GPU 利用率 0% (可能在 CPU 阶段/刚完成一个 batch), 显存 18.3/97.9 GB

---

## 汇总

| 服务器 | GPU | 模型 | 任务 | 进度 | 预计完成 |
|--------|-----|------|------|------|----------|
| 21461 | 0 | Llama | Greedy unc | **998/998 完成** | — |
| 21461 | 0 | Llama | Greedy con S1 | 20/998 (2.0%) | ~02:00 |
| 21461 | 0 | Llama | Beam-4 unc | 待启动 | ~06:00+ |
| 21461 | 0 | Llama | Beam-4 con | 待启动 | ~10:00+ |
| 21461 | 1 | Qwen | Beam-4 unc | 929/998 (93.1%) | ~23:05 |
| 21461 | 1 | Qwen | Beam-4 con | 待启动 | ~明早 |
| 16980 | 0 | Llama | Beam-4 unc | 48/998 (4.8%) | ~02:40 |
| 16980 | 1 | Llama | Beam-4 con | 41/998 (4.1%) | ~03:00 |

## 需要注意的问题

1. **21461 GPU 0 级联正常工作**: 此前担心的 PID bug 并未阻止执行——greedy unc 完成后成功自动启动了 greedy con。但级联中的 beam-4 阶段（步骤 3-4）与 16980 上的任务**重复**（输出路径不同：`d064_llama_docred_beam4_unconstrained.jsonl` vs `_16980.jsonl`）。
2. **16980 任务已重启**: 此前检查时分别为 20/998 和 16/998，现在进程启动时间为 22:27-22:28，是新启动的进程（之前的可能异常退出或被手动重启）。如使用 `--skip_on_error` 且输出文件被覆盖，之前的进度已丢失。
3. **16980 GPU 1 利用率 0%**: 可能是瞬时现象（采样时恰好在 CPU 处理阶段），需关注是否真的在正常推理。
4. **Qwen beam-4 unc 即将完成**: ~25 分钟后完成，之后 Qwen beam-4 con 将自动启动，预计额外需要 ~5-6 小时。
