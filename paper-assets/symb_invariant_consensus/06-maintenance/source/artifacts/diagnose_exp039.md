# exp-039-14b-pw600-16639 诊断报告

## 结论：实验已成功完成，cron 监控误报

### a) 根因

**不是失败，是正常完成后进程退出。** cron 监控检测到进程不再运行，连续 5 次未找到 running process 或 sentinel/W&B 标记，自动标记为 failed。实际上实验已跑完 600/600，脚本正常打印 `FULL_MVP_DONE` 后退出。

- 无 OOM（dmesg 无相关记录，GPU 0 内存已释放至 0MiB）
- 无脚本错误（grep ERROR/FAIL/Traceback/Exception/OOM 全为 0 匹配）
- 无 vLLM 崩溃（vllm_exp032.log 末尾全是 200 OK 响应，无异常）

### b) 中间结果状态

- **intermediates/**: 600 个 JSON 文件（每个 problem 一个），完整保存
- **results.json**: 完整，包含 `summary` 和 `results`（600 条）
- 路径: `/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/`
- results.json 最后修改时间: 2026-05-19 12:44:55

### c) Resume 状态

无需 resume，实验已完成。

### d) 实验结果（可直接使用）

| 指标 | 值 |
|------|------|
| SICA accuracy | 71.5% (429/600) |
| SC accuracy | 73.5% (441/600) |
| Extraction rate | 99.2% |
| Contradiction rate | 0.6% |
| Problems with contradictions | 108/600 |
| Total constraints extracted | 94,306 |
| Total unique constraints | 22,036 |
| k (samples) | 12 |
| Total wall time | 659.6 min (11.0 hr) |

Per-level: OWA-D5 only (SICA=71.5%, SC=73.5%, n=600)

### e) 服务器当前状态

- GPU 0: 空闲（0MiB / 97,887MiB）
- GPU 1-3: 被其他实验使用（exp028b, exp033, exp048）
- tmux session `exp032`: 已不存在（脚本完成后自动关闭）
- 磁盘: overlay 44%, /dev/sda2 40%，充裕

### f) 建议

cron 监控对推理类实验（有限时间完成后退出）的判断逻辑需要改进：应检查输出目录是否有完成标记（如 `FULL_MVP_DONE` 在 log 中，或 results.json 中的 summary.n_problems == total），而非仅检测进程存活。
