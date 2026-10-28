AI ENGINEER INTERNSHIP
FINAL INTEGRATED 12-WEEK TRAINING & PROGRESS TRACKER
Beginner | Balanced track: software engineering + ML/DL + production-oriented AI engineering | Version 1.0 | 20 October 2026
This is a combined program from the uploaded “AI Engineer Plan: 4-Week Study Plan” (USER PLAN) and the earlier 12-week roadmap (ASSISTANT PLAN). It is designed for Word-based weekly execution and mentor sign-off.

## PROGRAM CONTROL SHEET

| Field | Value | Field | Value |
| --- | --- | --- | --- |
| Intern | ________________ | Mentor | ________________ |
| Start date | ________________ | Target completion | ________________ |
| Weekly capacity | 40 hours / 5 days | Total planned | 480 hours |
| Project repository | ________________ | Team / business domain | ________________ |
| Approved LLM provider | ________________ | Monthly API budget | ________________ |

## 1 | Objective, scope and scheduling

Graduation goal: a supervised Junior Applied AI Engineer candidate who can build, evaluate, secure, test and demonstrate an AI product and explain its architecture, trade-offs and limitations.
Schedule: 12 weeks x 5 working days. The uploaded plan uses 28 numbered study days across four 7-day weeks; these become learning modules redistributed over 60 weekdays, not a required 7-day workweek. Reserve one fifth of the intern’s time for testing, documentation and reviews.
Training emphasis: foundations (Python/data/ML/DL); model APIs and prompt/context engineering; RAG and retrieval; agents/workflows/MCP; UX, evaluation/security; deployment/integration and graduation defense. The capstone is incrementally built from Week 6 onward.
Learning modes: 2h structured study, 4h practice, 1h testing/documentation, 1h self-review or mentor help per day. Mentor touchpoints: daily short check-in, midweek technical coaching and Friday demo/scorecard.

## 2 | Learning stages & milestones

| Gate | Timing | Required demonstration | Pass condition |
| --- | --- | --- | --- |
| Foundation | End W4 | Python + data analysis + ML model + FastAPI | Gate score >=70/100; reproducible project |
| AI applications | End W8 | LLM API, structured outputs, prompt evaluation, RAG with citations | Gate score >=75/100; source-grounding/security checks |
| Final graduation | End W12 | Integrated Copilot + tool workflow + tests + deployment | Weighted score >=75/100 and mandatory gates pass |

## 3 | Twelve-week execution plan

## WEEK 01  |  Python, Git and AI Engineering Orientation

Outcome: Build working development habits and distinguish model-based systems from conventional software.

## Learning checklist:

- [ ] Learn — AI Engineer vs ML Engineer vs Data Scientist; when NOT to use AI
- [ ] Learn — Python syntax, data structures, functions, OOP, exceptions, typing
- [ ] Learn — Git branching, pull requests, virtual environments, secrets management
- [ ] Learn — Model-based systems: tokens/context windows, limitations, prototype vs production

## Implementation checklist:

- [ ] Build / practice — Configure isolated Python environment and repository
- [ ] Build / practice — Build student records CLI with CRUD, JSON persistence and validation
- [ ] Build / practice — Write one-page AI Engineer role note and 3 suitable / 1 unsuitable business cases
- [ ] Build / practice — Add at least 8 unit tests and a README

## Evidence and sign-off:

- [ ] Submit: CLI app + role note + Git repo
- [ ] Mentor review: Explain OOP, debug live, show a useful Git PR
- [ ] Acceptance: >=80% foundational quiz, all CRUD paths work
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Python tutorial; GitHub Skills
Source integration: ASSISTANT W1 + USER Module 1 (role/tokens/production distinctions).

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 02  |  Data, SQL, Mathematics and Exploratory Analysis

Outcome: Clean and interpret a real dataset without leakage.

## Learning checklist:

- [ ] Learn — NumPy, Pandas, Matplotlib and exploratory analysis
- [ ] Learn — SQL SELECT/JOIN/GROUP BY; missing values, outliers, train/test separation
- [ ] Learn — Statistics, probability, vectors, matrices and gradient intuition
- [ ] Learn — Data privacy and approved/public/synthetic datasets

## Implementation checklist:

- [ ] Build / practice — Analyze a public tabular dataset
- [ ] Build / practice — Clean missing/outlier records with documented choices
- [ ] Build / practice — Create >=5 charts and >=5 evidence-based observations
- [ ] Build / practice — Run basic SQL queries and save reproducible notebook

## Evidence and sign-off:

- [ ] Submit: Notebook + cleaning report + SQL examples
- [ ] Mentor review: Show preprocessing reasoning and identify possible leakage
- [ ] Acceptance: Notebook executes end-to-end; reproducible insights
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: NumPy Learn; Pandas docs; Google ML Crash Course
Source integration: ASSISTANT W2 retained; prerequisite not covered in USER four-week plan.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 03  |  Classical Machine Learning

Outcome: Train and compare classification models correctly.

## Learning checklist:

- [ ] Learn — Supervised vs unsupervised; regression vs classification
- [ ] Learn — Baseline, logistic regression, trees and random forests
- [ ] Learn — Train/validation/test; cross-validation; overfitting
- [ ] Learn — Precision, recall, F1, MAE/RMSE, confusion matrix

## Implementation checklist:

- [ ] Build / practice — Build churn or equivalent classification use case
- [ ] Build / practice — Train baseline plus 2 candidate models
- [ ] Build / practice — Plot evaluation metrics and analyze false positives/negatives
- [ ] Build / practice — Persist final model and build prediction script

## Evidence and sign-off:

- [ ] Submit: ML pipeline + comparison report + tests
- [ ] Mentor review: Explain metrics, splits and why the selected model wins
- [ ] Acceptance: Reproducible evaluation; no leakage
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Google ML Crash Course; scikit-learn guide
Source integration: ASSISTANT W3 retained; prerequisite not covered in USER plan.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 04  |  ML Pipelines and Production API

Outcome: Expose reproducible ML inference with a tested API.

## Learning checklist:

- [ ] Learn — Feature pipelines, tuning and imbalanced classes
- [ ] Learn — FastAPI, Pydantic validation, OpenAPI and pytest
- [ ] Learn — Model versioning and performance baseline
- [ ] Learn — Secure configuration, exceptions and error paths

## Implementation checklist:

- [ ] Build / practice — Tune model based on validation only
- [ ] Build / practice — Create /predict and /health endpoints
- [ ] Build / practice — Build >=8 API tests including invalid requests
- [ ] Build / practice — Produce baseline-vs-improved results and implementation notes

## Evidence and sign-off:

- [ ] Submit: FastAPI inference service + test report
- [ ] Mentor review: Review architecture, input validation and reproducibility
- [ ] Acceptance: Gate 1 >=70/100 and core endpoints/tests pass
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: FastAPI tutorial; scikit-learn guide
Source integration: ASSISTANT W4 retained; creates API foundation for USER model APIs.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 05  |  Deep Learning, Embeddings and Transformer Essentials

Outcome: Understand neural networks and compare modern NLP against classical approaches.

## Learning checklist:

- [ ] Learn — Tensors, autograd, networks, losses and optimization
- [ ] Learn — Tokenization, embeddings, attention and transformers
- [ ] Learn — Using pretrained NLP models; inference vs fine-tuning
- [ ] Learn — Model limitations, compute cost and evaluation

## Implementation checklist:

- [ ] Build / practice — Run PyTorch fundamentals exercises
- [ ] Build / practice — Create text sentiment classifier with pretrained model
- [ ] Build / practice — Compare to TF-IDF/classical baseline on hold-out data
- [ ] Build / practice — Document practical model selection trade-offs

## Evidence and sign-off:

- [ ] Submit: NLP notebook + metrics comparison
- [ ] Mentor review: Explain embeddings, transformer intuition and transfer learning
- [ ] Acceptance: Unseen set evaluated; transparent limitations
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: PyTorch tutorials; Hugging Face LLM Course
Source integration: ASSISTANT W5 retained; added bridge into USER embeddings/model integration.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 06  |  Model APIs, Prompt & Context Engineering

Outcome: Build robust model-powered features with structured output, streaming and measured prompting.

## Learning checklist:

- [ ] Learn — USER M2: model API roles, parameters, key management, retries, rate limits
- [ ] Learn — USER M2: streaming, chat history, token usage, errors, multimodal awareness
- [ ] Learn — USER M2: JSON Schema, structured outputs, safe read-only tool call
- [ ] Learn — USER M3: zero/few-shot, constraints, prompt/context selection and versioning

## Implementation checklist:

- [ ] Build / practice — Create streaming chat using approved model API
- [ ] Build / practice — Validate extraction output against Pydantic/JSON Schema (Zod optional for TypeScript)
- [ ] Build / practice — Implement one read-only tool and invalid argument tests
- [ ] Build / practice — Compare 2 prompt versions on >=20 cases; track quality, latency, tokens

## Evidence and sign-off:

- [ ] Submit: Streaming model app + structured extraction + prompt evaluation sheet
- [ ] Mentor review: Rebuild core model call, explain prompt failure analysis and tool security
- [ ] Acceptance: >=85% field accuracy on agreed dataset, no committed keys
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Microsoft Generative AI for Beginners; provider SDK docs
Source integration: USER Days 2–7 largely retained; ASSISTANT W6 combined. Zod changed to optional due to Python track.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 07  |  LangChain, Ingestion, Embeddings and pgvector

Outcome: Build retrieval and end-to-end grounded Q&A with source metadata.

## Learning checklist:

- [ ] Learn — USER M4: LangChain components, testability, tracing and direct-API trade-offs
- [ ] Learn — USER M5: PDF loading, cleaning, chunking, overlap, page/section metadata
- [ ] Learn — Embeddings, cosine similarity, Top-K, PostgreSQL and pgvector
- [ ] Learn — Grounded answers with citations and correct refusal

## Implementation checklist:

- [ ] Build / practice — Create ingestion pipeline for >=20 approved documents
- [ ] Build / practice — Create PostgreSQL + pgvector local database and similarity search
- [ ] Build / practice — Expose retrieval + QA API with page/document citations
- [ ] Build / practice — Prepare >=20 labeled RAG queries and collect Recall@5

## Evidence and sign-off:

- [ ] Submit: Document ingestion + pgvector search + RAG service
- [ ] Mentor review: Explain ingestion, evaluate retrieval, inspect citation correctness
- [ ] Acceptance: Recall@5 >=80% on defined benchmark; no fabricated sources
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: LangChain docs; pgvector GitHub; PostgreSQL docs
Source integration: USER Days 8–12 + ASSISTANT W7; USER pgvector selected as primary store instead of optional FAISS/Chroma.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 08  |  RAG Hardening, Evaluation and Security

Outcome: Quantify retrieval quality and prevent unsupported or unauthorized answers.

## Learning checklist:

- [ ] Learn — USER Day 13: tune chunk size, Top-K, thresholds and metadata filtering
- [ ] Learn — USER M9: eval criteria, retrieval/answer/citation/refusal tests
- [ ] Learn — Hybrid search and reranking concepts; context optimization
- [ ] Learn — Prompt injection, document access control and cross-user retrieval testing

## Implementation checklist:

- [ ] Build / practice — Compare >=2 chunking/retrieval configurations
- [ ] Build / practice — Create >=30-versioned test cases (include paraphrase/negative/adversarial cases)
- [ ] Build / practice — Test unauthorized document retrieval and poisoned document instructions
- [ ] Build / practice — Report retrieval, groundedness, citation, refusal, latency and cost

## Evidence and sign-off:

- [ ] Submit: Baseline-vs-improved RAG evaluation + security findings
- [ ] Mentor review: Gate 2 demo: defend evidence, bad cases and trade-offs
- [ ] Acceptance: >=85% grounded-answer pass; zero known critical document leaks
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: LangChain docs; OWASP LLM Top 10; Microsoft GenAI Beginners
Source integration: USER Days 13–14 and 24–26 + ASSISTANT W8 combined; evaluation moved earlier and expanded.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 09  |  LangGraph, Safe Agents, Tool Calling and MCP

Outcome: Implement controlled workflows and demonstrate correct state and approvals.

## Learning checklist:

- [ ] Learn — USER M6: graphs/nodes/edges, routing, checkpoints, persistence/recovery
- [ ] Learn — USER M6: human-in-the-loop interruption, resume/cancel, audit trail
- [ ] Learn — USER M7: agent loop, max steps, tool schema, least privilege/idempotency
- [ ] Learn — USER M7: MCP clients/servers/tools/resources/prompts and trust boundaries

## Implementation checklist:

- [ ] Build / practice — Build LangGraph stateful workflow with checkpoint and interruption test
- [ ] Build / practice — Add read-only document and mock-ticket lookup tools
- [ ] Build / practice — Demonstrate mock sensitive action that only proceeds after explicit approval (no real writes)
- [ ] Build / practice — Build/connect small read-only MCP example if core work meets target

## Evidence and sign-off:

- [ ] Submit: Agent + LangGraph workflow + tool audit + MCP lab evidence
- [ ] Mentor review: Contrast agent vs deterministic workflow; reproduce a failure/resume
- [ ] Acceptance: >=12/15 tests pass; 0 unauthorized tool actions; MCP lab optional for graduation
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Hugging Face Agents Course; LangGraph docs; MCP specification
Source integration: USER Days 15–21 retained but spaced over W9; ASSISTANT W9 combined; MCP optional advanced lab.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 10  |  AI UX, State, Security, Observability and Deployment

Outcome: Prepare a demonstrable AI service with predictable operations and safe user experience.

## Learning checklist:

- [ ] Learn — USER M8: streaming progress, loading/error/partial states, user controls
- [ ] Learn — USER M8: short-term history, history trimming, privacy-aware memory and delete
- [ ] Learn — USER M9: traces, regression, latency, model token/cost monitoring
- [ ] Learn — USER M10: threat modeling, tenant isolation, least privilege, audit logs
- [ ] Learn — ASSISTANT: Docker, CI basics, .NET REST integration and service health

## Implementation checklist:

- [ ] Build / practice — Create friendly chat UI with retry/cancel/error states
- [ ] Build / practice — Add bounded session history and clear-history action
- [ ] Build / practice — Add trace identifiers, token/latency logging and safe redaction
- [ ] Build / practice — Dockerize FastAPI and integrate with simple .NET mock client
- [ ] Build / practice — Run threat tests for prompt injection, invalid tools, unauthorized retrieval

## Evidence and sign-off:

- [ ] Submit: Dockerized service + integration tests + basic observability report
- [ ] Mentor review: Architecture, UX walkthrough, test simulated provider failure
- [ ] Acceptance: Reproducible setup, 0 hardcoded secrets / critical unresolved security defects
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Docker docs; FastAPI; OWASP LLM Top 10
Source integration: USER Days 22–26 + ASSISTANT W10 combined; production-like multi-tenant auth treated as advanced hardening.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 11  |  AI Knowledge & Operations Copilot — Build

Outcome: Integrate the approved features into a single cohesive MVP.

## Learning checklist:

- [ ] Learn — Architecture documentation: context/container/component
- [ ] Learn — Functional integration: RAG, citations, mock ticket lookup and safe workflows
- [ ] Learn — Test planning, configuration, dependency boundaries
- [ ] Learn — Accessibility/basic UX, error handling and testing

## Implementation checklist:

- [ ] Build / practice — Lock backlog into Must-have / Should-have / Stretch
- [ ] Build / practice — Integrate API, pgvector retrieval, UI, approved LLM and controlled tools
- [ ] Build / practice — Define permissions with synthetic users, verify sources and refusals
- [ ] Build / practice — Write integration tests and known-limitations document

## Evidence and sign-off:

- [ ] Submit: Capstone MVP + architectural diagrams + tests
- [ ] Mentor review: Sprint review against acceptance checklist and feature demonstrations
- [ ] Acceptance: All must-have flows work; no blocking defects
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Prior weeks repositories and architectural diagrams
Source integration: USER Day 27 + ASSISTANT W11 merged; scope adjusted to feasible 12-week beginner capstone.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## WEEK 12  |  Stabilization, Deployment and Graduation Defense

Outcome: Demonstrate an evaluated, documented and securely deployed product.

## Learning checklist:

