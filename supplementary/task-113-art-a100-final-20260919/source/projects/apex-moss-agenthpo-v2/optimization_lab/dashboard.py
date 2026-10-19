from __future__ import annotations

import html
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from optimization_lab.campaign import P1_ROUNDS
from optimization_lab.registry import ExperimentRegistry


PLAN = (
    ("P0", "评分器与环境门禁"),
    ("P1", "固定 Harness 对照（含同预算组）"),
    ("P2", "每道任务三条专用 Harness 谱系"),
    ("P3", "冻结版本的干净环境确认"),
)

TASK_LABELS = {
    "kernelbench_layernorm": "LayerNorm",
    "kernelbench_matmul_sigmoid_sum": "Matmul + Sigmoid + Sum",
}
BASELINE_LABELS = {
    "generic_zero_shot": "通用零样本做法",
    "equal_budget_general": "同预算通用工作流",
    "manual_naive": "人工设计的朴素流程",
}
BLOCKER_LABELS = {
    "p0_clean_confirmation_missing": "尚缺全新 GPU 容器中的 P0 复现确认",
    "executor_model_missing": "尚未锁定本次实验使用的做题模型",
    "model_call_cap_missing": "尚未批准每条路线最多可调用模型多少次",
    "gpu_seconds_cap_missing": "尚未批准每条路线最多可使用多少 GPU 时间",
    "api_dollar_cap_missing": "尚未批准 API 总费用上限",
    "gpu_dollar_cap_missing": "尚未批准 GPU 总费用上限",
}
_PRIVATE_LOG_RE = re.compile(r"private_evaluator(?:/[A-Za-z0-9._~+@%=:,-]+)*")
_ABSOLUTE_PATH_RE = re.compile(
    r"(?<![\w.])/(?:[A-Za-z0-9._~+@%=:,-]+/)+[A-Za-z0-9._~+@%=:,-]*"
)


