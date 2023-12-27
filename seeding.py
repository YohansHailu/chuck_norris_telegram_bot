from Persistence.DbContext import coding_jokes_repo

coding_jokes = [
    "Why do programmers like dark mode?\n– Because light attracts bugs",
    "What do cats and programmers have in common?\n-When either one is unusually happy and excited, an appropriate question would be, “did you find a bug?”",
    "Scientists and programmers have gotten together to write computer code that will not only warn of future global warming but also take credit for inventing the internet.\n-It’s a new Al-Gore-rithm",
    "A programmer’s wife tells him: “While you’re at the store, get some milk”.\n– He never comes back.",
    "What do the programmers do when they pay respect?\n-They printf",
    "Harry Potter was a programmer\n-He is fluent in Python",
    "A man is smoking a cigarette and blowing smoke rings into the air. His girlfriend becomes irritated with the smoke and says,\n-Can’t you see the warning on the cigarette pack? Smoking is hazardous to your health!” To this, the man replies, “I am a programmer. We don’t worry about warnings; we only worry about errors.",
    "Programming jokes are fun…\n– but only when executed properly.",
    "The two most difficult things in programming…\n– The two most difficult things in programming are memory management, naming things, and off by one errors.",
    "Why was the programmer always running into walls?\n-He couldn’t see sharp.",
    "My girlfriend told me I care more about my programming job than about her.\n-I told her she is the #1 thing I care about.",
    "I know I did okay on today’s programming test…\n…because my teacher gave me a C++.",
    "I used to work as a programmer for autocorrect….\n-Then they fried me for no raisin.",
    "How programmers curse?\n-Oh shift!",
    "What is the most used language in programming?\n-Profanity.",
    "I’ve been programming too much\n-I can barely cout of my eyes",
    "Programmer fired for following bad practice.\n-Refuses to comment.",
    "Teacher: “How would you describe your level of programming?”\n-Students: “Low”\nTeacher: “Ok, fine, you can write programs in assembler then”",
    "Every time there is a new project,\n– we programmers swear to ourselves that we will code it better this time",
    "What programming languages would we use if C didn’t exist?\n-Ans: PASAL, OBOL and BASI",
    "Why did the programmer quit his job?\n-because he didn’t get arrays.",
    "As a computer programmer, I love goose-feather pillows…\n-Because they are down-loaded!",
    "What is the most commonly used computer programming language?\n-Profanity.",
    "As a programmer\n-waking up is the 0th thing I do every morning",
    "Programming in C can be difficult at times…\n-Programming in C can be difficult at times, but you have to admit it builds tcharacter",
    "What do you call a Russian that enjoys programming?\n-Computin.",
    "Why did the C++ programmer do so well at his new job as a packaging and design engineer?\n-Because he was very good at orienting objects.",
    "How can we complete any article for programmers without referring to stack overflow?\n– After all, it is the brain behind every developer.",
    "Here’s a short programming joke: !false\n-It’s funny because it’s true. I hope that makes you laugh a bit.",
    "Why did the programmer leave his job ?\n-Because he couldn’t hack it.",
    "Why do programmers only go outside during the winter?\n-Because it’s code outside.",
    "Don’t anger a programming wizard.\n– They’ll curse you, and every time you remove it, they’ll just recurse.",
    "What you call it when computer programmers make fun of each other?\n-cyber boolean",
    "New programmers should begin with primitive puns\n-before attempting ones with more structure",
    "Attorney at law\n– Saying you’re an attorney at law is like saying you’re a software developer at programming or that you’re a policeman at racism",
    "What do programmers dance to?\n– Algorhythms"
]


for line in coding_jokes:
    obj = {"text":line, "likes":0}
    coding_jokes_repo.add(obj)
    

