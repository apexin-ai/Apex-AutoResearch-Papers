from __future__ import annotations

import html
import json
import math
import os
import tempfile
from pathlib import Path
from typing import Any

from optimization_lab.registry import ExperimentRegistry


STRATEGY_LABELS = {
    "profile_exploit": "分析强解",
    "architecture_reset": "架构重建",
    "counterfactual": "反向假设",
    "recombinant_frontier": "前沿重组",
}
TASK_LABELS = {
    "kernelbench_layernorm": "LayerNorm",
    "kernelbench_matmul_sigmoid_sum": "Matmul + Sigmoid + Sum",
}


class P2bDashboard:
    """Disposable public view derived only from the append-only P2b ledger."""

    def __init__(self, output_path: Path):
        self.output_path = output_path.resolve()

    def render(self, registry: ExperimentRegistry) -> None:
        plan_path = registry.root / "p2b_plan.json"
        if not plan_path.is_file():
            return
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        events = registry.read_events()
        rounds: dict[str, list[dict[str, Any]]] = {}
        for event in events:
            if event["event_type"] == "p2b_round_completed":
                rounds.setdefault(str(event["payload"]["lane_id"]), []).append(
                    event["payload"]
                )
        score_attempts = _score_attempts(events, rounds)
        completed = {
            str(event["payload"]["lane_id"])
            for event in events
            if event["event_type"] == "p2b_lane_completed"
        }
        phase_complete = any(
            event["event_type"] == "p2b_phase_changed"
            and event["payload"].get("status") == "completed"
            for event in events
        )
        phase_label = "P2B 已完成，P3 待授权" if phase_complete else "P2B 正在运行"
        model_calls = sum(
            event["event_type"] == "p2b_model_call_started" for event in events
        )
        profile_events = [
            event for event in events if event["event_type"] == "p2b_profile_completed"
        ]
        gpu_seconds = sum(
            float(event["payload"].get("gpu_seconds", 0.0))
            for event in profile_events
        ) + sum(
            float(item.get("feedback", {}).get("gpu_seconds", 0.0))
            for lane_rounds in rounds.values()
            for item in lane_rounds
        )

        lane_rows = []
        curve_cards = []
        for lane in plan.get("lanes", []):
            lane_id = str(lane["lane_id"])
            lane_rounds = sorted(
                rounds.get(lane_id, []), key=lambda item: int(item["round_number"])
            )
            lane_attempts = sorted(
                score_attempts.get(lane_id, []),
                key=lambda item: int(item["round_number"]),
            )
            scores = [
                float(item["feedback"]["speedup_vs_eager"])
                for item in lane_rounds
                if item.get("feedback", {}).get("correct")
                and item["feedback"].get("speedup_vs_eager") is not None
            ]
            best = max(scores) if scores else None
            latest = lane_rounds[-1] if lane_rounds else None
            latest_trend = latest.get("score_trend") if latest else None
            last_delta = (
                latest_trend.get("delta_vs_best_pct")
                if isinstance(latest_trend, dict)
                else None
            )
            latest_profile = latest.get("profile") if latest else None
            profile_level = (
                latest_profile.get("level", "—")
                if isinstance(latest_profile, dict)
                else "—"
            )
            state = "已冻结" if lane_id in completed else ("进行中" if latest else "待启动")
            lane_rows.append(
                "<tr>"
                f"<td>{html.escape(TASK_LABELS.get(str(lane['task_id']), str(lane['task_id'])))}</td>"
                f"<td>{html.escape(STRATEGY_LABELS.get(str(lane['strategy']), str(lane['strategy'])))}</td>"
                f"<td>{len(lane_rounds)} / 8</td>"
                f"<td>{best:.3f}×</td>" if best is not None else
                "<tr>"
                f"<td>{html.escape(TASK_LABELS.get(str(lane['task_id']), str(lane['task_id'])))}</td>"
                f"<td>{html.escape(STRATEGY_LABELS.get(str(lane['strategy']), str(lane['strategy'])))}</td>"
                f"<td>{len(lane_rounds)} / 8</td><td>—</td>"
            )
            lane_rows[-1] += (
                f"<td>{_pct(last_delta)}</td>"
                f"<td>{html.escape(str(profile_level))}</td>"
                f"<td>{html.escape(state)}</td>"
                "</tr>"
            )
            curve_cards.append(_curve_card(lane, lane_attempts))

        score_attempt_count = sum(map(len, score_attempts.values()))

        recent_rows = []
        for event in events[-12:][::-1]:
            payload = event["payload"]
            detail = payload.get("detail") or payload.get("lane_id") or ""
            recent_rows.append(
                "<tr>"
                f"<td>{html.escape(event['recorded_at'][11:19])}</td>"
                f"<td>{html.escape(event['event_type'])}</td>"
                f"<td>{html.escape(_public_text(str(detail)))}</td>"
                "</tr>"
            )

        page = f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="5">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MOSS KernelBench P2B</title>
