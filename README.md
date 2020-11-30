hello-world
===========

Make it work, make it right, make it fast.
-- Kent Beck

Creativity is intelligence having fun.
-- Albert Einstein

The future is here. It's just not widely distrubited yet.
-- William Gibson

===========

Piping in subprocess:
Instead of hardcoding "|" into a shell Popen (which doesn't work, anyway), set up individual Popens for each command in the chain, and tie them together using the stdout and stdin arguments to the Popen function.