class Dashboard:
    """Self-contained, auto-refreshing experiment status page."""

    def __init__(self, path: Path):
        self.path = path.resolve()

    def render(self, registry: ExperimentRegistry) -> None:
        events = registry.read_events()
        candidate_events = [
            event
            for event in self._effective_candidate_events(events)
            if str(event["payload"]["feedback"].get("candidate_id", "")).startswith(
                ("p1-", "p2-")
            )
        ]
        phase_events = [event for event in events if event["event_type"] == "phase_changed"]
        retired_tasks = {
            event["payload"]["task_id"]
            for event in events
            if event["event_type"] == "task_retired"
        }
        current_phase_event = phase_events[-1]["payload"] if phase_events else {}
        current_phase = current_phase_event.get("phase", "P0")
        current_phase_status = current_phase_event.get("status", "in_progress")
        campaign = self._load_campaign(registry.root / "campaign_plan.json")
        p0_clean_confirmed = any(
            event["event_type"] == "p0_clean_environment_confirmed"
            and event["payload"].get("status") == "ready"
            for event in events
        )
        campaign_ready = bool(campaign and campaign.get("execution_ready") is True)
        if current_phase == "P1" and current_phase_status == "completed":
            current_phase_label = "P1 已完成，P2 待授权"
        elif current_phase == "P2" and current_phase_status == "completed":
            current_phase_label = "P2 已完成，P3 待授权"
        elif current_phase == "P0" and p0_clean_confirmed:
            current_phase_label = (
                "P0 已通过，P1 待启动"
                if campaign_ready
                else "P0 已通过，P1 待授权"
            )
        else:
            current_phase_label = current_phase
        phase_explanation = (
            "P2 的每一轮都会产生新版 Harness，再由它生成和评分 Kernel；六条谱系彼此隔离。"
            if current_phase == "P2"
            else "P1 比较两道任务的六组固定 Harness；每轮改变的是 Kernel 代码，Harness 本身不变。"
        )
        resources = [event for event in events if event["event_type"] == "resource_checked"]
        tasks: dict[str, dict[str, Any]] = {}
        for event in candidate_events:
            payload = event["payload"]
            card = payload["feedback"]
            task_id = card["task_id"]
            summary = tasks.setdefault(
                task_id, {"runs": 0, "valid": 0, "correct": 0, "best": None}
            )
            summary["runs"] += 1
            summary["valid"] += int(card["valid_run"])
            summary["correct"] += int(card["correct"])
            speedup = card.get("speedup_vs_eager")
            if task_id not in retired_tasks and speedup is not None and (
                summary["best"] is None or speedup > summary["best"]
            ):
                summary["best"] = speedup

        plan_rows = "".join(
            f"<tr><td>{phase}</td><td>{html.escape(label)}</td><td>{self._phase_state(phase, current_phase, current_phase_status, p0_clean_confirmed, campaign_ready)}</td></tr>"
            for phase, label in PLAN
        )
        task_row_parts = []
        for task, data in sorted(tasks.items()):
            if task in retired_tasks:
                best = "已淘汰，不计分"
            else:
                best = "—" if data["best"] is None else f"{data['best']:.2f}×"
            task_row_parts.append(
                "<tr>"
                f"<td>{html.escape(self._task_label(task))}</td><td>{data['runs']}</td><td>{data['valid']}</td><td>{data['correct']}</td>"
                f"<td>{best}</td>"
                "</tr>"
            )
        task_rows = "".join(task_row_parts) or '<tr><td colspan="5">尚未运行候选</td></tr>'
        resource_rows = "".join(
            "<tr>"
            f"<td>{html.escape(self._public_text(event['payload'].get('name', '未知')))}</td>"
            f"<td>{html.escape(self._public_text(event['payload'].get('status', '未知')))}</td>"
            f"<td>{html.escape(self._public_text(event['payload'].get('detail', '')))}</td>"
            "</tr>"
            for event in resources[-8:]
        ) or '<tr><td colspan="3">等待资源预检</td></tr>'
        recent_rows = "".join(
            self._event_row(event, retired_tasks) for event in reversed(events[-15:])
        )
        recent_rows = recent_rows or '<tr><td colspan="3">实验刚初始化</td></tr>'
        campaign_section = (
            self._campaign_section(campaign, events) if campaign else ""
        )
        updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        page = f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="5">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MOSS KernelBench 实验看板</title>
