"""Setup + trace + segmentation for the 15 new BugsInPy instances."""
import json
import logging
import os
import subprocess
import sys

sys.path.insert(0, "/root/trace_distill_repair")

from trace_collector import TraceCollector
from structural_segmenter import StructuralSegmenter
from line_segmenter import LineSegmenter
from dtd_types import serialize_segment
from bugsinpy_setup import BugsInPySetup

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)
sys.stdout.reconfigure(line_buffering=True)

WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
INSTANCES_DIR = os.path.join(WORKSPACE, "instances")
OUTPUT_DIR = "/root/trace_distill_repair/pipeline_output_new"
os.makedirs(OUTPUT_DIR, exist_ok=True)

setup = BugsInPySetup(workspace_dir=WORKSPACE)
setup._ensure_repo()

# The 15 new candidates
NEW_BUGS = [
    ("scrapy", 3), ("scrapy", 4), ("scrapy", 7),
    ("tornado", 4), ("tornado", 5), ("tornado", 7),
    ("luigi", 5), ("luigi", 10), ("luigi", 14),
    ("youtube-dl", 5), ("youtube-dl", 10), ("youtube-dl", 20),
    ("black", 5), ("black", 14),
    ("fastapi", 5),
]

# For local clone: map project -> an existing instance's buggy dir
LOCAL_REPO_MAP = {
    "scrapy": os.path.join(INSTANCES_DIR, "scrapy_1", "buggy"),
    "tornado": os.path.join(INSTANCES_DIR, "tornado_1", "buggy"),
    "luigi": os.path.join(INSTANCES_DIR, "luigi_1", "buggy"),
    "youtube-dl": os.path.join(INSTANCES_DIR, "youtube-dl_1", "buggy"),
    "black": os.path.join(INSTANCES_DIR, "black_1", "buggy"),
    "fastapi": os.path.join(INSTANCES_DIR, "fastapi_1", "buggy"),
}

# ============ PHASE 1: Setup missing instances ============
logger.info("=== PHASE 1: Setting up instances ===")
setup_results = {}

for project, bug_id in NEW_BUGS:
    key = f"{project}_{bug_id}"
    buggy_dir = os.path.join(INSTANCES_DIR, key, "buggy")

    if os.path.isdir(buggy_dir) and os.path.isdir(os.path.join(buggy_dir, ".git")):
        logger.info("SKIP setup %s (already exists)", key)
        setup_results[key] = {"status": "exists"}
        continue

    # Read bug info to get commit ID
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    commit_id = bug_info.get("buggy_commit_id", "")

    if not commit_id:
        logger.error("FAIL setup %s: no buggy_commit_id", key)
        setup_results[key] = {"status": "failed", "error": "no commit id"}
        continue

    # Clone from local existing repo
    local_src = LOCAL_REPO_MAP.get(project, "")
    if not local_src or not os.path.isdir(local_src):
        logger.error("FAIL setup %s: no local repo for %s", key, project)
        setup_results[key] = {"status": "failed", "error": "no local repo"}
        continue

    try:
        os.makedirs(os.path.dirname(buggy_dir), exist_ok=True)
        logger.info("Cloning local %s -> %s", local_src, buggy_dir)
        subprocess.run(["git", "clone", local_src, buggy_dir], check=True, capture_output=True, timeout=120)
        subprocess.run(["git", "checkout", commit_id], check=True, capture_output=True, cwd=buggy_dir, timeout=30)
        setup_results[key] = {"status": "ok", "commit": commit_id[:8]}
        logger.info("OK setup %s (commit %s)", key, commit_id[:8])
    except Exception as e:
        setup_results[key] = {"status": "failed", "error": str(e)[:200]}
        logger.error("FAIL setup %s: %s", key, str(e)[:200])

logger.info("Phase 1 done: %d/%d ready",
    sum(1 for v in setup_results.values() if v["status"] in ("ok", "exists")), len(NEW_BUGS))

# ============ PHASE 2: Trace collection ============
logger.info("=== PHASE 2: Collecting traces ===")
collector = TraceCollector()
trace_results = {}

