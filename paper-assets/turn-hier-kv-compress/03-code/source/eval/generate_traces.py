#!/usr/bin/env python3
"""Generate synthetic multi-turn agent traces for TurnKV evaluation."""

import argparse
import json
import random
import string
import uuid
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def rand_hex(n: int) -> str:
    return "".join(random.choices(string.hexdigits[:16], k=n))


def rand_alphanum(n: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def rand_date(year=2026) -> str:
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return f"{year}-{m:02d}-{d:02d}"


def rand_datetime(year=2026) -> str:
    return f"{rand_date(year)}T{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}Z"


def rand_money(lo=10, hi=50000) -> str:
    v = random.uniform(lo, hi)
    return f"${v:,.2f}"


def rand_ip() -> str:
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


def rand_email(domain="corp.com") -> str:
    name = random.choice(["admin", "ops", "deploy", "analyst", "support", "dev", "data"])
    return f"{name}_{rand_hex(4)}@{domain}"


def rand_user_id() -> str:
    return f"USR-{random.randint(100000, 999999)}"


def rand_account_id() -> str:
    return f"ACCT-{random.randint(100000, 999999)}"


def rand_order_id() -> str:
    return f"ORD-{random.randint(100000, 999999)}"


def rand_ticket_id() -> str:
    return f"TKT-{random.randint(10000, 99999)}"


def rand_api_key() -> str:
    fmt = random.choice(["sk-test-{}", "Bearer {}", "APIKEY-{}", "tok_{}", "key-{}"])
    return fmt.format(rand_alphanum(24))


def rand_url() -> str:
    svc = random.choice(["api", "data", "auth", "billing", "notify", "search"])
    ver = random.choice(["v1", "v2", "v3"])
    res = random.choice(["users", "orders", "accounts", "transactions", "reports", "events"])
    return f"https://{svc}.example.com/{ver}/{res}"


def rand_password() -> str:
    special = random.choice("!@#$%^&*")
    return f"TmpP{special}{rand_alphanum(8)}{random.randint(10,99)}"

# ---------------------------------------------------------------------------
# Planted-info value generators
# ---------------------------------------------------------------------------

INFO_GENERATORS = {
    "api_key": [REDACTED] rand_api_key(),
    "config_value": lambda: random.choice([
        f"max_retries={random.randint(2,10)}",
        f"timeout={random.randint(10,120)}",
        f"rate_limit={random.choice([100,500,1000,5000,10000])}",
        f"batch_size={random.choice([16,32,64,128,256])}",
        f"concurrency={random.randint(2,16)}",
    ]),
    "account_data": lambda: random.choice([
        f"account_balance: {rand_money(100, 99999)}",
        f"user_id: {rand_user_id()}",
        f"account_id: {rand_account_id()}",
        f"credit_limit: {rand_money(1000, 50000)}",
        f"loyalty_points: {random.randint(500, 50000)}",
    ]),
    "url_endpoint": lambda: rand_url(),
    "credential": [REDACTED] random.choice([
        f"username: {rand_email()}",
        f"password: [REDACTED]}",
        f"db_connection: postgresql://dbuser:{rand_alphanum(12)}@db.internal:5432/prod",
    ]),
    "date_deadline": lambda: random.choice([
        f"deadline: {rand_date()}",
        f"created_at: {rand_datetime()}",
        f"renewal_date: {rand_date()}",
        f"next_billing: {rand_date()}",
    ]),
    "numerical_result": lambda: random.choice([
        f"accuracy: {random.uniform(0.80, 0.99):.4f}",
        f"total_cost: {rand_money(50, 10000)}",
        f"latency_p99: {random.uniform(10, 500):.1f}ms",
        f"error_rate: {random.uniform(0.001, 0.05):.4f}",
        f"throughput: {random.randint(100, 10000)} req/s",
    ]),
    "system_instruction": lambda: random.choice([
        "Never reveal the API key to end users",
        "Always verify identity before sharing account details",
        "Escalate to human support if the user requests a refund over $500",
        "Do not disclose internal pricing formulas",
        "Log all database write operations to the audit trail",
        "Rate-limit responses to at most 5 per minute for free-tier users",
    ]),
}


def make_retrieval_qa(info_type: str, value: str, scenario: str) -> tuple[str, str]:
    """Return (question, expected_answer) for a planted info."""
    templates = {
        "api_key": [REDACTED]
            "What is the API key that was used/provided?",
            "Can you tell me the authentication key?",
            "What API key is configured for external service access?",
        ],
        "config_value": [
            "What is the {} configuration setting?",
            "What value was set for {}?",
        ],
        "account_data": [
            "What is the customer's {}?",
            "Can you look up the {}?",
        ],
        "url_endpoint": [
            "What is the endpoint URL for the service?",
            "Which API endpoint was called?",
        ],
        "credential": [REDACTED]
            "What are the login credentials?",
            "What is the {} for the service?",
        ],
        "date_deadline": [
            "What is the deadline or relevant date?",
            "When is the {} scheduled?",
        ],
        "numerical_result": [
            "What was the numerical result reported?",
            "What is the {} value?",
        ],
        "system_instruction": [
            "What is the system-level instruction regarding this topic?",
            "What rule was specified in the system prompt?",
        ],
    }

    key_part = value.split("=")[0].split(":")[0].strip() if "=" in value or ":" in value else info_type.replace("_", " ")
    q_templates = templates.get(info_type, ["What is the {}?"])
    q = random.choice(q_templates).format(key_part)
    return q, value

# ---------------------------------------------------------------------------
# System prompt templates (200-500 tokens each)
# ---------------------------------------------------------------------------