<style>
body{{font-family:system-ui,-apple-system,sans-serif;margin:0;background:#f5f7fb;color:#18212f}}
main{{max-width:1100px;margin:32px auto;padding:0 20px}}h1{{margin-bottom:4px}}
.sub{{color:#627087;margin-top:0}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:16px}}
section{{background:white;border:1px solid #dfe5ee;border-radius:12px;padding:18px;box-shadow:0 3px 12px #1c2b4010}}
table{{width:100%;border-collapse:collapse}}th,td{{padding:9px 8px;border-bottom:1px solid #edf0f5;text-align:left;vertical-align:top}}
th{{color:#536176;font-size:13px}}.pill{{display:inline-block;background:#e8f1ff;color:#175bb5;border-radius:99px;padding:5px 10px}}
.foot{{color:#738096;font-size:13px;margin-top:18px}}code{{font-family:ui-monospace,monospace}}
</style></head><body><main>
<h1>MOSS KernelBench 实验看板</h1>
<p class="sub"><span class="pill">当前阶段：{html.escape(current_phase_label)}</span> {html.escape(phase_explanation)} 页面每5秒自动刷新。</p>
<div class="grid"><section><h2>实验计划</h2><table><thead><tr><th>阶段</th><th>目标</th><th>状态</th></tr></thead><tbody>{plan_rows}</tbody></table></section>
<section><h2>资源状态</h2><table><thead><tr><th>资源</th><th>状态</th><th>说明</th></tr></thead><tbody>{resource_rows}</tbody></table></section></div>
{campaign_section}
<section><h2>Kernel 候选进度</h2><table><thead><tr><th>任务</th><th>已评分</th><th>有效评分</th><th>正确</th><th>历史最佳</th></tr></thead><tbody>{task_rows}</tbody></table></section>
<section><h2>最近记录</h2><table><thead><tr><th>时间</th><th>事件</th><th>摘要</th></tr></thead><tbody>{recent_rows}</tbody></table></section>
<p class="foot">最后更新：{updated}　｜　事实来源：<code>ledger.jsonl</code>　｜　无效环境运行不计为候选失败。</p>
</main></body></html>"""
        self._write_atomic(page)

    @staticmethod
    def _phase_state(
        phase: str,
        current: str,
        current_status: str = "in_progress",
        p0_clean_confirmed: bool = False,
        campaign_ready: bool = False,
    ) -> str:
        if current_status == "completed":
            order = [item[0] for item in PLAN]
            if order.index(phase) <= order.index(current):
                return "已完成"
            if phase == "P2" and current == "P1":
                return "等待授权"
            if phase == "P3" and current == "P2":
                return "等待授权"
            return "等待"
        if current == "P0" and p0_clean_confirmed:
            if phase == "P0":
                return "已完成"
            if phase == "P1":
                return "待启动" if campaign_ready else "等待授权"
            return "等待"
        order = [item[0] for item in PLAN]
        if order.index(phase) < order.index(current):
            return "已完成"
        if phase == current:
            return "进行中"
        return "等待"

    @staticmethod
    def _event_row(event: dict[str, Any], retired_tasks: set[str]) -> str:
        payload = event["payload"]
        if event["event_type"] in {
            "candidate_evaluated",
            "candidate_evaluation_corrected",
        }:
            card = payload["feedback"]
            speed = card.get("speedup_vs_eager")
            summary = f"{card['candidate_id']} · {card['outcome']}"
            if event["event_type"] == "candidate_evaluation_corrected":
                summary += " · 分类已纠正"
            if card["task_id"] in retired_tasks:
                summary += " · 已淘汰，不计分"
            elif speed is not None:
                summary += f" · {speed:.2f}×"
        else:
            summary = payload.get("detail") or payload.get("status") or payload.get("phase") or ""
        return (
            "<tr>"
            f"<td>{html.escape(event['recorded_at'][11:19])}</td>"
            f"<td>{html.escape(event['event_type'])}</td>"
            f"<td>{html.escape(Dashboard._public_text(summary))}</td>"
            "</tr>"
        )

    @staticmethod
    def _effective_candidate_events(
        events: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        effective: dict[tuple[str, str], dict[str, Any]] = {}
        for event in events:
            if event["event_type"] not in {
                "candidate_evaluated",
                "candidate_evaluation_corrected",
            }:
                continue
            feedback = event["payload"].get("feedback", {})
            key = (
                str(feedback.get("task_id", "")),
                str(feedback.get("candidate_id", "")),
            )
            if all(key):
                effective[key] = event
        return list(effective.values())

    @staticmethod
    def _load_campaign(path: Path) -> dict[str, Any] | None:
        if not path.is_file():
            return None
        try:
            campaign = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        return campaign if isinstance(campaign, dict) else None

    @classmethod
    def _campaign_section(
        cls,
        campaign: dict[str, Any],
        events: list[dict[str, Any]],
    ) -> str:
        ready = campaign.get("execution_ready") is True
        readiness = "已满足开跑条件" if ready else "尚未获准执行"
        explanation = (
            "所有开跑条件已经写入计划；实际结果仍只以追加式实验账本为准。"
            if ready
            else "矩阵已经冻结，但以下条件补齐前不会调用做题模型或开始正式 GPU 刷分。"
        )
        blockers = campaign.get("blockers")
        blocker_items = []
        if isinstance(blockers, list):
            for blocker in blockers:
                blocker_items.append(
                    f"<li>{html.escape(BLOCKER_LABELS.get(str(blocker), '尚有一项开跑条件未完成'))}</li>"
                )
        blocker_list = (
            f"<ul>{''.join(blocker_items)}</ul>" if blocker_items else ""
        )

        baselines = [
            lane for lane in campaign.get("baselines", []) if isinstance(lane, dict)
        ] if isinstance(campaign.get("baselines"), list) else []
        lane_results = cls._effective_lane_results(events)
        baseline_rows_parts = []
        for lane in baselines:
            lane_id = str(lane.get("lane_id", ""))
            kind = str(lane.get("kind", ""))
            planned = P1_ROUNDS.get(kind, 0)
            results = lane_results.get(lane_id, [])
            completed = len(results)
            if completed == 0:
                state = f"待运行 0/{planned}"
            elif completed >= planned:
                state = f"已完成 {completed}/{planned}"
            else:
                state = f"进行中 {completed}/{planned}"
            if results:
                state += f"；最近：{results[-1].get('outcome', '未知')}"
                scores = [
                    float(result["speedup_vs_eager"])
                    for result in results
                    if result.get("correct")
                    and result.get("speedup_vs_eager") is not None
                ]
                state += (
                    f"；最好：{max(scores):.2f}×"
                    if scores
                    else "；尚无正确候选"
                )
            baseline_rows_parts.append(
                "<tr>"
                f"<td>{html.escape(cls._task_label(lane.get('task_id')))}</td>"
                f"<td>{html.escape(BASELINE_LABELS.get(kind, '冻结对照流程'))}</td>"
                "<td>固定，不迭代</td>"
                f"<td>{html.escape(state)}</td>"
                "</tr>"
            )
        baseline_rows = "".join(baseline_rows_parts) or '<tr><td colspan="4">尚未写入对照组计划</td></tr>'

        lineages = [
            lane for lane in campaign.get("lineages", []) if isinstance(lane, dict)
        ] if isinstance(campaign.get("lineages"), list) else []
        lineage_counts: dict[str, int] = {}
        p2_results = cls._effective_p2_lane_results(events)
        p2_completed = {
            str(event["payload"].get("lane_id", "")): event["payload"]
            for event in events
            if event["event_type"] == "p2_lineage_completed"
        }
        lineage_rows_parts = []
        for lane in lineages:
            task_id = str(lane.get("task_id", ""))
            lineage_id = str(lane.get("lineage_id", ""))
            lane_id = f"p2:{task_id}:{lineage_id}"
            lineage_counts[task_id] = lineage_counts.get(task_id, 0) + 1
            max_rounds = lane.get("max_rounds")
            rounds = max_rounds if isinstance(max_rounds, int) and max_rounds > 0 else "—"
            results = p2_results.get(lane_id, [])
            completed = p2_completed.get(lane_id)
            last_harness = (
                str(results[-1].get("harness_version_id", "—"))
                if results
                else "—"
            )
            scores = [
                float(result["feedback"]["speedup_vs_eager"])
                for result in results
                if result.get("feedback", {}).get("correct")
                and result.get("feedback", {}).get("speedup_vs_eager") is not None
            ]
            if completed is not None:
                state = f"已停止 {len(results)}/{rounds}；Harness {last_harness}"
            elif results:
                state = f"进行中 {len(results)}/{rounds}；Harness {last_harness}"
            else:
                state = f"待运行 0/{rounds}"
            if scores:
                state += f"；最好：{max(scores):.2f}×"
            lineage_rows_parts.append(
                "<tr>"
                f"<td>{html.escape(cls._task_label(task_id))}</td>"
                f"<td>独立路线 {lineage_counts[task_id]}（最多 {rounds} 轮）</td>"
                f"<td>{html.escape(state)}</td>"
                "</tr>"
            )
        lineage_rows = "".join(lineage_rows_parts) or '<tr><td colspan="3">尚未写入专用路线计划</td></tr>'

        experiment_starts = [
            event
            for event in events
            if event["event_type"] == "generation_started"
            and str(event["payload"].get("candidate_id", "")).startswith(
                ("p1-", "p2-")
            )
        ]
        experiment_cards = [
            event["payload"]["feedback"]
            for event in cls._effective_candidate_events(events)
            if str(event["payload"]["feedback"].get("candidate_id", "")).startswith(
                ("p1-", "p2-")
            )
        ]
        model_calls = str(len(experiment_starts))
        gpu_seconds = cls._number(
            sum(float(card.get("gpu_seconds", 0.0)) for card in experiment_cards)
        )
        return (
            '<section><h2>正式实验矩阵与开跑门禁</h2>'
            f'<p><span class="pill">{readiness}</span> {explanation}</p>'
            f"{blocker_list}"
            f'<p><strong>当前消耗：</strong>模型调用：{model_calls} 次　｜　GPU 计时消耗：{gpu_seconds} 秒</p>'
            f"<h3>P1：固定 Harness 对照（{len(baselines)} 条，其中两条为同预算通用流程）</h3>"
            f'<table><thead><tr><th>任务</th><th>对照做法</th><th>Harness</th><th>Kernel 候选状态</th></tr></thead><tbody>{baseline_rows}</tbody></table>'
            f"<h3>P2：专用 Harness 独立进化（{len(lineages)} 条）</h3>"
            f'<table><thead><tr><th>任务</th><th>独立路线</th><th>当前状态</th></tr></thead><tbody>{lineage_rows}</tbody></table>'
            "</section>"
        )

    @staticmethod
    def _effective_lane_results(
        events: list[dict[str, Any]],
    ) -> dict[str, list[dict[str, Any]]]:
        effective: dict[tuple[str, str], dict[str, Any]] = {}
        order: list[tuple[str, str]] = []
        for event in events:
            if event["event_type"] not in {
                "lane_candidate_completed",
                "candidate_evaluation_corrected",
            }:
                continue
            payload = event["payload"]
            lane_id = str(payload.get("lane_id", ""))
            candidate_id = str(payload.get("candidate_id", ""))
            if not lane_id or not candidate_id.startswith("p1-"):
                continue
            key = (lane_id, candidate_id)
            if key not in effective:
                order.append(key)
            effective[key] = payload.get("feedback", {})
        by_lane: dict[str, list[dict[str, Any]]] = {}
        for lane_id, candidate_id in order:
            by_lane.setdefault(lane_id, []).append(effective[(lane_id, candidate_id)])
        return by_lane

    @staticmethod
    def _effective_p2_lane_results(
        events: list[dict[str, Any]],
    ) -> dict[str, list[dict[str, Any]]]:
        effective: dict[tuple[str, str], dict[str, Any]] = {}
        order: list[tuple[str, str]] = []
        for event in events:
            if event["event_type"] not in {
                "p2_candidate_completed",
                "candidate_evaluation_corrected",
            }:
                continue
            payload = event["payload"]
            lane_id = str(payload.get("lane_id", ""))
            candidate_id = str(payload.get("candidate_id", ""))
            if not lane_id.startswith("p2:") or not candidate_id.startswith("p2-"):
                continue
            key = (lane_id, candidate_id)
            if key not in effective:
                order.append(key)
            if event["event_type"] == "candidate_evaluation_corrected":
                previous = effective.get(key, {})
                effective[key] = {**previous, **payload}
            else:
                effective[key] = payload
        by_lane: dict[str, list[dict[str, Any]]] = {}
        for lane_id, candidate_id in order:
            by_lane.setdefault(lane_id, []).append(effective[(lane_id, candidate_id)])
        return by_lane

    @staticmethod
    def _task_label(value: Any) -> str:
        task_id = str(value or "")
        return TASK_LABELS.get(task_id, "已冻结任务")

    @staticmethod
    def _number(value: Any) -> str:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return "未记录"
        return f"{value:g}"

    @staticmethod
    def _public_text(value: Any) -> str:
        text = str(value)
        text = _PRIVATE_LOG_RE.sub("[内部评测记录]", text)
        return _ABSOLUTE_PATH_RE.sub("[内部路径]", text)

    def _write_atomic(self, content: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(dir=self.path.parent, suffix=".html.tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(self.path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise
