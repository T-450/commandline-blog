---
title: "Prepping for GH-300: GitHub Copilot Certification"
date: 2026-06-05
author: "Edward"
description: "Full domain breakdown, plan comparison, agent mode deep dive, and study plan for the GH-300 GitHub Copilot Certification exam."
tags: ["Certification", "GitHub Copilot"]
tag: "Certification"
---

<p>I booked GH-300 for June 23. $59 with ESI discount (normally ~$118). Format is multiple choice + scenario-based at Pearson VUE. Passing is 700/1000, 100 minutes, 45-60 questions. Retake policy: 24 hours after first fail.</p>

<h2 class="wp-block-heading">Domain Breakdown</h2>

<p>The exam was significantly revised January 2026. Six domains:</p>

<ol>
<li>Use GitHub Copilot Responsibly (15–20%)</li>
<li>Use GitHub Copilot Features (25–30%) — heaviest domain</li>
<li>Understand Copilot Data & Architecture (10–15%)</li>
<li>Apply Prompt Engineering & Context Crafting (10–15%)</li>
<li>Improve Developer Productivity with Copilot (10–15%)</li>
<li>Configure Privacy, Exclusions & Safeguards (10–15%)</li>
</ol>

<p>Domains 2, 1, and 6 together push past 55% of the exam. That's where the focus goes.</p>

<h2 class="wp-block-heading">Domain 1: Responsible AI</h2>

<p>Microsoft's six AI principles to know by name: Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability.</p>

<p>Key fact: the developer who accepts a Copilot suggestion owns it. Not GitHub, not Microsoft. This comes up in questions about liability and code ownership.</p>

<p>Risks to know: hallucination (non-existent APIs), training data bias (Stack Overflow patterns are over-represented), IP/licensing risk (suggestions matching public code), security vulnerabilities (OWASP Top 10 patterns), non-determinism (same prompt, different output).</p>

<p>Mitigations: code review, SAST/DAST scanning, unit tests, human oversight, AI governance policies.</p>

<h2 class="wp-block-heading">Domain 2: Copilot Plans & Features</h2>

<p>Know the exact plan differences. This comes up a lot.</p>

<ul>
<li><strong>Free:</strong> 2,000 completions/mo, limited chat, no IP indemnity, no agent mode, no CLI</li>
<li><strong>Pro:</strong> Unlimited completions, IP indemnity, agent/plan/edit modes, CLI, NES, premium AI models, 300 premium requests/mo</li>
<li><strong>Business:</strong> Everything in Pro plus org policy management, content exclusions, audit logs. Prompts NOT used for training by default</li>
<li><strong>Enterprise:</strong> Everything in Business plus knowledge bases, PR summaries, custom/fine-tuned models, 1,000 premium requests/user/mo</li>
</ul>

<p>Knowledge bases and PR summaries are Enterprise-only. Content exclusions and audit logs are Business+. Free plan has zero IP indemnity. Common trap.</p>

<p>Chat modes you need to distinguish:</p>

<ul>
<li><strong>Ask mode:</strong> Q&A about code, doesn't create or modify files</li>
<li><strong>Edit mode:</strong> Targeted edits to specified files. Narrower scope than agent mode</li>
<li><strong>Plan mode:</strong> Creates a multi-step plan without executing. Click "Start Implementation" to switch to agent mode</li>
<li><strong>Agent mode:</strong> Autonomous multi-step coding. Runs terminal commands (with approval), edits multiple files, self-heals on errors</li>
</ul>

<p>Slash commands:</p>

<ul>
<li><code>/explain</code> — explain selected code</li>
<li><code>/fix</code> — suggest a fix</li>
<li><code>/tests</code> — generate tests for selected code only</li>
<li><code>/setup-tests</code> — configure entire test environment (runner, config files, initial tests). THIS IS DIFFERENT from /tests. Common exam question</li>
<li><code>/doc</code> — add documentation comments</li>
<li><code>/optimize</code> — suggest performance improvements</li>
<li><code>/clear</code> — reset chat context</li>
<li><code>/new</code> — scaffold a new project or component</li>
</ul>

<p>Chat context variables: <code>@workspace</code>, <code>@vscode</code>, <code>@terminal</code>, <code>#file</code>, <code>#selection</code>, <code>#codebase</code>.</p>

<p>NES (Next Edit Suggestions) proactively scans the open file and predicts the next logical edit based on recent changes. Affected lines highlighted in blue. Enabled separately from inline suggestions. Accept with Tab. Useful during refactoring — extracting a function prompts NES to suggest updating all call sites.</p>

