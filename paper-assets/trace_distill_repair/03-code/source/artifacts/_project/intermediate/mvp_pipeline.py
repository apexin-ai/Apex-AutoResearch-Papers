"""DTD MVP end-to-end pipeline.

Runs the full Diagnostic Trace Distillation pipeline:
1. Collect trace from buggy code
2. Segment (structural + line baseline)
3. Teacher scoring and filtering
4. Generate repair under 4 conditions (no_trace, full_trace, structural_filtered, line_filtered)
5. Evaluate repair against ground truth

Dependencies: openai, pandas (optional).
"""
from __future__ import annotations

import json
import logging
import os
import shlex
import subprocess
import time
from typing import Any, Dict, List, Optional

from dtd_types import TraceEvent, TraceSegment, ScoredSegment, estimate_tokens, serialize_event
from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from teacher_scorer import TeacherScorer

logger = logging.getLogger(__name__)

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    logger.warning("pandas not installed, DataFrame output unavailable")

REPAIR_PROMPT_TEMPLATE = """\
You are an expert software engineer. Fix the bug described below.

## Bug Report
{issue_description}

## Buggy Code
```python
{buggy_code}
```
{trace_section}
## Task
Provide the corrected code. Output ONLY the fixed Python code, no explanations.
"""

TRACE_SECTION_TEMPLATE = """
## Execution Trace ({condition})
The following trace information was collected during test execution:
```
{trace_context}
```
"""