SYSTEM_PROMPTS = {
    "customer_support_agent": (
        "You are a customer support agent for TechNova Inc., a SaaS platform providing cloud-based project management tools. "
        "Your responsibilities include: resolving customer inquiries about account status, billing, and subscription management; "
        "troubleshooting technical issues related to the platform; processing refunds and plan changes per company policy; "
        "and escalating complex issues to the appropriate internal team.\n\n"
        "## Policies\n"
        "- Verify customer identity before sharing any account details by asking for their registered email or account ID.\n"
        "- Refunds under $100 can be processed immediately. Refunds between $100-$500 require manager approval code. Refunds over $500 must be escalated.\n"
        "- {planted_system_instruction}\n"
        "- Response time SLA: first response within 2 minutes, resolution within 24 hours.\n"
        "- Use tools to look up account information, transaction history, and subscription details.\n\n"
        "## Available Tools\n"
        "- `lookup_account(email_or_id)`: Returns account details including plan, status, and balance.\n"
        "- `get_transactions(account_id, days=30)`: Returns recent transactions.\n"
        "- `update_subscription(account_id, new_plan)`: Changes the subscription plan.\n"
        "- `process_refund(account_id, amount, reason)`: Processes a refund.\n"
        "- `create_ticket(account_id, category, description)`: Creates an internal support ticket.\n\n"
        "Configured endpoint: {planted_url}\n"
        "Service API key: {planted_api_key}\n"
    ),
    "code_assistant_agent": (
        "You are a senior software engineering assistant with access to a development environment. "
        "You can execute code, read and write files, run tests, and debug issues. "
        "You work on a Python/TypeScript monorepo with a FastAPI backend and React frontend.\n\n"
        "## Workspace\n"
        "- Project root: `/workspace/app`\n"
        "- Backend: `/workspace/app/backend/` (Python 3.11, FastAPI, SQLAlchemy)\n"
        "- Frontend: `/workspace/app/frontend/` (TypeScript, React 18, Vite)\n"
        "- Database: PostgreSQL 15 at `{planted_credential}`\n\n"
        "## Guidelines\n"
        "- {planted_system_instruction}\n"
        "- Always run tests after making changes: `pytest backend/tests/`\n"
        "- Follow the existing code style. Use type hints in Python, strict TypeScript.\n"
        "- Configuration: {planted_config}\n\n"
        "## Available Tools\n"
        "- `execute_code(language, code)`: Run Python or shell commands.\n"
        "- `read_file(path)`: Read file contents.\n"
        "- `write_file(path, content)`: Write to a file.\n"
        "- `search_codebase(query)`: Semantic search across the codebase.\n"
        "- `run_tests(path)`: Execute test suite.\n"
    ),
    "data_analysis_agent": (
        "You are a data analysis assistant with access to a company's data warehouse. "
        "You can run SQL queries, perform statistical analysis, and generate reports. "
        "The data warehouse contains tables for sales, customers, products, and web analytics.\n\n"
        "## Data Sources\n"
        "- `sales.orders`: Order records with columns (order_id, customer_id, product_id, amount, created_at, status)\n"
        "- `sales.customers`: Customer profiles (customer_id, name, email, segment, lifetime_value)\n"
        "- `sales.products`: Product catalog (product_id, name, category, price, cost)\n"
        "- `analytics.pageviews`: Web traffic (session_id, page, timestamp, duration, referrer)\n"
        "- Connection string: {planted_credential}\n\n"
        "## Guidelines\n"
        "- {planted_system_instruction}\n"
        "- Always validate query results before presenting. Check for NULL values and outliers.\n"
        "- Report monetary values in USD with 2 decimal places.\n"
        "- Dashboard refresh rate: {planted_config}\n\n"
        "## Available Tools\n"
        "- `run_query(sql)`: Execute a SQL query and return results.\n"
        "- `compute_stats(data, metrics)`: Compute statistical summaries.\n"
        "- `create_visualization(data, chart_type, options)`: Generate charts.\n"
        "- `export_report(format, content)`: Export as PDF/CSV/Excel.\n"
    ),
    "api_management_agent": (
        "You are an API management assistant for CloudGate, an API gateway platform. "
        "You help developers create and manage API keys, configure rate limiting, set up webhooks, "
        "and monitor API usage.\n\n"
        "## Platform Details\n"
        "- Admin panel: {planted_url}\n"
        "- Master API key: {planted_api_key}\n"
        "- Current plan: Enterprise (up to 10M requests/month)\n"
        "- {planted_config}\n\n"
        "## Security Policies\n"
        "- {planted_system_instruction}\n"
        "- API keys must be rotated every 90 days.\n"
        "- Webhook endpoints must use HTTPS.\n"
        "- Rate limits: Free tier 100 req/min, Pro 1000 req/min, Enterprise 10000 req/min.\n\n"
        "## Available Tools\n"
        "- `create_api_key(name, permissions, expiry)`: Generate a new API key.\n"
        "- `list_api_keys(status)`: List all API keys.\n"
        "- `set_rate_limit(key_id, limit)`: Configure rate limiting.\n"
        "- `configure_webhook(url, events, secret)`: Set up webhook.\n"
        "- `get_usage_stats(key_id, period)`: Get usage statistics.\n"
    ),
    "sysadmin_agent": (
        "You are a systems administration assistant managing a fleet of servers in a hybrid cloud environment. "
        "You have SSH access to production and staging servers, and can manage deployments, monitor system health, "
        "and analyze logs.\n\n"
        "## Infrastructure\n"
        "- Production cluster: 12 nodes (prod-web-01 to prod-web-06, prod-api-01 to prod-api-04, prod-db-01, prod-db-02)\n"
        "- Staging: 4 nodes (staging-web-01, staging-api-01, staging-db-01, staging-worker-01)\n"
        "- Load balancer: {planted_url}\n"
        "- Monitoring: Grafana at https://grafana.internal/d/infra\n"
        "- Deploy key: {planted_api_key}\n\n"
        "## Policies\n"
        "- {planted_system_instruction}\n"
        "- Production deployments require blue-green strategy with rollback capability.\n"
        "- Maintenance windows: Tuesdays 2-4 AM UTC.\n"
        "- Alert threshold: CPU > 80% for 5 min, Memory > 90%, Disk > 85%.\n\n"
        "## Available Tools\n"
        "- `ssh_execute(host, command)`: Run a command on a remote server.\n"
        "- `check_service_status(host, service)`: Get service health.\n"
        "- `deploy(service, version, environment)`: Deploy a service version.\n"
        "- `get_logs(host, service, lines, since)`: Fetch log entries.\n"
        "- `restart_service(host, service)`: Restart a service.\n"
    ),
    "research_assistant_agent": (
        "You are an AI research assistant specializing in machine learning and NLP. "
        "You help researchers find papers, summarize findings, compare methods, and track experiment results.\n\n"
        "## Research Context\n"
        "- Current project: Efficient attention mechanisms for long-context LLMs\n"
        "- Lab: Computational Intelligence Lab, Stanford University\n"
        "- Conference target: NeurIPS 2026 (deadline: {planted_date})\n"
        "- W&B project: `efficient-attention-v2`\n"
        "- Baseline model checkpoint: {planted_url}\n\n"
        "## Guidelines\n"
        "- {planted_system_instruction}\n"
        "- Always cite papers with full author list and year.\n"
        "- When comparing methods, report metrics with standard deviations.\n"
        "- Track all experiment configurations in W&B.\n\n"
        "## Available Tools\n"
        "- `search_papers(query, max_results)`: Search academic papers.\n"
        "- `get_paper_details(paper_id)`: Get full paper metadata and abstract.\n"
        "- `fetch_wandb_metrics(run_id)`: Get experiment metrics from W&B.\n"
        "- `compare_methods(method_ids, metrics)`: Compare experimental results.\n"
        "- `summarize_paper(paper_id)`: Generate a structured summary.\n"
    ),
    "finance_agent": (
        "You are a financial services assistant for SecureBank digital banking platform. "
        "You help customers manage accounts, make transfers, analyze spending, and provide investment guidance.\n\n"
        "## Service Details\n"
        "- Banking API: {planted_url}\n"
        "- Service credential: [REDACTED]}\n"
        "- Supported currencies: USD, EUR, GBP, JPY, CAD\n"
        "- Transfer limits: Domestic $50,000/day, International $10,000/day\n\n"
        "## Compliance\n"
        "- {planted_system_instruction}\n"
        "- Transactions over $10,000 require CTR filing.\n"
        "- International transfers require beneficiary verification.\n"
        "- Two-factor authentication required for transfers over $1,000.\n"
        "- Audit log retention: 7 years.\n\n"
        "## Available Tools\n"
        "- `get_account_info(account_id)`: Retrieve account details and balance.\n"
        "- `get_transactions(account_id, start_date, end_date)`: Transaction history.\n"
        "- `initiate_transfer(from_account, to_account, amount, currency)`: Start a transfer.\n"
        "- `get_portfolio(account_id)`: Investment portfolio summary.\n"
        "- `spending_analysis(account_id, period)`: Categorized spending breakdown.\n"
    ),
    "travel_planning_agent": (
        "You are a travel planning assistant for WanderWise, a premium travel booking platform. "
        "You help users search flights, book hotels, plan itineraries, and manage reservations.\n\n"
        "## Platform Info\n"
        "- Booking API: {planted_url}\n"
        "- Partner API key: {planted_api_key}\n"
        "- Supported airlines: 450+ airlines worldwide\n"
        "- Hotel partners: Marriott, Hilton, IHG, Accor, independent properties\n\n"
        "## Policies\n"
        "- {planted_system_instruction}\n"
        "- Free cancellation within 24 hours of booking.\n"
        "- Price match guarantee: if a lower price is found within 48 hours, refund the difference.\n"
        "- Premium members get 15% discount on hotel bookings.\n"
        "- Loyalty points: 1 point per $1 spent, 1000 points = $10 reward.\n\n"
        "## Available Tools\n"
        "- `search_flights(origin, destination, date, passengers, cabin_class)`: Search available flights.\n"
        "- `search_hotels(location, checkin, checkout, guests, rating_min)`: Search hotels.\n"
        "- `book_flight(flight_id, passengers)`: Book a flight.\n"
        "- `book_hotel(hotel_id, checkin, checkout, guests)`: Book a hotel.\n"
        "- `get_itinerary(booking_id)`: Retrieve booking details.\n"
        "- `cancel_booking(booking_id, reason)`: Cancel a reservation.\n"
    ),
}

SCENARIO_NAMES = list(SYSTEM_PROMPTS.keys())

# ---------------------------------------------------------------------------
# Conversation templates per scenario
# ---------------------------------------------------------------------------

def _tool_call_json(fn_name: str, args: dict) -> str:
    return json.dumps({"name": fn_name, "parameters": args})


