---
title: "Introducing Command Line, and the new rules for builders"
date: 2026-06-02
author: "Jay Parikh"
description: "Agentic AI is here, and the traditional software development lifecycle is broken. Get ready for what comes next by shifting your workflows and your mindset."
tags: ["Conversation"]
tag: "Conversation"
image: "https://commandline.microsoft.com/wp-content/uploads/2026/06/introducing-command-line-and-the-new-rules-for-builders-card.png"
---

<p>Welcome to <a href="https://commandline.microsoft.com/" target="_blank" rel="noreferrer noopener"><em>Command Line</em></a>, a new blog where we’ll share what Microsoft builds, how our technical teams operate, and what we learn along the way. <a href="https://build.microsoft.com/" target="_blank" rel="noreferrer noopener">Build 2026</a> felt like the right time to roll this out, as we bring together engineering leaders from around the world to dive deep on building, deploying, and operating scalable AI systems. For those on the ground in San Francisco, you’ll notice that the vibe has shifted along with the locale. And that seems only fitting since the entire SDLC has changed dramatically, too.&nbsp;</p>



<p>To kick things off officially on <em>Command Line</em>, I thought I’d share some of the things we’ve learned about building in the agentic AI era. Things are evolving quickly, and the old rules no longer apply. Manual review processes are breaking under a flood of PRs that our workflows weren’t designed to accommodate. Build time iteration is being met with runtime learning loops as agents improve post-deployment. And the focus is shifting from shipping code to orchestrating systems.&nbsp;</p>


<figure class="pull-quote pull-quote--terminal pull-quote--cursor">
  <blockquote class="pull-quote-body">
    <span class="pull-quote-mark" aria-hidden="true">&gt;</span>
    <span class="pull-quote-text">Things are evolving quickly, and the old rules no longer apply.<span class="pull-quote-cursor" aria-hidden="true"></span></span>
  </blockquote>
  </figure>



<p>This is more than a productivity boost. It’s an entirely different relationship with code, tools, and decision-making. Throw out the old playbook. We need to develop a new set of rules for builders.&nbsp;</p>



<p>Here are 10 things that feel important and true today.&nbsp;Time will tell how durable they prove to be. We’re in a time of seismic disruption, so we all need to constantly challenge our assumptions. &nbsp;</p>



<h2 class="wp-block-heading">1. Build agent-first by default&nbsp;</h2>



<p>As you develop your proficiency with AI tools, you’ll probably find yourself reaching for the <a href="https://github.com/features/copilot/cli" target="_blank" rel="noreferrer noopener">Copilot CLI</a> in GitHub or agent mode in VS Code more often than not. Many senior engineers on our own teams and across the industry no longer write code by hand, and even small tweaks are made via agents when it’s more efficient.&nbsp;</p>



<h2 class="wp-block-heading">2. Context and skills are your most important asset&nbsp;</h2>



<p>When you first start using an agent in your repo, you’ll notice long sessions with higher failure rates. Start by prompting the agent to populate the knowledge base of Markdown files about your repo, verify the output to ensure correctness, and then set up a continuous improvement agent so that knowledge base memory is updated after each agent session. Things start to compound rapidly.&nbsp;</p>



<p>If you’re doing something repeatedly with an agent, wrap it into a reusable skill and share it. Team skills compound the same way code libraries do. If the same agent failure shows up twice, promote the correction into a reusable skill, test, eval, prompt, or workflow with a clear trigger.&nbsp;</p>



<h2 class="wp-block-heading">3. Plans are the real work&nbsp;</h2>



<p>When you invest in a good plan, the agent can often one-shot the implementation. Shift your energy from typing out code to shaping clear, scoped roadmaps. Human judgment lives&nbsp;in the plan. Execution runs on autopilot.&nbsp;</p>



<h2 class="wp-block-heading">4. Prototypes replace detailed PRDs&nbsp;</h2>



<p>Learning by doing should become the default. Experiment with live demos and prototypes to establish ground truth and guide your decisions before you commit to building. Think demos, not memos.&nbsp;</p>



<h2 class="wp-block-heading">5. Taste, not time, is the crucial limited resource&nbsp;</h2>



<p>When building is cheap, the discipline of deciding what’s worth building becomes more critical, not less. Product judgment and prioritization are the highest-leverage skills on the team. Additionally, with near-zero cost to prototype, deciding what to build now includes seeing concrete options upfront.&nbsp;</p>



<h2 class="wp-block-heading">6. Tackle the important but overlooked&nbsp;</h2>



<p>AI-forward velocity reclaims bandwidth for critical, high-value engineering debt and operational tasks that usually get pushed aside. That includes finding and fixing high-value sentry errors, repairing broken telemetry dashboards, running sentiment analysis on dogfooding feedback, and operationalizing more rigor in your data quality.&nbsp;</p>



<h2 class="wp-block-heading">7. Tests are your safety net&nbsp;</h2>



<p>At high velocity, good test coverage is what prevents you from shipping regressions. Invest in test quality the same way you invest in feature velocity.&nbsp;</p>



<h2 class="wp-block-heading">8. Don’t let code review become a bottleneck&nbsp;</h2>



<p>When small teams can ship hundreds of PRs every month, staying close to the codebase requires deliberate effort. Start using and trusting agentic code review tools like CCR, shifting first-pass code reviews to agents, and keeping humans in the loop for architectural oversight.&nbsp;</p>



<h2 class="wp-block-heading">9. Everything’s changing, not just code&nbsp;</h2>



<p>Build pipelines, verification, triage, planning, and team rituals all need to evolve. Longer shipping cycles gave you more time to uncover bugs. Shorter shipping cycles and a higher pace of code turnover decrease that buffer. As AI-assisted PR volume increases, you need automated, fast quality gates to keep up.&nbsp;</p>



<h2 class="wp-block-heading">10. Code is disposable&nbsp;</h2>



<p>Don’t be afraid to throw code away or rewrite it. For well-bounded features, the spec might become the durable artifact. And because code is disposable, you can be brutally honest in review and ditch what doesn’t serve the product. Embrace an egoless culture.&nbsp;</p>


<figure class="pull-quote pull-quote--signal">
  <blockquote class="pull-quote-body">
    <span class="pull-quote-mark" aria-hidden="true">&gt;</span>
    <span class="pull-quote-text">Taste should be the sharpest tool in your arsenal.</span>
  </blockquote>
  </figure>



<h2 class="wp-block-heading">Bonus: Another word on taste&nbsp;</h2>



<p>In the agentic AI era, taste is the ultimate differentiator and should be the sharpest tool in your arsenal. But don’t just set it and forget it. Keep coming back and feeding the flywheel. Human taste can be captured once in curated examples, then enforced continuously across every agent trajectory. The compounding improvement loop means that as you give feedback, the bar keeps rising.&nbsp;</p>



<p>That’s how you get high-quality code without humans writing every line.&nbsp;</p>