- [ ] Learn — Regression and failure-recovery testing
- [ ] Learn — LLM evaluation analysis, latency/cost and quality trade-offs
- [ ] Learn — Architecture decisions, operational limitations and runbook
- [ ] Learn — Communication: technical demo, handover and defense

## Implementation checklist:

- [ ] Build / practice — Run >=30 versioned eval cases and report results
- [ ] Build / practice — Execute security test matrix (injection, unauthorized document/tool, secret leakage)
- [ ] Build / practice — Clean repository and write README, setup/runbook and screenshots
- [ ] Build / practice — Record short demo; present architecture, known risks and next improvements

## Evidence and sign-off:

- [ ] Submit: Released Copilot + final presentation + demo + evaluation + security report
- [ ] Mentor review: Live defense, ask intern to modify/debug independently, final scoring
- [ ] Acceptance: Overall >=75/100 AND mandatory safety/functional gates pass
- [ ] Commit source code, tests, documentation and evidence links
- [ ] Record actual hours, blocker, review score and corrective actions
Resources: Docker docs; tests and evaluation documentation
Source integration: USER Day 28 + ASSISTANT W12 merged and extended into full graduation gate.

| Owner | Planned hrs | Actual hrs | Status | Mentor score | Sign-off |
| --- | --- | --- | --- | --- | --- |
| Intern / Mentor | 40 | ________ | ☐ Not started ☐ In progress ☐ Done | ____ / 100 | ________ |

## 4 | Capstone scope and acceptance checklist

Project name: AI Knowledge & Operations Copilot. A restricted demo assistant answering questions about approved sample documentation, citing evidence, and looking up records using mock/read-only service tools. Use synthetic or explicitly approved data; do not connect to production healthcare or business systems.

## Must-have functionality

- [ ] Ingest >=20 approved sample PDF/text documents with page/section metadata
- [ ] Store embeddings/chunks in PostgreSQL + pgvector
- [ ] Answer documented questions with traceable source citations
- [ ] Refuse unsupported questions; never invent a citation
- [ ] Expose FastAPI endpoints and working simple chat UI
- [ ] Read-only mock ticket lookup with validated tool arguments
- [ ] Add limited conversation history, error feedback and reset control
- [ ] Containerized documented local launch, test automation and safe configuration

## Must-have safeguards

- [ ] No committed secrets; env/config separation; restricted credentials
- [ ] Isolate documents across synthetic users; test unauthorized lookup
- [ ] Treat retrieved instructions as untrusted data; prompt injection tests
- [ ] Audit tool calls; bounded loop/retry/timeouts; no autonomous real writes
- [ ] Validate user inputs/tool parameters; appropriate errors and logging
- [ ] Keep personal/sensitive content out of logs; synthetic sample content only

## Should-have enhancements

- [ ] Streaming answers/progress and cancellation
- [ ] Comparative retrieval experiments and reranker discussion
- [ ] Checkpoint/recovery LangGraph workflow with approval on a mock action
- [ ] Simple monitoring summary (latency, failures, token spend)
- [ ] Sample .NET calling client and CI workflow

## Stretch goals, not graduation blockers

- [ ] Working MCP read-only connector
- [ ] Multimodal input integration
- [ ] Real multi-user authentication/tenant administration (sandbox only)
- [ ] Complex agent parallelism, long-term memory or advanced observability UI

## Capstone measurable targets

| Metric | Target | How to verify |
| --- | --- | --- |
| Document set | >=20 documents | Ingestion inventory |
| Evaluation cases | >=30 cases | Versioned question/expected evidence records |
| Retrieval | Recall@5 >=80% | Relevant-source annotation |
| Grounded answers | >=85% pass | Mentor rubric on supported answers |
| Agent scenarios | >=12/15 pass | Automated/manual scenario results |
| Security | 0 critical unresolved defects | Threat test log & sign-off |
| Latency | p95 <=10s if model/hardware allows | 20-query local benchmark; report caveats |
| Documentation | Full handover set | Repository check and independent setup |

## 5 | Weekly operating checklist

## Monday

- [ ] Define goals and acceptance criteria
- [ ] Study prerequisites; clarify constraints

## Tuesday

- [ ] Implement guided labs
- [ ] Commit working incremental code

## Wednesday

- [ ] Build independently; raise blockers early
- [ ] Review data/model quality