<style>
body{{margin:0;background:#f5f7fb;color:#172033;font:15px/1.5 system-ui,sans-serif}}
main{{max-width:1180px;margin:auto;padding:28px}}h1{{margin:0 0 6px}}.sub{{color:#667085}}
.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:18px 0}}
.card,section{{background:white;border:1px solid #e6e9ef;border-radius:12px;padding:16px}}
.metric{{font-size:26px;font-weight:700}}table{{width:100%;border-collapse:collapse}}
th,td{{padding:9px;border-bottom:1px solid #edf0f5;text-align:left}}th{{color:#536176}}
.pill{{display:inline-block;padding:5px 10px;border-radius:99px;background:#e8f1ff;color:#175bb5}}
.curve-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.curve-card{{border:1px solid #e6e9ef;border-radius:10px;padding:14px;min-width:0}}
.curve-card h3{{margin:0 0 3px}}.curve-meta{{margin:0 0 8px;color:#667085}}
.score-chart{{display:block;width:100%;height:auto;background:#fbfcfe;border-radius:8px}}
.score-history{{font-size:12px;margin-top:8px}}.score-history th,.score-history td{{padding:5px}}
.score-ok{{color:#087443}}.score-fail{{color:#b42318}}.score-unsealed{{color:#b54708}}
.chart-note{{font-size:12px;color:#667085;margin:8px 0 0}}
code{{font-family:ui-monospace,monospace}}@media(max-width:800px){{.cards{{grid-template-columns:1fr}}}}
@media(max-width:1000px){{.curve-grid{{grid-template-columns:1fr}}}}
</style></head><body><main>
<h1>MOSS KernelBench P2B 实时看板</h1>
<p class="sub"><span class="pill">{html.escape(phase_label)}</span>　页面每 5 秒自动刷新；唯一事实来源为追加式账本。</p>
<div class="cards"><div class="card"><div>模型调用</div><div class="metric">{model_calls} / 120</div></div>
<div class="card"><div>已完成候选轮次</div><div class="metric">{sum(map(len, rounds.values()))} / 64</div></div>
<div class="card"><div>账本评分记录</div><div class="metric">{score_attempt_count}</div></div>
<div class="card"><div>GPU 时间</div><div class="metric">{gpu_seconds:.1f}s</div></div></div>
<section><h2>八条 Harness 路线</h2><table><thead><tr><th>Task</th><th>路线</th><th>轮次</th><th>最好分</th><th>最近相对最好</th><th>分析级别</th><th>状态</th></tr></thead>
<tbody>{''.join(lane_rows)}</tbody></table></section>
<section><h2>Harness 逐轮分数曲线</h2>
<p class="sub">每个点对应一版 Harness 生成的一个 Kernel；红色叉号表示该轮未通过正确性。折线不跨越失败点，橙色点表示分数已写入账本但轮次因后续中断未封存。</p>
<div class="curve-grid">{''.join(curve_cards)}</div></section>
<section><h2>最近记录</h2><table><thead><tr><th>时间</th><th>事件</th><th>摘要</th></tr></thead><tbody>{''.join(recent_rows)}</tbody></table></section>
<p class="sub">P2B 只负责搜索；P3 没有执行入口，必须另行授权。</p>
</main></body></html>"""
        self._write_atomic(page)

    def _write_atomic(self, content: str) -> None:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(dir=self.output_path.parent, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(self.output_path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise


def _pct(value: Any) -> str:
    return "—" if value is None else f"{float(value):+.2f}%"


def _score_attempts(
    events: list[dict[str, Any]],
    completed_rounds: dict[str, list[dict[str, Any]]],
) -> dict[str, list[dict[str, Any]]]:
    """Return every scored attempt, including scores saved before later interruption."""
    attempts = {
        lane_id: [dict(item, _evidence_state="sealed") for item in lane_rounds]
        for lane_id, lane_rounds in completed_rounds.items()
    }
    occupied = {
        (lane_id, int(item["round_number"]))
        for lane_id, lane_rounds in completed_rounds.items()
        for item in lane_rounds
    }
    generated: dict[str, dict[str, Any]] = {}
    for event in events:
        if event["event_type"] != "p2b_candidate_generated":
            continue
        payload = event["payload"]
        candidate_id = payload.get("candidate_id")
        if isinstance(candidate_id, str):
            generated[candidate_id] = payload

    for event in events:
        if event["event_type"] != "candidate_evaluated":
            continue
        payload = event["payload"]
        feedback = payload.get("feedback")
        if not isinstance(feedback, dict):
            continue
        candidate_id = payload.get("candidate_id") or feedback.get("candidate_id")
        if not isinstance(candidate_id, str):
            continue
        source = generated.get(candidate_id)
        if source is None:
            continue
        lane_id = source.get("lane_id")
        round_number = source.get("round_number")
        if not isinstance(lane_id, str) or not isinstance(round_number, int):
            continue
        if (lane_id, round_number) in occupied:
            continue
        attempts.setdefault(lane_id, []).append(
            {
                "lane_id": lane_id,
                "round_number": round_number,
                "candidate_id": candidate_id,
                "policy_version_id": source.get("policy_version_id"),
                "feedback": feedback,
                "profile": None,
                "score_trend": None,
                "_evidence_state": "scored_unsealed",
            }
        )
        occupied.add((lane_id, round_number))
    return attempts


def _curve_card(lane: dict[str, Any], attempts: list[dict[str, Any]]) -> str:
    task_label = TASK_LABELS.get(str(lane["task_id"]), str(lane["task_id"]))
    strategy_label = STRATEGY_LABELS.get(
        str(lane["strategy"]), str(lane["strategy"])
    )
    starting_score = _number(lane.get("starting_score"))
    candidate_scores = [
        score for item in attempts if (score := _attempt_score(item)) is not None
    ]
    best = max(candidate_scores) if candidate_scores else None
    correct_count = len(candidate_scores)
    rows = [
        "<tr><td>起点</td><td>"
        f"{html.escape(str(lane.get('starting_candidate_id', '—')))}"
        f"</td><td>冻结基线</td><td>{_score_text(starting_score)}</td><td>—</td></tr>"
    ]
    for item in attempts:
        round_number = int(item["round_number"])
        feedback = item.get("feedback")
        feedback = feedback if isinstance(feedback, dict) else {}
        candidate_id = str(item.get("candidate_id", "—"))
        version = str(item.get("policy_version_id") or f"v{round_number:03d}")
        score = _attempt_score(item)
        evidence_state = item.get("_evidence_state")
        if evidence_state == "scored_unsealed":
            outcome = '<span class="score-unsealed">评分已保存；轮次未封存</span>'
        elif score is not None:
            outcome = '<span class="score-ok">正确</span>'
        else:
            outcome = '<span class="score-fail">正确性失败</span>'
        delta = (
            (score / starting_score - 1.0) * 100.0
            if score is not None and starting_score not in (None, 0.0)
            else None
        )
        rows.append(
            "<tr>"
            f"<td>{html.escape(version)}</td>"
            f"<td>{html.escape(candidate_id)}</td>"
            f"<td>{outcome}</td>"
            f"<td>{_score_text(score)}</td>"
            f"<td>{_pct(delta)}</td>"
            "</tr>"
        )
    return (
        '<article class="curve-card">'
        f"<h3>{html.escape(task_label)} · {html.escape(strategy_label)}</h3>"
        f'<p class="curve-meta">冻结起点 {_score_text(starting_score)} · '
        f"候选最好 {_score_text(best)} · 正确 {correct_count}/{len(attempts)}</p>"
        f"{_score_curve_svg(starting_score, attempts, task_label, strategy_label)}"
        '<table class="score-history"><thead><tr><th>Harness</th><th>Kernel</th>'
        "<th>结果</th><th>Speedup</th><th>相对起点</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
        '<p class="chart-note">事实来源：追加账本中的逐轮评分与已封存轮次。</p>'
        "</article>"
    )


def _score_curve_svg(
    starting_score: float | None,
    attempts: list[dict[str, Any]],
    task_label: str,
    strategy_label: str,
) -> str:
    width, height = 720, 230
    left, right, top, bottom = 58.0, 18.0, 20.0, 38.0
    plot_width = width - left - right
    plot_height = height - top - bottom
    values = ([] if starting_score is None else [starting_score]) + [
        score for item in attempts if (score := _attempt_score(item)) is not None
    ]
    if not values:
        return '<p class="chart-note">尚无可绘制分数。</p>'
    low, high = min(values), max(values)
    if math.isclose(low, high):
        padding = max(abs(high) * 0.05, 0.1)
    else:
        padding = max((high - low) * 0.12, 0.02)
    y_min = max(0.0, low - padding)
    y_max = high + padding
    if math.isclose(y_min, y_max):
        y_max = y_min + 1.0

    def x_position(round_number: int) -> float:
        return left + plot_width * round_number / 8.0

    def y_position(score: float) -> float:
        return top + (y_max - score) / (y_max - y_min) * plot_height

    parts = [
        f'<svg class="score-chart" viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{html.escape(task_label)} {html.escape(strategy_label)} 分数曲线">'
    ]
    for index, tick in enumerate((y_max, (y_max + y_min) / 2.0, y_min)):
        y = top + plot_height * index / 2.0
        parts.append(
            f'<line x1="{left:.1f}" y1="{y:.1f}" x2="{width-right:.1f}" '
            f'y2="{y:.1f}" stroke="#e5e9f0" stroke-width="1"/>'
            f'<text x="{left-7:.1f}" y="{y+4:.1f}" text-anchor="end" '
            f'font-size="11" fill="#667085">{tick:.3f}×</text>'
        )
    for round_number in range(9):
        x = x_position(round_number)
        label = "起点" if round_number == 0 else f"v{round_number:03d}"
        parts.append(
            f'<line x1="{x:.1f}" y1="{top:.1f}" x2="{x:.1f}" '
            f'y2="{top+plot_height:.1f}" stroke="#f0f2f5" stroke-width="1"/>'
            f'<text x="{x:.1f}" y="{height-13:.1f}" text-anchor="middle" '
            f'font-size="11" fill="#667085">{label}</text>'
        )
    if starting_score is not None:
        baseline_y = y_position(starting_score)
        parts.append(
            f'<line x1="{left:.1f}" y1="{baseline_y:.1f}" x2="{width-right:.1f}" '
            f'y2="{baseline_y:.1f}" stroke="#d97706" stroke-width="1.5" '
            'stroke-dasharray="5 4"/>'
        )

    attempts_by_round = {int(item["round_number"]): item for item in attempts}
    segments: list[list[tuple[int, float]]] = []
    segment: list[tuple[int, float]] = []
    if starting_score is not None:
        segment.append((0, starting_score))
    for round_number in range(1, 9):
        item = attempts_by_round.get(round_number)
        if item is None:
            if segment:
                segments.append(segment)
                segment = []
            continue
        score = _attempt_score(item)
        if score is None:
            if segment:
                segments.append(segment)
                segment = []
            continue
        segment.append((round_number, score))
    if segment:
        segments.append(segment)
    for points in segments:
        if len(points) < 2:
            continue
        encoded = " ".join(
            f"{x_position(round_number):.1f},{y_position(score):.1f}"
            for round_number, score in points
        )
        parts.append(
            f'<polyline points="{encoded}" fill="none" stroke="#2563eb" '
            'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        )
    if starting_score is not None:
        parts.append(
            f'<circle data-round="0" data-score="{starting_score:.6f}" '
            f'cx="{x_position(0):.1f}" cy="{y_position(starting_score):.1f}" r="5" '
            'fill="#d97706" stroke="white" stroke-width="2">'
            f"<title>冻结起点 · {starting_score:.6f}×</title></circle>"
        )
    failure_y = top + plot_height - 7.0
    for item in attempts:
        round_number = int(item["round_number"])
        candidate_id = html.escape(str(item.get("candidate_id", "—")))
        score = _attempt_score(item)
        x = x_position(round_number)
        if score is None:
            parts.append(
                f'<g data-round="{round_number}" data-outcome="incorrect">'
                f'<line x1="{x-6:.1f}" y1="{failure_y-6:.1f}" x2="{x+6:.1f}" '
                f'y2="{failure_y+6:.1f}" stroke="#dc2626" stroke-width="3"/>'
                f'<line x1="{x+6:.1f}" y1="{failure_y-6:.1f}" x2="{x-6:.1f}" '
                f'y2="{failure_y+6:.1f}" stroke="#dc2626" stroke-width="3"/>'
                f"<title>v{round_number:03d} · {candidate_id} · 正确性失败</title></g>"
            )
            continue
        unsealed = item.get("_evidence_state") == "scored_unsealed"
        fill = "#f59e0b" if unsealed else "#2563eb"
        state = "评分已保存；轮次未封存" if unsealed else "正确"
        parts.append(
            f'<circle data-round="{round_number}" data-score="{score:.6f}" '
            f'cx="{x:.1f}" cy="{y_position(score):.1f}" r="5" fill="{fill}" '
            'stroke="white" stroke-width="2">'
            f"<title>v{round_number:03d} · {candidate_id} · {score:.6f}× · {state}</title>"
            "</circle>"
        )
    parts.append("</svg>")
    return "".join(parts)


def _attempt_score(item: dict[str, Any]) -> float | None:
    feedback = item.get("feedback")
    if not isinstance(feedback, dict) or feedback.get("correct") is not True:
        return None
    return _number(feedback.get("speedup_vs_eager"))


def _number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _score_text(value: float | None) -> str:
    return "—" if value is None else f"{value:.6f}×"


def _public_text(text: str) -> str:
    import re

    return re.sub(r"(?<![A-Za-z0-9])/(?:[^\s:|]+/)*[^\s:|]+", "<private-path>", text)[:500]