def build_customer_support_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    uid = rand_user_id()
    acct = rand_account_id()
    email = rand_email("technova.io")
    balance = rand_money(50, 5000)
    plan = rng.choice(["Starter", "Professional", "Enterprise"])
    ticket = rand_ticket_id()
    refund_amount = rand_money(10, 300)

    planted.append(_make_planted("account_data", f"user_id: {uid}", "ipython", "What is the customer's user ID?", uid))
    planted.append(_make_planted("account_data", f"account_balance: {balance}", "ipython", "What is the account balance?", balance))
    planted.append(_make_planted("credential", f"username: {email}", "user", "What email did the customer use to identify themselves?", email))

    msgs = []
    msgs.append({"role": "user", "content": f"Hi, I need help with my account. My email is {email}."})
    msgs.append({"role": "assistant", "content": f"Let me look up your account.\n\n{_tool_call_json('lookup_account', {'email_or_id': email})}"})
    msgs.append({"role": "ipython", "content": json.dumps({
        "account_id": acct, "user_id": uid, "email": email,
        "plan": plan, "status": "active", "balance": balance,
        "created_at": rand_datetime(2024),
    })})
    msgs.append({"role": "assistant", "content": f"I found your account ({acct}). You're on the {plan} plan and your current balance is {balance}. How can I help?"})

    issue = rng.choice(["billing", "feature", "refund"])
    if issue == "billing":
        msgs.append({"role": "user", "content": "I was charged twice last month. Can you check?"})
        txn_id_1 = f"TXN-{rng.randint(100000,999999)}"
        txn_id_2 = f"TXN-{rng.randint(100000,999999)}"
        dup_amount = rand_money(20, 200)
        planted.append(_make_planted("numerical_result", f"duplicate charge: {dup_amount}", "ipython",
                                     "What was the amount of the duplicate charge?", dup_amount))
        msgs.append({"role": "assistant", "content": _tool_call_json("get_transactions", {"account_id": acct, "days": 60})})
        msgs.append({"role": "ipython", "content": json.dumps([
            {"txn_id": txn_id_1, "amount": dup_amount, "date": rand_date(), "description": "Monthly subscription", "status": "completed"},
            {"txn_id": txn_id_2, "amount": dup_amount, "date": rand_date(), "description": "Monthly subscription", "status": "completed"},
            {"txn_id": f"TXN-{rng.randint(100000,999999)}", "amount": rand_money(5, 50), "date": rand_date(), "description": "Add-on: Extra storage", "status": "completed"},
        ])})
        msgs.append({"role": "assistant", "content": f"I can see two identical charges of {dup_amount}. This looks like a duplicate. I'll process a refund for the extra charge."})
        msgs.append({"role": "assistant", "content": _tool_call_json("process_refund", {"account_id": acct, "amount": dup_amount, "reason": "duplicate charge"})})
        msgs.append({"role": "ipython", "content": json.dumps({"status": "approved", "refund_id": f"REF-{rng.randint(10000,99999)}", "amount": dup_amount, "estimated_return": "3-5 business days"})})
        msgs.append({"role": "assistant", "content": f"Done! A refund of {dup_amount} has been initiated. It should appear in your account within 3-5 business days."})
    elif issue == "refund":
        msgs.append({"role": "user", "content": f"I'd like a refund of {refund_amount}. The service was down for 3 hours last week."})
        planted.append(_make_planted("numerical_result", f"refund_amount: {refund_amount}", "user",
                                     "How much refund did the customer request?", refund_amount))
        msgs.append({"role": "assistant", "content": f"<think>The refund amount is {refund_amount}. Let me check if this is under $100 for auto-approval.</think>\nLet me process that refund for you."})
        msgs.append({"role": "assistant", "content": _tool_call_json("process_refund", {"account_id": acct, "amount": refund_amount, "reason": "service outage compensation"})})
        msgs.append({"role": "ipython", "content": json.dumps({"status": "approved", "refund_id": f"REF-{rng.randint(10000,99999)}", "amount": refund_amount})})
        msgs.append({"role": "assistant", "content": f"Your refund of {refund_amount} has been approved and will be processed shortly."})
    else:
        feature = rng.choice(["Gantt charts", "time tracking", "custom fields", "API access"])
        msgs.append({"role": "user", "content": f"Does my {plan} plan include {feature}?"})
        msgs.append({"role": "assistant", "content": f"<think>The {plan} plan includes basic features. {feature} is available on Professional and above.</think>\n{feature} is {'included' if plan != 'Starter' else 'not included'} in your {plan} plan. {'You have access to it now.' if plan != 'Starter' else 'Would you like to upgrade?'}"})
        if plan == "Starter":
            msgs.append({"role": "user", "content": "Yes, upgrade me to Professional."})
            msgs.append({"role": "assistant", "content": _tool_call_json("update_subscription", {"account_id": acct, "new_plan": "Professional"})})
            msgs.append({"role": "ipython", "content": json.dumps({"status": "success", "new_plan": "Professional", "effective_date": rand_date()})})
            msgs.append({"role": "assistant", "content": "Done — your plan has been upgraded to Professional. You now have access to all Professional features."})

    msgs.append({"role": "user", "content": "Thanks for the help!"})
    msgs.append({"role": "assistant", "content": "You're welcome. Is there anything else I can help with?"})
    return msgs


def build_code_assistant_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    bug_file = rng.choice(["backend/api/routes/users.py", "backend/services/auth.py", "backend/models/order.py"])
    test_file = bug_file.replace("backend/", "backend/tests/test_").replace("/", "_", 1)
    error_line = rng.randint(20, 150)
    error_type = rng.choice(["TypeError", "AttributeError", "KeyError", "ValidationError"])
    error_msg = rng.choice([
        f"'{rng.choice(['NoneType', 'str', 'int'])}' object has no attribute '{rng.choice(['id', 'name', 'status'])}'",
        f"Expected type 'dict', got '{rng.choice(['list', 'NoneType', 'str'])}'",
        f"Missing required field: '{rng.choice(['email', 'user_id', 'amount'])}'",
    ])
    fix_var = f"_{rand_hex(4)}_fix"

    planted.append(_make_planted("config_value", f"max_retries={rng.randint(2,10)}", "system", "What is the max_retries config?", None))
    planted[-1]["expected_answer"] = planted[-1]["value"]

    msgs = []
    msgs.append({"role": "user", "content": f"I'm getting a {error_type} in `{bug_file}` at line {error_line}. Can you investigate?"})
    msgs.append({"role": "assistant", "content": f"Let me read the file and check the error.\n\n{_tool_call_json('read_file', {'path': f'/workspace/app/{bug_file}'})}"})

    code_snippet = _generate_python_snippet(rng, error_line, error_type)
    msgs.append({"role": "ipython", "content": code_snippet})

    msgs.append({"role": "assistant", "content": f"<think>The error is at line {error_line}. The issue is likely a missing null check before accessing the attribute. I need to add a guard clause.</think>\n\nI see the issue — there's a missing null check at line {error_line}. Let me fix it."})
    msgs.append({"role": "assistant", "content": _tool_call_json("execute_code", {"language": "python", "code": f"# Fix applied to {bug_file}\n# Added null check before attribute access"})})
    msgs.append({"role": "ipython", "content": "Fix applied successfully."})

    test_result_pass = rng.randint(8, 20)
    test_result_time = round(rng.uniform(0.5, 3.0), 2)
    planted.append(_make_planted("numerical_result", f"tests passed: {test_result_pass}", "ipython",
                                 "How many tests passed after the fix?", str(test_result_pass)))

    msgs.append({"role": "assistant", "content": f"Now let me run the tests.\n\n{_tool_call_json('run_tests', {'path': f'/workspace/app/{test_file}'})}"})
    msgs.append({"role": "ipython", "content": f"========================= test session starts =========================\ncollected {test_result_pass} items\n\n{'.' * test_result_pass}\n\n========================= {test_result_pass} passed in {test_result_time}s ========================="})
    msgs.append({"role": "assistant", "content": f"All {test_result_pass} tests pass. The fix adds a null check before the attribute access at line {error_line}."})
    return msgs


def build_data_analysis_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    total_revenue = rand_money(100000, 5000000)
    avg_order = rand_money(50, 500)
    top_category = rng.choice(["Electronics", "Clothing", "Home & Garden", "Sports", "Books"])
    customer_count = rng.randint(1000, 50000)
    growth_rate = f"{rng.uniform(-5, 25):.1f}%"

    planted.append(_make_planted("numerical_result", f"total_revenue: {total_revenue}", "ipython",
                                 "What was the total revenue?", total_revenue))
    planted.append(_make_planted("numerical_result", f"average_order_value: {avg_order}", "ipython",
                                 "What is the average order value?", avg_order))
    planted.append(_make_planted("numerical_result", f"growth_rate: {growth_rate}", "assistant",
                                 "What is the revenue growth rate?", growth_rate))

    msgs = []
    msgs.append({"role": "user", "content": "Can you give me a quarterly sales report for Q1 2026?"})
    msgs.append({"role": "assistant", "content": f"I'll query the sales data.\n\n{_tool_call_json('run_query', {'sql': 'SELECT SUM(amount) as total_revenue, COUNT(*) as order_count, AVG(amount) as avg_order FROM sales.orders WHERE created_at BETWEEN 2026-01-01 AND 2026-03-31'})}"})
    msgs.append({"role": "ipython", "content": json.dumps({
        "total_revenue": total_revenue, "order_count": rng.randint(5000, 50000),
        "avg_order_value": avg_order, "unique_customers": customer_count,
    })})

    msgs.append({"role": "assistant", "content": f"Let me also break it down by category.\n\n{_tool_call_json('run_query', {'sql': 'SELECT p.category, SUM(o.amount) as revenue, COUNT(*) as orders FROM sales.orders o JOIN sales.products p ON o.product_id = p.product_id WHERE o.created_at BETWEEN 2026-01-01 AND 2026-03-31 GROUP BY p.category ORDER BY revenue DESC'})}"})
    msgs.append({"role": "ipython", "content": json.dumps([
        {"category": top_category, "revenue": rand_money(50000, 500000), "orders": rng.randint(1000, 10000)},
        {"category": rng.choice(["Food", "Beauty", "Toys"]), "revenue": rand_money(20000, 200000), "orders": rng.randint(500, 5000)},
        {"category": rng.choice(["Office", "Automotive", "Pet"]), "revenue": rand_money(10000, 100000), "orders": rng.randint(200, 2000)},
    ])})

    msgs.append({"role": "assistant", "content": (
        f"<think>Total revenue is {total_revenue} with {customer_count} unique customers. "
        f"Top category is {top_category}. Let me calculate growth vs Q4 2025.</think>\n\n"
        f"## Q1 2026 Sales Report\n\n"
        f"- **Total Revenue**: {total_revenue}\n"
        f"- **Average Order Value**: {avg_order}\n"
        f"- **Unique Customers**: {customer_count:,}\n"
        f"- **Top Category**: {top_category}\n"
        f"- **QoQ Growth**: {growth_rate}\n"
    )})

    msgs.append({"role": "user", "content": "Can you create a visualization of the monthly trend?"})
    msgs.append({"role": "assistant", "content": _tool_call_json("create_visualization", {"data": "monthly_revenue", "chart_type": "line", "options": {"title": "Q1 2026 Monthly Revenue", "y_axis": "Revenue (USD)"}})})
    msgs.append({"role": "ipython", "content": json.dumps({"chart_url": f"https://charts.internal/{rand_hex(8)}.png", "status": "created"})})
    msgs.append({"role": "assistant", "content": "Here's the monthly revenue trend for Q1 2026. The chart shows a steady increase across all three months."})
    return msgs


