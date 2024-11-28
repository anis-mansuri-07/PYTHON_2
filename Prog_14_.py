import re
st = """If you need assistance, feel free to contact the following people: 
John at johnsmith123@gmail.com.in.as, Sarah at sarah.jane77@gmail.com, and Michael 
at michael.brown78@gmail.com. For marketing inquiries, reach out to the team 
at marketing-team@gmail.com or sales inquiries at sales.support@gmail.com. 
The technical team can be reached via tech.guru101@gmail.com or support.tech@gmail.com.
For partnerships, email partnerships.dept@gmail.com or collab@startupmail.com. 
Finally, for any urgent matters, you can write directly to urgent@responsemail.com."""

patt = r"\w+@[\w\.]+"

f = re.findall(patt,st)
for i in f:
    print(i)