<h3 class="wp-block-heading">Agent Mode Deep Dive</h3>

<ol>
<li>User provides a high-level task description</li>
<li>Copilot reads the codebase — relevant files, dependencies, instruction files, package.json</li>
<li>Copilot creates sub-tasks and executes them: creates/edits files, runs terminal commands</li>
<li>Self-heals: if a command fails or tests break, it diagnoses and fixes the issue</li>
<li>Changes appear in a diff view — user reviews, keeps, or discards each file change</li>
</ol>

<p>Key distinction: IDE agent mode (local) vs Copilot cloud agent (runs in GitHub's ephemeral Actions environment, can open PRs). They are different features. The cloud agent is for delegating issues and getting a PR without any local work. Content exclusion does NOT apply to either.</p>

<p>Sub-agents are specialized child agents spawned for isolated sub-tasks. Each has its own fresh context window — prevents context pollution. They work in parallel and report back to the main agent. Triggered via the runSubAgent tool inside agent mode. Best use: fixing multiple independent issues without bloating the main context.</p>

<p>MCP (Model Context Protocol): open protocol for connecting Copilot Agent Mode to external tools and data sources. GA in VS Code since July 2025. Configured in VS Code settings or .vscode/mcp.json. Key distinction from Agent Skills: MCP front-loads all tool metadata at session start. Agent Skills use progressive disclosure (lazy loaded only when needed).</p>

<h2 class="wp-block-heading">Domain 3: Data & Architecture</h2>

<p>The code suggestion lifecycle:</p>

<ol>
<li>Context gathering (current file above and below cursor via Fill-In-the-Middle, open tabs, selected code, chat history, instruction files)</li>
<li>Prompt construction (system prompt from GitHub + user code context + developer request)</li>
<li>Proxy service filtering (safety/toxicity filter, duplication detector, PII detection, content policy)</li>
<li>LLM inference (next-token prediction)</li>
<li>Post-processing (dedup check, safety scan, formatting, ranking)</li>
<li>Ghost text delivery in IDE or chat response</li>
</ol>

<p>Context sources: current file (both sides of cursor via FIM), open editor tabs, explicitly attached files via <code>#file</code>, selected code (always prioritized), conversation history, instruction files (.github/copilot-instructions.md, .instructions.md, AGENTS.md/CLAUDE.md), comments immediately before cursor, function and variable names.</p>

<p>Code referencing (duplication detector): compares the suggestion plus ~150 characters of surrounding code against an index of public GitHub repositories. When a match is found, it's flagged with a source reference. Configure in Settings > Copilot > Suggestions matching public code. Options: show matching code (default) or block matching suggestions entirely. Admins can set this policy at the org level.</p>

<p>Data handling by plan: Free/Pro prompts MAY be used for training by default (opt-out available in Settings). Business/Enterprise prompts are explicitly NOT used. Important policy change: from April 24, 2026, Free, Pro, and Pro+ interaction data will be used for training UNLESS users opt out. Does not apply to Business or Enterprise.</p>

<p>LLM limitations: bounded context window (CLI auto-compacts at 95% of token limit), training data cutoff, most-seen bias (tutorial patterns over-represented), pattern inference vs calculation, no project awareness without explicit context files, non-determinism, security gaps.</p>

<h2 class="wp-block-heading">Domain 4: Prompt Engineering</h2>

<p>Anatomy of a good prompt: instruction/task + context (attached files, open code) + examples (few-shot) + constraints/format requirements.</p>

<p>Strategies:</p>

<ul>
<li><strong>Zero-shot:</strong> instruction only, no examples. For common well-understood tasks</li>
<li><strong>Few-shot:</strong> 1-3 input/output examples before the main request. Dramatically improves consistency for style-sensitive tasks</li>
<li><strong>Role prompting:</strong> assign a persona ("You are a senior TypeScript developer")</li>
<li><strong>Chain-of-thought:</strong> ask Copilot to reason step-by-step before producing code</li>
<li><strong>Negative instructions:</strong> explicitly state restrictions ("Do not use external libraries. Never use class components")</li>
<li><strong>Iterative refinement:</strong> start basic, add constraints progressively</li>
<li><strong>Plan mode first:</strong> for large multi-file changes — review the plan before executing</li>
</ul>

<p>Prompt files (.prompt.md) under .github/prompts/ are reusable templates invokable as slash commands. Currently PUBLIC PREVIEW. Frontmatter can configure agent/mode, model, and tools.</p>

<p>Instructions files: .github/copilot-instructions.md (project-level), .github/instructions/ (auto-loaded with description: and applyTo: frontmatter). Important: Copilot code review reads only the first 4,000 characters of instruction files and uses the BASE BRANCH version, not the PR branch version.</p>

<p>Best practices: be specific, break complex tasks into iterative steps, use Plan Mode for large changes, reference existing code patterns, specify language/framework/version, use negative instructions, use /clear between task switches, use comments as inline suggestion context, name functions descriptively.</p>

<h2 class="wp-block-heading">Domain 5: Developer Productivity</h2>

<p>Decision guide for scenario questions (which surface is most appropriate):</p>

<ul>
<li>Single function refactoring: Edit Mode</li>
<li>Multi-file feature: Agent Mode</li>
<li>Understanding legacy code: Ask Mode + /explain</li>
<li>Planning before executing: Plan Mode first</li>
<li>Tests for a specific function: /tests</li>
<li>Setting up test infrastructure: /setup-tests</li>
<li>Delegating an issue for a PR without local work: Copilot cloud agent</li>
<li>Terminal-first workflow: Copilot CLI</li>
<li>Sharing curated team context: Copilot Spaces</li>
</ul>

<p>Common use cases tested: code generation, explanation, debugging, refactoring, documentation (/doc), unit tests (/tests), language translation, security analysis, performance optimization (/optimize), modernization, CI/CD (Dockerfiles, Kubernetes manifests, GitHub Actions workflows).</p>

<p>Productivity API: GET /orgs/{org}/copilot/usage. Legacy metrics endpoints retired April 2, 2026.</p>

<h2 class="wp-block-heading">Domain 6: Privacy, Exclusions & Safeguards</h2>

<p>Content exclusions block: inline suggestions in excluded files, using excluded files as context, chat using excluded file content, code review of excluded files.</p>

<p>Content exclusions do NOT block: manual copy-paste of excluded code into a chat prompt, Copilot CLI, cloud agent, or Agent mode in IDEs, file existence, indirect type inference.</p>

<p>Propagation delay: up to 30 minutes. Restart the IDE to apply immediately.</p>

<p>Configure at repo level (Settings > Copilot > Content exclusion) or org level. Glob patterns like **/*.env, src/private/**, secrets.json.</p>

<p>Policy hierarchy: individual settings (when user is NOT managed by an org) < org policy (for Business/Enterprise seats) < enterprise policy (restricts org choices). Org/enterprise policies override individual settings when a user receives a seat from the org.</p>

<p>IP indemnity: available on Pro, Business, and Enterprise. Applies ONLY when the duplication detector was enabled AND the user did not override a flagged match.</p>

<p>Audit logs: Business+ only. Filter by action:copilot. Agentic audit log events include actor_is_agent and agent_session_id fields. Audit logs track events, not raw chat prompts.</p>

<h2 class="wp-block-heading">Study Resources on O'Reilly</h2>

<ul>
<li><strong>GitHub Copilot Certification Study Guide</strong> — Tom Taulli, Sybex, 240pp. Written for this cert. Covers the full exam objective map. Start here.</li>
<li><strong>Learning GitHub Copilot</strong> — Brent Laster, O'Reilly, 326pp. Goes deeper than the exam needs. Good for agent mode deep dive, custom instructions, prompt engineering patterns, Copilot extensions and Vision.</li>
<li><strong>GitHub Copilot Step by Step</strong> — Dr. Gomathi S., Microsoft Press. Hands-on examples, practice exercises, CI/CD integration.</li>
<li><strong>Use GitHub Copilot for Prompt Engineering</strong> — Rizel Scarlett, O'Reilly, 10pp. Quick skim for prompt patterns, context variables, agent vs chat.</li>
</ul>

<p>All accessible via O'Reilly (ACM membership).</p>

<p>Microsoft also offers a free practice assessment at Microsoft Learn and an official learning path "GitHub Copilot Fundamentals" split across two parts (Part 1: 5h12m, 9 modules; Part 2: 3h19m, 6 modules). The exam sandbox lets you preview the question format.</p>

<h2 class="wp-block-heading">Why Bother</h2>

<p>GitHub Copilot is already a daily tool. The cert validates the edges — the security controls, the admin surface, the extensibility model. Things you don't hit in day-to-day coding. Useful on the resume for AI Engineer roles.</p>

<p>No fluff. Just study the material, pass the exam, move on.</p>