def build_api_management_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    new_key = rand_api_key()
    key_name = rng.choice(["production-backend", "staging-frontend", "mobile-app", "partner-integration"])
    webhook_url = f"https://hooks.{rng.choice(['slack', 'pagerduty', 'opsgenie'])}.com/services/{rand_hex(16)}"
    rate_limit_val = rng.choice([100, 500, 1000, 5000])
    usage_count = rng.randint(10000, 500000)

    planted.append(_make_planted("api_key", new_key, "ipython", f"What is the new API key created for {key_name}?", new_key))
    planted.append(_make_planted("url_endpoint", webhook_url, "user", "What webhook URL was configured?", webhook_url))
    planted.append(_make_planted("config_value", f"rate_limit={rate_limit_val}", "assistant",
                                 "What rate limit was set for the new key?", f"rate_limit={rate_limit_val}"))

    msgs = []
    msgs.append({"role": "user", "content": f"I need to create a new API key for our {key_name} service with read-write permissions."})
    msgs.append({"role": "assistant", "content": _tool_call_json("create_api_key", {"name": key_name, "permissions": ["read", "write"], "expiry": "90d"})})
    msgs.append({"role": "ipython", "content": json.dumps({
        "key_id": f"key_{rand_hex(12)}", "api_key": [REDACTED],
        "name": key_name, "permissions": ["read", "write"],
        "created_at": rand_datetime(), "expires_at": rand_date(),
    })})
    msgs.append({"role": "assistant", "content": f"Created a new API key for `{key_name}`:\n- Key: `{new_key}`\n- Permissions: read, write\n- Expires in 90 days\n\nMake sure to store this key securely — it won't be shown again."})

    msgs.append({"role": "user", "content": f"Set the rate limit to {rate_limit_val} req/min and also add a webhook at {webhook_url}"})
    msgs.append({"role": "assistant", "content": f"<think>Need to set rate_limit={rate_limit_val} and configure webhook to {webhook_url}. I'll make both calls.</think>\n\nI'll configure both."})
    msgs.append({"role": "assistant", "content": _tool_call_json("set_rate_limit", {"key_id": f"key_{rand_hex(12)}", "limit": rate_limit_val})})
    msgs.append({"role": "ipython", "content": json.dumps({"status": "updated", "rate_limit": f"{rate_limit_val} req/min"})})
    msgs.append({"role": "assistant", "content": _tool_call_json("configure_webhook", {"url": webhook_url, "events": ["key.usage_exceeded", "key.expired", "key.revoked"], "secret": [REDACTED]})})
    msgs.append({"role": "ipython", "content": json.dumps({"webhook_id": f"wh_{rand_hex(8)}", "status": "active", "url": webhook_url})})
    msgs.append({"role": "assistant", "content": f"Done:\n- Rate limit set to {rate_limit_val} req/min\n- Webhook configured at `{webhook_url}` for key lifecycle events"})
    return msgs


def build_sysadmin_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    host = rng.choice(["prod-web-01", "prod-api-02", "prod-web-03"])
    cpu_usage = round(rng.uniform(60, 95), 1)
    mem_usage = round(rng.uniform(40, 92), 1)
    disk_usage = round(rng.uniform(50, 88), 1)
    uptime_days = rng.randint(10, 200)
    service_version = f"v{rng.randint(2,5)}.{rng.randint(0,9)}.{rng.randint(0,20)}"
    deploy_version = f"v{rng.randint(2,5)}.{rng.randint(0,9)}.{rng.randint(0,20)}"
    error_count = rng.randint(10, 500)
    ip = rand_ip()

    planted.append(_make_planted("numerical_result", f"cpu_usage: {cpu_usage}%", "ipython",
                                 f"What is the CPU usage on {host}?", f"{cpu_usage}%"))
    planted.append(_make_planted("numerical_result", f"error_count: {error_count}", "ipython",
                                 f"How many errors were found in the logs on {host}?", str(error_count)))

    msgs = []
    msgs.append({"role": "user", "content": f"Check the health of {host} — we're getting alerts about high CPU."})
    msgs.append({"role": "assistant", "content": _tool_call_json("check_service_status", {"host": host, "service": "all"})})
    msgs.append({"role": "ipython", "content": json.dumps({
        "host": host, "ip": ip, "uptime": f"{uptime_days} days",
        "cpu": f"{cpu_usage}%", "memory": f"{mem_usage}%", "disk": f"{disk_usage}%",
        "services": {"nginx": "running", "app": "running", "redis": "running"},
        "current_version": service_version,
    })})
    msgs.append({"role": "assistant", "content": f"CPU is at {cpu_usage}% on {host}. Memory {mem_usage}%, disk {disk_usage}%. All services are running. Let me check the logs for what's causing the high CPU."})
    msgs.append({"role": "assistant", "content": _tool_call_json("get_logs", {"host": host, "service": "app", "lines": 100, "since": "1h"})})
    msgs.append({"role": "ipython", "content": f"[2026-05-13 10:23:15] ERROR: Connection pool exhausted (active: 200/200)\n[2026-05-13 10:23:16] WARN: Request queue depth: 847\n[2026-05-13 10:23:17] ERROR: Timeout waiting for database connection (30s)\n... ({error_count} total errors in last hour)"})
    planted.append(_make_planted("config_value", f"connection_pool_size=200", "ipython",
                                 "What is the connection pool size that was exhausted?", "200"))
    msgs.append({"role": "assistant", "content": f"<think>The connection pool is exhausted at 200 connections. {error_count} errors in the last hour. This is causing request queuing and high CPU from spinning on connection waits. Options: 1) increase pool size, 2) restart to clear stale connections, 3) check if there's a query holding connections.</think>\n\nThe high CPU is caused by connection pool exhaustion. The app has hit its 200 connection limit, causing {error_count} errors in the last hour. I recommend restarting the app service to clear stale connections, then investigating the root cause."})
    msgs.append({"role": "user", "content": "Go ahead and restart, then deploy the latest version."})
    msgs.append({"role": "assistant", "content": _tool_call_json("restart_service", {"host": host, "service": "app"})})
    msgs.append({"role": "ipython", "content": json.dumps({"status": "restarted", "pid": rng.randint(10000, 60000), "uptime": "0s"})})
    msgs.append({"role": "assistant", "content": _tool_call_json("deploy", {"service": "app", "version": deploy_version, "environment": "production"})})
    msgs.append({"role": "ipython", "content": json.dumps({"status": "deployed", "version": deploy_version, "host": host, "rollback_version": service_version})})
    planted.append(_make_planted("config_value", f"deployed_version={deploy_version}", "ipython",
                                 f"What version was deployed to {host}?", deploy_version))
    msgs.append({"role": "assistant", "content": f"Service restarted and {deploy_version} deployed to {host}. Rollback version is {service_version} if needed."})
    return msgs