class MVPPipeline:
    CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]

    def __init__(
        self,
        teacher_api_key: [REDACTED] = None,
        repair_api_key: [REDACTED] = None,
        repair_model: str = "deepseek-chat",
        output_dir: str = "./mvp_results",
    ):
        self.collector = TraceCollector(max_events=50000, max_depth=30)
        self.structural_segmenter = StructuralSegmenter()
        self.line_segmenter = LineSegmenter(window_size=5, stride=5)
        self.teacher = TeacherScorer(api_key=[REDACTED]
        self.repair_api_key = [REDACTED] or os.environ.get("DEEPSEEK_API_KEY", "")
        self.repair_model = repair_model
        self.output_dir = os.path.abspath(output_dir)
        os.makedirs(self.output_dir, exist_ok=True)
        self._repair_client = None

    def _get_repair_client(self):
        if self._repair_client is None:
            from openai import OpenAI
            self._repair_client = OpenAI(
                api_key=[REDACTED],
                base_url="https://api.deepseek.com/v1",
            )
        return self._repair_client

    def run_single(self, instance: dict, buggy_code: str, fixed_code: str) -> dict:
        instance_id = f"{instance['project']}_{instance['bug_id']}"
        logger.info("Running pipeline for %s", instance_id)

        # 1. Collect trace
        events = self.collector.collect(
            instance.get("buggy_dir", ""),
            instance.get("test_command", ""),
            timeout=120,
        )
        logger.info("Collected %d trace events for %s", len(events), instance_id)

        # 2. Segment
        structural_segments = self.structural_segmenter.segment(events) if events else []
        line_segments = self.line_segmenter.segment(events) if events else []

        # 3. Teacher scoring
        issue = instance.get("issue_description", "")
        structural_scored = (
            self.teacher.score_batch(issue, buggy_code, structural_segments)
            if structural_segments else []
        )
        line_scored = (
            self.teacher.score_batch(issue, buggy_code, line_segments)
            if line_segments else []
        )
        structural_filtered = self.teacher.filter_segments(structural_scored)
        line_filtered = self.teacher.filter_segments(line_scored)

        # 4. Build repair prompts for each condition
        full_trace_text, truncation_info = self._format_full_trace(events, max_tokens=8000)
        structural_trace_text = self._format_filtered_trace(structural_filtered)
        line_trace_text = self._format_filtered_trace(line_filtered)

        conditions = {
            "no_trace": "",
            "full_trace": full_trace_text,
            "structural_filtered": structural_trace_text,
            "line_filtered": line_trace_text,
        }

        # 5. Call repair LLM for each condition
        buggy_file_relpath = instance.get("bug_info", {}).get("buggy_file", "")

        results = {"instance_id": instance_id, "trace_events_count": len(events)}
        results["full_trace_truncation"] = truncation_info
        for condition, trace_ctx in conditions.items():
            prompt = self._build_repair_prompt(issue, buggy_code, trace_ctx, condition)
            tokens_used = estimate_tokens(prompt)

            try:
                generated_fix = self._call_repair_llm(prompt)
            except Exception as e:
                logger.error("Repair LLM failed for %s/%s: %s", instance_id, condition, e)
                generated_fix = ""

            # 6. Evaluate
            eval_result = self._evaluate_repair(
                generated_fix, fixed_code,
                instance.get("test_command", ""),
                instance.get("buggy_dir", ""),
                buggy_file_relpath=buggy_file_relpath,
            )

            results[condition] = {
                "repair_success": eval_result["pass"],
                "eval_method": eval_result.get("method", "none"),
                "line_overlap": eval_result.get("line_overlap", 0.0),
                "tokens_used": tokens_used,
                "generated_fix_length": len(generated_fix),
            }
            logger.info("%s/%s: success=%s (method=%s), tokens=%d",
                        instance_id, condition, eval_result["pass"],
                        eval_result.get("method", "none"), tokens_used)

        results["segments_structural"] = len(structural_segments)
        results["segments_line"] = len(line_segments)
        results["filtered_structural"] = len(structural_filtered)
        results["filtered_line"] = len(line_filtered)

        if structural_segments:
            total_tokens = sum(s.segment.token_estimate for s in structural_scored)
            filtered_tokens = sum(s.segment.token_estimate for s in structural_filtered)
            results["compression_ratio"] = filtered_tokens / max(total_tokens, 1)
        else:
            results["compression_ratio"] = 1.0

        return results

    def run_batch(self, instances: List[dict]) -> Any:
        rows = []
        for inst in instances:
            from bugsinpy_setup import BugsInPySetup
            setup = BugsInPySetup(inst.get("buggy_dir", "./bugsinpy_workspace"))
            buggy_code = setup.get_buggy_code(inst)
            fixed_code = setup.get_fixed_code(inst)

            result = self.run_single(inst, buggy_code, fixed_code)

            for condition in self.CONDITIONS:
                cond_result = result.get(condition, {})
                rows.append({
                    "instance_id": result["instance_id"],
                    "condition": condition,
                    "repair_success": cond_result.get("repair_success", False),
                    "tokens_used": cond_result.get("tokens_used", 0),
                    "compression_ratio": result.get("compression_ratio", 1.0),
                    "trace_events_count": result.get("trace_events_count", 0),
                    "segments_count": result.get(
                        "segments_structural" if "structural" in condition else "segments_line", 0
                    ),
                })

        if HAS_PANDAS:
            return pd.DataFrame(rows)
        return rows

    def _build_repair_prompt(self, issue: str, code: str, trace_context: str, condition: str) -> str:
        trace_section = ""
        if trace_context:
            trace_section = TRACE_SECTION_TEMPLATE.format(
                condition=condition, trace_context=trace_context,
            )
        return REPAIR_PROMPT_TEMPLATE.format(
            issue_description=issue,
            buggy_code=code,
            trace_section=trace_section,
        )

    def _call_repair_llm(self, prompt: str) -> str:
        client = self._get_repair_client()
        response = client.chat.completions.create(
            model=self.repair_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=4096,
        )
        content = response.choices[0].message.content.strip()
        if content.startswith("```python"):
            content = content[len("```python"):].strip()
        if content.startswith("```"):
            content = content[3:].strip()
        if content.endswith("```"):
            content = content[:-3].strip()
        return content

    def _evaluate_repair(
        self, generated_fix: str, fixed_code: str,
        test_command: str, buggy_dir: str,
        buggy_file_relpath: str = "",
    ) -> dict:
        result = {"pass": False, "method": "none", "line_overlap": 0.0}

        if not generated_fix:
            return result

        gen_lines = generated_fix.strip().splitlines()
        fix_lines = fixed_code.strip().splitlines()
        if gen_lines == fix_lines:
            result["pass"] = True
            result["method"] = "exact_match"
            result["line_overlap"] = 1.0
            return result

        gen_set = set(gen_lines)
        fix_set = set(fix_lines)
        overlap = len(gen_set & fix_set)
        total = max(len(fix_set), 1)
        result["line_overlap"] = overlap / total

        if test_command and buggy_dir and buggy_file_relpath:
            test_result = self._run_test_evaluation(
                generated_fix, test_command, buggy_dir, buggy_file_relpath
            )
            result.update(test_result)
        else:
            result["method"] = "line_overlap_fallback"
            if result["line_overlap"] > 0.9:
                result["pass"] = True

        return result

    def _run_test_evaluation(
        self, generated_fix: str, test_command: str,
        buggy_dir: str, buggy_file_relpath: str,
    ) -> dict:
        buggy_file_path = os.path.join(buggy_dir, buggy_file_relpath)
        if not os.path.isfile(buggy_file_path):
            logger.warning("Buggy file not found: %s", buggy_file_path)
            return {"method": "test_skipped", "reason": "buggy_file_not_found"}

        with open(buggy_file_path, "r") as f:
            original_content = f.read()

        try:
            with open(buggy_file_path, "w") as f:
                f.write(generated_fix)

            try:
                proc = subprocess.run(
                    shlex.split(test_command),
                    capture_output=True,
                    text=True,
                    timeout=120,
                    cwd=buggy_dir,
                )
                return {
                    "pass": proc.returncode == 0,
                    "method": "test_execution",
                    "returncode": proc.returncode,
                    "stderr_snippet": proc.stderr[:500] if proc.stderr else "",
                }
            except subprocess.TimeoutExpired:
                return {"pass": False, "method": "test_execution", "reason": "timeout"}
            except Exception as e:
                logger.warning("Test execution failed: %s", e)
                return {"pass": False, "method": "test_execution", "reason": str(e)[:200]}
        finally:
            with open(buggy_file_path, "w") as f:
                f.write(original_content)

    def _format_full_trace(self, events: List[TraceEvent], max_tokens: int = 8000) -> tuple:
        lines = []
        truncated = False
        for idx, ev in enumerate(events):
            line = f"[{ev.event_type:9s}] {ev.function_name}:{ev.lineno} depth={ev.call_depth}"
            if ev.exception_info:
                line += f" EXCEPTION: {ev.exception_info[0]}: {ev.exception_info[1]}"
            lines.append(line)
            if estimate_tokens("\n".join(lines)) > max_tokens:
                remaining = len(events) - idx - 1
                lines.append(f"... ({remaining} more events truncated)")
                truncated = True
                break

        text = "\n".join(lines)
        events_included = len(lines) - (1 if truncated else 0)
        truncation_info = {
            "truncated": truncated,
            "events_included": events_included,
            "events_total": len(events),
            "truncation_ratio": (len(events) - events_included) / max(len(events), 1) if truncated else 0.0,
        }
        return text, truncation_info

    def _format_filtered_trace(self, scored_segments: List[ScoredSegment]) -> str:
        if not scored_segments:
            return "(no relevant trace segments found)"
        lines = []
        for ss in scored_segments:
            seg = ss.segment
            lines.append(f"--- {seg.segment_type} (confidence={ss.confidence:.2f}: {ss.reasoning[:80]}) ---")
            for ev in seg.events[:30]:
                line = f"  [{ev.event_type:9s}] {ev.function_name}:{ev.lineno}"
                key_locals = {k: v for k, v in list(ev.locals_snapshot.items())[:3]}
                if key_locals:
                    line += f" {key_locals}"
                lines.append(line)
            if len(seg.events) > 30:
                lines.append(f"  ... ({len(seg.events) - 30} more events)")
        return "\n".join(lines)

    def save_results(self, df: Any, path: Optional[str] = None):
        if path is None:
            path = os.path.join(self.output_dir, "mvp_results.csv")
        if HAS_PANDAS and hasattr(df, "to_csv"):
            df.to_csv(path, index=False)
        else:
            import csv
            with open(path, "w", newline="") as f:
                if df:
                    writer = csv.DictWriter(f, fieldnames=df[0].keys())
                    writer.writeheader()
                    writer.writerows(df)
        logger.info("Results saved to %s", path)

    def print_summary(self, df: Any):
        if HAS_PANDAS and hasattr(df, "groupby"):
            summary = df.groupby("condition").agg({
                "repair_success": ["sum", "count", "mean"],
                "tokens_used": "mean",
                "compression_ratio": "mean",
            })
            print("\n=== MVP Results Summary ===")
            print(summary.to_string())
        else:
            print("\n=== MVP Results Summary ===")
            from collections import defaultdict
            by_cond = defaultdict(list)
            for row in df:
                by_cond[row["condition"]].append(row)
            for cond, rows in by_cond.items():
                n = len(rows)
                successes = sum(1 for r in rows if r["repair_success"])
                avg_tokens = sum(r["tokens_used"] for r in rows) / max(n, 1)
                print(f"  {cond}: {successes}/{n} success, avg_tokens={avg_tokens:.0f}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s: %(message)s")

    pipeline = MVPPipeline(output_dir="./mvp_results")

    print("MVPPipeline initialized.")
    print(f"Conditions: {pipeline.CONDITIONS}")
    print(f"Output dir: {pipeline.output_dir}")

    demo_instance = {
        "project": "demo",
        "bug_id": 0,
        "buggy_dir": ".",
        "test_command": "",
        "issue_description": "Demo: division by zero when input contains 3",
    }
    demo_buggy = "def process(items):\n    return [100 / (x - 3) for x in items]\n"
    demo_fixed = "def process(items):\n    return [100 / (x - 3) if x != 3 else 0 for x in items]\n"

    prompt = pipeline._build_repair_prompt(
        demo_instance["issue_description"], demo_buggy, "", "no_trace"
    )
    print("\n=== Sample repair prompt (no_trace) ===")
    print(prompt[:500])

    print("\nTo run full pipeline, set DEEPSEEK_API_KEY and call pipeline.run_single().")