## Thursday

- [ ] Write tests, document and fix defects
- [ ] Open pull request for mentor review

## Friday

- [ ] Demo working changes and submit evidence
- [ ] Record score, issues, corrective action and sign-off

## 6 | Mentor scorecard and decision rules

| Assessment dimension | Weight | Evidence |
| --- | --- | --- |
| Technical understanding | 15% | Quizzes, explanations, code defense |
| Practical implementation | 25% | Running exercises and feature demonstration |
| Code quality & tests | 20% | Code reviews, reproducibility, tests |
| Graduation capstone | 25% | Functional coverage, evaluation, deployment |
| Ownership & communication | 15% | Progress reporting, learning and handover |

Weekly rating is 0–100 within each dimension; final weighted score = sum(dimension score x weight). Suggested outcome: >=85 strong candidate; 75–84 pass for supervised junior scope; 60–74 improvement required; <60 training objectives not reached. Gate failures on critical security or essential functionality override a numeric pass.

| Weekly review field | To fill |
| --- | --- |
| Week / dates | ________________________ |
| Quiz/knowledge score | _______ / 100 |
| Assignment / demo score | _______ / 100 |
| Code/test quality score | _______ / 100 |
| Autonomy | ☐ Guided ☐ Partial ☐ Independent |
| Acceptance | ☐ Accepted ☐ Rework ☐ Incomplete |
| PR / evidence URL | ________________________ |
| Top 3 improvements | 1. ____________ 2. ____________ 3. ____________ |
| Mentor / intern sign-off | ________________________ |

## 7 | Integrated change log and traceability

Classification: RETAINED = explicitly represented; ADAPTED = moved/simplified due to beginner prerequisites; OPTIONAL = stretch lab, not graduation blocker; NOT ADOPTED = excluded as an obligation, with rationale. Both sources are accounted for below.
7.1 | Your uploaded four-week plan

| Original item | Decision | Where / rationale |
| --- | --- | --- |
| AI Engineer role; demo vs production; tokens and contexts | RETAINED | Week 1 / Week 6 |
| Model APIs, streaming, multimodal overview | RETAINED; multimodal hands-on OPTIONAL | Week 6; multimodal integration stretch |
| Structured outputs, JSON Schema, Zod | ADAPTED | Week 6: Python Pydantic/JSON Schema mandatory; Zod optional for TypeScript |
| Tool calling / safe execution | RETAINED | Weeks 6, 9–10 |
| Prompt and context engineering, versions, eval | RETAINED | Weeks 6 and 8 |
| LangChain composition, tracing, direct API comparison | RETAINED | Week 7 |
| Ingestion, chunking, embeddings, pgvector | RETAINED | Week 7 primary stack |
| RAG grounding, citations, refusal, metadata filtering | RETAINED | Weeks 7–8, capstone |
| LangGraph, state, checkpoints, interruption | RETAINED | Week 9, W10–11 capstone |
| Human approval, auditability, bounded agents | RETAINED | Weeks 9–12 |
| MCP client/server example | OPTIONAL ADVANCED LAB | Week 9; included for exposure but not capstone blocker |
| AI UX, progress, retry, cancel, state/memory | RETAINED; memory scope limited | Week 10; session history only, no unnecessary long-term sensitive memory |
| 30 evaluation cases / tracing / security | RETAINED | Weeks 8, 10, 12; >=30 final cases |
| Multi-user authentication and tenant isolation | ADAPTED | Synthetic user access testing mandatory; complete production identity system not required |
| Business tools + sensitive write approval | ADAPTED | Mock write action with approval only; prohibit real writes |
| Seven-day week / complete in 4 weeks | NOT ADOPTED | Replaced by 5-day, 12-week beginner schedule |
| Full advanced AI copilot in Day 27–28 | NOT ADOPTED as 2-day expectation | Incrementally built Weeks 6–12 to support quality |

7.2 | Previous 12-week assistant roadmap