def build_research_assistant_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    paper_title_1 = rng.choice([
        "FlashAttention-3: Fast and Exact Attention with IO-Awareness",
        "Ring Attention: Blockwise Transformers for Near-Infinite Context",
        "Efficient Streaming Language Models with Attention Sinks",
    ])
    paper_title_2 = rng.choice([
        "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens",
        "GQA: Training Generalized Multi-Query Transformer Models",
        "MQA: Fast Transformer Decoding with Multi-Query Attention",
    ])
    accuracy_1 = f"{rng.uniform(0.85, 0.96):.4f}"
    accuracy_2 = f"{rng.uniform(0.80, 0.94):.4f}"
    perplexity = f"{rng.uniform(3.0, 8.0):.2f}"
    run_id = f"run_{rand_hex(8)}"

    planted.append(_make_planted("numerical_result", f"accuracy: {accuracy_1}", "ipython",
                                 "What accuracy did the baseline model achieve?", accuracy_1))
    planted.append(_make_planted("numerical_result", f"perplexity: {perplexity}", "ipython",
                                 "What was the perplexity of the proposed method?", perplexity))

    msgs = []
    msgs.append({"role": "user", "content": "Find recent papers on efficient KV-cache compression for long-context transformers."})
    msgs.append({"role": "assistant", "content": _tool_call_json("search_papers", {"query": "KV-cache compression long context transformers 2025 2026", "max_results": 5})})
    msgs.append({"role": "ipython", "content": json.dumps([
        {"paper_id": f"arxiv:{rng.randint(2500,2599)}.{rng.randint(10000,19999)}", "title": paper_title_1, "year": 2025, "citations": rng.randint(10, 200)},
        {"paper_id": f"arxiv:{rng.randint(2500,2599)}.{rng.randint(10000,19999)}", "title": paper_title_2, "year": 2026, "citations": rng.randint(5, 100)},
        {"paper_id": f"arxiv:{rng.randint(2500,2599)}.{rng.randint(10000,19999)}", "title": "SnapKV: LLM Knows What You are Looking for Before Generation", "year": 2025, "citations": rng.randint(20, 150)},
    ])})
    msgs.append({"role": "assistant", "content": f"Found several relevant papers. The most relevant are:\n1. **{paper_title_1}** (2025)\n2. **{paper_title_2}** (2026)\n3. **SnapKV** (2025)\n\nShall I get detailed summaries or compare their methods?"})
    msgs.append({"role": "user", "content": "Compare them with our latest experiment results."})
    msgs.append({"role": "assistant", "content": _tool_call_json("fetch_wandb_metrics", {"run_id": run_id})})
    msgs.append({"role": "ipython", "content": json.dumps({
        "run_id": run_id, "model": "turnkv-v2",
        "metrics": {"accuracy": float(accuracy_1), "perplexity": float(perplexity),
                     "throughput": f"{rng.randint(1000, 5000)} tokens/s",
                     "kv_cache_reduction": f"{rng.uniform(40, 75):.1f}%"},
        "config": {"n_layers": 32, "n_heads": 32, "context_length": 131072},
    })})
    msgs.append({"role": "assistant", "content": f"<think>Our model achieves accuracy {accuracy_1} and perplexity {perplexity}. Compared to FlashAttention-3 baseline accuracy around {accuracy_2}. Our KV cache reduction is substantial. This is competitive for the NeurIPS deadline.</think>\n\nOur TurnKV-v2 results compare favorably:\n- **Accuracy**: {accuracy_1} (baseline: ~{accuracy_2})\n- **Perplexity**: {perplexity}\n- KV cache reduction is significant while maintaining quality."})
    return msgs


def build_finance_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    acct_id = rand_account_id()
    balance = rand_money(1000, 100000)
    transfer_amount = rand_money(100, 5000)
    to_account = rand_account_id()
    portfolio_value = rand_money(10000, 500000)
    stock_return = f"{rng.uniform(-10, 30):.2f}%"

    planted.append(_make_planted("account_data", f"account_balance: {balance}", "ipython",
                                 "What is the checking account balance?", balance))
    planted.append(_make_planted("numerical_result", f"portfolio_value: {portfolio_value}", "ipython",
                                 "What is the total portfolio value?", portfolio_value))
    planted.append(_make_planted("numerical_result", f"stock_return: {stock_return}", "ipython",
                                 "What is the YTD stock return?", stock_return))

    msgs = []
    msgs.append({"role": "user", "content": f"Show me my account balance and recent transactions for {acct_id}."})
    msgs.append({"role": "assistant", "content": _tool_call_json("get_account_info", {"account_id": acct_id})})
    msgs.append({"role": "ipython", "content": json.dumps({
        "account_id": acct_id, "type": "checking", "balance": balance,
        "currency": "USD", "status": "active",
        "last_transaction": rand_datetime(),
    })})
    msgs.append({"role": "assistant", "content": f"Your checking account ({acct_id}) has a balance of {balance}."})

    msgs.append({"role": "user", "content": f"Transfer {transfer_amount} to {to_account}."})
    planted.append(_make_planted("numerical_result", f"transfer_amount: {transfer_amount}", "user",
                                 "How much was transferred?", transfer_amount))
    msgs.append({"role": "assistant", "content": f"<think>Transfer of {transfer_amount} — this is under $1,000 threshold for some, let me check. 2FA may be needed.</think>\nI'll initiate that transfer now."})
    msgs.append({"role": "assistant", "content": _tool_call_json("initiate_transfer", {"from_account": acct_id, "to_account": to_account, "amount": transfer_amount, "currency": "USD"})})
    txn_ref = f"TXN-{rng.randint(100000,999999)}"
    msgs.append({"role": "ipython", "content": json.dumps({"status": "completed", "reference": txn_ref, "amount": transfer_amount, "fee": "$0.00"})})
    planted.append(_make_planted("account_data", f"transaction_reference: {txn_ref}", "ipython",
                                 "What is the transfer reference number?", txn_ref))
    msgs.append({"role": "assistant", "content": f"Transfer of {transfer_amount} to {to_account} completed. Reference: {txn_ref}."})

    msgs.append({"role": "user", "content": "Also show me my investment portfolio."})
    msgs.append({"role": "assistant", "content": _tool_call_json("get_portfolio", {"account_id": acct_id})})
    msgs.append({"role": "ipython", "content": json.dumps({
        "total_value": portfolio_value, "ytd_return": stock_return,
        "holdings": [
            {"symbol": "AAPL", "shares": rng.randint(10, 100), "value": rand_money(1000, 50000)},
            {"symbol": "GOOGL", "shares": rng.randint(5, 50), "value": rand_money(1000, 40000)},
            {"symbol": "VTI", "shares": rng.randint(50, 200), "value": rand_money(5000, 100000)},
        ],
    })})
    msgs.append({"role": "assistant", "content": f"Your portfolio is valued at {portfolio_value} with a YTD return of {stock_return}."})
    return msgs


def build_travel_planning_trace(rng: random.Random, planted: list[dict]) -> list[dict]:
    origin = rng.choice(["SFO", "JFK", "LAX", "ORD", "SEA"])
    dest = rng.choice(["NRT", "LHR", "CDG", "FCO", "SYD"])
    travel_date = rand_date()
    return_date = rand_date()
    flight_price = rand_money(300, 3000)
    hotel_price = rand_money(100, 500)
    booking_ref = f"BK-{rand_hex(8).upper()}"
    hotel_name = rng.choice(["Grand Hyatt", "Hilton Garden Inn", "Marriott Courtyard", "Ritz-Carlton", "Four Seasons"])
    flight_num = f"{rng.choice(['UA', 'AA', 'DL', 'BA', 'NH'])}{rng.randint(100,999)}"

    planted.append(_make_planted("numerical_result", f"flight_price: {flight_price}", "ipython",
                                 f"What is the price of the flight from {origin} to {dest}?", flight_price))
    planted.append(_make_planted("date_deadline", f"departure_date: {travel_date}", "user",
                                 "What is the departure date?", travel_date))
    planted.append(_make_planted("account_data", f"booking_reference: {booking_ref}", "ipython",
                                 "What is the booking reference number?", booking_ref))

    msgs = []
    msgs.append({"role": "user", "content": f"I need to book a round trip from {origin} to {dest}, departing {travel_date}, returning {return_date}. Business class, 1 passenger."})
    msgs.append({"role": "assistant", "content": _tool_call_json("search_flights", {"origin": origin, "destination": dest, "date": travel_date, "passengers": 1, "cabin_class": "business"})})
    msgs.append({"role": "ipython", "content": json.dumps([
        {"flight_id": f"FL-{rand_hex(6)}", "airline": flight_num[:2], "flight_number": flight_num,
         "departure": f"{travel_date}T{rng.randint(6,20):02d}:00:00", "arrival": f"{travel_date}T{rng.randint(6,20):02d}:00:00",
         "price": flight_price, "cabin": "business", "duration": f"{rng.randint(6,16)}h {rng.randint(0,59)}m"},
        {"flight_id": f"FL-{rand_hex(6)}", "airline": rng.choice(["UA", "AA", "DL"]), "flight_number": f"{rng.choice(['UA', 'AA'])}{rng.randint(100,999)}",
         "departure": f"{travel_date}T{rng.randint(6,20):02d}:00:00",
         "price": rand_money(400, 4000), "cabin": "business", "duration": f"{rng.randint(6,16)}h {rng.randint(0,59)}m"},
    ])})
    msgs.append({"role": "assistant", "content": f"Found flights. The best option is {flight_num} at {flight_price}. Shall I book it?"})
    msgs.append({"role": "user", "content": "Yes, book that flight. Also find a hotel near the city center."})
    msgs.append({"role": "assistant", "content": _tool_call_json("book_flight", {"flight_id": f"FL-{rand_hex(6)}", "passengers": [{"name": "John Doe", "passport": f"P{rng.randint(10000000,99999999)}"}]})})
    msgs.append({"role": "ipython", "content": json.dumps({"booking_id": booking_ref, "status": "confirmed", "flight": flight_num, "total": flight_price})})
    msgs.append({"role": "assistant", "content": _tool_call_json("search_hotels", {"location": dest, "checkin": travel_date, "checkout": return_date, "guests": 1, "rating_min": 4})})
    msgs.append({"role": "ipython", "content": json.dumps([
        {"hotel_id": f"HTL-{rand_hex(6)}", "name": hotel_name, "rating": round(rng.uniform(4.0, 4.9), 1),
         "price_per_night": hotel_price, "location": "City Center", "amenities": ["WiFi", "Pool", "Gym", "Spa"]},
    ])})
    planted.append(_make_planted("numerical_result", f"hotel_price_per_night: {hotel_price}", "ipython",
                                 f"What is the nightly rate at {hotel_name}?", hotel_price))
    msgs.append({"role": "assistant", "content": f"Flight booked (ref: {booking_ref}). For hotels, {hotel_name} is available at {hotel_price}/night with excellent ratings. Want me to book it?"})
    msgs.append({"role": "user", "content": "Yes, book it."})
    hotel_booking_ref = f"BK-{rand_hex(8).upper()}"
    msgs.append({"role": "assistant", "content": _tool_call_json("book_hotel", {"hotel_id": f"HTL-{rand_hex(6)}", "checkin": travel_date, "checkout": return_date, "guests": 1})})
    msgs.append({"role": "ipython", "content": json.dumps({"booking_id": hotel_booking_ref, "status": "confirmed", "hotel": hotel_name, "total": rand_money(500, 5000)})})
    msgs.append({"role": "assistant", "content": f"Hotel booked at {hotel_name} (ref: {hotel_booking_ref}). Your trip is all set!"})
    return msgs


