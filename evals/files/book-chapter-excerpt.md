# Chapter 3: Why your monitoring lies to you

Here's the thing about monitoring: it's not just about collecting metrics. It's about trust. In today's rapidly evolving infrastructure landscape, teams are drowning in dashboards while starving for signal. This chapter explores the intricate interplay between what we measure and what we actually know.

Consider the humble health check. It returns 200 OK. The service is up. Or is it? The endpoint responds, the load balancer is satisfied, the dashboard glows green, and meanwhile the queue consumer has been wedged for forty minutes. The health check didn't lie, exactly. It answered a question nobody should have been asking.

This isn't a tooling problem. It's a thinking problem.

Three failures show up again and again. First, we measure what is easy rather than what matters. Second, we alert on symptoms rather than on the conditions that produce them. Third, we treat a green dashboard as evidence of health rather than as the absence of a specific kind of failure. Each of these is a choice, and each one compounds the others.

I define a **signal** as a measurement that changes what an operator does. If no decision depends on it, it is not a signal; it is decoration. By that definition most dashboards are mostly decoration, which underscores the importance of ruthless pruning.

The rest of this chapter walks through how to find your real signals, how to retire the decoration, and how to design alerts that someone will still respect at 3 a.m. Let's dive in.

Monitoring isn't a product. It's a practice.