| Original item | Decision | Where / rationale |
| --- | --- | --- |
| Python, Git and test foundations | RETAINED | W1 |
| SQL, NumPy/Pandas, stats and data prep | RETAINED | W2 |
| Classical ML, baselines and metrics | RETAINED | W3 |
| Feature engineering, model API, FastAPI | RETAINED | W4 |
| Deep Learning, PyTorch and transformers | RETAINED | W5 |
| LLMs/prompting/extraction | RETAINED + EXPANDED | W6 based on user API, streaming, context modules |
| Vector retrieval, citations and RAG | RETAINED + ADAPTED | W7 uses your pgvector as default instead of Chroma/FAISS |
| RAG enhancement and security evaluation | RETAINED + EXPANDED | W8 user filtering/refusal/security tests |
| Agent tools/workflows | RETAINED + EXPANDED | W9 adds LangGraph checkpoint/approval and MCP exposure |
| Docker, CI and .NET integration | RETAINED | W10 |
| Capstone W11–W12 | RETAINED + EXPANDED | Copilot requirements incorporate your functional/security requirements |
| Chroma / FAISS recommended options | NOT ADOPTED as primary | pgvector used to align with user plan; alternatives can be discussed |
| Unrestricted tool writes or production access | NOT ADOPTED | Unsafe and unnecessary for beginner internship |
| Standard weekly 40h and scoring gates | RETAINED | Program control and scorecard |

7.3 | Meaningful new additions (integration decisions)
- [ ] Source labels USER / ASSISTANT provided in every weekly module
- [ ] 60-weekday pacing and 3 monthly review gates
- [ ] Must-have / should-have / stretch scope control for beginner level
- [ ] Quantified evaluation cases, retrieval and security acceptance tests
- [ ] Weekly sign-off, planned-vs-actual hours, PR links and rework tracking
- [ ] Explicit constraints for privacy, synthetic data and no production write access

## 8 | Learning resources

| Area | Resource / URL |
| --- | --- |
| Python | https://docs.python.org/3/tutorial/ |
| Version control | https://skills.github.com/ |
| Data | https://numpy.org/learn/ \| https://pandas.pydata.org/docs/getting_started/ |
| ML | https://developers.google.com/machine-learning/crash-course |
| ML implementation | https://scikit-learn.org/stable/user_guide.html |
| Deep Learning | https://docs.pytorch.org/tutorials/beginner/basics/intro.html |
| Transformers | https://huggingface.co/learn/llm-course/chapter1/1 |
| GenAI application engineering | https://github.com/microsoft/generative-ai-for-beginners |
| LangChain | https://docs.langchain.com/oss/python/langchain/overview |
| LangGraph | https://docs.langchain.com/oss/python/langgraph/overview |
| Agents | https://huggingface.co/learn/agents-course/en/unit1/introduction |
| pgvector | https://github.com/pgvector/pgvector |
| MCP | https://modelcontextprotocol.io/ |
| FastAPI | https://fastapi.tiangolo.com/tutorial/ |
| Docker | https://docs.docker.com/get-started/ |
| AI Security | https://genai.owasp.org/llm-top-10/ |

Resource guidance: only assign the portions needed in a given week. Validate third-party library API details against documentation at implementation time. Avoid unapproved paid course subscriptions or production dataset exposure.

## 9 | Final graduation sign-off form

- [ ] 12 weekly evidence submissions received
- [ ] All three monthly gates assessed
- [ ] At least 30 capstone evaluation cases executed
- [ ] Model and retrieval limitations explained by intern
- [ ] Functional requirements and citation/refusal scenarios passed
- [ ] Threat model and critical security checks approved
- [ ] Independent setup from repository documentation succeeded
- [ ] Live architecture explanation and debugging exercise passed
- [ ] Mentor signed final score; improvement recommendations recorded

| Dimension | Weight | Score / 100 | Weighted result |
| --- | --- | --- | --- |
| Technical understanding | 15% | ______ | ______ |
| Practical implementation | 25% | ______ | ______ |
| Code quality and testing | 20% | ______ | ______ |
| Graduation capstone | 25% | ______ | ______ |
| Ownership and communication | 15% | ______ | ______ |
| TOTAL | 100% |  | ______ / 100 |

Final decision:  ☐ Strong junior candidate  ☐ Pass – supervised junior role  ☐ Extend development plan  ☐ Not passed
Mentor signature: ____________________   Intern signature: ____________________   Date: _______________