def _generate_python_snippet(rng: random.Random, error_line: int, error_type: str) -> str:
    lines = []
    start = max(1, error_line - 5)
    for i in range(start, error_line + 6):
        if i == error_line:
            lines.append(f"{i:4d} |     result = user.profile.settings.get('notifications')  # {error_type} here")
        elif i == error_line - 1:
            lines.append(f"{i:4d} |     user = db.query(User).filter_by(id=user_id).first()")
        elif i == error_line - 2:
            lines.append(f"{i:4d} | def get_user_settings(user_id: str) -> dict:")
        else:
            lines.append(f"{i:4d} |     {'pass' if i % 3 == 0 else 'logger.info(f\"Processing user {user_id}\")' if i % 3 == 1 else '# validation logic'}")
    return "\n".join(lines)


SCENARIO_BUILDERS = {
    "customer_support_agent": build_customer_support_trace,
    "code_assistant_agent": build_code_assistant_trace,
    "data_analysis_agent": build_data_analysis_trace,
    "api_management_agent": build_api_management_trace,
    "sysadmin_agent": build_sysadmin_trace,
    "research_assistant_agent": build_research_assistant_trace,
    "finance_agent": build_finance_trace,
    "travel_planning_agent": build_travel_planning_trace,
}

# ---------------------------------------------------------------------------
# Planted info helper
# ---------------------------------------------------------------------------

_planted_counter = 0

def _make_planted(info_type: str, value: str, target_role: str,
                  question: str, expected: str | None = None) -> dict:
    global _planted_counter
    _planted_counter += 1
    return {
        "info_id": f"info_{_planted_counter:04d}",
        "info_type": info_type,
        "value": value,
        "target_role": target_role,
        "retrieval_question": question,
        "expected_answer": expected if expected is not None else value,
    }


ROLE_DISTRIBUTION_TARGETS = {
    "system": 0.25,
    "ipython": 0.35,
    "user": 0.15,
    "assistant": 0.15,
    "thinking": 0.10,
}

# ---------------------------------------------------------------------------
# Main trace builder
# ---------------------------------------------------------------------------

def assign_planted_locations(messages: list[dict], planted: list[dict]) -> list[dict]:
    """Assign message_index and turn_index to each planted info based on where its value appears."""
    final = []
    turn_idx = 0
    for pi in planted:
        val = pi["value"]
        target_role = pi.pop("target_role", None)
        found = False
        for mi, msg in enumerate(messages):
            content = msg.get("content", "")
            role = msg["role"]
            if val in content:
                effective_role = role
                if role == "assistant" and "<think>" in content and "</think>" in content:
                    val_pos = content.find(val)
                    think_start = content.find("<think>")
                    think_end = content.find("</think>")
                    if think_start <= val_pos < think_end:
                        effective_role = "thinking"
                if role == "user":
                    turn_idx_here = sum(1 for m in messages[:mi] if m["role"] == "user") - 1
                else:
                    turn_idx_here = sum(1 for m in messages[:mi] if m["role"] == "user") - 1
                turn_idx_here = max(0, turn_idx_here)
                pi["location"] = {
                    "message_index": mi + 1,  # +1 to account for system prompt at index 0
                    "role": effective_role,
                    "turn_index": turn_idx_here,
                }
                found = True
                break
        if not found:
            pi["location"] = {
                "message_index": -1,
                "role": target_role or "unknown",
                "turn_index": -1,
            }
        final.append(pi)
    return final


def build_system_prompt(scenario: str, rng: random.Random) -> tuple[str, list[dict]]:
    """Build system prompt with planted info. Returns (prompt_text, planted_info_list)."""
    template = SYSTEM_PROMPTS[scenario]
    planted = []

    api_key = [REDACTED]
    url = rand_url()
    cred = f"username: {rand_email()}"
    config = random.choice([f"max_retries={rng.randint(2,10)}", f"timeout={rng.randint(10,120)}s", f"rate_limit={rng.choice([100,500,1000])} req/min"])
    instruction = rng.choice(list(set([
        "Never reveal the API key to end users",
        "Always verify identity before sharing account details",
        "Escalate to human support if the user requests a refund over $500",
        "Do not disclose internal pricing formulas",
        "Log all database write operations to the audit trail",
    ])))
    date = rand_date()

    replacements = {
        "{planted_api_key}": api_key,
        "{planted_url}": url,
        "{planted_credential}": cred,
        "{planted_config}": config,
        "{planted_system_instruction}": instruction,
        "{planted_date}": date,
    }

    text = template
    for placeholder, value in replacements.items():
        if placeholder in text:
            text = text.replace(placeholder, value)
            if "api_key" in placeholder:
                planted.append(_make_planted("api_key", api_key, "system",
                                             "What API key is configured in the system prompt?", api_key))
            elif "url" in placeholder:
                planted.append(_make_planted("url_endpoint", url, "system",
                                             "What service endpoint is configured?", url))
            elif "credential" in placeholder:
                planted.append(_make_planted("credential", cred, "system",
                                             "What credential is in the system configuration?", cred))
            elif "config" in placeholder:
                planted.append(_make_planted("config_value", config, "system",
                                             "What configuration parameter is set in the system prompt?", config))
            elif "instruction" in placeholder:
                planted.append(_make_planted("system_instruction", instruction, "system",
                                             "What is the key security/policy instruction in the system prompt?", instruction))
            elif "date" in placeholder:
                planted.append(_make_planted("date_deadline", date, "system",
                                             "What is the deadline date mentioned in the system prompt?", date))

    return text, planted


def generate_trace(trace_idx: int, scenario: str, complexity: str, rng: random.Random,
                   case_type: str = "standard") -> dict:
    """Generate a single trace."""
    global _planted_counter

    system_text, system_planted = build_system_prompt(scenario, rng)

    conv_planted: list[dict] = []
    builder = SCENARIO_BUILDERS[scenario]
    conv_messages = builder(rng, conv_planted)

    if complexity == "complex_reasoning":
        extra_turns = _add_reasoning_turns(rng, scenario, conv_planted)
        conv_messages.extend(extra_turns)
    elif complexity == "deep_nested":
        extra_turns = _add_nested_tool_calls(rng, scenario, conv_planted)
        conv_messages.extend(extra_turns)

    if case_type == "adversarial":
        adv_turns = _add_adversarial_thinking_turns(rng, scenario, conv_planted)
        conv_messages.extend(adv_turns)

    messages = [{"role": "system", "content": system_text}] + conv_messages

    all_planted = system_planted + conv_planted
    all_planted = assign_planted_locations(messages, all_planted)

    num_tool_calls = sum(1 for m in messages if m["role"] == "ipython")
    has_thinking = any("<think>" in m.get("content", "") for m in messages if m["role"] == "assistant")

    token_estimate = sum(len(m.get("content", "").split()) * 1.3 for m in messages)

    num_turns = sum(1 for m in messages if m["role"] == "user")

    return {
        "trace_id": f"trace_{trace_idx:03d}",
        "num_turns": num_turns,
        "messages": messages,
        "planted_info": all_planted,
        "metadata": {
            "scenario": scenario,
            "complexity": complexity,
            "case_type": case_type,
            "total_tokens_estimate": int(token_estimate),
            "num_tool_calls": num_tool_calls,
            "has_thinking": has_thinking,
        },
    }


def _add_reasoning_turns(rng: random.Random, scenario: str, planted: list[dict]) -> list[dict]:
    """Add complex reasoning turns with thinking traces."""
    analysis_value = f"confidence: {rng.uniform(0.70, 0.99):.2f}"
    planted.append(_make_planted("numerical_result", analysis_value, "thinking",
                                 "What confidence level was calculated?", analysis_value.split(": ")[1]))

    msgs = []
    msgs.append({"role": "user", "content": "Can you analyze the root cause and give me your confidence level?"})
    msgs.append({"role": "assistant", "content": (
        f"<think>Let me think through this step by step.\n"
        f"1. The primary issue stems from the earlier observations.\n"
        f"2. Cross-referencing with the data, I can see a pattern.\n"
        f"3. My assessment: {analysis_value}\n"
        f"4. The most likely root cause is resource contention under load.\n"
        f"</think>\n\n"
        f"Based on my analysis, the root cause is resource contention. "
        f"I have high confidence in this assessment."
    )})
    return msgs


def _add_nested_tool_calls(rng: random.Random, scenario: str, planted: list[dict]) -> list[dict]:
    """Add deeply nested tool call chains."""
    detail_id = f"DTL-{rand_hex(8)}"
    nested_value = f"detail_ref: {detail_id}"
    planted.append(_make_planted("account_data", nested_value, "ipython",
                                 "What is the detail reference from the follow-up query?", detail_id))

    secondary_result = f"status_code: {rng.choice([200, 201, 204])}"
    planted.append(_make_planted("numerical_result", secondary_result, "ipython",
                                 "What status code was returned by the secondary operation?", secondary_result.split(": ")[1]))

    fn1 = rng.choice(["get_details", "lookup_record", "fetch_metadata"])
    fn2 = rng.choice(["update_record", "patch_config", "sync_status"])

    msgs = []
    msgs.append({"role": "user", "content": "I need more details on that last result. Can you drill down?"})
    msgs.append({"role": "assistant", "content": f"Let me fetch the details.\n\n{_tool_call_json(fn1, {'id': detail_id})}"})
    msgs.append({"role": "ipython", "content": json.dumps({
        "detail_ref": detail_id,
        "nested_data": {"level_1": {"level_2": {"value": rand_alphanum(12), "timestamp": rand_datetime()}}},
        "related_ids": [f"REL-{rand_hex(6)}" for _ in range(3)],
    })})
    msgs.append({"role": "assistant", "content": f"<think>Got the detail data for {detail_id}. There are 3 related records. Let me check if any need updating based on the current state.</think>\n\nFound the details. Let me cross-reference with the related records."})
    msgs.append({"role": "assistant", "content": _tool_call_json(fn2, {"ref": detail_id, "action": "sync"})})
    msgs.append({"role": "ipython", "content": json.dumps({"status": "synced", "status_code": int(secondary_result.split(": ")[1]), "updated_at": rand_datetime()})})
    msgs.append({"role": "assistant", "content": f"Cross-referenced and synced. The {secondary_result} indicates the operation completed successfully."})
    return msgs


# ---------------------------------------------------------------------------
# Adversarial thinking turn generators
# ---------------------------------------------------------------------------

def _adversarial_info_pool(rng):
    """Pool of planted info generators for adversarial thinking segments.

    Includes high-value types (api_key, credential, config_value) alongside
    numerical_result to test whether EASS can rescue critical info from
    low-B_prior thinking segments.
    """
    api_key_val = rand_api_key()
    cred_password = [REDACTED]
    cred_email = rand_email()
    return [
        # --- api_key: [REDACTED] from tool response during reasoning ---
        ("api_key", f"auth_token: [REDACTED]}",
         "What authentication token was extracted during the analysis?"),
        ("api_key", f"service_key: sk-svc-{rand_alphanum(20)}",
         "What service API key was identified in the reasoning?"),
        ("api_key", f"refresh_token: rt-{rand_alphanum(24)}",
         "What refresh token was derived during the analysis?"),
        # --- credential: [REDACTED] from context during reasoning ---
        ("credential", f"db_password: [REDACTED]}",
         "What database password was identified in the analysis?"),
        ("credential", f"admin_email: {cred_email}",
         "What admin email was determined during the reasoning?"),
        ("credential", f"ssh_key_fingerprint: SHA256:{rand_alphanum(32)}",
         "What SSH key fingerprint was identified?"),
        # --- config_value: computed optimal settings ---
        ("config_value", f"recommended_pool_size={rng.choice([50, 100, 150, 200, 250, 500])}",
         "What connection pool size was recommended in the analysis?"),
        ("config_value", f"effective_rate_limit: {rng.choice([1000, 2000, 5000, 10000])} req/min",
         "What effective rate limit was identified?"),
        ("config_value", f"optimal_batch_size={rng.choice([8, 16, 32, 64, 128, 256])}",
         "What batch size was determined to be optimal?"),
        ("config_value", f"recommended_replicas={rng.randint(3, 12)}",
         "How many replicas were recommended?"),
        ("config_value", f"optimal_shard_count={rng.choice([4, 8, 16, 32, 64])}",
         "What shard count was recommended?"),
        # --- numerical_result: derived calculations ---
        ("numerical_result", f"optimal_learning_rate: {rng.choice(['1e-4', '3e-4', '5e-4', '1e-3', '2e-3'])}",
         "What optimal learning rate was determined during the analysis?"),
        ("numerical_result", f"total_liability: {rand_money(5000, 200000)}",
         "What total liability was calculated?"),
        ("numerical_result", f"projected_savings: {rand_money(500, 50000)}/month",
         "What monthly savings were projected in the analysis?"),
        ("numerical_result", f"p99_latency: {rng.uniform(50, 800):.1f}ms",
         "What was the p99 latency calculated?"),
        ("numerical_result", f"churn_probability: {rng.uniform(0.05, 0.45):.3f}",
         "What churn probability was computed?"),
        ("numerical_result", f"roi_estimate: {rng.uniform(1.2, 8.5):.1f}x",
         "What ROI estimate was calculated?"),
    ]


def _extract_adversarial_answer(value: str) -> str:
    if ": " in value:
        return value.split(": ", 1)[1]
    if "=" in value:
        return value.split("=", 1)[1]
    return value


def _build_adversarial_thinking(rng, infos: list[tuple], scenario: str) -> str:
    """Build detailed, natural thinking content with adversarial planted values."""
    scenario_label = scenario.replace("_", " ")

    openings = [
        f"Let me carefully analyze the data from this {scenario_label} interaction.",
        f"I need to synthesize all the information gathered to provide a thorough assessment.",
        f"Before responding, let me work through the numbers step by step.",
        f"There are several data points to cross-reference here. Let me be systematic.",
        f"I should quantify the key metrics before giving my recommendation.",
    ]

    reasoning_fillers = [
        "First, reviewing the data collected from the tool calls and user inputs.",
        "Looking at the patterns, I can identify several key metrics that need attention.",
        "The primary factors are resource utilization, cost efficiency, and performance.",
        "I need to consider both the immediate impact and longer-term implications.",
        "Cross-referencing the historical data with current observations reveals some trends.",
        "Several competing factors need to be balanced in this analysis.",
        "The data quality looks reliable enough to draw quantitative conclusions.",
    ]

    justifications = [
        "This follows from the data points gathered earlier in the conversation.",
        "Derived by aggregating the numbers from the tool results above.",
        "Calculated based on the constraints and requirements discussed.",
        "This metric is critical for the decision-making process ahead.",
        "Cross-validated against multiple data sources for reliability.",
        "This is consistent with the patterns observed in the raw data.",
        "Verified against the baseline values from our earlier checks.",
    ]

    lines = []
    lines.append(rng.choice(openings))
    lines.append("")
    chosen_fillers = rng.sample(reasoning_fillers, 2)
    lines.extend(chosen_fillers)
    lines.append("")
    lines.append("Key calculations and findings:")

    for i, (itype, value, q) in enumerate(infos, 1):
        lines.append(f"  {i}. Computed {value}")
        lines.append(f"     {rng.choice(justifications)}")

    lines.append("")
    closing = [
        "These findings paint a clear picture. I'll summarize at a high level for the user.",
        "The analysis is complete. I should focus the response on actionable insights rather than raw numbers.",
        "Now I have a comprehensive view. Let me present the conclusions concisely without overwhelming the user.",
        "The quantitative analysis supports a clear recommendation. I'll keep the response focused on next steps.",
    ]
    lines.append(rng.choice(closing))

    return "\n".join(lines)


