# 6/1 Feishu 恢复后第一批消息（预写，copy-paste 发送）

## 1. 给用户：标题决策 + 服务器 + 审稿确认

```
**diff_collision_sdf 进展汇报 + 3 项确认**

服务器离线期间完成了大量非 GPU 工作：
- 论文转 ICRA 双栏格式 (6+1 页) + 6 项 offensive 质量升级
- Reviewer 全文审查 PASS + negative results 威胁分析 PASS
- Demo curation 标注脚本 + RoboCasa eval + fine-tune config 全部就绪
- 服务器恢复执行 checklist 已备好

**需要确认 3 件事**：

1. **服务器**：westd-35807 和 westd-45947 均 Connection refused，请恢复开机。恢复后立即启动 D049 ablation（Pi0.5 baseline 多 seed 10 GPU-hrs 为最高优先）。

2. **论文标题**：Reviewer 建议去掉 "98%"（审稿人可能挑战），候选：
   - A: "Rethinking VLA Safety: Why Demonstrations, Not Geometry, Drive Collision Avoidance"
   - B: "The Illusion of Learned Safety: Evaluating Collision Avoidance in VLA Models"  
   - C: 保持现标题 "When 98% of Collision Avoidance is an Illusion"

3. **审稿**：已提交给 Review Director，请在飞书确认 review mode（推荐 fresh——论文大改后独立审查更有价值）。

4. **CoRL 2026**：DDL 5/28 已过，是否已提交？
```

## 2. 给 Manager：服务器恢复跟进

```
[diff_collision_sdf] 服务器恢复跟进

5/29 报告的 westd-35807/45947 离线问题仍未解决。Feishu 配额已恢复，再次报告：

- 两台服务器 Connection refused，2 张 GPU 空置 3 天
- 所有非 GPU 工作已完成，服务器恢复后可立即启动实验
- 是否能协助联系用户恢复服务器？或有其他可用服务器临时调配？
```
