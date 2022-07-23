# this one line of code took me 2 hours lol
# 06/28/2022 - 21:20 (utc+8)

print('\n'.join([f"{p1} vs {p2}".ljust(10)+(f"Player {(1,2)[dict(P='S',R='P',S='R')[p1]==p2]} won!", "Draw!")[p1==p2] for c in (lambda x: __import__('random').choice(x),)*20 for p1, p2 in zip(c('RPS'), c('RPS'))]))
