The pager went off at 2:14. Not the polite kind of page, the one where the escalation policy has already given up on two other people. I was the third name on the list, which tells you something about how the week had gone.

The dashboard was green. Every panel. I remember staring at it and thinking that green had stopped meaning anything to me about six months earlier, and that I had never said so out loud.

Here is what had happened, as far as we could reconstruct it the next morning. A consumer process had hung on a lock it was never going to get. The health endpoint lived in a different thread, so it kept answering. The load balancer kept routing. The queue kept filling. Nothing we measured was wrong, because we measured the parts that were fine.

You've probably got a version of this story. Most people who have run anything in production for more than a year do. The details change, the shape doesn't: the system tells you it's healthy, and it's telling the truth about the wrong thing.

I spent the next two weeks pulling panels off that dashboard. Forty-one of them, in the end. Nobody missed a single one.