for project, bug_id in NEW_BUGS:
    key = f"{project}_{bug_id}"
    if setup_results.get(key, {}).get("status") not in ("ok", "exists"):
        logger.info("SKIP trace %s (setup failed)", key)
        trace_results[key] = {"status": "skipped"}
        continue

    buggy_dir = os.path.join(INSTANCES_DIR, key, "buggy")

    # Get test command from bug info
    bug_dir = os.path.join(setup.repo_dir, "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    test_file = bug_info.get("test_file", "")
    test_cmd = bug_info.get("test_command", "")
    if not test_cmd:
        if test_file:
            files = test_file.replace(";", " ")
            test_cmd = f"python -m pytest {files}"
        else:
            test_cmd = "python -m pytest"

    # Find a main python file for code_path
    main_py = None
    for root, dirs, files in os.walk(buggy_dir):
        if ".git" in dirs:
            dirs.remove(".git")
        for f in sorted(files):
            if f.endswith(".py") and not f.startswith("test_") and f != "setup.py":
                main_py = os.path.join(root, f)
                break
        if main_py:
            break

    if not main_py:
        trace_results[key] = {"status": "failed", "error": "no python file"}
        logger.error("FAIL trace %s: no Python file", key)
        continue

    try:
        events = collector.collect(main_py, test_cmd, timeout=120, project_root=buggy_dir)
        if events:
            trace_file = os.path.join(OUTPUT_DIR, f"{key}_trace.json")
            with open(trace_file, "w") as f:
                json.dump([{
                    "event_type": e.event_type,
                    "function_name": e.function_name,
                    "filename": e.filename,
                    "lineno": e.lineno,
                    "call_depth": e.call_depth,
                } for e in events], f)
            trace_results[key] = {"status": "ok", "events": len(events), "events_obj": events}
            logger.info("OK trace %s: %d events", key, len(events))
        else:
            trace_results[key] = {"status": "failed", "error": "0 events"}
            logger.warning("FAIL trace %s: 0 events", key)
    except Exception as e:
        trace_results[key] = {"status": "failed", "error": str(e)[:200]}
        logger.error("FAIL trace %s: %s", key, str(e)[:200])

ok_traces = sum(1 for v in trace_results.values() if v["status"] == "ok")
logger.info("Phase 2 done: %d/%d traces collected", ok_traces, len(NEW_BUGS))

# ============ PHASE 3: Segmentation ============
logger.info("=== PHASE 3: Segmenting traces ===")
struct_seg = StructuralSegmenter()
line_seg = LineSegmenter(window_size=5, stride=5)
seg_results = {}

for key, tr in trace_results.items():
    if tr["status"] != "ok":
        continue

    events = tr["events_obj"]
    try:
        s_segs = struct_seg.segment(events)
        l_segs = line_seg.segment(events)

        type_dist = {}
        for s in s_segs:
            t = s.segment_type
            type_dist[t] = type_dist.get(t, 0) + 1

        s_file = os.path.join(OUTPUT_DIR, f"{key}_structural_segments.json")
        l_file = os.path.join(OUTPUT_DIR, f"{key}_line_segments.json")
        with open(s_file, "w") as f:
            json.dump([serialize_segment(s) for s in s_segs], f)
        with open(l_file, "w") as f:
            json.dump([serialize_segment(s) for s in l_segs], f)

        seg_results[key] = {
            "structural": len(s_segs),
            "line": len(l_segs),
            "types": type_dist,
        }
        logger.info("OK seg %s: structural=%d (types=%s), line=%d",
                     key, len(s_segs), type_dist, len(l_segs))
    except Exception as e:
        seg_results[key] = {"error": str(e)[:200]}
        logger.error("FAIL seg %s: %s", key, str(e)[:200])

# ============ SUMMARY ============
logger.info("=== FINAL SUMMARY ===")
summary = {
    "phase1_setup": setup_results,
    "phase2_traces": {k: {kk: vv for kk, vv in v.items() if kk != "events_obj"} for k, v in trace_results.items()},
    "phase3_segmentation": seg_results,
}

# Flag too_small / truncated
for key, tr in trace_results.items():
    if tr["status"] == "ok":
        n = tr["events"]
        flag = ""
        if n < 10:
            flag = "too_small"
        elif n >= 100000:
            flag = "truncated"
        if flag:
            summary["phase2_traces"][key]["flag"] = flag
            logger.info("FLAG %s: %s (%d events)", key, flag, n)

with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

logger.info("Setup: %d/%d ok", sum(1 for v in setup_results.values() if v["status"] in ("ok","exists")), len(NEW_BUGS))
logger.info("Traces: %d/%d ok", ok_traces, len(NEW_BUGS))
logger.info("Segments: %d/%d ok", len(seg_results), ok_traces)
logger.info("Output dir: %s", OUTPUT_DIR)
