# MVP Pilot Status Report

- 进程状态：**ALIVE** (PID 98594, 已运行 3h53m50s)
- ACDC 进度：**13.1%** (4255/32491 edges evaluated, ~24.3 it/s, ETA ~19 min)
  - 已移除 4236 条边，当前保留 19 条
  - 当前处理：Layer 11 attention heads 的输入边
- 结果：mvp_results.json 尚未生成（ACDC 仍在运行）
- GPU-5 状态：utilization 100%, memory 9311/24564 MiB (37.9%)
- 时间戳：2026-05-12T21:00 UTC (approx)

## 备注
- EAP-IG 和 Edge Pruning 阶段已完成（cache 文件存在：cache_eap_ig.json, cache_edge_pruning.json）
- 进程工作目录为 /root/min_necessary_circuit_css（非 /root/structfuse-mvp）
- 日志文件为 mvp_output.log（非 nohup.out）
- 预计 ACDC 阶段总耗时约 22 分钟，约 19 分钟后完成