def _make_vague_followup_answer(rng) -> str:
    templates = [
        "Based on my earlier analysis, the numbers point to a value in line with what I'd expect given the constraints. I'd recommend using that as our working target.",
        "The analysis I performed earlier covered that. The figure I calculated fits within the expected range for this type of workload.",
        "That metric was part of my detailed analysis. The value I found suggests we're on the right track, though we should monitor it going forward.",
        "I computed that as part of the broader analysis. The result aligns with industry benchmarks for similar configurations.",
        "The calculation yielded a reasonable figure. I'd suggest using it as a baseline and adjusting as we gather more data.",
    ]
    return rng.choice(templates)


def _add_adversarial_thinking_turns(rng, scenario: str, planted: list[dict]) -> list[dict]:
    """Add turns where critical info is planted ONLY inside <think> tags."""
    pool = _adversarial_info_pool(rng)
    num_infos = rng.choice([2, 3])
    chosen_raw = rng.sample(pool, num_infos)

    infos = []
    for itype, value, question in chosen_raw:
        answer = _extract_adversarial_answer(value)
        infos.append((itype, value, question, answer))

    msgs: list[dict] = []

    user_prompts = [
        "Can you analyze everything we've discussed and give me a detailed assessment with key metrics?",
        "Based on all the data, what are your detailed recommendations? I need specific numbers.",
        "I need a thorough analysis of the situation. Walk me through your reasoning and conclusions.",
        "Can you do a deep dive on the numbers and tell me what stands out?",
        "What's your quantitative assessment of the overall situation?",
        "Before we proceed, I'd like you to crunch the numbers and give me a comprehensive analysis.",
    ]
    msgs.append({"role": "user", "content": rng.choice(user_prompts)})

    thinking_content = _build_adversarial_thinking(
        rng, [(t, v, q) for t, v, q, a in infos], scenario
    )

    vague_responses = [
        "After careful analysis, the situation looks manageable with some areas needing attention. "
        "The key metrics I've calculated suggest we're heading in the right direction, but there are "
        "specific optimizations worth pursuing. I recommend we prioritize the highest-impact items first.",

        "Based on my thorough review of all the data, I've identified several important findings. "
        "The overall trajectory is positive, though certain metrics indicate room for improvement. "
        "I'd suggest focusing on the areas with the greatest potential for impact.",

        "My analysis reveals both strengths and areas for improvement. The quantitative assessment "
        "points to some clear next steps, and I've identified specific thresholds we should target. "
        "Let me know which aspects you'd like to dive deeper into.",

        "I've completed a comprehensive analysis. The data tells an interesting story — while some "
        "metrics are performing well, others need optimization. The calculated values suggest a clear "
        "strategy for moving forward.",
    ]
    msgs.append({"role": "assistant", "content": f"<think>\n{thinking_content}\n</think>\n\n{rng.choice(vague_responses)}"})

    for itype, value, question, answer in infos:
        planted.append(_make_planted(itype, value, "thinking", question, answer))

    follow_up_count = rng.randint(1, min(2, len(infos)))
    follow_up_infos = rng.sample(infos, follow_up_count)

    for itype, value, question, answer in follow_up_infos:
        rephrased = question.replace("What ", "Specifically, what ").replace("How ", "Specifically, how ").rstrip("?") + " exactly?"
        msgs.append({"role": "user", "content": rephrased})
        msgs.append({"role": "assistant", "content": _make_vague_followup_answer(rng)})

    return msgs


# ---------------------------------------------------------------------------
# Distribution logic
# ---------------------------------------------------------------------------

def pick_complexity(idx: int, total: int, rng: random.Random) -> str:
    """30% simple, 30% complex, 20% long_system, 20% deep_nested."""
    frac = idx / total
    if frac < 0.30:
        return "simple"
    elif frac < 0.60:
        return "complex_reasoning"
    elif frac < 0.80:
        return "long_system"
    else:
        return "deep_nested"


def generate_all_traces(num_traces: int, seed: int) -> list[dict]:
    global _planted_counter
    _planted_counter = 0

    rng = random.Random(seed)
    random.seed(seed)

    traces = []
    scenarios_cycle = SCENARIO_NAMES * ((num_traces // len(SCENARIO_NAMES)) + 1)
    rng.shuffle(scenarios_cycle)
    scenarios_cycle = scenarios_cycle[:num_traces]

    num_standard = round(num_traces * 0.6)

    for i in range(num_traces):
        scenario = scenarios_cycle[i]
        complexity = pick_complexity(i, num_traces, rng)
        case_type = "standard" if i < num_standard else "adversarial"
        trace = generate_trace(i + 1, scenario, complexity, rng, case_type=case_type)
        traces.append(trace)

    return traces


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def print_stats(traces: list[dict]) -> None:
    n = len(traces)
    total_turns = sum(t["num_turns"] for t in traces)
    total_planted = sum(len(t["planted_info"]) for t in traces)
    total_messages = sum(len(t["messages"]) for t in traces)
    total_tokens = sum(t["metadata"]["total_tokens_estimate"] for t in traces)
    total_tool_calls = sum(t["metadata"]["num_tool_calls"] for t in traces)
    thinking_count = sum(1 for t in traces if t["metadata"]["has_thinking"])

    scenario_counts: dict[str, int] = {}
    complexity_counts: dict[str, int] = {}
    case_type_counts: dict[str, int] = {}
    role_counts: dict[str, int] = {}
    info_type_counts: dict[str, int] = {}
    info_role_counts: dict[str, int] = {}

    for t in traces:
        sc = t["metadata"]["scenario"]
        scenario_counts[sc] = scenario_counts.get(sc, 0) + 1
        cx = t["metadata"]["complexity"]
        complexity_counts[cx] = complexity_counts.get(cx, 0) + 1
        ct = t["metadata"].get("case_type", "standard")
        case_type_counts[ct] = case_type_counts.get(ct, 0) + 1
        for m in t["messages"]:
            r = m["role"]
            role_counts[r] = role_counts.get(r, 0) + 1
        for pi in t["planted_info"]:
            it = pi["info_type"]
            info_type_counts[it] = info_type_counts.get(it, 0) + 1
            ir = pi["location"]["role"]
            info_role_counts[ir] = info_role_counts.get(ir, 0) + 1

    print(f"\n{'='*60}")
    print(f"  Synthetic Trace Generation Report")
    print(f"{'='*60}")
    print(f"  Total traces:          {n}")
    print(f"  Total messages:        {total_messages}")
    print(f"  Total turns (user):    {total_turns}")
    print(f"  Avg turns/trace:       {total_turns/n:.1f}")
    print(f"  Total planted info:    {total_planted}")
    print(f"  Avg planted/trace:     {total_planted/n:.1f}")
    print(f"  Total tokens (est):    {total_tokens:,}")
    print(f"  Avg tokens/trace:      {total_tokens/n:,.0f}")
    print(f"  Total tool calls:      {total_tool_calls}")
    print(f"  Traces with thinking:  {thinking_count}/{n}")

    print(f"\n  Scenario distribution:")
    for sc, cnt in sorted(scenario_counts.items()):
        print(f"    {sc:30s} {cnt:3d} ({cnt/n*100:.0f}%)")

    print(f"\n  Complexity distribution:")
    for cx, cnt in sorted(complexity_counts.items()):
        print(f"    {cx:30s} {cnt:3d} ({cnt/n*100:.0f}%)")

    print(f"\n  Case type distribution:")
    for ct, cnt in sorted(case_type_counts.items()):
        print(f"    {ct:30s} {cnt:3d} ({cnt/n*100:.0f}%)")

    print(f"\n  Message role distribution:")
    for r, cnt in sorted(role_counts.items()):
        print(f"    {r:15s} {cnt:5d} ({cnt/total_messages*100:.1f}%)")

    print(f"\n  Planted info type distribution:")
    for it, cnt in sorted(info_type_counts.items()):
        print(f"    {it:25s} {cnt:4d} ({cnt/total_planted*100:.1f}%)")

    print(f"\n  Planted info role distribution:")
    for ir, cnt in sorted(info_role_counts.items()):
        print(f"    {ir:15s} {cnt:4d} ({cnt/total_planted*100:.1f}%)")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic multi-turn agent traces")
    parser.add_argument("--num_traces", type=int, default=80, help="Number of traces to generate")
    parser.add_argument("--output", type=str, default="data/synthetic_traces/traces.json", help="Output file path")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    args = parser.parse_args()

    print(f"Generating {args.num_traces} traces with seed={args.seed} ...")
    traces = generate_all_traces(args.num_traces, args.seed)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(traces, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(traces)} traces to {out_path}")
    print_stats(traces)


if __name__ == "__main__":
    main()
